:order: 16
:type: topic
:category: Projective & Harmonic Geometry
:tags: dalembert, monge, similitude, projective, apollonius

.. _f-16:

=========================
F.16 d'Alembert's Theorem
=========================

*Monge–d'Alembert Collinearity of the Six Centers of Similitude of Three Circles*

.. enunciation::

   Given three circles of distinct radii in the plane, their six pairwise internal and external centers of similitude lie by threes on four projective lines L_{+++}, L_{--+}, L_{-+-}, and L_{+--} (the Monge–d'Alembert similitude axes).

.. figure:: f-16.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.16 (d'Alembert's Theorem)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O_1 : Point
   R_1 : Point
   O_2 : Point
   R_2 : Point
   O_3 : Point
   =====
   C_1 = circle(O_1, R_1)
   C_2 = circle(O_2, R_2)
   C_3 = circle(O_3, R_3)
   S_12 = external_similitude(C_1, C_2)
   S_23 = external_similitude(C_2, C_3)
   dAlembert_axis = line(S_12, S_23)

Mathematical Synthesis
----------------------

Building on Topic 05 (:ref:`F.5 <f-05>`), Seelig's multi-color constructions in Topic 16 (:cite:`SeeligNotebooks`) illustrate the theorem of :person:`d'Alembert <dalembert>` and Gaspard Monge: for three circles :math:`\Gamma_A, \Gamma_B, \Gamma_C`, the three external :term:`centers of similitude` :math:`S_{\text{EX }AB}, S_{\text{EX }AC}, S_{\text{EX }BC}` are collinear on axis :math:`L_{+++}`, while each external center is collinear with the two complementary internal centers on :math:`L_{--+}, L_{-+-}, L_{+--}`.

In Folios 3–4, Seelig connects these four similitude axes to Gergonne's solution of the **Problem of :person:`Apollonius <apollonius>`** (finding the 8 circles simultaneously tangent to :math:`\Gamma_A, \Gamma_B, \Gamma_C`) and executes a compass construction of five mutually tangent circles (inner and outer Soddy circles).

Key Algebraic Identities
------------------------

.. math::

   L_{+++}:\; \{S_{\text{EX}\,AB},\, S_{\text{EX}\,BC},\, S_{\text{EX}\,CA}\}, \qquad L_{+--}:\; \{S_{\text{EX}\,AB},\, S_{\text{IN}\,BC},\, S_{\text{IN}\,CA}\}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0114–0117``, 4 scanned manuscript pages in ``resources/seelig/16_dalembert``)
   * - **Euclid's Elements**
     - :ref:`VI.2`, :ref:`VI.4` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Centers of Similitude`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.16" [label="F.16\nd'Alembert's Theorem", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-16/index.html"];
       "F.5" [label="F.5\nCenters of Similitude", fillcolor="#90ee90", color="#2e8b57", URL="../f-05/index.html"];
       "F.5" -> "F.16";
   }

**Prerequisites**: :ref:`F.5 Centers of Similitude <f-05>`

.. toctree::
   :hidden:

   folios
   code
