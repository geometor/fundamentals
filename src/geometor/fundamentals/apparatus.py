"""Scholarly apparatus registries and RST generators for GEOMETOR Fundamentals.

Maintains canonical definitions for geometric glossary terms, historical and
modern mathematicians (including Fred W. Seelig), and bibliographic references,
and compiles `resources/*.json` alongside `docsrc/glossary.rst`,
`docsrc/persons.rst`, and `docsrc/bibliography.rst`.
"""

from __future__ import annotations

import json
from pathlib import Path
import re

GLOSSARY_REGISTRY: dict[str, dict[str, object]] = {
    "Apollonian circles": {
        "definition": (
            "A family of circles defined as the locus of points whose distances "
            "from two fixed foci A and B have a constant ratio k, or the three "
            "circles of a triangle passing through a vertex and two isodynamic points."
        ),
        "aliases": [
            "Apollonian circle",
            "circle of Apollonius",
            "circles of Apollonius",
        ],
    },
    "barycentric coordinates": {
        "definition": (
            "Homogeneous coordinates (u : v : w) of a point P with respect to a "
            "reference triangle ABC, proportional to the signed areas of triangles "
            "PBC, PCA, and PAB."
        ),
        "aliases": [
            "barycentric",
            "homogeneous barycentric coordinates",
            "barycentrics",
        ],
    },
    "bilinear transformation": {
        "definition": (
            "A fractional linear or projective mapping of the form "
            "w = (az + b)/(cz + d) that preserves cross-ratios and maps circles "
            "and lines to circles and lines."
        ),
        "aliases": ["bilinear transformations", "Möbius transformation"],
    },
    "Carnot's theorem": {
        "definition": (
            "A theorem relating the signed distances from the circumcenter O to "
            "the sides of triangle ABC with the inradius r and circumradius R: "
            "d_a + d_b + d_c = R + r."
        ),
        "aliases": ["Carnot theorem"],
    },
    "centers of similitude": {
        "definition": (
            "The internal and external homothetic centers (:math:`S_+` and :math:`S_-`) of two "
            "circles, dividing the segment between their centers harmonically in "
            "the ratio of their radii."
        ),
        "aliases": ["center of similitude", "homothetic center", "similitude center"],
    },
    "centroid": {
        "definition": (
            "The point of concurrency G = X(2) of the three medians of a triangle, "
            "dividing each median in a 2:1 ratio with barycentric coordinates 1 : 1 : 1."
        ),
        "aliases": ["medians", "median"],
    },
    "Ceva's theorem": {
        "definition": (
            "A criterion for three cevians AD, BE, CF of triangle ABC to concur: "
            "(BD/DC)(CE/EA)(AF/FB) = 1."
        ),
        "aliases": ["cevian", "cevians"],
    },
    "circumcenter": {
        "definition": (
            "The center O = X(3) of the circumscribed circle of a triangle, "
            "located at the intersection of the perpendicular bisectors of the three sides."
        ),
        "aliases": ["circumcircle", "circumradius"],
    },
    "coaxial circles": {
        "definition": (
            "A one-parameter pencil of circles in which every pair shares the "
            "same radical axis; classified into intersecting (elliptic), "
            "non-intersecting (hyperbolic with limiting points), and tangent (parabolic) pencils."
        ),
        "aliases": ["coaxial system", "pencil of circles"],
    },
    "Conway triangle notation": {
        "definition": (
            "John H. Conway's algebraic system for triangle geometry setting "
            "S = 2K (twice the triangle area) and S_A = (b^2 + c^2 - a^2)/2 = bc cos A, "
            "S_B = (c^2 + a^2 - b^2)/2, S_C = (a^2 + b^2 - c^2)/2."
        ),
        "aliases": ["Conway notation", "Conway symbols"],
    },
    "cyclic quadrilateral": {
        "definition": (
            "A four-sided polygon inscribed in a single circle, satisfying "
            "opposite angle supplementary relations, Ptolemy's theorem, and "
            "Brahmagupta's area formula."
        ),
        "aliases": ["cyclic quad"],
    },
    "ellipse": {
        "definition": (
            "A conic section with eccentricity 0 <= e < 1 whose points have a "
            "constant sum of distances 2a from two fixed foci."
        ),
        "aliases": ["elliptical"],
    },
    "equilateral triangle": {
        "definition": (
            "A regular three-sided polygon with equal sides a = b = c and "
            "interior angles of 60 degrees, constructed in Euclid's Proposition I.1."
        ),
        "aliases": ["equilateral"],
    },
    "Euler line": {
        "definition": (
            "The line passing through a non-equilateral triangle's orthocenter H, "
            "nine-point center N, centroid G, and circumcenter O, with HG : GN : NO = 4 : 1 : 2."
        ),
        "aliases": [],
    },
    "excircle": {
        "definition": (
            "One of three circles tangent to one side of a triangle and the "
            "extensions of the other two sides, centered at an excenter I_a, I_b, or I_c."
        ),
        "aliases": ["excircles", "excenter", "excenters", "exradius", "extangent"],
    },
    "Fermat point": {
        "definition": (
            "The isogonic center F = X(13) minimizing the sum of distances "
            "PA + PB + PC to the vertices of a triangle with all angles < 120 degrees."
        ),
        "aliases": ["Torricelli point", "first Fermat point"],
    },
    "geometric mean": {
        "definition": (
            "The mean proporional sqrt(ab) between two positive lengths a and b, "
            "constructed as the altitude to the hypotenuse of a right triangle "
            "with segments a and b."
        ),
        "aliases": ["mean proportional"],
    },
    "golden ratio": {
        "definition": (
            "The extreme and mean ratio phi = (1 + sqrt(5))/2 ≈ 1.6180339887, "
            "satisfying phi^2 = phi + 1."
        ),
        "aliases": ["divine proportion", "golden section"],
    },
    "golden triangle": {
        "definition": (
            "An isosceles triangle whose side-to-base ratio is the golden ratio "
            "phi, having vertex angles of 36-72-72 degrees (acute) or 108-36-36 degrees (gnomon)."
        ),
        "aliases": ["golden triangles", "golden gnomon"],
    },
    "harmonic conjugate": {
        "definition": (
            "Given collinear points A, B, C, the point D is the harmonic conjugate "
            "of C with respect to (A, B) when the cross-ratio (A, B; C, D) = -1, "
            "so AC/CB = AD/BD."
        ),
        "aliases": ["harmonic conjugates", "harmonic range", "harmonic division"],
    },
    "harmonic mean": {
        "definition": (
            "The reciprocal of the arithmetic mean of reciprocals, H = 2ab/(a + b), "
            "realized geometrically by the segment separating harmonic conjugates."
        ),
        "aliases": [],
    },
    "Heron's formula": {
        "definition": (
            "The expression for the area K of a triangle in terms of its semiperimeter "
            "s = (a+b+c)/2: K = sqrt(s(s-a)(s-b)(s-c)), or in biquadratic side form "
            "16K^2 = 2a^2b^2 + 2b^2c^2 + 2c^2a^2 - a^4 - b^4 - c^4."
        ),
        "aliases": ["Heron formula"],
    },
    "incenter": {
        "definition": (
            "The center I = X(1) of the inscribed circle of a triangle, located "
            "at the concurrency of the three interior angle bisectors with "
            "barycentric coordinates a : b : c."
        ),
        "aliases": ["incircle", "inradius"],
    },
    "inversion": {
        "definition": (
            "A transformation with respect to a circle of center O and radius R "
            "mapping each point P to P' on ray OP such that OP * OP' = R^2."
        ),
        "aliases": ["inversive geometry", "circle inversion"],
    },
    "isosceles triangle": {
        "definition": (
            "A triangle with at least two equal sides and two equal base angles "
            "(Euclid I.5, Pons Asinorum)."
        ),
        "aliases": ["isosceles"],
    },
    "isotomic conjugate": {
        "definition": (
            "The point P' obtained by reflecting the cevian traces of P across "
            "the midpoints of the corresponding sides, with barycentric coordinates "
            "1/u : 1/v : 1/w."
        ),
        "aliases": ["isotomic"],
    },
    "Menelaus's theorem": {
        "definition": (
            "A collinearity criterion for three points D, E, F on the (extended) "
            "sides BC, CA, AB of triangle ABC: (BD/DC)(CE/EA)(AF/FB) = -1."
        ),
        "aliases": ["Menelaus theorem", "transversal"],
    },
    "nine-point circle": {
        "definition": (
            "Feuerbach's circle centered at N = X(5) of radius R/2 passing through "
            "the three side midpoints, the three altitude feet, and the three "
            "Euler midpoints between the vertices and the orthocenter."
        ),
        "aliases": ["Feuerbach circle", "nine-point center"],
    },
    "orthic triangle": {
        "definition": (
            "The pedal triangle H_A H_B H_C of the orthocenter H, formed by the "
            "feet of the three altitudes of triangle ABC; it minimizes perimeter "
            "among all inscribed triangles of an acute triangle (Fagnano's problem)."
        ),
        "aliases": [],
    },
    "orthocenter": {
        "definition": (
            "The concurrency H = X(4) of the three altitudes of a triangle, with "
            "barycentric coordinates tan A : tan B : tan C = 1/S_A : 1/S_B : 1/S_C."
        ),
        "aliases": ["altitude", "altitudes"],
    },
    "orthogonal circles": {
        "definition": (
            "Two circles that intersect at right angles, so that the radii to "
            "their intersection points are tangent to the other circle and "
            "d^2 = r_1^2 + r_2^2."
        ),
        "aliases": ["orthogonality"],
    },
    "parabola": {
        "definition": (
            "A conic section of eccentricity e = 1 defined as the locus of points "
            "equidistant from a focus F and a directrix line."
        ),
        "aliases": ["parabolas"],
    },
    "pedal triangle": {
        "definition": (
            "The triangle formed by the perpendicular projections of a point P "
            "onto the three sides of reference triangle ABC."
        ),
        "aliases": ["pedal triangles"],
    },
    "pole and polar": {
        "definition": (
            "A projective duality with respect to a conic or circle mapping a "
            "point P (the pole) to the line of harmonic conjugates or chord of "
            "contact (the polar)."
        ),
        "aliases": ["pole", "polar", "pole-polar"],
    },
    "power of a point": {
        "definition": (
            "For a point P and circle of center O and radius R, the invariant "
            "quantity Pi(P) = OP^2 - R^2 equal to the signed product PA * PB "
            "along any secant line through P."
        ),
        "aliases": ["chord intersection"],
    },
    "Pythagorean triple": {
        "definition": (
            "A tuple of positive integers (a, b, c) satisfying a^2 + b^2 = c^2, "
            "parametrized by Euclid's formula a = m^2 - n^2, b = 2mn, c = m^2 + n^2."
        ),
        "aliases": ["Pythagorean triples"],
    },
    "radical axis": {
        "definition": (
            "The locus of points having equal power with respect to two non-concentric "
            "circles, forming a line perpendicular to the line of centers."
        ),
        "aliases": ["radical axes", "radical center"],
    },
    "Stewart's theorem": {
        "definition": (
            "A theorem relating the length d of a cevian AD dividing side BC = a "
            "into segments m and n: b^2 m + c^2 n = a(d^2 + mn)."
        ),
        "aliases": ["Stewart theorem"],
    },
    "symmedian point": {
        "definition": (
            "The Lemoine point K = X(6), the concurrency of the reflections of "
            "the medians across the angle bisectors, with barycentric coordinates "
            "a^2 : b^2 : c^2."
        ),
        "aliases": ["symmedian", "Lemoine point"],
    },
    "trilinear coordinates": {
        "definition": (
            "Homogeneous coordinates (alpha : beta : gamma) proportional to the "
            "signed directed distances from a point P to the sidelines BC, CA, AB, "
            "related to barycentrics by (u : v : w) = (a*alpha : b*beta : c*gamma)."
        ),
        "aliases": ["trilinear", "trilinears"],
    },
    "vesica piscis": {
        "definition": (
            "The lens-shaped intersection of two congruent circles each passing "
            "through the other's center, fundamental to Euclid I.1 and Gothic "
            "pointed arch tracery with height-to-width ratio sqrt(3)."
        ),
        "aliases": ["vesica"],
    },
}

