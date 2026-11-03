:order: 25
:type: topic
:category: Projective & Harmonic Geometry
:tags: harmonic-conjugates, orthogonal-circles, apollonius, duality, ogilvy

.. _f-25:

========================
F.25 Harmonic Conjugates
========================

*Orthogonal Circles, Ogilvy's Theorem, Dual Relations, and the Pi_+/Pi_- Symmetry Master Diagram*

.. enunciation::

   Collinear points C and D divide segment AB (of midpoint M and half-length r) internally and externally in the same ratio k = \|AC\|/\|BC\| = \|AD\|/\|BD\| if and only if \|MC\|*\|MD\| = r^2, which occurs if and only if the circle on diameter AB and the Apollonian circle on diameter CD intersect orthogonally.

.. figure:: f-25.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.25 (Harmonic Conjugates)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   M = midpoint(A, B)
   circle_AB = circle(M, B)
   D = harmonic_conjugate(A, B, C)
   O_A = midpoint(C, D)
   Apollonius = circle(O_A, C)
   P, P' = intersect(circle_AB, Apollonius)
   polar = segment(P, P')

Mathematical Synthesis
----------------------

Spanning 28 folios (`FWS 6/20/2014`, :cite:`SeeligNotebooks`) and citing :person:`C. Stanley Ogilvy <ogilvy>` (:cite:`Ogilvy1969`, pp. 19–27) and Heath's commentary on :cite:`EuclidElements` VI.3 (p. 198), Topic 25 is Seelig's definitive treatise on :term:`harmonic conjugate` geometry and :term:`orthogonal circles`.

Setting :math:`\kappa = |MC|/r = \frac{k-1}{k+1}` on circle :g:`circle_AB` (center :g:`M`, radius :math:`r`) and :math:`\kappa' = |M'B|/R = 1/k` on the orthogonal :g:`Apollonius` circle (center :g:`O_A`, radius :math:`R`), Seelig proves his **Theorem 1 (Duality Theorem)**: :math:`(\kappa, k)` and :math:`(\kappa', k')` are reciprocal duals (:math:`\kappa' = 1/k, k' = 1/\kappa`). Introducing the hyperbolic-like invariants :math:`\Pi_+ \triangleq \frac{1}{\kappa} + \kappa` and :math:`\Pi_- \triangleq \frac{1}{\kappa} - \kappa` (satisfying :math:`\Pi_+^2 - \Pi_-^2 = 4`), he expresses every chord, :term:`altitude <orthocenter>` :math:`p = PQ`, projection :math:`q = MQ`, center distance :math:`d = MM'`, and tangent :math:`T, T'` in closed symmetric form, verified with the exact rational example :math:`\kappa = 3/7, r = 42, R = 40, d = 58`.

Key Algebraic Identities
------------------------

.. math::

   \frac{|AC|}{|CB|} = \frac{|AD|}{|BD|} = k = \frac{1 + \kappa}{1 - \kappa}, \qquad |MC| \cdot |MD| = x y = r^2, \qquad \frac{2}{|AB|} = \frac{1}{|AC|} + \frac{1}{|AD|}

.. math::

   \Pi_+ = \frac{1}{\kappa} + \kappa, \quad \Pi_- = \frac{1}{\kappa} - \kappa, \quad \Pi_+^2 - \Pi_-^2 = 4, \quad R = \frac{r}{2}\Pi_-, \quad d = \frac{r}{2}\Pi_+, \quad p = r\frac{\Pi_-}{\Pi_+}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0140–0167``, 28 scanned manuscript pages in ``resources/seelig/25_harmonic-conjugates``)
   * - **Euclid's Elements**
     - :ref:`III.36`, :ref:`VI.3` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`, :ref:`G.5`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Harmonic Conjugates``, ``HC Tables``, ``Apollonian Circles``, ``Coaxial Circles`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.25" [label="F.25\nHarmonic Conjugates", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-25/index.html"];
       "F.2" [label="F.2\nBilinear Transformations", fillcolor="#90ee90", color="#2e8b57", URL="../f-02/index.html"];
       "F.2" -> "F.25";
       "F.8" [label="F.8\nChord Intersection", fillcolor="#90ee90", color="#2e8b57", URL="../f-08/index.html"];
       "F.8" -> "F.25";
       "F.12" [label="F.12\nCoaxial Circles", fillcolor="#90ee90", color="#2e8b57", URL="../f-12/index.html"];
       "F.12" -> "F.25";
       "F.26" [label="F.26\nHarmonic Conjugate Inversion", fillcolor="#e0e0e0", color="#777777", URL="../f-26/index.html"];
       "F.25" -> "F.26";
       "F.27" [label="F.27\nHarmonic Mean", fillcolor="#e0e0e0", color="#777777", URL="../f-27/index.html"];
       "F.25" -> "F.27";
       "F.31" [label="F.31\nLogic Tests", fillcolor="#e0e0e0", color="#777777", URL="../f-31/index.html"];
       "F.25" -> "F.31";
       "F.39" [label="F.39\nPole and Polar with Respect to a Triangle", fillcolor="#e0e0e0", color="#777777", URL="../f-39/index.html"];
       "F.25" -> "F.39";
       "F.44" [label="F.44\nHomothetic Ratios and Crossed Diagonals", fillcolor="#e0e0e0", color="#777777", URL="../f-44/index.html"];
       "F.25" -> "F.44";
       "F.51" [label="F.51\nApollonian Circles and the Problem of Apollonius", fillcolor="#e0e0e0", color="#777777", URL="../f-51/index.html"];
       "F.25" -> "F.51";
   }

**Prerequisites**: :ref:`F.2 Bilinear Transformations <f-02>`, :ref:`F.8 Chord Intersection <f-08>`, :ref:`F.12 Coaxial Circles <f-12>`

**Required for**: :ref:`F.26 Harmonic Conjugate Inversion <f-26>`, :ref:`F.27 Harmonic Mean <f-27>`, :ref:`F.31 Logic Tests <f-31>`, :ref:`F.39 Pole and Polar with Respect to a Triangle <f-39>`, :ref:`F.44 Homothetic Ratios and Crossed Diagonals <f-44>`, :ref:`F.51 Apollonian Circles and the Problem of Apollonius <f-51>`

.. toctree::
   :hidden:

   folios
   code
