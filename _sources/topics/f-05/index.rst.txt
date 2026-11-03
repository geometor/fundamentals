:order: 5
:type: topic
:category: Projective & Harmonic Geometry
:tags: similitude, homothety, harmonic, circles, tangents

.. _f-05:

=========================
F.5 Centers of Similitude
=========================

*Internal and External Homothetic Centers Dividing the Line of Centers Harmonically*

.. enunciation::

   Given two circles (O_1, r_1) and (O_2, r_2) separated by center distance d = \|O_1 O_2\| with r_2 > r_1, their common internal and external tangents concur at the internal and external centers of similitude S_IN and S_EX, which divide O_1 O_2 harmonically in the ratio r_1 : r_2.

.. figure:: f-05.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.5 (Centers of Similitude)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O_1 : Point
   R_1 : Point
   O_2 : Point
   R_2 : Point
   =====
   C_1 = circle(O_1, R_1)
   C_2 = circle(O_2, R_2)
   S_IN = internal_similitude(O_1, R_1, O_2, R_2)
   S_EX = external_similitude(O_1, R_1, O_2, R_2)

Mathematical Synthesis
----------------------

Citing Volume I, p. 207 of his geometry notebooks (:cite:`SeeligNotebooks`), Seelig constructs the :term:`centers of similitude` of two circles :g:`C_1` :math:`(O_1, r_1)` and :g:`C_2` :math:`(O_2, r_2)` separated by :math:`d = |O_1 O_2|`. The internal center :g:`S_IN` (:math:`S_{IN}`) and external center :g:`S_EX` (:math:`S_{EX}`) divide the segment :math:`O_1 O_2` internally and externally in the exact ratio :math:`r_1 : r_2`, forming a four-point :term:`harmonic conjugate` range :math:`(O_1, O_2; S_{IN}, S_{EX})`.

Key Algebraic Identities
------------------------

.. math::

   |O_1 S_{IN}| = d \frac{r_1}{r_2 + r_1}, \qquad |S_{IN} O_2| = d \frac{r_2}{r_2 + r_1}

.. math::

   |S_{EX} O_1| = d \frac{r_1}{r_2 - r_1}, \qquad |S_{EX} O_2| = d \frac{r_2}{r_2 - r_1}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0021–0021``, 1 scanned manuscript page in ``resources/seelig/05_centers-of-similitude``)
   * - **Euclid's Elements**
     - :ref:`VI.2`, :ref:`VI.4` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(55)`, :ref:`X(56)` (:cite:`Kimberling1998`)
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
       "F.5" [label="F.5\nCenters of Similitude", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-05/index.html"];
       "F.2" [label="F.2\nBilinear Transformations", fillcolor="#90ee90", color="#2e8b57", URL="../f-02/index.html"];
       "F.2" -> "F.5";
       "F.16" [label="F.16\nd'Alembert's Theorem", fillcolor="#e0e0e0", color="#777777", URL="../f-16/index.html"];
       "F.5" -> "F.16";
       "F.20" [label="F.20\nExtangent", fillcolor="#e0e0e0", color="#777777", URL="../f-20/index.html"];
       "F.5" -> "F.20";
       "F.44" [label="F.44\nHomothetic Ratios and Crossed Diagonals", fillcolor="#e0e0e0", color="#777777", URL="../f-44/index.html"];
       "F.5" -> "F.44";
       "F.48" [label="F.48\nVerisimilitude, Corner Subtriangles, and Excircle Homothety", fillcolor="#e0e0e0", color="#777777", URL="../f-48/index.html"];
       "F.5" -> "F.48";
   }

**Prerequisites**: :ref:`F.2 Bilinear Transformations <f-02>`

**Required for**: :ref:`F.16 d'Alembert's Theorem <f-16>`, :ref:`F.20 Extangent <f-20>`, :ref:`F.44 Homothetic Ratios and Crossed Diagonals <f-44>`, :ref:`F.48 Verisimilitude, Corner Subtriangles, and Excircle Homothety <f-48>`

.. toctree::
   :hidden:

   folios
   code
