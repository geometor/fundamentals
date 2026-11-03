:order: 36
:type: topic
:category: Triangle Centers & Classical Circles
:tags: orthic-triangle, orthocenter, fagnano, pedal-triangle, tangential

.. _f-36:

====================
F.36 Orthic Triangle
====================

*Pedal Triangle of the Orthocenter, Tangential Homothety, and Fagnano's Minimum-Perimeter Problem*

.. enunciation::

   The orthic triangle H_A H_B H_C formed by the altitude feet of an acute triangle ABC is the pedal triangle of the orthocenter H = X(4), is homothetic to the tangential triangle, has H as its incenter, and solves Fagnano's 1775 problem by minimizing the perimeter among all triangles inscribed in ABC.

.. figure:: f-36.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.36 (Orthic Triangle)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   H_A = foot(A, line(B, C))
   H_B = foot(B, line(C, A))
   H_C = foot(C, line(A, B))
   H = intersection(line(A, H_A), line(B, H_B))
   s_ab = segment(H_A, H_B)
   s_bc = segment(H_B, H_C)
   s_ca = segment(H_C, H_A)

Mathematical Synthesis
----------------------

On Folio ``orthic012.jpg`` (:cite:`SeeligNotebooks`), Seelig synthesizes the three defining properties of the :term:`orthic triangle` :math:`\triangle H_A H_B H_C`: (1) it is the :term:`pedal triangle` of the :term:`orthocenter` :g:`H` (:ref:`X(4)`), whose :term:`altitudes <orthocenter>` bisect the interior angles of :math:`\triangle H_A H_B H_C` so that :g:`H` is the :term:`incenter` of the :term:`orthic triangle`; (2) its sides are anti-parallel to :math:`BC, CA, AB` and parallel to the tangents to the :term:`circumcircle` at :g:`A`, :g:`B`, :g:`C`, making it homothetic to the tangential triangle; and (3) for any acute :math:`\triangle ABC`, it solves :person:`Fagnano`'s Problem (1775), achieving the minimum perimeter :math:`p_{\text{orthic}} = 2K/R = 4R\sin\alpha\sin\beta\sin\gamma` among all inscribed triangles.

On the canonical :math:`(5,6,7)` acute triangle (:math:`K = 6\sqrt{6}, R = \frac{35\sqrt{6}}{24}`), the orthic sides are :math:`a\cos\alpha = \frac{19}{7}, b\cos\beta = \frac{9}{7}, c\cos\gamma = \frac{1}{5}`, giving the exact minimum Fagnano perimeter :math:`p_{\text{orthic}} = \frac{2K}{R} = \frac{288}{35}`.

Key Algebraic Identities
------------------------

.. math::

   a_{\text{orthic}} = a \cos\alpha, \qquad b_{\text{orthic}} = b \cos\beta, \qquad c_{\text{orthic}} = c \cos\gamma

.. math::

   p_{\text{orthic}} = \frac{2 K}{R} = 4 R \sin\alpha\sin\beta\sin\gamma, \qquad K_{\text{orthic}} = 2 K \cos\alpha\cos\beta\cos\gamma

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0232–0232``, 1 scanned manuscript page in ``resources/seelig/36_orthic-triangle``)
   * - **Euclid's Elements**
     - :ref:`I.12`, :ref:`III.32` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.4`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(3)`, :ref:`X(4)`, :ref:`X(5)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Orthic Triangle``, ``Orthocenter``, ``Pedal Triangle`` (:ref:`Spreadsheets <spreadsheets>`)

Computational Workbook Verification
-----------------------------------

The following worksheets from :person:`seelig`'s ``Triangles and Circles.ods``
workbook verify the numerical and symbolic formulas for this topic on
the canonical :math:`(a, b, c) = (5, 6, 7)` triangle:

.. admonition:: Worksheet: ``Orthic Triangle`` (*Triangles and Circles.ods*)

   **Key Formulas & Parameters**

   .. list-table::
      :widths: 12 28 20 40
      :header-rows: 1

      * - Cell
        - Label / Context
        - Value
        - OpenFormula
      * - ``G18``
        - G18
        - ``5``
        - ``=G16``
      * - ``H18``
        - 5
        - ``5``
        - ``=H16``
      * - ``G19``
        - G19
        - ``-9``
        - ``=G17``
      * - ``H19``
        - -9
        - ``4``
        - ``=H17``
      * - ``G20``
        - G20
        - ``0``
        - ``=G18``
      * - ``H20``
        - 0
        - ``6``
        - ``=H18``
      * - ``G22``
        - G22
        - ``9.2``
        - ``=SQRT((G18-G17)^2+(H18-H17)^2)``
      * - ``H22``
        - 9.2
        - ``9.2``
        - ``=G23``

   **Cell Excerpt**

   .. list-table::

      * - Orthic Triangle
        - —
        - —
        - —
        - —
        - —
      * - The reference triangle DR's orthic t
        - —
        - —
        - —
        - —
        - —
      * - The three vertices are the three foo
        - —
        - —
        - —
        - —
        - —
      * - The orthic center H is the incenter 
        - —
        - —
        - —
        - —
        - —
      * - This is an incredibly useful triangl
        - —
        - —
        - —
        - —
        - —
      * - Since most sketches start with a DC,
        - —
        - —
        - —
        - —
        - —

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
       "F.36" [label="F.36\nOrthic Triangle", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-36/index.html"];
       "F.34" [label="F.34\nNine-Point Circle", fillcolor="#90ee90", color="#2e8b57", URL="../f-34/index.html"];
       "F.34" -> "F.36";
       "F.35" [label="F.35\nObtuse and Acute Triangles", fillcolor="#90ee90", color="#2e8b57", URL="../f-35/index.html"];
       "F.35" -> "F.36";
       "F.38" [label="F.38\nPedal Triangles", fillcolor="#e0e0e0", color="#777777", URL="../f-38/index.html"];
       "F.36" -> "F.38";
   }

**Prerequisites**: :ref:`F.34 Nine-Point Circle <f-34>`, :ref:`F.35 Obtuse and Acute Triangles <f-35>`

**Required for**: :ref:`F.38 Pedal Triangles <f-38>`

.. toctree::
   :hidden:

   folios
   code