PERSONS_REGISTRY: dict[str, dict[str, str]] = {
    "seelig": {
        "name": "Fred W. Seelig",
        "dates": "20th–21st c.",
        "summary": (
            "Independent geometric researcher and compiler of the 55 notebooks "
            "and computational spreadsheets forming the GEOMETOR Fundamentals archive. "
            "His investigations bridge classical synthetic geometry, Conway triangle "
            "notation, homogeneous barycentric coordinates, and exact algebraic verification."
        ),
    },
    "euclid": {
        "name": "Euclid of Alexandria",
        "dates": "fl. 300 BCE",
        "summary": (
            "Greek mathematician and author of the *Elements*, whose compass-and-straightedge "
            "propositions underpin the constructive foundations of every topic in this codex."
        ),
    },
    "apollonius": {
        "name": "Apollonius of Perga",
        "dates": "c. 240–c. 190 BCE",
        "summary": (
            "Greek geometer known as 'The Great Geometer', author of *Conics* and "
            "discoverer of the Apollonian circles of constant distance ratio."
        ),
    },
    "pappus": {
        "name": "Pappus of Alexandria",
        "dates": "c. 290–c. 350 CE",
        "summary": (
            "Hellenistic mathematician whose *Synagoge* (*Collection*) preserved "
            "projective invariants, harmonic cross-ratios, and Stewart's theorem precursors."
        ),
    },
    "heron": {
        "name": "Heron of Alexandria",
        "dates": "c. 10–c. 70 CE",
        "summary": (
            "Greek mathematician and engineer who gave the classical proof of "
            "Heron's formula for the area of a triangle in terms of its side lengths."
        ),
    },
    "ptolemy": {
        "name": "Claudius Ptolemy",
        "dates": "c. 100–c. 170 CE",
        "summary": (
            "Alexandrian astronomer and mathematician whose *Almagest* established "
            "Ptolemy's theorem on the diagonals and sides of a cyclic quadrilateral."
        ),
    },
    "menelaus": {
        "name": "Menelaus of Alexandria",
        "dates": "c. 70–140 CE",
        "summary": (
            "Greek mathematician and astronomer who formulated Menelaus's theorem "
            "for collinearity on a triangle's sidelines."
        ),
    },
    "ceva": {
        "name": "Giovanni Ceva",
        "dates": "1647–1734",
        "summary": (
            "Italian mathematician who published *De lineis rectis* (1678), "
            "establishing Ceva's theorem for concurrent cevians in a triangle."
        ),
    },
    "stewart": {
        "name": "Matthew Stewart",
        "dates": "1717–1785",
        "summary": (
            "Scottish mathematician who published Stewart's theorem in *Some General "
            "Theorems of Considerable Use in the Higher Parts of Mathematics* (1746)."
        ),
    },
    "carnot": {
        "name": "Lazare Carnot",
        "dates": "1753–1823",
        "summary": (
            "French mathematician and engineer whose *Géométrie de position* (1803) "
            "introduced signed geometric quantities and Carnot's theorem."
        ),
    },
    "euler": {
        "name": "Leonhard Euler",
        "dates": "1707–1783",
        "summary": (
            "Swiss mathematician who proved the collinearity of the orthocenter, "
            "centroid, nine-point center, and circumcenter (the Euler line) and "
            "the distance formula d^2 = R(R - 2r) between incenter and circumcenter."
        ),
    },
    "feuerbach": {
        "name": "Karl Wilhelm Feuerbach",
        "dates": "1800–1834",
        "summary": (
            "German geometer who proved in 1822 that the nine-point circle is "
            "internally tangent to the incircle and externally tangent to the three excircles."
        ),
    },
    "poncelet": {
        "name": "Jean-Victor Poncelet",
        "dates": "1788–1867",
        "summary": (
            "French mathematician and founder of modern projective geometry, "
            "developing pole-polar duality, harmonic ranges, and coaxial pencils."
        ),
    },
    "steiner": {
        "name": "Jakob Steiner",
        "dates": "1796–1863",
        "summary": (
            "Swiss geometer who systematized the power of a point, radical axes, "
            "and synthetic projective constructions."
        ),
    },
    "fermat": {
        "name": "Pierre de Fermat",
        "dates": "1607–1665",
        "summary": (
            "French mathematician who posed the problem of finding the point "
            "minimizing the sum of distances to the three vertices of a triangle."
        ),
    },
    "dalembert": {
        "name": "Jean le Rond d'Alembert",
        "dates": "1717–1783",
        "summary": (
            "French mathematician and physicist associated with d'Alembert's "
            "theorem on the collinearity of external and internal centers of "
            "similitude of three circles (Monge–d'Alembert theorem)."
        ),
    },
    "conway": {
        "name": "John Horton Conway",
        "dates": "1937–2020",
        "summary": (
            "English mathematician who introduced Conway triangle notation "
            "(S, S_A, S_B, S_C, S_omega), extensively adopted by Fred Seelig "
            "throughout his notebooks."
        ),
    },
    "kimberling": {
        "name": "Clark Kimberling",
        "dates": "b. 1942",
        "summary": (
            "American mathematician and creator of the *Encyclopedia of Triangle "
            "Centers* (ETC), whose X(n) indexing links directly to Seelig's triangle studies."
        ),
    },
    "yiu": {
        "name": "Paul Yiu",
        "dates": "Contemporary",
        "summary": (
            "Mathematician and author of *Introduction to the Geometry of the Triangle*, "
            "a primary reference in Fred Seelig's notes on homogeneous barycentric coordinates."
        ),
    },
    "coxeter": {
        "name": "H. S. M. Coxeter",
        "dates": "1907–2003",
        "summary": (
            "Geometer and co-author of *Geometry Revisited*, frequently cited in "
            "the notebooks for coaxial circles, inversion, and projective geometry."
        ),
    },
    "altshiller_court": {
        "name": "Nathan Altshiller-Court",
        "dates": "1881–1968",
        "summary": (
            "Author of *College Geometry: An Introduction to the Modern Geometry "
            "of the Triangle and the Circle*, heavily referenced in Seelig's "
            "harmonic and similitude derivations."
        ),
    },
    "markowski": {
        "name": "George Markowski",
        "dates": "Contemporary",
        "summary": (
            "Mathematician examined in Seelig's Topic 32 notebook for the circumcircle "
            "midpoint-sagitta theorem J*K*L = (1/2)*r^2*R = (R^2 - d_IO^2)^2 / (8R)."
        ),
    },
    "ogilvy": {
        "name": "C. Stanley Ogilvy",
        "dates": "1913–2000",
        "summary": (
            "American mathematician and author of *Excursions in Geometry* (1969), "
            "frequently cited by Fred Seelig for coaxial circles, harmonic division, "
            "and orthogonal circle inversion."
        ),
    },
    "torricelli": {
        "name": "Evangelista Torricelli",
        "dates": "1608–1647",
        "summary": (
            "Italian physicist and mathematician who gave the classical equilateral-triangle "
            "circumcircle construction for the Fermat–Torricelli point X(13)."
        ),
    },
    "fagnano": {
        "name": "Giovanni Francesco Fagnano",
        "dates": "1715–1797",
        "summary": (
            "Italian mathematician who proved in 1775 that the orthic triangle "
            "minimizes perimeter among all triangles inscribed in an acute triangle."
        ),
    },
    "newton": {
        "name": "Isaac Newton",
        "dates": "1642–1727",
        "summary": (
            "English mathematician and physicist whose *Universal Arithmetick* "
            "established algebraic triangle relations such as c = s - K/s for right triangles."
        ),
    },
    "dorrie": {
        "name": "Heinrich Dörrie",
        "dates": "1873–1955",
        "summary": (
            "German mathematician and author of *100 Great Problems of Elementary "
            "Mathematics*, cited by Seelig in his study of the Problem of Apollonius."
        ),
    },
}

