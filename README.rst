GEOMETOR • fundamentals
=======================

**Visit the Online Archive:** https://geometor.github.io/fundamentals/

.. image:: docsrc/topics/f-01/f-01.svg
   :alt: GEOMETOR • fundamentals featured geometric construction
   :target: https://geometor.github.io/fundamentals/
   :align: center

**Fred W. Seelig • Fundamentals of Constructive Geometry (F.1–F.55) • semantic digital archive**

Mission
-------

``geometor/fundamentals`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It preserves, formalizes, and computationally validates the complete geometric corpus of Fred W. Seelig—comprising 55 fundamental constructions across 353 manuscript folios and 59 computational worksheets. By uniting classical Euclidean synthesis, projective and harmonic geometry, and exact SymPy modeling, the archive liberates handwritten mathematical discoveries into addressable semantic units with calibrated vector graphics and rigorous algebraic proofs across the GEOMETOR corpus.

Catalogs in This Archive
------------------------

- `Fundamentals of Constructive Geometry <https://geometor.github.io/fundamentals/topics/>`_ — 55 elementary constructions and axiomatic primers (``F.1``–``F.55``) organized into a 3-track Book Codex (*Synthesis*, *Folios*, *Code*).


Repository Contents
-------------------

- ``docsrc/`` — RST tracks, topic codices, spreadsheets, and guides compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``resources/`` — Archival manuscript scans (353 folios), OpenDocument spreadsheets, and folio registries.
- ``src/geometor/fundamentals/`` — Topic compilation, spreadsheet verification, and Book Codex generation engine.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
