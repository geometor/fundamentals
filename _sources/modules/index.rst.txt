:navigation: header
:order: 70

=======
Modules
=======

``geometor.fundamentals`` is structured into modular subpackages for archival
ingestion, OpenDocument spreadsheet parsing, scholarly apparatus management,
symbolic construction, interactive SVG rendering, and Book Codex compilation:

- :mod:`geometor.fundamentals` — Package root and public pipeline exports.
- :mod:`geometor.fundamentals.catalog` — Master catalog of the 55 topics
  (``F.1``–``F.55``), dependency DAG, canon links, and diplomatic folio transcriptions.
- :mod:`geometor.fundamentals.ingest` — Archival migration and 4-digit folio
  generator (``0001``–``0353``) for ``resources/seelig/`` and ``resources/spreadsheets/``.
- :mod:`geometor.fundamentals.spreadsheets` — OpenDocument Spreadsheet (``.ods``)
  parser and formula extractor for ``Triangles and Circles.ods``.
- :mod:`geometor.fundamentals.apparatus` — Glossary, persons, and bibliography
  registries and RST generators.
- :mod:`geometor.fundamentals.construct` — ``geometor.model.Model`` construction
  engine and standalone ``model.py`` code generator.
- :mod:`geometor.fundamentals.render` — Interactive Explorer-styled SVG renderer.
- :mod:`geometor.fundamentals.transform` — 3-Track Book Codex RST compiler.
- :mod:`geometor.fundamentals.folio_review` — CLI inspector for reviewing the
  353 manuscript folios.