CITATIONS_REGISTRY: dict[str, dict[str, str]] = {
    "SeeligNotebooks": {
        "text": (
            "Seelig, Fred W. *Geometrical Notebooks: 55 Studies in Constructive, "
            "Projective, and Algebraic Triangle Geometry* (353 manuscript folios, "
            "2011–2015). GEOMETOR Fundamentals Archive."
        ),
    },
    "SeeligSpreadsheets": {
        "text": (
            "Seelig, Fred W. *Triangles and Circles* (OpenDocument Workbook, "
            "59 worksheets) and *Circumcircle-Circumcenter* studies. "
            "GEOMETOR Fundamentals Archive."
        ),
    },
    "EuclidElements": {
        "text": (
            "Euclid. *The Thirteen Books of Euclid's Elements*, translated with "
            "introduction and commentary by Sir Thomas L. Heath, 2nd ed. "
            "Cambridge University Press, 1926 (Dover reprint, 1956)."
        ),
    },
    "Ogilvy1969": {
        "text": (
            "Ogilvy, C. Stanley. *Excursions in Geometry*. Oxford University Press, "
            "1969 (Dover reprint, 1990)."
        ),
    },
    "Dorrie1965": {
        "text": (
            "Dörrie, Heinrich. *100 Great Problems of Elementary Mathematics: "
            "Their History and Solution*. Dover Publications, 1965 (Problem #32, "
            "Circles of Apollonius, pp. 154–160)."
        ),
    },
    "Mitchell2005": {
        "text": (
            "Mitchell, Douglas W. 'A Heron-Type Formula for the Reciprocal Area "
            "of a Triangle.' *The Mathematical Gazette* 89 (Nov. 2005): 494."
        ),
    },
    "BaloglouHelfgott2008": {
        "text": (
            "Baloglou, George, and Michel Helfgott. 'Angles, Area, and Perimeter "
            "Caught in a Cubic.' *Forum Geometricorum* 8 (2008): 13–25."
        ),
    },
    "Wells1991": {
        "text": (
            "Wells, David. *The Penguin Dictionary of Curious and Interesting "
            "Geometry*. Penguin Books, 1991 (p. 75)."
        ),
    },
    "AbramowitzStegun1964": {
        "text": (
            "Abramowitz, Milton, and Irene A. Stegun, eds. *Handbook of "
            "Mathematical Functions with Formulas, Graphs, and Mathematical Tables*. "
            "NBS Applied Mathematics Series 55, 1964 (p. 299)."
        ),
    },
    "Yiu2001": {
        "text": (
            "Yiu, Paul. *Introduction to the Geometry of the Triangle*. "
            "Department of Mathematics, Florida Atlantic University, 2001 (rev. 2013)."
        ),
    },
    "AltshillerCourt2007": {
        "text": (
            "Altshiller-Court, Nathan. *College Geometry: An Introduction to the "
            "Modern Geometry of the Triangle and the Circle*, 2nd ed. "
            "Barnes & Noble, 1952 (Dover reprint, 2007)."
        ),
    },
    "CoxeterGreitzer1967": {
        "text": (
            "Coxeter, H. S. M., and S. L. Greitzer. *Geometry Revisited*. "
            "Mathematical Association of America, New Mathematical Library #19, 1967."
        ),
    },
    "Johnson1929": {
        "text": (
            "Johnson, Roger A. *Modern Geometry: An Elementary Treatise on the "
            "Geometry of the Triangle and the Circle*. Houghton Mifflin, 1929 "
            "(Dover reprint as *Advanced Euclidean Geometry*, 1960)."
        ),
    },
    "Kimberling1998": {
        "text": (
            "Kimberling, Clark. 'Triangle Centers and Central Triangles.' "
            "*Congressus Numerantium* 129 (1998): 1–295; and *Encyclopedia of "
            "Triangle Centers (ETC)*."
        ),
    },
    "Posamentier2002": {
        "text": (
            "Posamentier, Alfred S. *Advanced Euclidean Geometry: Excursions for "
            "Students and Teachers*. Key College Publishing, 2002."
        ),
    },
}


