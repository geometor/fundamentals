===================
F.17 Ellipse — Code
===================

.. enunciation::

   Given semi-major axis a and semi-minor axis b, a four-center circular-arc oval approximating the ellipse x^2/a^2 + y^2/b^2 = 1 is constructed by a 7-step five-circle compass procedure, while the exact conic satisfies F = a*e, d = a/e, and vertex mean proportional V = a = sqrt(d*F).

.. figure:: f-17.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.17 (Ellipse)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
