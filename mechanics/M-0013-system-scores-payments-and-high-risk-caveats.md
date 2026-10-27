# M-0013 - System Scores, Payments, and High-Risk Caveats

## Summary

By-facility system score values are deterministic enough to plan around, but several high-impact caveats remain live: bugged agricultural ports, suspected routing exploits, pad-size mismatches, and other issues that can make a build mechanically worse than it looks on paper.

## Status

Extracted

## Confidence

Current working confidence: 78%.

The score values themselves are strong; the caveat layer remains patch-sensitive.

## Mechanic statement

- Population does not contribute to system score.
- Weekly architect credits are driven by system score and modified by Happiness: Credits per week = System Score x ~10,000 credits x (1 + Happiness) (guide PDF page 81).
- The ~10,000 credits per point varies week by week by roughly +/- 2% (guide PDF page 81, footnote 31).
- Facilities built mid-week contribute a pro-rated part of their weekly credits (about 5,000 per point for a station built mid-week), and unclaimed weeks accumulate into one game-mail (guide PDF page 81, footnote 30).
- Appendix C provides deterministic score values by facility class.
- The recovered sources also preserve multiple planner-relevant caveats and bugs, including agricultural zero-output cases, settlement pad-size divergence, and suspected nested-port passthrough behavior.
- Routing displays are not a complete causal proof of influence, so visible-arrow-count reasoning is itself a planner-relevant caveat.
- Model-only demolition or replacement decisions remain unsafe when they depend on inferred routed influence rather than live Market Links confirmation.

## Planner behaviour

- Use Appendix C score values for payout estimates instead of hand-wavy heuristics.
- Keep bug-sensitive recommendations explicitly marked as experimental or caveated.
- Elevate demolition, nested-port exploit reliance, and agriculture reliability to high-risk planner warnings.
- Elevate `arrow-count-only` routing interpretations to a planner warning rather than a recommendation basis.

## Evidence basis

- `evidence/claim_register.csv`
- `reference_sources/MG-0001-megaguide-v2-3/mega-guide-v2.3.0-pdftotext.txt` (PDF page 81, footnotes 30-31; Appendix C, PDF page 99)
- `docs/contradiction_register.md`
- `planner/planner_risk_register.md`
- `reference_sources/FW-0001-strong-weak-links/strong-and-weak-links-illustrated-reference.txt`

## Related mechanics

- `M-0009`
- `M-0010`
- `M-0011`
- `M-0012`

## Related experiments

- `LV-0009`
- `LV-0010`

## Open questions

- Which current bugs are variant-specific and which are systemic?
- How much live drift should be tolerated before a caveat is reclassified as a contradiction or a retired issue?
- When should a routing-display warning be upgraded from `caution` to `hard block` for planner output?
