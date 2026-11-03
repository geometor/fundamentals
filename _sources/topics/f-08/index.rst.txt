:order: 8
:type: topic
:category: Circle Geometry & Pencils
:tags: chords, power-of-a-point, sagitta, ptolemy, circles

.. _f-08:

======================
F.8 Chord Intersection
======================

*Intersecting Chords Theorem, Sagitta Formula, Power of a Point, and Ptolemy's Bound*

.. enunciation::

   If two chords AB and CD of a circle (O, R) intersect at a point X at distance r = \|OX\| from the center, then the product of their segments is constant and equals the power of X with respect to the circle: \|AX\|*\|BX\| = \|CX\|*\|DX\| = R^2 - \|OX\|^2.

.. figure:: f-08.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.8 (Chord Intersection)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O : Point
   A : Point
   B : Point
   C : Point
   D : Point
   =====
   circle = circle(O, A)
   AB = segment(A, B)
   CD = segment(C, D)
   P = intersect(AB, CD)
   AC = segment(A, C)
   DB = segment(D, B)

Mathematical Synthesis
----------------------

In Topic 08 (:cite:`SeeligNotebooks`), Seelig proves the Intersecting Chords Theorem (:cite:`EuclidElements`, Proposition III.35) via the similarity of :math:`\triangle AXC \sim \triangle DXB` (matching :g:`AC` and :g:`DB` across intersection :g:`P`) and equates the common product to the :term:`power of a point` :math:`R^2 - |OX|^2`.

He illustrates the theorem with two numerical problems: computing the sagitta :math:`x = \frac{5(3-\sqrt{5})}{2} \approx 1.91` of a chord of length :math:`10` in a circle of diameter :math:`15`, and solving :math:`x(10-x) = 4\cdot 4 \implies x = 2, 8` where :math:`R^2 - |OX|^2 = 16`, noting that the inscribed quadrilateral :math:`ACBD` satisfies :person:`Ptolemy <ptolemy>`'s relation :math:`AC\cdot BD + AD\cdot BC = AB\cdot CD = 80`.

Key Algebraic Identities
------------------------

.. math::

   |AX| \cdot |BX| = |CX| \cdot |DX| = R^2 - |OX|^2, \qquad x_{\text{sagitta}} = R - \sqrt{R^2 - \left(\frac{c}{2}\right)^2}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0050–0053``, 4 scanned manuscript pages in ``resources/seelig/08_chord-intersection``)
   * - **Euclid's Elements**
     - :ref:`III.35`, :ref:`III.36` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Chord Intersection`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.8" [label="F.8\nChord Intersection", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-08/index.html"];
       "F.9" [label="F.9\nCircle Equations", fillcolor="#e0e0e0", color="#777777", URL="../f-09/index.html"];
       "F.8" -> "F.9";
       "F.10" [label="F.10\nCircles and Geometric Mean", fillcolor="#e0e0e0", color="#777777", URL="../f-10/index.html"];
       "F.8" -> "F.10";
       "F.12" [label="F.12\nCoaxial Circles", fillcolor="#e0e0e0", color="#777777", URL="../f-12/index.html"];
       "F.8" -> "F.12";
       "F.13" [label="F.13\nCompare Triangles in Circles", fillcolor="#e0e0e0", color="#777777", URL="../f-13/index.html"];
       "F.8" -> "F.13";
       "F.15" [label="F.15\nCyclic Quadrilateral", fillcolor="#e0e0e0", color="#777777", URL="../f-15/index.html"];
       "F.8" -> "F.15";
       "F.25" [label="F.25\nHarmonic Conjugates", fillcolor="#e0e0e0", color="#777777", URL="../f-25/index.html"];
       "F.8" -> "F.25";
       "F.26" [label="F.26\nHarmonic Conjugate Inversion", fillcolor="#e0e0e0", color="#777777", URL="../f-26/index.html"];
       "F.8" -> "F.26";
   }

**Required for**: :ref:`F.9 Circle Equations <f-09>`, :ref:`F.10 Circles and Geometric Mean <f-10>`, :ref:`F.12 Coaxial Circles <f-12>`, :ref:`F.13 Compare Triangles in Circles <f-13>`, :ref:`F.15 Cyclic Quadrilateral <f-15>`, :ref:`F.25 Harmonic Conjugates <f-25>`, :ref:`F.26 Harmonic Conjugate Inversion <f-26>`

.. toctree::
   :hidden:

   folios
   code
