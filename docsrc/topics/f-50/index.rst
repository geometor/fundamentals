:order: 50
:type: topic
:category: Triangle Centers & Classical Circles
:tags: altitude, orthocenter, heron, symphonic, conway

.. _f-50:

==============================================================================
F.50 Altitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem
==============================================================================

*The Sweet Theorem (h = ab/c), Reciprocal Altitude Area Formula, and Six Orthocenter Identities*

.. enunciation::

   Given the three altitudes h_A, h_B, h_C of triangle ABC with reciprocal semiperimeter H = (h_A^{-1} + h_B^{-1} + h_C^{-1})/2, Mitchell's reciprocal Heron formula states K^{-1} = 4 sqrt(H (H - h_A^{-1})(H - h_B^{-1})(H - h_C^{-1})), and a triangle is right-angled at C if and only if h_A^{-2} + h_B^{-2} = h_C^{-2} (the Symphonic Theorem).

.. figure:: f-50.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.50 (Altitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   H_A = foot(A, line(B, C))
   H_B = foot(B, line(C, A))
   H_C = foot(C, line(A, B))
   h_a = segment(A, H_A)
   h_b = segment(B, H_B)
   h_c = segment(C, H_C)
   H = intersection(line(A, H_A), line(B, H_B))

Mathematical Synthesis
----------------------

Across four folios (:cite:`SeeligNotebooks`), Seelig synthesizes the metric laws of the three :term:`altitude` segments :g:`h_a`, :g:`h_b`, :g:`h_c`. Folio 1 (*Altitude of a Right Triangle (the sweet theorem)*) derives :math:`h = ab/c` and the Inverse Pythagorean Theorem :math:`h^{-2} = a^{-2} + b^{-2}`. Folios 2–3 record :person:`Mitchell`'s (2005) reciprocal :term:`Heron's formula` (:cite:`Mitchell2005`): defining :math:`H = \frac{1}{2}(h_A^{-1}+h_B^{-1}+h_C^{-1})`, the reciprocal area is :math:`K^{-1} = 4\sqrt{H(H-h_A^{-1})(H-h_B^{-1})(H-h_C^{-1})}`, which immediately recovers each side via :math:`a = 2K/h_A`. Seelig also names the *Symphonic Theorem*: since :math:`h_A = b, h_B = a, h_C = ab/c` in a right triangle, the three :term:`altitudes <orthocenter>` satisfy :math:`h_A^{-2} + h_B^{-2} = h_C^{-2}`.

Folio 4 compiles six classical :term:`orthocenter` identities in :term:`Conway triangle notation`, including the sum of upper altitude segments :math:`t_A + t_B + t_C = |AH| + |BH| + |CH| = 2(r + R)` and the altitude-chord product :math:`|AH|\cdot|HH_A| = |BH|\cdot|HH_B| = |CH|\cdot|HH_C|`.

Key Algebraic Identities
------------------------

.. math::

   H = \frac{h_A^{-1} + h_B^{-1} + h_C^{-1}}{2}, \qquad \frac{1}{K} = 4\sqrt{H(H - h_A^{-1})(H - h_B^{-1})(H - h_C^{-1})}

.. math::

   \frac{1}{h_A^2} + \frac{1}{h_B^2} = \frac{1}{h_C^2} \quad (\gamma = 90^\circ), \qquad |AH| + |BH| + |CH| = 2(r + R)

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0318–0321``, 4 scanned manuscript pages in ``resources/seelig/50_altitudes``)
   * - **Euclid's Elements**
     - :ref:`I.12`, :ref:`I.47`, :ref:`VI.8` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.4`, :ref:`G.11`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(3)`, :ref:`X(4)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Altitudes``, ``Orthocenter``, ``Right Triangle`` (:ref:`Spreadsheets <spreadsheets>`)

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
       "F.50" [label="F.50\nAltitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-50/index.html"];
       "F.3" [label="F.3\nBiquadratic Forms in Heron's Formula", fillcolor="#90ee90", color="#2e8b57", URL="../f-03/index.html"];
       "F.3" -> "F.50";
       "F.14" [label="F.14\nConway Notation", fillcolor="#90ee90", color="#2e8b57", URL="../f-14/index.html"];
       "F.14" -> "F.50";
       "F.34" [label="F.34\nNine-Point Circle", fillcolor="#90ee90", color="#2e8b57", URL="../f-34/index.html"];
       "F.34" -> "F.50";
       "F.42" [label="F.42\nAltitude of a Pythagorean Triple Triangle", fillcolor="#90ee90", color="#2e8b57", URL="../f-42/index.html"];
       "F.42" -> "F.50";
   }

**Prerequisites**: :ref:`F.3 Biquadratic Forms in Heron's Formula <f-03>`, :ref:`F.14 Conway Notation <f-14>`, :ref:`F.34 Nine-Point Circle <f-34>`, :ref:`F.42 Altitude of a Pythagorean Triple Triangle <f-42>`

.. toctree::
   :hidden:

   folios
   code
