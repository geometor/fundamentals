===========================
F.14 Conway Notation — Code
===========================

.. enunciation::

   In John H. Conway's triangle notation, setting S = 2K (twice the area of triangle ABC), S_omega = (a^2 + b^2 + c^2)/2, and S_A = (b^2 + c^2 - a^2)/2, S_B = (c^2 + a^2 - b^2)/2, S_C = (a^2 + b^2 - c^2)/2 reduces trigonometric and barycentric identities to polynomial expressions satisfying S_B S_C + S_C S_A + S_A S_B = S^2.

.. figure:: f-14.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.14 (Conway Notation)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
