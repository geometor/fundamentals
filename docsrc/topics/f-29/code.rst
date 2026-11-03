====================
F.29 Inradius — Code
====================

.. enunciation::

   The inradius r = K / s = (1/2) sqrt(((b+c-a)(c+a-b)(a+b-c))/(a+b+c)) = 4 R sin(alpha/2) sin(beta/2) sin(gamma/2) takes integer values on primitive Pythagorean triples and partitions the perimeter into Conway segments x, y, z whose touchpoints T_A, T_B, T_C concur at the Gergonne point Ge = X(7).

.. figure:: f-29.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.29 (Inradius)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
