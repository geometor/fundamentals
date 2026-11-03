================================================
F.41 Geometric Problems and Extremal Loci — Code
================================================

.. enunciation::

   Among all triangles with longest side c = \|AB\| = 1, the acute locus inside the vesica piscis above the semicircle on AB has area A = int_0^{sqrt(3)} (sqrt(4 - x^2) - 1) dx - pi/4 = (5 pi - 6 sqrt(3))/12 approx 0.44297 (for c = 2), and maximizing d_IO over acute triangles approaches the degenerate right-isosceles limit C -> (0, 1).

.. figure:: f-41.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.41 (Geometric Problems and Extremal Loci)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
