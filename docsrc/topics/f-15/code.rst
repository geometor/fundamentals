================================
F.15 Cyclic Quadrilateral — Code
================================

.. enunciation::

   A cyclic quadrilateral WXYZ whose interior angles form the arithmetic progression theta, 2*theta, 3*theta, 4*theta has theta = 36 degrees (W = 36, X = 72, Y = 144, Z = 108) and golden-ratio diagonals \|XZ\| = 2 sin(36) = sqrt(3 - phi) and \|WY\| = 2 sin(72) = phi*sqrt(3 - phi) in the unit circle; by contrast, no non-trivial cyclic quadrilateral can have interior angles in geometric progression theta, k*theta, k^2*theta, k^3*theta.

.. figure:: f-15.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.15 (Cyclic Quadrilateral)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
