:order: 41
:type: topic
:category: Polygons, Tessellations & Special Triangles
:tags: problems, monte-carlo, vesica-piscis, euler, acute

.. _f-41:

=========================================
F.41 Geometric Problems and Extremal Loci
=========================================

*Maximizing Euler Distance d_IO for Acute Triangles, Monte Carlo Vesica Integration, and 25-Problem Compendium*

.. enunciation::

   Among all triangles with longest side c = \|AB\| = 1, the acute locus inside the vesica piscis above the semicircle on AB has area A = int_0^{sqrt(3)} (sqrt(4 - x^2) - 1) dx - pi/4 = (5 pi - 6 sqrt(3))/12 approx 0.44297 (for c = 2), and maximizing d_IO over acute triangles approaches the degenerate right-isosceles limit C -> (0, 1).

.. figure:: f-41.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.41 (Geometric Problems and Extremal Loci)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   M = midpoint(A, B)
   c_semi = circle(M, A)
   c_left = circle(A, B)
   c_right = circle(B, A)
   O = circumcenter(A, B, C)
   I = incenter(A, B, C)

Mathematical Synthesis
----------------------

This 10-folio collection (:cite:`SeeligNotebooks`) combines two analytic geometry sheets (Folios 1–2), a dated calculus and Monte Carlo investigation *Find an acute triangle that maximizes :math:`d_{IO}`* (`FWS 2015/04/24`, Folios 3–4), and a 25-problem compendium (*Problem Set*, Folios 5–10) that served as the blueprint for Seelig's notebook archive.

In his April 24, 2015 study, Seelig fixes base :math:`c = 2` and constrains vertex :g:`C` to the region where :math:`c` is the longest side (inside the :term:`vesica piscis` of radii 2 centered at :g:`A` and :g:`B`) while :math:`\triangle ABC` remains acute (outside the semicircle :g:`c_semi` of radius 1 and between the vertical lines at :g:`A` and :g:`B`). Integrating :math:`A = \int_0^{\sqrt{3}}(\sqrt{4-x^2}-1)\,dx - \frac{\pi}{4} = \frac{5\pi - 6\sqrt{3}}{12} \approx 0.44297`, he explains why his spreadsheet Monte Carlo sampler on :math:`[0,\sqrt{3}]\times[0,1]` has an acceptance rate of :math:`0.44297/\sqrt{3} \approx 25.6\%`, and finds that :math:`d_{IO}` increases monotonically toward the right-triangle boundary :math:`C \to (0, 1)`.

Key Algebraic Identities
------------------------

.. math::

   A_{\text{acute}} = \int_0^{\sqrt{3}} \left(\sqrt{4 - x^2} - 1\right) dx - \frac{\pi}{4} = \frac{5\pi - 6\sqrt{3}}{12} \approx 0.44297

.. math::

   p_{\text{accept}} = \frac{A_{\text{acute}}}{\sqrt{3}} \approx 0.25575, \qquad d_{IO} = \sqrt{R^2 - 2 r R}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0257–0266``, 10 scanned manuscript pages in ``resources/seelig/41_problems``)
   * - **Euclid's Elements**
     - :ref:`I.1`, :ref:`III.31` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.1`, :ref:`G.7`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(3)` (:cite:`Kimberling1998`)
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
       "F.41" [label="F.41\nGeometric Problems and Extremal Loci", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-41/index.html"];
       "F.32" [label="F.32\nMarkowski's Theorem", fillcolor="#90ee90", color="#2e8b57", URL="../f-32/index.html"];
       "F.32" -> "F.41";
       "F.35" [label="F.35\nObtuse and Acute Triangles", fillcolor="#90ee90", color="#2e8b57", URL="../f-35/index.html"];
       "F.35" -> "F.41";
       "F.37" [label="F.37\nEuler's Inradius Parabola", fillcolor="#90ee90", color="#2e8b57", URL="../f-37/index.html"];
       "F.37" -> "F.41";
       "F.49" [label="F.49\nVesica Piscis and Acute-Obtuse Probability", fillcolor="#e0e0e0", color="#777777", URL="../f-49/index.html"];
       "F.41" -> "F.49";
   }

**Prerequisites**: :ref:`F.32 Markowski's Theorem <f-32>`, :ref:`F.35 Obtuse and Acute Triangles <f-35>`, :ref:`F.37 Euler's Inradius Parabola <f-37>`

**Required for**: :ref:`F.49 Vesica Piscis and Acute-Obtuse Probability <f-49>`

.. toctree::
   :hidden:

   folios
   code
