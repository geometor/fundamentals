:order: 20
:type: topic
:category: Triangle Centers & Classical Lines
:tags: excircle, extangent, euler-formula, incircle, circumcircle

.. _f-20:

==============
F.20 Extangent
==============

*The Extangents Triangle, Excircles, and Differentiation of Euler's Incenter-Circumcenter Formula*

.. enunciation::

   The external common tangents to the incircle and circumcircle (or excircles) bound the extangents triangle, while Euler's relation d_{IO}^2 = R^2 - 2rR has derivative d(d_{IO})/dR = (R - r)/sqrt(R^2 - 2rR).

.. figure:: f-20.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.20 (Extangent)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   A : Point
   B : Point
   C : Point
   =====
   I = incenter(A, B, C)
   I_a = excenter_a(A, B, C)
   I_b = excenter_b(A, B, C)
   I_c = excenter_c(A, B, C)
   incircle = circle(I, T_C)
   excircle_C = circle(I_c, E_C)

Mathematical Synthesis
----------------------

In Topic 20 (:cite:`SeeligNotebooks`), Seelig constructs the **extangents triangle** formed by the external tangents to the :term:`incenter` / :term:`excircle` configuration and differentiates :person:`Euler <euler>`'s distance formula :math:`d_{IO} = \sqrt{R^2 - 2rR}` with respect to :math:`R`, confirming Euler's inequality :math:`R \ge 2r` with equality only for the :term:`equilateral triangle`.

Key Algebraic Identities
------------------------

.. math::

   d_{IO}^2 = R^2 - 2 r R, \qquad \frac{d}{d R}(d_{IO}) = \frac{R - r}{\sqrt{R^2 - 2 r R}}, \qquad r_a = \frac{K}{s - a}, \quad r_b = \frac{K}{s - b}, \quad r_c = \frac{K}{s - c}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0127–0127``, 1 scanned manuscript page in ``resources/seelig/20_extangent``)
   * - **Euclid's Elements**
     - :ref:`IV.4` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.3`
   * - **Encyclopedia of Triangle Centers**
     - :ref:`X(1)`, :ref:`X(3)`, :ref:`X(40)`, :ref:`X(55)`, :ref:`X(56)` (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Excenters``, ``Incircle-Incenter``, ``Centers of Similitude`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.20" [label="F.20\nExtangent", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-20/index.html"];
       "F.5" [label="F.5\nCenters of Similitude", fillcolor="#90ee90", color="#2e8b57", URL="../f-05/index.html"];
       "F.5" -> "F.20";
       "F.11" [label="F.11\nCircumcenter", fillcolor="#90ee90", color="#2e8b57", URL="../f-11/index.html"];
       "F.11" -> "F.20";
       "F.28" [label="F.28\nIncenter", fillcolor="#90ee90", color="#2e8b57", URL="../f-28/index.html"];
       "F.28" -> "F.20";
   }

**Prerequisites**: :ref:`F.5 Centers of Similitude <f-05>`, :ref:`F.11 Circumcenter <f-11>`, :ref:`F.28 Incenter <f-28>`

.. toctree::
   :hidden:

   folios
   code
