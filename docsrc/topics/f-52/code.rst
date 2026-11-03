===============================================
F.52 Homogeneous Barycentric Coordinates — Code
===============================================

.. enunciation::

   Every triangle center X(n) has homogeneous barycentric coordinates (u : v : w) normalizable to absolute weights lambda_A + lambda_B + lambda_C = 1 such that X = lambda_A A + lambda_B B + lambda_C C; for the nine-point center N = X(5), lambda_A = 1/4 + (b^2 - c^2)(a^2 - (b^2 + c^2)) / (32 K^2).

.. figure:: f-52.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.52 (Homogeneous Barycentric Coordinates)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
