:order: 51
:type: topic
:category: Circle Inversion, Coaxial & Radical Systems
:tags: apollonius, apollonian-circles, harmonic, inversion, coaxial

.. _f-51:

=====================================================
F.51 Apollonian Circles and the Problem of Apollonius
=====================================================

*Locus |PA|/|PB| = k, Integer Mean Triples, Power of a Point, and Dörrie's 8-Circle Tangency Table*

.. enunciation::

   The locus of points P with distance ratio \|PA\| / \|PB\| = k > 1 (where \|AB\| = d) is the Apollonian circle of radius R = d k / (k^2 - 1) centered at distance M' = d / (k^2 - 1) beyond B, cutting line AB at the internal and external harmonic conjugates C and D such that \|A T'\|^2 = \|AC\| \|AD\| = \|AB\| \|A M'\|.

.. figure:: f-51.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.51 (Apollonian Circles and the Problem of Apollonius)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   D = harmonic_conjugate(A, B, C)
   M_p = midpoint(C, D)
   c_apol = circle(M_p, C)

Mathematical Synthesis
----------------------

Dated February 7, 2014 (:cite:`SeeligNotebooks`), Seelig's nine-folio treatise on the :term:`Apollonian circles` combines the locus definition :math:`|PA|/|PB| = k` (Folios 1–8) with the classic *Problem of :person:`Apollonius`* (Folio 9, citing :person:`Dorrie`'s *100 Great Problems of Elementary Mathematics*, Problem #32, pp. 154–160, :cite:`Dorrie1965`). Given :math:`|AB| = d`, the internal and external bisectors of :math:`\angle APB` meet :math:`AB` at the :term:`harmonic conjugate` points :g:`C` and :g:`D` (:person:`Euclid` *Elements* :ref:`VI.3`), giving diameter endpoints separated by :math:`2R = \frac{2dk}{k^2-1}` and center :g:`M_p` at :math:`M' = \frac{d}{k^2-1}` from :g:`B`.

Across Folios 4–7, Seelig proves the power-of-a-point tangent identity :math:`|AT'|^2 = |AC|\cdot|AD| = |AB|\cdot|AM'|` and asks when two numbers :math:`m, n` yield simultaneous integer arithmetic, geometric, and harmonic means—finding the parametric solution :math:`m = 36, n = 324 \implies A = 180, G = 108, H = 64.8` (or scaled by 5 for all integers). Folio 9 classifies all :math:`2^3 = 8` Apollonian tangent circles to three given circles by their internal (``I``) or external (``X``) tangency signatures.

Key Algebraic Identities
------------------------

.. math::

   \frac{|PA|}{|PB|} = k \implies M' = \frac{d}{k^2 - 1}, \qquad R = \frac{d k}{k^2 - 1}, \qquad R^2 - {M'}^2 = \frac{d^2}{k^2 - 1}

.. math::

   |A T'|^2 = |AC|\cdot|AD| = |AB|\cdot|A M'| = d(d + M') = \frac{d^2 k^2}{k^2 - 1}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0322–0330``, 9 scanned manuscript pages in ``resources/seelig/51_apollonian-circles``)
   * - **Euclid's Elements**
     - :ref:`III.36`, :ref:`VI.3` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.5`, :ref:`G.7`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Apollonian Circles``, ``Harmonic Conjugates``, ``Coaxial Circles`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.51" [label="F.51\nApollonian Circles and the Problem of Apollonius", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-51/index.html"];
       "F.2" [label="F.2\nBilinear Transformations", fillcolor="#90ee90", color="#2e8b57", URL="../f-02/index.html"];
       "F.2" -> "F.51";
       "F.10" [label="F.10\nCircles and Geometric Mean", fillcolor="#90ee90", color="#2e8b57", URL="../f-10/index.html"];
       "F.10" -> "F.51";
       "F.12" [label="F.12\nCoaxial Circles", fillcolor="#90ee90", color="#2e8b57", URL="../f-12/index.html"];
       "F.12" -> "F.51";
       "F.25" [label="F.25\nHarmonic Conjugates", fillcolor="#90ee90", color="#2e8b57", URL="../f-25/index.html"];
       "F.25" -> "F.51";
       "F.27" [label="F.27\nHarmonic Mean", fillcolor="#90ee90", color="#2e8b57", URL="../f-27/index.html"];
       "F.27" -> "F.51";
   }

**Prerequisites**: :ref:`F.2 Bilinear Transformations <f-02>`, :ref:`F.10 Circles and Geometric Mean <f-10>`, :ref:`F.12 Coaxial Circles <f-12>`, :ref:`F.25 Harmonic Conjugates <f-25>`, :ref:`F.27 Harmonic Mean <f-27>`

.. toctree::
   :hidden:

   folios
   code
