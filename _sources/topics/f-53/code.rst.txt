=============================================
F.53 Geometric Half-Angle Trigonometry — Code
=============================================

.. enunciation::

   In a unit semicircle of radius R = 1 and diameter AB = 2, a point P at central angle theta has altitude sin(theta), base projections 1 + cos(theta) and 1 - cos(theta), and chord \|AP\| = 2 cos(theta/2) = sqrt(2 + 2 cos(theta)), giving cos^2(theta/2) = (1 + cos(theta))/2 and sin^2(theta/2) = (1 - cos(theta))/2.

.. figure:: f-53.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.53 (Geometric Half-Angle Trigonometry)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
