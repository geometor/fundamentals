# GEOMETOR: Fundamentals

**Foundational Constructive Geometry Codex & The Fred W. Seelig Archive**

`geometor/fundamentals` preserves and synthesizes the geometrical notebooks (**55 topics**, **353 scanned manuscript folios**) and computational OpenDocument spreadsheets (**59 worksheets** in `Triangles and Circles.ods`, plus `circumcircle-circumcenter.ods` and `triangle-basics-draw.ods`) compiled by **Fred W. Seelig**, unifying them into a **3-Track Book Codex** powered by `geometor.model` and `sympy`.

---

## 1. Architectural Overview

The repository is structured to match `geometor/euclid`, `geometor/elements`, and `geometor/etc`:

### Archival Resources (`resources/`)
* **`resources/seelig/<NN_slug>/`**: Normalized 55 topic folders containing sequential 4-digit folio scans (`0001.jpg`–`0353.jpg`), diplomatic mathematical transcriptions (`0001.rst`–`0353.rst`), and editorial apparatus (`0001.notes.rst`–`0353.notes.rst`) compatible with `publish folio`.
* **`resources/seelig/folio_reviews.json`**: Verification status registry across all 353 folios.
* **`resources/spreadsheets/`**: Fred Seelig's OpenDocument workbooks (`Triangles and Circles.ods`, `00.triangle-basics/circumcircle-circumcenter.ods`, `00.triangle-basics/triangle-basics-draw.ods`) and the extracted `worksheets.json` formula index.
* **`resources/topics.json`**, **`resources/glossary.json`**, **`resources/persons.json`**, **`resources/citations.json`**: Machine-readable catalogs for the 55 topics and scholarly apparatus.

### 3-Track Book Codex (`docsrc/topics/`)
Configured with `:layout: book` and `.. collection::\n :type: topic\n :sort: order`. Each topic (`docsrc/topics/f-01/` through `docsrc/topics/f-55/`) contains:
1. **Track 1 — Synthesis (`index.rst`)**: Formal `.. enunciation::`, interactive Explorer-styled SVG figure (`f-NN.svg`), `.. signature::` block (`given` / `steps`), symbolic SymPy derivations on the canonical $(a, b, c) = (5, 6, 7)$ reference triangle, collapsible OpenDocument spreadsheet tables, Graphviz dependency DAG, and cross-repository links to `geometor/euclid`, `geometor/elements` (`G.<n>`), and `geometor/etc` (`X(n)`).
2. **Track 2 — Folios (`folios.rst`)**: Heading `F.N <Title> — Folios`, displaying Fred Seelig's scanned notebook pages (`<NNNN>.jpg`) alongside `.. folio:: <NNNN>` diplomatic transcriptions and editorial commentary.
3. **Track 3 — Code (`code.rst`)**: Heading `F.N <Title> — Code`, presenting the `.. enunciation::`, rendered SVG diagram, and standalone executable `model.py` script (`.. literalinclude:: model.py`).

---

## 2. Key Modules (`src/geometor/fundamentals/`)

* [`catalog.py`](file:///home/phi/PROJECTS/geometor/fundamentals/src/geometor/fundamentals/catalog.py): Master catalog of all 55 topics (`F.1`–`F.55`), internal dependency DAG, external canon mappings, and diplomatic folio transcriptions.
* [`ingest.py`](file:///home/phi/PROJECTS/geometor/fundamentals/src/geometor/fundamentals/ingest.py): Archival migration and 4-digit folio serializer (`0001`–`0353`).
* [`spreadsheets.py`](file:///home/phi/PROJECTS/geometor/fundamentals/src/geometor/fundamentals/spreadsheets.py): OpenDocument Spreadsheet (`.ods`) XML parser and RST formula table generator.
* [`apparatus.py`](file:///home/phi/PROJECTS/geometor/fundamentals/src/geometor/fundamentals/apparatus.py): Scholarly registries (`GLOSSARY_REGISTRY`, `PERSONS_REGISTRY`, `CITATIONS_REGISTRY`), JSON exporters, RST generators, and `enrich_text()`.
* [`construct.py`](file:///home/phi/PROJECTS/geometor/fundamentals/src/geometor/fundamentals/construct.py): `geometor.model.Model` symbolic construction builder and standalone `model.py` generator.
* [`render.py`](file:///home/phi/PROJECTS/geometor/fundamentals/src/geometor/fundamentals/render.py): Interactive Explorer-styled SVG renderer with pan/zoom/reset/labels/guides toolbar and two-way `.geom-ref[data-ref]` hover highlighting.
* [`transform.py`](file:///home/phi/PROJECTS/geometor/fundamentals/src/geometor/fundamentals/transform.py): 3-Track Book Codex compiler for `docsrc/topics/`.
* [`folio_review.py`](file:///home/phi/PROJECTS/geometor/fundamentals/src/geometor/fundamentals/folio_review.py): CLI inspector (`fundamentals-review`) for the 353 manuscript folios.

---

## 3. Development Commands

```bash
# Ingest archive and compile the 55-topic Book Codex
uv run --offline fundamentals build

# Inspect folio summary or a specific folio
uv run --offline fundamentals status
uv run --offline fundamentals-review --folio 0001

# Run tests
uv run --offline pytest

# Build Sphinx documentation
sphinx-build -b html docsrc docs
```
