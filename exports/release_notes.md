# Release Notes

## CRE Knowledge v0.5.0 (tag `cre-knowledge-v0.5.0`)

How strong links flow on a body with both an orbital and a planetary port, measured in game.

### New

- `EV-0007`: Wregoe ZN-X c28-28 A 5. The Dodec and the Large Planetary Port on the same body are compared from journal strengths. Weak links cancel in their difference. All six economies match the rule exactly.
- `RB-0029` (`Confirmed`):
  - surface facilities link to the planetary port, which passes their links on to the orbital port;
  - orbital facilities link to the orbital port only;
  - the planetary port adds its own strong link per economy (tier value plus the body's modifiers) and sends no weak links.
- `C-0014`: the guide's footnote 20 (links form with both ports) is contradicted by page 59 and by the measurement.

### Changed

- `RB-0017` and `RB-0020`: caveats point to `RB-0029`. `RB-0020` stays `Extracted` because port priority among ports of the same kind is not measured.

## CRE Knowledge v0.4.0 (tag `cre-knowledge-v0.4.0`)

The first rules settled by in-game measurement.

### New

- `EV-0006`: colony port economy strengths measured from game journals (game
  4.4.1.1 to 4.4.2.1, October 2026) and Spansh station data. For a colony
  port, the journal's `StationEconomies` `Proportion` is the economy's
  strength, not a share. Registered as a citable source.
- `RB-0028` (`Confirmed`): the strong-link modifier list also applies to a
  port's own economies. Each inherited economy starts at 1.0 and moves 0.4 per
  applicable condition. A tidally locked planet in a binary pair counts as
  tidally locked to its star.
- `tools/validate_rulebook.py`: in-game evidence records (`EV-`) can be cited.
  The quote must appear in the record. `Confirmed` accepts a first-party source
  or in-game evidence, as the status vocabulary already said. `Likely` still
  needs a first-party source.

### Changed

- `RB-0012` (no stacking): `Disputed` to `Confirmed`. Vasellini Prefecture shows
  Industrial 2.20, below the 2.40 that stacking would give before links.
  Contradiction `C-0011` is settled.
- `RB-0013` (volcanism): `Extracted` to `Confirmed`, with its size. Volcanism adds
  0.4 to the port's own Extraction and nothing else.
- `RB-0016` (weak links 0.05): `Likely` to `Confirmed`.
- `RB-0018`: the tidal-lock-to-star Agriculture decrease includes binary pairs.
  New caveats record the water-world Agriculture evidence (`C-0012`) and one
  older observation consistent with the terraformable boost not working
  (`C-0013`, still `Disputed`).
- `RB-0010` and `RB-0019`: caveats point to the measured values.

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
