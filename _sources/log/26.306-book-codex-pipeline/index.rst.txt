:date: 2026-11-02
:type: log
:tags: codex, seelig, model, spreadsheets

=========================================================
3-Track Book Codex & Fred W. Seelig Archive Serialization
=========================================================

Upgraded ``geometor.fundamentals`` to match the architectural, symbolic, and
visual standard of ``geometor/euclid``, ``geometor/elements``, and
``geometor/etc``:

- **Archival Migration**: Migrated all 55 topic folders (**353 scanned
  manuscript pages**) from the legacy Grav ``pages/`` directory into
  ``resources/seelig/<NN_slug>/`` with 4-digit folio identifiers
  (``0001.jpg``–``0353.jpg``), diplomatic ``<NNNN>.rst`` transcriptions,
  ``<NNNN>.notes.rst`` editorial apparatus, and ``folio_reviews.json``.
- **Spreadsheet Extraction**: Migrated ``Triangles and Circles.ods`` (59
  worksheets), ``circumcircle-circumcenter.ods``, and ``triangle-basics-draw.ods``
  into ``resources/spreadsheets/`` and parsed all formulas into
  ``resources/spreadsheets/worksheets.json`` and :ref:`Spreadsheets <spreadsheets>`.
- **3-Track Book Codex**: Compiled :ref:`F.1 <f-01>` through :ref:`F.55 <f-55>`
  in ``docsrc/topics/`` with **Synthesis** (``index.rst``), **Folios**
  (``folios.rst``), and **Code** (``code.rst`` + ``model.py`` + interactive
  ``f-NN.svg``).
- **Scholarly Apparatus**: Added ``resources/glossary.json``,
  ``resources/persons.json``, and ``resources/citations.json`` along with
  ``docsrc/glossary.rst``, ``docsrc/persons.rst``, and ``docsrc/bibliography.rst``.
