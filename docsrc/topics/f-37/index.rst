:order: 37
:type: topic
:category: Conics & Analytic Loci
:tags: parabola, euler, inradius, circumradius, harmonic

.. _f-37:

==============================
F.37 Euler's Inradius Parabola
==============================

*Parabolic Locus r(d) = (R^2 - d^2)/(2R) and Harmonic Factorization of Euler's Identity*

.. enunciation::

   For a fixed circumradius R, Euler's relation d^2 = R^2 - 2 r R defines a downward-opening parabola r(d) = R/2 - d^2/(2R) = (R - d)(R + d)/(2R) with vertex (0, R/2) at the equilateral triangle and roots at the degenerate limits d = +/- R.

.. figure:: f-37.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.37 (Euler's Inradius Parabola)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   V : Point
   F : Point
   directrix : Line
   P : Point
   =====
   Q = foot(P, directrix)
   s_fp = segment(F, P)
   s_pq = segment(P, Q)
   tangent = bisector(F, P, Q)

Mathematical Synthesis
----------------------

In this three-folio study (:cite:`SeeligNotebooks`), Seelig reinterprets :person:`Euler`'s triangle distance theorem :math:`d^2 = R^2 - 2rR` (where :math:`d = |IO|`) as a functional locus :math:`r(d) = \frac{R}{2} - \frac{d^2}{2R}` over a fixed :term:`circumcircle` of radius :math:`R`. Plotting :math:`r` against :math:`d` yields a downward-opening :term:`parabola` whose vertex :math:`(0, R/2)` represents the :term:`equilateral triangle` (:math:`r = R/2`, Euler's inequality maximum) and whose horizontal intercepts :math:`d = \pm R` represent degenerate flat triangles (:math:`r = 0`).

Factoring the numerator as :math:`r(d) = \frac{(R-d)(R+d)}{2R}`, Seelig connects the segments :math:`R-d` and :math:`R+d` partitioned by the :term:`incenter` :g:`I` along a diameter of the :term:`circumcircle <circumcenter>` to the :term:`power of a point` :math:`(R-d)(R+d) = 2rR` and :term:`harmonic conjugate` division.

Key Algebraic Identities
------------------------

.. math::

   d^2 = R^2 - 2 r R \iff r(d) = \frac{R}{2} - \frac{d^2}{2 R} = \frac{(R - d)(R + d)}{2 R}

.. math::

   r_{\max} = r(0) = \frac{R}{2}, \qquad (R - d)(R + d) = 2 r R

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0233–0235``, 3 scanned manuscript pages in ``resources/seelig/37_parabolas``)
   * - **Euclid's Elements**
     - :ref:`II.5`, :ref:`III.35` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.7`, :ref:`G.8`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(3)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Incircle-Incenter``, ``Circumcircle-Circumcenter`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.37" [label="F.37\nEuler's Inradius Parabola", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-37/index.html"];
       "F.1" [label="F.1\nAlbert's Parabola", fillcolor="#90ee90", color="#2e8b57", URL="../f-01/index.html"];
       "F.1" -> "F.37";
       "F.11" [label="F.11\nCircumcenter", fillcolor="#90ee90", color="#2e8b57", URL="../f-11/index.html"];
       "F.11" -> "F.37";
       "F.29" [label="F.29\nInradius", fillcolor="#90ee90", color="#2e8b57", URL="../f-29/index.html"];
       "F.29" -> "F.37";
       "F.41" [label="F.41\nGeometric Problems and Extremal Loci", fillcolor="#e0e0e0", color="#777777", URL="../f-41/index.html"];
       "F.37" -> "F.41";
   }

**Prerequisites**: :ref:`F.1 Albert's Parabola <f-01>`, :ref:`F.11 Circumcenter <f-11>`, :ref:`F.29 Inradius <f-29>`

**Required for**: :ref:`F.41 Geometric Problems and Extremal Loci <f-41>`

.. toctree::
   :hidden:

   folios
   code
