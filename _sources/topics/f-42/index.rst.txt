:order: 42
:type: topic
:category: Polygons, Tessellations & Special Triangles
:tags: pythagorean-triples, altitude, right-triangle, euclid, harmonic

.. _f-42:

==============================================
F.42 Altitude of a Pythagorean Triple Triangle
==============================================

*Inverse Pythagorean Theorem, Hypotenuse Projections, and Incircle Touchpoint Distinction*

.. enunciation::

   In a right triangle with legs a, b and hypotenuse c, the altitude h_c = a b / c satisfies the Inverse Pythagorean Theorem 1/h_c^2 = 1/a^2 + 1/b^2 and divides the hypotenuse into projections u = b^2/c and y = a^2/c with h_c^2 = u y.

.. figure:: f-42.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.42 (Altitude of a Pythagorean Triple Triangle)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   c_hyp = segment(A, B)
   H_C = foot(C, line(A, B))
   h_c = segment(C, H_C)
   I = incenter(A, B, C)
   T_C = foot(I, line(A, B))

Mathematical Synthesis
----------------------

Titled *The :term:`Altitude <orthocenter>` of a :term:`Pythagorean Triple` Triangle* (:cite:`SeeligNotebooks`), this four-folio study examines the right-triangle altitude :g:`h_c` dropped from the right angle :g:`C` to the hypotenuse :g:`A` :g:`B` (:person:`Euclid` *Elements* :ref:`VI.8`). Equating twice the area :math:`2K = ab = ch_c` gives :math:`h_c = ab/c` and the Inverse Pythagorean Theorem :math:`\frac{1}{h_c^2} = \frac{a^2+b^2}{a^2 b^2} = \frac{1}{a^2} + \frac{1}{b^2}`, while the hypotenuse projections :math:`u = b^2/c` and :math:`y = a^2/c` satisfy the :term:`geometric mean` identity :math:`h_c = \sqrt{uy}`.

On Folio 3, Seelig highlights a classic geometric pitfall inside a bold warning box: the :term:`cevian <Ceva's theorem>` from :g:`C` to the :term:`incircle` touchpoint :g:`T_C` (which splits :math:`c` into :math:`s-a` and :math:`s-b` with :math:`K = (s-a)(s-b)`) does *not* coincide with the perpendicular altitude foot :g:`H_C` (*"CT_c is not \perp to BA"*) unless :math:`a = b`.

Key Algebraic Identities
------------------------

.. math::

   h_c = \frac{a b}{c}, \qquad \frac{1}{h_c^2} = \frac{1}{a^2} + \frac{1}{b^2}, \qquad u = \frac{b^2}{c},\; y = \frac{a^2}{c},\; h_c^2 = u y

.. math::

   |A T_C| = s - a \neq u = \frac{b^2}{c} \quad (a \neq b), \qquad K = (s - a)(s - b) = \frac{a b}{2}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0267–0270``, 4 scanned manuscript pages in ``resources/seelig/42_pythagorean-triples``)
   * - **Euclid's Elements**
     - :ref:`I.47`, :ref:`VI.8` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.4`, :ref:`G.11`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(4)`, :ref:`X(7)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Pythagorean Triples``, ``Right Triangle``, ``Altitudes`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.42" [label="F.42\nAltitude of a Pythagorean Triple Triangle", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-42/index.html"];
       "F.10" [label="F.10\nCircles and Geometric Mean", fillcolor="#90ee90", color="#2e8b57", URL="../f-10/index.html"];
       "F.10" -> "F.42";
       "F.29" [label="F.29\nInradius", fillcolor="#90ee90", color="#2e8b57", URL="../f-29/index.html"];
       "F.29" -> "F.42";
       "F.33" [label="F.33\nEuclidean (m, n) Generators", fillcolor="#90ee90", color="#2e8b57", URL="../f-33/index.html"];
       "F.33" -> "F.42";
       "F.50" [label="F.50\nAltitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-50/index.html"];
       "F.42" -> "F.50";
   }

**Prerequisites**: :ref:`F.10 Circles and Geometric Mean <f-10>`, :ref:`F.29 Inradius <f-29>`, :ref:`F.33 Euclidean (m, n) Generators <f-33>`

**Required for**: :ref:`F.50 Altitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem <f-50>`

.. toctree::
   :hidden:

   folios
   code
