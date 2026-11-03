:order: 46
:type: topic
:category: Projective & Harmonic Geometry
:tags: stewart, apollonius, cevian, median, cosine-law

.. _f-46:

======================
F.46 Stewart's Theorem
======================

*Cevian Length Identity f^2 = k a^2 + k' b^2 - k k' c^2 and Apollonius's Median Formula*

.. enunciation::

   If a cevian of length f from C divides base c = AB into segments k' c and k c (with k + k' = 1), Stewart's Theorem states f^2 = k a^2 + k' b^2 - k k' c^2; at the midpoint k = k' = 1/2, this yields Apollonius's median formula f^2 = (1/2)(a^2 + b^2 - c^2/2).

.. figure:: f-46.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.46 (Stewart's Theorem)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   D : Point
   =====
   a = segment(B, C)
   b = segment(C, A)
   c = segment(A, B)
   f_cev = segment(C, D)
   H_C = foot(C, line(A, B))

Mathematical Synthesis
----------------------

Dated November 18, 2013 (:cite:`SeeligNotebooks`), Seelig's two-page proof of :term:`Stewart's theorem` (*":term:`Stewart's Theorem` (also called :person:`Apollonius`' Theorem)"*, after :person:`Stewart`'s 1746 *Some General Theorems of Considerable Use in the Higher Parts of Mathematics*, :cite:`Stewart1746`) normalizes the base segments of :math:`c = AB` by dimensionless :term:`barycentric <barycentric coordinates>` weights :math:`k' = |AD|/c` and :math:`k = |DB|/c` (:math:`k + k' = 1`). Applying the Law of Cosines (or Euclid II.12/II.13 via the :term:`altitude <orthocenter>` foot :g:`H_C`) to the supplementary angles at :g:`D`, the cosine terms cancel upon weighting by :math:`k` and :math:`k'`, leaving the universal :term:`cevian <Ceva's theorem>` formula :math:`f^2 = k a^2 + k' b^2 - k k' c^2`.

On Folio 2, Seelig sets :math:`k = k' = 1/2` to immediately recover :person:`Apollonius <apollonius>`'s :term:`median <centroid>` length identity :math:`m_c^2 = \frac{1}{2}\left(a^2 + b^2 - \frac{1}{2}c^2\right)`. On the canonical :math:`(5,6,7)` triangle, this gives :math:`m_c^2 = \frac{1}{2}(25 + 36 - 49/2) = \frac{73}{4}`, so :math:`m_c = \frac{\sqrt{73}}{2}`.

Key Algebraic Identities
------------------------

.. math::

   f^2 = k a^2 + k' b^2 - k k' c^2 \qquad (k + k' = 1,\; |AD| = k' c,\; |DB| = k c)

.. math::

   k = k' = \frac{1}{2} \implies m_c^2 = \frac{1}{2}\left(a^2 + b^2 - \frac{1}{2}c^2\right) = \frac{2 a^2 + 2 b^2 - c^2}{4}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0293–0294``, 2 scanned manuscript pages in ``resources/seelig/46_stewarts-theorem``)
   * - **Euclid's Elements**
     - :ref:`II.12`, :ref:`II.13` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`, :ref:`G.11`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(2)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Stewart's Theorem``, ``Ceva & Menelaus``, ``Centroid`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.46" [label="F.46\nStewart's Theorem", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-46/index.html"];
       "F.6" [label="F.6\nCentroid", fillcolor="#90ee90", color="#2e8b57", URL="../f-06/index.html"];
       "F.6" -> "F.46";
       "F.7" [label="F.7\nCeva and Menelaus", fillcolor="#90ee90", color="#2e8b57", URL="../f-07/index.html"];
       "F.7" -> "F.46";
       "F.35" [label="F.35\nObtuse and Acute Triangles", fillcolor="#90ee90", color="#2e8b57", URL="../f-35/index.html"];
       "F.35" -> "F.46";
       "F.48" [label="F.48\nVerisimilitude, Corner Subtriangles, and Excircle Homothety", fillcolor="#e0e0e0", color="#777777", URL="../f-48/index.html"];
       "F.46" -> "F.48";
   }

**Prerequisites**: :ref:`F.6 Centroid <f-06>`, :ref:`F.7 Ceva and Menelaus <f-07>`, :ref:`F.35 Obtuse and Acute Triangles <f-35>`

**Required for**: :ref:`F.48 Verisimilitude, Corner Subtriangles, and Excircle Homothety <f-48>`

.. toctree::
   :hidden:

   folios
   code
