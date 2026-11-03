======================================
F.35 Obtuse and Acute Triangles — Code
======================================

.. enunciation::

   By Euclid's Elements II.12 (excess) and II.13 (deficit), the square on side a opposite an obtuse or acute angle satisfies a^2 = b^2 + c^2 +/- 2 c x, where x = \|a^2 - (b^2 + c^2)\| / (2 c) is the projection of side b onto line c and h = sqrt(b^2 - x^2) is the altitude.

.. figure:: f-35.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.35 (Obtuse and Acute Triangles)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
