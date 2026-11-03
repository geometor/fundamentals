.. include:: docsrc/intro.rst

Installation & CLI Usage
------------------------

Within the ``geometor`` ``uv`` workspace:

.. code-block:: bash

   # Ingest Fred Seelig's 55 topics (353 folios) and spreadsheets, and compile the Book Codex
   uv run --offline fundamentals build

   # Display summary table of all 55 topics and 353 folios
   uv run --offline fundamentals status

   # Inspect a specific 4-digit folio transcription
   uv run --offline fundamentals-review --folio 0001

   # Run test suite
   uv run --offline pytest

   # Build HTML documentation
   sphinx-build -b html docsrc docs
