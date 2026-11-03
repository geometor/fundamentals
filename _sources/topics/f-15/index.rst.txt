:order: 15
:type: topic
:category: Circle Geometry & Pencils
:tags: cyclic-quadrilateral, ptolemy, golden-ratio, chords, polygons

.. _f-15:

=========================
F.15 Cyclic Quadrilateral
=========================

*Golden-Ratio Chords for Angles theta, 2*theta, 3*theta, 4*theta, Ptolemy's Theorem, and Geometric Progression Impossibility*

.. enunciation::

   A cyclic quadrilateral WXYZ whose interior angles form the arithmetic progression theta, 2*theta, 3*theta, 4*theta has theta = 36 degrees (W = 36, X = 72, Y = 144, Z = 108) and golden-ratio diagonals \|XZ\| = 2 sin(36) = sqrt(3 - phi) and \|WY\| = 2 sin(72) = phi*sqrt(3 - phi) in the unit circle; by contrast, no non-trivial cyclic quadrilateral can have interior angles in geometric progression theta, k*theta, k^2*theta, k^3*theta.

.. figure:: f-15.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.15 (Cyclic Quadrilateral)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O : Point
   A : Point
   B : Point
   C : Point
   D : Point
   =====
   circumcircle = circle(O, A)
   ABCD = polygon(A, B, C, D)
   e = segment(A, C)
   f = segment(B, D)
   P = intersect(e, f)

Mathematical Synthesis
----------------------

Written in April 2015 (:cite:`SeeligNotebooks`), Seelig's 16-folio investigation of the :term:`cyclic quadrilateral` :math:`WXYZ` explores three distinct problems. First, when the interior angles are :math:`\theta, 2\theta, 3\theta, 4\theta`, the opposite-angle supplementary law (:cite:`EuclidElements` III.22) forces the ordering :math:`W = 36^\circ, X = 72^\circ, Y = 144^\circ, Z = 108^\circ`, so the diagonals :g:`e` and :g:`f` in a unit circle have exact :term:`golden ratio` lengths :math:`|XZ| = 2\sin 36^\circ = \sqrt{3-\phi}` and :math:`|YW| = 2\sin 72^\circ = \phi\sqrt{3-\phi}`.

Second, when the *central* angles are :math:`\theta, 2\theta, 3\theta, 4\theta` (:math:`\theta = 36^\circ`), the sides and diagonals are :math:`a = \phi - 1, c = \phi, |WY| = \phi, |XZ| = 2`. Third, in Folios 15–16 (*'An Open :term:`Cyclic Quadrilateral` Problem'*), Seelig proves that no non-square cyclic quadrilateral can have interior angles in geometric progression :math:`\theta, k\theta, k^2\theta, k^3\theta` because the resulting supplementary cubics :math:`k^3 \mp k^2 \mp k \pm 1 = 0` have only roots :math:`\pm 1, \pm i`.

Key Algebraic Identities
------------------------

.. math::

   \theta + 2\theta + 3\theta + 4\theta = 360^\circ \implies \theta = 36^\circ, \qquad f = |XZ| = 2\sin 36^\circ = \sqrt{3 - \phi}, \qquad e = |YW| = 2\sin 72^\circ = \phi\sqrt{3 - \phi}

.. math::

   a c + b d = e f \quad (\text{Ptolemy}), \qquad (k^3 - k^2 + k - 1) = (k - 1)(k^2 + 1) = 0

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0098–0113``, 16 scanned manuscript pages in ``resources/seelig/15_cyclic-quadrilateral``)
   * - **Euclid's Elements**
     - :ref:`III.21`, :ref:`III.22`, :ref:`IV.11` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Cyclic Quad``, ``Chord Intersection`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.15" [label="F.15\nCyclic Quadrilateral", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-15/index.html"];
       "F.8" [label="F.8\nChord Intersection", fillcolor="#90ee90", color="#2e8b57", URL="../f-08/index.html"];
       "F.8" -> "F.15";
   }

**Prerequisites**: :ref:`F.8 Chord Intersection <f-08>`

.. toctree::
   :hidden:

   folios
   code
