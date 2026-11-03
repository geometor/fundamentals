================================================
F.40 Regular Polygons and Nested Radicals — Code
================================================

.. enunciation::

   For a regular N-gon inscribed in a unit circle (R = 1), doubling the number of sides maps edge length E_{N/2} to E_N = sqrt(2 - sqrt(4 - E_{N/2}^2)), generating closed-form nested quadratic radicals for the 2^k, 3*2^k, 5*2^k, and 15*2^k polygon families.

.. figure:: f-40.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.40 (Regular Polygons and Nested Radicals)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
