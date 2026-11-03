:order: 43
:type: topic
:category: Circle Inversion, Coaxial & Radical Systems
:tags: radical-axis, radical-center, coaxial, altitude, circles

.. _f-43:

====================================
F.43 Radical Axes and Radical Center
====================================

*Two-Circle Radical Division, Vertex-Altitude Circle Radical Center, and Circular Lens Regimes*

.. enunciation::

   The radical axis of two circles of radii r_1, r_2 with center separation d cuts the line of centers at x = d/2 + (r_1^2 - r_2^2)/(2 d) from O_1, and the three radical axes of the vertex-altitude circles Gamma_A(h_A), Gamma_B(h_B), Gamma_C(h_C) concur at the radical center W.

.. figure:: f-43.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.43 (Radical Axes and Radical Center)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O_1 : Point
   A_1 : Point
   O_2 : Point
   A_2 : Point
   =====
   c_1 = circle(O_1, A_1)
   c_2 = circle(O_2, A_2)
   l_centers = line(O_1, O_2)
   P_1 = intersection(c_1, c_2)
   rad_axis = perpendicular(P_1, l_centers)

Mathematical Synthesis
----------------------

Spanning 11 folios (:cite:`SeeligNotebooks`), Seelig's treatise on the :term:`radical axis` begins (Folio 1) with the fundamental two-circle division formula :math:`x = \frac{d}{2} + \frac{r_1^2 - r_2^2}{2d}`, tested on :math:`r_1=1, r_2=2, d=5` to give :math:`|O_1 P| = 2.2, |O_2 P| = 2.8`, and equal tangent length :math:`t = \frac{4\sqrt{6}}{5} \approx 1.9596`. Folios 2–8 (`FWS Dec. 8/2014`) execute an ambitious 7-page analytic calculation: placing circles :math:`\Gamma_A(h_A), \Gamma_B(h_B), \Gamma_C(h_C)` at the vertices of a triangle with radii equal to the three :term:`altitudes <orthocenter>`, Seelig derives each pairwise :term:`radical axis` in double-intercept form :math:`\frac{x}{x_0} + \frac{y}{y_0} = 1` and solves for their common :term:`radical center` :math:`W = (2.586, 0.603)` on the :math:`(2,3,4)` triangle.

Folios 9–11 classify the five relative position regimes of two circles as :math:`d` varies from :math:`d > r_1 + r_2` (disjoint) through external/internal tangency to :math:`d < |r_1 - r_2|`, recording the circular lens intersection chord and area.

Key Algebraic Identities
------------------------

.. math::

   x = |O_1 P| = \frac{d}{2} + \frac{r_1^2 - r_2^2}{2 d}, \qquad x' = |O_2 P| = \frac{d}{2} - \frac{r_1^2 - r_2^2}{2 d}, \qquad t^2 = x^2 - r_1^2 = {x'}^2 - r_2^2

.. math::

   \Gamma_A(A, h_A),\; \Gamma_B(B, h_B),\; \Gamma_C(C, h_C) \implies \frac{x}{x_0} + \frac{y}{y_0} = 1

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0271–0281``, 11 scanned manuscript pages in ``resources/seelig/43_radical-axes``)
   * - **Euclid's Elements**
     - :ref:`II.5`, :ref:`III.36` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.7`, :ref:`G.11`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Radical Axes``, ``Coaxial Circles`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.43" [label="F.43\nRadical Axes and Radical Center", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-43/index.html"];
       "F.9" [label="F.9\nCircle Equations", fillcolor="#90ee90", color="#2e8b57", URL="../f-09/index.html"];
       "F.9" -> "F.43";
       "F.12" [label="F.12\nCoaxial Circles", fillcolor="#90ee90", color="#2e8b57", URL="../f-12/index.html"];
       "F.12" -> "F.43";
   }

**Prerequisites**: :ref:`F.9 Circle Equations <f-09>`, :ref:`F.12 Coaxial Circles <f-12>`

.. toctree::
   :hidden:

   folios
   code
