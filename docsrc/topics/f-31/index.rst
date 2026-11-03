:order: 31
:type: topic
:category: Algebraic & Coordinate Systems
:tags: boolean, logic, collinear, harmonic, spreadsheet

.. _f-31:

================
F.31 Logic Tests
================

*Boolean Distance Inequality Triples and Signed Collinear Division Ratios*

.. enunciation::

   Given collinear points A, B, C, the three Boolean inequality tests T_1 = (\|CA\| < \|AB\|), T_2 = (\|CB\| < \|AB\|), and T_3 = (\|CA\| < \|CB\|) uniquely partition the line AB into Region A (-1 < k < 0), interior segment AB (0 < k < infty), and Region B (-infty < k < -1), determining the sign of k = +/- \|AC\| / \|BC\|.

.. figure:: f-31.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.31 (Logic Tests)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   l = line(A, B)
   s_ab = segment(A, B)
   s_ac = segment(A, C)
   s_bc = segment(B, C)

Mathematical Synthesis
----------------------

When automating :term:`harmonic conjugate` and :term:`Apollonian circles` calculations in C.a.R. and OpenDocument spreadsheets (:cite:`SeeligNotebooks`), Euclidean distance functions return unsigned magnitudes :math:`\|CA\|, \|CB\|, \|AB\|`. In this six-page treatise (*Three Logical Tests — Boolean outputs 1=True / 0=False*, numbered ``1/``–``6/``), Seelig defines three elementary predicates :math:`T_1: \|CA\| < \|AB\|`, :math:`T_2: \|CB\| < \|AB\|`, and :math:`T_3: \|CA\| < \|CB\|`.

Enumerating all :math:`2^3 = 8` truth assignments across Scenarios I–VI, Seelig shows that Region :g:`A` (external on the :g:`A`-side, :math:`-1 < k < 0`) is characterized by :math:`\overline{T}_2 T_3`, the interior of segment :g:`A` :g:`B` (:math:`0 < k < \infty`) by :math:`T_1 T_2`, and Region :g:`B` (external on the :g:`B`-side, :math:`-\infty < k < -1`) by :math:`\overline{T}_1 \overline{T}_3`, compiling nested ``if(...)`` formulas for both C.a.R. (Folio 4) and Excel/Calc (Folios 5–6).

Key Algebraic Identities
------------------------

.. math::

   T_1 = (\|CA\| < \|AB\|), \qquad T_2 = (\|CB\| < \|AB\|), \qquad T_3 = (\|CA\| < \|CB\|)

.. math::

   \text{Region } A:\; \overline{T}_2 T_3\; (-1 < k < 0), \qquad \text{Region } AB:\; T_1 T_2\; (0 < k < \infty), \qquad \text{Region } B:\; \overline{T}_1\overline{T}_3\; (-\infty < k < -1)

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0215–0220``, 6 scanned manuscript pages in ``resources/seelig/31_logic-tests``)
   * - **Euclid's Elements**
     - :ref:`V.8` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.5`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Point in Triangle``, ``Point in Triangle (2)``, ``Harmonic Conjugates`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.31" [label="F.31\nLogic Tests", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-31/index.html"];
       "F.2" [label="F.2\nBilinear Transformations", fillcolor="#90ee90", color="#2e8b57", URL="../f-02/index.html"];
       "F.2" -> "F.31";
       "F.25" [label="F.25\nHarmonic Conjugates", fillcolor="#90ee90", color="#2e8b57", URL="../f-25/index.html"];
       "F.25" -> "F.31";
   }

**Prerequisites**: :ref:`F.2 Bilinear Transformations <f-02>`, :ref:`F.25 Harmonic Conjugates <f-25>`

.. toctree::
   :hidden:

   folios
   code