def export_apparatus_json(resources_dir: Path) -> None:
    """Write `glossary.json`, `persons.json`, and `citations.json` into `resources_dir`.

    Args:
        resources_dir: Target `resources/` directory path.
    """
    resources_dir.mkdir(parents=True, exist_ok=True)
    (resources_dir / "glossary.json").write_text(
        json.dumps(
            dict(sorted(GLOSSARY_REGISTRY.items())), indent=2, ensure_ascii=False
        )
        + "\n",
        encoding="utf-8",
    )
    (resources_dir / "persons.json").write_text(
        json.dumps(dict(sorted(PERSONS_REGISTRY.items())), indent=2, ensure_ascii=False)
        + "\n",
        encoding="utf-8",
    )
    (resources_dir / "citations.json").write_text(
        json.dumps(
            dict(sorted(CITATIONS_REGISTRY.items())), indent=2, ensure_ascii=False
        )
        + "\n",
        encoding="utf-8",
    )


def generate_apparatus_rst(docsrc_dir: Path) -> None:
    """Generate `docsrc/glossary.rst`, `docsrc/persons.rst`, and `docsrc/bibliography.rst`.

    Args:
        docsrc_dir: Path to `docsrc/`.
    """
    docsrc_dir.mkdir(parents=True, exist_ok=True)

    # 1. glossary.rst
    g_lines: list[str] = [
        ":navigation: header",
        ":order: 30",
        "",
        ".. _glossary:",
        "",
        "========",
        "Glossary",
        "========",
        "",
        "Canonical geometric definitions and concepts referenced across the 55",
        "topics of the Fundamentals codex.",
        "",
        ".. glossary::",
        "   :sorted:",
        "",
    ]
    for term, data in sorted(GLOSSARY_REGISTRY.items(), key=lambda kv: kv[0].lower()):
        g_lines.append(f"   {term}")
        for alias in data.get("aliases", []):  # type: ignore[union-attr]
            g_lines.append(f"   {alias}")
        defn = str(data.get("definition", ""))
        g_lines.append(f"      {defn}")
        g_lines.append("")

    etc_centers: list[tuple[int, str, str]] = [
        (
            1,
            "Incenter",
            "Concurrency of the three interior angle bisectors; barycentrics a : b : c.",
        ),
        (2, "Centroid", "Concurrency of the three medians; barycentrics 1 : 1 : 1."),
        (
            3,
            "Circumcenter",
            "Concurrency of the three perpendicular bisectors; barycentrics a^2 S_A : b^2 S_B : c^2 S_C.",
        ),
        (
            4,
            "Orthocenter",
            "Concurrency of the three altitudes; barycentrics S_B S_C : S_C S_A : S_A S_B.",
        ),
        (
            5,
            "Nine-Point Center",
            "Midpoint of O and H on the Euler line; center of Feuerbach's nine-point circle.",
        ),
        (
            6,
            "Symmedian (Lemoine) Point",
            "Isogonal conjugate of the centroid G; barycentrics a^2 : b^2 : c^2.",
        ),
        (
            7,
            "Gergonne Point",
            "Concurrency of cevians to the incircle contact points T_A, T_B, T_C.",
        ),
        (
            8,
            "Nagel Point",
            "Concurrency of cevians to the excircle touchpoints; isotomic conjugate of X(7).",
        ),
        (
            9,
            "Mittenpunkt",
            "Symmedian point of the excentral triangle; perspector of the excentral and medial triangles.",
        ),
        (
            11,
            "Feuerbach Point",
            "Point of internal tangency between the incircle and the nine-point circle.",
        ),
        (
            13,
            "First Fermat (Torricelli) Point",
            "First isogonic center minimizing :math:`|PA| + |PB| + |PC|` for angles < 120 degrees.",
        ),
        (
            14,
            "Second Fermat Point",
            "Second isogonic center constructed via inwardly directed equilateral triangles.",
        ),
        (
            15,
            "First Isodynamic Point",
            "Isogonal conjugate of X(13); common intersection of the three Apollonian circles.",
        ),
        (
            16,
            "Second Isodynamic Point",
            "Isogonal conjugate of X(14); second common intersection of the three Apollonian circles.",
        ),
        (
            20,
            "De Longchamps Point",
            "Reflection of the orthocenter H across the circumcenter O on the Euler line.",
        ),
        (
            26,
            "Circumcenter of the Tangential Triangle",
            "Center of the circle circumscribing the tangential triangle.",
        ),
        (
            40,
            "Bevan Point",
            "Circumcenter of the excentral triangle I_A I_B I_C; reflection of I across O.",
        ),
        (
            55,
            "Internal Center of Similitude of Incircle and Circumcircle",
            "Insimilicenter dividing segment OI internally in ratio R : r.",
        ),
        (
            56,
            "External Center of Similitude of Incircle and Circumcircle",
            "Exsimilicenter dividing segment OI externally in ratio R : -r.",
        ),
    ]
    g_lines.extend(
        [
            "Kimberling Triangle Centers (ETC Index)",
            "---------------------------------------",
            "",
        ]
    )
    for xnum, xname, xdesc in etc_centers:
        x_label = f"X({xnum})"
        etc_url = f"https://geometor.github.io/etc/centers/x-{xnum:04d}/"
        g_lines.extend(
            [
                f".. _{x_label}:",
                "",
                f"{x_label} — {xname}",
                "~" * len(f"{x_label} — {xname}"),
                "",
                f"{xdesc} (`GEOMETOR ETC {x_label} <{etc_url}>`__).",
                "",
            ]
        )
    (docsrc_dir / "glossary.rst").write_text("\n".join(g_lines), encoding="utf-8")

    # 2. persons.rst
    p_lines: list[str] = [
        ":navigation: header",
        ":order: 40",
        "",
        ".. _persons:",
        "",
        "=======",
        "Persons",
        "=======",
        "",
        "Mathematicians, geometers, and researchers referenced in the",
        ":person:`seelig` archive and synthetic derivations.",
        "",
    ]
    for pid, pdata in sorted(
        PERSONS_REGISTRY.items(), key=lambda kv: kv[1]["name"].split()[-1].lower()
    ):
        header = f"{pdata['name']} ({pdata['dates']})"
        p_lines.extend(
            [
                f".. _person-{pid}:",
                f".. _{pid}:",
                "",
                header,
                "-" * max(4, len(header)),
                "",
                str(pdata["summary"]),
                "",
            ]
        )
    (docsrc_dir / "persons.rst").write_text("\n".join(p_lines), encoding="utf-8")

    # 3. bibliography.rst
    b_lines: list[str] = [
        ":navigation: header",
        ":order: 50",
        "",
        ".. _bibliography:",
        "",
        "============",
        "Bibliography",
        "============",
        "",
        "Primary sources, classical treatises, and modern triangle geometry",
        "monographs cited across the Fundamentals codex.",
        "",
    ]
    for cid, cdata in sorted(CITATIONS_REGISTRY.items(), key=lambda kv: kv[0].lower()):
        b_lines.extend(
            [
                f".. _cite-{cid}:",
                f".. _{cid}:",
                "",
                cid,
                "-" * max(4, len(cid)),
                "",
                str(cdata["text"]),
                "",
            ]
        )
    (docsrc_dir / "bibliography.rst").write_text("\n".join(b_lines), encoding="utf-8")


