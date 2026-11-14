:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:
.. _about-fundamentals:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

*GEOMETOR fundamentals* establishes the constructive and axiomatic foundation of the GEOMETOR library, synthesizing classical synthetic, projective, harmonic, and compass-and-straightedge geometry through the archival corpus of :person:`Fred W. Seelig <seelig>`. Spanning 55 comprehensive geometric topics across 353 manuscript folios and 59 computational worksheets (*Triangles and Circles.ods*, *circumcircle-circumcenter.ods*, *triangle-basics-draw.ods*), this work investigates the core architecture of geometric order—from elementary Euclidean constructions and circle pencils to harmonic conjugates, pole-and-polar duality, and triangle center loci.

Every topic (:ref:`F.1 <f-01>` through :ref:`F.55 <f-55>`) is systematically extracted into an addressable 3-Track Book Codex. Track 1 (**Synthesis**) presents formal geometric enunciations, interactive SVG constructions with bidirectional hover highlighting, constructive signatures, and symbolic derivations on canonical reference configurations. Track 2 (**Folios**) preserves high-resolution primary archival scans (``0001.jpg``–``0353.jpg``) paired with diplomatic mathematical transcriptions. Track 3 (**Code**) provides standalone, executable Python scripts using :mod:`geometor.model` and :mod:`sympy` to verify all geometric and algebraic invariants to exact symbolic zero.

Within the broader GEOMETOR ecosystem, *fundamentals* serves as the operational bridge uniting classical axiomatic deduction with contemporary symbolic computation. It connects the foundational definitions and postulates of :cite:`Euclid's Elements <euclid_elements>` (:mod:`geometor.elements`) and projective configurations (:mod:`geometor.pappus`) to modern triangle center algebra in Kimberling's Encyclopedia of Triangle Centers (:cite:`Kimberling's ETC <kimberling_etc>`, :mod:`geometor.etc`). Through this synthesis, historical draftsmanship and handwritten mathematical notebooks are transformed into an executable geometric canon.

The GEOMETOR Mission
--------------------

Founded and directed by **phi ARCHITECT**, the GEOMETOR initiative is dedicated to the systematic digitization, symbolic formalization, and multi-medium re-articulation of classical geometric and axiomatic literature across 2,300+ years of mathematical history. GEOMETOR bridges historical philology and modern computational geometry through three structural pillars:

Extracting Historical Semantic Knowledge
    Moving beyond passive page scans and lossy optical character recognition (OCR), GEOMETOR recovers the living deductive architecture of classical, Renaissance, and modern mathematical treatises. Enunciations, geometric constructions, proof steps, axiomatic justifications, marginal citations, primary-source folios (rendered dynamically through ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams are converted into structured, machine-addressable semantic graphs.

Exact Symbolic Grounding (``geometor.model``)
    Eliminating floating-point approximation errors entirely, GEOMETOR anchors geometric constructions and center proofs in 100% exact symbolic algebra via :mod:`sympy` and Rational Trigonometry invariants (quadrance, spread, cross-ratio) evaluated over exact algebraic number fields. Every center, line concurrence, circle intersection, and tangency condition is verified to exact symbolic zero.

Repurposing Knowledge Across Mediums
    Extracted semantic and algebraic models are mobilized across synchronized multi-track Book Codices and EPUB 3 editions via ``photon-platform/publish``, computable deductive canons (:mod:`geometor.elements`, :mod:`geometor.etc`, :mod:`geometor.pappus`, :mod:`geometor.divine`), interactive SVG laboratories (:mod:`geometor.explorer`), high-definition visual broadcasts, and neuro-symbolic program synthesis engines (:mod:`geometor.seer`) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

This edition curates and computationally formalizes modern geometrical manuscripts:

Primary Sources
    * **Fred W. Seelig Archive**: Handwritten geometrical notebooks spanning 353 pages across 55 topical studies (:cite:`SeeligNotebooks`), accompanied by 59 computational worksheets in OpenDocument format (:cite:`SeeligSpreadsheets`).
    * **Classical References**: Historical connections to Euclid's *Elements* (:cite:`Euclid <euclid_elements>`), Apollonius's *Conics*, Pappus's *Collection*, and modern college geometry treatises.

Digital Scriptorium Methodology
    * **Three-Track Architecture**: Each study integrates formal synthetic exposition (:doc:`/topics/index`), high-resolution manuscript scans with folio transcriptions, and executable Python code models.
    * **Symbolic Grounding**: Constructions are evaluated using :mod:`geometor.model.Model` to ensure exact algebraic closure without numeric rounding errors.
    * **Apparatus**: For full bibliographical citations, see :doc:`/bibliography`; for biographical notes on figures cited throughout the archive, see :doc:`/persons`; and for the spreadsheet catalog, see :doc:`/spreadsheets/index`.
