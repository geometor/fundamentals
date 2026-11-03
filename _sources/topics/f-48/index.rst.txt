:order: 48
:type: topic
:category: Circle Inversion, Coaxial & Radical Systems
:tags: similitude, incircle, excircle, homothety, stewart

.. _f-48:

================================================================
F.48 Verisimilitude, Corner Subtriangles, and Excircle Homothety
================================================================

*Incircle Tangent Subtriangles (r_A + r_B + r_C = r), Excircle Similitude, and Cevian Bounds*

.. enunciation::

   If lines parallel to the sides of triangle ABC are drawn tangent to the incircle, the three corner subtriangles are homothetic to ABC with scale factors x/s, y/s, z/s (where x = s - a, y = s - b, z = s - c), so their inradii satisfy r_A + r_B + r_C = r.

.. figure:: f-48.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.48 (Verisimilitude, Corner Subtriangles, and Excircle Homothety)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   I = incenter(A, B, C)
   T_A = foot(I, line(B, C))
   c_in = circle(I, T_A)
   P_A = intersection(segment(A, I), c_in)
   l_tan = perpendicular(P_A, line(A, I))

Mathematical Synthesis
----------------------

In this nine-folio investigation (:cite:`SeeligNotebooks`), Seelig explores homothetic scaling (*verisimilitude*) across three connected settings. First (Folios 1–4), drawing tangents to the :term:`incircle` parallel to :math:`BC, CA, AB` cuts off three corner subtriangles homothetic to :math:`\triangle ABC` from vertices :g:`A`, :g:`B`, :g:`C`. Because the distance from :g:`A` to the :term:`incircle <incenter>` touchpoint is :math:`x = s-a`, the corner subtriangle at :g:`A` has semiperimeter :math:`s_A = x = s-a`! Consequently its scale factor is :math:`x/s`, its inradius is :math:`r_A = r(x/s)`, its area is :math:`K_A = K(x/s)^2`, and summing over all three corners gives the remarkable invariant :math:`r_A + r_B + r_C = r\frac{x+y+z}{s} = r`.

Second (`FWS 2014/9/7`, Folios 5–6), Seelig analyzes *:term:`CENTERS OF SIMILITUDE`: :term:`EXCIRCLES <excircle>`*, treating vertex :g:`A` as the external :term:`center of similitude` of the incircle :math:`(I, r)` and the :math:`A`-excircle :math:`(I_A, R_A)` separated by :math:`d = |II_A|`, deriving :math:`|AI| = d\frac{r}{R_A - r}` and :math:`|AI_A| = d\frac{R_A}{R_A - r}`. Third (Folios 7–9), he solves :term:`Stewart's theorem` as a quadratic in :math:`k` for a prescribed :term:`cevian <Ceva's theorem>` length :math:`d = 4` in :math:`(a,b,c) = (7,5,10)`, finding the two roots :math:`k \in \{0.613, 0.147\}` above the :term:`altitude <orthocenter>` minimum :math:`d_{\min} = h_c = 3.25`.

Key Algebraic Identities
------------------------

.. math::

   s_A = x = s - a, \qquad r_A = r\frac{x}{s}, \qquad K_A = K\left(\frac{x}{s}\right)^2, \qquad r_A + r_B + r_C = r\frac{x + y + z}{s} = r

.. math::

   |AI| = |II_A|\frac{r}{r_a - r}, \qquad |AI_A| = |II_A|\frac{r_a}{r_a - r}, \qquad c^2 k^2 - (c^2 + a^2 - b^2) k + (a^2 - d^2) = 0

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0306–0314``, 9 scanned manuscript pages in ``resources/seelig/48_verisimilitude``)
   * - **Euclid's Elements**
     - :ref:`IV.4`, :ref:`VI.4` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.5`, :ref:`G.8`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(55)`, :ref:`X(56)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Centers of Similitude``, ``Incircle-Incenter``, ``Stewart's Theorem`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.48" [label="F.48\nVerisimilitude, Corner Subtriangles, and Excircle Homothety", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-48/index.html"];
       "F.5" [label="F.5\nCenters of Similitude", fillcolor="#90ee90", color="#2e8b57", URL="../f-05/index.html"];
       "F.5" -> "F.48";
       "F.14" [label="F.14\nConway Notation", fillcolor="#90ee90", color="#2e8b57", URL="../f-14/index.html"];
       "F.14" -> "F.48";
       "F.29" [label="F.29\nInradius", fillcolor="#90ee90", color="#2e8b57", URL="../f-29/index.html"];
       "F.29" -> "F.48";
       "F.46" [label="F.46\nStewart's Theorem", fillcolor="#90ee90", color="#2e8b57", URL="../f-46/index.html"];
       "F.46" -> "F.48";
   }

**Prerequisites**: :ref:`F.5 Centers of Similitude <f-05>`, :ref:`F.14 Conway Notation <f-14>`, :ref:`F.29 Inradius <f-29>`, :ref:`F.46 Stewart's Theorem <f-46>`

.. toctree::
   :hidden:

   folios
   code
