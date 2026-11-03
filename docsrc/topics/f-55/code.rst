===========================================================================
F.55 Compass Constructions and Angle-to-Side Triangle Reconstruction — Code
===========================================================================

.. enunciation::

   Given the three interior angles (alpha, beta, gamma) of a triangle normalized to unit area K = 1 (so s = 1/r), the Conway intouch segments x = s - a = r cot(alpha/2), y = s - b = r cot(beta/2), and z = s - c = r cot(gamma/2) determine the side lengths a = y + z, b = z + x, and c = x + y = 2 s - (a + b).

.. figure:: f-55.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.55 (Compass Constructions and Angle-to-Side Triangle Reconstruction)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
