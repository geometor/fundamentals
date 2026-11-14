:navigation: header
:order: 20
:nav_title: Usage

.. _usage:

Using This Edition
==================

.. rubric:: Reader's Guide to the Interactive Constructive Codex & Symbolic Pipeline

The GEOMETOR edition of the *Fundamentals of Constructive Geometry* unites Fred W. Seelig's 55 notebook topics, 353 archival folios, and 59 computational spreadsheets with interactive reading tracks, theme-adaptive vector figures, and exact symbolic proofs.

Interactive Codex Features
--------------------------

1. Synchronized Reading Tracks
   Each of the 55 topics (:math:`\text{F.1}` through :math:`\text{F.55}`) provides three synchronized parallel tracks accessible from the topic header bar:
   
   * **Synthesis Track:** Formal enunciation, interactive Explorer SVG construction, constructive signature (`given` / `steps`), symbolic SymPy derivations on the canonical :math:`(a, b, c) = (5, 6, 7)` triangle, and Graphviz dependency DAG.
   * **Folios Track:** High-resolution archival manuscript scans (``0001.jpg``–``0353.jpg``) paired with diplomatic mathematical transcriptions and editorial commentary.
   * **Code Track:** Standalone executable Python script (``model.py``) generating the exact ``geometor.model.Model`` and rendering the SVG plate.

2. Primary-Source Folio Milestones
   Marginal page and folio markers (such as ``[f. 0001]``) link directly to high-resolution manuscript scans archived in ``resources/folios/``. Header **Folio** badges open the archival witness directly in a side drawer or new tab.

3. Interactive Diagrams & Deductive Links
   Throughout the text, geometric entities, assertions, and algebraic expressions link to formal definitions:
   
   * Calibrated SVG figures dynamically adapt between light and dark reading themes.
   * Geometric labels (:g:`A`, :g:`B`, :g:`C`, :g:`O`, :g:`H`, :g:`I`) highlight corresponding points and lines on companion diagrams.
   * Internal citations cross-reference classical loci in :cite:`Euclid's Elements <EuclidElements>` and sister repositories.

4. Computational Spreadsheets
   59 OpenDocument computational worksheets (including the master ``Triangles and Circles.ods``) are integrated with direct cell formula inspectors and exact arithmetic verification.

5. Full-Text Search with In-Page Highlighting
   The sidebar search queries the entire corpus of 55 topics, manuscript transcriptions, spreadsheet formulas, and glossaries. Search query parameters automatically append ``?highlight=`` to highlight matched terms directly inside propositions and remarks.

6. Categories, Tags, Document Types & Collection Views
   Browse topics, geometric invariants, and historical figures via the sidebar index. Collection pages support switching between **Cards**, **Banners**, and **List** layout modes.

7. People, Bibliography & Glossary Tooltips
   Hovering over any mathematician (:person:`Euclid of Alexandria <euclid>`, :person:`Plato of Athens <plato>`, :person:`Pythagoras of Samos <pythagoras>`, :person:`phi ARCHITECT <phi>`, :person:`Fred W. Seelig <seelig>`), citation (:cite:`SeeligNotebooks`, :cite:`EuclidElements`), or technical term (:term:`circumcircle`, :term:`nine-point circle`, :term:`barycentric coordinates`, :term:`Conway triangle notation`) displays an instant context card.

----

Command-Line & Python Verification API
--------------------------------------

In addition to web reading, ``geometor.fundamentals`` executes a two-stage pipeline—**Ingest** and **Transform**—to build the 55-topic Book Codex and Fred W. Seelig archive.

Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Ingest Fred Seelig's 55 topics (353 folios) and spreadsheets into resources/
   uv run --offline fundamentals ingest

   # Compile the 55 3-Track Book Codex folders, SVGs, and apparatus into docsrc/
   uv run --offline fundamentals transform

   # Run both ingest and transform in one step
   uv run --offline fundamentals build

   # Display summary table of all 55 topics and 353 folios
   uv run --offline fundamentals status

   # Inspect a specific 4-digit folio transcription and editorial notes
   uv run --offline fundamentals-review --folio 0001

   # Build the Sphinx HTML documentation
   publish build

Running Standalone Construction Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every topic directory (``docsrc/topics/f-NN/``) includes a standalone
``model.py`` script that constructs the ``geometor.model.Model``, computes
symbolic SymPy invariants on the canonical :math:`(a, b, c) = (5, 6, 7)`
triangle, and renders the interactive SVG diagram ``f-NN.svg``:

.. code-block:: bash

   /home/phi/PROJECTS/geometor/.venv/bin/python docsrc/topics/f-06/model.py
