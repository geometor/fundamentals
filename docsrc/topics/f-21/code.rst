========================
F.21 Fermat Point — Code
========================

.. enunciation::

   For any triangle ABC whose largest interior angle is less than 120 degrees, erecting external equilateral triangles BCX_A, CAY_B, ABZ_C on its sides yields concurrent segments AX_A, BY_B, CZ_C that intersect at the Fermat-Torricelli point F = X(13), where <AFB = <BFC = <CFA = 120 degrees and FA + FB + FC is minimized.

.. figure:: f-21.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.21 (Fermat Point)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
