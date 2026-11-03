:order: 44
:type: topic
:category: Projective & Harmonic Geometry
:tags: ratios, similitude, homothety, harmonic, crossed-ladders

.. _f-44:

============================================
F.44 Homothetic Ratios and Crossed Diagonals
============================================

*Internal and External Division of Parallel Uprights from a Center of Similitude*

.. enunciation::

   Given two parallel uprights of heights h_1 < h_2 separated by horizontal distance d and viewed from their external center of similitude O, the crossed diagonals meet at horizontal distance x = d h_1 / (h_1 + h_2) from the first upright, while O lies at distance y - x = d h_1 / (h_2 - h_1) to its left, forming a harmonic range.

.. figure:: f-44.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.44 (Homothetic Ratios and Crossed Diagonals)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   P_1 : Point
   P_2 : Point
   =====
   s_1 = segment(A, P_1)
   s_2 = segment(B, P_2)
   O_ext = intersection(line(A, B), line(P_1, P_2))
   O_int = intersection(line(A, P_2), line(B, P_1))

Mathematical Synthesis
----------------------

Across five folios (:cite:`SeeligNotebooks`), Seelig analyzes the projective and metric proportions of two homothetic right triangles sharing an apex angle :math:`\phi` at :g:`O_ext` with parallel vertical uprights :math:`h_1 < h_2` separated by distance :math:`d` along the baseline :g:`A` :g:`B`. By similar triangles (:person:`Euclid` *Elements* :ref:`VI.2` and :ref:`VI.4`), the crossed diagonals :math:`AP_2` and :math:`BP_1` intersect at :g:`O_int` at horizontal distance :math:`x = d\frac{h_1}{h_1+h_2}` from :g:`A` (and height :math:`h = \frac{h_1 h_2}{h_1+h_2}`, half the :term:`harmonic mean`), while the external apex :g:`O_ext` lies at distance :math:`y - x = d\frac{h_1}{h_2-h_1}` from :g:`A`.

Adding the internal and external distances yields the total span between the two :term:`centers of similitude` :math:`y = \frac{2 d h_1 h_2}{h_2^2 - h_1^2}` and its midpoint :math:`z = \frac{d h_1 h_2}{h_2^2 - h_1^2}`, reproducing the Apollonian :term:`harmonic conjugate` formulas with :math:`k = h_2/h_1`.

Key Algebraic Identities
------------------------

.. math::

   x = d\frac{h_1}{h_1 + h_2}, \qquad y - x = d\frac{h_1}{h_2 - h_1}, \qquad h = \frac{h_1 h_2}{h_1 + h_2}

.. math::

   y = \frac{2 d h_1 h_2}{h_2^2 - h_1^2}, \qquad z = \frac{y}{2} = \frac{d h_1 h_2}{h_2^2 - h_1^2}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0282–0286``, 5 scanned manuscript pages in ``resources/seelig/44_ratios``)
   * - **Euclid's Elements**
     - :ref:`VI.2`, :ref:`VI.4` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.5`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Centers of Similitude``, ``Harmonic Conjugates`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.44" [label="F.44\nHomothetic Ratios and Crossed Diagonals", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-44/index.html"];
       "F.5" [label="F.5\nCenters of Similitude", fillcolor="#90ee90", color="#2e8b57", URL="../f-05/index.html"];
       "F.5" -> "F.44";
       "F.25" [label="F.25\nHarmonic Conjugates", fillcolor="#90ee90", color="#2e8b57", URL="../f-25/index.html"];
       "F.25" -> "F.44";
       "F.27" [label="F.27\nHarmonic Mean", fillcolor="#90ee90", color="#2e8b57", URL="../f-27/index.html"];
       "F.27" -> "F.44";
   }

**Prerequisites**: :ref:`F.5 Centers of Similitude <f-05>`, :ref:`F.25 Harmonic Conjugates <f-25>`, :ref:`F.27 Harmonic Mean <f-27>`

.. toctree::
   :hidden:

   folios
   code
