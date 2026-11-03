:order: 23
:type: topic
:category: Special Triangles & Sacred Proportions
:tags: golden-ratio, golden-triangle, pentagon, stewart, euclid-iv-10

.. _f-23:

=====================
F.23 Golden Triangles
=====================

*The 72-72-36 Sublime Triangle, 5th Roots of Unity, and Normalized Stewart's Theorem*

.. enunciation::

   In the acute golden isosceles triangle ABC with base AB = 1, legs AC = BC = phi, and angles 72-72-36 degrees, bisecting base angle B meets AC at D such that CD = 1, DA = phi - 1 = 1/phi, and BD = AB = 1, partitioning ABC into a smaller golden triangle BCD and a golden gnomon ABD.

.. figure:: f-23.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.23 (Golden Triangles)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   =====
   C = golden_apex(A, B)
   ABC = polygon(A, B, C)
   D = golden_section(A, C)
   BD = segment(B, D)

Mathematical Synthesis
----------------------

Constructed in :cite:`EuclidElements` IV.10 (`G.25` in ``geometor/elements``), the acute :term:`golden triangle` :g:`ABC` has leg-to-base ratio equal to the :term:`golden ratio` :math:`\phi = \frac{1+\sqrt{5}}{2}`. In Topic 23 (:cite:`SeeligNotebooks`), Seelig computes the :term:`altitude <orthocenter>` :math:`CM = \sqrt{\phi^2 - 1/4} = \frac{\sqrt{\phi + 3/4}}{\phi}` and segment :math:`AD = 2\sin 36^\circ = \sqrt{3 - \phi} \approx 1.1756` when :g:`D` divides leg :math:`BC` into :math:`\phi - 1` and :math:`1`.

In Folio 2 (`FWS 12/21/2014`), he constructs the nested *'GOLDEN IDENTITY TRIANGLES'* (right triangles sharing unit altitude with base angles :math:`72^\circ, 54^\circ, 36^\circ, 18^\circ`) and tabulates the 5th roots of unity :math:`e^{i 2\pi n/5}`. In Folio 3 (`FWS 11/18/2013`), he proves the normalized form of :term:`Stewart's theorem` :math:`f^2 = k a^2 + k' b^2 - k k' c^2` (:math:`k + k' = 1`).

Key Algebraic Identities
------------------------

.. math::

   \phi = \frac{1 + \sqrt{5}}{2}, \qquad \cos 36^\circ = \frac{\phi}{2}, \qquad \cos 72^\circ = \frac{\phi - 1}{2} = \frac{1}{2\phi}, \qquad 2\sin 36^\circ = \sqrt{3 - \phi}

.. math::

   f^2 = k a^2 + k' b^2 - k k' c^2 \qquad (k + k' = 1)

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0132–0134``, 3 scanned manuscript pages in ``resources/seelig/23_golden-triangles``)
   * - **Euclid's Elements**
     - :ref:`II.11`, :ref:`IV.10`, :ref:`IV.11`, :ref:`VI.30` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.10`, :ref:`G.25`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Golden Triangle``, ``Polygon Table`` (:ref:`Spreadsheets <spreadsheets>`)

Computational Workbook Verification
-----------------------------------

The following worksheets from :person:`seelig`'s ``Triangles and Circles.ods``
workbook verify the numerical and symbolic formulas for this topic on
the canonical :math:`(a, b, c) = (5, 6, 7)` triangle:

.. admonition:: Worksheet: ``Golden Triangle`` (*Triangles and Circles.ods*)

   **Key Formulas & Parameters**

   .. list-table::
      :widths: 12 28 20 40
      :header-rows: 1

      * - Cell
        - Label / Context
        - Value
        - OpenFormula
      * - ``F11``
        - F11
        - ``0.09549``
        - ``=F13^2``
      * - ``F12``
        - F12
        - ``0.19098``
        - ``=1-[.$F$36]/2``
      * - ``F13``
        - F13
        - ``0.30902``
        - ``=1/(2*[.F$36])``
      * - ``F14``
        - F14
        - ``0.32492``
        - ``=TAN(RADIANS(18))``
      * - ``F15``
        - \|IM\|
        - ``0.36327``
        - ``=F35/F42``
      * - ``F16``
        - \|GM\|
        - ``0.51295``
        - ``=F35/3``
      * - ``F17``
        - F17
        - ``0.52786``
        - ``=(F36-0.5)/(F36+0.5)``
      * - ``F18``
        - F18
        - ``0.58779``
        - ``=F31/2``

   **Cell Excerpt**

   .. list-table::

      * - The Golden Triangle
        - —
        - —
        - —
        - —
        - —
      * - Isosceles triangle with equal sides 
        - —
        - —
        - —
        - —
        - —
      * - Unity base length, vertex angle 36°,
        - —
        - —
        - —
        - —
        - —
      * - Fred W. Seelig
        - —
        - —
        - —
        - —
        - —
      * - Mar. 22, 2015
        - —
        - —
        - Created
        - —
        - —
      * - Mar. 31, 2015
        - —
        - —
        - Last Modified
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
       "F.23" [label="F.23\nGolden Triangles", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-23/index.html"];
       "F.7" [label="F.7\nCeva and Menelaus", fillcolor="#90ee90", color="#2e8b57", URL="../f-07/index.html"];
       "F.7" -> "F.23";
       "F.18" [label="F.18\nEquilateral Triangle", fillcolor="#90ee90", color="#2e8b57", URL="../f-18/index.html"];
       "F.18" -> "F.23";
       "F.40" [label="F.40\nRegular Polygons and Nested Radicals", fillcolor="#e0e0e0", color="#777777", URL="../f-40/index.html"];
       "F.23" -> "F.40";
   }

**Prerequisites**: :ref:`F.7 Ceva and Menelaus <f-07>`, :ref:`F.18 Equilateral Triangle <f-18>`

**Required for**: :ref:`F.40 Regular Polygons and Nested Radicals <f-40>`

.. toctree::
   :hidden:

   folios
   code
