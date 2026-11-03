=============================
F.46 Stewart's Theorem — Code
=============================

.. enunciation::

   If a cevian of length f from C divides base c = AB into segments k' c and k c (with k + k' = 1), Stewart's Theorem states f^2 = k a^2 + k' b^2 - k k' c^2; at the midpoint k = k' = 1/2, this yields Apollonius's median formula f^2 = (1/2)(a^2 + b^2 - c^2/2).

.. figure:: f-46.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.46 (Stewart's Theorem)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
