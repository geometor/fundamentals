:order: 55
:type: topic
:category: Polygons, Tessellations & Special Triangles
:tags: constructions, vesica-piscis, inradius, conway, trigonometry

.. _f-55:

====================================================================
F.55 Compass Constructions and Angle-to-Side Triangle Reconstruction
====================================================================

*Vesica-Square Drawings and Reconstructing (a, b, c) from Interior Angles Under Scale Normalization*

.. enunciation::

   Given the three interior angles (alpha, beta, gamma) of a triangle normalized to unit area K = 1 (so s = 1/r), the Conway intouch segments x = s - a = r cot(alpha/2), y = s - b = r cot(beta/2), and z = s - c = r cot(gamma/2) determine the side lengths a = y + z, b = z + x, and c = x + y = 2 s - (a + b).

.. figure:: f-55.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.55 (Compass Constructions and Angle-to-Side Triangle Reconstruction)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   I = incenter(A, B, C)
   T_A = foot(I, line(B, C))
   T_B = foot(I, line(C, A))
   T_C = foot(I, line(A, B))
   c_in = circle(I, T_A)

Mathematical Synthesis
----------------------

Closing the 55-topic archive (:cite:`SeeligNotebooks`), this five-folio folder pairs two pure compass-and-straightedge drawings (`drawings-001`–`002`, showing overlapping circles, a :term:`vesica piscis`, and an inscribed square with perpendicular axes) with a three-page analytic study (`misc-2-001`–`003`) on reconstructing a triangle's side lengths :math:`(a,b,c)` and vertex coordinates :math:`(A,B,C)` from its interior angles :math:`(\alpha, \beta, \gamma)` under three alternative scale normalizations.

Under the unit-area normalization :math:`K = r s = 1` (so :math:`s = 1/r`), Seelig expresses the :term:`Conway triangle notation` intouch segments via the half-angle cotangents :math:`x = s - a = r\cot(\alpha/2)`, :math:`y = s - b = r\cot(\beta/2)`, and :math:`z = s - c = r\cot(\gamma/2)`, recovering :math:`c = (s-a) + (s-b) = 2s - (a+b)` and :math:`r^2 = \frac{1}{\cot(\alpha/2) + \cot(\beta/2) + \cot(\gamma/2)}`.

Key Algebraic Identities
------------------------

.. math::

   s - a = r\cot\frac{\alpha}{2}, \qquad s - b = r\cot\frac{\beta}{2}, \qquad s - c = r\cot\frac{\gamma}{2}

.. math::

   K = r s = 1 \implies s = \frac{1}{r}, \qquad c = (s - a) + (s - b) = 2 s - (a + b)

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0349–0353``, 5 scanned manuscript pages in ``resources/seelig/55_misc``)
   * - **Euclid's Elements**
     - :ref:`I.1`, :ref:`IV.4` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.1`, :ref:`G.8`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(7)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``General Reference``, ``Incircle-Incenter`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.55" [label="F.55\nCompass Constructions and Angle-to-Side Triangle Reconstruction", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-55/index.html"];
       "F.14" [label="F.14\nConway Notation", fillcolor="#90ee90", color="#2e8b57", URL="../f-14/index.html"];
       "F.14" -> "F.55";
       "F.29" [label="F.29\nInradius", fillcolor="#90ee90", color="#2e8b57", URL="../f-29/index.html"];
       "F.29" -> "F.55";
       "F.49" [label="F.49\nVesica Piscis and Acute-Obtuse Probability", fillcolor="#90ee90", color="#2e8b57", URL="../f-49/index.html"];
       "F.49" -> "F.55";
   }

**Prerequisites**: :ref:`F.14 Conway Notation <f-14>`, :ref:`F.29 Inradius <f-29>`, :ref:`F.49 Vesica Piscis and Acute-Obtuse Probability <f-49>`

.. toctree::
   :hidden:

   folios
   code
