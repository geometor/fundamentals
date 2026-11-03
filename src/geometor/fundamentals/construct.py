"""Symbolic and constructive geometry engine for the 55 topics of GEOMETOR Fundamentals.

Builds `geometor.model.Model` instances and standalone `model.py` scripts
grounded in Fred W. Seelig's canonical reference configurations, including the
reference acute triangle `(a, b, c) = (5, 6, 7)` on baseline `AB = 7` with
`A = (0, 0)`, `B = (7, 0)`, and `C = (30/7, 12*sqrt(6)/7)`.
"""

from __future__ import annotations

import logging
import math
from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model
from geometor.model.element import CircleElement, Element

_SILENT_LOGGER = logging.getLogger("geometor.fundamentals.silent")
_SILENT_LOGGER.addHandler(logging.NullHandler())
_SILENT_LOGGER.propagate = False


def create_model(name: str = "Fundamentals Construction") -> Model:
    """Create a silent `geometor.model.Model` instance for fast batch or standalone execution.

    Args:
        name: Human-readable title for the construction model.

    Returns:
        Initialized `Model` instance.
    """
    return Model(name, logger=_SILENT_LOGGER)


def add_point(
    model: Model,
    x: float,
    y: float,
    label: str,
    classes: list[str] | None = None,
    parents: list[Any] | None = None,
    guide: bool = False,
) -> spg.Point:
    """Register a `Point` element in `model` with label `label` and CSS `classes`.

    Args:
        model: Target `Model` instance.
        x: Cartesian x-coordinate.
        y: Cartesian y-coordinate.
        label: Algebraic identifier (e.g., `'A'`, `'O'`, `'M_A'`).
        classes: Optional list of CSS classes (`'given'`, `'center'`, `'focus'`, etc.).
        parents: Optional list of parent elements.
        guide: Whether the point is a construction guide.

    Returns:
        Registered `sympy.geometry.Point` instance.
    """
    existing = model.get_element_by_ID(label)
    if existing is not None and isinstance(existing, spg.Point):
        if classes:
            for c in classes:
                model[existing].classes[c] = ""
        return existing

    rx = round(float(x), 8)
    ry = round(float(y), 8)
    pt = spg.Point(sp.Float(rx), sp.Float(ry), evaluate=False)
    step = 0
    while pt in model and model[pt].ID != label:
        step += 1
        pt = spg.Point(sp.Float(rx + step * 1e-7), sp.Float(ry), evaluate=False)
    el = Element(
        pt,
        parents=parents or [],
        classes=classes or [],
        ID=label,
        guide=guide,
    )
    super(Model, model).__setitem__(pt, el)
    return pt


