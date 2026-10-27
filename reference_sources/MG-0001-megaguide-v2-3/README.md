# MG-0001 - Elite Dangerous Colonization Mega Guide

Source tier: Tier 2 - community reference

Version: 2.3.0 (title page). Revision table top row: 2.4.0, status "WIP", game
version 4.2.2.0. Last released row: 2.3.0, 31 October 2025, game version 4.2.1.2.
The guide's title page says the 4.2.2.0 patch change (a nerf announced at -70%,
later revised to -25%) is **not incorporated**; treat any figure that patch
touches as possibly out of date.

Author: CMDR Mechan, "with input/additions/comments/suggestions/corrections from
dozens of CMDRs across a large number of communities".

Licence: CC BY-SA 4.0 (<https://creativecommons.org/licenses/by-sa/4.0/>). The
texts in this folder are redistributed under the same licence, with attribution
to CMDR Mechan and the contributing CMDRs. The guide is not endorsed by Frontier
Developments, and neither is this repository. No Elite Dangerous assets or
imagery from the guide are included.

## Files

| File | What it is | SHA-256 |
|---|---|---|
| `mega-guide-v2.3.0-pdftotext.txt` | **Citation text (since CRE Knowledge v0.3.0).** `pdftotext -layout` (poppler 24.02.0) of the 121-page PDF, unmodified. Includes the guide's footnotes. | `359e8fd00d3df3da0f10562f19012c7f71d06cf82933d09bfcf89d1fb296fbd3` |
| `elite-dangerous-colonization-mega-guide-v2-3.txt` | Earlier text extraction from an uploaded DOCX (about 89 MB, not committed). Kept for history; it **lost every footnote**. | `aa80fb9a1314246c24fce85cdfe978f56222a487a01b0dde443b70d739b7dcd3` |

Source PDF (not committed, 95,643,300 bytes, `Elite_Dangerous_Colonization_Mega_Guide-1.pdf`,
supplied by the repository owner on 2026-10-21): SHA-256
`aaabd23cf5ed6161a9b2dadb76a6a7d6b385e4d8c73e87de3bca0339087b69d5`. The same
pdftotext file is committed in the ed-finder repository at
`docs/reference/colonisation/sources/mega-guide-v2.3.0/mega-guide-v2.3.0.txt`
with the same checksum.

## Page numbers and footnotes

Cite pages from `mega-guide-v2.3.0-pdftotext.txt`. Its page numbers are **PDF
page numbers**: each page ends with a form-feed character and (except the title
page) the guide's own footer `Elite Dangerous Colonization Mega Guide ... Page N`.
The guide's table of contents is off by one in places, and claims extracted from
the DOCX text before v0.3.0 (`evidence/claim_register.csv`) may cite a page one
lower than the PDF page; the text quoted is what identifies the passage.

Footnotes appear at the foot of the page that cites them. `pdftotext` writes a
footnote marker directly after the word or number it follows, so a marker can
look like part of a number: on PDF page 27 "Port9" is "Port" with footnote 9,
and on page 28 "2810 (!) Green CPs" is "28" with footnote 10. On page 48
"1.012" is "1.0" with footnote 12. Read numbers next to a footnote with care.

Images are not in the text. Two population formulas (PDF page 78) are images;
the rulebook records only the values the text states.

The guide's typography leaves zero-width spaces (U+200B) in many lines; tools
that match quotes against this file remove them first.
