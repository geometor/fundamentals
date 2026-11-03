"""Catalog data for Topics F.29 through F.55 of GEOMETOR Fundamentals."""

from __future__ import annotations

TOPICS_29_TO_55: list[dict[str, object]] = [
    {
        "num": 29,
        "id": "F.29",
        "slug": "inradius",
        "legacy_folder": "29.inradius",
        "title": "Inradius",
        "subtitle": "Special Inradius Values, Conway Intouch Segments, and the Gergonne Point",
        "category": "Triangle Centers & Classical Circles",
        "tags": ["inradius", "incircle", "conway", "gergonne", "heron"],
        "enunciation": (
            "The inradius r = K / s = (1/2) sqrt(((b+c-a)(c+a-b)(a+b-c))/(a+b+c)) "
            "= 4 R sin(alpha/2) sin(beta/2) sin(gamma/2) takes integer values on primitive "
            "Pythagorean triples and partitions the perimeter into Conway segments x, y, z "
            "whose touchpoints T_A, T_B, T_C concur at the Gergonne point Ge = X(7)."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "I = incenter(A, B, C)",
            "T_A = foot(I, line(B, C))",
            "T_B = foot(I, line(C, A))",
            "T_C = foot(I, line(A, B))",
            "Ge = intersection(line(A, T_A), line(B, T_B))",
            "c_in = circle(I, T_A)",
        ],
        "synthesis": [
            "Seelig's three-folio dossier on the :term:`inradius` (:cite:`SeeligNotebooks`) opens with "
            "his master reference sheet *Inradius / Special Inradius Values*, pairing the Heron radical "
            ":math:`r = \\frac{1}{2}\\sqrt{\\frac{(b+c-a)(c+a-b)(a+b-c)}{a+b+c}} = \\frac{K}{s}` and the "
            "trigonometric product :math:`r = 4R\\sin\\frac{\\alpha}{2}\\sin\\frac{\\beta}{2}\\sin\\frac{\\gamma}{2}` "
            "with a five-row benchmark table: Pythagorean triples :math:`(3,4,5)\\mapsto r=1`, "
            ":math:`(5,12,13)\\mapsto r=2`, :math:`(8,15,17)\\mapsto r=3`, and :math:`(7,24,25)\\mapsto r=3`; "
            "the :math:`30^\\circ\\text{--}60^\\circ\\text{--}90^\\circ` triangle; and the :term:`golden triangle` "
            ":math:`(\\phi b, \\phi b, b)` with :math:`r = \\frac{b}{2}\\sqrt{5-2\\sqrt{5}}`.",
            "In Folios 2–3, Seelig connects :term:`Conway triangle notation` (:math:`x = s-a, y = s-b, z = s-c`) "
            "to the :term:`incircle` contact points :g:`T_A`, :g:`T_B`, :g:`T_C` and their concurrency at the "
            ":term:`Gergonne point` :g:`Ge` (:ref:`X(7)`), verifying :math:`r = \\sqrt{xyz/(x+y+z)}` on a "
            "measured scalene drawing (:math:`a=28.3, b=19, c=30.8, s=39, K=263`) and on the canonical "
            ":math:`(5,6,7)` triangle (:math:`x=4, y=3, z=2, s=9, r = \\frac{2\\sqrt{6}}{3}`).",
        ],
        "equations": [
            r"r = \frac{K}{s} = \frac{1}{2}\sqrt{\frac{(b+c-a)(c+a-b)(a+b-c)}{a+b+c}} = \sqrt{\frac{x y z}{x + y + z}}",
            r"r = 4 R \sin\frac{\alpha}{2}\sin\frac{\beta}{2}\sin\frac{\gamma}{2}, \qquad x = s - a,\; y = s - b,\; z = s - c",
        ],
        "depends_on": ["F.14", "F.28"],
        "euclid_refs": ["IV.4"],
        "elements_refs": ["G.8"],
        "etc_refs": ["X(1)", "X(7)"],
        "spreadsheets": ["Incircle-Incenter", "General Reference"],
        "folio_summaries": [
            (
                "Inradius & Special Inradius Values",
                "Records algebraic and trigonometric formulas for :math:`r` alongside a special-value table for Pythagorean triples :math:`(3,4,5), (5,12,13), (8,15,17), (7,24,25)`, the :math:`30^\\circ\\text{--}60^\\circ\\text{--}90^\\circ` triangle, and the golden triangle :math:`(\\phi b, \\phi b, b)` with :math:`r = \\frac{b}{2}\\sqrt{5-2\\sqrt{5}}`.",
            ),
            (
                "Conway Intouch Segments & Gergonne Point (Page 1)",
                "Relates :math:`x = s-a, y = s-b, z = s-c` to the incircle contact points :math:`T_A, T_B, T_C` and the Gergonne point :math:`G_e = AT_A \\cap BT_B \\cap CT_C`, deriving :math:`r^2 = xyz/s`.",
            ),
            (
                "Measured Scalene Verification (Page 2)",
                "Constructs the incircle and Gergonne cevians on a measured triangle (:math:`a=28.3, b=19, c=30.8, s=39, x=10.7, y=20, z=8.2, K=263`) and verifies :math:`r = K/s \\approx 6.74`.",
            ),
        ],
    },
    {
        "num": 30,
        "id": "F.30",
        "slug": "isosceles",
        "legacy_folder": "30.isoceles",
        "title": "Isosceles Triangles",
        "subtitle": "Perimeter-Area Cubic, Cardano's Depressed Cubic, and Newton's Right-Triangle Formula",
        "category": "Polygons, Tessellations & Special Triangles",
        "tags": ["isosceles", "cubic", "cardano", "newton", "heron"],
        "enunciation": (
            "An isosceles triangle of given semiperimeter s and area K has half-base x = c/2 "
            "governed by the cubic 2 s x^3 - s^2 x^2 + K^2 = 0, which under x = y + s/6 "
            "reduces to Cardano's depressed cubic y^3 - (s^2/12) y - (s^3/54 - K^2/(2s)) = 0."
        ),
        "signature_given": ["A : Point", "B : Point", "M : Point"],
        "signature_steps": [
            "c_base = segment(A, B)",
            "perp = perpendicular(M, c_base)",
            "C = point_on(perp)",
            "a_leg = segment(B, C)",
            "b_leg = segment(C, A)",
        ],
        "synthesis": [
            "Citing :person:`Baloglou` and :person:`Helfgott` (*Forum Geometricorum* 8, 2008, pp. 13–25, "
            ":cite:`BaloglouHelfgott2008`), :person:`Peterson`'s mathematical blog, and :person:`Newton`'s "
            "*Universal Arithmetick* (:cite:`NewtonArithmetica`), Seelig investigates how prescribing the "
            "semiperimeter :math:`s` and area :math:`K` determines a triangle (:cite:`SeeligNotebooks`). "
            "Whereas a right triangle has a linear hypotenuse formula :math:`c = s - K/s` (Newton), an "
            ":term:`isosceles triangle` with legs :math:`a = b = s - x` and half-base :math:`x = c/2` satisfies "
            ":math:`h = \\sqrt{s(s-2x)}` and :math:`K = x\\sqrt{s(s-2x)}`, leading to the cubic "
            ":math:`2sx^3 - s^2 x^2 + K^2 = 0`.",
            "Applying the Tschirnhaus shift :math:`x = y + s/6` (with :math:`a = -s/2, b = 0, c = K^2/(2s)`), "
            "Seelig reduces the equation to :person:`Cardano`'s depressed cubic :math:`y^3 + py + q = 0` with "
            ":math:`p = -s^2/12` and :math:`q = -s^3/54 + K^2/(2s)`, analyzing the discriminant threshold "
            ":math:`K_{\\max} = s^2/(3\\sqrt{3})` achieved at the equilateral triangle (:math:`x = s/3`).",
        ],
        "equations": [
            r"a = b = s - x, \qquad x = \frac{c}{2}, \qquad K = x\sqrt{s(s - 2x)} \implies 2 s x^3 - s^2 x^2 + K^2 = 0",
            r"x = y + \frac{s}{6} \implies y^3 - \frac{s^2}{12} y + \left(\frac{K^2}{2s} - \frac{s^3}{54}\right) = 0, \qquad c_{\text{right}} = s - \frac{K}{s}",
        ],
        "depends_on": ["F.3"],
        "euclid_refs": ["I.5", "I.6"],
        "elements_refs": ["G.1"],
        "etc_refs": [],
        "spreadsheets": ["Isosceles Triangle", "Right Triangle"],
        "folio_summaries": [
            (
                "Scanner Separator Sheet",
                "Blank dark separator scan preceding the four-page isosceles cubic manuscript.",
            ),
            (
                "Isosceles Triangle — Area-Perimeter Cubic (Page 1)",
                "Cites Baloglou & Helfgott (2008) and Ivars Peterson; sets :math:`x = c/2, a = s-x, h = \\sqrt{s(s-2x)}` to derive :math:`2sx^3 - s^2 x^2 + K^2 = 0`.",
            ),
            (
                "Newton's Right-Triangle Formula & Cubic Setup (Page 2)",
                "Contrasts Newton's *Universal Arithmetick* right-triangle identity :math:`c = s - K/s` with the isosceles cubic :math:`x^3 - \\frac{s}{2}x^2 + \\frac{K^2}{2s} = 0`.",
            ),
            (
                "Reduction to Depressed Cubic (Page 3)",
                "Substitutes :math:`x = y - a/3 = y + s/6` into :math:`x^3 + ax^2 + bx + c = 0` to eliminate the quadratic term, obtaining :math:`p = -s^2/12` and :math:`q = -s^3/54 + K^2/(2s)`.",
            ),
            (
                "Cardano's Formula & Casus Irreducibilis (Page 4)",
                "Writes Cardano's radical solution for :math:`y^3 + py + q = 0` and checks the discriminant boundary :math:`q^2/4 + p^3/27 \\le 0` corresponding to two real isosceles solutions coalescing at the equilateral triangle.",
            ),
        ],
    },
    {
        "num": 31,
        "id": "F.31",
        "slug": "logic-tests",
        "legacy_folder": "31.logic-tests",
        "title": "Logic Tests",
        "subtitle": "Boolean Distance Inequality Triples and Signed Collinear Division Ratios",
        "category": "Algebraic & Coordinate Systems",
        "tags": ["boolean", "logic", "collinear", "harmonic", "spreadsheet"],
        "enunciation": (
            "Given collinear points A, B, C, the three Boolean inequality tests "
            "T_1 = (|CA| < |AB|), T_2 = (|CB| < |AB|), and T_3 = (|CA| < |CB|) uniquely "
            "partition the line AB into Region A (-1 < k < 0), interior segment AB (0 < k < infty), "
            "and Region B (-infty < k < -1), determining the sign of k = +/- |AC| / |BC|."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "l = line(A, B)",
            "s_ab = segment(A, B)",
            "s_ac = segment(A, C)",
            "s_bc = segment(B, C)",
        ],
        "synthesis": [
            "When automating :term:`harmonic conjugate` and :term:`Apollonian circles` calculations in C.a.R. "
            "and OpenDocument spreadsheets (:cite:`SeeligNotebooks`), Euclidean distance functions return "
            "unsigned magnitudes :math:`\\|CA\\|, \\|CB\\|, \\|AB\\|`. In this six-page treatise (*Three Logical "
            "Tests — Boolean outputs 1=True / 0=False*, numbered ``1/``–``6/``), Seelig defines three elementary "
            "predicates :math:`T_1: \\|CA\\| < \\|AB\\|`, :math:`T_2: \\|CB\\| < \\|AB\\|`, and "
            ":math:`T_3: \\|CA\\| < \\|CB\\|`.",
            "Enumerating all :math:`2^3 = 8` truth assignments across Scenarios I–VI, Seelig shows that "
            "Region :g:`A` (external on the :g:`A`-side, :math:`-1 < k < 0`) is characterized by "
            ":math:`\\overline{T}_2 T_3`, the interior of segment :g:`A` :g:`B` (:math:`0 < k < \\infty`) by "
            ":math:`T_1 T_2`, and Region :g:`B` (external on the :g:`B`-side, :math:`-\\infty < k < -1`) by "
            ":math:`\\overline{T}_1 \\overline{T}_3`, compiling nested ``if(...)`` formulas for both C.a.R. "
            "(Folio 4) and Excel/Calc (Folios 5–6).",
        ],
        "equations": [
            r"T_1 = (\|CA\| < \|AB\|), \qquad T_2 = (\|CB\| < \|AB\|), \qquad T_3 = (\|CA\| < \|CB\|)",
            r"\text{Region } A:\; \overline{T}_2 T_3\; (-1 < k < 0), \qquad \text{Region } AB:\; T_1 T_2\; (0 < k < \infty), \qquad \text{Region } B:\; \overline{T}_1\overline{T}_3\; (-\infty < k < -1)",
        ],
        "depends_on": ["F.2", "F.25"],
        "euclid_refs": ["V.8"],
        "elements_refs": ["G.5"],
        "etc_refs": [],
        "spreadsheets": [
            "Point in Triangle",
            "Point in Triangle (2)",
            "Harmonic Conjugates",
        ],
        "folio_summaries": [
            (
                "Three Logical Tests — Boolean Outputs (Page 1/)",
                "Defines predicates :math:`T_1, T_2, T_3` on :math:`\\|CA\\|, \\|CB\\|, \\|AB\\|` and partitions the line through :math:`A, B` into Region :math:`A`, Region :math:`AB`, and Region :math:`B`.",
            ),
            (
                "Truth Table & Scenarios I–III (Page 2/)",
                "Evaluates :math:`(T_1, T_2, T_3)` across Scenarios I–III as :math:`C` traverses the ray beyond :math:`A` and the left half of segment :math:`AB`.",
            ),
            (
                "Scenarios IV–VI & Signed Ratio k (Page 3/)",
                "Completes Scenarios IV–VI across the right half of :math:`AB` and the ray beyond :math:`B`, mapping each region to the interval of :math:`k = \\pm\\|AC\\|/\\|BC\\|`.",
            ),
            (
                "C.a.R. Conditional Expression Synthesis (Page 4/)",
                "Translates the Boolean minterms :math:`\\overline{T}_2 T_3, T_1 T_2, \\overline{T}_1\\overline{T}_3` into C.a.R. ``if(...)`` expressions for signed :math:`k`.",
            ),
            (
                "Spreadsheet Implementation — Part 1 (Page 5/)",
                "Writes Excel/OpenFormula ``IF``/``AND`` cell expressions testing whether :math:`C` lies inside :math:`AB` or externally on either side.",
            ),
            (
                "Spreadsheet Implementation — Part 2 (Page 6/)",
                "Verifies the Boolean logic cells against numeric test coordinates for :math:`A, B, C` and their harmonic conjugate :math:`D`.",
            ),
        ],
    },
    {
        "num": 32,
        "id": "F.32",
        "slug": "markowski",
        "legacy_folder": "32.markowski",
        "title": "Markowski's Theorem",
        "subtitle": "Circumcircle Midpoint Sagitta Product, Euler's Inequality, and Midpoint Inversion",
        "category": "Circle Inversion, Coaxial & Radical Systems",
        "tags": ["markowski", "sagitta", "circumcircle", "incircle", "euler"],
        "enunciation": (
            "If J, K, L denote the perpendicular sagittas from the side midpoints of triangle ABC "
            "to the circumcircle, Markowski's Theorem states J K L = (1/2) r^2 R = (R^2 - d_IO^2)^2 / (8 R)."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "O = circumcenter(A, B, C)",
            "I = incenter(A, B, C)",
            "c_out = circle(O, A)",
            "M_A = midpoint(B, C)",
            "P_A = intersection(ray(O, M_A), c_out)",
            "J = segment(M_A, P_A)",
        ],
        "synthesis": [
            "Dated April 23, 2015 (:cite:`SeeligNotebooks`), Seelig's two-page investigation *GIVEN :math:`d_{IO}` "
            "and :math:`R` — what is :math:`J\\cdot K\\cdot L`? (:person:`Markowski`'s Theorem)* examines the "
            "three :term:`sagitta` segments :math:`J, K, L` extending from the side midpoints :g:`M_A`, :g:`M_B`, "
            ":g:`M_C` to the :term:`circumcircle` :g:`c_out`. Combining :term:`Markowski's theorem` "
            ":math:`JKL = \\frac{1}{2}r^2 R` with :person:`Euler`'s identity :math:`d_{IO} = \\sqrt{R^2 - 2rR}`, "
            "Seelig eliminates the :term:`inradius` :math:`r = (R^2 - d_{IO}^2)/(2R)` to express the sagitta "
            "product purely in terms of :math:`R` and :math:`d_{IO}`: :math:`JKL = \\frac{(R^2 - d_{IO}^2)^2}{8R}`.",
            "On Folio 1, Seelig also notes the midpoint circle-inversion radius :math:`\\rho_I = \\sqrt{R^2 - (a/2)^2}` "
            "fixing the vertices of side :math:`a`. On Folio 2, he tests the formula on the equilateral triangle "
            "(:math:`d_{IO}=0 \\implies JKL = R^3/8`) and the :math:`30^\\circ\\text{--}60^\\circ\\text{--}90^\\circ` "
            "triangle (:math:`R=1, r=(\\sqrt{3}-1)/2, d_{IO}^2 = 2-\\sqrt{3}, JKL = (2-\\sqrt{3})/4`). In a candid "
            'archival moment (*"Stumped! FWS 4/23/2015"*), Seelig substitutes :math:`d_{IO}^2 = 2-\\sqrt{3}` into '
            ":math:`(R^2 - (d_{IO}^2)^2)^2/(8R)`, accidentally squaring :math:`d_{IO}^2` a second time—whose removal "
            "immediately reconciles both sides to :math:`(2-\\sqrt{3})/4`.",
        ],
        "equations": [
            r"J K L = \frac{1}{2} r^2 R = \frac{(R^2 - d_{IO}^2)^2}{8 R}, \qquad d_{IO}^2 = R^2 - 2 r R",
            r"J + K + L = 2 R + r, \qquad \rho_I = \sqrt{R^2 - \left(\frac{a}{2}\right)^2}",
        ],
        "depends_on": ["F.4", "F.11", "F.29"],
        "euclid_refs": ["III.35", "IV.5"],
        "elements_refs": ["G.7", "G.8"],
        "etc_refs": ["X(1)", "X(3)"],
        "spreadsheets": ["Circumcircle-Circumcenter", "Incircle-Incenter"],
        "folio_summaries": [
            (
                "Markowski's Theorem & Midpoint Inversion (FWS 4/23/2015)",
                "Combines :math:`d_{IO} = \\sqrt{R^2-2rR}` and :math:`JKL = \\frac{1}{2}r^2 R` to derive :math:`JKL = \\frac{(R^2-d_{IO}^2)^2}{8R}`, and records the midpoint inversion circle radius :math:`\\rho_I = \\sqrt{R^2-(a/2)^2}`.",
            ),
            (
                "Equilateral & 30-60-90 Triangle Verifications (FWS 4/23/2015)",
                "Verifies :math:`JKL = R^3/8` for the equilateral triangle and :math:`JKL = (2-\\sqrt{3})/4` for the :math:`30^\\circ\\text{--}60^\\circ\\text{--}90^\\circ` triangle (:math:`R=1`), where an extra squaring of :math:`d_{IO}^2 = 2-\\sqrt{3}` prompted the marginal note *'Stumped! FWS 4/23/2015'*.",
            ),
        ],
    },
    {
        "num": 33,
        "id": "F.33",
        "slug": "m-n",
        "legacy_folder": "33.m-n",
        "title": "Euclidean (m, n) Generators",
        "subtitle": "Parametric Pythagorean Triple Table for 2 <= m <= 7",
        "category": "Polygons, Tessellations & Special Triangles",
        "tags": ["pythagorean-triples", "euclid", "number-theory", "right-triangle"],
        "enunciation": (
            "For integers m > n >= 1, Euclid's quadratic generators a = m^2 - n^2, b = 2 m n, "
            "and c = m^2 + n^2 satisfy a^2 + b^2 = c^2 and inradius r = n(m - n)."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "a = segment(B, C)",
            "b = segment(C, A)",
            "c = segment(A, B)",
        ],
        "synthesis": [
            "This single-folio reference table (:cite:`SeeligNotebooks`) tabulates :person:`Euclid`'s parametric "
            "generators :math:`(m, n, m^2-n^2, 2mn, m^2+n^2)` (from *Elements* Book X, Lemma 1 to X.29) across "
            "11 integer pairs for :math:`2 \\le m \\le 7`: from :math:`(m,n) = (2,1) \\mapsto (3,4,5)` through "
            ":math:`(3,2)\\mapsto(5,12,13)`, :math:`(4,1)\\mapsto(15,8,17)`, :math:`(4,3)\\mapsto(7,24,25)`, "
            ":math:`(5,2)\\mapsto(21,20,29)`, :math:`(5,4)\\mapsto(9,40,41)`, :math:`(6,1)\\mapsto(35,12,37)`, "
            ":math:`(6,5)\\mapsto(11,60,61)`, :math:`(7,2)\\mapsto(45,28,53)`, :math:`(7,4)\\mapsto(33,56,65)`, "
            "to :math:`(7,6)\\mapsto(13,84,85)`.",
            "Every row in Seelig's table omits common-factor pairs (such as :math:`(3,1)` or :math:`(4,2)`) so "
            "that all 11 generated triples are primitive :term:`Pythagorean triple` right triangles with integer "
            ":term:`inradius` :math:`r = n(m-n)` and semiperimeter :math:`s = m(m+n)`.",
        ],
        "equations": [
            r"a = m^2 - n^2, \qquad b = 2 m n, \qquad c = m^2 + n^2, \qquad a^2 + b^2 = (m^2 + n^2)^2 = c^2",
            r"s = m(m + n), \qquad r = n(m - n), \qquad K = m n (m^2 - n^2)",
        ],
        "depends_on": ["F.29"],
        "euclid_refs": ["I.47", "X.29"],
        "elements_refs": ["G.11"],
        "etc_refs": [],
        "spreadsheets": ["Pythagorean Triples", "Right Triangle"],
        "folio_summaries": [
            (
                "Euclidean (m, n) Pythagorean Triple Table",
                "Tabulates :math:`(m, n, m^2-n^2, 2mn, m^2+n^2)` for 11 coprime pairs of opposite parity from :math:`(2,1)\\mapsto(3,4,5)` to :math:`(7,6)\\mapsto(13,84,85)`.",
            ),
        ],
    },
    {
        "num": 34,
        "id": "F.34",
        "slug": "nine-point-circle",
        "legacy_folder": "34.nine-point-circle",
        "title": "Nine-Point Circle",
        "subtitle": "Feuerbach's Nine-Point Circle, Euler Line Collinearity, and Orthocenter Distance Identities",
        "category": "Triangle Centers & Classical Circles",
        "tags": [
            "nine-point-circle",
            "euler-line",
            "orthocenter",
            "circumcenter",
            "feuerbach",
        ],
        "enunciation": (
            "The circle Gamma_N passing through the three altitude feet H_A, H_B, H_C also passes "
            "through the three side midpoints M_A, M_B, M_C and the three Euler midpoints; its radius "
            "is r_N = R/2 and its center N = X(5) bisects segment OH on the Euler line."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "M_A = midpoint(B, C)",
            "M_B = midpoint(C, A)",
            "M_C = midpoint(A, B)",
            "O = circumcenter(A, B, C)",
            "H = orthocenter(A, B, C)",
            "N = midpoint(O, H)",
            "c_nine = circle(N, M_A)",
        ],
        "synthesis": [
            "In this concentrated summary folio (:cite:`SeeligNotebooks`), Seelig defines the "
            ':term:`nine-point circle` :math:`\\Gamma_N` (*"The circle that passes through all three footers '
            'is the nine point circle"*), recording its center :g:`N` (:ref:`X(5)`), radius '
            ":math:`r_N = \\frac{1}{2}R`, and two expressions for the distance between the :term:`circumcenter` "
            ":g:`O` (:ref:`X(3)`) and :term:`orthocenter` :g:`H` (:ref:`X(4)`): "
            ":math:`|OH| = \\sqrt{2r^2 + 4R^2 - S_\\omega}` (where :math:`S_\\omega = \\frac{1}{2}(a^2+b^2+c^2)`) "
            "and :math:`|OH|^2 = AH^2 + BH^2 + CH^2 - 3R^2 = 9R^2 - (a^2+b^2+c^2)`.",
            "A pencil annotation highlights that :g:`N` lies on the :term:`Euler line` through :g:`O`, :g:`G`, :g:`H` "
            "at the midpoint of :g:`O` :g:`H`, illustrated by a compass drawing of the obtuse :math:`(2,3,4)` "
            "triangle showing the exterior altitude feet and their common circle :math:`\\Gamma_N`. On the canonical "
            ":math:`(5,6,7)` triangle, :math:`R = \\frac{35\\sqrt{6}}{24}`, :math:`r_N = \\frac{35\\sqrt{6}}{48}`, "
            "and :math:`|OH|^2 = 9\\left(\\frac{1225}{96}\\right) - 110 = \\frac{155}{32}`.",
        ],
        "equations": [
            r"r_N = \frac{1}{2} R, \qquad N = \frac{O + H}{2} = X(5), \qquad |ON| = \frac{1}{2}|OH|",
            r"|OH|^2 = 9 R^2 - (a^2 + b^2 + c^2) = 2 r^2 + 4 R^2 - \frac{a^2 + b^2 + c^2}{2}",
        ],
        "depends_on": ["F.6", "F.11"],
        "euclid_refs": ["IV.5"],
        "elements_refs": ["G.7"],
        "etc_refs": ["X(2)", "X(3)", "X(4)", "X(5)"],
        "spreadsheets": ["9-Point Circle", "Euler Line", "Orthocenter"],
        "folio_summaries": [
            (
                "Nine-Point Circle & Orthocenter Distance Identities",
                "Defines :math:`\\Gamma_N` through the three altitude feet with center :math:`N = X(5)` on the Euler line and radius :math:`r_N = R/2`, records :math:`|OH| = \\sqrt{2r^2+4R^2-S_\\omega}` and :math:`|OH|^2 = AH^2+BH^2+CH^2-3R^2`, and sketches the :math:`(2,3,4)` obtuse configuration.",
            ),
        ],
    },
    {
        "num": 35,
        "id": "F.35",
        "slug": "obtuse-and-acute",
        "legacy_folder": "35.obtuse-and-acute",
        "title": "Obtuse and Acute Triangles",
        "subtitle": "Euclid's Excess and Deficit (II.12 & II.13), Altitude-Median Offsets, and Apollonius's Theorem",
        "category": "Polygons, Tessellations & Special Triangles",
        "tags": ["euclid", "obtuse", "acute", "altitude", "median", "cosine-law"],
        "enunciation": (
            "By Euclid's Elements II.12 (excess) and II.13 (deficit), the square on side a opposite "
            "an obtuse or acute angle satisfies a^2 = b^2 + c^2 +/- 2 c x, where x = |a^2 - (b^2 + c^2)| / (2 c) "
            "is the projection of side b onto line c and h = sqrt(b^2 - x^2) is the altitude."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "l_ab = line(A, B)",
            "H_C = foot(C, l_ab)",
            "M_C = midpoint(A, B)",
            "h_c = segment(C, H_C)",
            "x_proj = segment(A, H_C)",
            "d_mh = segment(M_C, H_C)",
        ],
        "synthesis": [
            "Titled *OBTUSE AND ACUTE TRIANGLES / EUCLID'S CONCEPT OF 'EXCESS' AND 'DEFICIT'* (:cite:`SeeligNotebooks`), "
            "this seven-folio study recovers :person:`Euclid`'s geometric precursors to the Law of Cosines: "
            ":ref:`II.12` (*excess* :math:`+2cx` for obtuse triangles) and :ref:`II.13` (*deficit* :math:`-2cx` "
            "for acute triangles). Without invoking trigonometric functions, Seelig computes the altitude foot "
            "projection :math:`x = \\pm\\frac{a^2-(b^2+c^2)}{2c}` and altitude :math:`h = \\sqrt{b^2-x^2}` directly "
            "from the three side lengths.",
            "Across Folios 2–7, Seelig works out three canonical integer triangles in complete detail: the obtuse "
            ":math:`(3,5,7)` Eisenstein triangle (:math:`120^\\circ` angle, :math:`x = 1.5, h_B = \\frac{3\\sqrt{3}}{2}` "
            "and :math:`x = \\frac{65}{14}, h_c = \\frac{15\\sqrt{3}}{14}`), the acute :math:`(5,6,7)` triangle "
            "(:math:`x = 1`, division ratio :math:`r/r' = 28/9`), and the acute :math:`(7,8,9)` triangle, computing "
            "the exact distance :math:`|m_A h_A| = \\frac{17}{14}, |m_B h_B| = \\frac{33}{16}, |m_C h_C| = \\frac{5}{6}` "
            "between each midpoint and altitude foot, before closing with :person:`Apollonius`'s median identity "
            ":math:`D^2 = \\frac{U^2+V^2}{2} - (E/2)^2`.",
        ],
        "equations": [
            r"a^2 = b^2 + c^2 \pm 2 c x \implies x = \frac{|a^2 - (b^2 + c^2)|}{2 c}, \qquad h^2 = b^2 - x^2",
            r"|M_C H_C| = \left|\frac{c}{2} - x\right| = \frac{|a^2 - b^2|}{2 c}, \qquad m_c^2 = \frac{a^2 + b^2}{2} - \left(\frac{c}{2}\right)^2",
        ],
        "depends_on": ["F.3", "F.6"],
        "euclid_refs": ["II.12", "II.13"],
        "elements_refs": ["G.3", "G.11"],
        "etc_refs": ["X(2)", "X(4)"],
        "spreadsheets": ["General Reference", "5-6-7 A,B,C", "Altitudes"],
        "folio_summaries": [
            (
                "Euclid's Concept of Excess (II.12) & Deficit (II.13)",
                "Formulates :math:`a^2 = b^2 + c^2 \\pm 2cx`, solves for the projection :math:`x = \\pm\\frac{a^2-(b^2+c^2)}{2c}`, and recovers altitude :math:`h = \\sqrt{b^2-x^2}`.",
            ),
            (
                "Obtuse (3, 5, 7) Triangle — Base 5 Projection",
                "Evaluates :math:`a=7, b=3, c=5` to find exterior projection :math:`x = 1.5`, altitude :math:`h_B = \\frac{3\\sqrt{3}}{2}`, and :math:`120^\\circ` obtuse angle.",
            ),
            (
                "Obtuse (3, 5, 7) Triangle — Base 7 Projection",
                "Projects onto the longest side :math:`c=7` to find :math:`x = 65/14, h_c = \\frac{15\\sqrt{3}}{14}`, and area :math:`K = \\frac{15\\sqrt{3}}{4}`.",
            ),
            (
                "Acute (5, 6, 7) Triangle Deficit Analysis",
                "Applies Euclid II.13 to :math:`(5,6,7)`, finding interior projection :math:`x = 1`, altitude :math:`h = 2\\sqrt{6}`, and segment ratio :math:`r/r' = 28/9`.",
            ),
            (
                "Acute (7, 8, 9) Triangle — Altitude Foot Offsets (Page 1)",
                "Computes the altitude feet :math:`h_A, h_B, h_C` and midpoints :math:`m_A, m_B, m_C` on the :math:`(7,8,9)` triangle.",
            ),
            (
                "Acute (7, 8, 9) Triangle — Midpoint-to-Foot Distances (Page 2)",
                "Evaluates the exact rational offsets :math:`|m_A h_A| = 17/14, |m_B h_B| = 33/16`, and :math:`|m_C h_C| = 5/6`.",
            ),
            (
                "Median Theorem from Excess & Deficit",
                "Adds Euclid II.12 and II.13 on the two halves of a bisected base :math:`E` to prove Apollonius's median formula :math:`D^2 = \\frac{U^2+V^2}{2} - (E/2)^2`.",
            ),
        ],
    },
    {
        "num": 36,
        "id": "F.36",
        "slug": "orthic-triangle",
        "legacy_folder": "36.orthic-triangle",
        "title": "Orthic Triangle",
        "subtitle": "Pedal Triangle of the Orthocenter, Tangential Homothety, and Fagnano's Minimum-Perimeter Problem",
        "category": "Triangle Centers & Classical Circles",
        "tags": [
            "orthic-triangle",
            "orthocenter",
            "fagnano",
            "pedal-triangle",
            "tangential",
        ],
        "enunciation": (
            "The orthic triangle H_A H_B H_C formed by the altitude feet of an acute triangle ABC "
            "is the pedal triangle of the orthocenter H = X(4), is homothetic to the tangential "
            "triangle, has H as its incenter, and solves Fagnano's 1775 problem by minimizing "
            "the perimeter among all triangles inscribed in ABC."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "H_A = foot(A, line(B, C))",
            "H_B = foot(B, line(C, A))",
            "H_C = foot(C, line(A, B))",
            "H = intersection(line(A, H_A), line(B, H_B))",
            "s_ab = segment(H_A, H_B)",
            "s_bc = segment(H_B, H_C)",
            "s_ca = segment(H_C, H_A)",
        ],
        "synthesis": [
            "On Folio ``orthic012.jpg`` (:cite:`SeeligNotebooks`), Seelig synthesizes the three defining "
            "properties of the :term:`orthic triangle` :math:`\\triangle H_A H_B H_C`: (1) it is the "
            ":term:`pedal triangle` of the :term:`orthocenter` :g:`H` (:ref:`X(4)`), whose altitudes bisect the "
            "interior angles of :math:`\\triangle H_A H_B H_C` so that :g:`H` is the incenter of the orthic "
            "triangle; (2) its sides are anti-parallel to :math:`BC, CA, AB` and parallel to the tangents to "
            "the :term:`circumcircle` at :g:`A`, :g:`B`, :g:`C`, making it homothetic to the tangential triangle; "
            "and (3) for any acute :math:`\\triangle ABC`, it solves :person:`Fagnano`'s Problem (1775), "
            "achieving the minimum perimeter :math:`p_{\\text{orthic}} = 2K/R = 4R\\sin\\alpha\\sin\\beta\\sin\\gamma` "
            "among all inscribed triangles.",
            "On the canonical :math:`(5,6,7)` acute triangle (:math:`K = 6\\sqrt{6}, R = \\frac{35\\sqrt{6}}{24}`), "
            "the orthic sides are :math:`a\\cos\\alpha = \\frac{19}{7}, b\\cos\\beta = \\frac{9}{7}, c\\cos\\gamma = \\frac{1}{5}`, "
            "giving the exact minimum Fagnano perimeter :math:`p_{\\text{orthic}} = \\frac{2K}{R} = \\frac{288}{35}`.",
        ],
        "equations": [
            r"a_{\text{orthic}} = a \cos\alpha, \qquad b_{\text{orthic}} = b \cos\beta, \qquad c_{\text{orthic}} = c \cos\gamma",
            r"p_{\text{orthic}} = \frac{2 K}{R} = 4 R \sin\alpha\sin\beta\sin\gamma, \qquad K_{\text{orthic}} = 2 K \cos\alpha\cos\beta\cos\gamma",
        ],
        "depends_on": ["F.34", "F.35"],
        "euclid_refs": ["I.12", "III.32"],
        "elements_refs": ["G.4"],
        "etc_refs": ["X(3)", "X(4)", "X(5)"],
        "spreadsheets": ["Orthic Triangle", "Orthocenter", "Pedal Triangle"],
        "folio_summaries": [
            (
                "The Orthic Triangle & Fagnano's Problem",
                "Records the three fundamental characterizations of the orthic triangle: (1) pedal triangle of :math:`H`, (2) homothetic to the tangential triangle, and (3) solution to Fagnano's 1775 minimum-perimeter inscribed triangle problem.",
            ),
        ],
    },
    {
        "num": 37,
        "id": "F.37",
        "slug": "parabolas",
        "legacy_folder": "37.parabolas",
        "title": "Euler's Inradius Parabola",
        "subtitle": "Parabolic Locus r(d) = (R^2 - d^2)/(2R) and Harmonic Factorization of Euler's Identity",
        "category": "Conics & Analytic Loci",
        "tags": ["parabola", "euler", "inradius", "circumradius", "harmonic"],
        "enunciation": (
            "For a fixed circumradius R, Euler's relation d^2 = R^2 - 2 r R defines a downward-opening "
            "parabola r(d) = R/2 - d^2/(2R) = (R - d)(R + d)/(2R) with vertex (0, R/2) at the "
            "equilateral triangle and roots at the degenerate limits d = +/- R."
        ),
        "signature_given": ["V : Point", "F : Point", "directrix : Line", "P : Point"],
        "signature_steps": [
            "Q = foot(P, directrix)",
            "s_fp = segment(F, P)",
            "s_pq = segment(P, Q)",
            "tangent = bisector(F, P, Q)",
        ],
        "synthesis": [
            "In this three-folio study (:cite:`SeeligNotebooks`), Seelig reinterprets :person:`Euler`'s triangle "
            "distance theorem :math:`d^2 = R^2 - 2rR` (where :math:`d = |IO|`) as a functional locus "
            ":math:`r(d) = \\frac{R}{2} - \\frac{d^2}{2R}` over a fixed :term:`circumcircle` of radius :math:`R`. "
            "Plotting :math:`r` against :math:`d` yields a downward-opening :term:`parabola` whose vertex "
            ":math:`(0, R/2)` represents the equilateral triangle (:math:`r = R/2`, Euler's inequality maximum) "
            "and whose horizontal intercepts :math:`d = \\pm R` represent degenerate flat triangles (:math:`r = 0`).",
            "Factoring the numerator as :math:`r(d) = \\frac{(R-d)(R+d)}{2R}`, Seelig connects the segments "
            ":math:`R-d` and :math:`R+d` partitioned by the :term:`incenter` :g:`I` along a diameter of the "
            "circumcircle to the power of a point :math:`(R-d)(R+d) = 2rR` and :term:`harmonic conjugate` division.",
        ],
        "equations": [
            r"d^2 = R^2 - 2 r R \iff r(d) = \frac{R}{2} - \frac{d^2}{2 R} = \frac{(R - d)(R + d)}{2 R}",
            r"r_{\max} = r(0) = \frac{R}{2}, \qquad (R - d)(R + d) = 2 r R",
        ],
        "depends_on": ["F.1", "F.11", "F.29"],
        "euclid_refs": ["II.5", "III.35"],
        "elements_refs": ["G.7", "G.8"],
        "etc_refs": ["X(1)", "X(3)"],
        "spreadsheets": ["Incircle-Incenter", "Circumcircle-Circumcenter"],
        "folio_summaries": [
            (
                "Euler's Identity as a Downward Parabola r(d)",
                "Inverts :math:`d^2 = R^2 - 2rR` into :math:`r(d) = \\frac{R}{2} - \\frac{d^2}{2R}` and plots the parabola from vertex :math:`(0, R/2)` to roots :math:`(\\pm R, 0)`.",
            ),
            (
                "Factored Form & Power of the Incenter",
                "Rewrites :math:`2rR = (R-d)(R+d)` as the chord-segment product of the incenter inside the circumcircle of radius :math:`R`.",
            ),
            (
                "Harmonic Division Along the Circumdiameter",
                "Relates the diameter segments :math:`R-d` and :math:`R+d` to the harmonic ratio :math:`k = (R+d)/(R-d)`.",
            ),
        ],
    },
    {
        "num": 38,
        "id": "F.38",
        "slug": "pedal-triangles",
        "legacy_folder": "38.pedol-triangles",
        "title": "Pedal Triangles",
        "subtitle": "Trilinear Pedal Side Lengths, Euler's Pedal Area Theorem, and Carnot's Perpendicularity Law",
        "category": "Triangle Centers & Classical Circles",
        "tags": ["pedal-triangle", "trilinear", "carnot", "circumcircle", "area"],
        "enunciation": (
            "The pedal triangle A'B'C' of a point P(tau_A : tau_B : tau_C) has area "
            "Delta(P) = ((R^2 - OP^2)/(4 R^2)) Delta, and its six side-projection segments "
            "satisfy Carnot's alternating square identity AC'^2 + BA'^2 + CB'^2 = C'B^2 + A'C^2 + B'A^2."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point", "P : Point"],
        "signature_steps": [
            "P_A = foot(P, line(B, C))",
            "P_B = foot(P, line(C, A))",
            "P_C = foot(P, line(A, B))",
            "s_ab = segment(P_A, P_B)",
            "s_bc = segment(P_B, P_C)",
            "s_ca = segment(P_C, P_A)",
        ],
        "synthesis": [
            "In this two-folio study (:cite:`SeeligNotebooks`), Seelig summarizes the metric and coordinate "
            "laws of the :term:`pedal triangle` :math:`\\triangle A'B'C'` (labeled :g:`P_A`, :g:`P_B`, :g:`P_C` "
            "in the construction) of a point :g:`P` with homogeneous trilinear coordinates "
            ":math:`(\\tau_A : \\tau_B : \\tau_C)`. Folio 1 records the exact pedal side length "
            ":math:`a' = \\frac{abc\\sqrt{\\tau_B^2 + \\tau_C^2 + 2\\tau_B\\tau_C\\cos\\alpha}}{2R(a\\tau_A + b\\tau_B + c\\tau_C)}` "
            "and :person:`Euler`'s pedal area theorem :math:`(\\Delta P) = \\frac{R^2 - OP^2}{4R^2}\\Delta`, "
            "which vanishes precisely when :g:`P` lies on the :term:`circumcircle` (:person:`Simson`'s line theorem).",
            "Folio 2 pairs :person:`Carnot`'s alternating segment square identity "
            ":math:`{AC'}^2 + {BA'}^2 + {CB'}^2 = {C'B}^2 + {A'C}^2 + {B'A}^2` (annotated with Seelig's marginal "
            'exclamation *"wow!"*) with the :math:`3\\times 3` trilinear coordinate matrix for the vertices '
            ":math:`A', B', C'`.",
        ],
        "equations": [
            r"a' = \frac{a b c \sqrt{\tau_B^2 + \tau_C^2 + 2\tau_B\tau_C\cos\alpha}}{2 R (a\tau_A + b\tau_B + c\tau_C)}, \qquad \Delta(P) = \frac{R^2 - OP^2}{4 R^2}\Delta",
            r"{AC'}^2 + {BA'}^2 + {CB'}^2 = {C'B}^2 + {A'C}^2 + {B'A}^2",
        ],
        "depends_on": ["F.4", "F.36"],
        "euclid_refs": ["I.12", "I.47"],
        "elements_refs": ["G.4", "G.11"],
        "etc_refs": ["X(1)", "X(3)", "X(4)"],
        "spreadsheets": ["Pedal Triangle", "Orthic Triangle"],
        "folio_summaries": [
            (
                "Pedal Triangle Side Lengths & Area Formula",
                "Records the trilinear pedal side-length formula for :math:`a', b', c'` and Euler's pedal area relation :math:`(\\Delta P) = \\frac{R^2-OP^2}{4R^2}\\Delta`.",
            ),
            (
                "Carnot's Alternating Square Law & Trilinear Matrix",
                "Writes the alternating segment square equality :math:`{AC'}^2 + {BA'}^2 + {CB'}^2 = {C'B}^2 + {A'C}^2 + {B'A}^2` (*'wow!'*) and the :math:`3\\times 3` trilinear coordinate matrix of :math:`A', B', C'`.",
            ),
        ],
    },
    {
        "num": 39,
        "id": "F.39",
        "slug": "pole-polar",
        "legacy_folder": "39.pole-polar",
        "title": "Pole and Polar with Respect to a Triangle",
        "subtitle": "Trilinear Polar Line, Desargues Perspectivity, and Metric Distance Questions",
        "category": "Projective & Harmonic Geometry",
        "tags": [
            "pole-polar",
            "projective",
            "trilinear-polar",
            "desargues",
            "harmonic",
        ],
        "enunciation": (
            "Given a triangle ABC and a point P with cevian traces A', B', C', the intersections "
            "X = BC cap B'C', Y = CA cap C'A', and Z = AB cap A'B' are collinear on the trilinear "
            "polar L of the pole P."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point", "P : Point"],
        "signature_steps": [
            "A_p = intersection(line(B, C), line(A, P))",
            "B_p = intersection(line(C, A), line(B, P))",
            "C_p = intersection(line(A, B), line(C, P))",
            "X = intersection(line(B, C), line(B_p, C_p))",
            "Y = intersection(line(C, A), line(C_p, A_p))",
            "polar = line(X, Y)",
        ],
        "synthesis": [
            "Dated May 6, 2015 (:cite:`SeeligNotebooks`), Seelig's study *POLE & POLAR W.r.t. A TRIANGLE "
            "(projective geometry)* constructs the :term:`trilinear polar` :g:`polar` (line :math:`L`) of a "
            "perspector/pole :g:`P` with respect to :math:`\\triangle ABC`. Drawing the cevians through :g:`P` "
            "to their traces :g:`A_p`, :g:`B_p`, :g:`C_p` (:math:`A', B', C'`), the harmonic conjugates "
            ":g:`X` :math:`= BC \\cap B'C'`, :g:`Y` :math:`= CA \\cap C'A'`, and :math:`Z = AB \\cap A'B'` "
            "are collinear by :person:`Desargues`'s Theorem along the trilinear polar :math:`L`.",
            "In the lower half of the folio, Seelig formulates a program of metric research questions linking "
            "projective duality to Euclidean triangle centers: determining the perpendicular distance "
            ":math:`d(P, L)` and the distances :math:`OP, IP, OL, IL` from the :term:`circumcenter` :g:`O` and "
            ":term:`incenter` :g:`I` to the pole :g:`P` and polar :math:`L` in terms of barycentric coordinates.",
        ],
        "equations": [
            r"P = (u : v : w) \iff L:\; \frac{x}{u} + \frac{y}{v} + \frac{z}{w} = 0",
            r"(B, C;\, A', X) = (C, A;\, B', Y) = (A, B;\, C', Z) = -1",
        ],
        "depends_on": ["F.7", "F.25"],
        "euclid_refs": ["VI.2", "VI.3"],
        "elements_refs": ["G.5"],
        "etc_refs": ["X(1)", "X(2)", "X(3)"],
        "spreadsheets": ["Pole & Polar", "Harmonic Conjugates"],
        "folio_summaries": [
            (
                "Pole & Polar W.r.t. a Triangle (May 6, 2015)",
                "Constructs the cevian triangle :math:`A'B'C'` of pole :math:`P` and the collinear perspectrix/trilinear polar :math:`L` through :math:`X, Y, Z`, posing open metric questions for :math:`d(P,L), OP, IP, OL, IL`.",
            ),
        ],
    },
    {
        "num": 40,
        "id": "F.40",
        "slug": "polygons",
        "legacy_folder": "40.polygons",
        "title": "Regular Polygons and Nested Radicals",
        "subtitle": "Archimedean Edge-Doubling Recursion, Golden Decagon/Pentagon Radicals, and the Pentadecagon",
        "category": "Polygons, Tessellations & Special Triangles",
        "tags": [
            "polygons",
            "pentagon",
            "decagon",
            "pentadecagon",
            "golden-ratio",
            "radicals",
        ],
        "enunciation": (
            "For a regular N-gon inscribed in a unit circle (R = 1), doubling the number of sides "
            "maps edge length E_{N/2} to E_N = sqrt(2 - sqrt(4 - E_{N/2}^2)), generating closed-form "
            "nested quadratic radicals for the 2^k, 3*2^k, 5*2^k, and 15*2^k polygon families."
        ),
        "signature_given": ["O : Point", "A : Point"],
        "signature_steps": [
            "c_unit = circle(O, A)",
            "l_oa = line(O, A)",
            "perp = perpendicular(O, l_oa)",
            "B = intersection(perp, c_unit)",
            "M = midpoint(O, B)",
            "c_five = circle(M, A)",
        ],
        "synthesis": [
            "Spanning 18 folios (:cite:`SeeligNotebooks`), Seelig's treatise on regular :term:`polygons` "
            "derives the Archimedean edge-doubling recursion :math:`E_N = \\sqrt{2 - \\sqrt{4 - E_{N/2}^2}}` "
            "(for circumradius :math:`R=1`, where :math:`E_N = 2\\sin(\\pi/N)` and apothem "
            ":math:`r_N = \\frac{1}{2}\\sqrt{4 - E_N^2}`) and compiles complete nested-radical tables across "
            "four constructible families: the square/octagon chain (:math:`E_4 = \\sqrt{2}, E_8 = \\sqrt{2-\\sqrt{2}}, "
            "E_{16}, E_{32}, E_{64}`), the triangle/hexagon/dodecagon chain (:math:`E_3 = \\sqrt{3}, E_6 = 1, "
            "E_{12} = \\sqrt{2-\\sqrt{3}}, E_{24}`), and the :term:`golden ratio` pentagon/decagon chain "
            "(:math:`E_5 = \\sqrt{3-\\phi} = \\frac{1}{2}\\sqrt{10-2\\sqrt{5}} \\approx 1.17557, "
            "E_{10} = \\sqrt{2-\\phi} = \\phi - 1 \\approx 0.61803, E_{20} = \\sqrt{2-\\sqrt{2+\\phi}}`).",
            "Dated April 20, 2015, the second half of the dossier investigates the regular 15-gon "
            "(:person:`Euclid` *Elements* :ref:`IV.16`, :math:`E_{15} = 2\\sin 12^\\circ \\approx 0.41582`), "
            "citing James Stafford's exact radical table for multiples of :math:`\\pi/30 = 6^\\circ`, alongside "
            "an angle-chasing exploration of the regular enneagon (:math:`N=9`, requiring a cubic trisection) "
            "and two auxiliary Cartesian cevian sheets.",
        ],
        "equations": [
            r"E_N = 2\sin\frac{\pi}{N} = \sqrt{2 - \sqrt{4 - E_{N/2}^2}}, \qquad r_N = \cos\frac{\pi}{N} = \frac{1}{2}\sqrt{4 - E_N^2}",
            r"E_{10} = \phi - 1 = \sqrt{2 - \phi}, \qquad E_5 = \sqrt{3 - \phi}, \qquad E_{15} = 2\sin 12^\circ = \frac{1}{4}\left(\sqrt{10 + 2\sqrt{5}} + \sqrt{3} - \sqrt{15}\right)",
        ],
        "depends_on": ["F.23"],
        "euclid_refs": ["IV.11", "IV.15", "IV.16", "XIII.9", "XIII.10"],
        "elements_refs": ["G.9", "G.10"],
        "etc_refs": [],
        "spreadsheets": ["Polygon Table", "Golden Triangle"],
        "folio_summaries": [
            (
                "Edge-Doubling Recursion for Unit-Circle Polygons (2-001)",
                "Derives :math:`E_N = \\sqrt{2-\\sqrt{4-E_{N/2}^2}}` and apothem :math:`r_N = \\frac{1}{2}\\sqrt{4-E_N^2}` from the sagitta right triangle in a unit circle (:math:`R=1`).",
            ),
            (
                "Square & Octagon Doubling Family (2-002)",
                "Evaluates nested radicals for :math:`N = 4, 8, 16, 32, 64` starting from :math:`E_4 = \\sqrt{2}`.",
            ),
            (
                "Hexagon & Dodecagon Doubling Family (2-003)",
                "Evaluates nested radicals for :math:`N = 3, 6, 12, 24, 48` starting from :math:`E_3 = \\sqrt{3}` and :math:`E_6 = 1`.",
            ),
            (
                "Pentagon & Decagon Golden Ratio Radicals (2-004)",
                "Expresses :math:`E_{10} = \\phi^{-1} = \\sqrt{2-\\phi}`, :math:`E_5 = \\sqrt{3-\\phi}`, and :math:`E_{20} = \\sqrt{2-\\sqrt{2+\\phi}}` in terms of :math:`\\phi = \\frac{1+\\sqrt{5}}{2}`.",
            ),
            (
                "Master Polygon Reference Table (2-005)",
                "Compiles :math:`N, \\theta_N, E_N, r_N`, and perimeter :math:`N E_N \\to 2\\pi` across all constructible families.",
            ),
            (
                "Regular Pentadecagon E_15 Derivation (2-006, FWS 4/20/2015)",
                "Computes :math:`E_{15} = 2\\sin 12^\\circ \\approx 0.415823` using :math:`12^\\circ = 30^\\circ - 18^\\circ` and Euclid IV.16.",
            ),
            (
                "Stafford's Exact Radical Table for pi/30 (2-007)",
                "Cites James Stafford's trigonometric radical table for multiples of :math:`6^\\circ = \\pi/30` to verify :math:`\\sin 12^\\circ` and :math:`\\cos 12^\\circ`.",
            ),
            (
                "Pentadecagon Apothem & Area (2-008)",
                "Simplifies the nested radical for :math:`r_{15} = \\cos 12^\\circ` and the area :math:`K_{15} = \\frac{15}{2}E_{15}r_{15}`.",
            ),
            (
                "30-gon & 60-gon Doubling Steps (2-009)",
                "Applies the edge-doubling recursion to :math:`E_{15}` to obtain :math:`E_{30}` and :math:`E_{60}`.",
            ),
            (
                "Inscribed Triangle & Square Constructions (001)",
                "Compass diagrams of the inscribed equilateral triangle (:math:`E_3 = \\sqrt{3}R`) and square (:math:`E_4 = \\sqrt{2}R`).",
            ),
            (
                "Inscribed Pentagon & Decagon Geometry (002)",
                "Shows Ptolemy's / Euclid XIII.10 relation :math:`E_5^2 = R^2 + E_{10}^2` inside the unit circle.",
            ),
            (
                "Golden Triangle & Gnomon Decomposition of the Decagon (003)",
                "Partitions the regular decagon into ten acute :math:`72^\\circ\\text{--}72^\\circ\\text{--}36^\\circ` golden triangles.",
            ),
            (
                "Chord Length & Central Angle Identities (004)",
                "Relates chord length :math:`c(\\theta) = 2R\\sin(\\theta/2)` to the sagitta :math:`s = R - \\sqrt{R^2 - (c/2)^2}`.",
            ),
            (
                "Polygon Perimeter & Area Convergence to pi (005)",
                "Tabulates :math:`\\pi_N = \\frac{N}{2}E_N` and :math:`A_N = \\frac{N}{2}E_N r_N` for increasing :math:`N`.",
            ),
            (
                "Regular Enneagon (N = 9) Angle-Chasing Attempt — Page 1 (006)",
                "Investigates chord relationships in the regular 9-gon (:math:`20^\\circ` central half-angle).",
            ),
            (
                "Regular Enneagon (N = 9) Diagonal Relations — Page 2 (007)",
                "Records the three diagonal lengths of the regular enneagon and notes the irreducible cubic :math:`x^3 - 3x + 1 = 0`.",
            ),
            (
                "Cartesian Cevian Length Sheet — Part 1 (009)",
                "Derives cevian segment lengths in a Cartesian triangle frame.",
            ),
            (
                "Cartesian Cevian Length Sheet — Part 2 (010)",
                "Completes the algebraic expansion of the Cartesian cevian length formula.",
            ),
        ],
    },
    {
        "num": 41,
        "id": "F.41",
        "slug": "problems",
        "legacy_folder": "41.problems",
        "title": "Geometric Problems and Extremal Loci",
        "subtitle": "Maximizing Euler Distance d_IO for Acute Triangles, Monte Carlo Vesica Integration, and 25-Problem Compendium",
        "category": "Polygons, Tessellations & Special Triangles",
        "tags": ["problems", "monte-carlo", "vesica-piscis", "euler", "acute"],
        "enunciation": (
            "Among all triangles with longest side c = |AB| = 1, the acute locus inside the "
            "vesica piscis above the semicircle on AB has area A = int_0^{sqrt(3)} (sqrt(4 - x^2) - 1) dx "
            "- pi/4 = (5 pi - 6 sqrt(3))/12 approx 0.44297 (for c = 2), and maximizing d_IO over "
            "acute triangles approaches the degenerate right-isosceles limit C -> (0, 1)."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "M = midpoint(A, B)",
            "c_semi = circle(M, A)",
            "c_left = circle(A, B)",
            "c_right = circle(B, A)",
            "O = circumcenter(A, B, C)",
            "I = incenter(A, B, C)",
        ],
        "synthesis": [
            "This 10-folio collection (:cite:`SeeligNotebooks`) combines two analytic geometry sheets "
            "(Folios 1–2), a dated calculus and Monte Carlo investigation *Find an acute triangle that "
            "maximizes :math:`d_{IO}`* (`FWS 2015/04/24`, Folios 3–4), and a 25-problem compendium "
            "(*Problem Set*, Folios 5–10) that served as the blueprint for Seelig's notebook archive.",
            "In his April 24, 2015 study, Seelig fixes base :math:`c = 2` and constrains vertex :g:`C` to "
            "the region where :math:`c` is the longest side (inside the :term:`vesica piscis` of radii 2 "
            "centered at :g:`A` and :g:`B`) while :math:`\\triangle ABC` remains acute (outside the semicircle "
            ":g:`c_semi` of radius 1 and between the vertical lines at :g:`A` and :g:`B`). Integrating "
            ":math:`A = \\int_0^{\\sqrt{3}}(\\sqrt{4-x^2}-1)\\,dx - \\frac{\\pi}{4} = \\frac{5\\pi - 6\\sqrt{3}}{12} \\approx 0.44297`, "
            "he explains why his spreadsheet Monte Carlo sampler on :math:`[0,\\sqrt{3}]\\times[0,1]` has an "
            "acceptance rate of :math:`0.44297/\\sqrt{3} \\approx 25.6\\%`, and finds that :math:`d_{IO}` increases "
            "monotonically toward the right-triangle boundary :math:`C \\to (0, 1)`.",
        ],
        "equations": [
            r"A_{\text{acute}} = \int_0^{\sqrt{3}} \left(\sqrt{4 - x^2} - 1\right) dx - \frac{\pi}{4} = \frac{5\pi - 6\sqrt{3}}{12} \approx 0.44297",
            r"p_{\text{accept}} = \frac{A_{\text{acute}}}{\sqrt{3}} \approx 0.25575, \qquad d_{IO} = \sqrt{R^2 - 2 r R}",
        ],
        "depends_on": ["F.32", "F.35", "F.37"],
        "euclid_refs": ["I.1", "III.31"],
        "elements_refs": ["G.1", "G.7"],
        "etc_refs": ["X(1)", "X(3)"],
        "spreadsheets": ["Monte Carlo", "General Reference"],
        "folio_summaries": [
            (
                "Algebraic & Radical Simplification Sheet (001)",
                "Works through radical and quadratic simplifications used across the triangle problem set.",
            ),
            (
                "Coordinate Line & Circle Intersection Sheet (002)",
                "Solves simultaneous line-circle equations in Cartesian coordinates.",
            ),
            (
                "Maximizing d_IO for an Acute Triangle — Vesica Integration (2-001, FWS 2015/04/24)",
                "Integrates the acute region :math:`A = \\int_0^{\\sqrt{3}}(\\sqrt{4-x^2}-1)\\,dx - \\pi/4 \\approx 0.44297` above the right-triangle semicircle to explain the 26% Monte Carlo hit rate.",
            ),
            (
                "Extremal Limit C -> (0, 1) for d_IO (2-002)",
                "Tracks :math:`R, r, d_{IO}` as :math:`C` approaches the boundary point :math:`(0,1)` of the acute region.",
            ),
            (
                "Master Geometry Problem Set — Problems 1–4 (2-003)",
                "States research problems on triangle reconstruction from partial elements, Euler's formula, and harmonic division.",
            ),
            (
                "Master Geometry Problem Set — Problems 5–9 (2-004)",
                "Poses problems on Apollonian circles, radical axes, and centers of similitude.",
            ),
            (
                "Master Geometry Problem Set — Problems 10–14 (2-005)",
                "Poses problems on Ceva, Menelaus, Stewart's Theorem, and barycentric coordinates.",
            ),
            (
                "Master Geometry Problem Set — Problems 15–19 (2-006)",
                "Poses problems on the nine-point circle, orthic triangle, and Conway's notation.",
            ),
            (
                "Master Geometry Problem Set — Problems 20–23 (2-007)",
                "Poses problems on regular polygons, golden triangles, and biquadratic Heron forms.",
            ),
            (
                "Master Geometry Problem Set — Problems 24–25 (2-008)",
                "Concludes the 25-problem syllabus with projective pole-polar and bilinear transformation challenges.",
            ),
        ],
    },
    {
        "num": 42,
        "id": "F.42",
        "slug": "pythagorean-triples",
        "legacy_folder": "42.pythagorean-triples",
        "title": "Altitude of a Pythagorean Triple Triangle",
        "subtitle": "Inverse Pythagorean Theorem, Hypotenuse Projections, and Incircle Touchpoint Distinction",
        "category": "Polygons, Tessellations & Special Triangles",
        "tags": [
            "pythagorean-triples",
            "altitude",
            "right-triangle",
            "euclid",
            "harmonic",
        ],
        "enunciation": (
            "In a right triangle with legs a, b and hypotenuse c, the altitude h_c = a b / c "
            "satisfies the Inverse Pythagorean Theorem 1/h_c^2 = 1/a^2 + 1/b^2 and divides the "
            "hypotenuse into projections u = b^2/c and y = a^2/c with h_c^2 = u y."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "c_hyp = segment(A, B)",
            "H_C = foot(C, line(A, B))",
            "h_c = segment(C, H_C)",
            "I = incenter(A, B, C)",
            "T_C = foot(I, line(A, B))",
        ],
        "synthesis": [
            "Titled *The Altitude of a Pythagorean Triple Triangle* (:cite:`SeeligNotebooks`), this four-folio "
            "study examines the right-triangle altitude :g:`h_c` dropped from the right angle :g:`C` to the "
            "hypotenuse :g:`A` :g:`B` (:person:`Euclid` *Elements* :ref:`VI.8`). Equating twice the area "
            ":math:`2K = ab = ch_c` gives :math:`h_c = ab/c` and the Inverse Pythagorean Theorem "
            ":math:`\\frac{1}{h_c^2} = \\frac{a^2+b^2}{a^2 b^2} = \\frac{1}{a^2} + \\frac{1}{b^2}`, while "
            "the hypotenuse projections :math:`u = b^2/c` and :math:`y = a^2/c` satisfy the :term:`geometric mean` "
            "identity :math:`h_c = \\sqrt{uy}`.",
            "On Folio 3, Seelig highlights a classic geometric pitfall inside a bold warning box: the cevian "
            "from :g:`C` to the :term:`incircle` touchpoint :g:`T_C` (which splits :math:`c` into "
            ":math:`s-a` and :math:`s-b` with :math:`K = (s-a)(s-b)`) does *not* coincide with the perpendicular "
            'altitude foot :g:`H_C` (*"CT_c is not \\perp to BA"*) unless :math:`a = b`.',
        ],
        "equations": [
            r"h_c = \frac{a b}{c}, \qquad \frac{1}{h_c^2} = \frac{1}{a^2} + \frac{1}{b^2}, \qquad u = \frac{b^2}{c},\; y = \frac{a^2}{c},\; h_c^2 = u y",
            r"|A T_C| = s - a \neq u = \frac{b^2}{c} \quad (a \neq b), \qquad K = (s - a)(s - b) = \frac{a b}{2}",
        ],
        "depends_on": ["F.10", "F.29", "F.33"],
        "euclid_refs": ["I.47", "VI.8"],
        "elements_refs": ["G.4", "G.11"],
        "etc_refs": ["X(1)", "X(4)", "X(7)"],
        "spreadsheets": ["Pythagorean Triples", "Right Triangle", "Altitudes"],
        "folio_summaries": [
            (
                "Altitude of a Pythagorean Triple Triangle (001)",
                "Derives :math:`h_c = ab/c`, the Inverse Pythagorean Theorem :math:`h_c^{-2} = a^{-2} + b^{-2}`, and the hypotenuse segments :math:`u = b^2/c, y = a^2/c`.",
            ),
            (
                "Rational Evaluation on Primitive Triples (002)",
                "Evaluates :math:`h_c, u, y` on :math:`(3,4,5)\\mapsto (12/5, 9/5, 16/5)` and :math:`(5,12,13)\\mapsto (60/13, 25/13, 144/13)`.",
            ),
            (
                "Self-Corrected Fallacy Box: CT_c vs. Altitude CH_c (003)",
                "Proves that the incircle touchpoint :math:`T_C` (:math:`|AT_C| = s-a`) is distinct from the altitude foot :math:`H_C` (:math:`|AH_C| = b^2/c`), boxing the warning *'CT_c is not \\perp to BA'*.",
            ),
            (
                "Orthocentric Projection Segments (004)",
                "Relates the right-triangle altitude segments to the general orthocentric system of an acute/obtuse triangle.",
            ),
        ],
    },
    {
        "num": 43,
        "id": "F.43",
        "slug": "radical-axes",
        "legacy_folder": "43.radical-axes",
        "title": "Radical Axes and Radical Center",
        "subtitle": "Two-Circle Radical Division, Vertex-Altitude Circle Radical Center, and Circular Lens Regimes",
        "category": "Circle Inversion, Coaxial & Radical Systems",
        "tags": ["radical-axis", "radical-center", "coaxial", "altitude", "circles"],
        "enunciation": (
            "The radical axis of two circles of radii r_1, r_2 with center separation d cuts the "
            "line of centers at x = d/2 + (r_1^2 - r_2^2)/(2 d) from O_1, and the three radical axes "
            "of the vertex-altitude circles Gamma_A(h_A), Gamma_B(h_B), Gamma_C(h_C) concur at the "
            "radical center W."
        ),
        "signature_given": ["O_1 : Point", "A_1 : Point", "O_2 : Point", "A_2 : Point"],
        "signature_steps": [
            "c_1 = circle(O_1, A_1)",
            "c_2 = circle(O_2, A_2)",
            "l_centers = line(O_1, O_2)",
            "P_1 = intersection(c_1, c_2)",
            "rad_axis = perpendicular(P_1, l_centers)",
        ],
        "synthesis": [
            "Spanning 11 folios (:cite:`SeeligNotebooks`), Seelig's treatise on the :term:`radical axis` "
            "begins (Folio 1) with the fundamental two-circle division formula "
            ":math:`x = \\frac{d}{2} + \\frac{r_1^2 - r_2^2}{2d}`, tested on :math:`r_1=1, r_2=2, d=5` to give "
            ":math:`|O_1 P| = 2.2, |O_2 P| = 2.8`, and equal tangent length :math:`t = \\frac{4\\sqrt{6}}{5} \\approx 1.9596`. "
            "Folios 2–8 (`FWS Dec. 8/2014`) execute an ambitious 7-page analytic calculation: placing circles "
            ":math:`\\Gamma_A(h_A), \\Gamma_B(h_B), \\Gamma_C(h_C)` at the vertices of a triangle with radii equal "
            "to the three altitudes, Seelig derives each pairwise radical axis in double-intercept form "
            ":math:`\\frac{x}{x_0} + \\frac{y}{y_0} = 1` and solves for their common :term:`radical center` "
            ":math:`W = (2.586, 0.603)` on the :math:`(2,3,4)` triangle.",
            "Folios 9–11 classify the five relative position regimes of two circles as :math:`d` varies from "
            ":math:`d > r_1 + r_2` (disjoint) through external/internal tangency to :math:`d < |r_1 - r_2|`, "
            "recording the circular lens intersection chord and area.",
        ],
        "equations": [
            r"x = |O_1 P| = \frac{d}{2} + \frac{r_1^2 - r_2^2}{2 d}, \qquad x' = |O_2 P| = \frac{d}{2} - \frac{r_1^2 - r_2^2}{2 d}, \qquad t^2 = x^2 - r_1^2 = {x'}^2 - r_2^2",
            r"\Gamma_A(A, h_A),\; \Gamma_B(B, h_B),\; \Gamma_C(C, h_C) \implies \frac{x}{x_0} + \frac{y}{y_0} = 1",
        ],
        "depends_on": ["F.9", "F.12"],
        "euclid_refs": ["II.5", "III.36"],
        "elements_refs": ["G.7", "G.11"],
        "etc_refs": [],
        "spreadsheets": ["Radical Axes", "Coaxial Circles"],
        "folio_summaries": [
            (
                "Two-Circle Radical Axis & Equal Tangents (001)",
                "Derives :math:`x = \\frac{d}{2} + \\frac{r_1^2-r_2^2}{2d}` and tests :math:`r_1=1, r_2=2, d=5 \\implies x=2.2, x'=2.8, t = \\frac{4\\sqrt{6}}{5}`.",
            ),
            (
                "Radical Center of Vertex-Altitude Circles — Setup (002, FWS Dec. 8/2014)",
                "Defines circles :math:`\\Gamma_A(h_A), \\Gamma_B(h_B), \\Gamma_C(h_C)` centered at :math:`A, B, C` with radii equal to the three altitudes.",
            ),
            (
                "Radical Axis of Gamma_A and Gamma_B (003)",
                "Computes the radical foot along side :math:`c = AB` and writes the perpendicular line equation.",
            ),
            (
                "Radical Axis of Gamma_A and Gamma_C in Intercept Form (004)",
                "Projects the radical axis of :math:`\\Gamma_A` and :math:`\\Gamma_C` onto the Cartesian frame of :math:`AB` and derives :math:`x/x_0 + y/y_0 = 1`.",
            ),
            (
                "Radical Axis of Gamma_B and Gamma_C (005)",
                "Derives the double-intercept equation for the third radical axis opposite side :math:`a = BC`.",
            ),
            (
                "2x2 Linear System for the Radical Center W (006)",
                "Intersects two radical axes in intercept form to solve for the radical center :math:`W = (W_x, W_y)`.",
            ),
            (
                "Numerical Evaluation on the (2, 3, 4) Triangle — Part 1 (007)",
                "Computes the altitudes :math:`h_A, h_B, h_C` and pairwise radical intercepts of the :math:`(2,3,4)` obtuse triangle.",
            ),
            (
                "Numerical Evaluation on the (2, 3, 4) Triangle — Part 2 (008)",
                "Finds the exact radical center coordinates :math:`W = (2.586, 0.603)` and verifies concurrency of all three radical axes.",
            ),
            (
                "Two-Circle Separation Regimes (009)",
                "Classifies disjoint, externally tangent, intersecting, internally tangent, and nested circle pairs by comparing :math:`d` with :math:`r_1 \\pm r_2`.",
            ),
            (
                "Common Chord & Sagitta of Intersecting Circles (010)",
                "Expresses the common chord length :math:`2y = 2\\sqrt{r_1^2 - x^2}` in terms of Heron's radical on :math:`(r_1, r_2, d)`.",
            ),
            (
                "Circular Lens Area Formula (011)",
                "Integrates/sums the two circular sector-minus-triangle segments to obtain the asymmetric lens area.",
            ),
        ],
    },
    {
        "num": 44,
        "id": "F.44",
        "slug": "ratios",
        "legacy_folder": "44.ratios",
        "title": "Homothetic Ratios and Crossed Diagonals",
        "subtitle": "Internal and External Division of Parallel Uprights from a Center of Similitude",
        "category": "Projective & Harmonic Geometry",
        "tags": ["ratios", "similitude", "homothety", "harmonic", "crossed-ladders"],
        "enunciation": (
            "Given two parallel uprights of heights h_1 < h_2 separated by horizontal distance d "
            "and viewed from their external center of similitude O, the crossed diagonals meet at "
            "horizontal distance x = d h_1 / (h_1 + h_2) from the first upright, while O lies at "
            "distance y - x = d h_1 / (h_2 - h_1) to its left, forming a harmonic range."
        ),
        "signature_given": ["A : Point", "B : Point", "P_1 : Point", "P_2 : Point"],
        "signature_steps": [
            "s_1 = segment(A, P_1)",
            "s_2 = segment(B, P_2)",
            "O_ext = intersection(line(A, B), line(P_1, P_2))",
            "O_int = intersection(line(A, P_2), line(B, P_1))",
        ],
        "synthesis": [
            "Across five folios (:cite:`SeeligNotebooks`), Seelig analyzes the projective and metric "
            "proportions of two homothetic right triangles sharing an apex angle :math:`\\phi` at :g:`O_ext` "
            "with parallel vertical uprights :math:`h_1 < h_2` separated by distance :math:`d` along the "
            "baseline :g:`A` :g:`B`. By similar triangles (:person:`Euclid` *Elements* :ref:`VI.2` and :ref:`VI.4`), "
            "the crossed diagonals :math:`AP_2` and :math:`BP_1` intersect at :g:`O_int` at horizontal distance "
            ":math:`x = d\\frac{h_1}{h_1+h_2}` from :g:`A` (and height :math:`h = \\frac{h_1 h_2}{h_1+h_2}`, "
            "half the :term:`harmonic mean`), while the external apex :g:`O_ext` lies at distance "
            ":math:`y - x = d\\frac{h_1}{h_2-h_1}` from :g:`A`.",
            "Adding the internal and external distances yields the total span between the two centers of "
            "similitude :math:`y = \\frac{2 d h_1 h_2}{h_2^2 - h_1^2}` and its midpoint "
            ":math:`z = \\frac{d h_1 h_2}{h_2^2 - h_1^2}`, reproducing the Apollonian :term:`harmonic conjugate` "
            "formulas with :math:`k = h_2/h_1`.",
        ],
        "equations": [
            r"x = d\frac{h_1}{h_1 + h_2}, \qquad y - x = d\frac{h_1}{h_2 - h_1}, \qquad h = \frac{h_1 h_2}{h_1 + h_2}",
            r"y = \frac{2 d h_1 h_2}{h_2^2 - h_1^2}, \qquad z = \frac{y}{2} = \frac{d h_1 h_2}{h_2^2 - h_1^2}",
        ],
        "depends_on": ["F.5", "F.25", "F.27"],
        "euclid_refs": ["VI.2", "VI.4"],
        "elements_refs": ["G.5"],
        "etc_refs": [],
        "spreadsheets": ["Centers of Similitude", "Harmonic Conjugates"],
        "folio_summaries": [
            (
                "Homothetic Right Triangles & Crossed Diagonals (001)",
                "Sets up uprights :math:`h_1, h_2` separated by :math:`d` from apex :math:`O` (angle :math:`\\phi`) and derives :math:`x = d h_1/(h_1+h_2)` and :math:`y-x = d h_1/(h_2-h_1)`.",
            ),
            (
                "Total Span y & Midpoint z Between Similitude Centers (002)",
                "Combines :math:`x` and :math:`y-x` to obtain :math:`y = \\frac{2dh_1h_2}{h_2^2-h_1^2}` and :math:`z = \\frac{dh_1h_2}{h_2^2-h_1^2}`.",
            ),
            (
                "Crossed-Ladder Height & Harmonic Mean (003)",
                "Shows that the height of the crossed-diagonal intersection is :math:`h = \\frac{h_1 h_2}{h_1+h_2} = \\frac{1}{2}H(h_1,h_2)`, independent of :math:`d`.",
            ),
            (
                "Dimensionless Ratio Parameterization k = h_2 / h_1 (004)",
                "Divides top and bottom by :math:`h_1^2` to recover the canonical Apollonian formulas :math:`x = d/(k+1), y-x = d/(k-1), z = dk/(k^2-1)`.",
            ),
            (
                "Numerical & Graphical Verification (005)",
                "Tests the formulas on integer height pairs :math:`(h_1, h_2) = (1,2)` and :math:`(2,3)`.",
            ),
        ],
    },
    {
        "num": 45,
        "id": "F.45",
        "slug": "squares",
        "legacy_folder": "45.squares",
        "title": "Squares, Subdivided Lattices, and the Japanese Theorem",
        "subtitle": "Inscribed Squares, Cevians Inside a Square, Equilateral Subdivisions, and Carnot's Theorem",
        "category": "Polygons, Tessellations & Special Triangles",
        "tags": ["squares", "polygons", "carnot", "japanese-theorem", "equilateral"],
        "enunciation": (
            "A square inscribed in a circle of radius R has side s = sqrt(2) R; inside a square of "
            "side s, intersecting cevians divide the interior in exact rational proportions, and by "
            "Carnot's Theorem the sum of inradii in any triangulation of a cyclic polygon is invariant."
        ),
        "signature_given": ["O : Point", "A : Point"],
        "signature_steps": [
            "c_out = circle(O, A)",
            "l_oa = line(O, A)",
            "C = intersection(l_oa, c_out)",
            "perp = perpendicular(O, l_oa)",
            "B = intersection(perp, c_out)",
            "D = intersection(perp, c_out)",
        ],
        "synthesis": [
            "This six-folio compilation (:cite:`SeeligNotebooks`) brings together four geometric studies "
            "centered on regular :term:`polygons` and triangulations: Folio 1 pairs the compass construction "
            "of a square (:math:`s = \\sqrt{2}R`) and an :term:`equilateral triangle` (:math:`s = \\sqrt{3}R`) "
            "inscribed in a circle of radius :math:`R`; Folios 2–3 solve for the Cartesian intersection "
            ":math:`N = (X_N, Y_N)` of two diagonal/edge cevians inside a square of side :math:`s`; "
            "Folio 4–5 analyze subdivided equilateral triangle lattices of side 6 and side 1; and Folio 6 "
            "summarizes :person:`Carnot`'s Theorem (:math:`OM_A + OM_B + OM_C = R + r`) as the foundation "
            "of the classic Japanese Sangaku theorem on cyclic polygon triangulations.",
        ],
        "equations": [
            r"s_{\square} = \sqrt{2}\,R, \qquad s_{\triangle} = \sqrt{3}\,R, \qquad OM_A + OM_B + OM_C = R + r",
            r"X_N = \frac{s \cdot u v}{u + v - u v}, \qquad Y_N = \frac{s \cdot u (1 - v)}{u + v - u v}",
        ],
        "depends_on": ["F.4", "F.18", "F.40"],
        "euclid_refs": ["IV.6", "IV.7"],
        "elements_refs": ["G.9"],
        "etc_refs": [],
        "spreadsheets": ["Polygon Table", "General Reference"],
        "folio_summaries": [
            (
                "Compass Construction of Inscribed Square & Equilateral Triangle (001)",
                "Inscribes a square of side :math:`\\sqrt{2}R` and an equilateral triangle of side :math:`\\sqrt{3}R` inside a circle of radius :math:`R`.",
            ),
            (
                "Line Intersection N Inside a Square — Setup (002)",
                "Sets up a square of side :math:`s` on Cartesian axes and writes the two-intercept equations of intersecting cevians meeting at :math:`N = (X_N, Y_N)`.",
            ),
            (
                "Line Intersection N Inside a Square — Solution (003)",
                "Solves the :math:`2\\times 2` linear system for :math:`(X_N, Y_N)` and computes the areas of the four resulting sub-regions.",
            ),
            (
                "Subdivided Square & Circle Packing Sketch (004)",
                "Sketches nested squares and inscribed circles scaling by powers of :math:`1/\\sqrt{2}`.",
            ),
            (
                "Subdivided Equilateral Triangles of Sides 6 and 1 (005)",
                "Partitions an equilateral triangle of side 6 into 36 unit equilateral triangles and computes sub-triangle altitudes and centroids.",
            ),
            (
                "Carnot's Theorem & the Japanese Sangaku Theorem (006)",
                "Recalls :math:`OM_A + OM_B + OM_C = R + r` and explains how summing over a cyclic polygon triangulation proves the invariance of the inradii sum.",
            ),
        ],
    },
    {
        "num": 46,
        "id": "F.46",
        "slug": "stewarts-theorem",
        "legacy_folder": "46.stewart-s-theorem",
        "title": "Stewart's Theorem",
        "subtitle": "Cevian Length Identity f^2 = k a^2 + k' b^2 - k k' c^2 and Apollonius's Median Formula",
        "category": "Projective & Harmonic Geometry",
        "tags": ["stewart", "apollonius", "cevian", "median", "cosine-law"],
        "enunciation": (
            "If a cevian of length f from C divides base c = AB into segments k' c and k c "
            "(with k + k' = 1), Stewart's Theorem states f^2 = k a^2 + k' b^2 - k k' c^2; "
            "at the midpoint k = k' = 1/2, this yields Apollonius's median formula "
            "f^2 = (1/2)(a^2 + b^2 - c^2/2)."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point", "D : Point"],
        "signature_steps": [
            "a = segment(B, C)",
            "b = segment(C, A)",
            "c = segment(A, B)",
            "f_cev = segment(C, D)",
            "H_C = foot(C, line(A, B))",
        ],
        "synthesis": [
            "Dated November 18, 2013 (:cite:`SeeligNotebooks`), Seelig's two-page proof of "
            ":term:`Stewart's theorem` (*\"Stewart's Theorem (also called :person:`Apollonius`' Theorem)\"*, "
            "after :person:`Stewart`'s 1746 *Some General Theorems of Considerable Use in the Higher Parts of "
            "Mathematics*, :cite:`Stewart1746`) normalizes the base segments of :math:`c = AB` by dimensionless "
            "barycentric weights :math:`k' = |AD|/c` and :math:`k = |DB|/c` (:math:`k + k' = 1`). Applying the "
            "Law of Cosines (or Euclid II.12/II.13 via the altitude foot :g:`H_C`) to the supplementary angles "
            "at :g:`D`, the cosine terms cancel upon weighting by :math:`k` and :math:`k'`, leaving the "
            "universal cevian formula :math:`f^2 = k a^2 + k' b^2 - k k' c^2`.",
            "On Folio 2, Seelig sets :math:`k = k' = 1/2` to immediately recover Apollonius's median length "
            "identity :math:`m_c^2 = \\frac{1}{2}\\left(a^2 + b^2 - \\frac{1}{2}c^2\\right)`. On the canonical "
            ":math:`(5,6,7)` triangle, this gives :math:`m_c^2 = \\frac{1}{2}(25 + 36 - 49/2) = \\frac{73}{4}`, "
            "so :math:`m_c = \\frac{\\sqrt{73}}{2}`.",
        ],
        "equations": [
            r"f^2 = k a^2 + k' b^2 - k k' c^2 \qquad (k + k' = 1,\; |AD| = k' c,\; |DB| = k c)",
            r"k = k' = \frac{1}{2} \implies m_c^2 = \frac{1}{2}\left(a^2 + b^2 - \frac{1}{2}c^2\right) = \frac{2 a^2 + 2 b^2 - c^2}{4}",
        ],
        "depends_on": ["F.6", "F.7", "F.35"],
        "euclid_refs": ["II.12", "II.13"],
        "elements_refs": ["G.3", "G.11"],
        "etc_refs": ["X(2)"],
        "spreadsheets": ["Stewart's Theorem", "Ceva & Menelaus", "Centroid"],
        "folio_summaries": [
            (
                "Stewart's Theorem Proof (stewart-001, FWS 11/18/2013)",
                "Defines dimensionless base fractions :math:`k, k'` (:math:`k+k'=1`) for cevian :math:`f = |CD|` and eliminates :math:`\\cos\\theta` between :math:`\\triangle ACD` and :math:`\\triangle BCD` to prove :math:`f^2 = k a^2 + k' b^2 - k k' c^2`.",
            ),
            (
                "Apollonius's Median Formula as Special Case (stewart-002)",
                "Evaluates Stewart's identity at the midpoint :math:`k = k' = 1/2` to obtain :math:`f^2 = \\frac{1}{2}(a^2 + b^2 - \\frac{1}{2}c^2)`.",
            ),
        ],
    },
    {
        "num": 47,
        "id": "F.47",
        "slug": "u-v-w",
        "legacy_folder": "47.u-v-w",
        "title": "The UVW Coordinate Triangle",
        "subtitle": "Altitude-Origin Cartesian Frame A(-U,0), B(W,0), C(0,V) and 2x2 Cevian Trace Matrices",
        "category": "Algebraic & Coordinate Systems",
        "tags": ["coordinates", "cevian", "heronian", "matrices", "ceva"],
        "enunciation": (
            "Placing the altitude foot H_C at the origin (0, 0) with A = (-U, 0), B = (W, 0), and "
            "C = (0, V) parameterizes any triangle by three numbers (U, V, W) with a = sqrt(V^2 + W^2), "
            "b = sqrt(U^2 + V^2), c = U + W, and reduces the cevian traces D, E, F through P(p, q) "
            "to explicit 2x2 rational matrix formulas."
        ),
        "signature_given": [
            "H_C : Point",
            "A : Point",
            "B : Point",
            "C : Point",
            "P : Point",
        ],
        "signature_steps": [
            "s_ab = segment(A, B)",
            "s_ch = segment(C, H_C)",
            "D = intersection(line(B, C), line(A, P))",
            "E = intersection(line(C, A), line(B, P))",
            "F = intersection(line(A, B), line(C, P))",
        ],
        "synthesis": [
            "Across 11 folios (:cite:`SeeligNotebooks`), Seelig develops his signature coordinate apparatus: "
            "*The UVW Triangle*. By placing the altitude foot :g:`H_C` at the Cartesian origin :math:`(0,0)` "
            "so that :g:`A` :math:`= (-U, 0)`, :g:`B` :math:`= (W, 0)`, and :g:`C` :math:`= (0, V)`, every "
            "side and line equation enters double-intercept form (:math:`AC: -x/U + y/V = 1` and "
            ":math:`BC: x/W + y/V = 1`). When :math:`(U, V)` and :math:`(V, W)` are chosen as legs of two "
            "Pythagorean triples sharing height :math:`V`—such as :math:`(U,V,W) = (5,12,16)` on Folios 3–4—"
            "the juxtaposed triangle has integer sides :math:`(a,b,c) = (20, 13, 21)` and integer area "
            ":math:`K = 126` (a Heronian triangle).",
            "Given an interior perspector :g:`P` :math:`= (p, q)`, Seelig formulates :math:`2\\times 2` matrix "
            "systems for the cevian traces :g:`D` :math:`= BC \\cap AP`, :g:`E` :math:`= CA \\cap BP`, and "
            ":g:`F` :math:`= AB \\cap CP`, testing the formulas on :math:`(U,V,W,p,q) = (8,8,16,4,4)` to obtain "
            "exact rational traces :math:`D = (6.4, 4.8), E = (-2, 6), F = (8, 0)` and verifying "
            ":person:`Ceva`'s ratio product :math:`1`.",
        ],
        "equations": [
            r"A = (-U, 0), \qquad B = (W, 0), \qquad C = (0, V), \qquad a^2 = V^2 + W^2,\; b^2 = U^2 + V^2,\; c = U + W",
            r"F_x = \frac{p V}{V - q}, \qquad D = \left(\frac{W V (U + p)}{V(U + W) + q W},\; \frac{V q (U + W)}{V(U + W) + q W}\right)",
        ],
        "depends_on": ["F.7", "F.35"],
        "euclid_refs": ["I.47", "VI.2"],
        "elements_refs": ["G.4", "G.5"],
        "etc_refs": ["X(2)", "X(4)"],
        "spreadsheets": ["UVW Triangle", "Ceva & Menelaus"],
        "folio_summaries": [
            (
                "The UVW Triangle — Coordinate & Intercept Setup (001)",
                "Places :math:`A=(-U,0), B=(W,0), C=(0,V)` around the altitude foot :math:`(0,0)` and writes the intercept equations of sides :math:`AC` and :math:`BC`.",
            ),
            (
                "2x2 Matrix System for Cevian Trace D (002)",
                "Intersects line :math:`AP` through :math:`P(p,q)` with side :math:`BC` via Cramer's rule to solve for :math:`D = (D_x, D_y)`.",
            ),
            (
                "Heronian Juxtaposition Example (U, V, W) = (5, 12, 16) — Page 1 (003)",
                "Combines :math:`(5,12,13)` and :math:`(12,16,20)` along shared altitude :math:`V=12` to form the :math:`(20,13,21)` Heronian triangle (:math:`K=126`).",
            ),
            (
                "Heronian Juxtaposition Example — Centers & Radii (004)",
                "Computes :math:`s=27, r = 14/3, R = 65/6`, and the coordinates of :math:`G, I, O, H` in the :math:`(5,12,16)` UVW frame.",
            ),
            (
                "2x2 Matrix System for Cevian Trace E (005)",
                "Intersects line :math:`BP` with side :math:`AC` to derive the closed-form coordinates of :math:`E = (E_x, E_y)`.",
            ),
            (
                "Cevian Trace F on the Baseline & Ceva Ratios (006)",
                "Finds :math:`F = (pV/(V-q), 0)` on the :math:`x`-axis and computes the signed Ceva ratios along all three sides.",
            ),
            (
                "Worked Benchmark (U, V, W, p, q) = (8, 8, 16, 4, 4) — Page 1 (007)",
                "Evaluates the matrix formulas at :math:`U=8, V=8, W=16, P=(4,4)` to obtain :math:`D=(6.4, 4.8), E=(-2, 6), F=(8, 0)`.",
            ),
            (
                "Worked Benchmark (8, 8, 16, 4, 4) — Ceva & Menelaus Check (008)",
                "Verifies that the segment ratios determined by :math:`D, E, F` multiply to :math:`1`.",
            ),
            (
                "Barycentric Conversion in the UVW Frame (009)",
                "Expresses the normalized barycentric coordinates :math:`(\\lambda_A, \\lambda_B, \\lambda_C)` of :math:`P(p,q)` in terms of :math:`U, V, W`.",
            ),
            (
                "Inverse Mapping from (a, b, c) to (U, V, W) (010)",
                "Uses Euclid II.12/II.13 to recover :math:`U = (b^2+c^2-a^2)/(2c), W = (a^2+c^2-b^2)/(2c)`, and :math:`V = 2K/c`.",
            ),
            (
                "Spreadsheet Formula Summary for the UVW Worksheet (011)",
                "Summarizes the cell formulas implemented in the ``UVW Triangle`` tab of ``Triangles and Circles.ods``.",
            ),
        ],
    },
    {
        "num": 48,
        "id": "F.48",
        "slug": "verisimilitude",
        "legacy_folder": "48.verisimilitude",
        "title": "Verisimilitude, Corner Subtriangles, and Excircle Homothety",
        "subtitle": "Incircle Tangent Subtriangles (r_A + r_B + r_C = r), Excircle Similitude, and Cevian Bounds",
        "category": "Circle Inversion, Coaxial & Radical Systems",
        "tags": ["similitude", "incircle", "excircle", "homothety", "stewart"],
        "enunciation": (
            "If lines parallel to the sides of triangle ABC are drawn tangent to the incircle, "
            "the three corner subtriangles are homothetic to ABC with scale factors x/s, y/s, z/s "
            "(where x = s - a, y = s - b, z = s - c), so their inradii satisfy r_A + r_B + r_C = r."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "I = incenter(A, B, C)",
            "T_A = foot(I, line(B, C))",
            "c_in = circle(I, T_A)",
            "P_A = intersection(segment(A, I), c_in)",
            "l_tan = perpendicular(P_A, line(A, I))",
        ],
        "synthesis": [
            "In this nine-folio investigation (:cite:`SeeligNotebooks`), Seelig explores homothetic scaling "
            "(*verisimilitude*) across three connected settings. First (Folios 1–4), drawing tangents to the "
            ":term:`incircle` parallel to :math:`BC, CA, AB` cuts off three corner subtriangles homothetic to "
            ":math:`\\triangle ABC` from vertices :g:`A`, :g:`B`, :g:`C`. Because the distance from :g:`A` to "
            "the incircle touchpoint is :math:`x = s-a`, the corner subtriangle at :g:`A` has semiperimeter "
            ":math:`s_A = x = s-a`! Consequently its scale factor is :math:`x/s`, its inradius is "
            ":math:`r_A = r(x/s)`, its area is :math:`K_A = K(x/s)^2`, and summing over all three corners gives "
            "the remarkable invariant :math:`r_A + r_B + r_C = r\\frac{x+y+z}{s} = r`.",
            "Second (`FWS 2014/9/7`, Folios 5–6), Seelig analyzes *CENTERS OF SIMILITUDE: EXCIRCLES*, treating "
            "vertex :g:`A` as the external :term:`center of similitude` of the incircle :math:`(I, r)` and the "
            ":math:`A`-excircle :math:`(I_A, R_A)` separated by :math:`d = |II_A|`, deriving "
            ":math:`|AI| = d\\frac{r}{R_A - r}` and :math:`|AI_A| = d\\frac{R_A}{R_A - r}`. Third (Folios 7–9), "
            "he solves :term:`Stewart's theorem` as a quadratic in :math:`k` for a prescribed cevian length "
            ":math:`d = 4` in :math:`(a,b,c) = (7,5,10)`, finding the two roots :math:`k \\in \\{0.613, 0.147\\}` "
            "above the altitude minimum :math:`d_{\\min} = h_c = 3.25`.",
        ],
        "equations": [
            r"s_A = x = s - a, \qquad r_A = r\frac{x}{s}, \qquad K_A = K\left(\frac{x}{s}\right)^2, \qquad r_A + r_B + r_C = r\frac{x + y + z}{s} = r",
            r"|AI| = |II_A|\frac{r}{r_a - r}, \qquad |AI_A| = |II_A|\frac{r_a}{r_a - r}, \qquad c^2 k^2 - (c^2 + a^2 - b^2) k + (a^2 - d^2) = 0",
        ],
        "depends_on": ["F.5", "F.14", "F.29", "F.46"],
        "euclid_refs": ["IV.4", "VI.4"],
        "elements_refs": ["G.5", "G.8"],
        "etc_refs": ["X(1)", "X(55)", "X(56)"],
        "spreadsheets": [
            "Centers of Similitude",
            "Incircle-Incenter",
            "Stewart's Theorem",
        ],
        "folio_summaries": [
            (
                "Corner Subtriangles Tangent to the Incircle — Semiperimeter s_A = x (001)",
                "Proves by equal tangent segments that the corner subtriangle cut off at vertex :math:`A` by a tangent to the incircle parallel to :math:`BC` has semiperimeter :math:`s_A = s - a = x`.",
            ),
            (
                "Inradii Sum Identity r_A + r_B + r_C = r (002)",
                "Uses homothety ratio :math:`x/s` to derive :math:`r_A = r(x/s), K_A = K(x/s)^2`, and :math:`r_A + r_B + r_C = r(x+y+z)/s = r`.",
            ),
            (
                "Infinite Chain of Tangential Corner Incircles (003)",
                "Sums the geometric series of nested incircles marching into vertex :math:`A` with ratio :math:`\\rho_A = (1 - \\sin(\\alpha/2))/(1 + \\sin(\\alpha/2))`.",
            ),
            (
                "Numerical Evaluation on the (5, 6, 7) Triangle (004)",
                "Evaluates :math:`x/s = 4/9, y/s = 3/9, z/s = 2/9` and checks :math:`r_A + r_B + r_C = r` and :math:`K_A + K_B + K_C = \\frac{29}{81}K`.",
            ),
            (
                "Centers of Similitude: Excircles — Part 1 (005, FWS 2014/9/7)",
                "Models vertex :math:`A` and the internal/external touchpoint harmonic conjugates along line :math:`AI I_A` for the incircle and :math:`A`-excircle.",
            ),
            (
                "Centers of Similitude: Excircles — Part 2 (006)",
                "Derives :math:`|AI| = d\\frac{r}{R-r}` and :math:`|AI_A| = d\\frac{R}{R-r}` (where :math:`R = r_a` is the exradius and :math:`d = |II_A|`).",
            ),
            (
                "Inverse Stewart Problem: Finding k for Given Cevian Length d (007)",
                "Rearranges Stewart's theorem into the quadratic :math:`c^2 k^2 - (c^2+a^2-b^2)k + (a^2-d^2) = 0`.",
            ),
            (
                "Worked Quadratic Example (a, b, c, d) = (7, 5, 10, 4) (008)",
                "Solves for the two base division ratios :math:`k = 0.613` and :math:`k = 0.147` at which a cevian of length :math:`d=4` meets base :math:`c=10`.",
            ),
            (
                "Discriminant & Minimum Cevian Length d_min = h_c (009)",
                "Shows that the quadratic discriminant vanishes precisely when :math:`d = d_{\\min} = h_c \\approx 3.25` (the perpendicular altitude).",
            ),
        ],
    },
    {
        "num": 49,
        "id": "F.49",
        "slug": "vesica-pisces",
        "legacy_folder": "49.vesica-pisces",
        "title": "Vesica Piscis and Acute-Obtuse Probability",
        "subtitle": "Locus of Longest-Side Triangles, Semicircle Partition, and Exact Area Ratio 3 pi / (5 pi - 6 sqrt(3))",
        "category": "Polygons, Tessellations & Special Triangles",
        "tags": [
            "vesica-piscis",
            "euclid",
            "acute",
            "obtuse",
            "monte-carlo",
            "probability",
        ],
        "enunciation": (
            "When segment AB of length c is the longest side of triangle ABC, vertex C lies inside "
            "the vesica piscis of area c^2 (4 pi - 3 sqrt(3))/6; the semicircle of diameter AB "
            "partitions each quadrant of area c^2 (4 pi - 3 sqrt(3))/24 into an obtuse region "
            "(O) = c^2 pi / 16 and an acute region (A) = c^2 (5 pi - 6 sqrt(3))/48, giving an "
            "exact obtuse-to-acute probability ratio (O)/(A) = 3 pi / (5 pi - 6 sqrt(3)) approx 1.773."
        ),
        "signature_given": ["A : Point", "B : Point"],
        "signature_steps": [
            "c_left = circle(A, B)",
            "c_right = circle(B, A)",
            "C = intersection(c_left, c_right)",
            "M = midpoint(A, B)",
            "c_semi = circle(M, A)",
        ],
        "synthesis": [
            "Titled *Notes on the locus of points C such that c = |AB| is the longest side* "
            "(:cite:`SeeligNotebooks`), this three-folio jewel connects :person:`Euclid`'s Opening Proposition "
            ":ref:`I.1` (the :term:`vesica piscis` formed by :g:`c_left` and :g:`c_right` of radius :math:`c`) "
            "with :ref:`III.31` (:person:`Thales`'s semicircle :g:`c_semi` on diameter :g:`A` :g:`B` of radius "
            ":math:`c/2`). Because :math:`|AC| \\le c` and :math:`|BC| \\le c`, any triangle with longest side "
            ":math:`c` has vertex :g:`C` inside the vesica piscis; by fourfold symmetry, Seelig analyzes a "
            "single upper-half quadrant of total area :math:`(O) + (A) = c^2\\left(\\frac{\\pi}{6} - \\frac{\\sqrt{3}}{8}\\right)`.",
            "Inside the Thales quarter-disk of radius :math:`c/2`, the angle at :g:`C` is obtuse (:math:`\\gamma > 90^\\circ`), "
            "giving obtuse area :math:`(O) = \\frac{1}{4}\\pi(c/2)^2 = c^2\\frac{\\pi}{16}`. Subtracting :math:`(O)` "
            "from the quarter-vesica leaves the acute region :math:`(A) = c^2\\frac{5\\pi - 6\\sqrt{3}}{48}`. "
            "Dividing the two yields the exact geometric probability ratio "
            ":math:`\\frac{(O)}{(A)} = \\frac{3\\pi}{5\\pi - 6\\sqrt{3}} \\approx 1.7731` (63.94% obtuse vs. "
            "36.06% acute)—confirming why random triangles in the ``Monte Carlo`` spreadsheet are predominantly obtuse!",
        ],
        "equations": [
            r"(O) + (A) = c^2\left(\frac{\pi}{6} - \frac{\sqrt{3}}{8}\right) = c^2\frac{4\pi - 3\sqrt{3}}{24}, \qquad (O) = \frac{1}{4}\pi\left(\frac{c}{2}\right)^2 = c^2\frac{\pi}{16}",
            r"(A) = c^2\frac{5\pi - 6\sqrt{3}}{48}, \qquad \frac{(O)}{(A)} = \frac{3\pi}{5\pi - 6\sqrt{3}} \approx 1.7731",
        ],
        "depends_on": ["F.18", "F.35", "F.41"],
        "euclid_refs": ["I.1", "III.31"],
        "elements_refs": ["G.1", "G.7"],
        "etc_refs": [],
        "spreadsheets": ["Monte Carlo", "General Reference"],
        "folio_summaries": [
            (
                "Locus of Longest-Side Triangles in the Vesica Piscis (001)",
                "Identifies the region where :math:`|AC| \\le c` and :math:`|BC| \\le c` with the vesica piscis on :math:`AB` and computes the quarter-vesica area :math:`c^2\\frac{4\\pi-3\\sqrt{3}}{24}`.",
            ),
            (
                "Thales Semicircle Partition into Obtuse (O) & Acute (A) Regions (002)",
                "Uses the semicircle of radius :math:`c/2` on diameter :math:`AB` to separate obtuse triangles :math:`(O) = c^2\\pi/16` from acute triangles :math:`(A) = c^2\\frac{5\\pi-6\\sqrt{3}}{48}`.",
            ),
            (
                "Exact Obtuse-to-Acute Probability Ratio (003)",
                "Evaluates :math:`(O)/(A) = \\frac{3\\pi}{5\\pi-6\\sqrt{3}} \\approx 1.773` and compares with the empirical counts in the Monte Carlo spreadsheet.",
            ),
        ],
    },
    {
        "num": 50,
        "id": "F.50",
        "slug": "altitudes",
        "legacy_folder": "50.altitudes",
        "title": "Altitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem",
        "subtitle": "The Sweet Theorem (h = ab/c), Reciprocal Altitude Area Formula, and Six Orthocenter Identities",
        "category": "Triangle Centers & Classical Circles",
        "tags": ["altitude", "orthocenter", "heron", "symphonic", "conway"],
        "enunciation": (
            "Given the three altitudes h_A, h_B, h_C of triangle ABC with reciprocal semiperimeter "
            "H = (h_A^{-1} + h_B^{-1} + h_C^{-1})/2, Mitchell's reciprocal Heron formula states "
            "K^{-1} = 4 sqrt(H (H - h_A^{-1})(H - h_B^{-1})(H - h_C^{-1})), and a triangle is "
            "right-angled at C if and only if h_A^{-2} + h_B^{-2} = h_C^{-2} (the Symphonic Theorem)."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "H_A = foot(A, line(B, C))",
            "H_B = foot(B, line(C, A))",
            "H_C = foot(C, line(A, B))",
            "h_a = segment(A, H_A)",
            "h_b = segment(B, H_B)",
            "h_c = segment(C, H_C)",
            "H = intersection(line(A, H_A), line(B, H_B))",
        ],
        "synthesis": [
            "Across four folios (:cite:`SeeligNotebooks`), Seelig synthesizes the metric laws of the "
            "three :term:`altitude` segments :g:`h_a`, :g:`h_b`, :g:`h_c`. Folio 1 (*Altitude of a Right "
            "Triangle (the sweet theorem)*) derives :math:`h = ab/c` and the Inverse Pythagorean Theorem "
            ":math:`h^{-2} = a^{-2} + b^{-2}`. Folios 2–3 record :person:`Mitchell`'s (2005) reciprocal "
            ":term:`Heron's formula` (:cite:`Mitchell2005`): defining :math:`H = \\frac{1}{2}(h_A^{-1}+h_B^{-1}+h_C^{-1})`, "
            "the reciprocal area is :math:`K^{-1} = 4\\sqrt{H(H-h_A^{-1})(H-h_B^{-1})(H-h_C^{-1})}`, which "
            "immediately recovers each side via :math:`a = 2K/h_A`. Seelig also names the *Symphonic Theorem*: "
            "since :math:`h_A = b, h_B = a, h_C = ab/c` in a right triangle, the three altitudes satisfy "
            ":math:`h_A^{-2} + h_B^{-2} = h_C^{-2}`.",
            "Folio 4 compiles six classical :term:`orthocenter` identities in :term:`Conway triangle notation`, "
            "including the sum of upper altitude segments :math:`t_A + t_B + t_C = |AH| + |BH| + |CH| = 2(r + R)` "
            "and the altitude-chord product :math:`|AH|\\cdot|HH_A| = |BH|\\cdot|HH_B| = |CH|\\cdot|HH_C|`.",
        ],
        "equations": [
            r"H = \frac{h_A^{-1} + h_B^{-1} + h_C^{-1}}{2}, \qquad \frac{1}{K} = 4\sqrt{H(H - h_A^{-1})(H - h_B^{-1})(H - h_C^{-1})}",
            r"\frac{1}{h_A^2} + \frac{1}{h_B^2} = \frac{1}{h_C^2} \quad (\gamma = 90^\circ), \qquad |AH| + |BH| + |CH| = 2(r + R)",
        ],
        "depends_on": ["F.3", "F.14", "F.34", "F.42"],
        "euclid_refs": ["I.12", "I.47", "VI.8"],
        "elements_refs": ["G.4", "G.11"],
        "etc_refs": ["X(1)", "X(3)", "X(4)"],
        "spreadsheets": ["Altitudes", "Orthocenter", "Right Triangle"],
        "folio_summaries": [
            (
                "Altitude of a Right Triangle — 'The Sweet Theorem' (altitude-right-001)",
                "Proves :math:`h = ab/c` and the Inverse Pythagorean Theorem :math:`h^{-2} = a^{-2} + b^{-2}`.",
            ),
            (
                "Mitchell's Reciprocal Heron Formula for Altitudes (altitudes-001)",
                "Cites Douglas W. Mitchell (2005) to express :math:`K^{-1} = 4\\sqrt{H(H-h_A^{-1})(H-h_B^{-1})(H-h_C^{-1})}` and reconstructs :math:`(a,b,c) = (2K/h_A, 2K/h_B, 2K/h_C)`.",
            ),
            (
                "The Symphonic Theorem & Altitude Ratios (altitudes-002)",
                "States the Symphonic Theorem :math:`h_A^{-2} + h_B^{-2} = h_C^{-2}` for right triangles and relates :math:`h_A : h_B : h_C = a^{-1} : b^{-1} : c^{-1}`.",
            ),
            (
                "Six Orthocenter Segment Identities in Conway Notation (altitudes-003)",
                "Records :math:`t_A + t_B + t_C = 2(r+R)` and five companion identities for the upper and lower orthocenter segments.",
            ),
        ],
    },
    {
        "num": 51,
        "id": "F.51",
        "slug": "apollonian-circles",
        "legacy_folder": "51.appolonian-circles",
        "title": "Apollonian Circles and the Problem of Apollonius",
        "subtitle": "Locus |PA|/|PB| = k, Integer Mean Triples, Power of a Point, and Dörrie's 8-Circle Tangency Table",
        "category": "Circle Inversion, Coaxial & Radical Systems",
        "tags": [
            "apollonius",
            "apollonian-circles",
            "harmonic",
            "inversion",
            "coaxial",
        ],
        "enunciation": (
            "The locus of points P with distance ratio |PA| / |PB| = k > 1 (where |AB| = d) is "
            "the Apollonian circle of radius R = d k / (k^2 - 1) centered at distance M' = d / (k^2 - 1) "
            "beyond B, cutting line AB at the internal and external harmonic conjugates C and D "
            "such that |A T'|^2 = |AC| |AD| = |AB| |A M'|."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "D = harmonic_conjugate(A, B, C)",
            "M_p = midpoint(C, D)",
            "c_apol = circle(M_p, C)",
        ],
        "synthesis": [
            "Dated February 7, 2014 (:cite:`SeeligNotebooks`), Seelig's nine-folio treatise on the "
            ":term:`Apollonian circles` combines the locus definition :math:`|PA|/|PB| = k` (Folios 1–8) with "
            "the classic *Problem of :person:`Apollonius`* (Folio 9, citing :person:`Dorrie`'s *100 Great "
            "Problems of Elementary Mathematics*, Problem #32, pp. 154–160, :cite:`Dorrie1965`). Given "
            ":math:`|AB| = d`, the internal and external bisectors of :math:`\\angle APB` meet :math:`AB` at "
            "the :term:`harmonic conjugate` points :g:`C` and :g:`D` (:person:`Euclid` *Elements* :ref:`VI.3`), "
            "giving diameter endpoints separated by :math:`2R = \\frac{2dk}{k^2-1}` and center :g:`M_p` at "
            ":math:`M' = \\frac{d}{k^2-1}` from :g:`B`.",
            "Across Folios 4–7, Seelig proves the power-of-a-point tangent identity "
            ":math:`|AT'|^2 = |AC|\\cdot|AD| = |AB|\\cdot|AM'|` and asks when two numbers :math:`m, n` yield "
            "simultaneous integer arithmetic, geometric, and harmonic means—finding the parametric solution "
            ":math:`m = 36, n = 324 \\implies A = 180, G = 108, H = 64.8` (or scaled by 5 for all integers). "
            "Folio 9 classifies all :math:`2^3 = 8` Apollonian tangent circles to three given circles by "
            "their internal (``I``) or external (``X``) tangency signatures.",
        ],
        "equations": [
            r"\frac{|PA|}{|PB|} = k \implies M' = \frac{d}{k^2 - 1}, \qquad R = \frac{d k}{k^2 - 1}, \qquad R^2 - {M'}^2 = \frac{d^2}{k^2 - 1}",
            r"|A T'|^2 = |AC|\cdot|AD| = |AB|\cdot|A M'| = d(d + M') = \frac{d^2 k^2}{k^2 - 1}",
        ],
        "depends_on": ["F.2", "F.10", "F.12", "F.25", "F.27"],
        "euclid_refs": ["III.36", "VI.3"],
        "elements_refs": ["G.5", "G.7"],
        "etc_refs": [],
        "spreadsheets": [
            "Apollonian Circles",
            "Harmonic Conjugates",
            "Coaxial Circles",
        ],
        "folio_summaries": [
            (
                "Apollonian Circle Center M' & Radius R (apollonian-001, FWS 2/7/2014)",
                "Derives :math:`|BC| = d/(k+1), |BD| = d/(k-1), M' = d/(k^2-1)`, and :math:`R = dk/(k^2-1)` for the locus :math:`|PA|/|PB| = k`.",
            ),
            (
                "Cartesian Equation Completion of the Square (apollonian-002)",
                "Expands :math:`(x+d)^2 + y^2 = k^2(x^2+y^2)` and completes the square to confirm center :math:`(d/(k^2-1), 0)` and radius :math:`dk/(k^2-1)`.",
            ),
            (
                "Angle Bisector Proof via Euclid VI.3 (apollonian-003)",
                "Shows that the internal and external bisectors of :math:`\\angle APB` meet :math:`AB` at fixed harmonic points :math:`C, D` with :math:`\\angle CPD = 90^\\circ`.",
            ),
            (
                "Power of Point A & Tangent Length |AT'| (apollonian-004)",
                "Proves :math:`|AT'|^2 = |AC|\\cdot|AD| = |AB|\\cdot|AM'|` for the tangent :math:`AT'` from :math:`A` to the Apollonian circle.",
            ),
            (
                "Orthogonal Circle of Inversion Centered at A or B (apollonian-005)",
                "Shows that the circle centered at :math:`A` of radius :math:`|AT'| = dk/\\sqrt{k^2-1}` is orthogonal to the Apollonian circle.",
            ),
            (
                "Arithmetic, Geometric & Harmonic Means on Segment AD (apollonian-006)",
                "Identifies :math:`|AB|, |AC|, |AD|, |AM'|` with the classical Pythagorean means.",
            ),
            (
                "Integer Mean Search: m = 36, n = 324 (apollonian-007)",
                "Solves for integer pairs :math:`(m,n)` having integer arithmetic mean :math:`A = 180` and geometric mean :math:`G = 108`.",
            ),
            (
                "Coaxial Family of Apollonian Circles for Varying k (apollonian-008)",
                "Plots the nested Apollonian circles around limiting points :math:`A` and :math:`B` with the perpendicular bisector as the :math:`k=1` radical axis.",
            ),
            (
                "Problem of Apollonius — Dörrie's 8-Circle I/X Tangency Table (apollonius-2-001)",
                "Cites Heinrich Dörrie (#32, pp. 154–160) and tabulates all 8 solution circles by their internal (``I``) and external (``X``) tangency states to three given circles.",
            ),
        ],
    },
    {
        "num": 52,
        "id": "F.52",
        "slug": "homogeneous-barycentric-coordinates",
        "legacy_folder": "52.homogeneous-barycentric-coordinates",
        "title": "Homogeneous Barycentric Coordinates",
        "subtitle": "Classical Center Catalog X(1)–X(8), Sidelength Polynomials for X(5), and 5-6-7 Evaluations",
        "category": "Algebraic & Coordinate Systems",
        "tags": [
            "barycentric",
            "triangle-centers",
            "etc",
            "nine-point-circle",
            "conway",
        ],
        "enunciation": (
            "Every triangle center X(n) has homogeneous barycentric coordinates (u : v : w) "
            "normalizable to absolute weights lambda_A + lambda_B + lambda_C = 1 such that "
            "X = lambda_A A + lambda_B B + lambda_C C; for the nine-point center N = X(5), "
            "lambda_A = 1/4 + (b^2 - c^2)(a^2 - (b^2 + c^2)) / (32 K^2)."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "G = centroid(A, B, C)",
            "I = incenter(A, B, C)",
            "O = circumcenter(A, B, C)",
            "H = orthocenter(A, B, C)",
            "N = midpoint(O, H)",
            "euler = line(O, H)",
        ],
        "synthesis": [
            "Spanning 15 folios (:cite:`SeeligNotebooks`), Seelig's master treatise on "
            ":term:`homogeneous barycentric coordinates` (HBC) bridges classical synthetic geometry, "
            ":person:`Kimberling`'s *Encyclopedia of Triangle Centers* (:cite:`KimberlingETC`), and "
            "programmable calculator/spreadsheet computation. Folios 1–6 (`bari-centers-001`–`006`) "
            "tabulate the unnormalized homogeneous coordinates :math:`(u:v:w)`, normalizing sums "
            ":math:`\\Sigma = u+v+w`, and exact numerical evaluations on the canonical :math:`(5,6,7)` "
            "triangle for eight fundamental centers: :term:`incenter` :g:`I` :math:`= X(1) = (a:b:c)`, "
            ":term:`centroid` :g:`G` :math:`= X(2) = (1:1:1)`, :term:`circumcenter` :g:`O` :math:`= X(3) = (a^2 S_A : b^2 S_B : c^2 S_C)`, "
            ":term:`orthocenter` :g:`H` :math:`= X(4) = (S_B S_C : S_C S_A : S_A S_B)`, nine-point center "
            ":g:`N` :math:`= X(5)`, :term:`symmedian point` :math:`K = X(6) = (a^2:b^2:c^2)`, "
            ":term:`Gergonne point` :math:`Ge = X(7)`, and :term:`Nagel point` :math:`Na = X(8) = (s-a:s-b:s-c)`.",
            "In Folios 7–15 (`homogenus-barycentric-co001`–`009`, dated `FWS 2014/9/14`), Seelig derives "
            "two explicit forms for the normalized barycentric coordinates of the nine-point center "
            ":g:`N` (:ref:`X(5)`): Form I (trigonometric, :math:`u = a\\cos(\\beta - \\gamma)`) and Form II "
            "(purely polynomial in the side lengths: :math:`\\lambda_A = W + \\frac{P^2/a^2 + a^4}{D}` with "
            ":math:`D = 4U - 2S_4 = 16K^2`), verifying Form II on the :math:`(3,4,5)` right triangle "
            ":math:`(\\frac{1}{4} : \\frac{1}{4} : \\frac{1}{2})`, the :math:`(5,6,7)` acute triangle "
            ":math:`(0.28299 : 0.30208 : 0.41493)`, and a compass drawing of the :math:`(7,8,9)` nine-point "
            "circle (:math:`R_N = \\frac{21}{20}\\sqrt{5}`).",
        ],
        "equations": [
            r"P = \lambda_A A + \lambda_B B + \lambda_C C \qquad (\lambda_A + \lambda_B + \lambda_C = 1), \qquad \lambda_A = \frac{u}{u + v + w} = \frac{[PBC]}{[ABC]}",
            r"X(1) = (a : b : c),\quad X(2) = (1 : 1 : 1),\quad X(3) = (a^2 S_A : b^2 S_B : c^2 S_C),\quad X(4) = (S_B S_C : S_C S_A : S_A S_B),\quad X(6) = (a^2 : b^2 : c^2)",
        ],
        "depends_on": ["F.6", "F.11", "F.14", "F.28", "F.34"],
        "euclid_refs": ["IV.4", "IV.5", "VI.1"],
        "elements_refs": ["G.7", "G.8"],
        "etc_refs": ["X(1)", "X(2)", "X(3)", "X(4)", "X(5)", "X(6)", "X(7)", "X(8)"],
        "spreadsheets": [
            "Barycentric",
            "Barycentric (2)",
            "9-Point Circle",
            "5-6-7 A,B,C",
        ],
        "folio_summaries": [
            (
                "Homogeneous Barycentric Coordinates — Area & Mass Interpretation (bari-centers-001)",
                "Defines :math:`\\lambda_A = [PBC]/[ABC], \\lambda_B = [PCA]/[ABC], \\lambda_C = [PAB]/[ABC]` with :math:`\\lambda_A + \\lambda_B + \\lambda_C = 1`.",
            ),
            (
                "Master Barycentric Catalog: X(1), X(2), X(3), X(4) (bari-centers-002)",
                "Tabulates algebraic and Conway-notation barycentric weights for the incenter :math:`I`, centroid :math:`G`, circumcenter :math:`O`, and orthocenter :math:`H`.",
            ),
            (
                "Master Barycentric Catalog: X(5), X(6), X(7), X(8) (bari-centers-003)",
                "Tabulates barycentric weights for the nine-point center :math:`N`, symmedian point :math:`K`, Gergonne point :math:`G_e`, and Nagel point :math:`N_a`.",
            ),
            (
                "Canonical (5, 6, 7) Barycentric Evaluation Table — Part 1 (bari-centers-004)",
                "Evaluates exact rational and decimal normalized barycentric coordinates of :math:`I, G, O, H` on the :math:`(5,6,7)` triangle.",
            ),
            (
                "Canonical (5, 6, 7) Barycentric Evaluation Table — Part 2 (bari-centers-005)",
                "Evaluates normalized barycentric and Cartesian coordinates of :math:`N, K, G_e, N_a` on the :math:`(5,6,7)` triangle.",
            ),
            (
                "Euler Line Barycentric Combinations (bari-centers-006)",
                "Verifies :math:`G = \\frac{2}{3}O + \\frac{1}{3}H` and :math:`N = \\frac{1}{2}O + \\frac{1}{2}H` directly on the normalized barycentric triples.",
            ),
            (
                "Nine-Point Center N = X(5) — Form I & Form II (co001, FWS 2014/9/14)",
                "States Form I (:math:`a\\cos(\\beta-\\gamma)`) and derives Form II (:math:`\\lambda_A = W + \\frac{P^2/a^2 + a^4}{D}` with :math:`D = 4U - 2S_4`) purely in terms of side lengths :math:`a, b, c`.",
            ),
            (
                "Algebraic Reduction of Form II (co002)",
                "Expands the symmetric polynomials :math:`P = abc, U = a^2b^2+b^2c^2+c^2a^2, S_4 = a^4+b^4+c^4` and proves :math:`\\lambda_A + \\lambda_B + \\lambda_C = 1`.",
            ),
            (
                "Verification of Form II on the (3, 4, 5) Right Triangle (co003)",
                "Evaluates Form II at :math:`(a,b,c) = (3,4,5)` to obtain :math:`(\\lambda_A, \\lambda_B, \\lambda_C) = (1/4, 1/4, 1/2)`.",
            ),
            (
                "Verification of Form II on the (5, 6, 7) Triangle (co004)",
                "Evaluates Form II at :math:`(a,b,c) = (5,6,7)` to obtain :math:`(\\lambda_A, \\lambda_B, \\lambda_C) = (163/576, 174/576, 239/576) \\approx (0.28299, 0.30208, 0.41493)`.",
            ),
            (
                "Nine-Point Circle of the (7, 8, 9) Triangle — Calculations (co005)",
                "Computes :math:`N, R = \\frac{21\\sqrt{5}}{10}`, and :math:`R_N = \\frac{21\\sqrt{5}}{20}` for the :math:`(7,8,9)` acute triangle.",
            ),
            (
                "Nine-Point Circle of the (7, 8, 9) Triangle — Compass Drawing (co006)",
                "Full-page geometric construction of :math:`\\triangle ABC` with sides :math:`(7,8,9)` and its nine-point circle :math:`\\Gamma_N` passing through all nine classical points.",
            ),
            (
                "Barycentric-to-Cartesian Matrix Transformation (co007)",
                "Writes the :math:`2\\times 3` affine conversion matrix mapping :math:`(\\lambda_A, \\lambda_B, \\lambda_C)` to :math:`(x, y)`.",
            ),
            (
                "Barycentric Distance & Cevian Trace Formulas (co008)",
                "Records the cevian trace ratios :math:`|BD|/|DC| = \\lambda_C/\\lambda_B` and the barycentric distance metric.",
            ),
            (
                "HP-35s & Spreadsheet Verification Case (co009)",
                "Cross-checks the barycentric coordinates and Cartesian outputs against the HP-35s triangle program.",
            ),
        ],
    },
    {
        "num": 53,
        "id": "F.53",
        "slug": "trig",
        "legacy_folder": "53.trig",
        "title": "Geometric Half-Angle Trigonometry",
        "subtitle": "Unit Semicircle Chord Proof of cos^2(theta/2) and sin^2(theta/2)",
        "category": "Algebraic & Coordinate Systems",
        "tags": ["trigonometry", "half-angle", "semicircle", "thales", "pythagoras"],
        "enunciation": (
            "In a unit semicircle of radius R = 1 and diameter AB = 2, a point P at central angle "
            "theta has altitude sin(theta), base projections 1 + cos(theta) and 1 - cos(theta), and "
            "chord |AP| = 2 cos(theta/2) = sqrt(2 + 2 cos(theta)), giving cos^2(theta/2) = (1 + cos(theta))/2 "
            "and sin^2(theta/2) = (1 - cos(theta))/2."
        ),
        "signature_given": ["O : Point", "A : Point", "P : Point"],
        "signature_steps": [
            "c_unit = circle(O, A)",
            "l_oa = line(O, A)",
            "B = intersection(l_oa, c_unit)",
            "H = foot(P, l_oa)",
            "s_ap = segment(A, P)",
            "s_bp = segment(B, P)",
        ],
        "synthesis": [
            "In this elegant single-folio geometric proof (:cite:`SeeligNotebooks`), Seelig derives the "
            "half-angle identities for :math:`\\cos^2(\\theta/2)` and :math:`\\sin^2(\\theta/2)` directly from "
            "a unit semicircle (:math:`R = 1`, diameter :math:`|AB| = 2`) without algebraic angle-addition "
            "expansion. Dropping the altitude :math:`|PH| = \\sin\\theta` from :g:`P` to diameter :g:`A` :g:`B` "
            "divides the diameter into :math:`|AH| = 1 + \\cos\\theta` and :math:`|HB| = 1 - \\cos\\theta`.",
            "By the inscribed angle theorem (:person:`Euclid` *Elements* :ref:`III.20`), the angle at :g:`A` is "
            ":math:`\\theta/2`, so the chord :g:`s_ap` has length :math:`2x = 2\\cos(\\theta/2)`. Applying the "
            "Pythagorean theorem (:ref:`I.47`) to right triangle :math:`\\triangle AHP` gives "
            ":math:`(2x)^2 = \\sin^2\\theta + (1 + \\cos\\theta)^2 = 2 + 2\\cos\\theta`, whence "
            ":math:`x^2 = \\cos^2\\frac{\\theta}{2} = \\frac{1}{2} + \\frac{1}{2}\\cos\\theta` and "
            ":math:`\\sin^2\\frac{\\theta}{2} = \\frac{1}{2} - \\frac{1}{2}\\cos\\theta`.",
        ],
        "equations": [
            r"(2 x)^2 = \sin^2\theta + (1 + \cos\theta)^2 = 2 + 2\cos\theta \implies \cos^2\frac{\theta}{2} = \frac{1 + \cos\theta}{2}",
            r"\sin^2\frac{\theta}{2} = 1 - \cos^2\frac{\theta}{2} = \frac{1 - \cos\theta}{2}, \qquad \tan\frac{\theta}{2} = \frac{\sin\theta}{1 + \cos\theta}",
        ],
        "depends_on": ["F.10"],
        "euclid_refs": ["I.47", "III.20", "III.31"],
        "elements_refs": ["G.7", "G.11"],
        "etc_refs": [],
        "spreadsheets": ["Trig Identities", "General Reference"],
        "folio_summaries": [
            (
                "Unit Semicircle Proof of Half-Angle Identities",
                "Constructs right triangle :math:`AHP` inside a unit semicircle (:math:`R=1, |AH|=1+\\cos\\theta, |PH|=\\sin\\theta, |AP|=2\\cos(\\theta/2)`) to prove :math:`\\cos^2(\\theta/2) = \\frac{1}{2}(1+\\cos\\theta)` and :math:`\\sin^2(\\theta/2) = \\frac{1}{2}(1-\\cos\\theta)`.",
            ),
        ],
    },
    {
        "num": 54,
        "id": "F.54",
        "slug": "scripts",
        "legacy_folder": "54.scripts",
        "title": "HP-35s Triangle Program and Coordinate Scripts",
        "subtitle": "BARY 2 CAR and CAR 2 BARY Matrix Routines, Register Map A–Z, and 5-6-7 Verification",
        "category": "Algebraic & Coordinate Systems",
        "tags": ["scripts", "hp-35s", "barycentric", "coordinates", "matrices"],
        "enunciation": (
            "In the canonical frame A = (0, 0), B = (M, 0), C = (I, J), the forward and inverse "
            "barycentric-Cartesian transformations BARY 2 CAR and CAR 2 BARY are given by "
            "P = M U + I V, Q = J V and V = Q / J, U = (P - I V) / M, T = 1 - (U + V)."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point", "P : Point"],
        "signature_steps": [
            "s_ab = segment(A, B)",
            "H_C = foot(C, line(A, B))",
            "H_P = foot(P, line(A, B))",
        ],
        "synthesis": [
            "Dated September 10, 2014 with ``LAST EDIT May 7, 2015`` (:cite:`SeeligNotebooks`), these two "
            "folios document Seelig's ``HP-35s [T] [Triangle]`` calculator program specification. Placing "
            ":g:`A` at :math:`(0,0)`, :g:`B` at :math:`(M,0)`, and :g:`C` at :math:`(I,J)`, the program "
            "maps normalized :term:`homogeneous barycentric coordinates` :math:`(T, U, V) = (\\lambda_A, \\lambda_B, \\lambda_C)` "
            "to Cartesian coordinates :math:`(P, Q) = (x, y)` via the upper-triangular routine ``BARY 2 CAR``: "
            ":math:`P = MU + IV, Q = JV`.",
            "Conversely, the inverse routine ``CAR 2 BARY`` recovers the barycentric weights in three "
            "register operations: :math:`V = Q/J`, :math:`U = (P - IV)/M`, and :math:`T = 1 - (U + V)`. "
            "Folio 2 records the complete ``A``–``Z`` memory register map of the HP-35s alongside a worked "
            "validation on the canonical :math:`(5,6,7)` triangle.",
        ],
        "equations": [
            r"\text{BARY 2 CAR:}\quad \begin{bmatrix} P \\ Q \end{bmatrix} = \begin{bmatrix} M & I \\ 0 & J \end{bmatrix} \begin{bmatrix} U \\ V \end{bmatrix}, \qquad T + U + V = 1",
            r"\text{CAR 2 BARY:}\quad V = \frac{Q}{J}, \qquad U = \frac{P - I V}{M}, \qquad T = 1 - (U + V)",
        ],
        "depends_on": ["F.47", "F.52"],
        "euclid_refs": ["VI.2"],
        "elements_refs": ["G.5"],
        "etc_refs": ["X(1)", "X(2)", "X(3)", "X(4)"],
        "spreadsheets": ["Barycentric", "5-6-7 A,B,C"],
        "folio_summaries": [
            (
                "HP-35s [T] [Triangle] Program Specification (FWS Sept. 10, 2014 / May 7, 2015)",
                "Defines the ``BARY 2 CAR`` (:math:`P = MU+IV, Q = JV`) and ``CAR 2 BARY`` (:math:`V = Q/J, U = (P-IV)/M, T = 1-(U+V)`) routines for :math:`A=(0,0), B=(M,0), C=(I,J)`.",
            ),
            (
                "HP-35s Register Map A–Z & (5, 6, 7) Test Case",
                "Documents the allocation of calculator registers ``A`` through ``Z`` and verifies the forward and inverse routines on the :math:`(5,6,7)` triangle.",
            ),
        ],
    },
    {
        "num": 55,
        "id": "F.55",
        "slug": "misc",
        "legacy_folder": "55.misc",
        "title": "Compass Constructions and Angle-to-Side Triangle Reconstruction",
        "subtitle": "Vesica-Square Drawings and Reconstructing (a, b, c) from Interior Angles Under Scale Normalization",
        "category": "Polygons, Tessellations & Special Triangles",
        "tags": [
            "constructions",
            "vesica-piscis",
            "inradius",
            "conway",
            "trigonometry",
        ],
        "enunciation": (
            "Given the three interior angles (alpha, beta, gamma) of a triangle normalized to "
            "unit area K = 1 (so s = 1/r), the Conway intouch segments x = s - a = r cot(alpha/2), "
            "y = s - b = r cot(beta/2), and z = s - c = r cot(gamma/2) determine the side lengths "
            "a = y + z, b = z + x, and c = x + y = 2 s - (a + b)."
        ),
        "signature_given": ["A : Point", "B : Point", "C : Point"],
        "signature_steps": [
            "I = incenter(A, B, C)",
            "T_A = foot(I, line(B, C))",
            "T_B = foot(I, line(C, A))",
            "T_C = foot(I, line(A, B))",
            "c_in = circle(I, T_A)",
        ],
        "synthesis": [
            "Closing the 55-topic archive (:cite:`SeeligNotebooks`), this five-folio folder pairs two pure "
            "compass-and-straightedge drawings (`drawings-001`–`002`, showing overlapping circles, a "
            ":term:`vesica piscis`, and an inscribed square with perpendicular axes) with a three-page analytic "
            "study (`misc-2-001`–`003`) on reconstructing a triangle's side lengths :math:`(a,b,c)` and vertex "
            "coordinates :math:`(A,B,C)` from its interior angles :math:`(\\alpha, \\beta, \\gamma)` under "
            "three alternative scale normalizations.",
            "Under the unit-area normalization :math:`K = r s = 1` (so :math:`s = 1/r`), Seelig expresses "
            "the :term:`Conway triangle notation` intouch segments via the half-angle cotangents "
            ":math:`x = s - a = r\\cot(\\alpha/2)`, :math:`y = s - b = r\\cot(\\beta/2)`, and "
            ":math:`z = s - c = r\\cot(\\gamma/2)`, recovering :math:`c = (s-a) + (s-b) = 2s - (a+b)` and "
            ":math:`r^2 = \\frac{1}{\\cot(\\alpha/2) + \\cot(\\beta/2) + \\cot(\\gamma/2)}`.",
        ],
        "equations": [
            r"s - a = r\cot\frac{\alpha}{2}, \qquad s - b = r\cot\frac{\beta}{2}, \qquad s - c = r\cot\frac{\gamma}{2}",
            r"K = r s = 1 \implies s = \frac{1}{r}, \qquad c = (s - a) + (s - b) = 2 s - (a + b)",
        ],
        "depends_on": ["F.14", "F.29", "F.49"],
        "euclid_refs": ["I.1", "IV.4"],
        "elements_refs": ["G.1", "G.8"],
        "etc_refs": ["X(1)", "X(7)"],
        "spreadsheets": ["General Reference", "Incircle-Incenter"],
        "folio_summaries": [
            (
                "Compass Construction — Vesica Piscis & Orthogonal Axes (drawings-001)",
                "Full-page compass and straightedge construction of a vesica piscis, perpendicular bisector, and inscribed circles.",
            ),
            (
                "Compass Construction — Inscribed Square & Diagonal Grid (drawings-002)",
                "Compass construction of a circle, orthogonal diameters, and inscribed square with auxiliary secant lines.",
            ),
            (
                "Reconstructing a Triangle from Angles (alpha, beta, gamma) — Assumption Sets (misc-2-001)",
                "Sets up the problem of determining :math:`(a,b,c)` and vertex coordinates :math:`(A,B,C)` from :math:`(\\alpha, \\beta, \\gamma)` under three scale normalizations (:math:`c=1`, :math:`R=1`, or :math:`K=1`).",
            ),
            (
                "Unit-Area Normalization K = 1 & Intouch Cotangents (misc-2-002)",
                "Uses :math:`K = rs = 1 \\implies s = 1/r` and :math:`s - a = r\\cot(\\alpha/2), s - b = r\\cot(\\beta/2)` to solve for :math:`r, s`, and :math:`(a,b,c)`.",
            ),
            (
                "Side Recovery c = 2s - (a + b) & Vertex Coordinates (misc-2-003)",
                "Recovers :math:`c = (s-a)+(s-b) = 2s-(a+b)` and writes the resulting Cartesian coordinates of :math:`A, B, C`.",
            ),
        ],
    },
]
