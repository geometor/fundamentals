:order: 11
:type: topic
:category: Triangle Centers & Classical Lines
:tags: circumcenter, circumcircle, tangential-triangle, barycentric

.. _f-11:

=================
F.11 Circumcenter
=================

*Perpendicular Bisectors, Cartesian Determinant Formulas, Circumcircle Subtriangles, and the Tangential Triangle*

.. enunciation::

   The perpendicular bisectors of the three sides of triangle ABC concur at the circumcenter O = X(3), equidistant from A, B, C by the circumradius R = abc/(4K), with homogeneous barycentric coordinates a^2 S_A : b^2 S_B : c^2 S_C.

.. figure:: f-11.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.11 (Circumcenter)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   M_A = midpoint(B, C)
   M_B = midpoint(C, A)
   M_C = midpoint(A, B)
   perp_a = perpendicular(M_A, line(B, C))
   perp_b = perpendicular(M_B, line(C, A))
   O = intersect(perp_a, perp_b)
   circumcircle = circle(O, A)

Mathematical Synthesis
----------------------

Dated May 25 and May 31, 2011 (:cite:`SeeligNotebooks`), Seelig's study of the :term:`circumcenter` :g:`O` :math:`= X(3)` derives the exact Cartesian coordinates :math:`(x_0, y_0)` from vertex coordinates (correcting a sign error in Joseph O'Rourke's published formula), transcribes Christopher Morley's poem *'A circle is a happy thing to be'*, and decomposes :math:`\triangle ABC` into the three :term:`isosceles <isosceles triangle>` :term:`circumcircle <circumcenter>` subtriangles :math:`\triangle AOB, \triangle BOC, \triangle COA` of :term:`altitudes <orthocenter>` :math:`h_C = \sqrt{R^2 - (c/2)^2}`.

In Folios 5–6, Seelig constructs the **tangential triangle** bounded by the tangent lines to the :g:`circumcircle` at :g:`A`, :g:`B`, :g:`C`, contrasting the acute case (where the tangential triangle encloses :math:`\triangle ABC`) with the obtuse case. On the canonical :math:`(5, 6, 7)` triangle, :math:`R = \frac{35\sqrt{6}}{24} \approx 3.57217` and :math:`O = (7/2, 5\sqrt{6}/18) \approx (3.5, 0.6804)`.

Key Algebraic Identities
------------------------

.. math::

   R = \frac{a b c}{4 K}, \qquad O = \left(a^2 S_A : b^2 S_B : c^2 S_C\right) = \left(\sin 2\alpha : \sin 2\beta : \sin 2\gamma\right)

.. math::

   D = 2\left[x_A(y_C - y_B) + x_B(y_A - y_C) + x_C(y_B - y_A)\right], \qquad x_0 = \frac{\sum (x_A^2 + y_A^2)(y_C - y_B)}{D}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0066–0071``, 6 scanned manuscript pages in ``resources/seelig/11_circumcenter``)
   * - **Euclid's Elements**
     - :ref:`III.1`, :ref:`IV.5` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`, :ref:`G.4`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(3)`, :ref:`X(26)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Circumcircle-Circumcenter``, ``Circumcircle Solver``, ``General Reference`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.11" [label="F.11\nCircumcenter", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-11/index.html"];
       "F.3" [label="F.3\nBiquadratic Forms in Heron's Formula", fillcolor="#90ee90", color="#2e8b57", URL="../f-03/index.html"];
       "F.3" -> "F.11";
       "F.4" [label="F.4\nCarnot's Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-04/index.html"];
       "F.11" -> "F.4";
       "F.13" [label="F.13\nCompare Triangles in Circles", fillcolor="#e0e0e0", color="#777777", URL="../f-13/index.html"];
       "F.11" -> "F.13";
       "F.20" [label="F.20\nExtangent", fillcolor="#e0e0e0", color="#777777", URL="../f-20/index.html"];
       "F.11" -> "F.20";
       "F.28" [label="F.28\nIncenter", fillcolor="#e0e0e0", color="#777777", URL="../f-28/index.html"];
       "F.11" -> "F.28";
       "F.32" [label="F.32\nMarkowski's Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-32/index.html"];
       "F.11" -> "F.32";
       "F.34" [label="F.34\nNine-Point Circle", fillcolor="#e0e0e0", color="#777777", URL="../f-34/index.html"];
       "F.11" -> "F.34";
       "F.37" [label="F.37\nEuler's Inradius Parabola", fillcolor="#e0e0e0", color="#777777", URL="../f-37/index.html"];
       "F.11" -> "F.37";
       "F.52" [label="F.52\nHomogeneous Barycentric Coordinates", fillcolor="#e0e0e0", color="#777777", URL="../f-52/index.html"];
       "F.11" -> "F.52";
   }

**Prerequisites**: :ref:`F.3 Biquadratic Forms in Heron's Formula <f-03>`

**Required for**: :ref:`F.4 Carnot's Theorem <f-04>`, :ref:`F.13 Compare Triangles in Circles <f-13>`, :ref:`F.20 Extangent <f-20>`, :ref:`F.28 Incenter <f-28>`, :ref:`F.32 Markowski's Theorem <f-32>`, :ref:`F.34 Nine-Point Circle <f-34>`, :ref:`F.37 Euler's Inradius Parabola <f-37>`, :ref:`F.52 Homogeneous Barycentric Coordinates <f-52>`

.. toctree::
   :hidden:

   folios
   code
