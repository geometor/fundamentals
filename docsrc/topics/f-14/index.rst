:order: 14
:type: topic
:category: Algebraic & Coordinate Systems
:tags: conway, barycentric, brocard, altitudes, stewart

.. _f-14:

====================
F.14 Conway Notation
====================

*John H. Conway's Algebraic Triangle Symbols, Brocard Angle, and Altitude Partitions*

.. enunciation::

   In John H. Conway's triangle notation, setting S = 2K (twice the area of triangle ABC), S_omega = (a^2 + b^2 + c^2)/2, and S_A = (b^2 + c^2 - a^2)/2, S_B = (c^2 + a^2 - b^2)/2, S_C = (a^2 + b^2 - c^2)/2 reduces trigonometric and barycentric identities to polynomial expressions satisfying S_B S_C + S_C S_A + S_A S_B = S^2.

.. figure:: f-14.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.14 (Conway Notation)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   H = orthocenter(A, B, C)
   O = circumcenter(A, B, C)
   G = centroid(A, B, C)
   Euler = line(O, H)

Mathematical Synthesis
----------------------

:person:`John H. Conway <conway>`'s algebraic notation (:term:`Conway triangle notation`) is the primary symbolic language used across Seelig's notebooks and :person:`Paul Yiu <yiu>`'s *Introduction to the Geometry of the Triangle* (:cite:`Yiu2001`, :cite:`SeeligNotebooks`).

In Folios 1–2, Seelig evaluates all Conway invariants on his canonical reference triangle :math:`(a, b, c) = (5, 6, 7)`: :math:`K = 6\sqrt{6}`, :math:`S = 12\sqrt{6}`, :math:`S_\omega = 55`, :math:`S_A = 30`, :math:`S_B = 19`, :math:`S_C = 6`, :term:`altitude <orthocenter>` :math:`J = h_c = \frac{12\sqrt{6}}{7}`, projection :math:`I = \frac{30}{7}`, :math:`y`-intercept :math:`N = \frac{84}{19}\sqrt{6}`, and fractional base splits :math:`k_c = \frac{30}{49}` and :math:`k_c' = \frac{19}{49}`.

Key Algebraic Identities
------------------------

.. math::

   S = 2 K, \qquad S_\omega = \frac{a^2 + b^2 + c^2}{2} = S \cot\omega, \qquad S_A = \frac{b^2 + c^2 - a^2}{2} = b c \cos\alpha

.. math::

   S^2 = b^2 c^2 - S_A^2 = S_A S_B + S_B S_C + S_C S_A, \qquad S_A S_B S_C = S^2 (S_\omega - 4 R^2)

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0092–0097``, 6 scanned manuscript pages in ``resources/seelig/14_conway-notation``)
   * - **Euclid's Elements**
     - :ref:`II.12`, :ref:`II.13` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(2)`, :ref:`X(3)`, :ref:`X(4)`, :ref:`X(6)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``General Reference``, ``Conway's Conversions``, ``5-6-7 A,B,C``, ``Barycentric`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.14" [label="F.14\nConway Notation", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-14/index.html"];
       "F.3" [label="F.3\nBiquadratic Forms in Heron's Formula", fillcolor="#90ee90", color="#2e8b57", URL="../f-03/index.html"];
       "F.3" -> "F.14";
       "F.21" [label="F.21\nFermat Point", fillcolor="#e0e0e0", color="#777777", URL="../f-21/index.html"];
       "F.14" -> "F.21";
       "F.29" [label="F.29\nInradius", fillcolor="#e0e0e0", color="#777777", URL="../f-29/index.html"];
       "F.14" -> "F.29";
       "F.48" [label="F.48\nVerisimilitude, Corner Subtriangles, and Excircle Homothety", fillcolor="#e0e0e0", color="#777777", URL="../f-48/index.html"];
       "F.14" -> "F.48";
       "F.50" [label="F.50\nAltitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-50/index.html"];
       "F.14" -> "F.50";
       "F.52" [label="F.52\nHomogeneous Barycentric Coordinates", fillcolor="#e0e0e0", color="#777777", URL="../f-52/index.html"];
       "F.14" -> "F.52";
       "F.55" [label="F.55\nCompass Constructions and Angle-to-Side Triangle Reconstruction", fillcolor="#e0e0e0", color="#777777", URL="../f-55/index.html"];
       "F.14" -> "F.55";
   }

**Prerequisites**: :ref:`F.3 Biquadratic Forms in Heron's Formula <f-03>`

**Required for**: :ref:`F.21 Fermat Point <f-21>`, :ref:`F.29 Inradius <f-29>`, :ref:`F.48 Verisimilitude, Corner Subtriangles, and Excircle Homothety <f-48>`, :ref:`F.50 Altitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem <f-50>`, :ref:`F.52 Homogeneous Barycentric Coordinates <f-52>`, :ref:`F.55 Compass Constructions and Angle-to-Side Triangle Reconstruction <f-55>`

.. toctree::
   :hidden:

   folios
   code
