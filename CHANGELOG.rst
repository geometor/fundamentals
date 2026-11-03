=========
Changelog
=========

0.1.0 (2026-11-02)
------------------

- **Archival Migration (`resources/`)**:
  - Migrated all 55 handwritten geometry notebook topics (**353 scanned folios**) by Fred W. Seelig from the legacy Grav `pages/` hierarchy into `resources/seelig/<NN_slug>/` with sequential 4-digit folio identifiers (`0001.jpg`–`0353.jpg`), diplomatic `.rst` transcriptions, `.notes.rst` commentary, and `folio_reviews.json`.
  - Migrated OpenDocument spreadsheets (`Triangles and Circles.ods` with 59 worksheets, `circumcircle-circumcenter.ods`, `triangle-basics-draw.ods`) into `resources/spreadsheets/` and extracted `worksheets.json`.
- **3-Track Book Codex (`docsrc/topics/f-01`–`f-55`)**:
  - Compiled **Track 1 — Synthesis (`index.rst`)** with formal `.. enunciation::`, interactive Explorer-styled SVG diagrams (`f-NN.svg`), `.. signature::` blocks, SymPy derivations on the canonical `(a, b, c) = (5, 6, 7)` triangle, collapsible spreadsheet tables, Graphviz dependency DAGs, and cross-links to `geometor/euclid`, `geometor/elements` (`G.<n>`), and `geometor/etc` (`X(n)`).
  - Compiled **Track 2 — Folios (`folios.rst`)** pairing all 353 manuscript scans with `.. folio::` markers, diplomatic mathematical transcriptions, and editorial notes.
  - Compiled **Track 3 — Code (`code.rst`)** with standalone executable `model.py` scripts using `geometor.model` and `sympy`.
- **Scholarly Apparatus**:
  - Added `resources/glossary.json`, `resources/persons.json`, and `resources/citations.json` and generated `docsrc/glossary.rst`, `docsrc/persons.rst`, and `docsrc/bibliography.rst`.

0.0.1 (2023-11-28)
------------------

- Initial repository scaffold and raw archival import.
