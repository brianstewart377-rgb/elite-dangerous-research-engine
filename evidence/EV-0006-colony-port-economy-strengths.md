# EV-0006 - Colony port economy strengths from journals and Spansh

## Evidence type

Live game data, measured. Colony ports' economy strengths read from the game's
own journal, cross-checked against Spansh station data. This record settles the
stacking question (`C-0011`) and the size of the volcanism bonus (`RB-0013`). It
also shows that the strong-link modifier list applies to a port's own economies.

## Sources

- **The owner's game journals**, 2026-10-11 to 2026-10-31, game versions 4.4.1.1
  to 4.4.2.1. The `Docked` event lists `StationEconomies` with `Name` and
  `Proportion`. The commander name and ID in the files are not recorded here.
- **Spansh station data**, fetched 2026-10-31 from
  `https://spansh.co.uk/api/dump/<system id64>` and
  `https://spansh.co.uk/api/stations/search`. Spansh stores each station's
  economies multiplied by 100 (for example `Agriculture: 155.0`), with the
  station's last update time. Body data (type, tidal lock, volcanism,
  terraforming state, signals, reserve level) comes from the same dumps.
- **The owner's in-game report**, 2026-10-31. Two space farms in Praea Euq
  WV-W b2-2, one at planet 7 and one at planet 8, were demolished, and Lynch's
  Paycut then showed Agriculture 1.10.

## How the game reports strength

For a colony port, `Proportion` in the journal is the economy's strength, not a
share of 1. For example, Mackenzie Shirilla Driving School (Dodec, Wregoe ZN-X
c28-28) reported Extraction 6.95, Refinery 3.65, Industrial 3.15, Military 1.00,
High Tech 0.25 and Agriculture 0.05. Pre-colonisation stations still report
shares that add up to 1 (Jameson Memorial: High Tech 0.67, Industrial 0.33).

Every journal value below matches Spansh's value divided by 100 where both
exist. For example, Uncle Touchy's Puzzle Basement is
`{'Agriculture': 155.0, 'Extraction': 5.0, 'Military': 5.0, 'Tourism': 140.0}`
in Spansh.

## Method

- The host body is the body the port is on (surface ports, which Spansh nests
  under their body) or, for orbital ports, the body whose distance from arrival
  matches the station's.
- A case is used only when no other body within 12 light seconds would give a
  different answer, unless the observed economies themselves rule the other
  body out (stated where that applies).
- The worked sums use the rulebook's own values:
  - 1.0 per inherited economy (`RB-0012`);
  - plus or minus 0.4 per modifier (`RB-0019`), from the condition list in
    `RB-0018`;
  - 0.4, 0.8 or 1.2 per strong link by tier (`RB-0015`);
  - 0.05 per weak link (`RB-0016`).

## Observations

