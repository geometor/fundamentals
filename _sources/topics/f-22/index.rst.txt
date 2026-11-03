:order: 22
:type: topic
:category: Conics & Analytic Loci
:tags: functions, gaussian, error-function, probability, approximation

.. _f-22:

==============
F.22 Functions
==============

*Gaussian Error Function Approximations (Abramowitz & Stegun) and Probability Distributions*

.. enunciation::

   The standard normal cumulative distribution Phi(x) and error function erf(x) satisfy Phi(x) = 1/2 + (1/2) erf(x/sqrt(2)), where erf(x) is approximated to 1.5e-7 accuracy by Abramowitz and Stegun's 5-term rational-exponential formula.

.. figure:: f-22.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.22 (Functions)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O : Point
   A_1 : Point
   A_2 : Point
   B_1 : Point
   =====
   major_axis = segment(A_1, A_2)
   b = segment(O, B_1)
   P = point_on_curve(A_2, B_1)

Mathematical Synthesis
----------------------

Used by Seelig for his Monte Carlo geometric probability simulations (see :ref:`F.41 <f-41>` and :ref:`F.49 <f-49>`), Topic 22 (:cite:`SeeligNotebooks`) records the interconversion formulas among :math:`\Phi(x), Q(x), \operatorname{erf}(x), \operatorname{erfc}(x)`, the 5-term rational-exponential approximation from Abramowitz & Stegun (:cite:`AbramowitzStegun1964`, p. 299, Eq. 7.1.26), and summary integrals for the Binomial, Poisson, Bernoulli, Uniform, Exponential, and Normal distributions.

Key Algebraic Identities
------------------------

.. math::

   \Phi(x) = \frac{1}{2} + \frac{1}{2}\operatorname{erf}\left(\frac{x}{\sqrt{2}}\right), \qquad \operatorname{erf}(x) \approx 1 - \left(\sum_{k=1}^5 a_k t^k\right) e^{-x^2}, \quad t = \frac{1}{1 + 0.3275911 x}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0130–0131``, 2 scanned manuscript pages in ``resources/seelig/22_functions``)
   * - **Euclid's Elements**
     - Classical Euclidean synthesis (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - Foundational construction
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``General Reference`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.22" [label="F.22\nFunctions", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-22/index.html"];
   }

.. toctree::
   :hidden:

   folios
   code
