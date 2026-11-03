:order: 35
:type: topic
:category: Polygons, Tessellations & Special Triangles
:tags: euclid, obtuse, acute, altitude, median, cosine-law

.. _f-35:

===============================
F.35 Obtuse and Acute Triangles
===============================

*Euclid's Excess and Deficit (II.12 & II.13), Altitude-Median Offsets, and Apollonius's Theorem*

.. enunciation::

   By Euclid's Elements II.12 (excess) and II.13 (deficit), the square on side a opposite an obtuse or acute angle satisfies a^2 = b^2 + c^2 +/- 2 c x, where x = \|a^2 - (b^2 + c^2)\| / (2 c) is the projection of side b onto line c and h = sqrt(b^2 - x^2) is the altitude.

.. figure:: f-35.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.35 (Obtuse and Acute Triangles)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   l_ab = line(A, B)
   H_C = foot(C, l_ab)
   M_C = midpoint(A, B)
   h_c = segment(C, H_C)
   x_proj = segment(A, H_C)
   d_mh = segment(M_C, H_C)

Mathematical Synthesis
----------------------

Titled *OBTUSE AND ACUTE TRIANGLES / EUCLID'S CONCEPT OF 'EXCESS' AND 'DEFICIT'* (:cite:`SeeligNotebooks`), this seven-folio study recovers :person:`Euclid`'s geometric precursors to the Law of Cosines: :ref:`II.12` (*excess* :math:`+2cx` for obtuse triangles) and :ref:`II.13` (*deficit* :math:`-2cx` for acute triangles). Without invoking trigonometric functions, Seelig computes the :term:`altitude <orthocenter>` foot projection :math:`x = \pm\frac{a^2-(b^2+c^2)}{2c}` and altitude :math:`h = \sqrt{b^2-x^2}` directly from the three side lengths.

Across Folios 2–7, Seelig works out three canonical integer triangles in complete detail: the obtuse :math:`(3,5,7)` Eisenstein triangle (:math:`120^\circ` angle, :math:`x = 1.5, h_B = \frac{3\sqrt{3}}{2}` and :math:`x = \frac{65}{14}, h_c = \frac{15\sqrt{3}}{14}`), the acute :math:`(5,6,7)` triangle (:math:`x = 1`, division ratio :math:`r/r' = 28/9`), and the acute :math:`(7,8,9)` triangle, computing the exact distance :math:`|m_A h_A| = \frac{17}{14}, |m_B h_B| = \frac{33}{16}, |m_C h_C| = \frac{5}{6}` between each midpoint and altitude foot, before closing with :person:`Apollonius`'s :term:`median <centroid>` identity :math:`D^2 = \frac{U^2+V^2}{2} - (E/2)^2`.

Key Algebraic Identities
------------------------

.. math::

   a^2 = b^2 + c^2 \pm 2 c x \implies x = \frac{|a^2 - (b^2 + c^2)|}{2 c}, \qquad h^2 = b^2 - x^2

.. math::

   |M_C H_C| = \left|\frac{c}{2} - x\right| = \frac{|a^2 - b^2|}{2 c}, \qquad m_c^2 = \frac{a^2 + b^2}{2} - \left(\frac{c}{2}\right)^2

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0225–0231``, 7 scanned manuscript pages in ``resources/seelig/35_obtuse-and-acute``)
   * - **Euclid's Elements**
     - :ref:`II.12`, :ref:`II.13` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`, :ref:`G.11`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(2)`, :ref:`X(4)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``General Reference``, ``5-6-7 A,B,C``, ``Altitudes`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.35" [label="F.35\nObtuse and Acute Triangles", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-35/index.html"];
       "F.3" [label="F.3\nBiquadratic Forms in Heron's Formula", fillcolor="#90ee90", color="#2e8b57", URL="../f-03/index.html"];
       "F.3" -> "F.35";
       "F.6" [label="F.6\nCentroid", fillcolor="#90ee90", color="#2e8b57", URL="../f-06/index.html"];
       "F.6" -> "F.35";
       "F.36" [label="F.36\nOrthic Triangle", fillcolor="#e0e0e0", color="#777777", URL="../f-36/index.html"];
       "F.35" -> "F.36";
       "F.41" [label="F.41\nGeometric Problems and Extremal Loci", fillcolor="#e0e0e0", color="#777777", URL="../f-41/index.html"];
       "F.35" -> "F.41";
       "F.46" [label="F.46\nStewart's Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-46/index.html"];
       "F.35" -> "F.46";
       "F.47" [label="F.47\nThe UVW Coordinate Triangle", fillcolor="#e0e0e0", color="#777777", URL="../f-47/index.html"];
       "F.35" -> "F.47";
       "F.49" [label="F.49\nVesica Piscis and Acute-Obtuse Probability", fillcolor="#e0e0e0", color="#777777", URL="../f-49/index.html"];
       "F.35" -> "F.49";
   }

**Prerequisites**: :ref:`F.3 Biquadratic Forms in Heron's Formula <f-03>`, :ref:`F.6 Centroid <f-06>`

**Required for**: :ref:`F.36 Orthic Triangle <f-36>`, :ref:`F.41 Geometric Problems and Extremal Loci <f-41>`, :ref:`F.46 Stewart's Theorem <f-46>`, :ref:`F.47 The UVW Coordinate Triangle <f-47>`, :ref:`F.49 Vesica Piscis and Acute-Obtuse Probability <f-49>`

.. toctree::
   :hidden:

   folios
   code
