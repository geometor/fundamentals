:order: 53
:type: topic
:category: Algebraic & Coordinate Systems
:tags: trigonometry, half-angle, semicircle, thales, pythagoras

.. _f-53:

======================================
F.53 Geometric Half-Angle Trigonometry
======================================

*Unit Semicircle Chord Proof of cos^2(theta/2) and sin^2(theta/2)*

.. enunciation::

   In a unit semicircle of radius R = 1 and diameter AB = 2, a point P at central angle theta has altitude sin(theta), base projections 1 + cos(theta) and 1 - cos(theta), and chord \|AP\| = 2 cos(theta/2) = sqrt(2 + 2 cos(theta)), giving cos^2(theta/2) = (1 + cos(theta))/2 and sin^2(theta/2) = (1 - cos(theta))/2.

.. figure:: f-53.svg
   :align: center
   :width: 100%

   Interactive GEOMETOR construction for **F.53 (Geometric Half-Angle Trigonometry)**. Hover any geometric label in the text or figure to highlight the corresponding element.

.. signature::

   O : Point
   A : Point
   P : Point
   =====
   c_unit = circle(O, A)
   l_oa = line(O, A)
   B = intersection(l_oa, c_unit)
   H = foot(P, l_oa)
   s_ap = segment(A, P)
   s_bp = segment(B, P)

Mathematical Synthesis
----------------------

In this elegant single-folio geometric proof (:cite:`SeeligNotebooks`), Seelig derives the half-angle identities for :math:`\cos^2(\theta/2)` and :math:`\sin^2(\theta/2)` directly from a unit semicircle (:math:`R = 1`, diameter :math:`|AB| = 2`) without algebraic angle-addition expansion. Dropping the :term:`altitude <orthocenter>` :math:`|PH| = \sin\theta` from :g:`P` to diameter :g:`A` :g:`B` divides the diameter into :math:`|AH| = 1 + \cos\theta` and :math:`|HB| = 1 - \cos\theta`.

By the inscribed angle theorem (:person:`Euclid` *Elements* :ref:`III.20`), the angle at :g:`A` is :math:`\theta/2`, so the chord :g:`s_ap` has length :math:`2x = 2\cos(\theta/2)`. Applying the Pythagorean theorem (:ref:`I.47`) to right triangle :math:`\triangle AHP` gives :math:`(2x)^2 = \sin^2\theta + (1 + \cos\theta)^2 = 2 + 2\cos\theta`, whence :math:`x^2 = \cos^2\frac{\theta}{2} = \frac{1}{2} + \frac{1}{2}\cos\theta` and :math:`\sin^2\frac{\theta}{2} = \frac{1}{2} - \frac{1}{2}\cos\theta`.

Key Algebraic Identities
------------------------

.. math::

   (2 x)^2 = \sin^2\theta + (1 + \cos\theta)^2 = 2 + 2\cos\theta \implies \cos^2\frac{\theta}{2} = \frac{1 + \cos\theta}{2}

.. math::

   \sin^2\frac{\theta}{2} = 1 - \cos^2\frac{\theta}{2} = \frac{1 - \cos\theta}{2}, \qquad \tan\frac{\theta}{2} = \frac{\sin\theta}{1 + \cos\theta}

Cross-Repository Canon & Archival Provenance
--------------------------------------------

.. list-table::
   :widths: 28 72

   * - **Seelig Archive Folios**
     - :doc:`folios` (Folios ``0346–0346``, 1 scanned manuscript page in ``resources/seelig/53_trig``)
   * - **Euclid's Elements**
     - :ref:`I.47`, :ref:`III.20`, :ref:`III.31` (:cite:`EuclidElements`)
   * - **GEOMETOR Elements (G-Index)**
     - :ref:`G.7`, :ref:`G.11`
   * - **Encyclopedia of Triangle Centers**
     - General projective / metric locus (:cite:`Kimberling1998`)
   * - **Seelig Spreadsheets**
     - ``Trig Identities``, ``General Reference`` (:ref:`Spreadsheets <spreadsheets>`)

Constructive Dependency Graph
-----------------------------

.. graphviz::

   digraph dependency {
       rankdir=TB;
       bgcolor="transparent";
       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];
       edge [color="#888888", arrowsize=0.7];
       "F.53" [label="F.53\nGeometric Half-Angle Trigonometry", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-53/index.html"];
       "F.10" [label="F.10\nCircles and Geometric Mean", fillcolor="#90ee90", color="#2e8b57", URL="../f-10/index.html"];
       "F.10" -> "F.53";
   }

**Prerequisites**: :ref:`F.10 Circles and Geometric Mean <f-10>`

.. toctree::
   :hidden:

   folios
   code
