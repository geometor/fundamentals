"""Foundational constructive geometry codex and the Fred W. Seelig archive.

Key Components:
---------------
- **Catalog** (:mod:`geometor.fundamentals.catalog`): Master registry of the 55
  foundational geometry topics (`F.1` through `F.55`), dependencies, canon links,
  and diplomatic folio transcriptions.
- **Ingest** (:mod:`geometor.fundamentals.ingest`): Archival pipeline migrating
  Fred W. Seelig's 353 handwritten notebook scans (`0001.jpg`–`0353.jpg`) and
  OpenDocument spreadsheets into `resources/`.
- **Spreadsheets** (:mod:`geometor.fundamentals.spreadsheets`): OpenDocument
  Spreadsheet (`.ods`) parser extracting cell values and OpenFormula expressions
  from `Triangles and Circles.ods` (59 worksheets).
- **Apparatus** (:mod:`geometor.fundamentals.apparatus`): Scholarly registries
  and RST generators for `glossary.json`, `persons.json`, and `citations.json`.
- **Construct** (:mod:`geometor.fundamentals.construct`): Symbolic and Euclidean
  construction engine building `geometor.model.Model` instances and standalone
  `model.py` scripts on the canonical `(a, b, c) = (5, 6, 7)` triangle.
- **Render** (:mod:`geometor.fundamentals.render`): Interactive Explorer-styled
  SVG diagram renderer with pan/zoom/reset/labels/guides controls and two-way
  `.geom-ref[data-ref]` hover highlighting.
- **Transform** (:mod:`geometor.fundamentals.transform`): 3-Track Book Codex
  compiler generating `index.rst` (Synthesis), `folios.rst` (Folios), and
  `code.rst` (Code) across `docsrc/topics/f-01/` through `docsrc/topics/f-55/`.
"""

from __future__ import annotations

from .app import main, run
from .apparatus import export_apparatus_json, generate_apparatus_rst
from .construct import build_topic_model, generate_topic_model_code
from .ingest import ingest_archive
from .render import render_svg
from .spreadsheets import build_spreadsheets_index, parse_ods_file
from .transform import generate_codex

__all__ = [
    "build_spreadsheets_index",
    "build_topic_model",
    "export_apparatus_json",
    "generate_apparatus_rst",
    "generate_codex",
    "generate_topic_model_code",
    "ingest_archive",
    "main",
    "parse_ods_file",
    "render_svg",
    "run",
]
__version__ = "0.1.0"
