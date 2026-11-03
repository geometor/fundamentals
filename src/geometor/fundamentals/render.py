"""Explorer-styled interactive SVG renderer for GEOMETOR Fundamentals.

Renders a `geometor.model.Model` (along with optional analytical conic curves
such as parabolas and ellipses) into a standalone, interactive SVG diagram with
embedded dark/light mode styling, pan/zoom/reset/labels/guides controls, and
two-way `.geom-ref[data-ref]` hover highlighting synchronized with the prose.
"""

from __future__ import annotations

import math
from pathlib import Path
from xml.sax.saxutils import escape

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

Point = spg.Point
Line = spg.Line
Circle = spg.Circle
Polygon = (spg.Polygon, spg.Triangle)
Segment = spg.Segment

EXPLORER_SVG_CSS = """
. explorer-canvas, svg.fundamentals-diagram {
    background-color: #111111;
    border: 1px solid #333;
    border-radius: 6px;
    width: 100%;
    height: auto;
    max-height: 540px;
    display: block;
    margin: 0.5rem auto;
    user-select: none;
    overflow: hidden;
    cursor: grab;
}
svg.fundamentals-diagram:active {
    cursor: grabbing;
}
@media (prefers-color-scheme: light) {
    svg.fundamentals-diagram {
        background-color: #fafafa;
        border-color: #ddd;
    }
    svg.fundamentals-diagram .Point {
        stroke: #fafafa !important;
    }
    svg.fundamentals-diagram .Point.given {
        fill: #111111 !important;
    }
    svg.fundamentals-diagram .label-halo {
        stroke: #fafafa !important;
    }
    svg.fundamentals-diagram .label-fill {
        fill: #111111 !important;
    }
    svg.fundamentals-diagram .Line,
    svg.fundamentals-diagram .Segment {
        stroke: #555555;
    }
}
.Line, .Segment {
    stroke: #999999;
    stroke-linecap: round;
    vector-effect: non-scaling-stroke;
    stroke-width: 1.2px;
    fill: none;
    opacity: 0.78;
    transition: stroke-width 0.15s ease, opacity 0.15s ease, filter 0.15s ease;
}
.Circle, .Curve {
    stroke: #c93b76;
    vector-effect: non-scaling-stroke;
    stroke-width: 1.25px;
    fill: none;
    opacity: 0.82;
    transition: stroke-width 0.15s ease, opacity 0.15s ease, filter 0.15s ease;
}
.Polygon {
    fill: rgba(70, 130, 180, 0.10);
    stroke: #5c9fd6;
    vector-effect: non-scaling-stroke;
    stroke-width: 1.8px;
    stroke-linejoin: round;
    transition: stroke-width 0.15s ease, fill-opacity 0.15s ease;
}
.Point {
    fill: #e5c07b;
    stroke: #111111;
    vector-effect: non-scaling-stroke;
    stroke-width: 1.4px;
    transition: r 0.15s ease, filter 0.15s ease;
}
.Point.given {
    fill: #ffffff;
}
.Point.focus, .Point.center, .Point.target {
    fill: #00e5ff;
}
.Point.harmonic, .Point.conjugate {
    fill: #ff5252;
}
.Point.midpoint, .Point.foot {
    fill: #98c379;
}
.Line.guide, .Circle.guide, .Segment.guide {
    stroke-dasharray: 4 4;
    opacity: 0.42;
    stroke-width: 0.9px;
}
.Line.reference, .Segment.reference {
    stroke: #5c9fd6;
    stroke-width: 1.8px;
    opacity: 0.9;
}
.Line.euler, .Line.axis, .Segment.euler, .Segment.axis {
    stroke: #e06c75;
    stroke-width: 1.8px;
    opacity: 0.92;
}
.Line.cevian, .Segment.cevian, .Segment.altitude, .Segment.median, .Segment.bisector {
    stroke: #98c379;
    stroke-width: 1.4px;
    opacity: 0.85;
}
.Circle.circumcircle {
    stroke: #e06c75;
    stroke-width: 1.5px;
}
.Circle.incircle, .Circle.excircle {
    stroke: #e5c07b;
    stroke-width: 1.5px;
}
.Circle.ninepoint, .Circle.apollonius, .Circle.coaxial {
    stroke: #61afef;
    stroke-width: 1.5px;
}
.Curve.parabola, .Curve.ellipse, .Curve.hyperbola {
    stroke: #c678dd;
    stroke-width: 2.0px;
    opacity: 0.95;
}
.element-group {
    cursor: pointer;
}
.element-group.svg-hovered .Line,
.element-group.svg-hovered .Segment,
.element-group.svg-hovered .Circle,
.element-group.svg-hovered .Curve,
.element-group.svg-hovered .Polygon {
    stroke: #00e5ff !important;
    stroke-width: 2.8px !important;
    opacity: 1.0 !important;
    filter: drop-shadow(0 0 5px rgba(0, 229, 255, 0.75));
}
.element-group.svg-hovered .Point {
    fill: #00e5ff !important;
    filter: drop-shadow(0 0 6px rgba(0, 229, 255, 0.9));
}
.geom-ref {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-weight: 600;
    padding: 0.05em 0.3em;
    border-radius: 3px;
    background: rgba(97, 175, 239, 0.14);
    color: #61afef;
    cursor: pointer;
    transition: background-color 0.15s ease, color 0.15s ease;
}
.geom-ref:hover, .geom-ref.ref-hovered {
    background: #00e5ff;
    color: #111111;
}
.svg-control-btn {
    cursor: pointer;
}
.svg-control-btn rect {
    fill: rgba(30, 30, 30, 0.82);
    stroke: #555;
    stroke-width: 1px;
    rx: 3px;
}
.svg-control-btn:hover rect {
    fill: rgba(60, 60, 60, 0.95);
    stroke: #00e5ff;
}
.svg-control-btn text {
    fill: #ddd;
    font-family: sans-serif;
    font-size: 9px;
    font-weight: 600;
    text-anchor: middle;
    dominant-baseline: central;
    pointer-events: none;
}
svg.hide-labels .labels-layer {
    display: none;
}
svg.hide-guides .guide {
    display: none;
}
"""

