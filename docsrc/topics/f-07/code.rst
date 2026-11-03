============================
F.7 Ceva and Menelaus — Code
============================

.. enunciation::

   Three cevians AD, BE, CF of triangle ABC concur at a point P if and only if (AF/FB)(BD/DC)(CE/EA) = +1 (Ceva's Theorem), whereas points D, E, F' on the sidelines are collinear if and only if (AF'/F'B)(BD/DC)(CE/EA) = -1 (Menelaus's Theorem), making (A, B; F, F') a harmonic range.

.. figure:: f-07.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.7 (Ceva and Menelaus)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