def add_line(
    model: Model,
    pt1: spg.Point,
    pt2: spg.Point,
    label: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Line | None:
    """Register a `Line` element passing through `pt1` and `pt2`.

    Args:
        model: Target `Model` instance.
        pt1: First defining point.
        pt2: Second defining point.
        label: Optional line identifier; defaults to `'[ P Q ]'`.
        classes: Optional list of CSS style classes.
        guide: Whether the line is a dashed construction guide.

    Returns:
        Registered `sympy.geometry.Line` or `None` if points coincide.
    """
    if math.hypot(float(pt1.x) - float(pt2.x), float(pt1.y) - float(pt2.y)) < 1e-6:
        return None
    if not label:
        label = f"[ {model[pt1].ID} {model[pt2].ID} ]"
    ln = spg.Line(pt1, pt2, evaluate=False)
    cls_list = list(classes or [])
    if guide and "guide" not in cls_list:
        cls_list.append("guide")
    el = Element(
        ln,
        parents=[pt1, pt2],
        classes=cls_list,
        ID=label,
        guide=guide,
    )
    super(Model, model).__setitem__(ln, el)
    return ln


def add_segment(
    model: Model,
    pt1: spg.Point,
    pt2: spg.Point,
    label: str = "",
    classes: list[str] | None = None,
) -> spg.Segment | None:
    """Register a `Segment` element joining `pt1` and `pt2`.

    Args:
        model: Target `Model` instance.
        pt1: First endpoint.
        pt2: Second endpoint.
        label: Optional segment identifier.
        classes: Optional list of CSS style classes.

    Returns:
        Registered `sympy.geometry.Segment` or `None` if endpoints coincide.
    """
    if math.hypot(float(pt1.x) - float(pt2.x), float(pt1.y) - float(pt2.y)) < 1e-6:
        return None
    if not label:
        label = f"/ {model[pt1].ID} {model[pt2].ID} /"
    seg = spg.Segment(pt1, pt2, evaluate=False)
    el = Element(
        seg,
        parents=[pt1, pt2],
        classes=classes or ["segment"],
        ID=label,
        guide=False,
    )
    super(Model, model).__setitem__(seg, el)
    return seg


def add_circle(
    model: Model,
    pt_center: spg.Point,
    pt_radius: spg.Point,
    label: str = "",
    classes: list[str] | None = None,
    guide: bool = False,
) -> spg.Circle | None:
    """Register a `Circle` centered at `pt_center` passing through `pt_radius`.

    Args:
        model: Target `Model` instance.
        pt_center: Center point of the circle.
        pt_radius: Point on the circumference defining the radius.
        label: Optional circle identifier; defaults to `'( O A )'`.
        classes: Optional list of CSS style classes.
        guide: Whether the circle is a dashed construction guide.

    Returns:
        Registered `sympy.geometry.Circle` or `None` if radius vanishes.
    """
    r_val = math.hypot(
        float(pt_center.x) - float(pt_radius.x),
        float(pt_center.y) - float(pt_radius.y),
    )
    if r_val < 1e-7:
        return None
    if not label:
        label = f"( {model[pt_center].ID} {model[pt_radius].ID} )"
    circ = spg.Circle(pt_center, sp.Float(round(r_val, 8)), evaluate=False)
    cls_list = list(classes or [])
    if guide and "guide" not in cls_list:
        cls_list.append("guide")
    el = CircleElement(
        circ,
        pt_radius=pt_radius,
        parents=[pt_center, pt_radius],
        classes=cls_list,
        ID=label,
        guide=guide,
    )
    super(Model, model).__setitem__(circ, el)
    return circ


def add_polygon(
    model: Model,
    pts: list[spg.Point],
    label: str = "",
    classes: list[str] | None = None,
) -> spg.Polygon:
    """Register a `Polygon` or `Triangle` element in `model`.

    Args:
        model: Target `Model` instance.
        pts: Ordered vertex points.
        label: Optional polygon identifier; defaults to `'< A B C >'`.
        classes: Optional list of CSS style classes.

    Returns:
        Registered `sympy.geometry.Polygon` or `Triangle`.
    """
    if not label:
        ids_str = " ".join(model[p].ID for p in pts)
        label = f"< {ids_str} >"
    if len(pts) == 3:
        poly = sp.Basic.__new__(spg.Triangle, *pts)
    else:
        poly = sp.Basic.__new__(spg.Polygon, *pts)
    el = Element(
        poly,
        parents=pts,
        classes=classes or [],
        ID=label,
        guide=False,
    )
    super(Model, model).__setitem__(poly, el)
    return poly


def setup_seelig_triangle(
    model: Model,
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> dict[str, Any]:
    """Construct Fred Seelig's canonical triangle `ABC` on baseline `AB = c`.

    Default `(a, b, c) = (5, 6, 7)` sets `A = (0, 0)`, `B = (7, 0)`, and
    `C = (30/7, 12*sqrt(6)/7) ≈ (4.285714, 4.199028)`.

    Args:
        model: Target `Model` instance.
        sides: Side lengths `(a, b, c)` opposite `(A, B, C)`.
        show_guides: Whether to include the Euclid I.22 construction circles.

    Returns:
        Dictionary of points and triangle invariants (`A`, `B`, `C`, `a`, `b`, `c`,
        `s`, `K`, `R`, `r`, `SA`, `SB`, `SC`, `bary_to_xy`).
    """
    a, b, c = sides
    ax, ay = 0.0, 0.0
    bx, by = c, 0.0
    cx = (b**2 + c**2 - a**2) / (2.0 * c)
    cy = math.sqrt(max(0.0, b**2 - cx**2))

    pt_a = add_point(model, ax, ay, "A", classes=["given"])
    pt_b = add_point(model, bx, by, "B", classes=["given"])
    pt_c = add_point(model, cx, cy, "C", classes=["given"])

    if show_guides:
        add_circle(model, pt_a, pt_c, "( A C )", classes=["guide"], guide=True)
        add_circle(model, pt_b, pt_c, "( B C )", classes=["guide"], guide=True)

    add_polygon(model, [pt_a, pt_b, pt_c], "ABC")
    add_segment(model, pt_a, pt_b, "c", classes=["reference"])
    add_segment(model, pt_b, pt_c, "a", classes=["reference"])
    add_segment(model, pt_c, pt_a, "b", classes=["reference"])

    s = 0.5 * (a + b + c)
    area = math.sqrt(max(0.0, s * (s - a) * (s - b) * (s - c)))
    r_in = area / s
    r_circ = (a * b * c) / (4.0 * area)
    sa = 0.5 * (b**2 + c**2 - a**2)
    sb = 0.5 * (c**2 + a**2 - b**2)
    sc = 0.5 * (a**2 + b**2 - c**2)

    def bary_to_xy(u: float, v: float, w: float) -> tuple[float, float]:
        denom = u + v + w
        return (
            (u * ax + v * bx + w * cx) / denom,
            (u * ay + v * by + w * cy) / denom,
        )

    return {
        "A": pt_a,
        "B": pt_b,
        "C": pt_c,
        "A_xy": (ax, ay),
        "B_xy": (bx, by),
        "C_xy": (cx, cy),
        "a": a,
        "b": b,
        "c": c,
        "s": s,
        "K": area,
        "R": r_circ,
        "r": r_in,
        "SA": sa,
        "SB": sb,
        "SC": sc,
        "bary_to_xy": bary_to_xy,
    }


def _add_bary_point(
    model: Model,
    ctx: dict[str, Any],
    u: float,
    v: float,
    w: float,
    label: str,
    classes: list[str] | None = None,
) -> spg.Point:
    """Add a point to `model` from homogeneous barycentric coordinates `(u : v : w)`.

    Args:
        model: Target `Model` instance.
        ctx: Triangle context dictionary from :func:`setup_seelig_triangle`.
        u: First barycentric weight.
        v: Second barycentric weight.
        w: Third barycentric weight.
        label: Point identifier.
        classes: Optional CSS style classes.

    Returns:
        Registered `spg.Point`.
    """
    px, py = ctx["bary_to_xy"](u, v, w)
    return add_point(model, px, py, label, classes=classes)


def build_topic_model(
    topic_num: int,
    title: str = "",
) -> tuple[Model, list[dict[str, object]]]:
    """Construct the exact geometric model and optional analytic curves for topic `F.<topic_num>`.

    Args:
        topic_num: Integer topic number (1 through 55).
        title: Human-readable topic title.

    Returns:
        Tuple of `(model, extra_curves)` ready for SVG rendering and analysis.
    """
    model = create_model(f"F.{topic_num}: {title}" if title else f"F.{topic_num}")
    extra_curves: list[dict[str, object]] = []

    if topic_num == 1:
        # F.1 Albert's Parabola: Parabola y = x^2/4, focus F=(0,1), directrix y=-1,
        # vertex V=(0,0), point P=(4,4), tangent and reflection
        v_pt = add_point(model, 0.0, 0.0, "V", classes=["given"])
        f_pt = add_point(model, 0.0, 1.0, "F", classes=["focus"])
        d_left = add_point(model, -4.5, -1.0, "D_1", classes=["guide"], guide=True)
        d_right = add_point(model, 5.5, -1.0, "D_2", classes=["guide"], guide=True)
        add_line(model, d_left, d_right, "directrix", classes=["axis"])
        add_line(model, v_pt, f_pt, "axis", classes=["guide"], guide=True)
        p_pt = add_point(model, 3.0, 2.25, "P", classes=["target"])
        q_pt = add_point(model, 3.0, -1.0, "Q", classes=["foot"])
        t_pt = add_point(model, 0.0, -2.25, "T", classes=["midpoint"])
        add_segment(model, f_pt, p_pt, "/ F P /", classes=["cevian"])
        add_segment(model, p_pt, q_pt, "/ P Q /", classes=["cevian"])
        add_segment(model, f_pt, q_pt, "/ F Q /", classes=["guide"])
        add_line(model, t_pt, p_pt, "tangent", classes=["euler"])
        pts = [(x * 0.2, (x * 0.2) ** 2 / 4.0) for x in range(-22, 26)]
        extra_curves.append(
            {"label": "parabola", "points": pts, "classes": ["parabola"]}
        )
        return model, extra_curves

    if topic_num == 2:
        # F.2 Bilinear Transformations: Projective mapping of 4 harmonic points A, C, B, D
        a_pt = add_point(model, 0.0, 0.0, "A", classes=["given"])
        c_pt = add_point(model, 2.5, 0.0, "C", classes=["midpoint"])
        b_pt = add_point(model, 4.0, 0.0, "B", classes=["given"])
        d_pt = add_point(model, 10.0, 0.0, "D", classes=["harmonic"])
        s_pt = add_point(model, 3.2, 4.2, "S", classes=["focus"])
        a2 = add_point(model, 0.64, 0.84, "A'", classes=["given"])
        c2 = add_point(model, 2.75, 1.5, "C'", classes=["midpoint"])
        b2 = add_point(model, 3.68, 1.81, "B'", classes=["given"])
        d2 = add_point(model, 6.22, 2.68, "D'", classes=["harmonic"])
        add_line(model, a_pt, d_pt, "l", classes=["reference"])
        add_line(model, a2, d2, "l'", classes=["euler"])
        for p in (a_pt, c_pt, b_pt, d_pt):
            add_segment(model, s_pt, p, classes=["cevian"])
        return model, extra_curves

    if topic_num in {3, 14, 35, 53, 54, 55}:
        # F.3 Biquadratic Heron, F.14 Conway Notation, F.35 Obtuse/Acute, F.53 Trig, F.54 Scripts, F.55 Misc
        ctx = setup_seelig_triangle(
            model, (5.0, 6.0, 7.0), show_guides=(topic_num == 3)
        )
        sa, sb, sc = ctx["SA"], ctx["SB"], ctx["SC"]
        pt_h = _add_bary_point(
            model, ctx, sb * sc, sc * sa, sa * sb, "H", classes=["center"]
        )
        pt_o = _add_bary_point(
            model,
            ctx,
            ctx["a"] ** 2 * sa,
            ctx["b"] ** 2 * sb,
            ctx["c"] ** 2 * sc,
            "O",
            classes=["center"],
        )
        pt_hc = _add_bary_point(model, ctx, sb, sa, 0.0, "H_C", classes=["foot"])
        add_segment(model, ctx["C"], pt_hc, "h_c", classes=["altitude"])
        add_circle(model, pt_o, ctx["A"], "circumcircle", classes=["circumcircle"])
        if topic_num == 14:
            pt_g = _add_bary_point(model, ctx, 1.0, 1.0, 1.0, "G", classes=["focus"])
            add_line(model, pt_o, pt_h, "Euler", classes=["euler"])
            _ = pt_g
        return model, extra_curves

    if topic_num == 4:
        # F.4 Carnot's Theorem: d_a + d_b + d_c = R + r
        ctx = setup_seelig_triangle(model, (5.0, 6.0, 7.0))
        a, b, c = ctx["a"], ctx["b"], ctx["c"]
        sa, sb, sc = ctx["SA"], ctx["SB"], ctx["SC"]
        pt_o = _add_bary_point(
            model, ctx, a**2 * sa, b**2 * sb, c**2 * sc, "O", classes=["focus"]
        )
        pt_i = _add_bary_point(model, ctx, a, b, c, "I", classes=["center"])
        ma = _add_bary_point(model, ctx, 0.0, 1.0, 1.0, "M_A", classes=["midpoint"])
        mb = _add_bary_point(model, ctx, 1.0, 0.0, 1.0, "M_B", classes=["midpoint"])
        mc = _add_bary_point(model, ctx, 1.0, 1.0, 0.0, "M_C", classes=["midpoint"])
        add_segment(model, pt_o, ma, "d_a", classes=["cevian"])
        add_segment(model, pt_o, mb, "d_b", classes=["cevian"])
        add_segment(model, pt_o, mc, "d_c", classes=["cevian"])
        add_circle(model, pt_o, ctx["A"], "circumcircle", classes=["circumcircle"])
        t_c = add_point(model, float(pt_i.x), 0.0, "T_C", classes=["foot"])
        add_circle(model, pt_i, t_c, "incircle", classes=["incircle"])
        return model, extra_curves

    if topic_num in {5, 16, 48}:
        # F.5 Centers of Similitude, F.16 d'Alembert, F.48 Verisimilitude
        o1 = add_point(model, 0.0, 0.0, "O_1", classes=["center"])
        r1_pt = add_point(model, 0.0, 1.5, "R_1", classes=["midpoint"])
        o2 = add_point(model, 5.0, 0.0, "O_2", classes=["center"])
        r2_pt = add_point(model, 5.0, 3.0, "R_2", classes=["midpoint"])
        s_int = add_point(model, 5.0 / 3.0, 0.0, "S_+", classes=["harmonic"])
        s_ext = add_point(model, -5.0, 0.0, "S_-", classes=["focus"])
        add_circle(model, o1, r1_pt, "C_1", classes=["circumcircle"])
        add_circle(model, o2, r2_pt, "C_2", classes=["incircle"])
        add_line(model, s_ext, o2, "axis", classes=["reference"])
        add_line(model, s_ext, r2_pt, "tangent_ext", classes=["euler"])
        add_segment(model, o1, r1_pt, "r_1", classes=["cevian"])
        add_segment(model, o2, r2_pt, "r_2", classes=["cevian"])
        if topic_num == 16:
            o3 = add_point(model, 2.5, 4.0, "O_3", classes=["center"])
            r3_pt = add_point(model, 2.5, 5.0, "R_3", classes=["guide"], guide=True)
            add_circle(model, o3, r3_pt, "C_3", classes=["ninepoint"])
            s_23 = add_point(model, 1.25, 6.0, "S_{23}", classes=["focus"])
            add_line(model, s_ext, s_23, "dAlembert_axis", classes=["euler"])
        return model, extra_curves

    if topic_num == 6:
        # F.6 Centroid: G = X(2), medians AM_A, BM_B, CM_C, medial triangle
        ctx = setup_seelig_triangle(model, (5.0, 6.0, 7.0))
        ma = _add_bary_point(model, ctx, 0.0, 1.0, 1.0, "M_A", classes=["midpoint"])
        mb = _add_bary_point(model, ctx, 1.0, 0.0, 1.0, "M_B", classes=["midpoint"])
        mc = _add_bary_point(model, ctx, 1.0, 1.0, 0.0, "M_C", classes=["midpoint"])
        pt_g = _add_bary_point(model, ctx, 1.0, 1.0, 1.0, "G", classes=["focus"])
        add_segment(model, ctx["A"], ma, "m_a", classes=["median"])
        add_segment(model, ctx["B"], mb, "m_b", classes=["median"])
        add_segment(model, ctx["C"], mc, "m_c", classes=["median"])
        add_polygon(model, [ma, mb, mc], "M_A M_B M_C")
        _ = pt_g
        return model, extra_curves

    if topic_num in {7, 47, 52}:
        # F.7 Ceva and Menelaus, F.47 u-v-w, F.52 Homogeneous Barycentric Coordinates
        ctx = setup_seelig_triangle(model, (5.0, 6.0, 7.0))
        u, v, w = 2.0, 3.0, 4.0
        pt_p = _add_bary_point(model, ctx, u, v, w, "P", classes=["focus"])
        pt_d = _add_bary_point(model, ctx, 0.0, v, w, "D", classes=["foot"])
        pt_e = _add_bary_point(model, ctx, u, 0.0, w, "E", classes=["foot"])
        pt_f = _add_bary_point(model, ctx, u, v, 0.0, "F", classes=["foot"])
        add_segment(model, ctx["A"], pt_d, "AD", classes=["cevian"])
        add_segment(model, ctx["B"], pt_e, "BE", classes=["cevian"])
        add_segment(model, ctx["C"], pt_f, "CF", classes=["cevian"])
        add_polygon(model, [pt_d, pt_e, pt_f], "DEF")
        if topic_num == 7:
            # Menelaus trilinear polar line meeting AB extended at F'
            pt_f_ext = _add_bary_point(
                model, ctx, -u, v, 0.0, "F'", classes=["harmonic"]
            )
            add_line(model, pt_d, pt_e, "Menelaus", classes=["euler"])
            add_line(model, ctx["A"], ctx["B"], "AB_ext", classes=["guide"], guide=True)
            _ = pt_f_ext
        return model, extra_curves

    if topic_num in {8, 9, 13}:
        # F.8 Chord Intersection, F.9 Circle Equations, F.13 Compare Triangles in Circles
        o_pt = add_point(model, 0.0, 0.0, "O", classes=["center"])
        a_pt = add_point(model, -3.0, -2.0, "A", classes=["given"])
        r_val = math.hypot(3.0, 2.0)
        b_pt = add_point(
            model, r_val * math.cos(0.4), r_val * math.sin(0.4), "B", classes=["given"]
        )
        c_pt = add_point(
            model, r_val * math.cos(2.1), r_val * math.sin(2.1), "C", classes=["given"]
        )
        d_pt = add_point(
            model,
            r_val * math.cos(-0.9),
            r_val * math.sin(-0.9),
            "D",
            classes=["given"],
        )
        add_circle(model, o_pt, a_pt, "circle", classes=["circumcircle"])
        add_segment(model, a_pt, b_pt, "AB", classes=["reference"])
        add_segment(model, c_pt, d_pt, "CD", classes=["reference"])
        # Intersection P of chords AB and CD
        ln1 = spg.Line(a_pt, b_pt)
        ln2 = spg.Line(c_pt, d_pt)
        inter = ln1.intersection(ln2)
        if inter:
            ip = inter[0]
            add_point(model, float(ip.x), float(ip.y), "P", classes=["focus"])
        add_Segment_extra = add_segment(model, a_pt, c_pt, "AC", classes=["cevian"])
        add_segment(model, d_pt, b_pt, "DB", classes=["cevian"])
        _ = add_Segment_extra
        return model, extra_curves

    if topic_num in {10, 27, 33, 44}:
        # F.10 Circles & Geometric Mean, F.27 Harmonic Mean, F.33 m-n, F.44 Ratios
        m_val, n_val = 5.0, 2.0
        a_pt = add_point(model, 0.0, 0.0, "A", classes=["given"])
        h_pt = add_point(model, m_val, 0.0, "H", classes=["foot"])
        b_pt = add_point(model, m_val + n_val, 0.0, "B", classes=["given"])
        o_pt = add_point(model, 0.5 * (m_val + n_val), 0.0, "O", classes=["center"])
        g_val = math.sqrt(m_val * n_val)
        c_pt = add_point(model, m_val, g_val, "C", classes=["focus"])
        # Harmonic mean foot K of H on OC
        ox = 0.5 * (m_val + n_val)
        dx, dy = m_val - ox, g_val
        t_proj = ((m_val - ox) * dx) / (dx**2 + dy**2)
        k_pt = add_point(
            model, ox + t_proj * dx, t_proj * dy, "K", classes=["harmonic"]
        )
        add_circle(model, o_pt, b_pt, "semicircle", classes=["circumcircle"])
        add_polygon(model, [a_pt, b_pt, c_pt], "ABC")
        add_segment(model, c_pt, h_pt, "G", classes=["altitude"])
        add_segment(model, o_pt, c_pt, "A_mean", classes=["euler"])
        add_segment(model, c_pt, k_pt, "H_mean", classes=["cevian"])
        return model, extra_curves

    if topic_num == 11:
        # F.11 Circumcenter: O = X(3), perpendicular bisectors, circumcircle
        ctx = setup_seelig_triangle(model, (5.0, 6.0, 7.0))
        a, b, c = ctx["a"], ctx["b"], ctx["c"]
        sa, sb, sc = ctx["SA"], ctx["SB"], ctx["SC"]
        pt_o = _add_bary_point(
            model, ctx, a**2 * sa, b**2 * sb, c**2 * sc, "O", classes=["focus"]
        )
        ma = _add_bary_point(model, ctx, 0.0, 1.0, 1.0, "M_A", classes=["midpoint"])
        mb = _add_bary_point(model, ctx, 1.0, 0.0, 1.0, "M_B", classes=["midpoint"])
        mc = _add_bary_point(model, ctx, 1.0, 1.0, 0.0, "M_C", classes=["midpoint"])
        add_line(model, pt_o, ma, "perp_a", classes=["cevian"])
        add_line(model, pt_o, mb, "perp_b", classes=["cevian"])
        add_line(model, pt_o, mc, "perp_c", classes=["cevian"])
        add_circle(model, pt_o, ctx["A"], "circumcircle", classes=["circumcircle"])
        return model, extra_curves

    if topic_num in {12, 43}:
        # F.12 Coaxial Circles & F.43 Radical Axes
        r_top = add_point(model, 0.0, 3.2, "R_1", classes=["midpoint"])
        r_bot = add_point(model, 0.0, -3.2, "R_2", classes=["midpoint"])
        l1 = add_point(model, -2.0, 0.0, "L_1", classes=["focus"])
        l2 = add_point(model, 2.0, 0.0, "L_2", classes=["focus"])
        add_line(model, r_top, r_bot, "radical_axis", classes=["euler"])
        add_line(model, l1, l2, "line_of_centers", classes=["reference"])
        for idx, cx in enumerate([-3.5, -2.5, 2.5, 3.8], start=1):
            rad = math.sqrt(cx**2 - 4.0)
            c_pt = add_point(model, cx, 0.0, f"O_{idx}", classes=["center"])
            p_pt = add_point(model, cx, rad, f"P_{idx}", classes=["guide"], guide=True)
            add_circle(model, c_pt, p_pt, f"C_{idx}", classes=["coaxial"])
        return model, extra_curves

    if topic_num == 15:
        # F.15 Cyclic Quadrilateral: Ptolemy's theorem AC*BD = AB*CD + BC*AD
        o_pt = add_point(model, 0.0, 0.0, "O", classes=["center"])
        r = 4.0
        angles = [-2.4, -0.6, 0.7, 2.1]
        labels = ["A", "B", "C", "D"]
        pts: list[spg.Point] = []
        for ang, lbl in zip(angles, labels):
            pts.append(
                add_point(
                    model, r * math.cos(ang), r * math.sin(ang), lbl, classes=["given"]
                )
            )
        add_circle(model, o_pt, pts[0], "circumcircle", classes=["circumcircle"])
        add_polygon(model, pts, "ABCD")
        add_segment(model, pts[0], pts[2], "e", classes=["euler"])
        add_segment(model, pts[1], pts[3], "f", classes=["euler"])
        ln1 = spg.Line(pts[0], pts[2])
        ln2 = spg.Line(pts[1], pts[3])
        inter = ln1.intersection(ln2)
        if inter:
            add_point(
                model, float(inter[0].x), float(inter[0].y), "P", classes=["focus"]
            )
        return model, extra_curves

    if topic_num in {17, 22, 37}:
        # F.17 Ellipse, F.22 Functions, F.37 Parabolas
        a_semi, b_semi = 5.0, 3.0
        c_focus = math.sqrt(a_semi**2 - b_semi**2)
        o_pt = add_point(model, 0.0, 0.0, "O", classes=["center"])
        f1 = add_point(model, -c_focus, 0.0, "F_1", classes=["focus"])
        f2 = add_point(model, c_focus, 0.0, "F_2", classes=["focus"])
        v1 = add_point(model, -a_semi, 0.0, "A_1", classes=["given"])
        v2 = add_point(model, a_semi, 0.0, "A_2", classes=["given"])
        b1 = add_point(model, 0.0, b_semi, "B_1", classes=["midpoint"])
        ang = 1.05
        px, py = a_semi * math.cos(ang), b_semi * math.sin(ang)
        p_pt = add_point(model, px, py, "P", classes=["target"])
        add_segment(model, v1, v2, "major_axis", classes=["reference"])
        add_segment(model, o_pt, b1, "b", classes=["cevian"])
        add_segment(model, f1, p_pt, "r_1", classes=["euler"])
        add_segment(model, f2, p_pt, "r_2", classes=["euler"])
        add_circle(model, o_pt, v2, "auxiliary_circle", classes=["guide"], guide=True)
        e_pts = [
            (
                a_semi * math.cos(2.0 * math.pi * k / 72),
                b_semi * math.sin(2.0 * math.pi * k / 72),
            )
            for k in range(73)
        ]
        extra_curves.append(
            {"label": "ellipse", "points": e_pts, "classes": ["ellipse"]}
        )
        return model, extra_curves

    if topic_num in {18, 24, 49}:
        # F.18 Equilateral Triangle, F.24 Gothic, F.49 Vesica Piscis (Euclid I.1)
        a_pt = add_point(model, 0.0, 0.0, "A", classes=["given"])
        b_pt = add_point(model, 4.0, 0.0, "B", classes=["given"])
        h = 2.0 * math.sqrt(3.0)
        c_pt = add_point(model, 2.0, h, "C", classes=["focus"])
        d_pt = add_point(model, 2.0, -h, "D", classes=["harmonic"])
        m_pt = add_point(model, 2.0, 0.0, "M", classes=["midpoint"])
        g_pt = add_point(model, 2.0, h / 3.0, "G", classes=["center"])
        add_circle(model, a_pt, b_pt, "( A B )", classes=["circumcircle"])
        add_circle(model, b_pt, a_pt, "( B A )", classes=["incircle"])
        add_polygon(model, [a_pt, b_pt, c_pt], "ABC")
        add_segment(model, c_pt, d_pt, "CD", classes=["euler"])
        add_segment(model, a_pt, b_pt, "AB", classes=["reference"])
        add_circle(model, g_pt, a_pt, "circumcircle", classes=["ninepoint"])
        _ = m_pt
        return model, extra_curves

    if topic_num in {19, 28, 29}:
        # F.19 Equal Incircle Theorem, F.28 Incenter, F.29 Inradius
        ctx = setup_seelig_triangle(model, (5.0, 6.0, 7.0))
        a, b, c = ctx["a"], ctx["b"], ctx["c"]
        pt_i = _add_bary_point(model, ctx, a, b, c, "I", classes=["focus"])
        ta = _add_bary_point(model, ctx, 0.0, 1.0, 1.0, "D_A", classes=["midpoint"])
        # Gergonne touchpoints on BC, CA, AB:
        s = ctx["s"]
        t_bc = _add_bary_point(model, ctx, 0.0, s - c, s - b, "T_A", classes=["foot"])
        t_ca = _add_bary_point(model, ctx, s - c, 0.0, s - a, "T_B", classes=["foot"])
        t_ab = _add_bary_point(model, ctx, s - b, s - a, 0.0, "T_C", classes=["foot"])
        add_segment(model, ctx["A"], pt_i, "bis_A", classes=["bisector"])
        add_segment(model, ctx["B"], pt_i, "bis_B", classes=["bisector"])
        add_segment(model, ctx["C"], pt_i, "bis_C", classes=["bisector"])
        add_segment(model, pt_i, t_ab, "r", classes=["euler"])
        add_circle(model, pt_i, t_ab, "incircle", classes=["incircle"])
        add_polygon(model, [t_bc, t_ca, t_ab], "contact_triangle")
        _ = ta
        return model, extra_curves

    if topic_num == 20:
        # F.20 Extangent & Excircles: I_a, I_b, I_c and incircle
        ctx = setup_seelig_triangle(model, (5.0, 6.0, 7.0))
        a, b, c = ctx["a"], ctx["b"], ctx["c"]
        pt_i = _add_bary_point(model, ctx, a, b, c, "I", classes=["center"])
        ia = _add_bary_point(model, ctx, -a, b, c, "I_a", classes=["focus"])
        ib = _add_bary_point(model, ctx, a, -b, c, "I_b", classes=["focus"])
        ic = _add_bary_point(model, ctx, a, b, -c, "I_c", classes=["focus"])
        t_ab = add_point(model, float(pt_i.x), 0.0, "T_C", classes=["foot"])
        t_ext_c = add_point(model, float(ic.x), 0.0, "E_C", classes=["foot"])
        add_circle(model, pt_i, t_ab, "incircle", classes=["incircle"])
        add_circle(model, ic, t_ext_c, "excircle_C", classes=["excircle"])
        add_polygon(model, [ia, ib, ic], "excentral_triangle")
        return model, extra_curves

    if topic_num == 21:
        # F.21 Fermat Point X(13): outer equilateral triangles on sides of ABC
        ctx = setup_seelig_triangle(model, (5.0, 6.0, 7.0))
        a, b, c = ctx["a"], ctx["b"], ctx["c"]
        sa, sb, sc = ctx["SA"], ctx["SB"], ctx["SC"]
        s2 = 2.0 * ctx["K"]
        rt3 = math.sqrt(3.0)
        u = 1.0 / (sa + s2 / rt3)
        v = 1.0 / (sb + s2 / rt3)
        w = 1.0 / (sc + s2 / rt3)
        pt_f = _add_bary_point(model, ctx, u, v, w, "F", classes=["focus"])
        # Outer equilateral apex C' on AB
        c_ext = add_point(model, 0.5 * c, -0.5 * rt3 * c, "C'", classes=["harmonic"])
        add_polygon(model, [ctx["A"], ctx["B"], c_ext], "ABC'")
        add_segment(model, ctx["C"], c_ext, "CC'", classes=["euler"])
        add_segment(model, ctx["A"], pt_f, "FA", classes=["cevian"])
        add_segment(model, ctx["B"], pt_f, "FB", classes=["cevian"])
        add_segment(model, ctx["C"], pt_f, "FC", classes=["cevian"])
        _ = (a, b)
        return model, extra_curves

    if topic_num in {23, 30, 32}:
        # F.23 Golden Triangles, F.30 Isosceles, F.32 Markowski
        phi = 0.5 * (1.0 + math.sqrt(5.0))
        a_pt = add_point(model, 0.0, 0.0, "A", classes=["given"])
        b_pt = add_point(model, 1.0, 0.0, "B", classes=["given"])
        cx = 0.5
        cy = math.sqrt(phi**2 - 0.25)
        c_pt = add_point(model, cx, cy, "C", classes=["focus"])
        # Bisector of angle B divides AC at D in the golden ratio
        dx = cx / phi
        dy = cy / phi
        d_pt = add_point(model, dx, dy, "D", classes=["harmonic"])
        add_polygon(model, [a_pt, b_pt, c_pt], "ABC")
        add_segment(model, b_pt, d_pt, "BD", classes=["euler"])
        add_circle(model, a_pt, b_pt, "( A B )", classes=["guide"], guide=True)
        return model, extra_curves

    if topic_num in {25, 26, 39, 51}:
        # F.25 Harmonic Conjugates, F.26 Harmonic Conjugate Inversion,
        # F.39 Pole-Polar, F.51 Apollonian Circles
        a_pt = add_point(model, 0.0, 0.0, "A", classes=["given"])
        b_pt = add_point(model, 6.0, 0.0, "B", classes=["given"])
        o_pt = add_point(model, 3.0, 0.0, "M", classes=["center"])
        c_pt = add_point(model, 4.0, 0.0, "C", classes=["midpoint"])
        d_pt = add_point(model, 7.5, 0.0, "D", classes=["harmonic"])
        m_cd = add_point(model, 5.75, 0.0, "O_A", classes=["center"])
        # Circle on AB and Apollonius circle on CD (ratio 2:1)
        add_circle(model, o_pt, b_pt, "circle_AB", classes=["circumcircle"])
        add_circle(model, m_cd, c_pt, "Apollonius", classes=["ninepoint"])
        add_line(model, a_pt, d_pt, "axis", classes=["reference"])
        # Intersection T of the two orthogonal circles:
        tx = 4.0
        ty = math.sqrt(max(0.0, 9.0 - (tx - 3.0) ** 2))
        t_pt = add_point(model, tx, ty, "P", classes=["focus"])
        t_bot = add_point(model, tx, -ty, "P'", classes=["foot"])
        add_segment(model, t_pt, t_bot, "polar", classes=["euler"])
        add_segment(model, o_pt, t_pt, "R", classes=["cevian"])
        add_segment(model, m_cd, t_pt, "tangent", classes=["cevian"])
        return model, extra_curves

    if topic_num in {31, 41}:
        # F.31 Logic Tests (Point-in-Triangle), F.41 Problems
        ctx = setup_seelig_triangle(model, (5.0, 6.0, 7.0))
        p_in = _add_bary_point(model, ctx, 2.0, 2.0, 3.0, "P_{in}", classes=["focus"])
        p_out = _add_bary_point(
            model, ctx, -1.0, 2.0, 3.0, "P_{out}", classes=["harmonic"]
        )
        for v in (ctx["A"], ctx["B"], ctx["C"]):
            add_segment(model, v, p_in, classes=["cevian"])
            add_segment(model, v, p_out, classes=["guide"])
        return model, extra_curves

    if topic_num in {34, 36, 38, 50}:
        # F.34 Nine-Point Circle, F.36 Orthic Triangle, F.38 Pedal Triangles, F.50 Altitudes
        ctx = setup_seelig_triangle(model, (5.0, 6.0, 7.0))
        a, b, c = ctx["a"], ctx["b"], ctx["c"]
        sa, sb, sc = ctx["SA"], ctx["SB"], ctx["SC"]
        pt_h = _add_bary_point(
            model, ctx, sb * sc, sc * sa, sa * sb, "H", classes=["focus"]
        )
        pt_o = _add_bary_point(
            model, ctx, a**2 * sa, b**2 * sb, c**2 * sc, "O", classes=["center"]
        )
        pt_g = _add_bary_point(model, ctx, 1.0, 1.0, 1.0, "G", classes=["center"])
        ha = _add_bary_point(model, ctx, 0.0, sc, sb, "H_A", classes=["foot"])
        hb = _add_bary_point(model, ctx, sc, 0.0, sa, "H_B", classes=["foot"])
        hc = _add_bary_point(model, ctx, sb, sa, 0.0, "H_C", classes=["foot"])
        add_segment(model, ctx["A"], ha, "h_a", classes=["altitude"])
        add_segment(model, ctx["B"], hb, "h_b", classes=["altitude"])
        add_segment(model, ctx["C"], hc, "h_c", classes=["altitude"])
        add_polygon(model, [ha, hb, hc], "H_A H_B H_C")
        if topic_num == 34:
            ma = _add_bary_point(model, ctx, 0.0, 1.0, 1.0, "M_A", classes=["midpoint"])
            mb = _add_bary_point(model, ctx, 1.0, 0.0, 1.0, "M_B", classes=["midpoint"])
            mc = _add_bary_point(model, ctx, 1.0, 1.0, 0.0, "M_C", classes=["midpoint"])
            nx = 0.5 * (float(pt_o.x) + float(pt_h.x))
            ny = 0.5 * (float(pt_o.y) + float(pt_h.y))
            pt_n = add_point(model, nx, ny, "N", classes=["focus"])
            add_circle(model, pt_n, ma, "nine_point_circle", classes=["ninepoint"])
            add_line(model, pt_o, pt_h, "Euler", classes=["euler"])
            _ = (mb, mc, pt_g)
        return model, extra_curves

    if topic_num in {40, 45}:
        # F.40 Polygons & F.45 Squares
        o_pt = add_point(model, 0.0, 0.0, "O", classes=["center"])
        r = 4.0
        n_sides = 4 if topic_num == 45 else 6
        verts: list[spg.Point] = []
        for k in range(n_sides):
            ang = 2.0 * math.pi * k / n_sides + (math.pi / 4.0 if n_sides == 4 else 0.0)
            verts.append(
                add_point(
                    model,
                    r * math.cos(ang),
                    r * math.sin(ang),
                    f"V_{k + 1}",
                    classes=["given"],
                )
            )
        add_circle(model, o_pt, verts[0], "circumcircle", classes=["circumcircle"])
        add_polygon(model, verts, "polygon")
        m_side = add_point(
            model,
            0.5 * (float(verts[0].x) + float(verts[1].x)),
            0.5 * (float(verts[0].y) + float(verts[1].y)),
            "M",
            classes=["foot"],
        )
        add_circle(model, o_pt, m_side, "incircle", classes=["incircle"])
        add_segment(model, o_pt, verts[0], "R", classes=["euler"])
        add_segment(model, o_pt, m_side, "r", classes=["cevian"])
        return model, extra_curves

    if topic_num == 42:
        # F.42 Pythagorean Triples: (3, 4, 5) with incircle r=1 and excircles r_a=2, r_b=3, r_c=6
        ctx = setup_seelig_triangle(model, (3.0, 4.0, 5.0))
        a, b, c = ctx["a"], ctx["b"], ctx["c"]
        pt_i = _add_bary_point(model, ctx, a, b, c, "I", classes=["focus"])
        pt_o = _add_bary_point(model, ctx, 0.0, 1.0, 1.0, "O", classes=["midpoint"])
        t_ab = add_point(model, float(pt_i.x), 0.0, "T_C", classes=["foot"])
        add_circle(model, pt_i, t_ab, "incircle", classes=["incircle"])
        add_circle(model, pt_o, ctx["A"], "circumcircle", classes=["circumcircle"])
        add_segment(model, ctx["C"], pt_o, "m_c", classes=["euler"])
        return model, extra_curves

    # Default / F.46 Stewart's Theorem: b^2*m + c^2*n = a*(d^2 + m*n)
    ctx = setup_seelig_triangle(model, (5.0, 6.0, 7.0))
    pt_d = _add_bary_point(model, ctx, 0.0, 3.0, 2.0, "D", classes=["focus"])
    pt_hc = _add_bary_point(
        model, ctx, 0.0, ctx["SC"], ctx["SB"], "H_A", classes=["foot"]
    )
    add_segment(model, ctx["A"], pt_d, "d", classes=["euler"])
    add_segment(model, ctx["A"], pt_hc, "h_a", classes=["altitude"])
    return model, extra_curves


def generate_topic_model_code(
    topic_num: int,
    title: str,
    enunciation: str,
) -> str:
    """Generate a standalone executable `model.py` script for topic `F.<topic_num>`.

    Args:
        topic_num: Integer topic number (1 through 55).
        title: Topic title string.
        enunciation: Formal geometric enunciation for the module docstring.

    Returns:
        Formatted Python source code for `docsrc/topics/f-NN/model.py`.
    """
    slug = f"f-{topic_num:02d}"
    return f'''"""GEOMETOR Fundamentals construction model for F.{topic_num}: {title}.

Enunciation:
    {enunciation}
"""
from __future__ import annotations

from pathlib import Path

import sympy as sp
from geometor.fundamentals.construct import build_topic_model
from geometor.fundamentals.render import render_svg
from geometor.model import Model


def construct_f_{topic_num:02d}() -> tuple[Model, dict[str, sp.Expr]]:
    """Construct the exact symbolic/geometric model for F.{topic_num} ({title}).

    Returns:
        Tuple of the populated `geometor.model.Model` and a dictionary of
        symbolic SymPy invariants for the reference configuration.
    """
    model, _ = build_topic_model({topic_num}, {title!r})

    # Canonical Seelig reference triangle (a, b, c) = (5, 6, 7) symbolic invariants
    a, b, c = sp.Integer(5), sp.Integer(6), sp.Integer(7)
    s = (a + b + c) / 2
    area = sp.sqrt(s * (s - a) * (s - b) * (s - c))
    inradius = area / s
    circumradius = (a * b * c) / (4 * area)
    s_a = (b**2 + c**2 - a**2) / 2
    s_b = (c**2 + a**2 - b**2) / 2
    s_c = (a**2 + b**2 - c**2) / 2

    invariants: dict[str, sp.Expr] = {{
        "s": s,
        "K": area,
        "r": sp.simplify(inradius),
        "R": sp.simplify(circumradius),
        "S_A": s_a,
        "S_B": s_b,
        "S_C": s_c,
    }}
    return model, invariants


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model, extra_curves = build_topic_model({topic_num}, {title!r})
    svg_out = render_svg(model, here / "{slug}.svg", extra_curves=extra_curves)
    _, sym_invariants = construct_f_{topic_num:02d}()
    print(f"F.{topic_num}: {title}")
    print(f"  Elements in model: {{len(model)}}")
    print(f"  Rendered SVG:      {{svg_out.name}}")
    for k, v in sym_invariants.items():
        print(f"  {{k}} = {{v}}")
'''
