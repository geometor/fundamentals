:order: 47
:type: topic
:category: Algebraic & Coordinate Systems
:tags: coordinates, cevian, heronian, matrices, ceva

.. _f-47:

================================
F.47 The UVW Coordinate Triangle
================================

*Altitude-Origin Cartesian Frame A(-U,0), B(W,0), C(0,V) and 2x2 Cevian Trace Matrices*

.. enunciation::

   Placing the altitude foot H_C at the origin (0, 0) with A = (-U, 0), B = (W, 0), and C = (0, V) parameterizes any triangle by three numbers (U, V, W) with a = sqrt(V^2 + W^2), b = sqrt(U^2 + V^2), c = U + W, and reduces the cevian traces D, E, F through P(p, q) to explicit 2x2 rational matrix formulas.

.. figure:: f-47.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.47 (The UVW Coordinate Triangle)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   H_C : Point
   A : Point
   B : Point
   C : Point
   P : Point
   =====
   s_ab = segment(A, B)
   s_ch = segment(C, H_C)
   D = intersection(line(B, C), line(A, P))
   E = intersection(line(C, A), line(B, P))
   F = intersection(line(A, B), line(C, P))

Mathematical Synthesis
----------------------

Across 11 folios (:cite:`SeeligNotebooks`), Seelig develops his signature coordinate apparatus: *The UVW Triangle*. By placing the :term:`altitude <orthocenter>` foot :g:`H_C` at the Cartesian origin :math:`(0,0)` so that :g:`A` :math:`= (-U, 0)`, :g:`B` :math:`= (W, 0)`, and :g:`C` :math:`= (0, V)`, every side and line equation enters double-intercept form (:math:`AC: -x/U + y/V = 1` and :math:`BC: x/W + y/V = 1`). When :math:`(U, V)` and :math:`(V, W)` are chosen as legs of two :term:`Pythagorean triples <Pythagorean triple>` sharing height :math:`V`—such as :math:`(U,V,W) = (5,12,16)` on Folios 3–4—the juxtaposed triangle has integer sides :math:`(a,b,c) = (20, 13, 21)` and integer area :math:`K = 126` (a Heronian triangle).

Given an interior perspector :g:`P` :math:`= (p, q)`, Seelig formulates :math:`2\times 2` matrix systems for the :term:`cevian <Ceva's theorem>` traces :g:`D` :math:`= BC \cap AP`, :g:`E` :math:`= CA \cap BP`, and :g:`F` :math:`= AB \cap CP`, testing the formulas on :math:`(U,V,W,p,q) = (8,8,16,4,4)` to obtain exact rational traces :math:`D = (6.4, 4.8), E = (-2, 6), F = (8, 0)` and verifying :person:`Ceva`'s ratio product :math:`1`.

Key Algebraic Identities
------------------------

.. math::

   A = (-U, 0), \qquad B = (W, 0), \qquad C = (0, V), \qquad a^2 = V^2 + W^2,\; b^2 = U^2 + V^2,\; c = U + W

.. math::

   F_x = \frac{p V}{V - q}, \qquad D = \left(\frac{W V (U + p)}{V(U + W) + q W},\; \frac{V q (U + W)}{V(U + W) + q W}\right)

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0295–0305``, 11 scanned manuscript pages in ``resources/seelig/47_u-v-w``)
   * - **Euclid's Elements**
     - :ref:`I.47`, :ref:`VI.2` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.4`, :ref:`G.5`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(2)`, :ref:`X(4)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``UVW Triangle``, ``Ceva & Menelaus`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.47" [label="F.47\nThe UVW Coordinate Triangle", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-47/index.html"];
       "F.7" [label="F.7\nCeva and Menelaus", fillcolor="#90ee90", color="#2e8b57", URL="../f-07/index.html"];
       "F.7" -> "F.47";
       "F.35" [label="F.35\nObtuse and Acute Triangles", fillcolor="#90ee90", color="#2e8b57", URL="../f-35/index.html"];
       "F.35" -> "F.47";
       "F.54" [label="F.54\nHP-35s Triangle Program and Coordinate Scripts", fillcolor="#e0e0e0", color="#777777", URL="../f-54/index.html"];
       "F.47" -> "F.54";
   }

**Prerequisites**: :ref:`F.7 Ceva and Menelaus <f-07>`, :ref:`F.35 Obtuse and Acute Triangles <f-35>`

**Required for**: :ref:`F.54 HP-35s Triangle Program and Coordinate Scripts <f-54>`

.. toctree::
   :hidden:

   folios
   code