| Port | System | Source and date | Host body | Observed |
|---|---|---|---|---|
| Vasellini Prefecture (Coriolis) | Praea Euq KF-Z c2 (Pristine) | Journal, 5 dockings 2026-10-12 to 2026-10-29 | An icy moon of A 3 (A 3 a, b and c are all icy, tidally locked, Major Water Geysers, 2 geological signals). The gas giant A 3 itself is ruled out because a gas giant would give High Tech. | Industrial 2.20, Extraction 1.80 |
| Macbeth Vision (Dodec) | Praea Euq KF-Z c3 (Pristine) | Journal, 3 dockings 2026-10-20 to 2026-10-27 | B 3, high metal content, no volcanism (2.9 Ls; no other body within 12 Ls) | Extraction 1.40 |
| Rosseland Hub (Outpost) | Praea Euq QJ-B b0 (Pristine) | Spansh, updated 2026-05-18 | A 2, high metal content, no volcanism (0.00 Ls) | Extraction 1.40 |
| Pordenone Vision (Outpost) | Praea Euq IP-A c21 (Pristine) | Spansh, updated 2025-05-16 | 1, high metal content, Metallic Magma volcanism (0.04 Ls) | Extraction 1.80 |
| Cabral Gateway (Coriolis) | HIP 60517 (Pristine) | Spansh, updated 2026-07-14 | A rocky moon of 4. Moons 4 a to 4 f are all rocky and lie within 3 Ls, and each gives the same answer (volcanism does not affect Refinery). The gas giant 4 is ruled out because it would give High Tech and Industrial. | Refinery 1.40 |
| Heyerdahl Beacon | Praea Euq HF-A d75 | Spansh, updated 2025-11-17 | A 5, water world, not tidally locked, Major Silicate Vapour Geysers (0.00 Ls) | Agriculture 1.40, Tourism 1.40 |
| Low Town (Orbis) | Praea Euq IL-Y d56 | Spansh, updated 2026-07-26 | ABC 1, water world, not tidally locked (0.01 Ls) | Agriculture 1.40, Tourism 1.50, Military 0.10, High Tech 0.05 |
| Simak's Progress (Outpost) | Praea Euq IP-A c6 (Pristine) | Spansh, updated 2025-05-16 | 5, terraformable water world, tidally locked to its star, Major Rocky Magma (0.03 Ls) | Agriculture 1.00, Tourism 1.40 |
| Uncle Touchy's Puzzle Basement (Coriolis) | Praea Euq WV-W b2-2 (Pristine) | Journal, 15 dockings 2026-10-12 to 2026-10-29 | Planet 7 or 8: a pair of water worlds orbiting each other, both tidally locked, Major Water Geysers | Agriculture 1.55 until 2026-10-28 21:38 UTC; 1.10 from 2026-10-29 10:20 UTC. Tourism 1.40, Military 0.05, Extraction 0.05 throughout |
| Lynch's Paycut (Ocellus) | Praea Euq WV-W b2-2 | Journal, 8 dockings 2026-10-12 to 2026-10-27; owner report 2026-10-31 | The other planet of the same pair | Agriculture 1.55, then 1.10 after the farms were demolished. Tourism 1.40, Military 0.05, Extraction 0.05 |
| The Cornucopia (Dodec) | Praea Euq WV-W b2-2 | Journal, 2 dockings 2026-10-11 to 2026-10-14 | A water world at 60.7 Ls, not tidally locked | Agriculture 2.35, Tourism 1.40, Military 0.05, Extraction 0.05 |

## Findings

### 1. Body economies and modifiers do not stack (settles `C-0011`)

At Vasellini Prefecture, the icy body and its geologicals both give Industrial.
Not stacking, Industrial starts at 1.0 and the Pristine boost makes it 1.40
before links. Stacking, it would start at 2.0 and be 2.40 before links. Links
only add, so 2.40 cannot become the observed 2.20. Industrial 2.20 at Vasellini
Prefecture is below the 2.40 that stacking would give before any links, so the
body economy and the geologicals did not stack. The 0.80 above 1.40 comes from
links. For example, a Tier 1 Industrial facility on the same body gives a strong
link of 0.4 plus the Pristine boost.

### 2. Volcanism adds 0.4 to Extraction, and only to Extraction (`RB-0013`)

- Rosseland Hub and Pordenone Vision are both outposts on high metal content
  worlds in Pristine systems. Rosseland Hub's world has no volcanism and shows
  Extraction 1.40; Pordenone Vision's world has volcanism and shows Extraction
  1.80.
- At Vasellini Prefecture (current game version), Extraction is
  1.0 + 0.4 (Pristine) + 0.4 (volcanism) = 1.80, as observed.
- Volcanism did not raise the other economies of a volcanic water world:
  Heyerdahl Beacon shows Agriculture 1.40 and Tourism 1.40, and the WV-W b2-2
  ports show Tourism 1.40. Each is 1.0 plus the water-world boost alone.

Volcanism on the host body added exactly 0.4 to the port's own Extraction and
did not change its other economies.

### 3. The modifier list applies to a port's own economies

Each inherited economy starts at 1.0 and moves by 0.4 for each condition in the
strong-link modifier list that holds for the port's body or system:

- Pristine reserves boost Extraction: Macbeth Vision and Rosseland Hub,
  1.0 + 0.4 = 1.40.
- Pristine reserves boost Refinery: Cabral Gateway, 1.0 + 0.4 = 1.40.
- Orbiting a water world boosts Tourism: Heyerdahl Beacon, Low Town (plus two
  0.05 weak links) and all three WV-W b2-2 ports, 1.0 + 0.4 = 1.40.
