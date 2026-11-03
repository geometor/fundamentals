:order: 4
:type: topic
:category: Triangle Centers & Classical Lines
:tags: carnot, circumcenter, incenter, inradius, circumradius

.. _f-04:

====================
F.4 Carnot's Theorem
====================

*Signed Distances from the Circumcenter to the Sides and the Japanese Theorem*

.. enunciation::

   In any triangle ABC, the sum of the signed perpendicular distances from the circumcenter O to the three sides BC, CA, AB equals the sum of the circumradius R and the inradius r: d_a + d_b + d_c = R + r.

.. figure:: f-04.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.4 (Carnot's Theorem)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   O = circumcenter(A, B, C)
   I = incenter(A, B, C)
   M_A = midpoint(B, C)
   M_B = midpoint(C, A)
   M_C = midpoint(A, B)
   d_a = segment(O, M_A)
   d_b = segment(O, M_B)
   d_c = segment(O, M_C)

Mathematical Synthesis
----------------------

Attributed to :person:`Lazare Carnot <carnot>` (1753–1823), :term:`Carnot's theorem` links the perpendicular distances :g:`d_a`, :g:`d_b`, :g:`d_c` from the :term:`circumcenter` :g:`O` :math:`= X(3)` to the side midpoints :g:`M_A`, :g:`M_B`, :g:`M_C` directly to the :term:`circumradius <circumcenter>` :math:`R` and :term:`inradius <incenter>` :math:`r` around the :term:`incenter` :g:`I` :math:`= X(1)`.

Seelig highlights the signed distance convention: :math:`d_m` is positive when :math:`O M_m` lies wholly inside :math:`\triangle ABC` and negative when :g:`O` lies outside the corresponding side (as in an obtuse triangle where :math:`-OH_A + OH_B + OH_C = R + r`). As an immediate corollary, Seelig illustrates the **Japanese Theorem for cyclic polygons**: the sum of the inradii of the triangles in any triangulation of a cyclic polygon is invariant.

Key Algebraic Identities
------------------------

.. math::

   \sum_{m \in \{A, B, C\}} d_m = d_a + d_b + d_c = R(\cos\alpha + \cos\beta + \cos\gamma) = R + r

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0020–0020``, 1 scanned manuscript page in ``resources/seelig/04_carnots-theorem``)
   * - **Euclid's Elements**
     - :ref:`III.20`, :ref:`IV.4`, :ref:`IV.5` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(3)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``General Reference``, ``Circumcircle-Circumcenter``, ``Incircle-Incenter`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.4" [label="F.4\nCarnot's Theorem", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-04/index.html"];
       "F.3" [label="F.3\nBiquadratic Forms in Heron's Formula", fillcolor="#90ee90", color="#2e8b57", URL="../f-03/index.html"];
       "F.3" -> "F.4";
       "F.11" [label="F.11\nCircumcenter", fillcolor="#90ee90", color="#2e8b57", URL="../f-11/index.html"];
       "F.11" -> "F.4";
       "F.28" [label="F.28\nIncenter", fillcolor="#90ee90", color="#2e8b57", URL="../f-28/index.html"];
       "F.28" -> "F.4";
       "F.19" [label="F.19\nEqual Incircles Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-19/index.html"];
       "F.4" -> "F.19";
       "F.32" [label="F.32\nMarkowski's Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-32/index.html"];
       "F.4" -> "F.32";
       "F.38" [label="F.38\nPedal Triangles", fillcolor="#e0e0e0", color="#777777", URL="../f-38/index.html"];
       "F.4" -> "F.38";
       "F.45" [label="F.45\nSquares, Subdivided Lattices, and the Japanese Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-45/index.html"];
       "F.4" -> "F.45";
   }

**Prerequisites**: :ref:`F.3 Biquadratic Forms in Heron's Formula <f-03>`, :ref:`F.11 Circumcenter <f-11>`, :ref:`F.28 Incenter <f-28>`

**Required for**: :ref:`F.19 Equal Incircles Theorem <f-19>`, :ref:`F.32 Markowski's Theorem <f-32>`, :ref:`F.38 Pedal Triangles <f-38>`, :ref:`F.45 Squares, Subdivided Lattices, and the Japanese Theorem <f-45>`

.. toctree::
   :hidden:

   folios
   code
