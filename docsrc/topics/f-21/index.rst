:order: 21
:type: topic
:category: Triangle Centers & Classical Lines
:tags: fermat-point, torricelli, steiner, optimization, equilateral

.. _f-21:

=================
F.21 Fermat Point
=================

*Torricelli's Equilateral Construction for X(13), 120-Degree Equiangularity, and the Obtuse Threshold*

.. enunciation::

   For any triangle ABC whose largest interior angle is less than 120 degrees, erecting external equilateral triangles BCX_A, CAY_B, ABZ_C on its sides yields concurrent segments AX_A, BY_B, CZ_C that intersect at the Fermat-Torricelli point F = X(13), where <AFB = <BFC = <CFA = 120 degrees and FA + FB + FC is minimized.

.. figure:: f-21.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.21 (Fermat Point)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   C' = outer_equilateral_apex(A, B)
   ABC' = polygon(A, B, C')
   CC' = segment(C, C')
   F = fermat_point(A, B, C)

Mathematical Synthesis
----------------------

Dated July 6, 2011 and citing :person:`Evangelista Torricelli <torricelli>` and David Wells (:cite:`Wells1991`, p. 75; :cite:`SeeligNotebooks`), Seelig constructs the :term:`Fermat point` :g:`F` :math:`= X(13)` by erecting external :term:`equilateral <equilateral triangle>` triangles (such as :g:`ABC'` with apex :g:`C'`) on the sides of :math:`\triangle ABC` and intersecting their circumcircles with the Simpson/Torricelli lines :g:`CC'`.

In Folio 2, Seelig carefully distinguishes between the isogonic :person:`Jakob Steiner <steiner>` / :term:`Torricelli point <Fermat point>` (where sides subtend :math:`120^\circ`) and the true distance-minimizing Fermat point when an interior angle of :math:`\triangle ABC` is :math:`\ge 120^\circ`: in that obtuse regime, the :math:`120^\circ` point moves outside :math:`\triangle ABC` while the minimum of :math:`FA + FB + FC` collapses onto the obtuse vertex itself.

Key Algebraic Identities
------------------------

.. math::

   \angle AFB = \angle BFC = \angle CFA = 120^\circ, \qquad \min_{P} (|PA| + |PB| + |PC|) = |CC'| = \sqrt{\frac{a^2 + b^2 + c^2}{2} + 2\sqrt{3} K}

.. math::

   F = X(13) = \left(\csc\left(\alpha + \frac{\pi}{3}\right) : \csc\left(\beta + \frac{\pi}{3}\right) : \csc\left(\gamma + \frac{\pi}{3}\right)\right)

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0128–0129``, 2 scanned manuscript pages in ``resources/seelig/21_fermat-point``)
   * - **Euclid's Elements**
     - :ref:`I.1`, :ref:`III.21`, :ref:`III.22` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.1`, :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(13)`, :ref:`X(14)`, :ref:`X(15)`, :ref:`X(16)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``General Reference``, ``Barycentric`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.21" [label="F.21\nFermat Point", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-21/index.html"];
       "F.14" [label="F.14\nConway Notation", fillcolor="#90ee90", color="#2e8b57", URL="../f-14/index.html"];
       "F.14" -> "F.21";
       "F.18" [label="F.18\nEquilateral Triangle", fillcolor="#90ee90", color="#2e8b57", URL="../f-18/index.html"];
       "F.18" -> "F.21";
   }

**Prerequisites**: :ref:`F.14 Conway Notation <f-14>`, :ref:`F.18 Equilateral Triangle <f-18>`

.. toctree::
   :hidden:

   folios
   code