INTERACTIVE_SVG_JS = """
(function() {
  if (window.__fundamentalsSvgInit) return;
  window.__fundamentalsSvgInit = true;

  function initDiagram(svg) {
    if (svg.dataset.initialized) return;
    svg.dataset.initialized = "true";
    const vp = svg.querySelector(".svg-viewport");
    if (!vp) return;

    let scale = 1, tx = 0, ty = 0;
    let dragging = false, startX = 0, startY = 0;

    function applyTransform() {
      vp.setAttribute("transform", `translate(${tx},${ty}) scale(${scale})`);
    }

    svg.addEventListener("wheel", function(e) {
      e.preventDefault();
      const rect = svg.getBoundingClientRect();
      const vb = svg.viewBox.baseVal;
      const mx = vb.x + ((e.clientX - rect.left) / rect.width) * vb.width;
      const my = vb.y + ((e.clientY - rect.top) / rect.height) * vb.height;
      const factor = e.deltaY < 0 ? 1.15 : 1 / 1.15;
      const newScale = Math.min(Math.max(scale * factor, 0.25), 12);
      tx = mx - (mx - tx) * (newScale / scale);
      ty = my - (my - ty) * (newScale / scale);
      scale = newScale;
      applyTransform();
    }, { passive: false });

    svg.addEventListener("mousedown", function(e) {
      if (e.target.closest(".svg-controls")) return;
      dragging = true;
      startX = e.clientX;
      startY = e.clientY;
    });

    window.addEventListener("mousemove", function(e) {
      if (!dragging) return;
      const rect = svg.getBoundingClientRect();
      const vb = svg.viewBox.baseVal;
      const dx = ((e.clientX - startX) / rect.width) * vb.width;
      const dy = ((e.clientY - startY) / rect.height) * vb.height;
      startX = e.clientX;
      startY = e.clientY;
      tx += dx;
      ty += dy;
      applyTransform();
    });

    window.addEventListener("mouseup", function() {
      dragging = false;
    });

    svg.querySelectorAll(".svg-control-btn").forEach(function(btn) {
      btn.addEventListener("click", function(e) {
        e.stopPropagation();
        const action = btn.dataset.action;
        if (action === "zoom-in") { scale = Math.min(scale * 1.25, 12); applyTransform(); }
        else if (action === "zoom-out") { scale = Math.max(scale / 1.25, 0.25); applyTransform(); }
        else if (action === "reset") { scale = 1; tx = 0; ty = 0; applyTransform(); }
        else if (action === "labels") { svg.classList.toggle("hide-labels"); }
        else if (action === "guides") { svg.classList.toggle("hide-guides"); }
      });
    });
  }

  function setupHoverSync() {
    document.querySelectorAll("svg.fundamentals-diagram").forEach(initDiagram);

    document.addEventListener("mouseover", function(e) {
      const refEl = e.target.closest("[data-ref]");
      if (!refEl) return;
      const ref = refEl.dataset.ref;
      if (!ref) return;
      document.querySelectorAll(`.element-group[data-ref="${CSS.escape(ref)}"]`).forEach(el => el.classList.add("svg-hovered"));
      document.querySelectorAll(`.geom-ref[data-ref="${CSS.escape(ref)}"]`).forEach(el => el.classList.add("ref-hovered"));
    });

    document.addEventListener("mouseout", function(e) {
      const refEl = e.target.closest("[data-ref]");
      if (!refEl) return;
      const ref = refEl.dataset.ref;
      if (!ref) return;
      document.querySelectorAll(`.element-group[data-ref="${CSS.escape(ref)}"]`).forEach(el => el.classList.remove("svg-hovered"));
      document.querySelectorAll(`.geom-ref[data-ref="${CSS.escape(ref)}"]`).forEach(el => el.classList.remove("ref-hovered"));
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupHoverSync);
  } else {
    setupHoverSync();
  }
})();
"""


