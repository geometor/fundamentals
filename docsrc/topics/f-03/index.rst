:order: 3
:type: topic
:category: Algebraic & Coordinate Systems
:tags: heron, area, biquadratic, circumradius, sympy

.. _f-03:

========================================
F.3 Biquadratic Forms in Heron's Formula
========================================

*Symmetric Quadratic Substitutions, Circumcircle Families, and Extremal Side Lengths*

.. enunciation::

   Under the linear substitution X = a/2, W = (b + c)/2, and Y = (c - b)/2, Heron's area formula reduces to the biquadratic product K = sqrt((W^2 - X^2)(X^2 - Y^2)).

.. figure:: f-03.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.3 (Biquadratic Forms in Heron's Formula)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   a = segment(B, C)
   b = segment(C, A)
   c = segment(A, B)
   H_C = foot(C, c)
   h_c = segment(C, H_C)

Mathematical Synthesis
----------------------

In Topic 03 (:cite:`SeeligNotebooks`), Seelig reformulates :term:`Heron's formula` :math:`K = \sqrt{s(s-a)(s-b)(s-c)}` by introducing the symmetric half-sums and half-differences :math:`X = a/2`, :math:`W = (b+c)/2`, and :math:`Y = (c-b)/2 = -Z`. Because :math:`s = W + X`, :math:`s - a = W - X`, :math:`s - b = X + Y`, and :math:`s - c = X - Y`, the squared area collapses immediately into the biquadratic difference of squares :math:`K^2 = (W^2 - X^2)(X^2 - Y^2)`.

Seelig then studies a triangle inscribed in a circle of constant :term:`circumradius <circumcenter>` :math:`R` with fixed chord :math:`c` and varying side :math:`a`, expressing :math:`b(a; c, R)` via the Law of Sines and solving the stationarity condition via polynomial division of :math:`(x^3 - y^3)/(x - y)` to obtain the extremal relation :math:`{z_i^*}^2 = w_i^2 + w_i w_i' + {w_i'}^2`.

Key Algebraic Identities
------------------------

.. math::

   X = \frac{a}{2}, \quad W = \frac{b + c}{2}, \quad Y = \frac{c - b}{2} \implies K = \sqrt{(W^2 - X^2)(X^2 - Y^2)}

.. math::

   16 K^2 = 2 a^2 b^2 + 2 b^2 c^2 + 2 c^2 a^2 - a^4 - b^4 - c^4, \qquad {z_i^*}^2 = w_i^2 + w_i w_i' + {w_i'}^2

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0011–0019``, 9 scanned manuscript pages in ``resources/seelig/03_biquadratic-forms-in-herons-formula``)
   * - **Euclid's Elements**
     - :ref:`I.47`, :ref:`II.12`, :ref:`II.13` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.1`, :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(3)`, :ref:`X(4)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``General Reference``, ``5-6-7 A,B,C``, ``Biquadratic Heron``, ``Circumcircle Solver`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.3" [label="F.3\nBiquadratic Forms in Heron's Formula", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-03/index.html"];
       "F.4" [label="F.4\nCarnot's Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-04/index.html"];
       "F.3" -> "F.4";
       "F.6" [label="F.6\nCentroid", fillcolor="#e0e0e0", color="#777777", URL="../f-06/index.html"];
       "F.3" -> "F.6";
       "F.11" [label="F.11\nCircumcenter", fillcolor="#e0e0e0", color="#777777", URL="../f-11/index.html"];
       "F.3" -> "F.11";
       "F.13" [label="F.13\nCompare Triangles in Circles", fillcolor="#e0e0e0", color="#777777", URL="../f-13/index.html"];
       "F.3" -> "F.13";
       "F.14" [label="F.14\nConway Notation", fillcolor="#e0e0e0", color="#777777", URL="../f-14/index.html"];
       "F.3" -> "F.14";
       "F.28" [label="F.28\nIncenter", fillcolor="#e0e0e0", color="#777777", URL="../f-28/index.html"];
       "F.3" -> "F.28";
       "F.30" [label="F.30\nIsosceles Triangles", fillcolor="#e0e0e0", color="#777777", URL="../f-30/index.html"];
       "F.3" -> "F.30";
       "F.35" [label="F.35\nObtuse and Acute Triangles", fillcolor="#e0e0e0", color="#777777", URL="../f-35/index.html"];
       "F.3" -> "F.35";
   }

**Required for**: :ref:`F.4 Carnot's Theorem <f-04>`, :ref:`F.6 Centroid <f-06>`, :ref:`F.11 Circumcenter <f-11>`, :ref:`F.13 Compare Triangles in Circles <f-13>`, :ref:`F.14 Conway Notation <f-14>`, :ref:`F.28 Incenter <f-28>`, :ref:`F.30 Isosceles Triangles <f-30>`, :ref:`F.35 Obtuse and Acute Triangles <f-35>`, :ref:`F.50 Altitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem <f-50>`

.. toctree::
   :hidden:

   folios
   code
