# EV-0007 - Strong links on a body with both an orbital and a planetary port (Wregoe ZN-X c28-28 A 5)

## Evidence type

Live game data, measured. These are the economy strengths of two colony ports on the same body, read from the game's journal, and compared with the facilities built on that body. This record settles how strong links flow when a body has both an orbital port and a planetary port. The guide calls this "confusing, potentially bugged, and rather clunky" (`RB-0020`). Its page 59 and its footnote 20 disagree on it (`C-0014`).

## Sources

- **The owner's game journals** (game 4.4.2.1), `Docked` events, `StationEconomies` (strengths, see `EV-0006`):
  - Mackenzie Shirilla Driving School (Dodec, orbital, Tier 3): 9 dockings, 2026-10-29 to 2026-10-31, all identical.
  - Soundproof Hidden Basement Dungeon (Large Planetary Port, surface, Tier 3): 7 dockings on 2026-10-29, all identical.
  - The commander name and ID are not recorded here.
- **The system's Raven Colonial layout**, table view, read 2026-10-31 from `https://ravencolonial.com/#sys=Wregoe%20ZN-X%20c28-28`. This gives each site's body, facility type and status, and is used as data only.
- **Spansh** body and station data, fetched 2026-10-31 from `https://spansh.co.uk/api/dump/7780836610810`.
- **Facility tiers and economies** come from the ED-Finder facility catalogue (DaftMav construction sheet, `DM-0001`).

## The body

Wregoe ZN-X c28-28 A 5 is a high metal content world, tidally locked to its star, with Rocky Magma volcanism, 3 geological signals and no biological signals, in a Pristine system.

## Facilities on A 5 (Raven, 2026-10-31)

| Site | Type (catalogue) | Location | Tier | Economy | Status |
|---|---|---|---|---|---|
| Mackenzie Shirilla Driving School | Dodec starport (colony) | orbital | 3 | from the body | Complete |
| Soundproof Hidden Basement Dungeon | Large planetary port (colony) | surface | 3 | from the body | Complete |
| Quick Town | Mining outpost installation | orbital | 1 | Extraction | Complete |
| Apianus Prospect | Security installation | orbital | 2 | Military | Complete |
| Butz Point | Government installation | orbital | 2 | none | Complete |
| Alarcon Drilling Rigs | Extraction settlement, large | surface | 2 | Extraction | Complete |
| Khrushchev Beacon, Corrigan Legacy, Binney Terminal | Refinery hub (each) | surface | 2 | Refinery | Complete |
| Muller Extraction Prospect, Quebec Lima | | | | | Demolish |

## Observed

| Economy | Dodec (orbital) | Planetary port (surface) |
|---|---|---|
| Extraction | 6.95 | 3.75 |
| Refinery | 3.65 | 3.65 |
| Industrial | 3.15 | 1.55 |
| Military | 1.00 | 0.20 |
| High Tech | 0.25 | 0.25 |
| Agriculture | 0.05 | 0.05 |

## Method

Weak links come from supporting facilities on other bodies. They reach both ports on A 5 alike, so the difference between the two ports cancels them. The difference therefore depends only on how A 5's own facilities and ports link.

Strong-link values are from the rulebook:

- tier values 0.4, 0.8 and 1.2 (`RB-0015`);
- plus or minus 0.4 per condition (`RB-0018`, `RB-0019`). On A 5 that means Extraction +0.4 for Pristine and +0.4 for volcanism, Industrial and Refinery +0.4 for Pristine, and none for Military.

## Findings

The difference "Dodec minus planetary port", per economy, is set against the rule below:

| Economy | Observed difference | The rule gives |
|---|---|---|
| Extraction | +3.20 | Quick Town to the Dodec, 0.4 + 0.4 + 0.4 = 1.20, plus the planetary port's own Extraction link to the Dodec, 1.2 + 0.4 + 0.4 = 2.00 |
| Industrial | +1.60 | The planetary port's own Industrial link to the Dodec, 1.2 + 0.4 = 1.60 |
| Military | +0.80 | Apianus Prospect to the Dodec, 0.80 |
| Refinery | 0.00 | The three Refinery Hubs reach both ports alike (each 0.8 + 0.4 = 1.20) |
| High Tech | 0.00 | Weak links only |
| Agriculture | 0.00 | Weak links only |

The difference between the Dodec and the planetary port matched the rule exactly in all six economies.

The rule, as measured:

1. Surface supporting facilities form strong links with the planetary port. The planetary port passes those links on, unchanged, to the orbital port. Refinery is 3.65 at both ports.
2. Orbital supporting facilities form strong links with the orbital port only, and give the planetary port nothing. If they also linked to the planetary port, as the guide's footnote 20 says, the planetary port would show at least 4.60 Extraction (1.8 own + 1.6 Alarcon + 1.2 Quick Town) and 0.80 Military. It shows 3.75 and 0.20.
3. The planetary port also forms a strong link with the orbital port in each of its own economies. The link is worth its tier's value plus the body's modifiers for that economy.

Orbital facilities on a body with both kinds of port linked to the orbital port only, while surface facilities linked to the planetary port, which passed their links on to the orbital port together with its own strong link.

Check against the planetary port's own total. Its own economies are those of a colony port on A 5 (`RB-0028`): Extraction 1.0 + 0.4 + 0.4 = 1.80 and Industrial 1.0 + 0.4 = 1.40. Its strong links are Alarcon Drilling Rigs (Extraction 0.8 + 0.4 + 0.4 = 1.60) and the three Refinery Hubs (3.60). What is left over is a whole number of 0.05 weak links in every economy:

| Economy | Left over | Weak links |
|---|---|---|
| Extraction | 0.35 | 7 |
| Industrial | 0.15 | 3 |
| High Tech | 0.25 | 5 |
| Military | 0.20 | 4 |
| Refinery | 0.05 | 1 |
| Agriculture | 0.05 | 1 |

## Limits

- **One body, one pair of ports.** Both ports are Tier 3 colony ports. How priority works among several ports of the same kind is not tested here (`RB-0020`).
- **The weak-link sources** outside A 5 cannot all be named from Raven's list. For example, Spansh lists a Refinery settlement on A 7 d that the Raven layout does not. The method above does not depend on them.
- **A demolished site would change the result.** Muller Extraction Prospect is marked "Demolish" in Raven. If it still stood, its Extraction link (1.60) would push the planetary port above the observed 3.75 Extraction, so it is taken as demolished.

## Confidence

High that orbital facilities link only to the orbital port, that the planetary port passes on its surface facilities' links, and that it adds its own link per economy. These are exact matches in six economies from the game's own numbers.

## Planning impact

- On a body with both port kinds, the orbital port's economy includes everything built on the surface (passed on) plus the planetary port's own link. The planetary port's economy includes only the surface facilities.
- Orbital installations on such a body do nothing for the planetary port.
