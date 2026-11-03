:order: 54
:type: topic
:category: Algebraic & Coordinate Systems
:tags: scripts, hp-35s, barycentric, coordinates, matrices

.. _f-54:

===================================================
F.54 HP-35s Triangle Program and Coordinate Scripts
===================================================

*BARY 2 CAR and CAR 2 BARY Matrix Routines, Register Map A–Z, and 5-6-7 Verification*

.. enunciation::

   In the canonical frame A = (0, 0), B = (M, 0), C = (I, J), the forward and inverse barycentric-Cartesian transformations BARY 2 CAR and CAR 2 BARY are given by P = M U + I V, Q = J V and V = Q / J, U = (P - I V) / M, T = 1 - (U + V).

.. figure:: f-54.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.54 (HP-35s Triangle Program and Coordinate Scripts)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   P : Point
   =====
   s_ab = segment(A, B)
   H_C = foot(C, line(A, B))
   H_P = foot(P, line(A, B))

Mathematical Synthesis
----------------------

Dated September 10, 2014 with ``LAST EDIT May 7, 2015`` (:cite:`SeeligNotebooks`), these two folios document Seelig's ``HP-35s [T] [Triangle]`` calculator program specification. Placing :g:`A` at :math:`(0,0)`, :g:`B` at :math:`(M,0)`, and :g:`C` at :math:`(I,J)`, the program maps normalized :term:`homogeneous barycentric coordinates` :math:`(T, U, V) = (\lambda_A, \lambda_B, \lambda_C)` to Cartesian coordinates :math:`(P, Q) = (x, y)` via the upper-triangular routine ``BARY 2 CAR``: :math:`P = MU + IV, Q = JV`.

Conversely, the inverse routine ``CAR 2 BARY`` recovers the :term:`barycentric <barycentric coordinates>` weights in three register operations: :math:`V = Q/J`, :math:`U = (P - IV)/M`, and :math:`T = 1 - (U + V)`. Folio 2 records the complete ``A``–``Z`` memory register map of the HP-35s alongside a worked validation on the canonical :math:`(5,6,7)` triangle.

Key Algebraic Identities
------------------------

.. math::

   \text{BARY 2 CAR:}\quad \begin{bmatrix} P \\ Q \end{bmatrix} = \begin{bmatrix} M & I \\ 0 & J \end{bmatrix} \begin{bmatrix} U \\ V \end{bmatrix}, \qquad T + U + V = 1

.. math::

   \text{CAR 2 BARY:}\quad V = \frac{Q}{J}, \qquad U = \frac{P - I V}{M}, \qquad T = 1 - (U + V)

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0347–0348``, 2 scanned manuscript pages in ``resources/seelig/54_scripts``)
   * - **Euclid's Elements**
     - :ref:`VI.2` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.5`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(2)`, :ref:`X(3)`, :ref:`X(4)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Barycentric``, ``5-6-7 A,B,C`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.54" [label="F.54\nHP-35s Triangle Program and Coordinate Scripts", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-54/index.html"];
       "F.47" [label="F.47\nThe UVW Coordinate Triangle", fillcolor="#90ee90", color="#2e8b57", URL="../f-47/index.html"];
       "F.47" -> "F.54";
       "F.52" [label="F.52\nHomogeneous Barycentric Coordinates", fillcolor="#90ee90", color="#2e8b57", URL="../f-52/index.html"];
       "F.52" -> "F.54";
   }

**Prerequisites**: :ref:`F.47 The UVW Coordinate Triangle <f-47>`, :ref:`F.52 Homogeneous Barycentric Coordinates <f-52>`

.. toctree::
   :hidden:

   folios
   code
