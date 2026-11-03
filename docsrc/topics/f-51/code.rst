============================================================
F.51 Apollonian Circles and the Problem of Apollonius — Code
============================================================

.. enunciation::

   The locus of points P with distance ratio \|PA\| / \|PB\| = k > 1 (where \|AB\| = d) is the Apollonian circle of radius R = d k / (k^2 - 1) centered at distance M' = d / (k^2 - 1) beyond B, cutting line AB at the internal and external harmonic conjugates C and D such that \|A T'\|^2 = \|AC\| \|AD\| = \|AB\| \|A M'\|.

.. figure:: f-51.svg
   :align: center
   :width: 88%

   Output of ``model.py`` for **F.51 (Apollonian Circles and the Problem of Apollonius)**.

Symbolic Construction Script (``model.py``)
-------------------------------------------

.. literalinclude:: model.py
   :language: python
