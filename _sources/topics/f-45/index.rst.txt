:order: 45
:type: topic
:category: Polygons, Tessellations & Special Triangles
:tags: squares, polygons, carnot, japanese-theorem, equilateral

.. _f-45:

===========================================================
F.45 Squares, Subdivided Lattices, and the Japanese Theorem
===========================================================

*Inscribed Squares, Cevians Inside a Square, Equilateral Subdivisions, and Carnot's Theorem*

.. enunciation::

   A square inscribed in a circle of radius R has side s = sqrt(2) R; inside a square of side s, intersecting cevians divide the interior in exact rational proportions, and by Carnot's Theorem the sum of inradii in any triangulation of a cyclic polygon is invariant.

.. figure:: f-45.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.45 (Squares, Subdivided Lattices, and the Japanese Theorem)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O : Point
   A : Point
   =====
   c_out = circle(O, A)
   l_oa = line(O, A)
   C = intersection(l_oa, c_out)
   perp = perpendicular(O, l_oa)
   B = intersection(perp, c_out)
   D = intersection(perp, c_out)

Mathematical Synthesis
----------------------

This six-folio compilation (:cite:`SeeligNotebooks`) brings together four geometric studies centered on regular :term:`polygons` and triangulations: Folio 1 pairs the compass construction of a square (:math:`s = \sqrt{2}R`) and an :term:`equilateral triangle` (:math:`s = \sqrt{3}R`) inscribed in a circle of radius :math:`R`; Folios 2–3 solve for the Cartesian intersection :math:`N = (X_N, Y_N)` of two diagonal/edge :term:`cevians <Ceva's theorem>` inside a square of side :math:`s`; Folio 4–5 analyze subdivided :term:`equilateral triangle` lattices of side 6 and side 1; and Folio 6 summarizes :person:`Carnot`'s Theorem (:math:`OM_A + OM_B + OM_C = R + r`) as the foundation of the classic Japanese Sangaku theorem on cyclic polygon triangulations.

Key Algebraic Identities
------------------------

.. math::

   s_{\square} = \sqrt{2}\,R, \qquad s_{\triangle} = \sqrt{3}\,R, \qquad OM_A + OM_B + OM_C = R + r

.. math::

   X_N = \frac{s \cdot u v}{u + v - u v}, \qquad Y_N = \frac{s \cdot u (1 - v)}{u + v - u v}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0287–0292``, 6 scanned manuscript pages in ``resources/seelig/45_squares``)
   * - **Euclid's Elements**
     - :ref:`IV.6`, :ref:`IV.7` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.9`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Polygon Table``, ``General Reference`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.45" [label="F.45\nSquares, Subdivided Lattices, and the Japanese Theorem", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-45/index.html"];
       "F.4" [label="F.4\nCarnot's Theorem", fillcolor="#90ee90", color="#2e8b57", URL="../f-04/index.html"];
       "F.4" -> "F.45";
       "F.18" [label="F.18\nEquilateral Triangle", fillcolor="#90ee90", color="#2e8b57", URL="../f-18/index.html"];
       "F.18" -> "F.45";
       "F.40" [label="F.40\nRegular Polygons and Nested Radicals", fillcolor="#90ee90", color="#2e8b57", URL="../f-40/index.html"];
       "F.40" -> "F.45";
   }

**Prerequisites**: :ref:`F.4 Carnot's Theorem <f-04>`, :ref:`F.18 Equilateral Triangle <f-18>`, :ref:`F.40 Regular Polygons and Nested Radicals <f-40>`

.. toctree::
   :hidden:

   folios
   code
