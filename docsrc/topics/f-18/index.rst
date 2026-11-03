:order: 18
:type: topic
:category: Special Triangles & Sacred Proportions
:tags: equilateral, euclid-i-1, incenter, roots-of-unity, vesica

.. _f-18:

=========================
F.18 Equilateral Triangle
=========================

*Coincidence of Centers, h_A = 3r, and Complex Cube-Root Proof of an Incenter-Bisector Equilateral Triangle*

.. enunciation::

   In an equilateral triangle of side a, the incenter, centroid, circumcenter, and orthocenter coincide, with altitude h_A = (sqrt(3)/2)a = 3r and R = 2r; moreover, points A', B', C' placed along the angle bisectors AI, BI, CI of any triangle ABC at distances A'I = (2r/sqrt(3)) sin(alpha/2 + pi/6) form an equilateral triangle.

.. figure:: f-18.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.18 (Equilateral Triangle)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   =====
   c_a = circle(A, B)
   c_b = circle(B, A)
   C, D = intersect(c_a, c_b)
   ABC = polygon(A, B, C)

Mathematical Synthesis
----------------------

The :term:`equilateral triangle` constructed in :cite:`EuclidElements` Proposition I.1 (`G.1`) is the seed of constructive geometry: intersecting congruent circles :g:`( A B )` and :g:`( B A )` produces apex :g:`C` with :term:`altitude <orthocenter>` :math:`h_A = \frac{\sqrt{3}}{2}a = 3r` and :math:`R = 2r`, where :g:`G`, :math:`I`, :math:`O`, and :math:`H` all coincide (:cite:`SeeligNotebooks`).

In Folios 2–3 (`equilateral-2-001`–`002`), Seelig gives an algebraic and complex-number proof that points :math:`A', B', C'` chosen on the interior angle bisectors :math:`AI, BI, CI` of *any* triangle :math:`\triangle ABC` with :math:`A'I = \frac{2r}{\sqrt{3}}\sin(\frac{\alpha}{2} + \frac{\pi}{6})` form an :term:`equilateral triangle` :math:`\triangle A'B'C'` by verifying :math:`m + n\epsilon + p\epsilon^2 = 0` for :math:`\epsilon = e^{i 2\pi/3}`.

Key Algebraic Identities
------------------------

.. math::

   h_A = \frac{\sqrt{3}}{2} a = 3 r, \qquad R = \frac{a}{\sqrt{3}} = 2 r, \qquad K = \frac{\sqrt{3}}{4} a^2

.. math::

   A'I = \frac{2 r}{\sqrt{3}}\sin\left(\frac{\alpha}{2} + \frac{\pi}{6}\right), \qquad P(\epsilon) = m + n\epsilon + p\epsilon^2 = 0 \quad (\epsilon = e^{i 2\pi/3})

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0122–0124``, 3 scanned manuscript pages in ``resources/seelig/18_equilateral-triangle``)
   * - **Euclid's Elements**
     - :ref:`I.1`, :ref:`IV.2`, :ref:`IV.3` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.1`, :ref:`G.2`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(2)`, :ref:`X(3)`, :ref:`X(4)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``General Reference``, ``Polygon Table`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.18" [label="F.18\nEquilateral Triangle", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-18/index.html"];
       "F.21" [label="F.21\nFermat Point", fillcolor="#e0e0e0", color="#777777", URL="../f-21/index.html"];
       "F.18" -> "F.21";
       "F.23" [label="F.23\nGolden Triangles", fillcolor="#e0e0e0", color="#777777", URL="../f-23/index.html"];
       "F.18" -> "F.23";
       "F.24" [label="F.24\nGothic Arch", fillcolor="#e0e0e0", color="#777777", URL="../f-24/index.html"];
       "F.18" -> "F.24";
       "F.45" [label="F.45\nSquares, Subdivided Lattices, and the Japanese Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-45/index.html"];
       "F.18" -> "F.45";
       "F.49" [label="F.49\nVesica Piscis and Acute-Obtuse Probability", fillcolor="#e0e0e0", color="#777777", URL="../f-49/index.html"];
       "F.18" -> "F.49";
   }

**Required for**: :ref:`F.21 Fermat Point <f-21>`, :ref:`F.23 Golden Triangles <f-23>`, :ref:`F.24 Gothic Arch <f-24>`, :ref:`F.45 Squares, Subdivided Lattices, and the Japanese Theorem <f-45>`, :ref:`F.49 Vesica Piscis and Acute-Obtuse Probability <f-49>`

.. toctree::
   :hidden:

   folios
   code
