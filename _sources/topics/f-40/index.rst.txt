:order: 40
:type: topic
:category: Polygons, Tessellations & Special Triangles
:tags: polygons, pentagon, decagon, pentadecagon, golden-ratio, radicals

.. _f-40:

=========================================
F.40 Regular Polygons and Nested Radicals
=========================================

*Archimedean Edge-Doubling Recursion, Golden Decagon/Pentagon Radicals, and the Pentadecagon*

.. enunciation::

   For a regular N-gon inscribed in a unit circle (R = 1), doubling the number of sides maps edge length E_{N/2} to E_N = sqrt(2 - sqrt(4 - E_{N/2}^2)), generating closed-form nested quadratic radicals for the 2^k, 3*2^k, 5*2^k, and 15*2^k polygon families.

.. figure:: f-40.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.40 (Regular Polygons and Nested Radicals)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O : Point
   A : Point
   =====
   c_unit = circle(O, A)
   l_oa = line(O, A)
   perp = perpendicular(O, l_oa)
   B = intersection(perp, c_unit)
   M = midpoint(O, B)
   c_five = circle(M, A)

Mathematical Synthesis
----------------------

Spanning 18 folios (:cite:`SeeligNotebooks`), Seelig's treatise on regular :term:`polygons` derives the Archimedean edge-doubling recursion :math:`E_N = \sqrt{2 - \sqrt{4 - E_{N/2}^2}}` (for :term:`circumradius <circumcenter>` :math:`R=1`, where :math:`E_N = 2\sin(\pi/N)` and apothem :math:`r_N = \frac{1}{2}\sqrt{4 - E_N^2}`) and compiles complete nested-radical tables across four constructible families: the square/octagon chain (:math:`E_4 = \sqrt{2}, E_8 = \sqrt{2-\sqrt{2}}, E_{16}, E_{32}, E_{64}`), the triangle/hexagon/dodecagon chain (:math:`E_3 = \sqrt{3}, E_6 = 1, E_{12} = \sqrt{2-\sqrt{3}}, E_{24}`), and the :term:`golden ratio` pentagon/decagon chain (:math:`E_5 = \sqrt{3-\phi} = \frac{1}{2}\sqrt{10-2\sqrt{5}} \approx 1.17557, E_{10} = \sqrt{2-\phi} = \phi - 1 \approx 0.61803, E_{20} = \sqrt{2-\sqrt{2+\phi}}`).

Dated April 20, 2015, the second half of the dossier investigates the regular 15-gon (:person:`Euclid` *Elements* :ref:`IV.16`, :math:`E_{15} = 2\sin 12^\circ \approx 0.41582`), citing James Stafford's exact radical table for multiples of :math:`\pi/30 = 6^\circ`, alongside an angle-chasing exploration of the regular enneagon (:math:`N=9`, requiring a cubic trisection) and two auxiliary Cartesian :term:`cevian <Ceva's theorem>` sheets.

Key Algebraic Identities
------------------------

.. math::

   E_N = 2\sin\frac{\pi}{N} = \sqrt{2 - \sqrt{4 - E_{N/2}^2}}, \qquad r_N = \cos\frac{\pi}{N} = \frac{1}{2}\sqrt{4 - E_N^2}

.. math::

   E_{10} = \phi - 1 = \sqrt{2 - \phi}, \qquad E_5 = \sqrt{3 - \phi}, \qquad E_{15} = 2\sin 12^\circ = \frac{1}{4}\left(\sqrt{10 + 2\sqrt{5}} + \sqrt{3} - \sqrt{15}\right)

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0239–0256``, 18 scanned manuscript pages in ``resources/seelig/40_polygons``)
   * - **Euclid's Elements**
     - :ref:`IV.11`, :ref:`IV.15`, :ref:`IV.16`, :ref:`XIII.9`, :ref:`XIII.10` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.9`, :ref:`G.10`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Polygon Table``, ``Golden Triangle`` (:ref:`Spreadsheets <spreadsheets>`)

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
       "F.40" [label="F.40\nRegular Polygons and Nested Radicals", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-40/index.html"];
       "F.23" [label="F.23\nGolden Triangles", fillcolor="#90ee90", color="#2e8b57", URL="../f-23/index.html"];
       "F.23" -> "F.40";
       "F.45" [label="F.45\nSquares, Subdivided Lattices, and the Japanese Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-45/index.html"];
       "F.40" -> "F.45";
   }

**Prerequisites**: :ref:`F.23 Golden Triangles <f-23>`

**Required for**: :ref:`F.45 Squares, Subdivided Lattices, and the Japanese Theorem <f-45>`

.. toctree::
   :hidden:

   folios
   code
