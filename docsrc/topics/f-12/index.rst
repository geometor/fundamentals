:order: 12
:type: topic
:category: Circle Geometry & Pencils
:tags: coaxial-circles, radical-axis, apollonius, electromagnetics, ogilvy

.. _f-12:

====================
F.12 Coaxial Circles
====================

*Equipotential Pencils Around Point Charges, Limiting Points, and Orthogonal Families*

.. enunciation::

   A hyperbolic pencil of coaxial circles with limiting points L_1 = (-r, 0) and L_2 = (+r, 0) coincides with the Apollonian equipotential circles d_1 / d_2 = k around two point charges Q_1, Q_2, sharing the y-axis as their common radical axis.

.. figure:: f-12.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.12 (Coaxial Circles)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   L_1 : Point
   L_2 : Point
   R_1 : Point
   R_2 : Point
   =====
   radical_axis = line(R_1, R_2)
   line_of_centers = line(L_1, L_2)
   C_1 = coaxial_circle(L_1, L_2, -3.5)
   C_2 = coaxial_circle(L_1, L_2, 2.5)

Mathematical Synthesis
----------------------

Inspired by electrostatic equipotential contours around fixed point charges :math:`Q_1(-r, 0)` and :math:`Q_2(+r, 0)` in Kraus's *Electromagnetics* and :person:`C. Stanley Ogilvy <ogilvy>`'s *Excursions in Geometry* (:cite:`Ogilvy1969`), Seelig's 12-folio study (`Friday April 24, 2015`, :cite:`SeeligNotebooks`) unifies :term:`coaxial circles`, :term:`harmonic conjugate` division, :term:`radical axis` theory, and :term:`Apollonian circles`.

For potential ratio :math:`k = Q_1/Q_2 = d_1/d_2 = 2`, Seelig determines six landmark points :math:`P_1,\dots,P_6` on the equipotential circle: the internal and external :term:`harmonic division <harmonic conjugate>` points :math:`P_1 = (\frac{1}{3}r, 0)` and :math:`P_2 = (3r, 0)`, center :math:`M' = (\frac{5}{3}r, 0)`, radius :math:`R = \frac{4}{3}r`, vertical chord endpoints :math:`P_3, P_4 = (r, \pm \frac{2}{\sqrt{3}}r)`, and right-triangle vertices :math:`P_5, P_6` on the circle :math:`x^2 + y^2 = 2r^2`.

Key Algebraic Identities
------------------------

.. math::

   P_1 = \left(\frac{k - 1}{k + 1}r,\, 0\right), \qquad P_2 = \left(\frac{k + 1}{k - 1}r,\, 0\right), \qquad M' = \frac{k^2 + 1}{k^2 - 1}r, \qquad R = \frac{2 k}{k^2 - 1}r

.. math::

   x^2 + y^2 - 2 c_x x + r^2 = 0, \qquad E_{\text{TOT}} = k Q_1 \frac{x - x_1}{|x - x_1|^3} + k Q_2 \frac{x - x_2}{|x - x_2|^3} = 0

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0072–0083``, 12 scanned manuscript pages in ``resources/seelig/12_coaxial-circles``)
   * - **Euclid's Elements**
     - :ref:`III.35`, :ref:`III.36` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Coaxial Circles``, ``Coaxal Circle Table``, ``Apollonian Circles``, ``Radical Axes`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.12" [label="F.12\nCoaxial Circles", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-12/index.html"];
       "F.2" [label="F.2\nBilinear Transformations", fillcolor="#90ee90", color="#2e8b57", URL="../f-02/index.html"];
       "F.2" -> "F.12";
       "F.8" [label="F.8\nChord Intersection", fillcolor="#90ee90", color="#2e8b57", URL="../f-08/index.html"];
       "F.8" -> "F.12";
       "F.25" [label="F.25\nHarmonic Conjugates", fillcolor="#e0e0e0", color="#777777", URL="../f-25/index.html"];
       "F.12" -> "F.25";
       "F.43" [label="F.43\nRadical Axes and Radical Center", fillcolor="#e0e0e0", color="#777777", URL="../f-43/index.html"];
       "F.12" -> "F.43";
       "F.51" [label="F.51\nApollonian Circles and the Problem of Apollonius", fillcolor="#e0e0e0", color="#777777", URL="../f-51/index.html"];
       "F.12" -> "F.51";
   }

**Prerequisites**: :ref:`F.2 Bilinear Transformations <f-02>`, :ref:`F.8 Chord Intersection <f-08>`

**Required for**: :ref:`F.25 Harmonic Conjugates <f-25>`, :ref:`F.43 Radical Axes and Radical Center <f-43>`, :ref:`F.51 Apollonian Circles and the Problem of Apollonius <f-51>`

.. toctree::
   :hidden:

   folios
   code