def enrich_text(
    text: str,
    seen_terms: set[str] | None = None,
    seen_persons: set[str] | None = None,
) -> str:
    """Wrap first occurrences of registered glossary terms and persons in RST roles.

    Skips regions already inside backticks, math roles, or explicit RST roles.

    Args:
        text: Input RST paragraph or block.
        seen_terms: Optional mutable set tracking already-linked canonical terms.
        seen_persons: Optional mutable set tracking already-linked person IDs.

    Returns:
        Enriched RST string with `:term:` and `:person:` roles.
    """
    if seen_terms is None:
        seen_terms = set()
    if seen_persons is None:
        seen_persons = set()

    # Protect inline roles/code/math blocks from replacement
    protected: list[str] = []

    def _protect(match: re.Match[str]) -> str:
        idx = len(protected)
        protected.append(match.group(0))
        return f"__PROTECTED_{idx}__"

    working = re.sub(
        r"(:[a-z]+:`[^`]+`|``[^`]+``|`[^`]+`|\.\.\s+[a-z_-]+::)",
        _protect,
        text,
    )

    # Link persons first (by full name or surname)
    person_triggers: list[tuple[str, str]] = [
        ("Fred W. Seelig", "seelig"),
        ("Fred Seelig", "seelig"),
        ("Apollonius", "apollonius"),
        ("Ptolemy", "ptolemy"),
        ("Menelaus", "menelaus"),
        ("Giovanni Ceva", "ceva"),
        ("Matthew Stewart", "stewart"),
        ("Lazare Carnot", "carnot"),
        ("Feuerbach", "feuerbach"),
        ("Poncelet", "poncelet"),
        ("Jakob Steiner", "steiner"),
        ("d'Alembert", "dalembert"),
        ("John H. Conway", "conway"),
        ("Clark Kimberling", "kimberling"),
        ("Paul Yiu", "yiu"),
        ("Altshiller-Court", "altshiller_court"),
        ("Coxeter", "coxeter"),
        ("Markowski", "markowski"),
    ]
    for surface, pid in person_triggers:
        if pid in seen_persons:
            continue
        pattern = re.compile(rf"\b{re.escape(surface)}\b")
        if pattern.search(working):
            working = pattern.sub(
                lambda m: _protect_str(f":person:`{m.group(0)} <{pid}>`", protected),
                working,
                count=1,
            )
            seen_persons.add(pid)

    # Link glossary terms (longest phrase first)
    term_candidates: list[tuple[str, str]] = []
    for canonical, data in GLOSSARY_REGISTRY.items():
        term_candidates.append((canonical, canonical))
        for alias in data.get("aliases", []):  # type: ignore[union-attr]
            term_candidates.append((str(alias), canonical))
    term_candidates.sort(key=lambda item: len(item[0]), reverse=True)

    for surface, canonical in term_candidates:
        if canonical in seen_terms:
            continue
        pattern = re.compile(rf"\b{re.escape(surface)}\b", re.IGNORECASE)
        match = pattern.search(working)
        if match:
            matched_str = match.group(0)
            if matched_str.lower() == canonical.lower():
                role_str = f":term:`{matched_str}`"
            else:
                role_str = f":term:`{matched_str} <{canonical}>`"
            working = (
                working[: match.start()]
                + _protect_str(role_str, protected)
                + working[match.end() :]
            )
            seen_terms.add(canonical)

    # Restore protected spans
    for idx in range(len(protected) - 1, -1, -1):
        working = working.replace(f"__PROTECTED_{idx}__", protected[idx])
    return working


def _protect_str(replacement: str, protected: list[str]) -> str:
    """Store a replacement string in `protected` and return its placeholder token.

    Args:
        replacement: Role string to protect from subsequent regex passes.
        protected: Mutable list of protected strings.

    Returns:
        Placeholder token string.
    """
    idx = len(protected)
    protected.append(replacement)
    return f"__PROTECTED_{idx}__"