def _to_float(val: object) -> float:
    """Convert a SymPy or numeric expression safely to float.

    Args:
        val: SymPy expression or float/int.

    Returns:
        Floating-point value.
    """
    if isinstance(val, (int, float)):
        return float(val)
    return float(sp.N(val))  # type: ignore[arg-type]


def _format_svg_label(label: str) -> str:
    """Convert an algebraic label like `M_A` or `P'` into clean SVG `<tspan>` markup.

    Args:
        label: Element label string.

    Returns:
        SVG text/tspan inner markup.
    """
    clean = label.strip()
    if "_" in clean:
        base, sub = clean.split("_", 1)
        sub = sub.strip("{}")
        return f'{escape(base)}<tspan dy="0.3em" font-size="75%">{escape(sub)}</tspan>'
    return escape(clean)


def render_svg(
    model: Model,
    output_path: Path,
    extra_curves: list[dict[str, object]] | None = None,
    padding_ratio: float = 0.16,
) -> Path:
    """Render a `geometor.model.Model` to an interactive Explorer-styled SVG file.

    Args:
        model: Populated `geometor.model.Model` instance.
        output_path: Destination `.svg` file path.
        extra_curves: Optional list of parametric curve dictionaries with keys
            `label`, `points` (list of `(x, y)` floats), and `classes` (list of strings).
        padding_ratio: Fractional margin added around the bounding box of points/circles.

    Returns:
        Path to the written SVG file.
    """
    pts_xy: list[tuple[float, float]] = []
    for el, info in model.items():
        if isinstance(el, Point):
            x_f = _to_float(el.x)
            y_f = _to_float(el.y)
            if math.isfinite(x_f) and math.isfinite(y_f):
                pts_xy.append((x_f, y_f))
        elif isinstance(el, Circle):
            cx = _to_float(el.center.x)
            cy = _to_float(el.center.y)
            r = _to_float(el.radius)
            if "guide" not in info.classes and math.isfinite(r) and r < 25.0:
                pts_xy.extend([(cx - r, cy - r), (cx + r, cy + r)])

    if extra_curves:
        for curve in extra_curves:
            for px, py in curve.get("points", []):  # type: ignore[union-attr]
                pts_xy.append((float(px), float(py)))

    if not pts_xy:
        pts_xy = [(-2.0, -2.0), (8.0, 6.0)]

    min_x = min(p[0] for p in pts_xy)
    max_x = max(p[0] for p in pts_xy)
    min_y = min(p[1] for p in pts_xy)
    max_y = max(p[1] for p in pts_xy)

    span_x = max(max_x - min_x, 2.0)
    span_y = max(max_y - min_y, 2.0)
    span = max(span_x, span_y)
    pad = span * padding_ratio

    vb_x = min_x - pad
    vb_y = -(max_y + pad)
    vb_w = span_x + 2 * pad
    vb_h = span_y + 2 * pad

    unit = max(vb_w, vb_h) / 100.0
    pt_r = unit * 1.15
    font_sz = unit * 3.1

    polygons_svg: list[str] = []
    circles_svg: list[str] = []
    curves_svg: list[str] = []
    lines_svg: list[str] = []
    points_svg: list[str] = []
    labels_svg: list[str] = []

    clip_min_x = min_x - span * 1.5
    clip_max_x = max_x + span * 1.5
    clip_min_y = min_y - span * 1.5
    clip_max_y = max_y + span * 1.5

    for el, info in model.items():
        label = info.ID or ""
        cls_str = " ".join(info.classes.keys())

        if isinstance(el, Polygon):
            coord_pairs: list[str] = []
            for v in el.vertices:
                vx = _to_float(v.x)
                vy = -_to_float(v.y)
                coord_pairs.append(f"{vx:.4f},{vy:.4f}")
            pts_attr = " ".join(coord_pairs)
            polygons_svg.append(
                f'    <g class="element-group" data-ref="{escape(label)}">'
                f'<polygon class="Polygon {escape(cls_str)}" points="{pts_attr}">'
                f"<title>{escape(label)}</title></polygon></g>"
            )

        elif isinstance(el, Circle):
            cx = _to_float(el.center.x)
            cy = -_to_float(el.center.y)
            r = abs(_to_float(el.radius))
            circles_svg.append(
                f'    <g class="element-group" data-ref="{escape(label)}">'
                f'<circle class="Circle {escape(cls_str)}" cx="{cx:.4f}" cy="{cy:.4f}" r="{r:.4f}">'
                f"<title>{escape(label)}</title></circle></g>"
            )

        elif isinstance(el, Segment):
            p1, p2 = el.points
            x1, y1 = _to_float(p1.x), -_to_float(p1.y)
            x2, y2 = _to_float(p2.x), -_to_float(p2.y)
            lines_svg.append(
                f'    <g class="element-group" data-ref="{escape(label)}">'
                f'<line class="Segment {escape(cls_str)}" x1="{x1:.4f}" y1="{y1:.4f}" x2="{x2:.4f}" y2="{y2:.4f}">'
                f"<title>{escape(label)}</title></line></g>"
            )

        elif isinstance(el, Line):
            p1, p2 = el.points
            x1, y1 = _to_float(p1.x), _to_float(p1.y)
            x2, y2 = _to_float(p2.x), _to_float(p2.y)
            dx, dy = x2 - x1, y2 - y1
            length = math.hypot(dx, dy)
            if length > 1e-9:
                ux, uy = dx / length, dy / length
                reach = span * 2.5
                lx1, ly1 = x1 - ux * reach, -(y1 - uy * reach)
                lx2, ly2 = x1 + ux * reach, -(y1 + uy * reach)
                if (
                    min(x1, x2) >= clip_min_x
                    and max(x1, x2) <= clip_max_x
                    and min(y1, y2) >= clip_min_y
                    and max(y1, y2) <= clip_max_y
                ):
                    lines_svg.append(
                        f'    <g class="element-group" data-ref="{escape(label)}">'
                        f'<line class="Line {escape(cls_str)}" x1="{lx1:.4f}" y1="{ly1:.4f}" x2="{lx2:.4f}" y2="{ly2:.4f}">'
                        f"<title>{escape(label)}</title></line></g>"
                    )

        elif isinstance(el, Point):
            px = _to_float(el.x)
            py = -_to_float(el.y)
            if not (math.isfinite(px) and math.isfinite(py)):
                continue
            r_use = pt_r * (
                1.28
                if (
                    "focus" in info.classes
                    or "center" in info.classes
                    or "given" in info.classes
                )
                else 1.0
            )
            points_svg.append(
                f'    <g class="element-group" data-ref="{escape(label)}">'
                f'<circle class="Point {escape(cls_str)}" cx="{px:.4f}" cy="{py:.4f}" r="{r_use:.4f}">'
                f"<title>{escape(label)} ({px:.3f}, {-py:.3f})</title></circle></g>"
            )
            if label and "guide" not in info.classes:
                lx = px + pt_r * 1.65
                ly = py - pt_r * 1.45
                inner_lbl = _format_svg_label(label)
                labels_svg.append(
                    f'    <g class="element-group" data-ref="{escape(label)}">'
                    f'<text class="label-halo" x="{lx:.4f}" y="{ly:.4f}" font-family="sans-serif" '
                    f'font-size="{font_sz:.4f}" font-weight="600" stroke="#111111" '
                    f'stroke-width="{font_sz * 0.25:.4f}" stroke-linejoin="round" fill="none">{inner_lbl}</text>'
                    f'<text class="label-fill" x="{lx:.4f}" y="{ly:.4f}" font-family="sans-serif" '
                    f'font-size="{font_sz:.4f}" font-weight="600" fill="#f0f0f0">{inner_lbl}</text>'
                    f"</g>"
                )

    if extra_curves:
        for curve in extra_curves:
            c_label = str(curve.get("label", "curve"))
            c_classes = " ".join(str(c) for c in curve.get("classes", ["parabola"]))  # type: ignore[union-attr]
            c_pts = curve.get("points", [])
            if isinstance(c_pts, list) and len(c_pts) >= 2:
                d_parts: list[str] = []
                for idx, (cx, cy) in enumerate(c_pts):
                    cmd = "M" if idx == 0 else "L"
                    d_parts.append(f"{cmd}{float(cx):.4f},{-float(cy):.4f}")
                d_str = " ".join(d_parts)
                curves_svg.append(
                    f'    <g class="element-group" data-ref="{escape(c_label)}">'
                    f'<path class="Curve {escape(c_classes)}" d="{d_str}">'
                    f"<title>{escape(c_label)}</title></path></g>"
                )

    # Interactive control bar in top-right corner of viewBox
    btn_h = max(vb_w, vb_h) * 0.042
    btn_w = btn_h * 1.55
    gap = btn_h * 0.18
    buttons = [
        ("zoom-in", "+"),
        ("zoom-out", "−"),
        ("reset", "⟲"),
        ("labels", "Lbl"),
        ("guides", "Gde"),
    ]
    total_w = len(buttons) * btn_w + (len(buttons) - 1) * gap
    start_bx = vb_x + vb_w - total_w - gap * 1.5
    by = vb_y + gap * 1.5
    controls_svg: list[str] = ['  <g class="svg-controls">']
    for i, (action, text) in enumerate(buttons):
        bx = start_bx + i * (btn_w + gap)
        cx_t = bx + btn_w / 2.0
        cy_t = by + btn_h / 2.0
        controls_svg.append(
            f'    <g class="svg-control-btn" data-action="{action}">'
            f'<rect x="{bx:.4f}" y="{by:.4f}" width="{btn_w:.4f}" height="{btn_h:.4f}" />'
            f'<text x="{cx_t:.4f}" y="{cy_t:.4f}" style="font-size:{btn_h * 0.46:.4f}px">{text}</text>'
            f"</g>"
        )
    controls_svg.append("  </g>")

    svg_lines: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" class="fundamentals-diagram" '
        f'viewBox="{vb_x:.4f} {vb_y:.4f} {vb_w:.4f} {vb_h:.4f}">',
        f"  <style>{EXPLORER_SVG_CSS}</style>",
        '  <g class="svg-viewport">',
        '    <g class="polygons-layer">',
        *polygons_svg,
        "    </g>",
        '    <g class="circles-layer">',
        *circles_svg,
        "    </g>",
        '    <g class="curves-layer">',
        *curves_svg,
        "    </g>",
        '    <g class="lines-layer">',
        *lines_svg,
        "    </g>",
        '    <g class="points-layer">',
        *points_svg,
        "    </g>",
        '    <g class="labels-layer">',
        *labels_svg,
        "    </g>",
        "  </g>",
        *controls_svg,
        f"  <script>{INTERACTIVE_SVG_JS}</script>",
        "</svg>",
    ]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(svg_lines) + "\n", encoding="utf-8")
    return output_path
