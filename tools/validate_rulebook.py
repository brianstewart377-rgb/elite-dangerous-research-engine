#!/usr/bin/env python3
"""Validate the CRE rulebook (rulebook/rulebook.json) against the repository.

Every rule must cite at least one registered source with a short quote, and
every quote must appear in that source's committed text: for the Mega Guide
(MG-0001) on the cited PDF page of the pdftotext extraction, for the Frontier
sources (FD-*) in their reference README, and for in-game evidence records
(EV-*) in the record itself. `Confirmed` needs a first-party (FD-) source or
in-game evidence (EV-); `Likely` needs a first-party source. Related IDs and contradictions must
exist in the registers, and the structured values are checked for internal
consistency (CP escalation sequences against their formulas, Appendix C scores
against the guide's own lines). Standard library only.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RULEBOOK = REPO_ROOT / "rulebook" / "rulebook.json"
SCHEMA_ID = "cre-rulebook/v1"
MG_TEXT = REPO_ROOT / "reference_sources" / "MG-0001-megaguide-v2-3" / "mega-guide-v2.3.0-pdftotext.txt"
MG_TEXT_SHA256 = "359e8fd00d3df3da0f10562f19012c7f71d06cf82933d09bfcf89d1fb296fbd3"
MG_PAGES = 121
STATUSES = {"Confirmed", "Likely", "Extracted", "Disputed"}
TOPICS = {"scope", "construction_points", "economy", "links", "markets", "population", "score"}
ECONOMIES = {
    "Agriculture", "Extraction", "HighTech", "Industrial", "Military", "Refinery", "Tourism",
    "Terraforming", "Contraband",
}
RULE_ID = re.compile(r"RB-\d{4}\Z")
REGISTER_HEADER = re.compile(r"^## ([A-Z]{1,4}-\d{4}) - ", re.M)
RULE_FIELDS = {"id", "topic", "title", "status", "statement", "value", "sources", "related", "contradictions", "caveats"}


class RulebookError(ValueError):
    pass


def normalise(text: str) -> str:
    """Remove zero-width spaces and collapse every whitespace run to one space."""
    return re.sub(r"\s+", " ", text.replace("​", "")).strip()


def mega_guide_pages() -> list[str]:
    raw = MG_TEXT.read_bytes()
    if hashlib.sha256(raw).hexdigest() != MG_TEXT_SHA256:
        raise RulebookError("MG-0001 citation text checksum changed")
    pages = raw.decode("utf-8").split("\f")
    # 121 pages, each ending with a form feed, so the final split piece is empty.
    if len(pages) != MG_PAGES + 1 or normalise(pages[-1]):
        raise RulebookError("MG-0001 citation text does not have 121 form-feed pages")
    return [normalise(page) for page in pages[:MG_PAGES]]


def registered_sources() -> dict[str, dict[str, str]]:
    with open(REPO_ROOT / "reference_sources" / "source_register.csv", encoding="utf-8", newline="") as handle:
        return {row["source_id"]: row for row in csv.DictReader(handle)}


def known_ids() -> set[str]:
    ids: set[str] = set()
    for path in [*(REPO_ROOT / "mechanics").glob("*.md"), *(REPO_ROOT / "docs").glob("*register*.md"),
                 *(REPO_ROOT / "planner").glob("*register*.md")]:
        ids.update(REGISTER_HEADER.findall(path.read_text(encoding="utf-8")))
    ids.update(re.findall(r"\|\s*`(M-\d{4})`\s*\|", (REPO_ROOT / "mechanics" / "index.md").read_text(encoding="utf-8")))
    with open(REPO_ROOT / "evidence" / "claim_register.csv", encoding="utf-8", newline="") as handle:
        ids.update(row["claim_id"] for row in csv.DictReader(handle))
    return ids


def contradiction_ids() -> set[str]:
    return set(REGISTER_HEADER.findall((REPO_ROOT / "docs" / "contradiction_register.md").read_text(encoding="utf-8")))


def quote_found(quote: str | list[str], text: str) -> bool:
    """A quote is one passage, or (for multi-column tables, whose text the
    extractor interleaves) a list of fragments that appear in this order."""
    if isinstance(quote, str):
        return normalise(quote) in text
    position = 0
    for fragment in quote:
        found = text.find(normalise(fragment), position)
        if found < 0:
            return False
        position = found + len(normalise(fragment))
    return True


def check_quote(rule_id: str, citation: dict, sources: dict[str, dict[str, str]], pages: list[str]) -> None:
    source_id = citation.get("source_id")
    quote = citation.get("quote")
    if source_id not in sources:
        raise RulebookError(f"{rule_id}: unregistered source {source_id!r}")
    fragments = [quote] if isinstance(quote, str) else quote
    if (not isinstance(fragments, list) or not fragments
            or not all(isinstance(item, str) and len(normalise(item)) >= 5 for item in fragments)
            or len(normalise(" ".join(fragments))) < 8):
        raise RulebookError(f"{rule_id}: {source_id} citation needs a quote (or ordered fragments) of at least 8 characters")
    if source_id == "MG-0001":
        page = citation.get("page")
        if type(page) is not int or not 1 <= page <= MG_PAGES:
            raise RulebookError(f"{rule_id}: MG-0001 citation needs a PDF page 1-{MG_PAGES}")
        footnote = citation.get("footnote")
        if footnote is not None and (type(footnote) is not int or footnote < 1):
            raise RulebookError(f"{rule_id}: MG-0001 footnote must be a positive integer")
        if not quote_found(quote, pages[page - 1]):
            raise RulebookError(f"{rule_id}: quote not found on MG-0001 PDF page {page}: {quote!r}")
    elif source_id.startswith("FD-"):
        readme = REPO_ROOT / sources[source_id]["repo_path"] / "README.md"
        if not quote_found(quote, normalise(readme.read_text(encoding="utf-8"))):
            raise RulebookError(f"{rule_id}: quote not found in {readme.relative_to(REPO_ROOT)}: {quote!r}")
    elif source_id.startswith("EV-"):
        record = REPO_ROOT / sources[source_id]["repo_path"]
        if record.suffix != ".md" or record.parent != REPO_ROOT / "evidence" or not record.is_file():
            raise RulebookError(f"{rule_id}: {source_id} must point to an evidence/EV-*.md record")
        if not quote_found(quote, normalise(record.read_text(encoding="utf-8"))):
            raise RulebookError(f"{rule_id}: quote not found in {record.relative_to(REPO_ROOT)}: {quote!r}")
    else:
        raise RulebookError(f"{rule_id}: no quote check is defined for {source_id}")


def check_cp_escalation(rule_id: str, value: dict, pages: list[str]) -> None:
    formulas = {"3+(n-2)*2": lambda n: 3 + (n - 2) * 2, "(n-1)*6": lambda n: (n - 1) * 6}
    for tier in ("T2", "T3"):
        entry = value.get(tier)
        if not isinstance(entry, dict):
            raise RulebookError(f"{rule_id}: missing {tier} escalation")
        sequence = entry.get("first_five")
        formula = formulas.get(entry.get("nth_formula"))
        if formula is None or not isinstance(sequence, list) or len(sequence) != 5:
            raise RulebookError(f"{rule_id}: {tier} needs first_five and a known nth_formula")
        if any(formula(n) != sequence[n - 1] for n in range(2, 6)):
            raise RulebookError(f"{rule_id}: {tier} first_five disagrees with {entry['nth_formula']} for n >= 2")
        printed = " ".join(str(item) for item in sequence)
        if printed not in pages[26]:
            raise RulebookError(f"{rule_id}: {tier} first_five '{printed}' is not printed on MG-0001 PDF page 27")
        if entry.get("formula_applies_from") != 2:
            raise RulebookError(f"{rule_id}: {tier} formula applies from the 2nd counted port")


# FD-0001's override list, as recorded in its README, keyed to rulebook keys.
FD_OVERRIDE_LABELS = {
    "Black holes, Neutron Stars, White Dwarves": ("black_hole", "neutron_star", "white_dwarf"),
    "Brown Dwarves and all other star types": ("brown_dwarf", "other_star"),
    "Earth like worlds": ("earth_like_world",),
    "Water world": ("water_world",),
    "Ammonia world": ("ammonia_world",),
    "Gas giant": ("gas_giant",),
    "High metal content and metal rich world": ("high_metal_content_world", "metal_rich_body"),
    "Rocky ice": ("rocky_ice_body",),
    "Rocky": ("rocky_body",),
    "Icy": ("icy_body",),
    "Has rings (includes stars with asteroid belts)": ("rings",),
    "Has organics": ("organics",),
    "Has geologicals": ("geologicals",),
}
FD_OVERRIDE_LINE = re.compile(r'^- "([^"]+)": ((?:"[^"]+"(?:, )?)+)$', re.M)


def fd_overrides(sources: dict[str, dict[str, str]]) -> dict[str, set[str]]:
    readme = (REPO_ROOT / sources["FD-0001"]["repo_path"] / "README.md").read_text(encoding="utf-8")
    result: dict[str, set[str]] = {}
    for label, items in FD_OVERRIDE_LINE.findall(readme):
        if label in FD_OVERRIDE_LABELS:
            economies = {"HighTech" if item.lower() == "hightech" else item for item in re.findall(r'"([^"]+)"', items)}
            for key in FD_OVERRIDE_LABELS[label]:
                result[key] = economies
    if set(result) != {key for keys in FD_OVERRIDE_LABELS.values() for key in keys}:
        raise RulebookError("FD-0001 README override list is incomplete")
    return result


def check_against_fd_overrides(rule_id: str, mapping: dict, overrides: dict[str, set[str]]) -> None:
    for key, economies in mapping.items():
        if key in overrides and set(economies) != overrides[key]:
            raise RulebookError(f"{rule_id}: {key} {sorted(economies)} differs from FD-0001 {sorted(overrides[key])}")


def check_scores(rule_id: str, value: dict, pages: list[str]) -> None:
    scores = value.get("by_facility")
    page = value.get("page")
    if not isinstance(scores, dict) or len(scores) != 54 or type(page) is not int:
        raise RulebookError(f"{rule_id}: expected the 54 Appendix C facility scores with their page")
    for name, score in scores.items():
        if type(score) is not int or score < 1:
            raise RulebookError(f"{rule_id}: invalid score for {name}")
    # The appendix prints every entry as "<facility> : <score>" (names such as
    # "Agriculture Settlement: Small" have no space before their own colon).
    # Parse the whole list and compare complete values, so a score that is a
    # prefix of the printed one ("1" for "15") is refused.
    header = "Appendix C: Detailed By-Facility System Scores"
    text = pages[page - 1]
    start = text.find(header)
    end = text.find("Elite Dangerous Colonization Mega Guide", start + 1)
    if start < 0 or end < 0:
        raise RulebookError(f"{rule_id}: Appendix C list not found on MG-0001 PDF page {page}")
    body = text[start + len(header):end].strip()
    entries = re.findall(r"(\S.*?) : (\d+)(?= |$)", body)
    if " ".join(f"{name} : {score}" for name, score in entries) != body:
        raise RulebookError(f"{rule_id}: could not parse the Appendix C list on MG-0001 PDF page {page}")
    printed = {name: int(score) for name, score in entries}
    if len(printed) != len(entries):
        raise RulebookError(f"{rule_id}: the Appendix C list repeats a facility")
    if printed != scores:
        wrong = sorted(set(printed.items()) ^ set(scores.items()))
        raise RulebookError(f"{rule_id}: scores differ from MG-0001 PDF page {page}: {wrong}")


def supports(status: str, source_ids: list[str]) -> bool:
    """Confirmed needs a first-party source or in-game evidence; Likely a first-party source."""
    if status == "Confirmed":
        return any(source.startswith(("FD-", "EV-")) for source in source_ids)
    if status == "Likely":
        return any(source.startswith("FD-") for source in source_ids)
    return True


def check_economy_lists(rule_id: str, mapping: dict) -> None:
    for key, economies in mapping.items():
        if not isinstance(economies, list) or not economies or not set(economies) <= ECONOMIES:
            raise RulebookError(f"{rule_id}: {key} must list known economies")


def check_strong_link_modifiers(rule_id: str, value: dict, sources: dict[str, dict[str, str]], rule_contradictions: list[str]) -> None:
    for economy, entry in value.items():
        if economy not in ECONOMIES:
            raise RulebookError(f"{rule_id}: unknown economy {economy}")
        for direction in ("boosts", "decreases"):
            for condition in entry.get(direction, []):
                if not re.fullmatch(r"[a-z][a-z0-9_]*", condition.get("condition", "")):
                    raise RulebookError(f"{rule_id}: {economy} {direction} condition needs a snake_case id")
                listed = condition.get("listed_by")
                if not listed or not set(listed) <= set(sources):
                    raise RulebookError(f"{rule_id}: {economy} {condition['condition']} needs registered listed_by sources")
                status = condition.get("status")
                if status not in STATUSES:
                    raise RulebookError(f"{rule_id}: {economy} {condition['condition']} has an invalid status")
                if not supports(status, listed):
                    raise RulebookError(f"{rule_id}: {economy} {condition['condition']} is {status} but no source lists it that can support {status}")
                contradiction = condition.get("contradiction")
                if (status == "Disputed") != (contradiction is not None):
                    raise RulebookError(f"{rule_id}: {economy} {condition['condition']} needs a contradiction exactly when Disputed")
                if contradiction is not None and contradiction not in rule_contradictions:
                    raise RulebookError(f"{rule_id}: {economy} {condition['condition']} cites {contradiction}, which the rule does not list")


def validate(rulebook: dict) -> list[str]:
    if rulebook.get("schema") != SCHEMA_ID:
        raise RulebookError(f"schema must be {SCHEMA_ID}")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(rulebook.get("knowledge_version"))):
        raise RulebookError("knowledge_version must be MAJOR.MINOR.PATCH")
    if rulebook.get("release_tag") != f"cre-knowledge-v{rulebook['knowledge_version']}":
        raise RulebookError("release_tag must be cre-knowledge-v<knowledge_version>")
    if set(rulebook.get("status_vocabulary", {})) != STATUSES:
        raise RulebookError("status_vocabulary must define exactly the four statuses")
    sources = registered_sources()
    for entry in rulebook.get("sources", []):
        if entry.get("id") not in sources:
            raise RulebookError(f"rulebook source {entry.get('id')} is not in the source register")
    pages = mega_guide_pages()
    overrides = fd_overrides(sources)
    known = known_ids()
    contradictions = contradiction_ids()
    seen: set[str] = set()
    messages: list[str] = []
    rules = rulebook.get("rules")
    if not isinstance(rules, list) or not rules:
        raise RulebookError("rules must be a non-empty list")
    for rule in rules:
        rule_id = rule.get("id", "")
        if set(rule) != RULE_FIELDS:
            raise RulebookError(f"{rule_id}: fields must be exactly {sorted(RULE_FIELDS)}")
        if not RULE_ID.fullmatch(rule_id) or rule_id in seen:
            raise RulebookError(f"invalid or duplicate rule id {rule_id!r}")
        seen.add(rule_id)
        if rule["topic"] not in TOPICS or rule["status"] not in STATUSES:
            raise RulebookError(f"{rule_id}: invalid topic or status")
        if not rule["title"].strip() or not rule["statement"].strip():
            raise RulebookError(f"{rule_id}: title and statement are required")
        if not rule["sources"]:
            raise RulebookError(f"{rule_id}: at least one source is required")
        for citation in rule["sources"]:
            check_quote(rule_id, citation, sources, pages)
        if not supports(rule["status"], [c["source_id"] for c in rule["sources"]]):
            raise RulebookError(f"{rule_id}: {rule['status']} needs a first-party (FD-) citation"
                                + (" or in-game evidence (EV-)" if rule["status"] == "Confirmed" else ""))
        unknown = [ref for ref in rule["related"] if ref not in known]
        if unknown:
            raise RulebookError(f"{rule_id}: unknown related ids {unknown}")
        missing = [ref for ref in rule["contradictions"] if ref not in contradictions]
        if missing:
            raise RulebookError(f"{rule_id}: unknown contradictions {missing}")
        if rule["status"] == "Disputed" and not rule["contradictions"]:
            raise RulebookError(f"{rule_id}: Disputed needs a recorded contradiction")
        if not all(isinstance(item, str) and item.strip() for item in rule["caveats"]):
            raise RulebookError(f"{rule_id}: caveats must be non-empty strings")
        value = rule["value"]
        kind = value.get("kind") if isinstance(value, dict) else None
        if kind == "cp_port_escalation":
            check_cp_escalation(rule_id, value, pages)
        elif kind == "system_scores":
            check_scores(rule_id, value, pages)
        elif kind in ("body_base_economies", "local_body_modifiers"):
            check_economy_lists(rule_id, value["economies"])
            check_against_fd_overrides(rule_id, value["economies"], overrides)
        elif kind == "strong_link_modifiers":
            check_strong_link_modifiers(rule_id, value["economies"], sources, rule["contradictions"])
        messages.append(f"ok {rule_id} {rule['status']:<9} {rule['title']}")
    return messages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quiet", action="store_true")
    arguments = parser.parse_args()
    try:
        rulebook = json.loads(RULEBOOK.read_text(encoding="utf-8"))
        messages = validate(rulebook)
    except (RulebookError, OSError, json.JSONDecodeError, KeyError) as exc:
        print(f"rulebook invalid: {exc}", file=sys.stderr)
        return 1
    if not arguments.quiet:
        print("\n".join(messages))
    print(f"OK rulebook {rulebook['knowledge_version']}: {len(messages)} rules")
    return 0


if __name__ == "__main__":
    sys.exit(main())
