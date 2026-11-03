=======================
F.31 Logic Tests — Code
=======================

.. enunciation::

   Given collinear points A, B, C, the three Boolean inequality tests T_1 = (\|CA\| < \|AB\|), T_2 = (\|CB\| < \|AB\|), and T_3 = (\|CA\| < \|CB\|) uniquely partition the line AB into Region A (-1 < k < 0), interior segment AB (0 < k < infty), and Region B (-infty < k < -1), determining the sign of k = +/- \|AC\| / \|BC\|.

.. figure:: f-31.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.31 (Logic Tests)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
