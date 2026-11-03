:order: 1
:type: topic
:category: Conics & Analytic Loci
:tags: parabola, conics, normal, tangent, cubic

.. _f-01:

=====================
F.1 Albert's Parabola
=====================

*Tangent, Normal, and Depressed Cubic for Minimum Distance to a Parabola*

.. enunciation::

   Given a parabola y = x^2 and a point P = (P_x, P_y) on it, the tangent line T and normal line N at P satisfy y = 2 P_x x - P_x^2 and y = -x/(2 P_x) + P_x^2 + 1/2; requiring N to pass through (M, 0) yields the depressed cubic P_x^3 + (1/2) P_x - M/2 = 0.

.. figure:: f-01.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.1 (Albert's Parabola)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   V : Point
   F : Point
   directrix : Line
   P : Point
   =====
   Q = foot(P, directrix)
   s_fp = segment(F, P)
   s_pq = segment(P, Q)
   tangent = bisector(F, P, Q)

Mathematical Synthesis
----------------------

In his April 2015 study *Albert's :term:`Parabola` Problem* (Attempts #2 and #3, :cite:`SeeligNotebooks`), :person:`Fred W. Seelig <seelig>` investigates the tangent :g:`tangent` and normal :g:`N` to a :term:`parabola` in two coordinate frames: the vertex frame :math:`y = x^2` and the shifted directrix frame :math:`y = x^2 + 1` (where the :g:`directrix` is :math:`y = 0`, vertex :g:`V` is :math:`(0, 1)`, and focus :g:`F` is :math:`(0, 2)`).

For :math:`y = x^2` at :g:`P` :math:`= (P_x, P_x^2)`, the tangent :g:`T` has double-intercept form :math:`x/(P_x/2) + y/(-P_x^2) = 1`, while the normal :g:`N` has :math:`x`-intercept :math:`M = 2 P_x (P_x^2 + 1/2)`. Setting :math:`M = 4` produces the depressed cubic :math:`P_x^3 + \frac{1}{2}P_x - 2 = 0`, which simultaneously governs the minimum distance from a fixed point :math:`(M, 0)` on the directrix to a point :g:`Q` on the parabola.

Key Algebraic Identities
------------------------

.. math::

   T:\; y = 2 P_x x - P_x^2, \qquad N:\; y = -\frac{x}{2 P_x} + \left(P_x^2 + \frac{1}{2}\right)

.. math::

   P_x^3 + \frac{1}{2} P_x - \frac{M}{2} = 0, \qquad r = \frac{P_x + 4 P_x^3}{4}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0001–0002``, 2 scanned manuscript pages in ``resources/seelig/01_alberts-parabola``)
   * - **Euclid's Elements**
     - :ref:`I.11`, :ref:`I.12` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`, :ref:`G.4`
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
       "F.1" [label="F.1\nAlbert's Parabola", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-01/index.html"];
       "F.17" [label="F.17\nEllipse", fillcolor="#e0e0e0", color="#777777", URL="../f-17/index.html"];
       "F.1" -> "F.17";
       "F.37" [label="F.37\nEuler's Inradius Parabola", fillcolor="#e0e0e0", color="#777777", URL="../f-37/index.html"];
       "F.1" -> "F.37";
   }

**Required for**: :ref:`F.17 Ellipse <f-17>`, :ref:`F.37 Euler's Inradius Parabola <f-37>`

.. toctree::
   :hidden:

   folios
   code