- Orbiting a water world boosts Agriculture: Heyerdahl Beacon and Low Town,
  1.0 + 0.4 = 1.40.
- Tidal lock to the star decreases Agriculture: Simak's Progress,
  1.0 + 0.4 (water world) - 0.4 (tidal lock) = 1.00.

The port's own economies took the same plus or minus 0.4 modifiers as strong
links, starting from 1.0. This is the guide's own open note ("TO FIX: Modifiers
on planetary intrinsics DO apply", MG-0001 PDF page 2).

### 4. A tidally locked planet in a binary pair counts as tidally locked to its star

Uncle Touchy's Puzzle Basement and Lynch's Paycut orbit the two planets of a
tidally locked binary pair of water worlds. Before the farms were demolished,
both showed Agriculture 1.55. After the owner demolished the space farm at
planet 7 and the space farm at planet 8, both showed Agriculture 1.10, a drop of
0.45.

The only reading that fits:

- each port's own Agriculture is 1.0 + 0.4 (water world) - 0.4 (tidal lock) = 1.00;
- the farm on its own planet gave a strong link of 0.4 + 0.4 - 0.4 = 0.40;
- the farm on the partner planet gave a weak link of 0.05;
- before the demolition, 1.00 + 0.40 + 0.05 + 0.10 = 1.55, where 0.10 is two
  weak links from other Agriculture facilities;
- after it, 1.00 + 0.10 = 1.10.

Without the tidal-lock decrease, the port's own Agriculture would be 1.40, as at
Heyerdahl Beacon and Low Town, and could not fall to 1.10. Both ports dropped by
exactly 0.45 when the two farms were demolished, which fits only if a water world
tidally locked within a binary pair takes the tidal-lock-to-star decrease.

### 5. Weak links are 0.05

All three WV-W b2-2 ports show Military 0.05 and Extraction 0.05. No military or
extraction facility is on their bodies, and the bodies give neither economy. Low
Town shows High Tech 0.05 and Military 0.10. Each weak link added exactly 0.05 to
a port's economy.

### 6. Terraformable Agriculture boost (`C-0013`): one older observation

Simak's Progress orbits a terraformable water world and shows Agriculture 1.00.
That is the value with no terraformable boost; with it, the value would be 1.40.
The Spansh record is from 2025-05-16, so it does not show the current game's
behaviour. The condition stays `Disputed` until a current observation exists.

## Consistent cases not used as proof

These fit the same rules, but their host body or reserve level is not certain
from the data:

- **Very Point and Maylam's Inheritance** (high metal content worlds with
  volcanism; Extraction 1.80, Industrial 1.40). They fit if their systems have
  Pristine or Major reserves and the bodies have geologicals.
- **Coblentz Sanctuary and Hope's Inheritance** (icy bodies with organics;
  Industrial 1.40, Agriculture 1.00, Terraforming 1.00). Agriculture is
  1.0 + 0.4 (organics) - 0.4 (icy body).
- **Jael's Folly** (Extraction 1.40).
- **Donen Depot**, an Asteroid Base showing Extraction 1.40, is left out. Its
  host body is not certain, and specialised ports may follow different rules
  (`RB-0009`).

## Confidence

- **Directness:** High. These are the game's own numbers.
- **Specificity:** High for each named port.
- **Corroboration:** Medium. Each finding rests on one to five ports, and some
  Spansh records are older than the current game version (dates above).
- **Overall:** High that stacking does not occur and that volcanism adds 0.4 to
  Extraction. High that modifiers apply to a port's own economies. Medium-high
  for the binary-pair tidal lock (one system, two ports, one before-and-after
  test).

## Planning impact

- Use 1.0 per inherited economy, plus or minus 0.4 per applicable condition in
  `RB-0018`, for a port's own economies (`RB-0028`).
- Do not add a second 1.0 when two sources give the same economy (`RB-0012`).
- Treat a tidally locked planet in a binary pair as tidally locked to its star
  for the Agriculture decrease.
- Keep the terraformable Agriculture boost switched off.
