:order: 39
:type: topic
:category: Projective & Harmonic Geometry
:tags: pole-polar, projective, trilinear-polar, desargues, harmonic

.. _f-39:

==============================================
F.39 Pole and Polar with Respect to a Triangle
==============================================

*Trilinear Polar Line, Desargues Perspectivity, and Metric Distance Questions*

.. enunciation::

   Given a triangle ABC and a point P with cevian traces A', B', C', the intersections X = BC cap B'C', Y = CA cap C'A', and Z = AB cap A'B' are collinear on the trilinear polar L of the pole P.

.. figure:: f-39.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.39 (Pole and Polar with Respect to a Triangle)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   P : Point
   =====
   A_p = intersection(line(B, C), line(A, P))
   B_p = intersection(line(C, A), line(B, P))
   C_p = intersection(line(A, B), line(C, P))
   X = intersection(line(B, C), line(B_p, C_p))
   Y = intersection(line(C, A), line(C_p, A_p))
   polar = line(X, Y)

Mathematical Synthesis
----------------------

Dated May 6, 2015 (:cite:`SeeligNotebooks`), Seelig's study *POLE & :term:`POLAR <pole and polar>` W.r.t. A TRIANGLE (projective geometry)* constructs the :term:`trilinear polar` :g:`polar` (line :math:`L`) of a perspector/pole :g:`P` with respect to :math:`\triangle ABC`. Drawing the :term:`cevians <Ceva's theorem>` through :g:`P` to their traces :g:`A_p`, :g:`B_p`, :g:`C_p` (:math:`A', B', C'`), the :term:`harmonic conjugates <harmonic conjugate>` :g:`X` :math:`= BC \cap B'C'`, :g:`Y` :math:`= CA \cap C'A'`, and :math:`Z = AB \cap A'B'` are collinear by :person:`Desargues`'s Theorem along the :term:`trilinear <trilinear coordinates>` polar :math:`L`.

In the lower half of the folio, Seelig formulates a program of metric research questions linking projective duality to Euclidean triangle centers: determining the perpendicular distance :math:`d(P, L)` and the distances :math:`OP, IP, OL, IL` from the :term:`circumcenter` :g:`O` and :term:`incenter` :g:`I` to the pole :g:`P` and polar :math:`L` in terms of :term:`barycentric coordinates`.

Key Algebraic Identities
------------------------

.. math::

   P = (u : v : w) \iff L:\; \frac{x}{u} + \frac{y}{v} + \frac{z}{w} = 0

.. math::

   (B, C;\, A', X) = (C, A;\, B', Y) = (A, B;\, C', Z) = -1

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0238–0238``, 1 scanned manuscript page in ``resources/seelig/39_pole-polar``)
   * - **Euclid's Elements**
     - :ref:`VI.2`, :ref:`VI.3` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.5`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(2)`, :ref:`X(3)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Pole & Polar``, ``Harmonic Conjugates`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.39" [label="F.39\nPole and Polar with Respect to a Triangle", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-39/index.html"];
       "F.7" [label="F.7\nCeva and Menelaus", fillcolor="#90ee90", color="#2e8b57", URL="../f-07/index.html"];
       "F.7" -> "F.39";
       "F.25" [label="F.25\nHarmonic Conjugates", fillcolor="#90ee90", color="#2e8b57", URL="../f-25/index.html"];
       "F.25" -> "F.39";
   }

**Prerequisites**: :ref:`F.7 Ceva and Menelaus <f-07>`, :ref:`F.25 Harmonic Conjugates <f-25>`

.. toctree::
   :hidden:

   folios
   code
