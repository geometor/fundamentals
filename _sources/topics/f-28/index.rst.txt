:order: 28
:type: topic
:category: Triangle Centers & Classical Lines
:tags: incenter, incircle, inradius, euler-formula, barycentric

.. _f-28:

=============
F.28 Incenter
=============

*Concurrency of Angle Bisectors, Barycentric Coordinates a:b:c, Contact Vectors, and Incenter-Origin Shift*

.. enunciation::

   The three interior angle bisectors of triangle ABC concur at the incenter I = X(1) with homogeneous barycentric coordinates a : b : c, inradius r = K/s satisfying 1/r = 1/h_a + 1/h_b + 1/h_c, and Euler's distance d_{IO}^2 = R(R - 2r).

.. figure:: f-28.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.28 (Incenter)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   bis_A = angle_bisector(B, A, C)
   bis_B = angle_bisector(C, B, A)
   I = intersect(bis_A, bis_B)
   T_C = foot(I, line(A, B))
   incircle = circle(I, T_C)

Mathematical Synthesis
----------------------

Dated June 1 and November 8, 2011 and citing :person:`Nathan Altshiller-Court <altshiller_court>`'s *College Geometry* (:cite:`AltshillerCourt2007`, :cite:`SeeligNotebooks`), Topic 28 develops the complete coordinate, vector, and metric theory of the :term:`incenter` :g:`I` :math:`= X(1)`.

Seelig records the Cartesian weighted average :math:`\vec{I} = (a\vec{A} + b\vec{B} + c\vec{C})/(2s)`, the vector touchpoints :g:`T_A`, :g:`T_B`, :g:`T_C` along the sides using reduced lengths :math:`x = s-a, y = s-b, z = s-c`, the reciprocal :term:`altitude <orthocenter>` identity :math:`1/r = 1/h_a + 1/h_b + 1/h_c`, :person:`Euler <euler>`'s relation :math:`d^2 = R(R - 2r)`, and a coordinate translation placing the :term:`incenter` at the origin :math:`(0, 0)`. On the canonical :math:`(5, 6, 7)` triangle, :math:`r = \frac{2\sqrt{6}}{3} \approx 1.6330` and :math:`I = (4, \frac{2\sqrt{6}}{3})`.

Key Algebraic Identities
------------------------

.. math::

   \vec{I} = \frac{a \vec{A} + b \vec{B} + c \vec{C}}{a + b + c}, \qquad r = \frac{K}{s} = \sqrt{\frac{(s - a)(s - b)(s - c)}{s}}, \qquad \frac{1}{r} = \frac{1}{h_a} + \frac{1}{h_b} + \frac{1}{h_c}

.. math::

   2 r R = \frac{a b c}{a + b + c}, \qquad d_{IO}^2 = R(R - 2 r) \implies R \ge 2 r

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0202–0206``, 5 scanned manuscript pages in ``resources/seelig/28_incenter``)
   * - **Euclid's Elements**
     - :ref:`IV.4`, :ref:`VI.3` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(7)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Incircle-Incenter``, ``General Reference``, ``5-6-7 A,B,C`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.28" [label="F.28\nIncenter", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-28/index.html"];
       "F.3" [label="F.3\nBiquadratic Forms in Heron's Formula", fillcolor="#90ee90", color="#2e8b57", URL="../f-03/index.html"];
       "F.3" -> "F.28";
       "F.11" [label="F.11\nCircumcenter", fillcolor="#90ee90", color="#2e8b57", URL="../f-11/index.html"];
       "F.11" -> "F.28";
       "F.4" [label="F.4\nCarnot's Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-04/index.html"];
       "F.28" -> "F.4";
       "F.19" [label="F.19\nEqual Incircles Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-19/index.html"];
       "F.28" -> "F.19";
       "F.20" [label="F.20\nExtangent", fillcolor="#e0e0e0", color="#777777", URL="../f-20/index.html"];
       "F.28" -> "F.20";
       "F.29" [label="F.29\nInradius", fillcolor="#e0e0e0", color="#777777", URL="../f-29/index.html"];
       "F.28" -> "F.29";
       "F.52" [label="F.52\nHomogeneous Barycentric Coordinates", fillcolor="#e0e0e0", color="#777777", URL="../f-52/index.html"];
       "F.28" -> "F.52";
   }

**Prerequisites**: :ref:`F.3 Biquadratic Forms in Heron's Formula <f-03>`, :ref:`F.11 Circumcenter <f-11>`

**Required for**: :ref:`F.4 Carnot's Theorem <f-04>`, :ref:`F.19 Equal Incircles Theorem <f-19>`, :ref:`F.20 Extangent <f-20>`, :ref:`F.29 Inradius <f-29>`, :ref:`F.52 Homogeneous Barycentric Coordinates <f-52>`

.. toctree::
   :hidden:

   folios
   code
