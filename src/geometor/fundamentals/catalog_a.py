"""Catalog data for Topics F.1 through F.28 of GEOMETOR Fundamentals."""

from __future__ import annotations

TOPICS_1_TO_28: list[dict[str, object]] = [
    {
        "num": 1,
        "id": "F.1",
        "slug": "alberts-parabola",
        "legacy_folder": "01.albert-s-parabola",
        "title": "Albert's Parabola",
        "subtitle": "Tangent, Normal, and Depressed Cubic for Minimum Distance to a Parabola",
        "category": "Conics & Analytic Loci",
        "tags": ["parabola", "conics", "normal", "tangent", "cubic"],
        "enunciation": (
            "Given a parabola y = x^2 and a point P = (P_x, P_y) on it, the tangent line T "
            "and normal line N at P satisfy y = 2 P_x x - P_x^2 and y = -x/(2 P_x) + P_x^2 + 1/2; "
            "requiring N to pass through (M, 0) yields the depressed cubic P_x^3 + (1/2) P_x - M/2 = 0."
        ),
        "signature_given": ["V : Point", "F : Point", "directrix : Line", "P : Point"],
        "signature_steps": [
            "Q = foot(P, directrix)",
            "s_fp = segment(F, P)",
            "s_pq = segment(P, Q)",
            "tangent = bisector(F, P, Q)",
        ],
        "synthesis": [
            "In his April 2015 study *Albert's Parabola Problem* (Attempts #2 and #3, :cite:`SeeligNotebooks`), "
            "Fred W. Seelig investigates the tangent :g:`tangent` and normal :g:`N` to a :term:`parabola` in two "
            "coordinate frames: the vertex frame :math:`y = x^2` and the shifted directrix frame :math:`y = x^2 + 1` "
            "(where the :g:`directrix` is :math:`y = 0`, vertex :g:`V` is :math:`(0, 1)`, and focus :g:`F` is :math:`(0, 2)`).",
            "For :math:`y = x^2` at :g:`P` :math:`= (P_x, P_x^2)`, the tangent :g:`T` has double-intercept form "
            ":math:`x/(P_x/2) + y/(-P_x^2) = 1`, while the normal :g:`N` has :math:`x`-intercept "
            ":math:`M = 2 P_x (P_x^2 + 1/2)`. Setting :math:`M = 4` produces the depressed cubic "
            ":math:`P_x^3 + \\frac{1}{2}P_x - 2 = 0`, which simultaneously governs the minimum distance from a "
            "fixed point :math:`(M, 0)` on the directrix to a point :g:`Q` on the parabola.",
        ],
        "equations": [
            r"T:\; y = 2 P_x x - P_x^2, \qquad N:\; y = -\frac{x}{2 P_x} + \left(P_x^2 + \frac{1}{2}\right)",
            r"P_x^3 + \frac{1}{2} P_x - \frac{M}{2} = 0, \qquad r = \frac{P_x + 4 P_x^3}{4}",
        ],
        "depends_on": [],
        "euclid_refs": ["I.11", "I.12"],
        "elements_refs": ["G.3", "G.4"],
        "etc_refs": [],
        "spreadsheets": ["General Reference"],
        "folio_summaries": [
            (
                "Albert's Parabola Problem (Attempt #2, FWS Apr. 2015)",
                "Derives slope-intercept and double-intercept equations for tangent :math:`T` and normal :math:`N` to :math:`y = x^2`, records C.a.R. expressions, and reduces the normal intercept condition at :math:`(M,0)` (tested at :math:`M=4`) to the depressed cubic :math:`P_x^3 + \\frac{1}{2}P_x - 2 = 0`.",
            ),
            (
                "Albert's Parabola Problem — Attempt #3 (Directrix Frame)",
                "Shifts the parabola to :math:`y = x^2 + 1` with directrix :math:`y = 0`, vertex :math:`V(0,1)`, and focus :math:`F(0,2)`, and formulates the 3-step calculus minimization of :math:`d^2 = (P_x - Q_x)^2 + (P_y - Q_y)^2`.",
            ),
        ],
    },
    {
        "num": 2,
        "id": "F.2",
        "slug": "bilinear-transformations",
        "legacy_folder": "02.bilinear-transformations",
        "title": "Bilinear Transformations",
        "subtitle": "Projective Involutions, Derivative Identities, and the Apollonian Proportion",
        "category": "Projective & Harmonic Geometry",
        "tags": ["projective", "bilinear", "harmonic", "apollonius", "cross-ratio"],
        "enunciation": (
            "The canonical bilinear transformation B(x) = (1 + x)/(1 - x) and its inverse "
            "B^{-1}(y) = (y - 1)/(y + 1) link the internal division ratio kappa = x/r of a "
            "segment AB to the Apollonian distance ratio k = (1 + kappa)/(1 - kappa)."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point", "S : Point"],
        "signature_steps": [
            "D = harmonic_conjugate(A, B, C)",
            "l = line(A, B)",
            "l_prime = projective_image(S, l)",
        ],
        "synthesis": [
            "Dated December 5, 2013 and February 7, 2014 (:cite:`SeeligNotebooks`), Seelig's study of the "
            "canonical :term:`bilinear transformation` :math:`\\mathbb{B}(x) = \\frac{1+x}{1-x} = A(x)B(x)` "
            "(with :math:`A(x) = 1+x` and :math:`B(x) = (1-x)^{-1}`) establishes its differential identities "
            ":math:`\\mathbb{B}' = 2B^2 = B(1+\\mathbb{B})` and :math:`\\mathbb{B}'' = 4B^3`, together with "
            "the rectangular hyperbola conic equation :math:`x/4 - y/4 - xy/4 = 1/4` used for plotting in C.a.R.",
            "In Folios 7–8, Seelig connects :math:`k = \\mathbb{B}(\\kappa) = \\frac{1+\\kappa}{1-\\kappa}` "
            "directly to the Apollonian :term:`harmonic conjugate` division on segment :g:`A` :g:`B` of length :math:`d`, "
            "deriving the center :math:`M' = \\frac{d}{k^2-1}` and radius :math:`R = \\frac{dk}{k^2-1}` of the "
            ":term:`Apollonian circles` for :math:`k = 2, 3, 4`.",
        ],
        "equations": [
            r"\mathbb{B}(x) = \frac{1 + x}{1 - x}, \qquad \mathbb{B}^{-1}(y) = \frac{y - 1}{y + 1}, \qquad \mathbb{B}'(x) = \frac{2}{(1 - x)^2} = 2 B^2",
            r"k = \frac{|AC|}{|BC|} = \frac{1 + \kappa}{1 - \kappa} \iff \kappa = \frac{k - 1}{k + 1}, \qquad M' = \frac{d}{k^2 - 1}, \qquad R = \frac{d k}{k^2 - 1}",
        ],
        "depends_on": [],
        "euclid_refs": ["VI.3"],
        "elements_refs": ["G.5"],
        "etc_refs": [],
        "spreadsheets": ["Harmonic Conjugates", "Apollonian Circles", "HC Tables"],
        "folio_summaries": [
            (
                "Bilinear Transformation & Derivatives",
                "Defines :math:`\\mathbb{B}(1,x) = \\frac{1+x}{1-x} = A(x)B(x)`, derives :math:`\\mathbb{B}' = 2B^2` and :math:`\\mathbb{B}'' = 4B^3`, and plots the hyperbola with vertical asymptote :math:`x = 1`.",
            ),
            (
                "Inverse Transformation & Unit Square Grid",
                "Plots :math:`\\mathbb{B}(x)` and :math:`\\mathbb{B}^{-1}(y) = \\frac{y-1}{y+1}` on a unit-square grid and re-verifies :math:`\\mathbb{B}' = B(1+\\mathbb{B}) = 2B^2`.",
            ),
            (
                "Second Derivative Forms & C.a.R. Conic Fit (FWS 12/5/2013)",
                "Expresses :math:`\\mathbb{B}''` in two algebraic forms and derives the C.a.R. conic curve equation :math:`x/4 - y/4 - xy/4 = 1/4`.",
            ),
            (
                "Table 1 for B(x) & Inverse Derivatives",
                "Tabulates :math:`x, A, B, \\mathbb{B}, \\mathbb{B}'` for :math:`x \\in \\{-1, 0, 1/2, -1/3, 3\\}` and differentiates :math:`\\mathbb{B}^{-1}(y)`.",
            ),
            (
                "Table 2 for B^{-1}(y) & Conic Fit",
                "Tabulates :math:`y, A, B, \\mathbb{B}^{-1}, {\\mathbb{B}^{-1}}'` for :math:`y \\in \\{0, 1, 2, 3, 4\\}` and records the C.a.R. conic equation :math:`-x/4 + y/4 - xy/4 = 1/4`.",
            ),
            (
                "Bilinear Transformation — Scaling Properties",
                "Sets up the scaling relation :math:`\\mathbb{B}(R, \\eta x) = \\mathbb{B}(1, x)`.",
            ),
            (
                "Apollonian Proportion (FWS 2/7/2014)",
                "Applies :math:`k = \\frac{1+\\kappa}{1-\\kappa}` to harmonic points :math:`A, C, B, D` with :math:`B=0, A=-d`, deriving :math:`C = -d/(k+1), D = d/(k-1), M' = d/(k^2-1)`, and :math:`R = dk/(k^2-1)`.",
            ),
            (
                "Apollonian Circles for k = 2, 3, 4",
                "Tabulates and sketches the nested Apollonian circles with :math:`(M', R) = (\\frac{1}{3}d, \\frac{2}{3}d), (\\frac{1}{8}d, \\frac{3}{8}d), (\\frac{1}{15}d, \\frac{4}{15}d)`.",
            ),
        ],
    },
    {
        "num": 3,
        "id": "F.3",
        "slug": "biquadratic-forms-in-herons-formula",
        "legacy_folder": "03.biquadratic-forms-in-heron-s-formula",
        "title": "Biquadratic Forms in Heron's Formula",
        "subtitle": "Symmetric Quadratic Substitutions, Circumcircle Families, and Extremal Side Lengths",
        "category": "Algebraic & Coordinate Systems",
        "tags": ["heron", "area", "biquadratic", "circumradius", "sympy"],
        "enunciation": (
            "Under the linear substitution X = a/2, W = (b + c)/2, and Y = (c - b)/2, "
            "Heron's area formula reduces to the biquadratic product K = sqrt((W^2 - X^2)(X^2 - Y^2))."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "a = segment(B, C)",
            "b = segment(C, A)",
            "c = segment(A, B)",
            "H_C = foot(C, c)",
            "h_c = segment(C, H_C)",
        ],
        "synthesis": [
            "In Topic 03 (:cite:`SeeligNotebooks`), Seelig reformulates :term:`Heron's formula` "
            ":math:`K = \\sqrt{s(s-a)(s-b)(s-c)}` by introducing the symmetric half-sums and half-differences "
            ":math:`X = a/2`, :math:`W = (b+c)/2`, and :math:`Y = (c-b)/2 = -Z`. Because :math:`s = W + X`, "
            ":math:`s - a = W - X`, :math:`s - b = X + Y`, and :math:`s - c = X - Y`, the squared area "
            "collapses immediately into the biquadratic difference of squares :math:`K^2 = (W^2 - X^2)(X^2 - Y^2)`.",
            "Seelig then studies a triangle inscribed in a circle of constant circumradius :math:`R` with fixed "
            "chord :math:`c` and varying side :math:`a`, expressing :math:`b(a; c, R)` via the Law of Sines and "
            "solving the stationarity condition via polynomial division of :math:`(x^3 - y^3)/(x - y)` to obtain "
            "the extremal relation :math:`{z_i^*}^2 = w_i^2 + w_i w_i' + {w_i'}^2`.",
        ],
        "equations": [
            r"X = \frac{a}{2}, \quad W = \frac{b + c}{2}, \quad Y = \frac{c - b}{2} \implies K = \sqrt{(W^2 - X^2)(X^2 - Y^2)}",
            r"16 K^2 = 2 a^2 b^2 + 2 b^2 c^2 + 2 c^2 a^2 - a^4 - b^4 - c^4, \qquad {z_i^*}^2 = w_i^2 + w_i w_i' + {w_i'}^2",
        ],
        "depends_on": [],
        "euclid_refs": ["I.47", "II.12", "II.13"],
        "elements_refs": ["G.1", "G.3"],
        "etc_refs": ["X(1)", "X(3)", "X(4)"],
        "spreadsheets": [
            "General Reference",
            "5-6-7 A,B,C",
            "Biquadratic Heron",
            "Circumcircle Solver",
        ],
        "folio_summaries": [
            (
                "Biquadratic Forms in Heron's Formula",
                "Introduces :math:`K = \\sqrt{s(s-a)(s-b)(s-c)}` for a triangle inscribed in a circle of radius :math:`R` with constant :math:`c` and varying :math:`a`.",
            ),
            (
                "Symmetric Substitutions W, X, Y, Z",
                "Defines :math:`X = a/2, W = (b+c)/2, Y = (-b+c)/2, Z = (b-c)/2` to reduce Heron's formula to :math:`K = \\sqrt{(W^2 - X^2)(X^2 - Y^2)}`.",
            ),
            (
                "Three Circumcircle Diagrams",
                "Compass-and-straightedge constructions showing perpendicular bisector distances :math:`h_A, h_B, h_C`, circumradii :math:`R`, and central angle :math:`2\\beta`.",
            ),
            (
                "Circumcircle Trigonometry & Law of Sines",
                "Records :math:`a/2 = R\\sin\\alpha, b/2 = R\\sin\\beta, c/2 = R\\sin\\gamma` and :math:`R^2 = h_C^2 + (c/2)^2`.",
            ),
            (
                "Finding Sidelength b(a; c, R)",
                "Derives :math:`b = 2R\\sin(180^\\circ - (\\sin^{-1}\\frac{a}{2R} + \\sin^{-1}\\frac{c}{2R}))` for fixed chord :math:`c` and circumradius :math:`R`.",
            ),
            (
                "Heron's Formula Grouped Around b/2",
                "Factors :math:`K = \\sqrt{[(b/2)^2 - ((a-c)/2)^2][((a+c)/2)^2 - (b/2)^2]}`.",
            ),
            (
                "Differentiation for Critical Value z*",
                "Differentiates :math:`f(z) = T_1 + T_2 + T_3 - \\sqrt{3}E` where :math:`T_i = \\sqrt{((w_i/z)^2 - 1)(1 - (w_i'/z)^2)}`.",
            ),
            (
                "Polynomial Division & Closed Form for z*",
                "Uses :math:`(x^3 - y^3)/(x - y) = x^2 + xy + y^2` to prove :math:`{z_i^*}^2 = w_i^2 + w_i w_i' + {w_i'}^2`.",
            ),
            (
                "Numerical Evaluation & Means of z_1*, z_2*, z_3*",
                "Computes :math:`z_1^* = \\sqrt{91/4} \\approx 4.77, z_2^* = \\sqrt{57/4} \\approx 3.775, z_3^* = \\sqrt{21} \\approx 4.583` and compares their harmonic ($4.330$), geometric ($4.353$), and arithmetic ($4.376$) means.",
            ),
        ],
    },
    {
        "num": 4,
        "id": "F.4",
        "slug": "carnots-theorem",
        "legacy_folder": "04.carnot-s-theorem",
        "title": "Carnot's Theorem",
        "subtitle": "Signed Distances from the Circumcenter to the Sides and the Japanese Theorem",
        "category": "Triangle Centers & Classical Lines",
        "tags": ["carnot", "circumcenter", "incenter", "inradius", "circumradius"],
        "enunciation": (
            "In any triangle ABC, the sum of the signed perpendicular distances from the "
            "circumcenter O to the three sides BC, CA, AB equals the sum of the circumradius "
            "R and the inradius r: d_a + d_b + d_c = R + r."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "O = circumcenter(A, B, C)",
            "I = incenter(A, B, C)",
            "M_A = midpoint(B, C)",
            "M_B = midpoint(C, A)",
            "M_C = midpoint(A, B)",
            "d_a = segment(O, M_A)",
            "d_b = segment(O, M_B)",
            "d_c = segment(O, M_C)",
        ],
        "synthesis": [
            "Attributed to :person:`Lazare Carnot <carnot>` (1753–1823), :term:`Carnot's theorem` links the "
            "perpendicular distances :g:`d_a`, :g:`d_b`, :g:`d_c` from the :term:`circumcenter` :g:`O` :math:`= X(3)` "
            "to the side midpoints :g:`M_A`, :g:`M_B`, :g:`M_C` directly to the circumradius :math:`R` and inradius :math:`r` "
            "around the :term:`incenter` :g:`I` :math:`= X(1)`.",
            "Seelig highlights the signed distance convention: :math:`d_m` is positive when :math:`O M_m` lies wholly "
            "inside :math:`\\triangle ABC` and negative when :g:`O` lies outside the corresponding side (as in an obtuse "
            "triangle where :math:`-OH_A + OH_B + OH_C = R + r`). As an immediate corollary, Seelig illustrates the "
            "**Japanese Theorem for cyclic polygons**: the sum of the inradii of the triangles in any triangulation of "
            "a cyclic polygon is invariant.",
        ],
        "equations": [
            r"\sum_{m \in \{A, B, C\}} d_m = d_a + d_b + d_c = R(\cos\alpha + \cos\beta + \cos\gamma) = R + r",
        ],
        "depends_on": ["F.3", "F.11", "F.28"],
        "euclid_refs": ["III.20", "IV.4", "IV.5"],
        "elements_refs": ["G.3"],
        "etc_refs": ["X(1)", "X(3)"],
        "spreadsheets": [
            "General Reference",
            "Circumcircle-Circumcenter",
            "Incircle-Incenter",
        ],
        "folio_summaries": [
            (
                "Carnot's Theorem & The Japanese Theorem",
                "States Lazare Carnot's signed-distance relation :math:`\\sum d_m = R + r` with an obtuse-triangle circumcircle diagram (:math:`-OH_A + OH_B + OH_C = R + r`) and two triangulated cyclic polygon diagrams illustrating the invariance of the sum of inradii.",
            ),
        ],
    },
    {
        "num": 5,
        "id": "F.5",
        "slug": "centers-of-similitude",
        "legacy_folder": "05.centers-of-similitude",
        "title": "Centers of Similitude",
        "subtitle": "Internal and External Homothetic Centers Dividing the Line of Centers Harmonically",
        "category": "Projective & Harmonic Geometry",
        "tags": ["similitude", "homothety", "harmonic", "circles", "tangents"],
        "enunciation": (
            "Given two circles (O_1, r_1) and (O_2, r_2) separated by center distance d = |O_1 O_2| "
            "with r_2 > r_1, their common internal and external tangents concur at the internal and "
            "external centers of similitude S_IN and S_EX, which divide O_1 O_2 harmonically in the ratio r_1 : r_2."
        ),
        "signature_given": ["O_1 : Point", "R_1 : Point", "O_2 : Point", "R_2 : Point"],
        "signature_steps": [
            "C_1 = circle(O_1, R_1)",
            "C_2 = circle(O_2, R_2)",
            "S_IN = internal_similitude(O_1, R_1, O_2, R_2)",
            "S_EX = external_similitude(O_1, R_1, O_2, R_2)",
        ],
        "synthesis": [
            "Citing Volume I, p. 207 of his geometry notebooks (:cite:`SeeligNotebooks`), Seelig constructs the "
            ":term:`centers of similitude` of two circles :g:`C_1` :math:`(O_1, r_1)` and :g:`C_2` :math:`(O_2, r_2)` "
            "separated by :math:`d = |O_1 O_2|`. The internal center :g:`S_IN` (:math:`S_{IN}`) and external center "
            ":g:`S_EX` (:math:`S_{EX}`) divide the segment :math:`O_1 O_2` internally and externally in the exact "
            "ratio :math:`r_1 : r_2`, forming a four-point :term:`harmonic conjugate` range :math:`(O_1, O_2; S_{IN}, S_{EX})`.",
        ],
        "equations": [
            r"|O_1 S_{IN}| = d \frac{r_1}{r_2 + r_1}, \qquad |S_{IN} O_2| = d \frac{r_2}{r_2 + r_1}",
            r"|S_{EX} O_1| = d \frac{r_1}{r_2 - r_1}, \qquad |S_{EX} O_2| = d \frac{r_2}{r_2 - r_1}",
        ],
        "depends_on": ["F.2"],
        "euclid_refs": ["VI.2", "VI.4"],
        "elements_refs": ["G.3"],
        "etc_refs": ["X(55)", "X(56)"],
        "spreadsheets": ["Centers of Similitude"],
        "folio_summaries": [
            (
                "Centers of Similitude (Vol. I, p. 207)",
                "Dimensioned construction of circles :math:`(O_1, r_1)` and :math:`(O_2, r_2)` with common internal tangents meeting at :math:`S_{IN}` and common external tangents meeting at :math:`S_{EX}`, deriving the four exact distance formulas in terms of :math:`d, r_1, r_2`.",
            ),
        ],
    },
    {
        "num": 6,
        "id": "F.6",
        "slug": "centroid",
        "legacy_folder": "06.centroid",
        "title": "Centroid",
        "subtitle": "Concurrency of the Medians, Vector Average, and the Medial Triangle",
        "category": "Triangle Centers & Classical Lines",
        "tags": ["centroid", "medians", "medial-triangle", "barycentric"],
        "enunciation": (
            "The three medians AM_A, BM_B, CM_C joining the vertices of triangle ABC to the "
            "midpoints of the opposite sides concur at the centroid G = X(2), which divides "
            "each median in a 2 : 1 ratio and has homogeneous barycentric coordinates 1 : 1 : 1."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "M_A = midpoint(B, C)",
            "M_B = midpoint(C, A)",
            "M_C = midpoint(A, B)",
            "m_a = segment(A, M_A)",
            "m_b = segment(B, M_B)",
            "m_c = segment(C, M_C)",
            "G = intersect(m_a, m_b)",
        ],
        "synthesis": [
            "The :term:`centroid` :g:`G` :math:`= X(2)` is the center of mass of :math:`\\triangle ABC` and the "
            "concurrency point of the three median cevians :g:`m_a`, :g:`m_b`, :g:`m_c` meeting the opposite side "
            "midpoints :g:`M_A`, :g:`M_B`, :g:`M_C` (:cite:`SeeligNotebooks`).",
            "Connecting the midpoints forms the **medial triangle** :math:`\\triangle M_A M_B M_C`, which is "
            "homothetic to :math:`\\triangle ABC` with center :g:`G` and scale factor :math:`-1/2`, partitioning "
            ":math:`\\triangle ABC` into four congruent subtriangles of area :math:`K/4`. On the canonical "
            ":math:`(5, 6, 7)` triangle, :g:`G` has Cartesian coordinates :math:`(13/3, 4\\sqrt{6}/7) \\approx (4.3333, 1.3997)`.",
        ],
        "equations": [
            r"\vec{G} = \frac{\vec{A} + \vec{B} + \vec{C}}{3}, \qquad G = (1 : 1 : 1) \text{ in homogeneous barycentrics}",
            r"m_a^2 = \frac{2 b^2 + 2 c^2 - a^2}{4}, \qquad m_b^2 = \frac{2 c^2 + 2 a^2 - b^2}{4}, \qquad m_c^2 = \frac{2 a^2 + 2 b^2 - c^2}{4}",
        ],
        "depends_on": ["F.3"],
        "euclid_refs": ["I.10", "VI.2"],
        "elements_refs": ["G.3"],
        "etc_refs": ["X(2)"],
        "spreadsheets": ["General Reference", "Centroid", "5-6-7 A,B,C"],
        "folio_summaries": [
            (
                "Centroid Definition & Vector Average",
                "Draws :math:`\\triangle ABC` with congruent-tick-marked midpoints and medians concurring at :math:`G`, defining the centroid as the concurrency of median cevians.",
            ),
            (
                "The Medial Triangle M_A M_B M_C",
                "Constructs the medial triangle :math:`\\triangle M_A M_B M_C` inscribed in :math:`\\triangle ABC` together with medians meeting at :math:`G`.",
            ),
        ],
    },
    {
        "num": 7,
        "id": "F.7",
        "slug": "ceva-and-menelaus",
        "legacy_folder": "07.ceva-and-menalaus",
        "title": "Ceva and Menelaus",
        "subtitle": "Concurrent Cevians, Collinear Transversals, the MNIJ Lattice Framework, and Cevian Programs",
        "category": "Projective & Harmonic Geometry",
        "tags": ["ceva", "menelaus", "cevians", "harmonic", "gergonne", "stewart"],
        "enunciation": (
            "Three cevians AD, BE, CF of triangle ABC concur at a point P if and only if "
            "(AF/FB)(BD/DC)(CE/EA) = +1 (Ceva's Theorem), whereas points D, E, F' on the "
            "sidelines are collinear if and only if (AF'/F'B)(BD/DC)(CE/EA) = -1 (Menelaus's Theorem), "
            "making (A, B; F, F') a harmonic range."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point", "P : Point"],
        "signature_steps": [
            "D = intersect(line(A, P), line(B, C))",
            "E = intersect(line(B, P), line(C, A))",
            "F = intersect(line(C, P), line(A, B))",
            "F' = intersect(line(D, E), line(A, B))",
        ],
        "synthesis": [
            "Spanning 26 folios (:cite:`SeeligNotebooks`), Topic 07 is one of the richest investigations in the "
            "Seelig archive. Combining :term:`Ceva's theorem` (:person:`Giovanni Ceva <ceva>`, :math:`+1`) and "
            ":term:`Menelaus's theorem` (:person:`Menelaus <menelaus>`, :math:`-1`), Seelig demonstrates that the "
            "cevian trace :g:`F` and the trilinear polar intersection :g:`F'` divide side :g:`A` :g:`B` in a "
            ":term:`harmonic conjugate` range :math:`AF/FB = AF'/BF'`. In Folio 1 (`FWS 2011/11/07`), he applies "
            "Ceva's Theorem to equal tangent segments :math:`x = s-a, y = s-b, z = s-c` to prove the concurrency "
            "of the Gergonne point :math:`G_e = X(7)`.",
            "Across Folios 2–22, Seelig develops the **MNIJ coordinate system** (:math:`A=(0,0), B=(M,0), C=(I,J)`, "
            "with :math:`y`-intercept :math:`N = JM/(M-I)`), deriving closed-form rational expressions for the "
            "Cartesian trace coordinates :g:`D`, :g:`E`, :g:`F`, the cevian lengths :math:`d, e, f` via "
            ":term:`Stewart's theorem`, the trilinear area of the cevian triangle :math:`\\triangle DEF`, and a "
            "complete HP-35s calculator program (`FWS 8/25/2014`) verified on :math:`(a,b,c) = (6,9,13)` and "
            "on a Heronian :math:`(78, 90, 84)` triangle (`April 14, 2015`).",
        ],
        "equations": [
            r"\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = +1 \quad (\text{Ceva}), \qquad \frac{AF'}{F'B} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = -1 \quad (\text{Menelaus})",
            r"D_x = \frac{M J P}{J P + (M - I) Q}, \qquad E_x = \frac{M I Q}{I Q + (M - P) J}, \qquad F_x = \frac{I Q - J P}{Q - J}",
            r"\frac{PD}{AD} + \frac{PE}{BE} + \frac{PF}{CF} = 1, \qquad \frac{AP}{AD} + \frac{BP}{BE} + \frac{CP}{CF} = 2",
        ],
        "depends_on": ["F.2", "F.6"],
        "euclid_refs": ["VI.2"],
        "elements_refs": ["G.3", "G.5"],
        "etc_refs": ["X(1)", "X(2)", "X(7)", "X(8)"],
        "spreadsheets": [
            "Ceva & Menelaus",
            "Ceva",
            "Menelaus",
            "Ceva Compare",
            "6-9-13 Cevian",
        ],
        "folio_summaries": [
            (
                "Gergonne Point Concurrency via Ceva's Theorem (FWS 2011/11/07)",
                "Proves that the cevians to the incircle touchpoints :math:`D=T_A, E=T_B, F=T_C` concur at the Gergonne point :math:`G_e = X(7)` using equal tangent lengths :math:`x, y, z`.",
            ),
            (
                "Ceva's & Menelaus' Theorem — Integer Segments",
                "Side-by-side comparison of Ceva (:math:`+1`) and Menelaus (:math:`-1`) showing that :math:`(A, B; F, F')` form a harmonic range.",
            ),
            (
                "MNIJ Coordinate Framework for Integer Cevians",
                "Places :math:`A=(0,0), B=(M,0), C=(I,J)` with :math:`BC` intercept :math:`N = JM/(M-I)` to construct integer-segment Ceva configurations.",
            ),
            (
                "Pythagorean Triple Gluing Table",
                "Tabulates scaled Pythagorean right triangles (:math:`3\\text{–}4\\text{–}5, 6\\text{–}8\\text{–}10, 33\\text{–}56\\text{–}65`) sharing a common altitude :math:`J`.",
            ),
            (
                "Cut The Knot IMO Cevian Ratio Problem (FWS 2015/4/12)",
                "Uses parallel lines and similar triangles to evaluate :math:`PF/PC + PD/PA` given :math:`AF/BF = 1/3` and :math:`CD/BD = 1/2`.",
            ),
            (
                "Length of Cevian to Intouch Point",
                "Applies the Law of Cosines to compute the cevian lengths from vertices to the incircle touchpoints.",
            ),
            (
                "Stewart's Theorem for Cevians d, e, f",
                "Derives :math:`d^2 = \\frac{x b^2 + y c^2}{a} - xy` for all three cevians in terms of side splits.",
            ),
            (
                "Lattice Triangle Example (I=8, J=8, M=24, P=(12,4))",
                "Computes exact trace coordinates :math:`D, E, F` and verifies Ceva's product :math:`\\frac{16}{8}\\cdot\\frac{3/5}{2/5}\\cdot\\frac{2}{6} = +1`.",
            ),
            (
                "Heronian 78-90-84 Triangle Problem (Facebook, April 14, 2015)",
                "Constructs the :math:`78\\text{–}90\\text{–}84` Heronian triangle with trace splits :math:`(28,56), (39,39), (60,30)` and exact cevian lengths :math:`3\\sqrt{673}, 6\\sqrt{137}, 14\\sqrt{23}`.",
            ),
            (
                "Continuation of Heronian Cevian Calculations",
                "Completes the Stewart's theorem verification for :math:`AD, BE, CF` on the :math:`78\\text{–}90\\text{–}84` triangle.",
            ),
            (
                "Cevian Triangle DEF Side Lengths & Area in Trilinears",
                "Records exact formulas for :math:`|EF|, |FD|, |DE|` and :math:`\\text{Area}(\\triangle DEF)` in trilinear coordinates :math:`\\tau_A : \\tau_B : \\tau_C`.",
            ),
            (
                "Sub-Cevian Harmonic & Barycentric Identities",
                "Proves :math:`\\frac{AP}{PD} = \\frac{AE}{EC} + \\frac{AF}{FB}`, :math:`\\sum \\frac{PD}{AD} = 1`, and :math:`\\sum \\frac{AP}{AD} = 2`.",
            ),
            (
                "MNIJ Line Equations L_A, L_B, L_C, L_D, L_E, L_F",
                "Derives intercept equations for the three sidelines and three cevians through :math:`P(P, Q)`.",
            ),
            (
                "Exact Cartesian Coordinates of Traces D, E, F",
                "Solves the :math:`2\\times 2` linear intersections for :math:`D = L_D \\cap L_A`, :math:`E = L_E \\cap L_B`, and :math:`F = L_F \\cap L_C`.",
            ),
            (
                "Cevian Lengths d, e, f in MNIJ Coordinates",
                "Expresses :math:`d = |AD|, e = |BE|, f = |CF|` and vertex distances :math:`d_A, d_B, d_C` in terms of :math:`M, N, I, J, P, Q`.",
            ),
            (
                "Subtriangle Areas & Side Splits",
                "Computes the six side segments and six subtriangle areas around interior point :math:`P`.",
            ),
            (
                "Summary of MNIJ Cevian Formulas",
                "Consolidates trace coordinates, lengths, and Ceva ratio checks onto a reference sheet.",
            ),
            (
                "Cevian HP-35s Program Specification (1/, FWS 8/25/2014)",
                "Defines inputs, outputs, and equations for the HP-35s calculator program solving general cevians.",
            ),
            (
                "HP-35s Memory Register Map A–Z (2/, FWS 8/25/2014)",
                "Maps all 26 calculator registers `A`–`Z` to triangle and cevian parameters.",
            ),
            (
                "HP-35s Program Flow Diagram (3/)",
                "Flowchart of subroutine branches for computing trace points and cevian lengths.",
            ),
            (
                "Worked Test Case: 6-9-13 Triangle with P=(9,1) (Part 1)",
                "Evaluates :math:`I = 107/13 \\approx 8.23, J = 8\\sqrt{35}/13 \\approx 3.64, N \\approx 9.92`, and trace coordinates :math:`D(11.35, 1.26), E(4.69, 2.08), F(9.29, 0)`.",
            ),
            (
                "Worked Test Case: 6-9-13 Triangle (Part 2)",
                "Computes cevian lengths :math:`d = 11.42, e = 8.57, f = 3.79` and verifies Ceva's theorem.",
            ),
            (
                "Worked Test Case: 6-9-13 Triangle (Part 3)",
                "Cross-checks sub-cevian ratios and subtriangle areas against the Excel workbook.",
            ),
            (
                "Menelaus Worked Example on 20-23-31 Triangle",
                "Given :math:`AF = 20, AF' = 50, BD = DC = 10`, solves Menelaus's relation for :math:`CE/EA = 19/50` (:math:`CE \\approx 8.74`).",
            ),
            (
                "Circumcircles of Subtriangles APB, BPC, CPA",
                "Notes properties of the three circles passing through :math:`P` and pairs of triangle vertices.",
            ),
            (
                "Master Summary Sheet (Vol. 1, p. 128 & cevian analysis.xls)",
                "Compiles Ceva, Menelaus, Van Aubel, and mass-point identities linked to `cevian analysis.xls`.",
            ),
        ],
    },
    {
        "num": 8,
        "id": "F.8",
        "slug": "chord-intersection",
        "legacy_folder": "08.chord-intersection",
        "title": "Chord Intersection",
        "subtitle": "Intersecting Chords Theorem, Sagitta Formula, Power of a Point, and Ptolemy's Bound",
        "category": "Circle Geometry & Pencils",
        "tags": ["chords", "power-of-a-point", "sagitta", "ptolemy", "circles"],
        "enunciation": (
            "If two chords AB and CD of a circle (O, R) intersect at a point X at distance "
            "r = |OX| from the center, then the product of their segments is constant and "
            "equals the power of X with respect to the circle: |AX|*|BX| = |CX|*|DX| = R^2 - |OX|^2."
        ),
        "signature_given": [
            "O : Point",
            "A : Point",
            "B : Point",
            "C : Point",
            "D : Point",
        ],
        "signature_steps": [
            "circle = circle(O, A)",
            "AB = segment(A, B)",
            "CD = segment(C, D)",
            "P = intersect(AB, CD)",
            "AC = segment(A, C)",
            "DB = segment(D, B)",
        ],
        "synthesis": [
            "In Topic 08 (:cite:`SeeligNotebooks`), Seelig proves the Intersecting Chords Theorem "
            "(:cite:`EuclidElements`, Proposition III.35) via the similarity of :math:`\\triangle AXC \\sim \\triangle DXB` "
            "(matching :g:`AC` and :g:`DB` across intersection :g:`P`) and equates the common product to the "
            ":term:`power of a point` :math:`R^2 - |OX|^2`.",
            "He illustrates the theorem with two numerical problems: computing the sagitta "
            ":math:`x = \\frac{5(3-\\sqrt{5})}{2} \\approx 1.91` of a chord of length :math:`10` in a circle of "
            "diameter :math:`15`, and solving :math:`x(10-x) = 4\\cdot 4 \\implies x = 2, 8` where :math:`R^2 - |OX|^2 = 16`, "
            "noting that the inscribed quadrilateral :math:`ACBD` satisfies :person:`Ptolemy <ptolemy>`'s relation "
            ":math:`AC\\cdot BD + AD\\cdot BC = AB\\cdot CD = 80`.",
        ],
        "equations": [
            r"|AX| \cdot |BX| = |CX| \cdot |DX| = R^2 - |OX|^2, \qquad x_{\text{sagitta}} = R - \sqrt{R^2 - \left(\frac{c}{2}\right)^2}",
        ],
        "depends_on": [],
        "euclid_refs": ["III.35", "III.36"],
        "elements_refs": ["G.3"],
        "etc_refs": [],
        "spreadsheets": ["Chord Intersection"],
        "folio_summaries": [
            (
                "Sagitta of a Chord in a Circle of Diameter 15",
                "Computes the sagitta :math:`x = \\frac{15}{2} - \\sqrt{(15/2)^2 - 5^2} = \\frac{5(3-\\sqrt{5})}{2} \\approx 1.91` for a chord of length 10.",
            ),
            (
                "Intersecting Chords Problem (m = 8, n = 10)",
                "Solves :math:`4\\cdot 4 = x(10-x) \\implies x = 2, 8` and sets up isosceles triangles :math:`\\triangle OAB` and :math:`\\triangle OCD` to find :math:`|OX| = r`.",
            ),
            (
                "Proof via Similar Triangles & Power of Point X",
                "Proves :math:`AX\\cdot BX = CX\\cdot DX` from :math:`\\triangle AXC \\simeq \\triangle DXB` and equates it to :math:`R^2 - |OX|^2`.",
            ),
            (
                "Concentric Circles & Ptolemy's Formula (CRC, p. 10)",
                "Shows that :math:`R^2 - |OX|^2 = 16` with :math:`2R \\ge 10` leaves one degree of freedom (the angle between chords) and applies Ptolemy's theorem :math:`AC\\cdot BD + AD\\cdot BC = 80`.",
            ),
        ],
    },
    {
        "num": 9,
        "id": "F.9",
        "slug": "circle-equations",
        "legacy_folder": "09.circle-equations",
        "title": "Circle Equations",
        "subtitle": "Three-Circle Distance Systems in a Square and a Sangaku Tangent Circle Problem",
        "category": "Circle Geometry & Pencils",
        "tags": ["circles", "analytic-geometry", "sangaku", "square", "radical-axis"],
        "enunciation": (
            "Pairwise subtraction of Cartesian circle equations (x - u_i)^2 + (y - v_i)^2 = r_i^2 "
            "eliminates the quadratic terms x^2 + y^2 to yield linear radical-axis relations, "
            "determining both the side Z of a square from three corner distances and the radius "
            "of a Sangaku circle tangent to an inscribed square and equilateral triangle."
        ),
        "signature_given": [
            "O : Point",
            "A : Point",
            "B : Point",
            "C : Point",
            "D : Point",
        ],
        "signature_steps": [
            "circle = circle(O, A)",
            "AB = segment(A, B)",
            "CD = segment(C, D)",
            "P = intersect(AB, CD)",
        ],
        "synthesis": [
            "In Topic 09 (:cite:`SeeligNotebooks`), Seelig examines two multi-circle systems in Cartesian coordinates. "
            "In Folios 1–4 (`FWS 9/24/2014`), an interior point :math:`P(P, Q)` inside a square :math:`ABCD` of side :math:`Z` "
            "has distances :math:`PA = 3, PB = 5, PD = 7`. Subtracting the three circle equations yields "
            ":math:`-2ZP + Z^2 = 40`, :math:`-2ZQ + Z^2 = 16`, and :math:`2Z(Q - P) = 24`.",
            "In Folios 5–8 (`Posted Sept. 28, 2014`), Seelig models a **Sangaku problem** posed by Tony Garcia: "
            "inside a circle :math:`\\Gamma_O(R)` containing a rotated square :math:`ACBD` of side :math:`\\sqrt{2}R`, "
            "an equilateral triangle :math:`\\triangle ACE`, and circular arcs :math:`\\widehat{AB}` and :math:`\\widehat{CD}`, "
            "he derives the center :math:`P_y = \\frac{r_F^2 - r_I^2}{2(F_y - I_y)}` and radius :math:`r` of the "
            "inscribed circle tangent to both the triangle sides and the circular arcs.",
        ],
        "equations": [
            r"x^2 + y^2 = 9, \quad x^2 + (y - Z)^2 = 25, \quad (x - Z)^2 + y^2 = 49 \implies 2 Z (Q - P) = 24",
            r"l_{AE}:\; y = \sqrt{3}x - \frac{\sqrt{2}}{2}R, \qquad P_y = \frac{r_F^2 - r_I^2}{2(F_y - I_y)}",
        ],
        "depends_on": ["F.8"],
        "euclid_refs": ["I.47", "III.35"],
        "elements_refs": ["G.3"],
        "etc_refs": [],
        "spreadsheets": ["General Reference", "Radical Axes"],
        "folio_summaries": [
            (
                "Equations of Circles in a Square of Side Z (Part 1)",
                "Sets up :math:`x^2+y^2=9`, :math:`x^2+(y-Z)^2=25`, and :math:`(x-Z)^2+(y-Z)^2=49` for interior point :math:`P` in square :math:`ABCD`.",
            ),
            (
                "Semicircle Geometric Mean Representation (Part 2)",
                "Represents :math:`P^2` and :math:`Q^2` as geometric mean altitudes in semicircles of radii 3, 5, and 7.",
            ),
            (
                "Pairwise Subtraction of Circle Equations (Part 3)",
                "Subtracts the circle equations for :math:`PA=3, PB=5, PD=7` to obtain :math:`2Z(Q-P) = 24`.",
            ),
            (
                "Quadratic Solution for P, Q, and Z (FWS 9/24/2014)",
                "Evaluates :math:`P = \\frac{3}{2}(\\sqrt{3}-1) \\approx 1.09808, Q = 3\\sqrt{\\sqrt{3}/2} \\approx 2.79181`, and :math:`Z = 7.08492`.",
            ),
            (
                "Tony Garcia / Sangaku Problem Setup (Posted Sept. 28, 2014)",
                "Draws circle :math:`\\Gamma_O(R)`, inscribed square :math:`ACBD` of side :math:`\\sqrt{2}R`, equilateral triangle :math:`\\triangle ACE`, and inscribed tangent circle :math:`\\Gamma_P(r)`.",
            ),
            (
                "Line Equation for Side AE of Equilateral Triangle ACE",
                "Derives :math:`y = \\sqrt{3}x - \\frac{\\sqrt{2}}{2}R` for side :math:`AE`.",
            ),
            (
                "Circle Equation for Arc CD Centered at B",
                "Writes :math:`(x - \\frac{\\sqrt{2}}{2}R)^2 + (y - \\frac{\\sqrt{2}}{2}R)^2 = 2R^2` for arc :math:`\\widehat{CD}`.",
            ),
            (
                "Equating r^2 at Tangent Points F and I",
                "Solves for the Sangaku circle center ordinate :math:`P_y = \\frac{r_F^2 - r_I^2}{2(F_y - I_y)}`.",
            ),
        ],
    },
    {
        "num": 10,
        "id": "F.10",
        "slug": "circles-and-geometric-mean",
        "legacy_folder": "10.circles-and-geometric-mean",
        "title": "Circles and Geometric Mean",
        "subtitle": "Right-Triangle Altitude Mean Proportional, Square Partitions, and Barycentric Center Table",
        "category": "Circle Geometry & Pencils",
        "tags": ["geometric-mean", "semicircle", "thales", "barycentric", "circles"],
        "enunciation": (
            "In a semicircle on diameter AB = m + n, the perpendicular altitude h = CH from "
            "a point C on the circumference to AB is the geometric mean sqrt(m*n) of the "
            "segments AH = m and HB = n, while the radius OC = (m + n)/2 is their arithmetic mean."
        ),
        "signature_given": ["A : Point", "B : Point", "H : Point"],
        "signature_steps": [
            "O = midpoint(A, B)",
            "semicircle = circle(O, B)",
            "C = perpendicular_chord(H, AB, semicircle)",
            "G = segment(C, H)",
            "A_mean = segment(O, C)",
        ],
        "synthesis": [
            "By Thales's theorem and :cite:`EuclidElements` VI.13, any point :g:`C` on the :g:`semicircle` with "
            "diameter :g:`A` :g:`B` forms a right angle :math:`\\angle ACB = 90^\\circ`. Dropping the altitude "
            ":g:`G` (:math:`CH`) to :g:`H` on :g:`A` :g:`B` creates similar right triangles "
            ":math:`\\triangle ACH \\sim \\triangle CBH`, proving :math:`CH = \\sqrt{AH \\cdot HB}` (:term:`geometric mean`).",
            "In Topic 10 (:cite:`SeeligNotebooks`), Seelig applies this semicircle geometric mean identity "
            ":math:`P^2 = (r + Q)(r - Q)` to the three-circle square partition problem and compiles an early "
            "summary table of normalized homogeneous :term:`barycentric coordinates` for :math:`I, O, H, X(7), X(8), X(6), X(5)`.",
        ],
        "equations": [
            r"G = |CH| = \sqrt{m n}, \qquad A_{\text{mean}} = |OC| = \frac{m + n}{2}, \qquad H_{\text{mean}} = |CK| = \frac{2 m n}{m + n}",
        ],
        "depends_on": ["F.8", "F.9"],
        "euclid_refs": ["II.14", "III.31", "VI.8", "VI.13"],
        "elements_refs": ["G.3", "G.4"],
        "etc_refs": ["X(1)", "X(3)", "X(4)", "X(5)", "X(6)", "X(7)", "X(8)"],
        "spreadsheets": ["General Reference", "Harmonic Conjugates"],
        "folio_summaries": [
            (
                "Equations of Circles & Geometric Mean",
                "Expresses :math:`P^2 = (3+Q)(3-Q)` and :math:`P^2 = (5+(Z-Q))(5-(Z-Q))` as semicircle geometric means and derives :math:`Z(Q-P) = 12` and :math:`Q = \\frac{Z^2-16}{2Z}`.",
            ),
            (
                "Area Partition of Square ABCD into Four Rectangles",
                "Partitions the square of area :math:`Z^2` around :math:`P(P, Q)` into four rectangles ①–④ and relates their dimensions to the circle equations.",
            ),
            (
                "Homogeneous Barycentric Coordinates Table for I, O, H, Ge, Na, K, N",
                "Lists normalized HBC formulas in terms of :math:`S = a^2+b^2+c^2` and :math:`x, y, z`, noting `* This expression not found in ETC` for :math:`H = (S-2b^2)(S-2c^2)/D`.",
            ),
            (
                "Quadratic Maximization Exercise",
                "Differentiates :math:`f(t) = -16t^2 + 64t + 80` to find its maximum :math:`f(2) = 144`.",
            ),
        ],
    },
    {
        "num": 11,
        "id": "F.11",
        "slug": "circumcenter",
        "legacy_folder": "11.circumcenter",
        "title": "Circumcenter",
        "subtitle": "Perpendicular Bisectors, Cartesian Determinant Formulas, Circumcircle Subtriangles, and the Tangential Triangle",
        "category": "Triangle Centers & Classical Lines",
        "tags": ["circumcenter", "circumcircle", "tangential-triangle", "barycentric"],
        "enunciation": (
            "The perpendicular bisectors of the three sides of triangle ABC concur at the "
            "circumcenter O = X(3), equidistant from A, B, C by the circumradius R = abc/(4K), "
            "with homogeneous barycentric coordinates a^2 S_A : b^2 S_B : c^2 S_C."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "M_A = midpoint(B, C)",
            "M_B = midpoint(C, A)",
            "M_C = midpoint(A, B)",
            "perp_a = perpendicular(M_A, line(B, C))",
            "perp_b = perpendicular(M_B, line(C, A))",
            "O = intersect(perp_a, perp_b)",
            "circumcircle = circle(O, A)",
        ],
        "synthesis": [
            "Dated May 25 and May 31, 2011 (:cite:`SeeligNotebooks`), Seelig's study of the :term:`circumcenter` "
            ":g:`O` :math:`= X(3)` derives the exact Cartesian coordinates :math:`(x_0, y_0)` from vertex coordinates "
            "(correcting a sign error in Joseph O'Rourke's published formula), transcribes Christopher Morley's poem "
            "*'A circle is a happy thing to be'*, and decomposes :math:`\\triangle ABC` into the three isosceles "
            "circumcircle subtriangles :math:`\\triangle AOB, \\triangle BOC, \\triangle COA` of altitudes "
            ":math:`h_C = \\sqrt{R^2 - (c/2)^2}`.",
            "In Folios 5–6, Seelig constructs the **tangential triangle** bounded by the tangent lines to the "
            ":g:`circumcircle` at :g:`A`, :g:`B`, :g:`C`, contrasting the acute case (where the tangential triangle "
            "encloses :math:`\\triangle ABC`) with the obtuse case. On the canonical :math:`(5, 6, 7)` triangle, "
            ":math:`R = \\frac{35\\sqrt{6}}{24} \\approx 3.57217` and :math:`O = (7/2, 5\\sqrt{6}/18) \\approx (3.5, 0.6804)`.",
        ],
        "equations": [
            r"R = \frac{a b c}{4 K}, \qquad O = \left(a^2 S_A : b^2 S_B : c^2 S_C\right) = \left(\sin 2\alpha : \sin 2\beta : \sin 2\gamma\right)",
            r"D = 2\left[x_A(y_C - y_B) + x_B(y_A - y_C) + x_C(y_B - y_A)\right], \qquad x_0 = \frac{\sum (x_A^2 + y_A^2)(y_C - y_B)}{D}",
        ],
        "depends_on": ["F.3"],
        "euclid_refs": ["III.1", "IV.5"],
        "elements_refs": ["G.3", "G.4"],
        "etc_refs": ["X(3)", "X(26)"],
        "spreadsheets": [
            "Circumcircle-Circumcenter",
            "Circumcircle Solver",
            "General Reference",
        ],
        "folio_summaries": [
            (
                "Circumcenter of a Triangle (FWS 5/31/2011)",
                "Summary sheet with circumcircle diagram and Cartesian formulas for :math:`a, b, c, s, A_T, R = abc/(4A_T)`, and :math:`(x_0, y_0)`.",
            ),
            (
                "Poem by Christopher Morley (1890–1957)",
                "Handwritten transcription of Morley's 6-line geometric poem *'A circle is a happy thing to be'*.",
            ),
            (
                "Sign Correction of O'Rourke's Formula (FWS 5/25/2011)",
                "Derives :math:`(O_x, O_y)` from perpendicular bisector intersections and corrects the sign error in Joseph O'Rourke's formula.",
            ),
            (
                "Circumcircle Subtriangles",
                "Decomposes :math:`K = K_A + K_B + K_C = \\frac{1}{2}\\sum a\\sqrt{R^2 - (a/2)^2}` using central angles :math:`\\Phi_C = 2\\gamma` and subtriangle semiperimeters :math:`s_C = (2R+c)/2`.",
            ),
            (
                "Tangential Triangle Drawings (Acute vs. Obtuse)",
                "Side-by-side compass-and-straightedge constructions of the tangential triangle for an acute triangle and an obtuse triangle.",
            ),
            (
                "Properties of the Tangential Triangle",
                "Explanatory notes defining the tangential triangle formed by the tangents to the circumcircle at :math:`A, B, C`.",
            ),
        ],
    },
    {
        "num": 12,
        "id": "F.12",
        "slug": "coaxial-circles",
        "legacy_folder": "12.coaxial-circles",
        "title": "Coaxial Circles",
        "subtitle": "Equipotential Pencils Around Point Charges, Limiting Points, and Orthogonal Families",
        "category": "Circle Geometry & Pencils",
        "tags": [
            "coaxial-circles",
            "radical-axis",
            "apollonius",
            "electromagnetics",
            "ogilvy",
        ],
        "enunciation": (
            "A hyperbolic pencil of coaxial circles with limiting points L_1 = (-r, 0) and "
            "L_2 = (+r, 0) coincides with the Apollonian equipotential circles d_1 / d_2 = k "
            "around two point charges Q_1, Q_2, sharing the y-axis as their common radical axis."
        ),
        "signature_given": ["L_1 : Point", "L_2 : Point", "R_1 : Point", "R_2 : Point"],
        "signature_steps": [
            "radical_axis = line(R_1, R_2)",
            "line_of_centers = line(L_1, L_2)",
            "C_1 = coaxial_circle(L_1, L_2, -3.5)",
            "C_2 = coaxial_circle(L_1, L_2, 2.5)",
        ],
        "synthesis": [
            "Inspired by electrostatic equipotential contours around fixed point charges :math:`Q_1(-r, 0)` and "
            ":math:`Q_2(+r, 0)` in Kraus's *Electromagnetics* and :person:`C. Stanley Ogilvy <ogilvy>`'s "
            "*Excursions in Geometry* (:cite:`Ogilvy1969`), Seelig's 12-folio study (`Friday April 24, 2015`, "
            ":cite:`SeeligNotebooks`) unifies :term:`coaxial circles`, :term:`harmonic conjugate` division, "
            ":term:`radical axis` theory, and :term:`Apollonian circles`.",
            "For potential ratio :math:`k = Q_1/Q_2 = d_1/d_2 = 2`, Seelig determines six landmark points "
            ":math:`P_1,\\dots,P_6` on the equipotential circle: the internal and external harmonic division points "
            ":math:`P_1 = (\\frac{1}{3}r, 0)` and :math:`P_2 = (3r, 0)`, center :math:`M' = (\\frac{5}{3}r, 0)`, "
            "radius :math:`R = \\frac{4}{3}r`, vertical chord endpoints :math:`P_3, P_4 = (r, \\pm \\frac{2}{\\sqrt{3}}r)`, "
            "and right-triangle vertices :math:`P_5, P_6` on the circle :math:`x^2 + y^2 = 2r^2`.",
        ],
        "equations": [
            r"P_1 = \left(\frac{k - 1}{k + 1}r,\, 0\right), \qquad P_2 = \left(\frac{k + 1}{k - 1}r,\, 0\right), \qquad M' = \frac{k^2 + 1}{k^2 - 1}r, \qquad R = \frac{2 k}{k^2 - 1}r",
            r"x^2 + y^2 - 2 c_x x + r^2 = 0, \qquad E_{\text{TOT}} = k Q_1 \frac{x - x_1}{|x - x_1|^3} + k Q_2 \frac{x - x_2}{|x - x_2|^3} = 0",
        ],
        "depends_on": ["F.2", "F.8"],
        "euclid_refs": ["III.35", "III.36"],
        "elements_refs": ["G.3"],
        "etc_refs": [],
        "spreadsheets": [
            "Coaxial Circles",
            "Coaxal Circle Table",
            "Apollonian Circles",
            "Radical Axes",
        ],
        "folio_summaries": [
            (
                "Coaxal Circles & Electromagnetics Introduction",
                "Introduces coaxal circles via equipotentials around two charges (:math:`K = Q_1/Q_2 = 2`), citing Stanley Ogilvy and Wikipedia, with radical axis :math:`\\eta = 1`.",
            ),
            (
                "Template Table for K = 2",
                "Sets up table columns :math:`\\eta, R, MM'` for :math:`\\eta \\in \\{1, 1/2, 1/3, 2/3, 1/4, 3/4\\}` and their reciprocals.",
            ),
            (
                "Plan of Attack (Friday April 24, 2015)",
                "Outlines the HP-35s `COAXAL CIRCLES` program, Excel verification, Kraus EMag comparison, and synthesis with harmonic conjugates, radical axes, and pole-polar duality (for Vol. II, p. 280).",
            ),
            (
                "Numerical Table for k = 1/2, 1/3, 1/4",
                "Computes :math:`r-x, C, AC/BC, X, Y, Z, M'`, and :math:`R` on segment :math:`AB`.",
            ),
            (
                "Six Landmark Points P_1..P_6 on the Equipotential Circle",
                "Defines :math:`P_1..P_6` around charges :math:`Q_1(-r,0)` and :math:`Q_2(+r,0)` on blue grid paper.",
            ),
            (
                "Table of Algebraic Transforms (1)–(5)",
                "Catalogs the five fractional linear transforms relating :math:`k, a, x` and :math:`y^2 = (2r)^2/(k^2-1)`.",
            ),
            (
                "Exact Coordinates for k = 2 (P_1, P_2, M', R, P_3, P_4)",
                "Derives :math:`P_1 = (\\frac{1}{3}r, 0), P_2 = (3r, 0), R = \\frac{4}{3}r, M' = \\frac{5}{3}r`, and :math:`P_3, P_4 = (r, \\pm \\frac{2}{\\sqrt{3}}r)`.",
            ),
            (
                "Right-Triangle Locus for P_5, P_6",
                "Proves that right triangles :math:`\\triangle Q_1 P_5 Q_2` satisfy :math:`d_1^2 + d_2^2 = (2r)^2`, lying on the circle :math:`x^2 + y^2 = 2r^2` of radius :math:`\\sqrt{2}r`.",
            ),
            (
                "1D Collinear Electric Field Vector Formulation",
                "Writes :math:`E_i = k Q_i (x - x_i)/|x - x_i|^3` to preserve vector sign along the line of charges.",
            ),
            (
                "Zero-Field Point Between Like Charges",
                "Sets :math:`E_{\\text{TOT}} = 0` for :math:`+Q_1, +Q_2` and forms the cubic/absolute-value ratio.",
            ),
            (
                "Sign Interval Analysis for x_1 < x < x_2",
                "Tests sign cases of :math:`x - x_1` and :math:`x - x_2` across the three collinear intervals.",
            ),
            (
                "Alternative Coordinate Setup (-d/2, +d/2)",
                "Solves for :math:`P_1` with charges at :math:`\\pm d/2` and potential ratio :math:`V_1/V_2 = 1/2`.",
            ),
        ],
    },
    {
        "num": 13,
        "id": "F.13",
        "slug": "compare-triangles-in-circles",
        "legacy_folder": "13.compare-triangles-in-circles",
        "title": "Compare Triangles in Circles",
        "subtitle": "Inscribed Triangle Area with Fixed Chord and Circumradius, Nested Radical Chords, and Isosceles Decomposition",
        "category": "Circle Geometry & Pencils",
        "tags": ["circumcircle", "chords", "area", "nested-radicals", "medians"],
        "enunciation": (
            "For a family of triangles ABC inscribed in a fixed circle of radius R sharing a "
            "fixed chord AB = c (with central angle 2*phi where sin(phi) = c/(2R)), the area K "
            "decomposes into the signed sum of three central isosceles triangles: "
            "K = (1/2) c h_c + (1/2) a h_a - (1/2) b h_b."
        ),
        "signature_given": [
            "O : Point",
            "A : Point",
            "B : Point",
            "C : Point",
            "D : Point",
        ],
        "signature_steps": [
            "circle = circle(O, A)",
            "AB = segment(A, B)",
            "AC = segment(A, C)",
            "BC = segment(B, C)",
        ],
        "synthesis": [
            "Complementing Topic 03 (:ref:`F.3 <f-03>`), Seelig's 8-folio study in Topic 13 (:cite:`SeeligNotebooks`) "
            "tracks how the area :math:`K = (\\triangle ABC)` and side lengths :math:`a(\\theta; R), b(\\theta; R)` "
            "behave as vertex :g:`C` moves around a fixed circumcircle :math:`\\Gamma_R` above a fixed chord :math:`AB = c`.",
            "In Folio 3, he tabulates exact nested-radical chord lengths :math:`|BC| = \\frac{\\sqrt{2n^2 \\pm 2n\\sqrt{n^2-m^2}}}{n}` "
            "for :math:`c/R = 2m/n \\in [1/4, 7/4]`. In Folio 5, he highlights a result marked *'Surprise & pretty'*: "
            "decomposing :math:`(\\triangle ABC) = \\frac{1}{2}ch_c + \\frac{1}{2}ah_a - \\frac{1}{2}bh_b` into three "
            "isosceles triangles with common apex at the circumcenter :g:`O`.",
        ],
        "equations": [
            r"\sin\phi = \frac{c}{2 R}, \qquad h_c = \sqrt{R^2 - \left(\frac{c}{2}\right)^2}, \qquad (ABC) = \frac{1}{2} c h_c + \frac{1}{2} a h_a - \frac{1}{2} b h_b",
            r"a^2 = f^2 + \frac{c^2}{4} + f c \cos\theta, \qquad b^2 = f^2 + \frac{c^2}{4} - f c \cos\theta",
        ],
        "depends_on": ["F.3", "F.8", "F.11"],
        "euclid_refs": ["III.20", "IV.5"],
        "elements_refs": ["G.3"],
        "etc_refs": ["X(3)"],
        "spreadsheets": ["Circumcircle Solver", "Circumcircle-Circumcenter"],
        "folio_summaries": [
            (
                "Area K/R^2 vs. Sidelength a Curves",
                "Sketches qualitative plots of normalized area :math:`K/R^2` vs. :math:`a` (peaking when :math:`a` is a diameter) and :math:`b` vs. :math:`a`.",
            ),
            (
                "Compass Construction of Chord Families in Circle of Radius R",
                "Draws vertical chords for :math:`c/R \\in \\{1/2, 3/4, 1, 4/3, 3/2, \\sqrt{3}, 7/4, 2\\}` and an inscribed triangle :math:`\\triangle ABC`.",
            ),
            (
                "Nested Radical Table for c/R from 1/4 to 7/4",
                "Tabulates :math:`c/R, m/n = c/(2R), \\sqrt{n^2-m^2}/n`, and exact nested radicals for :math:`|BC|`.",
            ),
            (
                "Equations for a(theta; R) and b(theta; R) via Median f",
                "Uses median :math:`f = |MC|` at angle :math:`\\theta` to :math:`AB` to express :math:`a^2` and :math:`b^2`.",
            ),
            (
                "Isosceles Decomposition Around Circumcenter O ('Surprise & Pretty')",
                "Proves :math:`(ABC) = \\frac{1}{2}ch_c + \\frac{1}{2}ah_A - \\frac{1}{2}bh_B` and writes the Bretschneider/Brahmagupta area of quadrilateral :math:`ABCO`.",
            ),
            (
                "Area as a Function of Angles alpha, beta and R",
                "Poses the question of expressing :math:`K = (\\triangle ABC)` directly in terms of :math:`\\alpha, \\beta, R`.",
            ),
            (
                "Quadrilateral OABC Partitioned by Median f",
                "Decomposes :math:`OABC` into :math:`(OAM) + (OMC) + (MBC)` sharing median base :math:`f = MC`.",
            ),
            (
                "Clean Compass Construction of Cyclic Quadrilateral ABCO",
                "Draws cyclic quadrilateral :math:`ABCO` with three equal sides :math:`R, R, R`, chords :math:`c, a`, and diagonal :math:`b`.",
            ),
        ],
    },
    {
        "num": 14,
        "id": "F.14",
        "slug": "conway-notation",
        "legacy_folder": "14.conway-notation",
        "title": "Conway Notation",
        "subtitle": "John H. Conway's Algebraic Triangle Symbols, Brocard Angle, and Altitude Partitions",
        "category": "Algebraic & Coordinate Systems",
        "tags": ["conway", "barycentric", "brocard", "altitudes", "stewart"],
        "enunciation": (
            "In John H. Conway's triangle notation, setting S = 2K (twice the area of triangle ABC), "
            "S_omega = (a^2 + b^2 + c^2)/2, and S_A = (b^2 + c^2 - a^2)/2, S_B = (c^2 + a^2 - b^2)/2, "
            "S_C = (a^2 + b^2 - c^2)/2 reduces trigonometric and barycentric identities to polynomial "
            "expressions satisfying S_B S_C + S_C S_A + S_A S_B = S^2."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "H = orthocenter(A, B, C)",
            "O = circumcenter(A, B, C)",
            "G = centroid(A, B, C)",
            "Euler = line(O, H)",
        ],
        "synthesis": [
            ":person:`John H. Conway <conway>`'s algebraic notation (:term:`Conway triangle notation`) is the "
            "primary symbolic language used across Seelig's notebooks and Paul Yiu's *Introduction to the Geometry "
            "of the Triangle* (:cite:`Yiu2001`, :cite:`SeeligNotebooks`).",
            "In Folios 1–2, Seelig evaluates all Conway invariants on his canonical reference triangle "
            ":math:`(a, b, c) = (5, 6, 7)`: :math:`K = 6\\sqrt{6}`, :math:`S = 12\\sqrt{6}`, :math:`S_\\omega = 55`, "
            ":math:`S_A = 30`, :math:`S_B = 19`, :math:`S_C = 6`, altitude :math:`J = h_c = \\frac{12\\sqrt{6}}{7}`, "
            "projection :math:`I = \\frac{30}{7}`, :math:`y`-intercept :math:`N = \\frac{84}{19}\\sqrt{6}`, and "
            "fractional base splits :math:`k_c = \\frac{30}{49}` and :math:`k_c' = \\frac{19}{49}`.",
        ],
        "equations": [
            r"S = 2 K, \qquad S_\omega = \frac{a^2 + b^2 + c^2}{2} = S \cot\omega, \qquad S_A = \frac{b^2 + c^2 - a^2}{2} = b c \cos\alpha",
            r"S^2 = b^2 c^2 - S_A^2 = S_A S_B + S_B S_C + S_C S_A, \qquad S_A S_B S_C = S^2 (S_\omega - 4 R^2)",
        ],
        "depends_on": ["F.3"],
        "euclid_refs": ["II.12", "II.13"],
        "elements_refs": ["G.3"],
        "etc_refs": ["X(2)", "X(3)", "X(4)", "X(6)"],
        "spreadsheets": [
            "General Reference",
            "Conway's Conversions",
            "5-6-7 A,B,C",
            "Barycentric",
        ],
        "folio_summaries": [
            (
                "Conway Notation Definitions, Trig Functions & Identities",
                "Defines :math:`S = 2K, S_\\omega = S\\cot\\omega, S_A, S_B, S_C` and records the fundamental quadratic and cubic Conway identities.",
            ),
            (
                "Worked Evaluation on the 5-6-7 Reference Triangle (Part 1)",
                "Computes :math:`K = 6\\sqrt{6}, S = 12\\sqrt{6}, S_\\omega = 55, S_A = 30, S_B = 19, S_C = 6`, and vertex coordinates :math:`(I, J) = (30/7, 12\\sqrt{6}/7)`.",
            ),
            (
                "Intercept N and Altitude Splits on the 5-6-7 Triangle (Part 2)",
                "Finds the :math:`y`-intercept :math:`N = \\frac{84}{19}\\sqrt{6} \\approx 10.829` and altitude base fractions :math:`k_c = 30/49, k_c' = 19/49`.",
            ),
            (
                "Stewart's Theorem for Altitudes in Conway Notation",
                "Substitutes :math:`h_c = 2K/c` into :math:`a^2 k_c + b^2 k_c' - c^2 k_c k_c' = h_c^2` to solve for :math:`k_c`.",
            ),
            (
                "Alternative Sum-of-Squares Notation (S = a^2 + b^2 + c^2)",
                "Rewrites the cosine law and altitude quadratic using :math:`S \\triangleq a^2+b^2+c^2` and :math:`P \\triangleq abc`.",
            ),
            (
                "Clean Reference Card for Conway Symbols",
                "Summarizes :math:`S_A, S_B, S_C` as offsets from :math:`(a^2+b^2+c^2)/2`.",
            ),
        ],
    },
    {
        "num": 15,
        "id": "F.15",
        "slug": "cyclic-quadrilateral",
        "legacy_folder": "15.cyclic-quadrilateral",
        "title": "Cyclic Quadrilateral",
        "subtitle": "Golden-Ratio Chords for Angles theta, 2*theta, 3*theta, 4*theta, Ptolemy's Theorem, and Geometric Progression Impossibility",
        "category": "Circle Geometry & Pencils",
        "tags": [
            "cyclic-quadrilateral",
            "ptolemy",
            "golden-ratio",
            "chords",
            "polygons",
        ],
        "enunciation": (
            "A cyclic quadrilateral WXYZ whose interior angles form the arithmetic progression "
            "theta, 2*theta, 3*theta, 4*theta has theta = 36 degrees (W = 36, X = 72, Y = 144, Z = 108) "
            "and golden-ratio diagonals |XZ| = 2 sin(36) = sqrt(3 - phi) and |WY| = 2 sin(72) = phi*sqrt(3 - phi) "
            "in the unit circle; by contrast, no non-trivial cyclic quadrilateral can have interior angles "
            "in geometric progression theta, k*theta, k^2*theta, k^3*theta."
        ),
        "signature_given": [
            "O : Point",
            "A : Point",
            "B : Point",
            "C : Point",
            "D : Point",
        ],
        "signature_steps": [
            "circumcircle = circle(O, A)",
            "ABCD = polygon(A, B, C, D)",
            "e = segment(A, C)",
            "f = segment(B, D)",
            "P = intersect(e, f)",
        ],
        "synthesis": [
            "Written in April 2015 (:cite:`SeeligNotebooks`), Seelig's 16-folio investigation of the "
            ":term:`cyclic quadrilateral` :math:`WXYZ` explores three distinct problems. First, when the interior "
            "angles are :math:`\\theta, 2\\theta, 3\\theta, 4\\theta`, the opposite-angle supplementary law "
            "(:cite:`EuclidElements` III.22) forces the ordering :math:`W = 36^\\circ, X = 72^\\circ, Y = 144^\\circ, Z = 108^\\circ`, "
            "so the diagonals :g:`e` and :g:`f` in a unit circle have exact :term:`golden ratio` lengths "
            ":math:`|XZ| = 2\\sin 36^\\circ = \\sqrt{3-\\phi}` and :math:`|YW| = 2\\sin 72^\\circ = \\phi\\sqrt{3-\\phi}`.",
            "Second, when the *central* angles are :math:`\\theta, 2\\theta, 3\\theta, 4\\theta` (:math:`\\theta = 36^\\circ`), "
            "the sides and diagonals are :math:`a = \\phi - 1, c = \\phi, |WY| = \\phi, |XZ| = 2`. Third, in Folios 15–16 "
            "(*'An Open Cyclic Quadrilateral Problem'*), Seelig proves that no non-square cyclic quadrilateral can "
            "have interior angles in geometric progression :math:`\\theta, k\\theta, k^2\\theta, k^3\\theta` because "
            "the resulting supplementary cubics :math:`k^3 \\mp k^2 \\mp k \\pm 1 = 0` have only roots :math:`\\pm 1, \\pm i`.",
        ],
        "equations": [
            r"\theta + 2\theta + 3\theta + 4\theta = 360^\circ \implies \theta = 36^\circ, \qquad f = |XZ| = 2\sin 36^\circ = \sqrt{3 - \phi}, \qquad e = |YW| = 2\sin 72^\circ = \phi\sqrt{3 - \phi}",
            r"a c + b d = e f \quad (\text{Ptolemy}), \qquad (k^3 - k^2 + k - 1) = (k - 1)(k^2 + 1) = 0",
        ],
        "depends_on": ["F.8"],
        "euclid_refs": ["III.21", "III.22", "IV.11"],
        "elements_refs": ["G.3"],
        "etc_refs": [],
        "spreadsheets": ["Cyclic Quad", "Chord Intersection"],
        "folio_summaries": [
            (
                "Cyclic Quad with Angles theta, 2*theta, 3*theta, 4*theta (Cropped Copy, FWS 2015/4/9)",
                "Tabulates the four central isosceles triangles :math:`\\triangle WOX, \\triangle XOY, \\triangle YOZ, \\triangle ZOW` and sets the goal of finding :math:`|OP|`.",
            ),
            (
                "Cyclic Quad with Angles theta, 2*theta, 3*theta, 4*theta (Full Title, FWS 2015/4/9)",
                "Uncropped master page showing full title and central/inscribed angle relations.",
            ),
            (
                "Base Angle Equalities M = K, N = L & Butterfly Similarity (Page 2)",
                "Deduces :math:`M = K` and :math:`N = L` and applies :math:`\\triangle ZPW \\simeq \\triangle YPX`.",
            ),
            (
                "Inscribed Angles 36, 72, 144, 108 in Unit Circle (FWS Begun April 6, 2015)",
                "Establishes :math:`\\theta = 36^\\circ` and vertex ordering :math:`W=36^\\circ, X=72^\\circ, Y=144^\\circ, Z=108^\\circ` so opposite angles sum to :math:`180^\\circ`.",
            ),
            (
                "Diagonal |XZ| = 2 sin 36 = sqrt(3 - phi) (Page 2)",
                "Computes midpoint distance :math:`|OM_1| = \\cos 36^\\circ = \\phi/2` and chord :math:`|XZ| = \\sqrt{3-\\phi} \\approx 1.1756`.",
            ),
            (
                "Power of Diagonal Intersection P (Page 3, citing Vol. I, pp. 265–270)",
                "Relates :math:`d = |OP|` to diagonal segments :math:`m = |PX|, n = |PZ|` via :math:`r^2 = d^2 + mn`.",
            ),
            (
                "Diagonal |YW| = 2 sin 72 = phi*sqrt(3 - phi) (Page 4)",
                "Computes :math:`|OM_2| = \\cos 72^\\circ \\approx 0.3090` and :math:`|YW| = \\phi\\sqrt{3-\\phi} \\approx 1.9021`.",
            ),
            (
                "Non-Cyclic Trap When Angles Are Ordered Sequentially",
                "Shows that if :math:`W=36^\\circ, X=72^\\circ, Y=108^\\circ, Z=144^\\circ` in order around the perimeter, :math:`W + Y \\ne 180^\\circ` so :math:`WXYZ` is not cyclic.",
            ),
            (
                "Empirical C.a.R. Measurements of Side Lengths & Central Angles",
                "Records C.a.R. values :math:`a=1.93, b=1.09, c=0.11, d=1.87` and central angles :math:`150^\\circ, 66^\\circ, 6^\\circ, 138^\\circ`.",
            ),
            (
                "Central Angles in Arithmetic Progression (36, 72, 108, 144)",
                "Places vertices at :math:`e^{j0}, e^{j\\theta}, e^{j3\\theta}, e^{j6\\theta}`, obtaining golden-ratio sides :math:`a = \\phi-1, c = \\phi` and diagonals :math:`|WY| = \\phi, |XZ| = 2`.",
            ),
            (
                "Four Central Isosceles Triangles OWX, OXY, OYZ, OZW",
                "Isolated sketches of the four central sector triangles and their base angles.",
            ),
            (
                "Vector Construction of the Non-Cyclic Quadrilateral",
                "Constructs the non-cyclic quadrilateral with :math:`WX = 1` and comments on ambiguous problem statements.",
            ),
            (
                "Ptolemy's Theorem & Parameterization by Angle mu (Part 1)",
                "Normalizes diagonal :math:`WY = 1` and applies the Law of Sines and Ptolemy's theorem :math:`ac + bd = |XZ|`.",
            ),
            (
                "Product-to-Sum Reduction for |XZ| (Part 2)",
                "Expresses :math:`|XZ|` in terms of :math:`\\cos(2\\mu - 72^\\circ)` and :math:`\\cos(252^\\circ - 2\\mu)`.",
            ),
            (
                "An Open Cyclic Quadrilateral Problem (Fred Seelig, April 2015)",
                "Poses the question of whether a cyclic quadrilateral can have interior angles in geometric progression :math:`\\theta, k\\theta, k^2\\theta, k^3\\theta`.",
            ),
            (
                "Impossibility Proof via Cubic Factorization",
                "Proves that :math:`k^3 - k^2 - k + 1 = 0`, :math:`k^3 - k^2 + k - 1 = 0`, and :math:`k^3 + k^2 - k - 1 = 0` have only roots :math:`\\pm 1, \\pm i`, ruling out any non-trivial geometric progression.",
            ),
        ],
    },
    {
        "num": 16,
        "id": "F.16",
        "slug": "dalembert",
        "legacy_folder": "16.d-alembert",
        "title": "d'Alembert's Theorem",
        "subtitle": "Monge–d'Alembert Collinearity of the Six Centers of Similitude of Three Circles",
        "category": "Projective & Harmonic Geometry",
        "tags": ["dalembert", "monge", "similitude", "projective", "apollonius"],
        "enunciation": (
            "Given three circles of distinct radii in the plane, their six pairwise internal "
            "and external centers of similitude lie by threes on four projective lines "
            "L_{+++}, L_{--+}, L_{-+-}, and L_{+--} (the Monge–d'Alembert similitude axes)."
        ),
        "signature_given": [
            "O_1 : Point",
            "R_1 : Point",
            "O_2 : Point",
            "R_2 : Point",
            "O_3 : Point",
        ],
        "signature_steps": [
            "C_1 = circle(O_1, R_1)",
            "C_2 = circle(O_2, R_2)",
            "C_3 = circle(O_3, R_3)",
            "S_12 = external_similitude(C_1, C_2)",
            "S_23 = external_similitude(C_2, C_3)",
            "dAlembert_axis = line(S_12, S_23)",
        ],
        "synthesis": [
            "Building on Topic 05 (:ref:`F.5 <f-05>`), Seelig's multi-color constructions in Topic 16 (:cite:`SeeligNotebooks`) "
            "illustrate the theorem of :person:`d'Alembert <dalembert>` and Gaspard Monge: for three circles "
            ":math:`\\Gamma_A, \\Gamma_B, \\Gamma_C`, the three external :term:`centers of similitude` "
            ":math:`S_{\\text{EX }AB}, S_{\\text{EX }AC}, S_{\\text{EX }BC}` are collinear on axis :math:`L_{+++}`, "
            "while each external center is collinear with the two complementary internal centers on :math:`L_{--+}, L_{-+-}, L_{+--}`.",
            "In Folios 3–4, Seelig connects these four similitude axes to Gergonne's solution of the **Problem of "
            "Apollonius** (finding the 8 circles simultaneously tangent to :math:`\\Gamma_A, \\Gamma_B, \\Gamma_C`) and "
            "executes a compass construction of five mutually tangent circles (inner and outer Soddy circles).",
        ],
        "equations": [
            r"L_{+++}:\; \{S_{\text{EX}\,AB},\, S_{\text{EX}\,BC},\, S_{\text{EX}\,CA}\}, \qquad L_{+--}:\; \{S_{\text{EX}\,AB},\, S_{\text{IN}\,BC},\, S_{\text{IN}\,CA}\}",
        ],
        "depends_on": ["F.5"],
        "euclid_refs": ["VI.2", "VI.4"],
        "elements_refs": ["G.3"],
        "etc_refs": [],
        "spreadsheets": ["Centers of Similitude"],
        "folio_summaries": [
            (
                "D'Alembert's Theorem Multi-Color Constructions",
                "Two constructions with red external tangent cones and green internal tangent cones whose apexes lie on thick black collinearity lines.",
            ),
            (
                "The Four Similitude Axes L_{+++}, L_{--+}, L_{-+-}, L_{+--}",
                "Grid-paper drawing of circles :math:`A, B, C` showing all 6 centers of similitude and all 4 Monge–d'Alembert axes.",
            ),
            (
                "Connection to the Problem of Apollonius",
                "Lists the 6 similitude centers and sets up the `X`/`I` tangency state table for circles tangent to :math:`\\Gamma_A, \\Gamma_B, \\Gamma_C`.",
            ),
            (
                "Compass Construction of Mutually Tangent Soddy Circles",
                "Precision compass drawing of three mutually tangent circles enclosed by an outer tangent circle and surrounding a small inner tangent circle.",
            ),
        ],
    },
    {
        "num": 17,
        "id": "F.17",
        "slug": "ellipse",
        "legacy_folder": "17.ellipse",
        "title": "Ellipse",
        "subtitle": "Seven-Step Five-Circle Compass Oval Construction and Focus-Directrix Conic Relations",
        "category": "Conics & Analytic Loci",
        "tags": [
            "ellipse",
            "conics",
            "compass-construction",
            "eccentricity",
            "latus-rectum",
        ],
        "enunciation": (
            "Given semi-major axis a and semi-minor axis b, a four-center circular-arc oval "
            "approximating the ellipse x^2/a^2 + y^2/b^2 = 1 is constructed by a 7-step "
            "five-circle compass procedure, while the exact conic satisfies F = a*e, d = a/e, "
            "and vertex mean proportional V = a = sqrt(d*F)."
        ),
        "signature_given": ["O : Point", "A_1 : Point", "A_2 : Point", "B_1 : Point"],
        "signature_steps": [
            "F_1 = focus_left(O, A_2, B_1)",
            "F_2 = focus_right(O, A_2, B_1)",
            "P = point_on_ellipse(A_2, B_1)",
            "r_1 = segment(F_1, P)",
            "r_2 = segment(F_2, P)",
        ],
        "synthesis": [
            "In Topic 17 (:cite:`SeeligNotebooks`), Seelig documents a classical 7-step compass-and-straightedge "
            "procedure titled *'FIVE CIRCLE CONSTRUCTION ELLIPSE'* inside a bounding box of semi-axes :math:`a` and "
            ":math:`b`, locating major-axis centers :math:`C_2, C_3` and minor-axis centers :math:`C_1, C_4, C_5` "
            "so that the circular end-caps of radius :math:`r = |C_2 P|` join smoothly with the broad top/bottom arcs.",
            "In Folio 4, he derives the exact analytic relations among focal distance :math:`F`, directrix distance "
            ":math:`d = a/e`, eccentricity :math:`e`, semi-latus rectum :math:`p = b^2/a`, and the :term:`geometric mean` "
            "relation :math:`V = a = \\sqrt{d F}`.",
        ],
        "equations": [
            r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1, \qquad r_1 + r_2 = 2 a, \qquad V = a = \sqrt{d \cdot F}, \qquad L = \frac{2 b^2}{a}",
        ],
        "depends_on": ["F.1", "F.10"],
        "euclid_refs": ["I.47", "VI.13"],
        "elements_refs": ["G.3"],
        "etc_refs": [],
        "spreadsheets": ["General Reference"],
        "folio_summaries": [
            (
                "Five-Circle Construction Ellipse — Steps 1–4",
                "Sets up bounding box :math:`(a, b)`, diagonals :math:`L_1, L_2`, normals :math:`L_3, L_4` meeting at :math:`C_1, C_2, C_3`, and end-cap circles of radius :math:`r`.",
            ),
            (
                "Five-Circle Construction Ellipse — Steps 5–7",
                "Locates :math:`Q` with :math:`|BQ| = 2r`, draws circle :math:`(C_1, |C_1 Q|)` to find :math:`C_4, C_5`, and draws transition radials through :math:`C_2, C_3`.",
            ),
            (
                "Full-Page Compass Execution of the Five-Circle Oval",
                "Precision compass-and-straightedge construction showing centers :math:`C_1..C_5` and smooth tangent circular arcs.",
            ),
            (
                "Focus, Directrix, Eccentricity & Latus Rectum Identities",
                "Derives :math:`F = ae, d = a/e, e^2 = F/d, V = a = \\sqrt{dF}`, and latus rectum :math:`L = 2b^2/a`.",
            ),
        ],
    },
    {
        "num": 18,
        "id": "F.18",
        "slug": "equilateral-triangle",
        "legacy_folder": "18.equailateral-triangle",
        "title": "Equilateral Triangle",
        "subtitle": "Coincidence of Centers, h_A = 3r, and Complex Cube-Root Proof of an Incenter-Bisector Equilateral Triangle",
        "category": "Special Triangles & Sacred Proportions",
        "tags": ["equilateral", "euclid-i-1", "incenter", "roots-of-unity", "vesica"],
        "enunciation": (
            "In an equilateral triangle of side a, the incenter, centroid, circumcenter, and "
            "orthocenter coincide, with altitude h_A = (sqrt(3)/2)a = 3r and R = 2r; moreover, "
            "points A', B', C' placed along the angle bisectors AI, BI, CI of any triangle ABC "
            "at distances A'I = (2r/sqrt(3)) sin(alpha/2 + pi/6) form an equilateral triangle."
        ),
        "signature_given": ["A : Point", "B : Point"],
        "signature_steps": [
            "c_a = circle(A, B)",
            "c_b = circle(B, A)",
            "C, D = intersect(c_a, c_b)",
            "ABC = polygon(A, B, C)",
        ],
        "synthesis": [
            "The :term:`equilateral triangle` constructed in :cite:`EuclidElements` Proposition I.1 (`G.1`) is the "
            "seed of constructive geometry: intersecting congruent circles :g:`( A B )` and :g:`( B A )` produces "
            "apex :g:`C` with altitude :math:`h_A = \\frac{\\sqrt{3}}{2}a = 3r` and :math:`R = 2r`, where :g:`G`, "
            ":math:`I`, :math:`O`, and :math:`H` all coincide (:cite:`SeeligNotebooks`).",
            "In Folios 2–3 (`equilateral-2-001`–`002`), Seelig gives an algebraic and complex-number proof that "
            "points :math:`A', B', C'` chosen on the interior angle bisectors :math:`AI, BI, CI` of *any* triangle "
            ":math:`\\triangle ABC` with :math:`A'I = \\frac{2r}{\\sqrt{3}}\\sin(\\frac{\\alpha}{2} + \\frac{\\pi}{6})` "
            "form an equilateral triangle :math:`\\triangle A'B'C'` by verifying :math:`m + n\\epsilon + p\\epsilon^2 = 0` "
            "for :math:`\\epsilon = e^{i 2\\pi/3}`.",
        ],
        "equations": [
            r"h_A = \frac{\sqrt{3}}{2} a = 3 r, \qquad R = \frac{a}{\sqrt{3}} = 2 r, \qquad K = \frac{\sqrt{3}}{4} a^2",
            r"A'I = \frac{2 r}{\sqrt{3}}\sin\left(\frac{\alpha}{2} + \frac{\pi}{6}\right), \qquad P(\epsilon) = m + n\epsilon + p\epsilon^2 = 0 \quad (\epsilon = e^{i 2\pi/3})",
        ],
        "depends_on": [],
        "euclid_refs": ["I.1", "IV.2", "IV.3"],
        "elements_refs": ["G.1", "G.2"],
        "etc_refs": ["X(1)", "X(2)", "X(3)", "X(4)"],
        "spreadsheets": ["General Reference", "Polygon Table"],
        "folio_summaries": [
            (
                "Equilateral Triangle Fundamental Properties",
                "Lists coincidence of orthocenter, centroid, and incenter, equal altitudes, and :math:`h_A = 3r` (:math:`h_A = \\sqrt{3}/2` for :math:`a=1`).",
            ),
            (
                "Incenter-Bisector Equilateral Triangle Proof (Page 1)",
                "Simplifies :math:`A'I = r\\csc(\\alpha/2) - r\\cot(\\alpha/2) + \\frac{r}{\\sqrt{3}}\\cos(\\alpha/2) = \\frac{2r}{\\sqrt{3}}\\sin(\\frac{\\alpha}{2} + \\frac{\\pi}{6})`.",
            ),
            (
                "Incenter-Bisector Equilateral Triangle Proof via Roots of Unity (Page 2)",
                "Substitutes :math:`u = \\alpha/2 + \\pi/6, v = \\beta/2 + \\pi/6, w = \\gamma/2 + \\pi/6` (:math:`u+v+w=\\pi`) and complex cube root of unity :math:`\\epsilon = e^{i 2\\pi/3}`.",
            ),
        ],
    },
    {
        "num": 19,
        "id": "F.19",
        "slug": "equal-incircle-theorem",
        "legacy_folder": "19.equal-incircle-theorem",
        "title": "Equal Incircles Theorem",
        "subtitle": "Japanese Sangaku Ray-Fan Theorem Proved via Hyperbolic Tangents",
        "category": "Triangle Centers & Classical Lines",
        "tags": ["incircle", "inradius", "sangaku", "hyperbolic-functions"],
        "enunciation": (
            "If a fan of rays from apex P to a baseline cuts triangle ABC into consecutive "
            "subtriangles whose incircles have equal radii r_1 = r_2 = ... = r_n = r, then "
            "the ray angles gamma_n with the altitude PR (of height h) follow the hyperbolic "
            "progression tan(gamma_n) = sinh(a + n*b) with tanh(b/2) = r/(h - r), so overlapping "
            "pairs of subtriangles also have equal incircles."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "I = incenter(A, B, C)",
            "T_C = foot(I, line(A, B))",
            "incircle = circle(I, T_C)",
        ],
        "synthesis": [
            "The **Equal Incircles Theorem** is a celebrated Japanese Sangaku theorem: if rays from apex :g:`C` "
            "to base :g:`A` :g:`B` partition :math:`\\triangle ABC` into subtriangles with equal inradii :math:`r`, "
            "then the incircles of the triangles formed by every second ray (or every :math:`k`-th ray) are also equal.",
            "In Topic 19 (:cite:`SeeligNotebooks`), Seelig gives an elegant proof (marked *'interesting!!!'*): "
            "using similar triangles :math:`\\triangle OWX \\sim \\triangle PQX` at height :math:`h - r`, he derives "
            ":math:`(h - r)(\\tan\\gamma_{n+1} - \\tan\\gamma_n) = r(\\sec\\gamma_n + \\sec\\gamma_{n+1})` and shows "
            "that the hyperbolic parameterization :math:`\\tan\\gamma_n = \\sinh(a + nb), \\sec\\gamma_n = \\cosh(a + nb)` "
            "satisfies this recurrence identically with constant step :math:`\\tanh(b/2) = \\frac{r}{h-r}`.",
        ],
        "equations": [
            r"(h - r)(\tan\gamma_{n+1} - \tan\gamma_n) = r(\sec\gamma_n + \sec\gamma_{n+1})",
            r"\tan\gamma_n = \sinh(a + n b), \qquad \sec\gamma_n = \cosh(a + n b), \qquad \frac{r}{h - r} = \tanh\frac{b}{2}",
        ],
        "depends_on": ["F.4", "F.28"],
        "euclid_refs": ["IV.4", "VI.4"],
        "elements_refs": ["G.3"],
        "etc_refs": ["X(1)"],
        "spreadsheets": ["Incircle-Incenter"],
        "folio_summaries": [
            (
                "Equal Incircles Theorem Statement & Ray-Fan Diagrams",
                "States the theorem with two ray-fan diagrams and introduces the hyperbolic substitution :math:`\\tan\\gamma_n = \\sinh(a + nb)`.",
            ),
            (
                "Similarity Proof & Hyperbolic Identity ('interesting!!!')",
                "Uses :math:`\\triangle OWX \\sim \\triangle PQX` to derive :math:`(h-r)(\\tan\\gamma_{n+1}-\\tan\\gamma_n) = r(\\sec\\gamma_n+\\sec\\gamma_{n+1})` and reduces it to :math:`\\frac{r}{h-r} = \\tanh(b/2)`.",
            ),
        ],
    },
    {
        "num": 20,
        "id": "F.20",
        "slug": "extangent",
        "legacy_folder": "20.extangent",
        "title": "Extangent",
        "subtitle": "The Extangents Triangle, Excircles, and Differentiation of Euler's Incenter-Circumcenter Formula",
        "category": "Triangle Centers & Classical Lines",
        "tags": ["excircle", "extangent", "euler-formula", "incircle", "circumcircle"],
        "enunciation": (
            "The external common tangents to the incircle and circumcircle (or excircles) "
            "bound the extangents triangle, while Euler's relation d_{IO}^2 = R^2 - 2rR has "
            "derivative d(d_{IO})/dR = (R - r)/sqrt(R^2 - 2rR)."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "I = incenter(A, B, C)",
            "I_a = excenter_a(A, B, C)",
            "I_b = excenter_b(A, B, C)",
            "I_c = excenter_c(A, B, C)",
            "incircle = circle(I, T_C)",
            "excircle_C = circle(I_c, E_C)",
        ],
        "synthesis": [
            "In Topic 20 (:cite:`SeeligNotebooks`), Seelig constructs the **extangents triangle** formed by the "
            "external tangents to the :term:`incenter` / :term:`excircle` configuration and differentiates "
            ":person:`Euler <euler>`'s distance formula :math:`d_{IO} = \\sqrt{R^2 - 2rR}` with respect to :math:`R`, "
            "confirming Euler's inequality :math:`R \\ge 2r` with equality only for the :term:`equilateral triangle`.",
        ],
        "equations": [
            r"d_{IO}^2 = R^2 - 2 r R, \qquad \frac{d}{d R}(d_{IO}) = \frac{R - r}{\sqrt{R^2 - 2 r R}}, \qquad r_a = \frac{K}{s - a}, \quad r_b = \frac{K}{s - b}, \quad r_c = \frac{K}{s - c}",
        ],
        "depends_on": ["F.5", "F.11", "F.28"],
        "euclid_refs": ["IV.4"],
        "elements_refs": ["G.3"],
        "etc_refs": ["X(1)", "X(3)", "X(40)", "X(55)", "X(56)"],
        "spreadsheets": ["Excenters", "Incircle-Incenter", "Centers of Similitude"],
        "folio_summaries": [
            (
                "Extangents Triangle & Derivative of Euler's Distance d_{IO}",
                "Compass construction of the extangents triangle around an inscribed triangle and differentiation of :math:`d_{IO} = \\sqrt{R^2 - 2rR}` with respect to :math:`R`.",
            ),
        ],
    },
    {
        "num": 21,
        "id": "F.21",
        "slug": "fermat-point",
        "legacy_folder": "21.fermat-point",
        "title": "Fermat Point",
        "subtitle": "Torricelli's Equilateral Construction for X(13), 120-Degree Equiangularity, and the Obtuse Threshold",
        "category": "Triangle Centers & Classical Lines",
        "tags": [
            "fermat-point",
            "torricelli",
            "steiner",
            "optimization",
            "equilateral",
        ],
        "enunciation": (
            "For any triangle ABC whose largest interior angle is less than 120 degrees, "
            "erecting external equilateral triangles BCX_A, CAY_B, ABZ_C on its sides yields "
            "concurrent segments AX_A, BY_B, CZ_C that intersect at the Fermat-Torricelli point "
            "F = X(13), where <AFB = <BFC = <CFA = 120 degrees and FA + FB + FC is minimized."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "C' = outer_equilateral_apex(A, B)",
            "ABC' = polygon(A, B, C')",
            "CC' = segment(C, C')",
            "F = fermat_point(A, B, C)",
        ],
        "synthesis": [
            "Dated July 6, 2011 and citing :person:`Evangelista Torricelli <torricelli>` and David Wells "
            "(:cite:`Wells1991`, p. 75; :cite:`SeeligNotebooks`), Seelig constructs the :term:`Fermat point` "
            ":g:`F` :math:`= X(13)` by erecting external equilateral triangles (such as :g:`ABC'` with apex :g:`C'`) "
            "on the sides of :math:`\\triangle ABC` and intersecting their circumcircles with the Simpson/Torricelli "
            "lines :g:`CC'`.",
            "In Folio 2, Seelig carefully distinguishes between the isogonic :person:`Jakob Steiner <steiner>` / "
            "Torricelli point (where sides subtend :math:`120^\\circ`) and the true distance-minimizing Fermat point "
            "when an interior angle of :math:`\\triangle ABC` is :math:`\\ge 120^\\circ`: in that obtuse regime, the "
            ":math:`120^\\circ` point moves outside :math:`\\triangle ABC` while the minimum of :math:`FA + FB + FC` "
            "collapses onto the obtuse vertex itself.",
        ],
        "equations": [
            r"\angle AFB = \angle BFC = \angle CFA = 120^\circ, \qquad \min_{P} (|PA| + |PB| + |PC|) = |CC'| = \sqrt{\frac{a^2 + b^2 + c^2}{2} + 2\sqrt{3} K}",
            r"F = X(13) = \left(\csc\left(\alpha + \frac{\pi}{3}\right) : \csc\left(\beta + \frac{\pi}{3}\right) : \csc\left(\gamma + \frac{\pi}{3}\right)\right)",
        ],
        "depends_on": ["F.14", "F.18"],
        "euclid_refs": ["I.1", "III.21", "III.22"],
        "elements_refs": ["G.1", "G.3"],
        "etc_refs": ["X(13)", "X(14)", "X(15)", "X(16)"],
        "spreadsheets": ["General Reference", "Barycentric"],
        "folio_summaries": [
            (
                "Torricelli's Construction of the Fermat Point X(13) (FWS July 6, 2011)",
                "Step-by-step ruler-and-compass algorithm constructing external equilateral triangle :math:`\\triangle ABX` and its circumcircle to locate :math:`F = X(13)`.",
            ),
            (
                "Obtuse Triangle Regime & Distinction from the Steiner Point (Wells 1991, p. 75)",
                "Explains why :math:`S_{\\text{TOT}} = SA + SB + SC` is minimized at the obtuse vertex whenever an angle is :math:`\\ge 120^\\circ`.",
            ),
        ],
    },
    {
        "num": 22,
        "id": "F.22",
        "slug": "functions",
        "legacy_folder": "22.functions",
        "title": "Functions",
        "subtitle": "Gaussian Error Function Approximations (Abramowitz & Stegun) and Probability Distributions",
        "category": "Conics & Analytic Loci",
        "tags": [
            "functions",
            "gaussian",
            "error-function",
            "probability",
            "approximation",
        ],
        "enunciation": (
            "The standard normal cumulative distribution Phi(x) and error function erf(x) "
            "satisfy Phi(x) = 1/2 + (1/2) erf(x/sqrt(2)), where erf(x) is approximated to "
            "1.5e-7 accuracy by Abramowitz and Stegun's 5-term rational-exponential formula."
        ),
        "signature_given": ["O : Point", "A_1 : Point", "A_2 : Point", "B_1 : Point"],
        "signature_steps": [
            "major_axis = segment(A_1, A_2)",
            "b = segment(O, B_1)",
            "P = point_on_curve(A_2, B_1)",
        ],
        "synthesis": [
            "Used by Seelig for his Monte Carlo geometric probability simulations (see :ref:`F.41 <f-41>` and "
            ":ref:`F.49 <f-49>`), Topic 22 (:cite:`SeeligNotebooks`) records the interconversion formulas among "
            ":math:`\\Phi(x), Q(x), \\operatorname{erf}(x), \\operatorname{erfc}(x)`, the 5-term rational-exponential "
            "approximation from Abramowitz & Stegun (:cite:`AbramowitzStegun1964`, p. 299, Eq. 7.1.26), and summary "
            "integrals for the Binomial, Poisson, Bernoulli, Uniform, Exponential, and Normal distributions.",
        ],
        "equations": [
            r"\Phi(x) = \frac{1}{2} + \frac{1}{2}\operatorname{erf}\left(\frac{x}{\sqrt{2}}\right), \qquad \operatorname{erf}(x) \approx 1 - \left(\sum_{k=1}^5 a_k t^k\right) e^{-x^2}, \quad t = \frac{1}{1 + 0.3275911 x}",
        ],
        "depends_on": [],
        "euclid_refs": [],
        "elements_refs": [],
        "etc_refs": [],
        "spreadsheets": ["General Reference"],
        "folio_summaries": [
            (
                "Gaussian CDF Phi(x), Q(x), erf(x) & Abramowitz–Stegun Eq. 7.1.26",
                "Defines :math:`\\Phi(x), Q(x), \\operatorname{erf}(x), \\operatorname{erfc}(x)` and lists the 6 numerical constants :math:`p, a_1..a_5` from AMS-55, p. 299.",
            ),
            (
                "Six Discrete & Continuous Probability Distributions",
                "Summarizes formulas and density/CDF sketches for Binomial, Poisson, Bernoulli, Uniform, Exponential, and Normal distributions.",
            ),
        ],
    },
    {
        "num": 23,
        "id": "F.23",
        "slug": "golden-triangles",
        "legacy_folder": "23.golden-triangles",
        "title": "Golden Triangles",
        "subtitle": "The 72-72-36 Sublime Triangle, 5th Roots of Unity, and Normalized Stewart's Theorem",
        "category": "Special Triangles & Sacred Proportions",
        "tags": [
            "golden-ratio",
            "golden-triangle",
            "pentagon",
            "stewart",
            "euclid-iv-10",
        ],
        "enunciation": (
            "In the acute golden isosceles triangle ABC with base AB = 1, legs AC = BC = phi, "
            "and angles 72-72-36 degrees, bisecting base angle B meets AC at D such that "
            "CD = 1, DA = phi - 1 = 1/phi, and BD = AB = 1, partitioning ABC into a smaller "
            "golden triangle BCD and a golden gnomon ABD."
        ),
        "signature_given": ["A : Point", "B : Point"],
        "signature_steps": [
            "C = golden_apex(A, B)",
            "ABC = polygon(A, B, C)",
            "D = golden_section(A, C)",
            "BD = segment(B, D)",
        ],
        "synthesis": [
            "Constructed in :cite:`EuclidElements` IV.10 (`G.25` in ``geometor/elements``), the acute "
            ":term:`golden triangle` :g:`ABC` has leg-to-base ratio equal to the :term:`golden ratio` "
            ":math:`\\phi = \\frac{1+\\sqrt{5}}{2}`. In Topic 23 (:cite:`SeeligNotebooks`), Seelig computes the "
            "altitude :math:`CM = \\sqrt{\\phi^2 - 1/4} = \\frac{\\sqrt{\\phi + 3/4}}{\\phi}` and segment "
            ":math:`AD = 2\\sin 36^\\circ = \\sqrt{3 - \\phi} \\approx 1.1756` when :g:`D` divides leg :math:`BC` "
            "into :math:`\\phi - 1` and :math:`1`.",
            "In Folio 2 (`FWS 12/21/2014`), he constructs the nested *'GOLDEN IDENTITY TRIANGLES'* (right triangles "
            "sharing unit altitude with base angles :math:`72^\\circ, 54^\\circ, 36^\\circ, 18^\\circ`) and tabulates "
            "the 5th roots of unity :math:`e^{i 2\\pi n/5}`. In Folio 3 (`FWS 11/18/2013`), he proves the normalized "
            "form of :term:`Stewart's theorem` :math:`f^2 = k a^2 + k' b^2 - k k' c^2` (:math:`k + k' = 1`).",
        ],
        "equations": [
            r"\phi = \frac{1 + \sqrt{5}}{2}, \qquad \cos 36^\circ = \frac{\phi}{2}, \qquad \cos 72^\circ = \frac{\phi - 1}{2} = \frac{1}{2\phi}, \qquad 2\sin 36^\circ = \sqrt{3 - \phi}",
            r"f^2 = k a^2 + k' b^2 - k k' c^2 \qquad (k + k' = 1)",
        ],
        "depends_on": ["F.7", "F.18"],
        "euclid_refs": ["II.11", "IV.10", "IV.11", "VI.30"],
        "elements_refs": ["G.10", "G.25"],
        "etc_refs": [],
        "spreadsheets": ["Golden Triangle", "Polygon Table"],
        "folio_summaries": [
            (
                "Golden Triangle 72-72-36 & Segment AD",
                "Analyzes the :math:`72^\\circ\\text{–}72^\\circ\\text{–}36^\\circ` triangle with legs :math:`\\phi`, base :math:`1`, and point :math:`D` dividing :math:`BC` into :math:`\\phi-1` and :math:`1`, proving :math:`AD = 2\\sin 36^\\circ \\approx 1.1756`.",
            ),
            (
                "Golden Identity Triangles & 5th Roots of Unity (FWS 12/21/2014)",
                "Draws nested right triangles of angles :math:`72^\\circ, 54^\\circ, 36^\\circ, 18^\\circ` with altitude :math:`1` and tabulates :math:`\\operatorname{Re}` and :math:`\\operatorname{Im}` of :math:`e^{i 2\\pi n/5}`.",
            ),
            (
                "Normalized Stewart's Theorem Proof (FWS 11/18/2013)",
                "Proves :math:`f^2 = k a^2 + k' b^2 - k k' c^2` by reducing :math:`X = k(1-k)^2 + k^2(1-k) = k(1-k) = kk'`.",
            ),
        ],
    },
    {
        "num": 24,
        "id": "F.24",
        "slug": "gothic",
        "legacy_folder": "24.gothic",
        "title": "Gothic Arch",
        "subtitle": "Pointed Vesica Arch in a Square and Tangency Equations for the Inscribed Oculus Circle",
        "category": "Special Triangles & Sacred Proportions",
        "tags": ["gothic", "vesica", "equilateral", "circles", "architecture"],
        "enunciation": (
            "In a square ABCD of side s with pointed Gothic arch arcs of radius s centered at "
            "A(0, 0) and B(s, 0) meeting at apex E(s/2, (sqrt(3)/2)s), an inscribed tracery "
            "circle centered at P(s/2, Q) of radius r = s - p satisfies p*s = P_x H_x + P_y H_y "
            "at its tangency point H."
        ),
        "signature_given": ["A : Point", "B : Point"],
        "signature_steps": [
            "( A B ) = circle(A, B)",
            "( B A ) = circle(B, A)",
            "C, D = intersect(( A B ), ( B A ))",
            "M = midpoint(A, B)",
        ],
        "synthesis": [
            "Rooted in the :term:`vesica piscis` of :cite:`EuclidElements` I.1 (:ref:`F.18 <f-18>`), the pointed "
            "**Gothic arch** in Topic 24 (:cite:`SeeligNotebooks`) is bounded by two circular arcs :g:`( A B )` and "
            ":g:`( B A )` of radius :math:`s` inside a square :math:`ABCD` of side :math:`s`, together with diagonal "
            "radials :math:`l_{CF}: y = \\sqrt{3}x + s(1-\\sqrt{3})` and :math:`l_{DF}: y = -\\sqrt{3}x + s`.",
            "Seelig sets up the system of three circle equations for an oculus circle of radius :math:`r` centered on "
            "the symmetry axis at :math:`P(s/2, Q)`, proves the tangency dot-product identity "
            ":math:`p s = P_x H_x + P_y H_y` (where :math:`p = |AP| = s - r`), and uses the semicircle geometric mean "
            "to show :math:`g^2 = |AG|^2 = 2 s G_x`.",
        ],
        "equations": [
            r"r^2 = \left(x - \frac{s}{2}\right)^2 + (y - Q)^2, \qquad p s = P_x H_x + P_y H_y \quad (r = s - p), \qquad g^2 = G_x^2 + G_y^2 = 2 s G_x",
        ],
        "depends_on": ["F.9", "F.10", "F.18"],
        "euclid_refs": ["I.1", "III.11", "III.12"],
        "elements_refs": ["G.1", "G.3"],
        "etc_refs": [],
        "spreadsheets": ["General Reference"],
        "folio_summaries": [
            (
                "Gothic Arch & Oculus Circle System in Square of Side s",
                "Sets up circle :math:`r^2 = (x-s/2)^2 + (y-Q)^2`, arch :math:`s^2 = x^2+y^2`, and line :math:`l_{CF}: y = \\sqrt{3}x + s(1-\\sqrt{3})`.",
            ),
            (
                "Three-Circle Symmetry Analysis at Intersections H and G",
                "Exploits horizontal symmetry :math:`H_y = G_y` and :math:`G_x + H_x = s` across the centerline :math:`x = s/2`.",
            ),
            (
                "Tangency Inner-Product Identity p*s = P_x H_x + P_y H_y",
                "Uses internal tangency :math:`r = s - p` (:math:`p^2 = P_x^2 + P_y^2`) to derive :math:`p s = P_x H_x + P_y H_y`.",
            ),
            (
                "Semicircle Geometric Mean Proof of g^2 = 2*s*G_x",
                "Proves :math:`g^2 = G_x^2 + G_y^2 = 2sG_x` in a semicircle of diameter :math:`2s` centered at :math:`B`.",
            ),
            (
                "Biquadratic Reduction z^4 - 74z^2 + 928 = 0",
                "Solves the auxiliary circle-intersection system :math:`(P, Q) = (\\frac{z^2-40}{2z}, \\frac{z^2-16}{2z})` with :math:`P^2+Q^2=9` to get :math:`z^2 = 58`.",
            ),
        ],
    },
    {
        "num": 25,
        "id": "F.25",
        "slug": "harmonic-conjugates",
        "legacy_folder": "25.hamonic-conjugates",
        "title": "Harmonic Conjugates",
        "subtitle": "Orthogonal Circles, Ogilvy's Theorem, Dual Relations, and the Pi_+/Pi_- Symmetry Master Diagram",
        "category": "Projective & Harmonic Geometry",
        "tags": [
            "harmonic-conjugates",
            "orthogonal-circles",
            "apollonius",
            "duality",
            "ogilvy",
        ],
        "enunciation": (
            "Collinear points C and D divide segment AB (of midpoint M and half-length r) "
            "internally and externally in the same ratio k = |AC|/|BC| = |AD|/|BD| if and only if "
            "|MC|*|MD| = r^2, which occurs if and only if the circle on diameter AB and the "
            "Apollonian circle on diameter CD intersect orthogonally."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "M = midpoint(A, B)",
            "circle_AB = circle(M, B)",
            "D = harmonic_conjugate(A, B, C)",
            "O_A = midpoint(C, D)",
            "Apollonius = circle(O_A, C)",
            "P, P' = intersect(circle_AB, Apollonius)",
            "polar = segment(P, P')",
        ],
        "synthesis": [
            "Spanning 28 folios (`FWS 6/20/2014`, :cite:`SeeligNotebooks`) and citing :person:`C. Stanley Ogilvy <ogilvy>` "
            "(:cite:`Ogilvy1969`, pp. 19–27) and Heath's commentary on :cite:`EuclidElements` VI.3 (p. 198), Topic 25 "
            "is Seelig's definitive treatise on :term:`harmonic conjugate` geometry and :term:`orthogonal circles`.",
            "Setting :math:`\\kappa = |MC|/r = \\frac{k-1}{k+1}` on circle :g:`circle_AB` (center :g:`M`, radius :math:`r`) "
            "and :math:`\\kappa' = |M'B|/R = 1/k` on the orthogonal :g:`Apollonius` circle (center :g:`O_A`, radius :math:`R`), "
            "Seelig proves his **Theorem 1 (Duality Theorem)**: :math:`(\\kappa, k)` and :math:`(\\kappa', k')` are "
            "reciprocal duals (:math:`\\kappa' = 1/k, k' = 1/\\kappa`). Introducing the hyperbolic-like invariants "
            ":math:`\\Pi_+ \\triangleq \\frac{1}{\\kappa} + \\kappa` and :math:`\\Pi_- \\triangleq \\frac{1}{\\kappa} - \\kappa` "
            "(satisfying :math:`\\Pi_+^2 - \\Pi_-^2 = 4`), he expresses every chord, altitude :math:`p = PQ`, projection "
            ":math:`q = MQ`, center distance :math:`d = MM'`, and tangent :math:`T, T'` in closed symmetric form, "
            "verified with the exact rational example :math:`\\kappa = 3/7, r = 42, R = 40, d = 58`.",
        ],
        "equations": [
            r"\frac{|AC|}{|CB|} = \frac{|AD|}{|BD|} = k = \frac{1 + \kappa}{1 - \kappa}, \qquad |MC| \cdot |MD| = x y = r^2, \qquad \frac{2}{|AB|} = \frac{1}{|AC|} + \frac{1}{|AD|}",
            r"\Pi_+ = \frac{1}{\kappa} + \kappa, \quad \Pi_- = \frac{1}{\kappa} - \kappa, \quad \Pi_+^2 - \Pi_-^2 = 4, \quad R = \frac{r}{2}\Pi_-, \quad d = \frac{r}{2}\Pi_+, \quad p = r\frac{\Pi_-}{\Pi_+}",
        ],
        "depends_on": ["F.2", "F.8", "F.12"],
        "euclid_refs": ["III.36", "VI.3"],
        "elements_refs": ["G.3", "G.5"],
        "etc_refs": [],
        "spreadsheets": [
            "Harmonic Conjugates",
            "HC Tables",
            "Apollonian Circles",
            "Coaxial Circles",
        ],
        "folio_summaries": [
            (
                "Orthogonal Circles on Line AXBY (Page 1)",
                "Defines harmonic conjugates :math:`|AX|/|XB| = |AY|/|YB|` with :math:`c = |AB|` and :math:`k = |AX|/|AB|`.",
            ),
            (
                "Internal & External Division Ratios (Page 2)",
                "Expresses the division ratios in terms of :math:`k/(1-k)` on circle :math:`\\Gamma(m, r)` with :math:`r' = |mX|, d = |mY|`.",
            ),
            (
                "Symmetrical Ratio gamma = (r+r')/(r-r') = (d+r)/(d-r) (Page 3)",
                "Proves :math:`d = \\frac{\\gamma+1}{\\gamma-1}r` (*'What a pleasing, symmetrical result!'*).",
            ),
            (
                "Worked Example r = 1, k = 0.7 (Page 4)",
                "Computes :math:`\\gamma = 7/3` and :math:`|mX| = 0.4r`.",
            ),
            (
                "Inversion Identity r^2 = d*r' (Page 5, citing Ogilvy 1969, p. 19)",
                "Completes example (:math:`d = 2.5r`) and proves :math:`r^2 = |mX|\\cdot |mY|`.",
            ),
            (
                "Ogilvy's Theorem 8 on Orthogonal Circles (Page 6, Ogilvy p. 20)",
                "Proves that any circle dividing a diameter harmonically is orthogonal to the base circle (:math:`\\vec{mP} \\perp \\vec{zP}`).",
            ),
            (
                "Intersection Angle alpha of Two Circles (Page 7)",
                "Writes :math:`\\alpha = \\cos^{-1}\\left(\\frac{r_1^2+r_2^2-d^2}{2r_1r_2}\\right)` reducing to :math:`r^2+R^2=d^2` at :math:`90^\\circ`.",
            ),
            (
                "Harmonic Conjugates Master Summary (citing Euclid VI.3, Heath p. 198)",
                "Summarizes :math:`k, x, y, \\gamma, d, R`, the Apollonian circle :math:`\\Gamma_{O'}`, and the harmonic progression :math:`|AD|, |DC|, |DB|`.",
            ),
            (
                "Angle-Bisector & Tangent-Polar Properties (citing Ogilvy p. 27)",
                "Lists circle properties I (:math:`PC` bisects :math:`\\angle APD`) and II (perpendicular at :math:`C` meets :math:`\\Gamma` at :math:`P`, where tangent meets :math:`AB` at :math:`D`).",
            ),
            (
                "Barycentric/Coordinate Isolation of C and D",
                "Derives :math:`C = (A+kB)/(1+k)` and harmonic reciprocal formulas for :math:`D`.",
            ),
            (
                "Reciprocal Identities for k, k_2, k_3",
                "Proves :math:`\\frac{2}{B-A} = \\frac{1}{C} + \\frac{1}{D}` and :math:`2 = \\frac{1}{k_2} + \\frac{1}{k_3}`.",
            ),
            (
                "Summary Coordinate Box for C, D, r, R, O, O', E, d",
                "Compact coordinate reference for plotting orthogonal harmonic circles.",
            ),
            (
                "Right Triangle OPO' Altitude & Projections ('Very pretty!')",
                "Derives :math:`h = |PE| = rR/d`, :math:`x = |OE| = r^2/d`, :math:`y = |O'E| = R^2/d`, and inradius :math:`r_{\\text{inc}}`.",
            ),
            (
                "Reverse Scrap Sheet (Markov Channel Notes)",
                "Reverse side of scrap paper containing unrelated binary Markov channel equations.",
            ),
            (
                "12-Row Numerical Table for A = 0, B = 1",
                "Tabulates :math:`k, k_2, k_3` and radical axis coordinates across 12 parameter values.",
            ),
            (
                "Two-Color Dimensioned Orthogonal Circles Diagram",
                "Blue/red drawing of :math:`\\Gamma_O(r)` and :math:`\\Gamma_{O'}(R)` showing segments :math:`X, Y, Z, d, W`.",
            ),
            (
                "Master Diagram: Dual Relations & Internal Symmetry (FWS 6/20/2014)",
                "Yellow legal-pad master construction of semicircles :math:`\\Gamma_r, \\Gamma_R, \\Gamma_w, \\Gamma_\\rho` and segments :math:`t, t', T, T', p, q, \\delta, \\rho`.",
            ),
            (
                "Theorem 1: Duality Theorem (kappa' = 1/k, k' = 1/kappa)",
                "States the duality between :math:`(\\Gamma_r, \\kappa, k)` and :math:`(\\Gamma_R, \\kappa', k')` and lists 8 segment formulas.",
            ),
            (
                "Integer Parameterization r = 2mn, kappa = m/n & Example (3, 7)",
                "Derives :math:`d = \\frac{r}{2}(\\kappa + 1/\\kappa)` and tests :math:`m=3, n=7, r=42 \\implies R=40, d=58, p=840/29`.",
            ),
            (
                "Projection q = MQ = 2*kappa*r/(1 + kappa^2)",
                "Proves the formula for :math:`q = MQ` and verifies :math:`q = 882/29 \\approx 30.4` for :math:`(m,n)=(3,7)`.",
            ),
            (
                "Equivalence of Three Expressions for q' = M'Q",
                "Proves :math:`q' = d - q = \\sqrt{R^2 - p^2} = p^2/q` in terms of :math:`1/\\kappa \\pm \\kappa`.",
            ),
            (
                "Duplicate Scan of q' Equivalence Proof",
                "Second scan of the :math:`q'` equivalence derivation.",
            ),
            (
                "Invariants Pi_plus and Pi_minus (Pi_plus^2 - Pi_minus^2 = 4)",
                "Defines :math:`\\Pi_\\pm = \\frac{1}{\\kappa} \\pm \\kappa` and expresses :math:`R, d, p, q, q', \\delta` in terms of :math:`\\Pi_\\pm`.",
            ),
            (
                "Simplification of Midpoint Offset delta = (q' - q)/2",
                "Reduces :math:`\\delta = \\frac{r}{2}\\frac{\\Pi_-^2 - 4}{\\Pi_+}`.",
            ),
            (
                "Dual Chords t = CT, t' = BT' and Tangents T, T'",
                "Derives :math:`t = r\\sqrt{1-\\kappa^2}` and :math:`t' = R\\sqrt{1-{\\kappa'}^2} = r\\frac{1-\\kappa}{\\sqrt{\\kappa}}`.",
            ),
            (
                "Grid Summary Sheet of All 10 Symmetric Segment Formulas",
                "Consolidates :math:`p, q, d, q', \\delta, \\rho, t, t', T, T'` (*'remarkable symmetry'*).",
            ),
            (
                "Geometric Mean Proof that |BC| = r(1 - kappa)",
                "Proves :math:`|BC|^2 = 2|MC|\\cdot|M'B| = r^2(1-\\kappa)^2`.",
            ),
            (
                "External Tangent T' = R*sqrt(k^2 - 1)",
                "Completes the derivation of :math:`T' = r\\frac{2(1+\\kappa)}{\\sqrt{\\kappa}}`.",
            ),
        ],
    },
    {
        "num": 26,
        "id": "F.26",
        "slug": "harmonic-conjugate-inversion",
        "legacy_folder": "26.harmonic-conjugate-inversion",
        "title": "Harmonic Conjugate Inversion",
        "subtitle": "Inversion xy = r^2, Steiner's Power of a Point, the Important Parallelogram MDM_TT, and Diophantine Triples",
        "category": "Projective & Harmonic Geometry",
        "tags": [
            "inversion",
            "harmonic-conjugates",
            "power-of-a-point",
            "steiner",
            "diophantine",
        ],
        "enunciation": (
            "For a circle Gamma of center M and radius r on diameter AB, internal point C at "
            "x = |MC| and its harmonic conjugate D at y = |MD| are inverses satisfying x*y = r^2, "
            "while the tangent DT = T forms a parallelogram M D M_T T whose long diagonal z "
            "satisfies z^2 = y^2 + 3*r^2 by Stewart's Theorem."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "M = midpoint(A, B)",
            "circle_AB = circle(M, B)",
            "D = harmonic_conjugate(A, B, C)",
            "P, P' = tangent_points(D, circle_AB)",
            "polar = segment(P, P')",
        ],
        "synthesis": [
            "Titled *'The Relationship Between Harmonic Conjugation, Inversion, and The Powers of a Point, as "
            "Revealed by An Important Parallelogram'* (`FWS 11/19/2013`–`11/20/2013`, :cite:`SeeligNotebooks`), "
            "Topic 26 synthesizes :term:`inversion` (:math:`x y = r^2`), :person:`Jakob Steiner <steiner>`'s "
            ":term:`power of a point` (:math:`T^2 = y^2 - r^2 = AD\\cdot BD`), and :term:`Stewart's theorem`.",
            "Applying Stewart's theorem to the parallelogram :math:`M D M_T T` with sides :math:`r, y` and short "
            "diagonal :math:`T = |DT|`, Seelig proves that the long diagonal :math:`z = |M M_T|` satisfies "
            ":math:`z^2 = y^2 + 3r^2`. Furthermore, by rescaling any primitive :term:`Pythagorean triple` "
            ":math:`(\\hat{x}, \\hat{t}, \\hat{r})` by :math:`\\hat{x}`, he generates all-integer solutions "
            ":math:`(x, t, r, y, T) = (\\hat{x}^2, \\hat{x}\\hat{t}, \\hat{x}\\hat{r}, \\hat{r}^2, \\hat{r}\\hat{t})`, "
            "such as :math:`(9, 12, 15, 25, 20)` for :math:`\\kappa = 3/5`.",
        ],
        "equations": [
            r"x y = |MC| \cdot |MD| = r^2, \qquad T^2 = y^2 - r^2 = |AD| \cdot |BD|, \qquad z^2 + T^2 = 2(r^2 + y^2) \implies z^2 = y^2 + 3 r^2",
            r"(x,\, t,\, r,\, y,\, T) = \left(\hat{x}^2,\, \hat{x}\hat{t},\, \hat{x}\hat{r},\, \hat{r}^2,\, \hat{r}\hat{t}\right) \quad \text{where } \hat{x}^2 + \hat{t}^2 = \hat{r}^2",
        ],
        "depends_on": ["F.8", "F.25"],
        "euclid_refs": ["III.36", "VI.8"],
        "elements_refs": ["G.3", "G.5"],
        "etc_refs": [],
        "spreadsheets": ["Harmonic Conjugates", "HC Tables"],
        "folio_summaries": [
            (
                "Harmonic Conjugation, Inversion & The Important Parallelogram (FWS 11/19/2013)",
                "Introduces Fig. 1 showing circle :math:`\\Gamma(M, r)`, inverse points :math:`C, D` (:math:`xy = r^2`), tangent :math:`DT = T`, and parallelogram :math:`M D M_T T` with diagonal :math:`z`.",
            ),
            (
                "Jakob Steiner's Power of a Point (Page 2)",
                "Cites Jakob Steiner (1796–1863) for :math:`T^2 = y^2 - r^2 = PD\\cdot QD = AD\\cdot BD` (Fig. 2).",
            ),
            (
                "Similarity Proof of TD^2 = PD*QD & Example r=5, x=3 (FWS 11/19/2013)",
                "Proves :math:`\\triangle DTQ \\sim \\triangle DPT` and computes :math:`y = 25/3, AD = 40/3, BD = 10/3, T = 20/3`.",
            ),
            (
                "Stewart's Theorem on Parallelogram MDM_TT for Diagonal z",
                "Proves :math:`z^2 + T^2 = 2(r^2+y^2) \\implies z^2 = y^2 + 3r^2` and derives the reverse :math:`\\Gamma'` formula in terms of :math:`x', R`.",
            ),
            (
                "Reverse Formula Verification on Example 1 (FWS 11/19/2013)",
                "Rewrites :math:`z^2 = J + K + R^4(1/J + 1/K)` and confirms :math:`z^2 = 1300/9` from both forward and reverse equations.",
            ),
            (
                "Graphic Scaling & Integer Solutions Table",
                "Identifies the graphing sweet spot :math:`1/3 < x/r < 2/3` and tabulates integer 5-tuples :math:`(x, t, r, y, T)`.",
            ),
            (
                "Generating Integer 5-Tuples from Pythagorean Triples",
                "Proves that scaling :math:`(\\hat{x}, \\hat{t}, \\hat{r})` by :math:`\\hat{x}` and :math:`\\hat{r}` yields integer :math:`(x, t, r, y, T)`.",
            ),
            (
                "Collinearity Warning & Power of a Point Sketch",
                "Illustrates non-collinear tangent points and the secant power relation :math:`x^2 - r^2`.",
            ),
            (
                "Tangent-Chord Proof of TD^2 = DE*DF",
                "Detailed geometric proof using inscribed angles that :math:`\\triangle DTF \\sim \\triangle DET`.",
            ),
            (
                "Diophantine Problem Statement for (r, T, y) (FWS 11/19/2013)",
                "Formulates the number-theoretic problem of finding all-integer harmonic inversion configurations.",
            ),
            (
                "Master Landscape Table for kappa = 3/5 (FWS 11/20/2013)",
                "Complete table of graphical and exact integer coordinates (:math:`x=9, t=12, r=15, y=25, T=20, R=8, k=4`) with scale diagram.",
            ),
            (
                "Worked Example r = 3, R = 4, kappa = 1/3",
                "Verifies :math:`(W+w)/2 = (AD+BC)/2 = r+R = 7` for :math:`AB=6, CD=8`.",
            ),
            (
                "Harmonic Conjugate Kite Sample Problem (r = 5, x = 3)",
                "Computes all segments and ratios for :math:`\\kappa = 3/5, k = 4, k' = 5/3`.",
            ),
            (
                "Center Distance d and Radius R in Terms of kappa",
                "Tabulates :math:`\\kappa, 1/\\kappa - \\kappa, d/r` and remarks *'(Euclid and Apollonius would approve their use, I'm sure)'*.",
            ),
            (
                "Fibonacci & Lucas Prime Factorization Table (F_1 to F_25)",
                "Reverse side of Folio 14 listing prime factorizations of Fibonacci and Lucas numbers.",
            ),
        ],
    },
    {
        "num": 27,
        "id": "F.27",
        "slug": "harmonic-mean",
        "legacy_folder": "27.harmonic-mean",
        "title": "Harmonic Mean",
        "subtitle": "Compass Construction of the Harmonic Mean, Prime-Number Harmonic Ranges, and the Bilinear Lens",
        "category": "Projective & Harmonic Geometry",
        "tags": [
            "harmonic-mean",
            "geometric-mean",
            "euclid-vi-3",
            "primes",
            "bilinear",
        ],
        "enunciation": (
            "If C and D are harmonic conjugates with respect to segment AB (so |AC|/|CB| = |AD|/|BD|), "
            "then the length |CD| is the harmonic mean of |BD| and |AD|: "
            "|CD| = 2 |BD| |AD| / (|BD| + |AD|) = r (gamma + 1/gamma)."
        ),
        "signature_given": ["A : Point", "B : Point", "H : Point"],
        "signature_steps": [
            "O = midpoint(A, B)",
            "semicircle = circle(O, B)",
            "C = perpendicular_chord(H, AB, semicircle)",
            "K = foot(H, segment(O, C))",
            "H_mean = segment(C, K)",
        ],
        "synthesis": [
            "Dated October 25 and November 13–14, 2013 (:cite:`SeeligNotebooks`), Topic 27 develops both synthetic "
            "compass-and-straightedge constructions and algebraic number theory for the :term:`harmonic mean`. "
            "Citing Heath's notes on :cite:`EuclidElements` VI.3 (p. 198), Seelig shows that for harmonic points "
            ":math:`(A, B; C, D)` with :math:`|BD| = r(\\gamma - 1)` and :math:`|AD| = r(\\gamma + 1)`, the segment "
            ":math:`|CD| = r(\\gamma + 1/\\gamma)` is the harmonic mean of :math:`|BD|` and :math:`|AD|`, and gives "
            "a 7-step compass construction laying :math:`n = |BD|` onto :math:`m = |AD|` to form circle :math:`\\Gamma_0` "
            "of diameter :math:`m - n`.",
            "In Folios 15–16 (`Problems 6–10`), he studies harmonic ranges whose adjacent segments :math:`X = AC, Y = CB` "
            "are consecutive prime numbers :math:`P_{n+1}, P_n`, finding :math:`Z = \\frac{P_n(P_n+P_{n+1})}{P_{n+1}-P_n}` "
            "(:math:`10, 12, 30, 63/2`), and in Folios 17–19 (*'Bilinear Transform As Viewed Through the Lens of "
            "Harmonic Conjugates'*) explains why :math:`\\kappa = x/r \\in (0, 1)` is algebraically more fundamental "
            "than :person:`Apollonius <apollonius>`'s ratio :math:`k \\in (1, \\infty)`.",
        ],
        "equations": [
            r"|CD| = \operatorname{HM}(|BD|,\, |AD|) = \frac{2 |BD| \cdot |AD|}{|BD| + |AD|} = r\left(\gamma + \frac{1}{\gamma}\right), \qquad x^2 = \frac{(r / t)^2}{\frac{1}{r^2} + \frac{1}{t^2}} = \left(\frac{r}{\gamma}\right)^2",
            r"Y^2 + (X + Z) Y - X Z = 0 \implies Y = \frac{-(X + Z) + \sqrt{(X + Z)^2 + 4 X Z}}{2}",
        ],
        "depends_on": ["F.2", "F.10", "F.25"],
        "euclid_refs": ["VI.3", "VI.8", "VI.13"],
        "elements_refs": ["G.3", "G.5"],
        "etc_refs": [],
        "spreadsheets": ["Harmonic Conjugates", "HC Tables"],
        "folio_summaries": [
            (
                "Harmonic Mean |CD| = r(gamma + 1/gamma) & Construction Part I",
                "Proves :math:`|CD| = \\operatorname{HM}(|BD|, |AD|)` with a table for :math:`1/\\gamma \\in \\{2..6\\}` and begins the compass construction.",
            ),
            (
                "Harmonic Mean and the Power of a Circle (Page 3)",
                "Uses :math:`t^2 = mn` and :math:`\\triangle OxT \\sim \\triangle TxD` to derive :math:`x^2 = r^2[\\frac{1/t^2}{1/r^2+1/t^2}] = (r/\\gamma)^2`.",
            ),
            (
                "An Interesting Construction Involving the Harmonic Mean (Page 4)",
                "Constructs circle :math:`\\Gamma_0` of diameter :math:`AB = m-n` and auxiliary circle :math:`\\Gamma_Q` of diameter :math:`m+n`.",
            ),
            (
                "Parallel/Perpendicular Angle Chase on Circles Gamma_0 and Gamma_O'' (Page 6)",
                "Proves :math:`OT \\parallel UO''`, :math:`TU \\perp OD`, and :math:`x^2/r^2 = (r^2-x^2)/t^2`.",
            ),
            (
                "Boxed Formula for Projection x = r/gamma & Worked Example (Page 7)",
                "Completes the proof of :math:`x = r/\\gamma` and tests :math:`\\gamma = 2, r = 1 \\implies m=3, n=1, t^2=3, x=1/2`.",
            ),
            (
                "Harmonic Progression Proof via Euclid VI.3 (Heath p. 198)",
                "Shows that :math:`|AD| = r(\\gamma+1), |DC| = r(\\gamma+1/\\gamma), |DB| = r(\\gamma-1)` are in harmonic progression.",
            ),
            (
                "Asymptotic Limit lim_{gamma->inf} HM(gamma+1, gamma-1) = gamma",
                "Proves the asymptotic limit and tabulates values for :math:`\\gamma \\in \\{2, 3, 4, 5\\}`.",
            ),
            (
                "Derivation of x, y, and Apollonian Radius R from xy = r^2",
                "Derives :math:`x = r\\frac{k-1}{k+1}, y = r\\frac{k+1}{k-1}`, and :math:`R = \\frac{2rk}{k^2-1}`.",
            ),
            (
                "Identities for w = BC, W = AD, and Center Distance MM' = 2*rho",
                "Proves :math:`r/R = (1-\\kappa')/(1-\\kappa)` and tests :math:`k=3, \\kappa=1/2`.",
            ),
            (
                "Harmonic Progression Examples 1 & 2 (Cropped Scan)",
                "Works :math:`AC=4, CB=2, BD=6 \\implies CD = \\operatorname{HM}(6,12) = 8`.",
            ),
            (
                "Harmonic Progression with Euclid VI.3 Footnote (Partial Scan)",
                "Shows the first two lines of Footnote 1 on angle bisectors of :math:`\\triangle ABP`.",
            ),
            (
                "Harmonic Progression with Full Euclid VI.3 Footnote",
                "Uncropped scan showing all three lines of Footnote 1 citing *Elements* VI.3.",
            ),
            (
                "Harmonic Progression Page 2: Example 3 & r = 7/8, kappa = 1/2 (FWS 11/13/2013)",
                "Computes :math:`MM' = 35/32` and :math:`R = 21/32` for :math:`r = 7/8, \\kappa = 1/2`.",
            ),
            (
                "Duplicate Scan of Harmonic Progression Page 2",
                "Second scan of the `FWS 11/13/2013` worksheet.",
            ),
            (
                "Problems 6–9: Prime-Number Harmonic Ranges (FWS 11/14/2013)",
                "Evaluates :math:`Z = \\frac{P_n(P_n+P_{n+1})}{P_{n+1}-P_n}` for consecutive primes :math:`(3,2)\\to 10, (5,3)\\to 12, (7,5)\\to 30, (11,7)\\to 63/2`.",
            ),
            (
                "Problem 10: Quadratic for Middle Segment Y Given X and Z",
                "Solves :math:`Y^2 + (X+Z)Y - XZ = 0` for the internal segment :math:`Y = CB`.",
            ),
            (
                "Bilinear Transform Through the Lens of Harmonic Conjugates (Page 1, Oct. 25, 2013)",
                "Explains why :math:`\\kappa = x/r` is algebraically primary compared to Apollonius's ratio :math:`k`.",
            ),
            (
                "Hyperbola Plots for k(kappa) and kappa(k) (Page 2)",
                "Tables and sketches of :math:`k = \\frac{1+\\kappa}{1-\\kappa}` and :math:`\\kappa = \\frac{k-1}{k+1}`.",
            ),
            (
                "Self-Inverse Bilinear Transform y = (1-x)/(1+x) (Page 3)",
                "Plots :math:`y = \\frac{1-x}{1+x}` with asymptotes :math:`x = -1, y = -1`.",
            ),
        ],
    },
    {
        "num": 28,
        "id": "F.28",
        "slug": "incenter",
        "legacy_folder": "28.incenter",
        "title": "Incenter",
        "subtitle": "Concurrency of Angle Bisectors, Barycentric Coordinates a:b:c, Contact Vectors, and Incenter-Origin Shift",
        "category": "Triangle Centers & Classical Lines",
        "tags": ["incenter", "incircle", "inradius", "euler-formula", "barycentric"],
        "enunciation": (
            "The three interior angle bisectors of triangle ABC concur at the incenter "
            "I = X(1) with homogeneous barycentric coordinates a : b : c, inradius r = K/s "
            "satisfying 1/r = 1/h_a + 1/h_b + 1/h_c, and Euler's distance d_{IO}^2 = R(R - 2r)."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "bis_A = angle_bisector(B, A, C)",
            "bis_B = angle_bisector(C, B, A)",
            "I = intersect(bis_A, bis_B)",
            "T_C = foot(I, line(A, B))",
            "incircle = circle(I, T_C)",
        ],
        "synthesis": [
            "Dated June 1 and November 8, 2011 and citing :person:`Nathan Altshiller-Court <altshiller_court>`'s "
            "*College Geometry* (:cite:`AltshillerCourt2007`, :cite:`SeeligNotebooks`), Topic 28 develops the "
            "complete coordinate, vector, and metric theory of the :term:`incenter` :g:`I` :math:`= X(1)`.",
            "Seelig records the Cartesian weighted average :math:`\\vec{I} = (a\\vec{A} + b\\vec{B} + c\\vec{C})/(2s)`, "
            "the vector touchpoints :g:`T_A`, :g:`T_B`, :g:`T_C` along the sides using reduced lengths "
            ":math:`x = s-a, y = s-b, z = s-c`, the reciprocal altitude identity :math:`1/r = 1/h_a + 1/h_b + 1/h_c`, "
            ":person:`Euler <euler>`'s relation :math:`d^2 = R(R - 2r)`, and a coordinate translation placing the "
            "incenter at the origin :math:`(0, 0)`. On the canonical :math:`(5, 6, 7)` triangle, "
            ":math:`r = \\frac{2\\sqrt{6}}{3} \\approx 1.6330` and :math:`I = (4, \\frac{2\\sqrt{6}}{3})`.",
        ],
        "equations": [
            r"\vec{I} = \frac{a \vec{A} + b \vec{B} + c \vec{C}}{a + b + c}, \qquad r = \frac{K}{s} = \sqrt{\frac{(s - a)(s - b)(s - c)}{s}}, \qquad \frac{1}{r} = \frac{1}{h_a} + \frac{1}{h_b} + \frac{1}{h_c}",
            r"2 r R = \frac{a b c}{a + b + c}, \qquad d_{IO}^2 = R(R - 2 r) \implies R \ge 2 r",
        ],
        "depends_on": ["F.3", "F.11"],
        "euclid_refs": ["IV.4", "VI.3"],
        "elements_refs": ["G.3"],
        "etc_refs": ["X(1)", "X(7)"],
        "spreadsheets": ["Incircle-Incenter", "General Reference", "5-6-7 A,B,C"],
        "folio_summaries": [
            (
                "Incenter of a Triangle Summary Sheet (FWS 6/1/2011)",
                "Gives formulas for :math:`a, b, c, s, (X_O, Y_O), r = K/s`, and tangent segments :math:`s-a, s-b, s-c`.",
            ),
            (
                "Vector Equations for Contact Points T_A, T_B, T_C",
                "Expresses :math:`\\vec{T}_C = \\vec{A} + \\frac{x}{c}(\\vec{B}-\\vec{A})` and line intersection formulas.",
            ),
            (
                "Inradius, Altitudes & Euler's Formula (citing Altshiller-Court 2007)",
                "Records :math:`1/r = 1/h_a + 1/h_b + 1/h_c`, :math:`2rR = abc/(a+b+c)`, and :math:`d^2 = R(R-2r)`.",
            ),
            (
                "Inscribed Circle in Unit Right Triangle",
                "Graph-paper construction of the incircle and angle bisectors of the right triangle with vertices :math:`(0,0), (0,1), (1,0)`.",
            ),
            (
                "Translating a Triangle so the Incenter is at the Origin (FWS Nov 8, 2011)",
                "Derives shifted coordinates :math:`\\vec{A} = -\\vec{O}', \\vec{B} = \\vec{B}'-\\vec{O}', \\vec{C} = \\vec{C}'-\\vec{O}'` with :math:`O'_x = bc(1+\\cos\\alpha)/(2s), O'_y = bc\\sin\\alpha/(2s)`.",
            ),
        ],
    },
]
