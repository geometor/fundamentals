:order: 17
:type: topic
:category: Conics & Analytic Loci
:tags: ellipse, conics, compass-construction, eccentricity, latus-rectum

.. _f-17:

============
F.17 Ellipse
============

*Seven-Step Five-Circle Compass Oval Construction and Focus-Directrix Conic Relations*

.. enunciation::

   Given semi-major axis a and semi-minor axis b, a four-center circular-arc oval approximating the ellipse x^2/a^2 + y^2/b^2 = 1 is constructed by a 7-step five-circle compass procedure, while the exact conic satisfies F = a*e, d = a/e, and vertex mean proportional V = a = sqrt(d*F).

.. figure:: f-17.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.17 (Ellipse)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O : Point
   A_1 : Point
   A_2 : Point
   B_1 : Point
   =====
   F_1 = focus_left(O, A_2, B_1)
   F_2 = focus_right(O, A_2, B_1)
   P = point_on_ellipse(A_2, B_1)
   r_1 = segment(F_1, P)
   r_2 = segment(F_2, P)

Mathematical Synthesis
----------------------

In Topic 17 (:cite:`SeeligNotebooks`), Seelig documents a classical 7-step compass-and-straightedge procedure titled *'FIVE CIRCLE CONSTRUCTION :term:`ELLIPSE`'* inside a bounding box of semi-axes :math:`a` and :math:`b`, locating major-axis centers :math:`C_2, C_3` and minor-axis centers :math:`C_1, C_4, C_5` so that the circular end-caps of radius :math:`r = |C_2 P|` join smoothly with the broad top/bottom arcs.

In Folio 4, he derives the exact analytic relations among focal distance :math:`F`, directrix distance :math:`d = a/e`, eccentricity :math:`e`, semi-latus rectum :math:`p = b^2/a`, and the :term:`geometric mean` relation :math:`V = a = \sqrt{d F}`.

Key Algebraic Identities
------------------------

.. math::

   \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1, \qquad r_1 + r_2 = 2 a, \qquad V = a = \sqrt{d \cdot F}, \qquad L = \frac{2 b^2}{a}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0118–0121``, 4 scanned manuscript pages in ``resources/seelig/17_ellipse``)
   * - **Euclid's Elements**
     - :ref:`I.47`, :ref:`VI.13` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``General Reference`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.17" [label="F.17\nEllipse", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-17/index.html"];
       "F.1" [label="F.1\nAlbert's Parabola", fillcolor="#90ee90", color="#2e8b57", URL="../f-01/index.html"];
       "F.1" -> "F.17";
       "F.10" [label="F.10\nCircles and Geometric Mean", fillcolor="#90ee90", color="#2e8b57", URL="../f-10/index.html"];
       "F.10" -> "F.17";
   }

**Prerequisites**: :ref:`F.1 Albert's Parabola <f-01>`, :ref:`F.10 Circles and Geometric Mean <f-10>`

.. toctree::
   :hidden:

   folios
   code
