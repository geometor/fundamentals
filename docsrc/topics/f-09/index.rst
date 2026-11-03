:order: 9
:type: topic
:category: Circle Geometry & Pencils
:tags: circles, analytic-geometry, sangaku, square, radical-axis

.. _f-09:

====================
F.9 Circle Equations
====================

*Three-Circle Distance Systems in a Square and a Sangaku Tangent Circle Problem*

.. enunciation::

   Pairwise subtraction of Cartesian circle equations (x - u_i)^2 + (y - v_i)^2 = r_i^2 eliminates the quadratic terms x^2 + y^2 to yield linear radical-axis relations, determining both the side Z of a square from three corner distances and the radius of a Sangaku circle tangent to an inscribed square and equilateral triangle.

.. figure:: f-09.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.9 (Circle Equations)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O : Point
   A : Point
   B : Point
   C : Point
   D : Point
   =====
   circle = circle(O, A)
   AB = segment(A, B)
   CD = segment(C, D)
   P = intersect(AB, CD)

Mathematical Synthesis
----------------------

In Topic 09 (:cite:`SeeligNotebooks`), Seelig examines two multi-circle systems in Cartesian coordinates. In Folios 1–4 (`FWS 9/24/2014`), an interior point :math:`P(P, Q)` inside a square :math:`ABCD` of side :math:`Z` has distances :math:`PA = 3, PB = 5, PD = 7`. Subtracting the three circle equations yields :math:`-2ZP + Z^2 = 40`, :math:`-2ZQ + Z^2 = 16`, and :math:`2Z(Q - P) = 24`.

In Folios 5–8 (`Posted Sept. 28, 2014`), Seelig models a **Sangaku problem** posed by Tony Garcia: inside a circle :math:`\Gamma_O(R)` containing a rotated square :math:`ACBD` of side :math:`\sqrt{2}R`, an :term:`equilateral triangle` :math:`\triangle ACE`, and circular arcs :math:`\widehat{AB}` and :math:`\widehat{CD}`, he derives the center :math:`P_y = \frac{r_F^2 - r_I^2}{2(F_y - I_y)}` and radius :math:`r` of the inscribed circle tangent to both the triangle sides and the circular arcs.

Key Algebraic Identities
------------------------

.. math::

   x^2 + y^2 = 9, \quad x^2 + (y - Z)^2 = 25, \quad (x - Z)^2 + y^2 = 49 \implies 2 Z (Q - P) = 24

.. math::

   l_{AE}:\; y = \sqrt{3}x - \frac{\sqrt{2}}{2}R, \qquad P_y = \frac{r_F^2 - r_I^2}{2(F_y - I_y)}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0054–0061``, 8 scanned manuscript pages in ``resources/seelig/09_circle-equations``)
   * - **Euclid's Elements**
     - :ref:`I.47`, :ref:`III.35` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``General Reference``, ``Radical Axes`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.9" [label="F.9\nCircle Equations", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-09/index.html"];
       "F.8" [label="F.8\nChord Intersection", fillcolor="#90ee90", color="#2e8b57", URL="../f-08/index.html"];
       "F.8" -> "F.9";
       "F.10" [label="F.10\nCircles and Geometric Mean", fillcolor="#e0e0e0", color="#777777", URL="../f-10/index.html"];
       "F.9" -> "F.10";
       "F.24" [label="F.24\nGothic Arch", fillcolor="#e0e0e0", color="#777777", URL="../f-24/index.html"];
       "F.9" -> "F.24";
       "F.43" [label="F.43\nRadical Axes and Radical Center", fillcolor="#e0e0e0", color="#777777", URL="../f-43/index.html"];
       "F.9" -> "F.43";
   }

**Prerequisites**: :ref:`F.8 Chord Intersection <f-08>`

**Required for**: :ref:`F.10 Circles and Geometric Mean <f-10>`, :ref:`F.24 Gothic Arch <f-24>`, :ref:`F.43 Radical Axes and Radical Center <f-43>`

.. toctree::
   :hidden:

   folios
   code
