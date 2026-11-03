:order: 13
:type: topic
:category: Circle Geometry & Pencils
:tags: circumcircle, chords, area, nested-radicals, medians

.. _f-13:

=================================
F.13 Compare Triangles in Circles
=================================

*Inscribed Triangle Area with Fixed Chord and Circumradius, Nested Radical Chords, and Isosceles Decomposition*

.. enunciation::

   For a family of triangles ABC inscribed in a fixed circle of radius R sharing a fixed chord AB = c (with central angle 2*phi where sin(phi) = c/(2R)), the area K decomposes into the signed sum of three central isosceles triangles: K = (1/2) c h_c + (1/2) a h_a - (1/2) b h_b.

.. figure:: f-13.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.13 (Compare Triangles in Circles)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O : Point
   A : Point
   B : Point
   C : Point
   D : Point
   =====
   circle = circle(O, A)
   AB = segment(A, B)
   AC = segment(A, C)
   BC = segment(B, C)

Mathematical Synthesis
----------------------

Complementing Topic 03 (:ref:`F.3 <f-03>`), Seelig's 8-folio study in Topic 13 (:cite:`SeeligNotebooks`) tracks how the area :math:`K = (\triangle ABC)` and side lengths :math:`a(\theta; R), b(\theta; R)` behave as vertex :g:`C` moves around a fixed :term:`circumcircle <circumcenter>` :math:`\Gamma_R` above a fixed chord :math:`AB = c`.

In Folio 3, he tabulates exact nested-radical chord lengths :math:`|BC| = \frac{\sqrt{2n^2 \pm 2n\sqrt{n^2-m^2}}}{n}` for :math:`c/R = 2m/n \in [1/4, 7/4]`. In Folio 5, he highlights a result marked *'Surprise & pretty'*: decomposing :math:`(\triangle ABC) = \frac{1}{2}ch_c + \frac{1}{2}ah_a - \frac{1}{2}bh_b` into three :term:`isosceles <isosceles triangle>` triangles with common apex at the circumcenter :g:`O`.

Key Algebraic Identities
------------------------

.. math::

   \sin\phi = \frac{c}{2 R}, \qquad h_c = \sqrt{R^2 - \left(\frac{c}{2}\right)^2}, \qquad (ABC) = \frac{1}{2} c h_c + \frac{1}{2} a h_a - \frac{1}{2} b h_b

.. math::

   a^2 = f^2 + \frac{c^2}{4} + f c \cos\theta, \qquad b^2 = f^2 + \frac{c^2}{4} - f c \cos\theta

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0084–0091``, 8 scanned manuscript pages in ``resources/seelig/13_compare-triangles-in-circles``)
   * - **Euclid's Elements**
     - :ref:`III.20`, :ref:`IV.5` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(3)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Circumcircle Solver``, ``Circumcircle-Circumcenter`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.13" [label="F.13\nCompare Triangles in Circles", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-13/index.html"];
       "F.3" [label="F.3\nBiquadratic Forms in Heron's Formula", fillcolor="#90ee90", color="#2e8b57", URL="../f-03/index.html"];
       "F.3" -> "F.13";
       "F.8" [label="F.8\nChord Intersection", fillcolor="#90ee90", color="#2e8b57", URL="../f-08/index.html"];
       "F.8" -> "F.13";
       "F.11" [label="F.11\nCircumcenter", fillcolor="#90ee90", color="#2e8b57", URL="../f-11/index.html"];
       "F.11" -> "F.13";
   }

**Prerequisites**: :ref:`F.3 Biquadratic Forms in Heron's Formula <f-03>`, :ref:`F.8 Chord Intersection <f-08>`, :ref:`F.11 Circumcenter <f-11>`

.. toctree::
   :hidden:

   folios
   code
