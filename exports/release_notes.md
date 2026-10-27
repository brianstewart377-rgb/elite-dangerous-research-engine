# Release Notes

## CRE Knowledge v0.3.0 (tag `cre-knowledge-v0.3.0`)

The first release with a published rulebook (owner decision `D-0006`).

### New

- `rulebook.json`: 27 rules with stable IDs (`RB-0001` to `RB-0027`), exact
  values, statuses and quoted sources: construction points and T2/T3 port
  escalation, port families, body economies and modifiers (with the no-stacking
  rule), strong and weak link values and modifiers, top-two market protection,
  population growth and the population table, weekly payouts and Appendix C
  system scores. Its SHA-256 is recorded in `export_manifest.json`.
- `population_rules.csv` and `market_rules.csv`: the population and market
  registers, previously missing from the exports.
- Frontier first-party sources `FD-0001` (Trailblazers Update 3), `FD-0002`
  (Vanguards Patch 1) and `FD-0003` (update 4.1.2.101).
- `tools/validate_rulebook.py`, run by the bundle builder before export.

### Corrected

- The Mega Guide is now cited from a PDF-page `pdftotext` extraction that keeps
  the guide's footnotes (`MG-0001`, SHA-256 `359e8fd0...bd3`). The older DOCX
  extraction lost every footnote.
- Population growth ticks: the first growth phase is daily, over about 15 days
  (guide footnote 27), not weekly (`POP-0001`, `M-0012`, contradiction `C-0010`).
- Restored footnote caveats: volcanism also boosts intrinsic values (footnote
  13), rings and geologicals do not boost an intrinsic Extraction body (14), no
  Tier 3 facility creates strong links by itself (18), weekly payout variance and
  mid-week pro-rating (30, 31).
- ID collisions: population rules are now `POP-0001` to `POP-0012` (they shared
  the `PR-` prefix with planner rules); the B2a Agriculture test is now `EV-0005`
  (it duplicated `EV-0004`).
- `planner_rules.csv` regenerated from the current register.

### Recorded disagreements

- `C-0010`: Frontier says weekly maintenance ticks; measured data says daily.
- `C-0011`: Frontier says the overrides "may stack"; the guide says they do not.
- `C-0012`: the guide lists Water World as an Agriculture and High Tech
  strong-link boost; Frontier's list has it for Tourism only. The guide says
  the in-game Codex lists it and experiments confirmed it.
- `C-0013`: Frontier lists a terraformable body as an Agriculture strong-link
  boost; the guide reports it bugged and not working. The rulebook marks that
  condition `Disputed`.

`RB-0012` (stacking) and `RB-0022` (population ticks) are `Disputed`; each
gives the working rule in its statement.

### Limitations

- Most rules are `Extracted` (guide only). The live verification queue in
  `experiments/` has not been run.
- The 4.2.2.0 patch-note change is not incorporated (`RB-0001`).
- The Frontier sources were recorded through a web reader on 2026-10-27; their
  strong-link lists are an itemisation, not a verbatim copy.

## CRE Knowledge v0.2.0-draft (2026-06-29)

A prototype release-oriented export snapshot: canonical mechanics, planner
rules, unknowns, contradictions, observations, claims, evidence traceability
and the knowledge graph. Not a final public knowledge release.
