============
fundamentals
============

**Foundational Constructive Geometry Codex & The Fred W. Seelig Archive**

``geometor.fundamentals`` bridges classical Euclidean synthesis, projective and
harmonic geometry, and modern symbolic algebra. It preserves and synthesizes the
complete geometrical notebooks (**55 topics**, **353 manuscript folios**) and
computational spreadsheets (**59 worksheets** in ``Triangles and Circles.ods``)
compiled by :person:`seelig` (:cite:`SeeligNotebooks`, :cite:`SeeligSpreadsheets`).

Architecture of the Codex
-------------------------

Every topic (:ref:`F.1 <f-01>` through :ref:`F.55 <f-55>`) is presented as a
**3-Track Book Codex**:

1. **Track 1 — Synthesis** (``index.rst``): Formal geometric ``.. enunciation::``,
   interactive Explorer-styled SVG construction (``f-NN.svg``) with two-way
   hover highlighting, constructive ``.. signature::`` block, symbolic SymPy
   derivations on the canonical :math:`(a, b, c) = (5, 6, 7)` triangle,
   collapsible OpenDocument Spreadsheet tables, Graphviz dependency DAG, and
   cross-links to ``geometor/euclid``, ``geometor/elements`` (``G.<n>``), and
   ``geometor/etc`` (``X(n)``).
2. **Track 2 — Folios** (``folios.rst``): High-resolution archival scans
   (``0001.jpg``–``0353.jpg``) paired with ``.. folio::`` markers, diplomatic
   mathematical transcriptions, and editorial notes.
3. **Track 3 — Code** (``code.rst``): Standalone executable Python script
   (``model.py``) constructing the exact ``geometor.model.Model`` and verifying
   symbolic invariants.

Thematic Pillars
----------------

.. list-table::
   :widths: 28 18 54
   :header-rows: 1

   * - Pillar
     - Topics
     - Core Themes
   * - **I. Triangle Centers & Classical Lines**
     - :ref:`F.4 <f-04>`, :ref:`F.6 <f-06>`, :ref:`F.11 <f-11>`, :ref:`F.19 <f-19>`, :ref:`F.20 <f-20>`, :ref:`F.21 <f-21>`, :ref:`F.28 <f-28>`, :ref:`F.29 <f-29>`, :ref:`F.34 <f-34>`, :ref:`F.36 <f-36>`, :ref:`F.38 <f-38>`, :ref:`F.46 <f-46>`, :ref:`F.50 <f-50>`
     - :term:`Centroid` :math:`X(2)`, :term:`circumcenter` :math:`X(3)`, :term:`incenter` :math:`X(1)`, :term:`orthocenter` :math:`X(4)`, :term:`nine-point circle` :math:`X(5)`, :term:`Fermat point` :math:`X(13)`, :term:`orthic triangle`, :term:`pedal triangle`, :term:`Carnot's theorem`, and :term:`Stewart's theorem`.
   * - **II. Projective & Harmonic Geometry**
     - :ref:`F.2 <f-02>`, :ref:`F.5 <f-05>`, :ref:`F.7 <f-07>`, :ref:`F.16 <f-16>`, :ref:`F.25 <f-25>`, :ref:`F.26 <f-26>`, :ref:`F.27 <f-27>`, :ref:`F.39 <f-39>`, :ref:`F.48 <f-48>`
     - :term:`Ceva's theorem`, :term:`Menelaus's theorem`, :term:`harmonic conjugate`, :term:`inversion`, :term:`harmonic mean`, :term:`pole and polar` duality, :term:`centers of similitude`, and Monge–:person:`dalembert` collinearity.
   * - **III. Circle Geometry & Pencils**
     - :ref:`F.8 <f-08>`, :ref:`F.9 <f-09>`, :ref:`F.10 <f-10>`, :ref:`F.12 <f-12>`, :ref:`F.13 <f-13>`, :ref:`F.15 <f-15>`, :ref:`F.43 <f-43>`, :ref:`F.51 <f-51>`
     - :term:`Power of a point`, :term:`radical axis`, :term:`coaxial circles`, :term:`orthogonal circles`, :term:`Apollonian circles`, :term:`geometric mean`, and :term:`cyclic quadrilateral` (:person:`ptolemy`'s theorem).
   * - **IV. Algebraic & Coordinate Systems**
     - :ref:`F.3 <f-03>`, :ref:`F.14 <f-14>`, :ref:`F.31 <f-31>`, :ref:`F.33 <f-33>`, :ref:`F.35 <f-35>`, :ref:`F.42 <f-42>`, :ref:`F.44 <f-44>`, :ref:`F.47 <f-47>`, :ref:`F.52 <f-52>`, :ref:`F.53 <f-53>`, :ref:`F.54 <f-54>`, :ref:`F.55 <f-55>`
     - Homogeneous :term:`barycentric coordinates` :math:`(u : v : w)`, :term:`Conway triangle notation` (:math:`S, S_A, S_B, S_C`), biquadratic :term:`Heron's formula`, and :term:`Pythagorean triple` parametrization.
   * - **V. Conics & Analytic Loci**
     - :ref:`F.1 <f-01>`, :ref:`F.17 <f-17>`, :ref:`F.22 <f-22>`, :ref:`F.37 <f-37>`
     - Optical reflection and focal properties of the :term:`parabola` and :term:`ellipse`.
   * - **VI. Special Triangles & Sacred Proportions**
     - :ref:`F.18 <f-18>`, :ref:`F.23 <f-23>`, :ref:`F.24 <f-24>`, :ref:`F.30 <f-30>`, :ref:`F.32 <f-32>`, :ref:`F.40 <f-40>`, :ref:`F.41 <f-41>`, :ref:`F.45 <f-45>`, :ref:`F.49 <f-49>`
     - :term:`Vesica piscis`, :term:`equilateral triangle`, Gothic pointed arches, :term:`golden triangle`, :term:`golden ratio` :math:`\phi`, and :person:`markowski`'s critique.
