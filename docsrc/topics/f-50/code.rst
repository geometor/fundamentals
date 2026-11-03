=====================================================================================
F.50 Altitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem — Code
=====================================================================================

.. enunciation::

   Given the three altitudes h_A, h_B, h_C of triangle ABC with reciprocal semiperimeter H = (h_A^{-1} + h_B^{-1} + h_C^{-1})/2, Mitchell's reciprocal Heron formula states K^{-1} = 4 sqrt(H (H - h_A^{-1})(H - h_B^{-1})(H - h_C^{-1})), and a triangle is right-angled at C if and only if h_A^{-2} + h_B^{-2} = h_C^{-2} (the Symphonic Theorem).

.. figure:: f-50.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.50 (Altitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
