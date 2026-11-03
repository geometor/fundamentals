:order: 26
:type: topic
:category: Projective & Harmonic Geometry
:tags: inversion, harmonic-conjugates, power-of-a-point, steiner, diophantine

.. _f-26:

=================================
F.26 Harmonic Conjugate Inversion
=================================

*Inversion xy = r^2, Steiner's Power of a Point, the Important Parallelogram MDM_TT, and Diophantine Triples*

.. enunciation::

   For a circle Gamma of center M and radius r on diameter AB, internal point C at x = \|MC\| and its harmonic conjugate D at y = \|MD\| are inverses satisfying x*y = r^2, while the tangent DT = T forms a parallelogram M D M_T T whose long diagonal z satisfies z^2 = y^2 + 3*r^2 by Stewart's Theorem.

.. figure:: f-26.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.26 (Harmonic Conjugate Inversion)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   M = midpoint(A, B)
   circle_AB = circle(M, B)
   D = harmonic_conjugate(A, B, C)
   P, P' = tangent_points(D, circle_AB)
   polar = segment(P, P')

Mathematical Synthesis
----------------------

Titled *'The Relationship Between Harmonic Conjugation, :term:`Inversion`, and The Powers of a Point, as Revealed by An Important Parallelogram'* (`FWS 11/19/2013`–`11/20/2013`, :cite:`SeeligNotebooks`), Topic 26 synthesizes :term:`inversion` (:math:`x y = r^2`), :person:`Jakob Steiner <steiner>`'s :term:`power of a point` (:math:`T^2 = y^2 - r^2 = AD\cdot BD`), and :term:`Stewart's theorem`.

Applying :term:`Stewart's theorem` to the parallelogram :math:`M D M_T T` with sides :math:`r, y` and short diagonal :math:`T = |DT|`, Seelig proves that the long diagonal :math:`z = |M M_T|` satisfies :math:`z^2 = y^2 + 3r^2`. Furthermore, by rescaling any primitive :term:`Pythagorean triple` :math:`(\hat{x}, \hat{t}, \hat{r})` by :math:`\hat{x}`, he generates all-integer solutions :math:`(x, t, r, y, T) = (\hat{x}^2, \hat{x}\hat{t}, \hat{x}\hat{r}, \hat{r}^2, \hat{r}\hat{t})`, such as :math:`(9, 12, 15, 25, 20)` for :math:`\kappa = 3/5`.

Key Algebraic Identities
------------------------

.. math::

   x y = |MC| \cdot |MD| = r^2, \qquad T^2 = y^2 - r^2 = |AD| \cdot |BD|, \qquad z^2 + T^2 = 2(r^2 + y^2) \implies z^2 = y^2 + 3 r^2

.. math::

   (x,\, t,\, r,\, y,\, T) = \left(\hat{x}^2,\, \hat{x}\hat{t},\, \hat{x}\hat{r},\, \hat{r}^2,\, \hat{r}\hat{t}\right) \quad \text{where } \hat{x}^2 + \hat{t}^2 = \hat{r}^2

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0168–0182``, 15 scanned manuscript pages in ``resources/seelig/26_harmonic-conjugate-inversion``)
   * - **Euclid's Elements**
     - :ref:`III.36`, :ref:`VI.8` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`, :ref:`G.5`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Harmonic Conjugates``, ``HC Tables`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.26" [label="F.26\nHarmonic Conjugate Inversion", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-26/index.html"];
       "F.8" [label="F.8\nChord Intersection", fillcolor="#90ee90", color="#2e8b57", URL="../f-08/index.html"];
       "F.8" -> "F.26";
       "F.25" [label="F.25\nHarmonic Conjugates", fillcolor="#90ee90", color="#2e8b57", URL="../f-25/index.html"];
       "F.25" -> "F.26";
   }

**Prerequisites**: :ref:`F.8 Chord Intersection <f-08>`, :ref:`F.25 Harmonic Conjugates <f-25>`

.. toctree::
   :hidden:

   folios
   code
