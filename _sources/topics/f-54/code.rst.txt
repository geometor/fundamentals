==========================================================
F.54 HP-35s Triangle Program and Coordinate Scripts — Code
==========================================================

.. enunciation::

   In the canonical frame A = (0, 0), B = (M, 0), C = (I, J), the forward and inverse barycentric-Cartesian transformations BARY 2 CAR and CAR 2 BARY are given by P = M U + I V, Q = J V and V = Q / J, U = (P - I V) / M, T = 1 - (U + V).

.. figure:: f-54.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.54 (HP-35s Triangle Program and Coordinate Scripts)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
