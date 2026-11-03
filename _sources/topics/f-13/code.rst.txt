========================================
F.13 Compare Triangles in Circles — Code
========================================

.. enunciation::

   For a family of triangles ABC inscribed in a fixed circle of radius R sharing a fixed chord AB = c (with central angle 2*phi where sin(phi) = c/(2R)), the area K decomposes into the signed sum of three central isosceles triangles: K = (1/2) c h_c + (1/2) a h_a - (1/2) b h_b.

.. figure:: f-13.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.13 (Compare Triangles in Circles)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
