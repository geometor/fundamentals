===================================
F.19 Equal Incircles Theorem — Code
===================================

.. enunciation::

   If a fan of rays from apex P to a baseline cuts triangle ABC into consecutive subtriangles whose incircles have equal radii r_1 = r_2 = ... = r_n = r, then the ray angles gamma_n with the altitude PR (of height h) follow the hyperbolic progression tan(gamma_n) = sinh(a + n*b) with tanh(b/2) = r/(h - r), so overlapping pairs of subtriangles also have equal incircles.

.. figure:: f-19.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.19 (Equal Incircles Theorem)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
