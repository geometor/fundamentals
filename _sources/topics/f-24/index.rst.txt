:order: 24
:type: topic
:category: Special Triangles & Sacred Proportions
:tags: gothic, vesica, equilateral, circles, architecture

.. _f-24:

================
F.24 Gothic Arch
================

*Pointed Vesica Arch in a Square and Tangency Equations for the Inscribed Oculus Circle*

.. enunciation::

   In a square ABCD of side s with pointed Gothic arch arcs of radius s centered at A(0, 0) and B(s, 0) meeting at apex E(s/2, (sqrt(3)/2)s), an inscribed tracery circle centered at P(s/2, Q) of radius r = s - p satisfies p*s = P_x H_x + P_y H_y at its tangency point H.

.. figure:: f-24.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.24 (Gothic Arch)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   =====
   ( A B ) = circle(A, B)
   ( B A ) = circle(B, A)
   C, D = intersect(( A B ), ( B A ))
   M = midpoint(A, B)

Mathematical Synthesis
----------------------

Rooted in the :term:`vesica piscis` of :cite:`EuclidElements` I.1 (:ref:`F.18 <f-18>`), the pointed **Gothic arch** in Topic 24 (:cite:`SeeligNotebooks`) is bounded by two circular arcs :g:`( A B )` and :g:`( B A )` of radius :math:`s` inside a square :math:`ABCD` of side :math:`s`, together with diagonal radials :math:`l_{CF}: y = \sqrt{3}x + s(1-\sqrt{3})` and :math:`l_{DF}: y = -\sqrt{3}x + s`.

Seelig sets up the system of three circle equations for an oculus circle of radius :math:`r` centered on the symmetry axis at :math:`P(s/2, Q)`, proves the tangency dot-product identity :math:`p s = P_x H_x + P_y H_y` (where :math:`p = |AP| = s - r`), and uses the semicircle :term:`geometric mean` to show :math:`g^2 = |AG|^2 = 2 s G_x`.

Key Algebraic Identities
------------------------

.. math::

   r^2 = \left(x - \frac{s}{2}\right)^2 + (y - Q)^2, \qquad p s = P_x H_x + P_y H_y \quad (r = s - p), \qquad g^2 = G_x^2 + G_y^2 = 2 s G_x

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0135–0139``, 5 scanned manuscript pages in ``resources/seelig/24_gothic``)
   * - **Euclid's Elements**
     - :ref:`I.1`, :ref:`III.11`, :ref:`III.12` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.1`, :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``General Reference`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.24" [label="F.24\nGothic Arch", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-24/index.html"];
       "F.9" [label="F.9\nCircle Equations", fillcolor="#90ee90", color="#2e8b57", URL="../f-09/index.html"];
       "F.9" -> "F.24";
       "F.10" [label="F.10\nCircles and Geometric Mean", fillcolor="#90ee90", color="#2e8b57", URL="../f-10/index.html"];
       "F.10" -> "F.24";
       "F.18" [label="F.18\nEquilateral Triangle", fillcolor="#90ee90", color="#2e8b57", URL="../f-18/index.html"];
       "F.18" -> "F.24";
   }

**Prerequisites**: :ref:`F.9 Circle Equations <f-09>`, :ref:`F.10 Circles and Geometric Mean <f-10>`, :ref:`F.18 Equilateral Triangle <f-18>`

.. toctree::
   :hidden:

   folios
   code
