:order: 30
:type: topic
:category: Polygons, Tessellations & Special Triangles
:tags: isosceles, cubic, cardano, newton, heron

.. _f-30:

========================
F.30 Isosceles Triangles
========================

*Perimeter-Area Cubic, Cardano's Depressed Cubic, and Newton's Right-Triangle Formula*

.. enunciation::

   An isosceles triangle of given semiperimeter s and area K has half-base x = c/2 governed by the cubic 2 s x^3 - s^2 x^2 + K^2 = 0, which under x = y + s/6 reduces to Cardano's depressed cubic y^3 - (s^2/12) y - (s^3/54 - K^2/(2s)) = 0.

.. figure:: f-30.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.30 (Isosceles Triangles)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   M : Point
   =====
   c_base = segment(A, B)
   perp = perpendicular(M, c_base)
   C = point_on(perp)
   a_leg = segment(B, C)
   b_leg = segment(C, A)

Mathematical Synthesis
----------------------

Citing :person:`Baloglou` and :person:`Helfgott` (*Forum Geometricorum* 8, 2008, pp. 13–25, :cite:`BaloglouHelfgott2008`), :person:`Peterson`'s mathematical blog, and :person:`Newton`'s *Universal Arithmetick* (:cite:`NewtonArithmetica`), Seelig investigates how prescribing the semiperimeter :math:`s` and area :math:`K` determines a triangle (:cite:`SeeligNotebooks`). Whereas a right triangle has a linear hypotenuse formula :math:`c = s - K/s` (Newton), an :term:`isosceles triangle` with legs :math:`a = b = s - x` and half-base :math:`x = c/2` satisfies :math:`h = \sqrt{s(s-2x)}` and :math:`K = x\sqrt{s(s-2x)}`, leading to the cubic :math:`2sx^3 - s^2 x^2 + K^2 = 0`.

Applying the Tschirnhaus shift :math:`x = y + s/6` (with :math:`a = -s/2, b = 0, c = K^2/(2s)`), Seelig reduces the equation to :person:`Cardano`'s depressed cubic :math:`y^3 + py + q = 0` with :math:`p = -s^2/12` and :math:`q = -s^3/54 + K^2/(2s)`, analyzing the discriminant threshold :math:`K_{\max} = s^2/(3\sqrt{3})` achieved at the :term:`equilateral triangle` (:math:`x = s/3`).

Key Algebraic Identities
------------------------

.. math::

   a = b = s - x, \qquad x = \frac{c}{2}, \qquad K = x\sqrt{s(s - 2x)} \implies 2 s x^3 - s^2 x^2 + K^2 = 0

.. math::

   x = y + \frac{s}{6} \implies y^3 - \frac{s^2}{12} y + \left(\frac{K^2}{2s} - \frac{s^3}{54}\right) = 0, \qquad c_{\text{right}} = s - \frac{K}{s}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0210–0214``, 5 scanned manuscript pages in ``resources/seelig/30_isosceles``)
   * - **Euclid's Elements**
     - :ref:`I.5`, :ref:`I.6` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.1`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Isosceles Triangle``, ``Right Triangle`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.30" [label="F.30\nIsosceles Triangles", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-30/index.html"];
       "F.3" [label="F.3\nBiquadratic Forms in Heron's Formula", fillcolor="#90ee90", color="#2e8b57", URL="../f-03/index.html"];
       "F.3" -> "F.30";
   }

**Prerequisites**: :ref:`F.3 Biquadratic Forms in Heron's Formula <f-03>`

.. toctree::
   :hidden:

   folios
   code
