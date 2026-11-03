:order: 19
:type: topic
:category: Triangle Centers & Classical Lines
:tags: incircle, inradius, sangaku, hyperbolic-functions

.. _f-19:

============================
F.19 Equal Incircles Theorem
============================

*Japanese Sangaku Ray-Fan Theorem Proved via Hyperbolic Tangents*

.. enunciation::

   If a fan of rays from apex P to a baseline cuts triangle ABC into consecutive subtriangles whose incircles have equal radii r_1 = r_2 = ... = r_n = r, then the ray angles gamma_n with the altitude PR (of height h) follow the hyperbolic progression tan(gamma_n) = sinh(a + n*b) with tanh(b/2) = r/(h - r), so overlapping pairs of subtriangles also have equal incircles.

.. figure:: f-19.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.19 (Equal Incircles Theorem)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   I = incenter(A, B, C)
   T_C = foot(I, line(A, B))
   incircle = circle(I, T_C)

Mathematical Synthesis
----------------------

The **Equal Incircles Theorem** is a celebrated Japanese Sangaku theorem: if rays from apex :g:`C` to base :g:`A` :g:`B` partition :math:`\triangle ABC` into subtriangles with equal inradii :math:`r`, then the incircles of the triangles formed by every second ray (or every :math:`k`-th ray) are also equal.

In Topic 19 (:cite:`SeeligNotebooks`), Seelig gives an elegant proof (marked *'interesting!!!'*): using similar triangles :math:`\triangle OWX \sim \triangle PQX` at height :math:`h - r`, he derives :math:`(h - r)(\tan\gamma_{n+1} - \tan\gamma_n) = r(\sec\gamma_n + \sec\gamma_{n+1})` and shows that the hyperbolic parameterization :math:`\tan\gamma_n = \sinh(a + nb), \sec\gamma_n = \cosh(a + nb)` satisfies this recurrence identically with constant step :math:`\tanh(b/2) = \frac{r}{h-r}`.

Key Algebraic Identities
------------------------

.. math::

   (h - r)(\tan\gamma_{n+1} - \tan\gamma_n) = r(\sec\gamma_n + \sec\gamma_{n+1})

.. math::

   \tan\gamma_n = \sinh(a + n b), \qquad \sec\gamma_n = \cosh(a + n b), \qquad \frac{r}{h - r} = \tanh\frac{b}{2}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0125–0126``, 2 scanned manuscript pages in ``resources/seelig/19_equal-incircle-theorem``)
   * - **Euclid's Elements**
     - :ref:`IV.4`, :ref:`VI.4` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Incircle-Incenter`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.19" [label="F.19\nEqual Incircles Theorem", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-19/index.html"];
       "F.4" [label="F.4\nCarnot's Theorem", fillcolor="#90ee90", color="#2e8b57", URL="../f-04/index.html"];
       "F.4" -> "F.19";
       "F.28" [label="F.28\nIncenter", fillcolor="#90ee90", color="#2e8b57", URL="../f-28/index.html"];
       "F.28" -> "F.19";
   }

**Prerequisites**: :ref:`F.4 Carnot's Theorem <f-04>`, :ref:`F.28 Incenter <f-28>`

.. toctree::
   :hidden:

   folios
   code
