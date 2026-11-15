=========
Changelog
=========

0.1.4
-----
*2026-11-15*

- Ensure canonical GEOMETOR ``logo.png`` and ``favicon.ico`` brand assets are provisioned in ``docsrc/_static/`` and rendered in site headers and browser tabs.

0.1.3
-----
*2026-11-14*

- Standardized top-level ``About`` page (``docsrc/about/index.rst`` promoted to top header ``:order: 10``) with the three-pillar GEOMETOR semantic-extraction mission and archival provenance; retired ``docsrc/mission/`` stubs cleanly into Home and ``About``.

0.1.2
-----
*2026-11-14*

- Standardized Book Title Page, top-level Header Navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author/Translator profiles in ``People``, and English structural terminology.

0.1.1 (2026-11-13)
------------------

- **added**: Enabled 353/353 primary-source ``.jpg`` folio scan links across all 55 foundational geometry topics via ``photon-platform-publish`` v0.4.0 scan resolution and Book Codex header badges.

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
