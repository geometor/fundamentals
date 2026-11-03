:order: 33
:type: topic
:category: Polygons, Tessellations & Special Triangles
:tags: pythagorean-triples, euclid, number-theory, right-triangle

.. _f-33:

================================
F.33 Euclidean (m, n) Generators
================================

*Parametric Pythagorean Triple Table for 2 <= m <= 7*

.. enunciation::

   For integers m > n >= 1, Euclid's quadratic generators a = m^2 - n^2, b = 2 m n, and c = m^2 + n^2 satisfy a^2 + b^2 = c^2 and inradius r = n(m - n).

.. figure:: f-33.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.33 (Euclidean (m, n) Generators)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   a = segment(B, C)
   b = segment(C, A)
   c = segment(A, B)

Mathematical Synthesis
----------------------

This single-folio reference table (:cite:`SeeligNotebooks`) tabulates :person:`Euclid`'s parametric generators :math:`(m, n, m^2-n^2, 2mn, m^2+n^2)` (from *Elements* Book X, Lemma 1 to X.29) across 11 integer pairs for :math:`2 \le m \le 7`: from :math:`(m,n) = (2,1) \mapsto (3,4,5)` through :math:`(3,2)\mapsto(5,12,13)`, :math:`(4,1)\mapsto(15,8,17)`, :math:`(4,3)\mapsto(7,24,25)`, :math:`(5,2)\mapsto(21,20,29)`, :math:`(5,4)\mapsto(9,40,41)`, :math:`(6,1)\mapsto(35,12,37)`, :math:`(6,5)\mapsto(11,60,61)`, :math:`(7,2)\mapsto(45,28,53)`, :math:`(7,4)\mapsto(33,56,65)`, to :math:`(7,6)\mapsto(13,84,85)`.

Every row in Seelig's table omits common-factor pairs (such as :math:`(3,1)` or :math:`(4,2)`) so that all 11 generated triples are primitive :term:`Pythagorean triple` right triangles with integer :term:`inradius` :math:`r = n(m-n)` and semiperimeter :math:`s = m(m+n)`.

Key Algebraic Identities
------------------------

.. math::

   a = m^2 - n^2, \qquad b = 2 m n, \qquad c = m^2 + n^2, \qquad a^2 + b^2 = (m^2 + n^2)^2 = c^2

.. math::

   s = m(m + n), \qquad r = n(m - n), \qquad K = m n (m^2 - n^2)

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0223–0223``, 1 scanned manuscript page in ``resources/seelig/33_m-n``)
   * - **Euclid's Elements**
     - :ref:`I.47`, :ref:`X.29` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.11`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Pythagorean Triples``, ``Right Triangle`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.33" [label="F.33\nEuclidean (m, n) Generators", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-33/index.html"];
       "F.29" [label="F.29\nInradius", fillcolor="#90ee90", color="#2e8b57", URL="../f-29/index.html"];
       "F.29" -> "F.33";
       "F.42" [label="F.42\nAltitude of a Pythagorean Triple Triangle", fillcolor="#e0e0e0", color="#777777", URL="../f-42/index.html"];
       "F.33" -> "F.42";
   }

**Prerequisites**: :ref:`F.29 Inradius <f-29>`

**Required for**: :ref:`F.42 Altitude of a Pythagorean Triple Triangle <f-42>`

.. toctree::
   :hidden:

   folios
   code
