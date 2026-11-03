======================================================
F.49 Vesica Piscis and Acute-Obtuse Probability — Code
======================================================

.. enunciation::

   When segment AB of length c is the longest side of triangle ABC, vertex C lies inside the vesica piscis of area c^2 (4 pi - 3 sqrt(3))/6; the semicircle of diameter AB partitions each quadrant of area c^2 (4 pi - 3 sqrt(3))/24 into an obtuse region (O) = c^2 pi / 16 and an acute region (A) = c^2 (5 pi - 6 sqrt(3))/48, giving an exact obtuse-to-acute probability ratio (O)/(A) = 3 pi / (5 pi - 6 sqrt(3)) approx 1.773.

.. figure:: f-49.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.49 (Vesica Piscis and Acute-Obtuse Probability)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
