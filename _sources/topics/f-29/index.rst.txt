:order: 29
:type: topic
:category: Triangle Centers & Classical Circles
:tags: inradius, incircle, conway, gergonne, heron

.. _f-29:

=============
F.29 Inradius
=============

*Special Inradius Values, Conway Intouch Segments, and the Gergonne Point*

.. enunciation::

   The inradius r = K / s = (1/2) sqrt(((b+c-a)(c+a-b)(a+b-c))/(a+b+c)) = 4 R sin(alpha/2) sin(beta/2) sin(gamma/2) takes integer values on primitive Pythagorean triples and partitions the perimeter into Conway segments x, y, z whose touchpoints T_A, T_B, T_C concur at the Gergonne point Ge = X(7).

.. figure:: f-29.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.29 (Inradius)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   I = incenter(A, B, C)
   T_A = foot(I, line(B, C))
   T_B = foot(I, line(C, A))
   T_C = foot(I, line(A, B))
   Ge = intersection(line(A, T_A), line(B, T_B))
   c_in = circle(I, T_A)

Mathematical Synthesis
----------------------

Seelig's three-folio dossier on the :term:`inradius` (:cite:`SeeligNotebooks`) opens with his master reference sheet *:term:`Inradius <incenter>` / Special Inradius Values*, pairing the Heron radical :math:`r = \frac{1}{2}\sqrt{\frac{(b+c-a)(c+a-b)(a+b-c)}{a+b+c}} = \frac{K}{s}` and the trigonometric product :math:`r = 4R\sin\frac{\alpha}{2}\sin\frac{\beta}{2}\sin\frac{\gamma}{2}` with a five-row benchmark table: :term:`Pythagorean triples <Pythagorean triple>` :math:`(3,4,5)\mapsto r=1`, :math:`(5,12,13)\mapsto r=2`, :math:`(8,15,17)\mapsto r=3`, and :math:`(7,24,25)\mapsto r=3`; the :math:`30^\circ\text{--}60^\circ\text{--}90^\circ` triangle; and the :term:`golden triangle` :math:`(\phi b, \phi b, b)` with :math:`r = \frac{b}{2}\sqrt{5-2\sqrt{5}}`.

In Folios 2–3, Seelig connects :term:`Conway triangle notation` (:math:`x = s-a, y = s-b, z = s-c`) to the :term:`incircle` contact points :g:`T_A`, :g:`T_B`, :g:`T_C` and their concurrency at the :term:`Gergonne point` :g:`Ge` (:ref:`X(7)`), verifying :math:`r = \sqrt{xyz/(x+y+z)}` on a measured scalene drawing (:math:`a=28.3, b=19, c=30.8, s=39, K=263`) and on the canonical :math:`(5,6,7)` triangle (:math:`x=4, y=3, z=2, s=9, r = \frac{2\sqrt{6}}{3}`).

Key Algebraic Identities
------------------------

.. math::

   r = \frac{K}{s} = \frac{1}{2}\sqrt{\frac{(b+c-a)(c+a-b)(a+b-c)}{a+b+c}} = \sqrt{\frac{x y z}{x + y + z}}

.. math::

   r = 4 R \sin\frac{\alpha}{2}\sin\frac{\beta}{2}\sin\frac{\gamma}{2}, \qquad x = s - a,\; y = s - b,\; z = s - c

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0207–0209``, 3 scanned manuscript pages in ``resources/seelig/29_inradius``)
   * - **Euclid's Elements**
     - :ref:`IV.4` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.8`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(7)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Incircle-Incenter``, ``General Reference`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.29" [label="F.29\nInradius", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-29/index.html"];
       "F.14" [label="F.14\nConway Notation", fillcolor="#90ee90", color="#2e8b57", URL="../f-14/index.html"];
       "F.14" -> "F.29";
       "F.28" [label="F.28\nIncenter", fillcolor="#90ee90", color="#2e8b57", URL="../f-28/index.html"];
       "F.28" -> "F.29";
       "F.32" [label="F.32\nMarkowski's Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-32/index.html"];
       "F.29" -> "F.32";
       "F.33" [label="F.33\nEuclidean (m, n) Generators", fillcolor="#e0e0e0", color="#777777", URL="../f-33/index.html"];
       "F.29" -> "F.33";
       "F.37" [label="F.37\nEuler's Inradius Parabola", fillcolor="#e0e0e0", color="#777777", URL="../f-37/index.html"];
       "F.29" -> "F.37";
       "F.42" [label="F.42\nAltitude of a Pythagorean Triple Triangle", fillcolor="#e0e0e0", color="#777777", URL="../f-42/index.html"];
       "F.29" -> "F.42";
       "F.48" [label="F.48\nVerisimilitude, Corner Subtriangles, and Excircle Homothety", fillcolor="#e0e0e0", color="#777777", URL="../f-48/index.html"];
       "F.29" -> "F.48";
       "F.55" [label="F.55\nCompass Constructions and Angle-to-Side Triangle Reconstruction", fillcolor="#e0e0e0", color="#777777", URL="../f-55/index.html"];
       "F.29" -> "F.55";
   }

**Prerequisites**: :ref:`F.14 Conway Notation <f-14>`, :ref:`F.28 Incenter <f-28>`

**Required for**: :ref:`F.32 Markowski's Theorem <f-32>`, :ref:`F.33 Euclidean (m, n) Generators <f-33>`, :ref:`F.37 Euler's Inradius Parabola <f-37>`, :ref:`F.42 Altitude of a Pythagorean Triple Triangle <f-42>`, :ref:`F.48 Verisimilitude, Corner Subtriangles, and Excircle Homothety <f-48>`, :ref:`F.55 Compass Constructions and Angle-to-Side Triangle Reconstruction <f-55>`

.. toctree::
   :hidden:

   folios
   code
