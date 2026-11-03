:order: 7
:type: topic
:category: Projective & Harmonic Geometry
:tags: ceva, menelaus, cevians, harmonic, gergonne, stewart

.. _f-07:

=====================
F.7 Ceva and Menelaus
=====================

*Concurrent Cevians, Collinear Transversals, the MNIJ Lattice Framework, and Cevian Programs*

.. enunciation::

   Three cevians AD, BE, CF of triangle ABC concur at a point P if and only if (AF/FB)(BD/DC)(CE/EA) = +1 (Ceva's Theorem), whereas points D, E, F' on the sidelines are collinear if and only if (AF'/F'B)(BD/DC)(CE/EA) = -1 (Menelaus's Theorem), making (A, B; F, F') a harmonic range.

.. figure:: f-07.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.7 (Ceva and Menelaus)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   P : Point
   =====
   D = intersect(line(A, P), line(B, C))
   E = intersect(line(B, P), line(C, A))
   F = intersect(line(C, P), line(A, B))
   F' = intersect(line(D, E), line(A, B))

Mathematical Synthesis
----------------------

Spanning 26 folios (:cite:`SeeligNotebooks`), Topic 07 is one of the richest investigations in the Seelig archive. Combining :term:`Ceva's theorem` (:person:`Giovanni Ceva <ceva>`, :math:`+1`) and :term:`Menelaus's theorem` (:person:`Menelaus <menelaus>`, :math:`-1`), Seelig demonstrates that the cevian trace :g:`F` and the :term:`trilinear <trilinear coordinates>` :term:`polar <pole and polar>` intersection :g:`F'` divide side :g:`A` :g:`B` in a :term:`harmonic conjugate` range :math:`AF/FB = AF'/BF'`. In Folio 1 (`FWS 2011/11/07`), he applies :term:`Ceva's Theorem` to equal tangent segments :math:`x = s-a, y = s-b, z = s-c` to prove the concurrency of the Gergonne point :math:`G_e = X(7)`.

Across Folios 2–22, Seelig develops the **MNIJ coordinate system** (:math:`A=(0,0), B=(M,0), C=(I,J)`, with :math:`y`-intercept :math:`N = JM/(M-I)`), deriving closed-form rational expressions for the Cartesian trace coordinates :g:`D`, :g:`E`, :g:`F`, the cevian lengths :math:`d, e, f` via :term:`Stewart's theorem`, the trilinear area of the cevian triangle :math:`\triangle DEF`, and a complete HP-35s calculator program (`FWS 8/25/2014`) verified on :math:`(a,b,c) = (6,9,13)` and on a Heronian :math:`(78, 90, 84)` triangle (`April 14, 2015`).

Key Algebraic Identities
------------------------

.. math::

   \frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = +1 \quad (\text{Ceva}), \qquad \frac{AF'}{F'B} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = -1 \quad (\text{Menelaus})

.. math::

   D_x = \frac{M J P}{J P + (M - I) Q}, \qquad E_x = \frac{M I Q}{I Q + (M - P) J}, \qquad F_x = \frac{I Q - J P}{Q - J}

.. math::

   \frac{PD}{AD} + \frac{PE}{BE} + \frac{PF}{CF} = 1, \qquad \frac{AP}{AD} + \frac{BP}{BE} + \frac{CP}{CF} = 2

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0024–0049``, 26 scanned manuscript pages in ``resources/seelig/07_ceva-and-menelaus``)
   * - **Euclid's Elements**
     - :ref:`VI.2` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`, :ref:`G.5`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(2)`, :ref:`X(7)`, :ref:`X(8)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Ceva & Menelaus``, ``Ceva``, ``Menelaus``, ``Ceva Compare``, ``6-9-13 Cevian`` (:ref:`Spreadsheets <spreadsheets>`)

Computational Workbook Verification
-----------------------------------

The following worksheets from :person:`seelig`'s ``Triangles and Circles.ods``
workbook verify the numerical and symbolic formulas for this topic on
the canonical :math:`(a, b, c) = (5, 6, 7)` triangle:

.. admonition:: Worksheet: ``Ceva`` (*Triangles and Circles.ods*)

   **Key Formulas & Parameters**

   .. list-table::
      :widths: 12 28 20 40
      :header-rows: 1

      * - Cell
        - Label / Context
        - Value
        - OpenFormula
      * - ``F33``
        - A
        - ``-8``
        - ``=-F25``
      * - ``I33``
        - I33
        - ``-8``
        - ``=F38``
      * - ``J33``
        - -8
        - ``0``
        - ``=G38``
      * - ``F34``
        - B
        - ``16``
        - ``=F27``
      * - ``I34``
        - I34
        - ``16``
        - ``=F39``
      * - ``J34``
        - 16
        - ``0``
        - ``=G39``
      * - ``G35``
        - 0
        - ``8``
        - ``=F26``
      * - ``I35``
        - I35
        - ``0``
        - ``=F40``

   **Cell Excerpt**

   .. list-table::

      * - Ceva's Theorem
        - —
      * - If three lines meet inside a triangl
        - —
      * - Triangle ABC. Create three points D,
        - —
      * - for all possible triangles, then K i
        - —
      * - The product of side ratios equals un
        - —
      * - (AF/BF)*(BD/CD)*(CE/AE) = 1
        - —

.. admonition:: Worksheet: ``Menelaus`` (*Triangles and Circles.ods*)

   **Key Formulas & Parameters**

   .. list-table::
      :widths: 12 28 20 40
      :header-rows: 1

      * - Cell
        - Label / Context
        - Value
        - OpenFormula
      * - ``J10``
        - J10
        - ``5``
        - ``=G10``
      * - ``K10``
        - 5
        - ``6``
        - ``=H10``
      * - ``J11``
        - J11
        - ``0``
        - ``=G11``
      * - ``K11``
        - 0
        - ``0``
        - ``=H11``
      * - ``J12``
        - J12
        - ``18``
        - ``=G12``
      * - ``K12``
        - 18
        - ``0``
        - ``=H12``
      * - ``D13``
        - D13
        - ``A``
        - ``=D10``
      * - ``G13``
        - G13
        - ``5``
        - ``=G10``

   **Cell Excerpt**

   .. list-table::

      * - Menelaus Theorem
        - —
        - —
        - —
        - —
        - —
      * - A line cuts the triangle ABC at thre
        - —
        - —
        - —
        - —
        - —
      * - The product of ratios (BD/DC)*(CE/EA
        - —
        - —
        - —
        - —
        - —
      * - Fred Seelig
        - —
        - —
        - —
        - —
        - —
      * - Begun Oct. 28, 2011
        - —
        - —
        - —
        - —
        - —
      * - July 5, 2012
        - —
        - —
        - —
        - —
        - —

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.7" [label="F.7\nCeva and Menelaus", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-07/index.html"];
       "F.2" [label="F.2\nBilinear Transformations", fillcolor="#90ee90", color="#2e8b57", URL="../f-02/index.html"];
       "F.2" -> "F.7";
       "F.6" [label="F.6\nCentroid", fillcolor="#90ee90", color="#2e8b57", URL="../f-06/index.html"];
       "F.6" -> "F.7";
       "F.23" [label="F.23\nGolden Triangles", fillcolor="#e0e0e0", color="#777777", URL="../f-23/index.html"];
       "F.7" -> "F.23";
       "F.39" [label="F.39\nPole and Polar with Respect to a Triangle", fillcolor="#e0e0e0", color="#777777", URL="../f-39/index.html"];
       "F.7" -> "F.39";
       "F.46" [label="F.46\nStewart's Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-46/index.html"];
       "F.7" -> "F.46";
       "F.47" [label="F.47\nThe UVW Coordinate Triangle", fillcolor="#e0e0e0", color="#777777", URL="../f-47/index.html"];
       "F.7" -> "F.47";
   }

**Prerequisites**: :ref:`F.2 Bilinear Transformations <f-02>`, :ref:`F.6 Centroid <f-06>`

**Required for**: :ref:`F.23 Golden Triangles <f-23>`, :ref:`F.39 Pole and Polar with Respect to a Triangle <f-39>`, :ref:`F.46 Stewart's Theorem <f-46>`, :ref:`F.47 The UVW Coordinate Triangle <f-47>`

.. toctree::
   :hidden:

   folios
   code
