===============================
F.30 Isosceles Triangles — Code
===============================

.. enunciation::

   An isosceles triangle of given semiperimeter s and area K has half-base x = c/2 governed by the cubic 2 s x^3 - s^2 x^2 + K^2 = 0, which under x = y + s/6 reduces to Cardano's depressed cubic y^3 - (s^2/12) y - (s^3/54 - K^2/(2s)) = 0.

.. figure:: f-30.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.30 (Isosceles Triangles)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
