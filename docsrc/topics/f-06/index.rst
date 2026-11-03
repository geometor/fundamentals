:order: 6
:type: topic
:category: Triangle Centers & Classical Lines
:tags: centroid, medians, medial-triangle, barycentric

.. _f-06:

============
F.6 Centroid
============

*Concurrency of the Medians, Vector Average, and the Medial Triangle*

.. enunciation::

   The three medians AM_A, BM_B, CM_C joining the vertices of triangle ABC to the midpoints of the opposite sides concur at the centroid G = X(2), which divides each median in a 2 : 1 ratio and has homogeneous barycentric coordinates 1 : 1 : 1.

.. figure:: f-06.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.6 (Centroid)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   M_A = midpoint(B, C)
   M_B = midpoint(C, A)
   M_C = midpoint(A, B)
   m_a = segment(A, M_A)
   m_b = segment(B, M_B)
   m_c = segment(C, M_C)
   G = intersect(m_a, m_b)

Mathematical Synthesis
----------------------

The :term:`centroid` :g:`G` :math:`= X(2)` is the center of mass of :math:`\triangle ABC` and the concurrency point of the three :term:`median <centroid>` :term:`cevians <Ceva's theorem>` :g:`m_a`, :g:`m_b`, :g:`m_c` meeting the opposite side midpoints :g:`M_A`, :g:`M_B`, :g:`M_C` (:cite:`SeeligNotebooks`).

Connecting the midpoints forms the **medial triangle** :math:`\triangle M_A M_B M_C`, which is homothetic to :math:`\triangle ABC` with center :g:`G` and scale factor :math:`-1/2`, partitioning :math:`\triangle ABC` into four congruent subtriangles of area :math:`K/4`. On the canonical :math:`(5, 6, 7)` triangle, :g:`G` has Cartesian coordinates :math:`(13/3, 4\sqrt{6}/7) \approx (4.3333, 1.3997)`.

Key Algebraic Identities
------------------------

.. math::

   \vec{G} = \frac{\vec{A} + \vec{B} + \vec{C}}{3}, \qquad G = (1 : 1 : 1) \text{ in homogeneous barycentrics}

.. math::

   m_a^2 = \frac{2 b^2 + 2 c^2 - a^2}{4}, \qquad m_b^2 = \frac{2 c^2 + 2 a^2 - b^2}{4}, \qquad m_c^2 = \frac{2 a^2 + 2 b^2 - c^2}{4}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0022–0023``, 2 scanned manuscript pages in ``resources/seelig/06_centroid``)
   * - **Euclid's Elements**
     - :ref:`I.10`, :ref:`VI.2` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(2)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``General Reference``, ``Centroid``, ``5-6-7 A,B,C`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.6" [label="F.6\nCentroid", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-06/index.html"];
       "F.3" [label="F.3\nBiquadratic Forms in Heron's Formula", fillcolor="#90ee90", color="#2e8b57", URL="../f-03/index.html"];
       "F.3" -> "F.6";
       "F.7" [label="F.7\nCeva and Menelaus", fillcolor="#e0e0e0", color="#777777", URL="../f-07/index.html"];
       "F.6" -> "F.7";
       "F.34" [label="F.34\nNine-Point Circle", fillcolor="#e0e0e0", color="#777777", URL="../f-34/index.html"];
       "F.6" -> "F.34";
       "F.35" [label="F.35\nObtuse and Acute Triangles", fillcolor="#e0e0e0", color="#777777", URL="../f-35/index.html"];
       "F.6" -> "F.35";
       "F.46" [label="F.46\nStewart's Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-46/index.html"];
       "F.6" -> "F.46";
       "F.52" [label="F.52\nHomogeneous Barycentric Coordinates", fillcolor="#e0e0e0", color="#777777", URL="../f-52/index.html"];
       "F.6" -> "F.52";
   }

**Prerequisites**: :ref:`F.3 Biquadratic Forms in Heron's Formula <f-03>`

**Required for**: :ref:`F.7 Ceva and Menelaus <f-07>`, :ref:`F.34 Nine-Point Circle <f-34>`, :ref:`F.35 Obtuse and Acute Triangles <f-35>`, :ref:`F.46 Stewart's Theorem <f-46>`, :ref:`F.52 Homogeneous Barycentric Coordinates <f-52>`

.. toctree::
   :hidden:

   folios
   code
