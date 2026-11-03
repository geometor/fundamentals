:order: 32
:type: topic
:category: Circle Inversion, Coaxial & Radical Systems
:tags: markowski, sagitta, circumcircle, incircle, euler

.. _f-32:

========================
F.32 Markowski's Theorem
========================

*Circumcircle Midpoint Sagitta Product, Euler's Inequality, and Midpoint Inversion*

.. enunciation::

   If J, K, L denote the perpendicular sagittas from the side midpoints of triangle ABC to the circumcircle, Markowski's Theorem states J K L = (1/2) r^2 R = (R^2 - d_IO^2)^2 / (8 R).

.. figure:: f-32.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.32 (Markowski's Theorem)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   O = circumcenter(A, B, C)
   I = incenter(A, B, C)
   c_out = circle(O, A)
   M_A = midpoint(B, C)
   P_A = intersection(ray(O, M_A), c_out)
   J = segment(M_A, P_A)

Mathematical Synthesis
----------------------

Dated April 23, 2015 (:cite:`SeeligNotebooks`), Seelig's two-page investigation *GIVEN :math:`d_{IO}` and :math:`R` — what is :math:`J\cdot K\cdot L`? (:person:`Markowski`'s Theorem)* examines the three :term:`sagitta` segments :math:`J, K, L` extending from the side midpoints :g:`M_A`, :g:`M_B`, :g:`M_C` to the :term:`circumcircle` :g:`c_out`. Combining :term:`Markowski's theorem` :math:`JKL = \frac{1}{2}r^2 R` with :person:`Euler`'s identity :math:`d_{IO} = \sqrt{R^2 - 2rR}`, Seelig eliminates the :term:`inradius` :math:`r = (R^2 - d_{IO}^2)/(2R)` to express the sagitta product purely in terms of :math:`R` and :math:`d_{IO}`: :math:`JKL = \frac{(R^2 - d_{IO}^2)^2}{8R}`.

On Folio 1, Seelig also notes the midpoint circle-:term:`inversion` radius :math:`\rho_I = \sqrt{R^2 - (a/2)^2}` fixing the vertices of side :math:`a`. On Folio 2, he tests the formula on the :term:`equilateral triangle` (:math:`d_{IO}=0 \implies JKL = R^3/8`) and the :math:`30^\circ\text{--}60^\circ\text{--}90^\circ` triangle (:math:`R=1, r=(\sqrt{3}-1)/2, d_{IO}^2 = 2-\sqrt{3}, JKL = (2-\sqrt{3})/4`). In a candid archival moment (*"Stumped! FWS 4/23/2015"*), Seelig substitutes :math:`d_{IO}^2 = 2-\sqrt{3}` into :math:`(R^2 - (d_{IO}^2)^2)^2/(8R)`, accidentally squaring :math:`d_{IO}^2` a second time—whose removal immediately reconciles both sides to :math:`(2-\sqrt{3})/4`.

Key Algebraic Identities
------------------------

.. math::

   J K L = \frac{1}{2} r^2 R = \frac{(R^2 - d_{IO}^2)^2}{8 R}, \qquad d_{IO}^2 = R^2 - 2 r R

.. math::

   J + K + L = 2 R + r, \qquad \rho_I = \sqrt{R^2 - \left(\frac{a}{2}\right)^2}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0221–0222``, 2 scanned manuscript pages in ``resources/seelig/32_markowski``)
   * - **Euclid's Elements**
     - :ref:`III.35`, :ref:`IV.5` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.7`, :ref:`G.8`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(3)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Circumcircle-Circumcenter``, ``Incircle-Incenter`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.32" [label="F.32\nMarkowski's Theorem", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-32/index.html"];
       "F.4" [label="F.4\nCarnot's Theorem", fillcolor="#90ee90", color="#2e8b57", URL="../f-04/index.html"];
       "F.4" -> "F.32";
       "F.11" [label="F.11\nCircumcenter", fillcolor="#90ee90", color="#2e8b57", URL="../f-11/index.html"];
       "F.11" -> "F.32";
       "F.29" [label="F.29\nInradius", fillcolor="#90ee90", color="#2e8b57", URL="../f-29/index.html"];
       "F.29" -> "F.32";
       "F.41" [label="F.41\nGeometric Problems and Extremal Loci", fillcolor="#e0e0e0", color="#777777", URL="../f-41/index.html"];
       "F.32" -> "F.41";
   }

**Prerequisites**: :ref:`F.4 Carnot's Theorem <f-04>`, :ref:`F.11 Circumcenter <f-11>`, :ref:`F.29 Inradius <f-29>`

**Required for**: :ref:`F.41 Geometric Problems and Extremal Loci <f-41>`

.. toctree::
   :hidden:

   folios
   code
