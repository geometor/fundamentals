:navigation: header
:order: 20

=====
Usage
=====

``geometor.fundamentals`` executes a two-stage pipeline—**Ingest** and
**Transform**—to build the 55-topic Book Codex and Fred W. Seelig archive.

Command-Line Interface
----------------------

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
   sphinx-build -b html docsrc docs

Running Standalone Construction Models
--------------------------------------

Every topic directory (``docsrc/topics/f-NN/``) includes a standalone
``model.py`` script that constructs the ``geometor.model.Model``, computes
symbolic SymPy invariants on the canonical :math:`(a, b, c) = (5, 6, 7)`
triangle, and renders the interactive SVG diagram ``f-NN.svg``:

.. code-block:: bash

   uv run --offline python3 docsrc/topics/f-06/model.py
