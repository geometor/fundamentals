:order: 27
:type: topic
:category: Projective & Harmonic Geometry
:tags: harmonic-mean, geometric-mean, euclid-vi-3, primes, bilinear

.. _f-27:

==================
F.27 Harmonic Mean
==================

*Compass Construction of the Harmonic Mean, Prime-Number Harmonic Ranges, and the Bilinear Lens*

.. enunciation::

   If C and D are harmonic conjugates with respect to segment AB (so \|AC\|/\|CB\| = \|AD\|/\|BD\|), then the length \|CD\| is the harmonic mean of \|BD\| and \|AD\|: \|CD\| = 2 \|BD\| \|AD\| / (\|BD\| + \|AD\|) = r (gamma + 1/gamma).

.. figure:: f-27.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.27 (Harmonic Mean)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   H : Point
   =====
   O = midpoint(A, B)
   semicircle = circle(O, B)
   C = perpendicular_chord(H, AB, semicircle)
   K = foot(H, segment(O, C))
   H_mean = segment(C, K)

Mathematical Synthesis
----------------------

Dated October 25 and November 13–14, 2013 (:cite:`SeeligNotebooks`), Topic 27 develops both synthetic compass-and-straightedge constructions and algebraic number theory for the :term:`harmonic mean`. Citing Heath's notes on :cite:`EuclidElements` VI.3 (p. 198), Seelig shows that for harmonic points :math:`(A, B; C, D)` with :math:`|BD| = r(\gamma - 1)` and :math:`|AD| = r(\gamma + 1)`, the segment :math:`|CD| = r(\gamma + 1/\gamma)` is the :term:`harmonic mean` of :math:`|BD|` and :math:`|AD|`, and gives a 7-step compass construction laying :math:`n = |BD|` onto :math:`m = |AD|` to form circle :math:`\Gamma_0` of diameter :math:`m - n`.

In Folios 15–16 (`Problems 6–10`), he studies harmonic ranges whose adjacent segments :math:`X = AC, Y = CB` are consecutive prime numbers :math:`P_{n+1}, P_n`, finding :math:`Z = \frac{P_n(P_n+P_{n+1})}{P_{n+1}-P_n}` (:math:`10, 12, 30, 63/2`), and in Folios 17–19 (*'Bilinear Transform As Viewed Through the Lens of :term:`Harmonic Conjugates <harmonic conjugate>`'*) explains why :math:`\kappa = x/r \in (0, 1)` is algebraically more fundamental than :person:`Apollonius <apollonius>`'s ratio :math:`k \in (1, \infty)`.

Key Algebraic Identities
------------------------

.. math::

   |CD| = \operatorname{HM}(|BD|,\, |AD|) = \frac{2 |BD| \cdot |AD|}{|BD| + |AD|} = r\left(\gamma + \frac{1}{\gamma}\right), \qquad x^2 = \frac{(r / t)^2}{\frac{1}{r^2} + \frac{1}{t^2}} = \left(\frac{r}{\gamma}\right)^2

.. math::

   Y^2 + (X + Z) Y - X Z = 0 \implies Y = \frac{-(X + Z) + \sqrt{(X + Z)^2 + 4 X Z}}{2}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0183–0201``, 19 scanned manuscript pages in ``resources/seelig/27_harmonic-mean``)
   * - **Euclid's Elements**
     - :ref:`VI.3`, :ref:`VI.8`, :ref:`VI.13` (:cite:`EuclidElements`)
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
       "F.27" [label="F.27\nHarmonic Mean", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-27/index.html"];
       "F.2" [label="F.2\nBilinear Transformations", fillcolor="#90ee90", color="#2e8b57", URL="../f-02/index.html"];
       "F.2" -> "F.27";
       "F.10" [label="F.10\nCircles and Geometric Mean", fillcolor="#90ee90", color="#2e8b57", URL="../f-10/index.html"];
       "F.10" -> "F.27";
       "F.25" [label="F.25\nHarmonic Conjugates", fillcolor="#90ee90", color="#2e8b57", URL="../f-25/index.html"];
       "F.25" -> "F.27";
       "F.44" [label="F.44\nHomothetic Ratios and Crossed Diagonals", fillcolor="#e0e0e0", color="#777777", URL="../f-44/index.html"];
       "F.27" -> "F.44";
       "F.51" [label="F.51\nApollonian Circles and the Problem of Apollonius", fillcolor="#e0e0e0", color="#777777", URL="../f-51/index.html"];
       "F.27" -> "F.51";
   }

**Prerequisites**: :ref:`F.2 Bilinear Transformations <f-02>`, :ref:`F.10 Circles and Geometric Mean <f-10>`, :ref:`F.25 Harmonic Conjugates <f-25>`

**Required for**: :ref:`F.44 Homothetic Ratios and Crossed Diagonals <f-44>`, :ref:`F.51 Apollonian Circles and the Problem of Apollonius <f-51>`

.. toctree::
   :hidden:

   folios
   code
