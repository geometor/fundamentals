:order: 10
:type: topic
:category: Circle Geometry & Pencils
:tags: geometric-mean, semicircle, thales, barycentric, circles

.. _f-10:

===============================
F.10 Circles and Geometric Mean
===============================

*Right-Triangle Altitude Mean Proportional, Square Partitions, and Barycentric Center Table*

.. enunciation::

   In a semicircle on diameter AB = m + n, the perpendicular altitude h = CH from a point C on the circumference to AB is the geometric mean sqrt(m*n) of the segments AH = m and HB = n, while the radius OC = (m + n)/2 is their arithmetic mean.

.. figure:: f-10.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.10 (Circles and Geometric Mean)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   H : Point
   =====
   O = midpoint(A, B)
   semicircle = circle(O, B)
   C = perpendicular_chord(H, AB, semicircle)
   G = segment(C, H)
   A_mean = segment(O, C)

Mathematical Synthesis
----------------------

By Thales's theorem and :cite:`EuclidElements` VI.13, any point :g:`C` on the :g:`semicircle` with diameter :g:`A` :g:`B` forms a right angle :math:`\angle ACB = 90^\circ`. Dropping the :term:`altitude <orthocenter>` :g:`G` (:math:`CH`) to :g:`H` on :g:`A` :g:`B` creates similar right triangles :math:`\triangle ACH \sim \triangle CBH`, proving :math:`CH = \sqrt{AH \cdot HB}` (:term:`geometric mean`).

In Topic 10 (:cite:`SeeligNotebooks`), Seelig applies this semicircle :term:`geometric mean` identity :math:`P^2 = (r + Q)(r - Q)` to the three-circle square partition problem and compiles an early summary table of normalized homogeneous :term:`barycentric coordinates` for :math:`I, O, H, X(7), X(8), X(6), X(5)`.

Key Algebraic Identities
------------------------

.. math::

   G = |CH| = \sqrt{m n}, \qquad A_{\text{mean}} = |OC| = \frac{m + n}{2}, \qquad H_{\text{mean}} = |CK| = \frac{2 m n}{m + n}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0062–0065``, 4 scanned manuscript pages in ``resources/seelig/10_circles-and-geometric-mean``)
   * - **Euclid's Elements**
     - :ref:`II.14`, :ref:`III.31`, :ref:`VI.8`, :ref:`VI.13` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`, :ref:`G.4`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(3)`, :ref:`X(4)`, :ref:`X(5)`, :ref:`X(6)`, :ref:`X(7)`, :ref:`X(8)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``General Reference``, ``Harmonic Conjugates`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.10" [label="F.10\nCircles and Geometric Mean", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-10/index.html"];
       "F.8" [label="F.8\nChord Intersection", fillcolor="#90ee90", color="#2e8b57", URL="../f-08/index.html"];
       "F.8" -> "F.10";
       "F.9" [label="F.9\nCircle Equations", fillcolor="#90ee90", color="#2e8b57", URL="../f-09/index.html"];
       "F.9" -> "F.10";
       "F.17" [label="F.17\nEllipse", fillcolor="#e0e0e0", color="#777777", URL="../f-17/index.html"];
       "F.10" -> "F.17";
       "F.24" [label="F.24\nGothic Arch", fillcolor="#e0e0e0", color="#777777", URL="../f-24/index.html"];
       "F.10" -> "F.24";
       "F.27" [label="F.27\nHarmonic Mean", fillcolor="#e0e0e0", color="#777777", URL="../f-27/index.html"];
       "F.10" -> "F.27";
       "F.42" [label="F.42\nAltitude of a Pythagorean Triple Triangle", fillcolor="#e0e0e0", color="#777777", URL="../f-42/index.html"];
       "F.10" -> "F.42";
       "F.51" [label="F.51\nApollonian Circles and the Problem of Apollonius", fillcolor="#e0e0e0", color="#777777", URL="../f-51/index.html"];
       "F.10" -> "F.51";
       "F.53" [label="F.53\nGeometric Half-Angle Trigonometry", fillcolor="#e0e0e0", color="#777777", URL="../f-53/index.html"];
       "F.10" -> "F.53";
   }

**Prerequisites**: :ref:`F.8 Chord Intersection <f-08>`, :ref:`F.9 Circle Equations <f-09>`

**Required for**: :ref:`F.17 Ellipse <f-17>`, :ref:`F.24 Gothic Arch <f-24>`, :ref:`F.27 Harmonic Mean <f-27>`, :ref:`F.42 Altitude of a Pythagorean Triple Triangle <f-42>`, :ref:`F.51 Apollonian Circles and the Problem of Apollonius <f-51>`, :ref:`F.53 Geometric Half-Angle Trigonometry <f-53>`

.. toctree::
   :hidden:

   folios
   code
