============================
F.1 Albert's Parabola — Code
============================

.. enunciation::

   Given a parabola y = x^2 and a point P = (P_x, P_y) on it, the tangent line T and normal line N at P satisfy y = 2 P_x x - P_x^2 and y = -x/(2 P_x) + P_x^2 + 1/2; requiring N to pass through (M, 0) yields the depressed cubic P_x^3 + (1/2) P_x - M/2 = 0.

.. figure:: f-01.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.1 (Albert's Parabola)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
