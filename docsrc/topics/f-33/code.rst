=======================================
F.33 Euclidean (m, n) Generators — Code
=======================================

.. enunciation::

   For integers m > n >= 1, Euclid's quadratic generators a = m^2 - n^2, b = 2 m n, and c = m^2 + n^2 satisfy a^2 + b^2 = c^2 and inradius r = n(m - n).

.. figure:: f-33.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.33 (Euclidean (m, n) Generators)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
