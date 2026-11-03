:order: 38
:type: topic
:category: Triangle Centers & Classical Circles
:tags: pedal-triangle, trilinear, carnot, circumcircle, area

.. _f-38:

====================
F.38 Pedal Triangles
====================

*Trilinear Pedal Side Lengths, Euler's Pedal Area Theorem, and Carnot's Perpendicularity Law*

.. enunciation::

   The pedal triangle A'B'C' of a point P(tau_A : tau_B : tau_C) has area Delta(P) = ((R^2 - OP^2)/(4 R^2)) Delta, and its six side-projection segments satisfy Carnot's alternating square identity AC'^2 + BA'^2 + CB'^2 = C'B^2 + A'C^2 + B'A^2.

.. figure:: f-38.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.38 (Pedal Triangles)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   P : Point
   =====
   P_A = foot(P, line(B, C))
   P_B = foot(P, line(C, A))
   P_C = foot(P, line(A, B))
   s_ab = segment(P_A, P_B)
   s_bc = segment(P_B, P_C)
   s_ca = segment(P_C, P_A)

Mathematical Synthesis
----------------------

In this two-folio study (:cite:`SeeligNotebooks`), Seelig summarizes the metric and coordinate laws of the :term:`pedal triangle` :math:`\triangle A'B'C'` (labeled :g:`P_A`, :g:`P_B`, :g:`P_C` in the construction) of a point :g:`P` with homogeneous :term:`trilinear coordinates` :math:`(\tau_A : \tau_B : \tau_C)`. Folio 1 records the exact pedal side length :math:`a' = \frac{abc\sqrt{\tau_B^2 + \tau_C^2 + 2\tau_B\tau_C\cos\alpha}}{2R(a\tau_A + b\tau_B + c\tau_C)}` and :person:`Euler`'s pedal area theorem :math:`(\Delta P) = \frac{R^2 - OP^2}{4R^2}\Delta`, which vanishes precisely when :g:`P` lies on the :term:`circumcircle` (:person:`Simson`'s line theorem).

Folio 2 pairs :person:`Carnot`'s alternating segment square identity :math:`{AC'}^2 + {BA'}^2 + {CB'}^2 = {C'B}^2 + {A'C}^2 + {B'A}^2` (annotated with Seelig's marginal exclamation *"wow!"*) with the :math:`3\times 3` trilinear coordinate matrix for the vertices :math:`A', B', C'`.

Key Algebraic Identities
------------------------

.. math::

   a' = \frac{a b c \sqrt{\tau_B^2 + \tau_C^2 + 2\tau_B\tau_C\cos\alpha}}{2 R (a\tau_A + b\tau_B + c\tau_C)}, \qquad \Delta(P) = \frac{R^2 - OP^2}{4 R^2}\Delta

.. math::

   {AC'}^2 + {BA'}^2 + {CB'}^2 = {C'B}^2 + {A'C}^2 + {B'A}^2

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0236–0237``, 2 scanned manuscript pages in ``resources/seelig/38_pedal-triangles``)
   * - **Euclid's Elements**
     - :ref:`I.12`, :ref:`I.47` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.4`, :ref:`G.11`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(3)`, :ref:`X(4)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Pedal Triangle``, ``Orthic Triangle`` (:ref:`Spreadsheets <spreadsheets>`)

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

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.38" [label="F.38\nPedal Triangles", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-38/index.html"];
       "F.4" [label="F.4\nCarnot's Theorem", fillcolor="#90ee90", color="#2e8b57", URL="../f-04/index.html"];
       "F.4" -> "F.38";
       "F.36" [label="F.36\nOrthic Triangle", fillcolor="#90ee90", color="#2e8b57", URL="../f-36/index.html"];
       "F.36" -> "F.38";
   }

**Prerequisites**: :ref:`F.4 Carnot's Theorem <f-04>`, :ref:`F.36 Orthic Triangle <f-36>`

.. toctree::
   :hidden:

   folios
   code
