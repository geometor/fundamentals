:order: 49
:type: topic
:category: Polygons, Tessellations & Special Triangles
:tags: vesica-piscis, euclid, acute, obtuse, monte-carlo, probability

.. _f-49:

===============================================
F.49 Vesica Piscis and Acute-Obtuse Probability
===============================================

*Locus of Longest-Side Triangles, Semicircle Partition, and Exact Area Ratio 3 pi / (5 pi - 6 sqrt(3))*

.. enunciation::

   When segment AB of length c is the longest side of triangle ABC, vertex C lies inside the vesica piscis of area c^2 (4 pi - 3 sqrt(3))/6; the semicircle of diameter AB partitions each quadrant of area c^2 (4 pi - 3 sqrt(3))/24 into an obtuse region (O) = c^2 pi / 16 and an acute region (A) = c^2 (5 pi - 6 sqrt(3))/48, giving an exact obtuse-to-acute probability ratio (O)/(A) = 3 pi / (5 pi - 6 sqrt(3)) approx 1.773.

.. figure:: f-49.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.49 (Vesica Piscis and Acute-Obtuse Probability)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   =====
   c_left = circle(A, B)
   c_right = circle(B, A)
   C = intersection(c_left, c_right)
   M = midpoint(A, B)
   c_semi = circle(M, A)

Mathematical Synthesis
----------------------

Titled *Notes on the locus of points C such that c = |AB| is the longest side* (:cite:`SeeligNotebooks`), this three-folio jewel connects :person:`Euclid`'s Opening Proposition :ref:`I.1` (the :term:`vesica piscis` formed by :g:`c_left` and :g:`c_right` of radius :math:`c`) with :ref:`III.31` (:person:`Thales`'s semicircle :g:`c_semi` on diameter :g:`A` :g:`B` of radius :math:`c/2`). Because :math:`|AC| \le c` and :math:`|BC| \le c`, any triangle with longest side :math:`c` has vertex :g:`C` inside the :term:`vesica piscis`; by fourfold symmetry, Seelig analyzes a single upper-half quadrant of total area :math:`(O) + (A) = c^2\left(\frac{\pi}{6} - \frac{\sqrt{3}}{8}\right)`.

Inside the Thales quarter-disk of radius :math:`c/2`, the angle at :g:`C` is obtuse (:math:`\gamma > 90^\circ`), giving obtuse area :math:`(O) = \frac{1}{4}\pi(c/2)^2 = c^2\frac{\pi}{16}`. Subtracting :math:`(O)` from the quarter-vesica leaves the acute region :math:`(A) = c^2\frac{5\pi - 6\sqrt{3}}{48}`. Dividing the two yields the exact geometric probability ratio :math:`\frac{(O)}{(A)} = \frac{3\pi}{5\pi - 6\sqrt{3}} \approx 1.7731` (63.94% obtuse vs. 36.06% acute)—confirming why random triangles in the ``Monte Carlo`` spreadsheet are predominantly obtuse!

Key Algebraic Identities
------------------------

.. math::

   (O) + (A) = c^2\left(\frac{\pi}{6} - \frac{\sqrt{3}}{8}\right) = c^2\frac{4\pi - 3\sqrt{3}}{24}, \qquad (O) = \frac{1}{4}\pi\left(\frac{c}{2}\right)^2 = c^2\frac{\pi}{16}

.. math::

   (A) = c^2\frac{5\pi - 6\sqrt{3}}{48}, \qquad \frac{(O)}{(A)} = \frac{3\pi}{5\pi - 6\sqrt{3}} \approx 1.7731

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0315–0317``, 3 scanned manuscript pages in ``resources/seelig/49_vesica-pisces``)
   * - **Euclid's Elements**
     - :ref:`I.1`, :ref:`III.31` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.1`, :ref:`G.7`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Monte Carlo``, ``General Reference`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.49" [label="F.49\nVesica Piscis and Acute-Obtuse Probability", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-49/index.html"];
       "F.18" [label="F.18\nEquilateral Triangle", fillcolor="#90ee90", color="#2e8b57", URL="../f-18/index.html"];
       "F.18" -> "F.49";
       "F.35" [label="F.35\nObtuse and Acute Triangles", fillcolor="#90ee90", color="#2e8b57", URL="../f-35/index.html"];
       "F.35" -> "F.49";
       "F.41" [label="F.41\nGeometric Problems and Extremal Loci", fillcolor="#90ee90", color="#2e8b57", URL="../f-41/index.html"];
       "F.41" -> "F.49";
       "F.55" [label="F.55\nCompass Constructions and Angle-to-Side Triangle Reconstruction", fillcolor="#e0e0e0", color="#777777", URL="../f-55/index.html"];
       "F.49" -> "F.55";
   }

**Prerequisites**: :ref:`F.18 Equilateral Triangle <f-18>`, :ref:`F.35 Obtuse and Acute Triangles <f-35>`, :ref:`F.41 Geometric Problems and Extremal Loci <f-41>`

**Required for**: :ref:`F.55 Compass Constructions and Angle-to-Side Triangle Reconstruction <f-55>`

.. toctree::
   :hidden:

   folios
   code
