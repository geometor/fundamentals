:order: 34
:type: topic
:category: Triangle Centers & Classical Circles
:tags: nine-point-circle, euler-line, orthocenter, circumcenter, feuerbach

.. _f-34:

======================
F.34 Nine-Point Circle
======================

*Feuerbach's Nine-Point Circle, Euler Line Collinearity, and Orthocenter Distance Identities*

.. enunciation::

   The circle Gamma_N passing through the three altitude feet H_A, H_B, H_C also passes through the three side midpoints M_A, M_B, M_C and the three Euler midpoints; its radius is r_N = R/2 and its center N = X(5) bisects segment OH on the Euler line.

.. figure:: f-34.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.34 (Nine-Point Circle)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   M_A = midpoint(B, C)
   M_B = midpoint(C, A)
   M_C = midpoint(A, B)
   O = circumcenter(A, B, C)
   H = orthocenter(A, B, C)
   N = midpoint(O, H)
   c_nine = circle(N, M_A)

Mathematical Synthesis
----------------------

In this concentrated summary folio (:cite:`SeeligNotebooks`), Seelig defines the :term:`nine-point circle` :math:`\Gamma_N` (*"The circle that passes through all three footers is the nine point circle"*), recording its center :g:`N` (:ref:`X(5)`), radius :math:`r_N = \frac{1}{2}R`, and two expressions for the distance between the :term:`circumcenter` :g:`O` (:ref:`X(3)`) and :term:`orthocenter` :g:`H` (:ref:`X(4)`): :math:`|OH| = \sqrt{2r^2 + 4R^2 - S_\omega}` (where :math:`S_\omega = \frac{1}{2}(a^2+b^2+c^2)`) and :math:`|OH|^2 = AH^2 + BH^2 + CH^2 - 3R^2 = 9R^2 - (a^2+b^2+c^2)`.

A pencil annotation highlights that :g:`N` lies on the :term:`Euler line` through :g:`O`, :g:`G`, :g:`H` at the midpoint of :g:`O` :g:`H`, illustrated by a compass drawing of the obtuse :math:`(2,3,4)` triangle showing the exterior :term:`altitude <orthocenter>` feet and their common circle :math:`\Gamma_N`. On the canonical :math:`(5,6,7)` triangle, :math:`R = \frac{35\sqrt{6}}{24}`, :math:`r_N = \frac{35\sqrt{6}}{48}`, and :math:`|OH|^2 = 9\left(\frac{1225}{96}\right) - 110 = \frac{155}{32}`.

Key Algebraic Identities
------------------------

.. math::

   r_N = \frac{1}{2} R, \qquad N = \frac{O + H}{2} = X(5), \qquad |ON| = \frac{1}{2}|OH|

.. math::

   |OH|^2 = 9 R^2 - (a^2 + b^2 + c^2) = 2 r^2 + 4 R^2 - \frac{a^2 + b^2 + c^2}{2}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0224–0224``, 1 scanned manuscript page in ``resources/seelig/34_nine-point-circle``)
   * - **Euclid's Elements**
     - :ref:`IV.5` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.7`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(2)`, :ref:`X(3)`, :ref:`X(4)`, :ref:`X(5)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``9-Point Circle``, ``Euler Line``, ``Orthocenter`` (:ref:`Spreadsheets <spreadsheets>`)

Computational Workbook Verification
-----------------------------------

The following worksheets from :person:`seelig`'s ``Triangles and Circles.ods``
workbook verify the numerical and symbolic formulas for this topic on
the canonical :math:`(a, b, c) = (5, 6, 7)` triangle:

.. admonition:: Worksheet: ``Orthocenter`` (*Triangles and Circles.ods*)

   **Key Formulas & Parameters**

   .. list-table::
      :widths: 12 28 20 40
      :header-rows: 1

      * - Cell
        - Label / Context
        - Value
        - OpenFormula
      * - ``I5``
        - I5
        - ``A``
        - ``=D12``
      * - ``J5``
        - A
        - ``0``
        - ``=E12``
      * - ``K5``
        - 0
        - ``0``
        - ``=F12``
      * - ``H6``
        - H6
        - ``B``
        - ``=D13``
      * - ``I6``
        - B
        - ``6``
        - ``=E13``
      * - ``J6``
        - 6
        - ``0``
        - ``=F13``
      * - ``I7``
        - I7
        - ``C``
        - ``=D14``
      * - ``J7``
        - C
        - ``-2``
        - ``=E14``

   **Cell Excerpt**

   .. list-table::

      * - Orthocenter
        - —
        - —
        - —
        - —
        - —
      * - The orthocenter H  is the intersecti
        - —
        - —
        - —
        - —
        - —
      * - When the reference triangle is obtus
        - —
        - —
        - —
        - —
        - —
      * - and has radius rPOLAR2 = 4R2 - (a2+b
        - —
        - —
        - —
        - —
        - —
      * - Fred Seelig
        - —
        - —
        - —
        - —
        - —
      * - Begun 6/1/2011 and completely rework
        - —
        - —
        - —
        - —
        - —

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.34" [label="F.34\nNine-Point Circle", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-34/index.html"];
       "F.6" [label="F.6\nCentroid", fillcolor="#90ee90", color="#2e8b57", URL="../f-06/index.html"];
       "F.6" -> "F.34";
       "F.11" [label="F.11\nCircumcenter", fillcolor="#90ee90", color="#2e8b57", URL="../f-11/index.html"];
       "F.11" -> "F.34";
       "F.36" [label="F.36\nOrthic Triangle", fillcolor="#e0e0e0", color="#777777", URL="../f-36/index.html"];
       "F.34" -> "F.36";
       "F.50" [label="F.50\nAltitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-50/index.html"];
       "F.34" -> "F.50";
       "F.52" [label="F.52\nHomogeneous Barycentric Coordinates", fillcolor="#e0e0e0", color="#777777", URL="../f-52/index.html"];
       "F.34" -> "F.52";
   }

**Prerequisites**: :ref:`F.6 Centroid <f-06>`, :ref:`F.11 Circumcenter <f-11>`

**Required for**: :ref:`F.36 Orthic Triangle <f-36>`, :ref:`F.50 Altitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem <f-50>`, :ref:`F.52 Homogeneous Barycentric Coordinates <f-52>`

.. toctree::
   :hidden:

   folios
   code
