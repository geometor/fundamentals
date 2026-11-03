:order: 2
:type: topic
:category: Projective & Harmonic Geometry
:tags: projective, bilinear, harmonic, apollonius, cross-ratio

.. _f-02:

============================
F.2 Bilinear Transformations
============================

*Projective Involutions, Derivative Identities, and the Apollonian Proportion*

.. enunciation::

   The canonical bilinear transformation B(x) = (1 + x)/(1 - x) and its inverse B^{-1}(y) = (y - 1)/(y + 1) link the internal division ratio kappa = x/r of a segment AB to the Apollonian distance ratio k = (1 + kappa)/(1 - kappa).

.. figure:: f-02.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.2 (Bilinear Transformations)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   S : Point
   =====
   D = harmonic_conjugate(A, B, C)
   l = line(A, B)
   l_prime = projective_image(S, l)

Mathematical Synthesis
----------------------

Dated December 5, 2013 and February 7, 2014 (:cite:`SeeligNotebooks`), Seelig's study of the canonical :term:`bilinear transformation` :math:`\mathbb{B}(x) = \frac{1+x}{1-x} = A(x)B(x)` (with :math:`A(x) = 1+x` and :math:`B(x) = (1-x)^{-1}`) establishes its differential identities :math:`\mathbb{B}' = 2B^2 = B(1+\mathbb{B})` and :math:`\mathbb{B}'' = 4B^3`, together with the rectangular hyperbola conic equation :math:`x/4 - y/4 - xy/4 = 1/4` used for plotting in C.a.R.

In Folios 7–8, Seelig connects :math:`k = \mathbb{B}(\kappa) = \frac{1+\kappa}{1-\kappa}` directly to the Apollonian :term:`harmonic conjugate` division on segment :g:`A` :g:`B` of length :math:`d`, deriving the center :math:`M' = \frac{d}{k^2-1}` and radius :math:`R = \frac{dk}{k^2-1}` of the :term:`Apollonian circles` for :math:`k = 2, 3, 4`.

Key Algebraic Identities
------------------------

.. math::

   \mathbb{B}(x) = \frac{1 + x}{1 - x}, \qquad \mathbb{B}^{-1}(y) = \frac{y - 1}{y + 1}, \qquad \mathbb{B}'(x) = \frac{2}{(1 - x)^2} = 2 B^2

.. math::

   k = \frac{|AC|}{|BC|} = \frac{1 + \kappa}{1 - \kappa} \iff \kappa = \frac{k - 1}{k + 1}, \qquad M' = \frac{d}{k^2 - 1}, \qquad R = \frac{d k}{k^2 - 1}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0003–0010``, 8 scanned manuscript pages in ``resources/seelig/02_bilinear-transformations``)
   * - **Euclid's Elements**
     - :ref:`VI.3` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.5`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Harmonic Conjugates``, ``Apollonian Circles``, ``HC Tables`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.2" [label="F.2\nBilinear Transformations", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-02/index.html"];
       "F.5" [label="F.5\nCenters of Similitude", fillcolor="#e0e0e0", color="#777777", URL="../f-05/index.html"];
       "F.2" -> "F.5";
       "F.7" [label="F.7\nCeva and Menelaus", fillcolor="#e0e0e0", color="#777777", URL="../f-07/index.html"];
       "F.2" -> "F.7";
       "F.12" [label="F.12\nCoaxial Circles", fillcolor="#e0e0e0", color="#777777", URL="../f-12/index.html"];
       "F.2" -> "F.12";
       "F.25" [label="F.25\nHarmonic Conjugates", fillcolor="#e0e0e0", color="#777777", URL="../f-25/index.html"];
       "F.2" -> "F.25";
       "F.27" [label="F.27\nHarmonic Mean", fillcolor="#e0e0e0", color="#777777", URL="../f-27/index.html"];
       "F.2" -> "F.27";
       "F.31" [label="F.31\nLogic Tests", fillcolor="#e0e0e0", color="#777777", URL="../f-31/index.html"];
       "F.2" -> "F.31";
       "F.51" [label="F.51\nApollonian Circles and the Problem of Apollonius", fillcolor="#e0e0e0", color="#777777", URL="../f-51/index.html"];
       "F.2" -> "F.51";
   }

**Required for**: :ref:`F.5 Centers of Similitude <f-05>`, :ref:`F.7 Ceva and Menelaus <f-07>`, :ref:`F.12 Coaxial Circles <f-12>`, :ref:`F.25 Harmonic Conjugates <f-25>`, :ref:`F.27 Harmonic Mean <f-27>`, :ref:`F.31 Logic Tests <f-31>`, :ref:`F.51 Apollonian Circles and the Problem of Apollonius <f-51>`

.. toctree::
   :hidden:

   folios
   code
