=======================================
F.47 The UVW Coordinate Triangle — Code
=======================================

.. enunciation::

   Placing the altitude foot H_C at the origin (0, 0) with A = (-U, 0), B = (W, 0), and C = (0, V) parameterizes any triangle by three numbers (U, V, W) with a = sqrt(V^2 + W^2), b = sqrt(U^2 + V^2), c = U + W, and reduces the cevian traces D, E, F through P(p, q) to explicit 2x2 rational matrix formulas.

.. figure:: f-47.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.47 (The UVW Coordinate Triangle)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
