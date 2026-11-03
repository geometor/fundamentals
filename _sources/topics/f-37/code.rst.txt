=====================================
F.37 Euler's Inradius Parabola — Code
=====================================

.. enunciation::

   For a fixed circumradius R, Euler's relation d^2 = R^2 - 2 r R defines a downward-opening parabola r(d) = R/2 - d^2/(2R) = (R - d)(R + d)/(2R) with vertex (0, R/2) at the equilateral triangle and roots at the degenerate limits d = +/- R.

.. figure:: f-37.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.37 (Euler's Inradius Parabola)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
