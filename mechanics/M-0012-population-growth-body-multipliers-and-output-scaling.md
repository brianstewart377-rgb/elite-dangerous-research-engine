# M-0012 - Population Growth, Body Multipliers, and Output Scaling

## Summary

Population is one of the clearest long-run scaling mechanics in colonisation. It grows on a hybrid curve (a fixed-value phase of daily ticks over about 15 days, then a logistic curve), scales commodity output by square root rather than linearly, and depends heavily on both facility class and local body type.

## Status

Extracted

## Confidence

Current working confidence: 82%.

The global shape of the rule is strong, while some body-specific multipliers remain under-sampled.

## Mechanic statement

- Early growth uses fixed values for 14 ticks, then transitions into a logistic curve that approaches its asymptote after about a year.
- The early ticks are daily, usually spread over 15 days (13 full ticks plus partial ticks on C+1 and C+15/16; guide PDF page 77, footnote 27). Frontier's patch wording says "weekly maintenance tick" (`FD-0001`); see `C-0010`. Before v0.3.0 this mechanic said "weekly" because the DOCX extraction lost footnote 27.
- The logistic phase inflects at 100 days for space ports and 120 days for planetary ports (guide PDF pages 78-79, footnotes 28-29).
- Output scales with the square root of facility population.
- Population is attached to individual facilities, not automatically spread across the whole system.
- Body class and facility class both materially change asymptotic population and therefore long-run output.
- Population also appears to affect emissions grade and the effort needed to swing BGS control, though the exact gameplay magnitude remains less settled than the core growth curve.

## Planner behaviour

- Distinguish first-month output from year-scale mature output.
- Prefer body-specific population baselines when comparing similar facilities.
- Treat demolition-based population corrections as unsafe until directly tested.
- Treat emissions-grade and BGS-resistance effects as real but still coarse-grained in the current planner model.

## Evidence basis

- `evidence/claim_register.csv`
- `mechanics/population_rules_register.md`
- `reference_sources/MG-0001-megaguide-v2-3/mega-guide-v2.3.0-pdftotext.txt` (PDF pages 76-80)
- `reference_sources/FD-0001-trailblazers-update-3/README.md`

## Related mechanics

- `M-0008`
- `M-0010`
- `M-0011`

## Related experiments

- `LV-0008`
- `LV-0009`

## Open questions

- What are the missing body multipliers for under-sampled facilities?
- Does demolition reliably remove the population associated with demolished assets?
