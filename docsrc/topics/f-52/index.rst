:order: 52
:type: topic
:category: Algebraic & Coordinate Systems
:tags: barycentric, triangle-centers, etc, nine-point-circle, conway

.. _f-52:

========================================
F.52 Homogeneous Barycentric Coordinates
========================================

*Classical Center Catalog X(1)–X(8), Sidelength Polynomials for X(5), and 5-6-7 Evaluations*

.. enunciation::

   Every triangle center X(n) has homogeneous barycentric coordinates (u : v : w) normalizable to absolute weights lambda_A + lambda_B + lambda_C = 1 such that X = lambda_A A + lambda_B B + lambda_C C; for the nine-point center N = X(5), lambda_A = 1/4 + (b^2 - c^2)(a^2 - (b^2 + c^2)) / (32 K^2).

.. figure:: f-52.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.52 (Homogeneous Barycentric Coordinates)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   G = centroid(A, B, C)
   I = incenter(A, B, C)
   O = circumcenter(A, B, C)
   H = orthocenter(A, B, C)
   N = midpoint(O, H)
   euler = line(O, H)

Mathematical Synthesis
----------------------

Spanning 15 folios (:cite:`SeeligNotebooks`), Seelig's master treatise on :term:`homogeneous barycentric coordinates` (HBC) bridges classical synthetic geometry, :person:`Kimberling`'s *Encyclopedia of Triangle Centers* (:cite:`KimberlingETC`), and programmable calculator/spreadsheet computation. Folios 1–6 (`bari-centers-001`–`006`) tabulate the unnormalized homogeneous coordinates :math:`(u:v:w)`, normalizing sums :math:`\Sigma = u+v+w`, and exact numerical evaluations on the canonical :math:`(5,6,7)` triangle for eight fundamental centers: :term:`incenter` :g:`I` :math:`= X(1) = (a:b:c)`, :term:`centroid` :g:`G` :math:`= X(2) = (1:1:1)`, :term:`circumcenter` :g:`O` :math:`= X(3) = (a^2 S_A : b^2 S_B : c^2 S_C)`, :term:`orthocenter` :g:`H` :math:`= X(4) = (S_B S_C : S_C S_A : S_A S_B)`, :term:`nine-point center <nine-point circle>` :g:`N` :math:`= X(5)`, :term:`symmedian point` :math:`K = X(6) = (a^2:b^2:c^2)`, :term:`Gergonne point` :math:`Ge = X(7)`, and :term:`Nagel point` :math:`Na = X(8) = (s-a:s-b:s-c)`.

In Folios 7–15 (`homogenus-barycentric-co001`–`009`, dated `FWS 2014/9/14`), Seelig derives two explicit forms for the normalized :term:`barycentric coordinates` of the nine-point center :g:`N` (:ref:`X(5)`): Form I (trigonometric, :math:`u = a\cos(\beta - \gamma)`) and Form II (purely polynomial in the side lengths: :math:`\lambda_A = W + \frac{P^2/a^2 + a^4}{D}` with :math:`D = 4U - 2S_4 = 16K^2`), verifying Form II on the :math:`(3,4,5)` right triangle :math:`(\frac{1}{4} : \frac{1}{4} : \frac{1}{2})`, the :math:`(5,6,7)` acute triangle :math:`(0.28299 : 0.30208 : 0.41493)`, and a compass drawing of the :math:`(7,8,9)` nine-point circle (:math:`R_N = \frac{21}{20}\sqrt{5}`).

Key Algebraic Identities
------------------------

.. math::

   P = \lambda_A A + \lambda_B B + \lambda_C C \qquad (\lambda_A + \lambda_B + \lambda_C = 1), \qquad \lambda_A = \frac{u}{u + v + w} = \frac{[PBC]}{[ABC]}

.. math::

   X(1) = (a : b : c),\quad X(2) = (1 : 1 : 1),\quad X(3) = (a^2 S_A : b^2 S_B : c^2 S_C),\quad X(4) = (S_B S_C : S_C S_A : S_A S_B),\quad X(6) = (a^2 : b^2 : c^2)

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0331–0345``, 15 scanned manuscript pages in ``resources/seelig/52_homogeneous-barycentric-coordinates``)
   * - **Euclid's Elements**
     - :ref:`IV.4`, :ref:`IV.5`, :ref:`VI.1` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.7`, :ref:`G.8`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(2)`, :ref:`X(3)`, :ref:`X(4)`, :ref:`X(5)`, :ref:`X(6)`, :ref:`X(7)`, :ref:`X(8)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Barycentric``, ``Barycentric (2)``, ``9-Point Circle``, ``5-6-7 A,B,C`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.52" [label="F.52\nHomogeneous Barycentric Coordinates", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-52/index.html"];
       "F.6" [label="F.6\nCentroid", fillcolor="#90ee90", color="#2e8b57", URL="../f-06/index.html"];
       "F.6" -> "F.52";
       "F.11" [label="F.11\nCircumcenter", fillcolor="#90ee90", color="#2e8b57", URL="../f-11/index.html"];
       "F.11" -> "F.52";
       "F.14" [label="F.14\nConway Notation", fillcolor="#90ee90", color="#2e8b57", URL="../f-14/index.html"];
       "F.14" -> "F.52";
       "F.28" [label="F.28\nIncenter", fillcolor="#90ee90", color="#2e8b57", URL="../f-28/index.html"];
       "F.28" -> "F.52";
       "F.34" [label="F.34\nNine-Point Circle", fillcolor="#90ee90", color="#2e8b57", URL="../f-34/index.html"];
       "F.34" -> "F.52";
       "F.54" [label="F.54\nHP-35s Triangle Program and Coordinate Scripts", fillcolor="#e0e0e0", color="#777777", URL="../f-54/index.html"];
       "F.52" -> "F.54";
   }

**Prerequisites**: :ref:`F.6 Centroid <f-06>`, :ref:`F.11 Circumcenter <f-11>`, :ref:`F.14 Conway Notation <f-14>`, :ref:`F.28 Incenter <f-28>`, :ref:`F.34 Nine-Point Circle <f-34>`

**Required for**: :ref:`F.54 HP-35s Triangle Program and Coordinate Scripts <f-54>`

.. toctree::
   :hidden:

   folios
   code
