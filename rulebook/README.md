# CRE rulebook

`rulebook.json` is the Colonisation Research Engine's published product: a
pinned, machine-readable list of Elite Dangerous colonisation rules, each with a
stable ID, a plain-English statement, exact values where the sources give them,
a status, and quoted sources. Owner decision 2026-10-21 (`D-0006` in
`docs/decision_register.md`): tools such as ed-finder read a tagged release of
this file; the research registers in `mechanics/`, `evidence/` and `docs/` are
the working space behind it.

## How a consumer uses it

1. Take `exports/rulebook.json` from a release tag (`cre-knowledge-vX.Y.Z`).
2. Record its SHA-256 from `exports/export_manifest.json` and refuse the file if
   the checksum differs.
3. Cite rules by ID (`RB-0003`) and the release (`cre-knowledge-v0.3.0`).
4. Read `status` before relying on a rule (see below). `Disputed` rules give the
   working rule in `statement`; the contradiction record (`C-00xx` in
   `docs/contradiction_register.md`) gives both sides.

IDs are permanent. A rule that is replaced keeps its ID with a new statement in
a later release, or is withdrawn and its ID is never reused.

## Status

| Status | Meaning |
|---|---|
| `Confirmed` | A Frontier first-party source states it, or evidence in this repository verified it in game. |
| `Likely` | The community guide states it and a first-party source supports part of it, but not the exact values. |
| `Extracted` | Only the community guide (or another single non-first-party source) states it. Not verified in game. |
| `Disputed` | Sources disagree on the core of the rule. |

`Confirmed` and `Likely` rules always cite a first-party (`FD-`) source.

## Sources and quotes

Every rule cites at least one registered source (`reference_sources/source_register.csv`)
with a short quote. For the Mega Guide (`MG-0001`) the quote is checked against
the cited PDF page of `reference_sources/MG-0001-megaguide-v2-3/mega-guide-v2.3.0-pdftotext.txt`;
for Frontier sources (`FD-*`) against the source's README. Where the extractor
interleaves the columns of a table, a quote is given as ordered fragments.

## Validation

```text
python3 tools/validate_rulebook.py
```

The validator (standard library only) checks the structure, that every quote is
found where it is cited, that related IDs and contradictions exist in the
registers, that the CP escalation sequences match both their formulas and the
printed table, that the body-economy and modifier tables match Frontier's list,
and that every Appendix C score matches the guide's own line.
`tools/build_release_bundle.py` runs it before exporting the file, records the
file's SHA-256 in `exports/export_manifest.json`, and refuses an export that
differs from `rulebook/rulebook.json`.

## Changing a rule

A rule change is a pull request that edits `rulebook/rulebook.json`, cites its
sources, passes the validator, and is approved by the owner. A release bumps
`knowledge_version` (and `KNOWLEDGE_VERSION` in `tools/build_release_bundle.py`),
rebuilds the exports, and is tagged `cre-knowledge-v<version>`.

## Licence of quoted text

Quotes from the Mega Guide are CC BY-SA 4.0 (CMDR Mechan and contributing CMDRs);
see `reference_sources/MG-0001-megaguide-v2-3/README.md`.
