"""GEOMETOR Fundamentals construction model for F.50: Altitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem.

Enunciation:
    Given the three altitudes h_A, h_B, h_C of triangle ABC with reciprocal semiperimeter H = (h_A^{-1} + h_B^{-1} + h_C^{-1})/2, Mitchell's reciprocal Heron formula states K^{-1} = 4 sqrt(H (H - h_A^{-1})(H - h_B^{-1})(H - h_C^{-1})), and a triangle is right-angled at C if and only if h_A^{-2} + h_B^{-2} = h_C^{-2} (the Symphonic Theorem).
"""
from __future__ import annotations

from pathlib import Path

import sympy as sp
from geometor.fundamentals.construct import build_topic_model
from geometor.fundamentals.render import render_svg
from geometor.model import Model


def construct_f_50() -> tuple[Model, dict[str, sp.Expr]]:
    """Construct the exact symbolic/geometric model for F.50 (Altitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem).

    Returns:
        Tuple of the populated `geometor.model.Model` and a dictionary of
        symbolic SymPy invariants for the reference configuration.
    """
    model, _ = build_topic_model(50, "Altitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem")

    # Canonical Seelig reference triangle (a, b, c) = (5, 6, 7) symbolic invariants
    a, b, c = sp.Integer(5), sp.Integer(6), sp.Integer(7)
    s = (a + b + c) / 2
    area = sp.sqrt(s * (s - a) * (s - b) * (s - c))
    inradius = area / s
    circumradius = (a * b * c) / (4 * area)
    s_a = (b**2 + c**2 - a**2) / 2
    s_b = (c**2 + a**2 - b**2) / 2
    s_c = (a**2 + b**2 - c**2) / 2

    invariants: dict[str, sp.Expr] = {
        "s": s,
        "K": area,
        "r": sp.simplify(inradius),
        "R": sp.simplify(circumradius),
        "S_A": s_a,
        "S_B": s_b,
        "S_C": s_c,
    }
    return model, invariants


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model, extra_curves = build_topic_model(50, "Altitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem")
    svg_out = render_svg(model, here / "f-50.svg", extra_curves=extra_curves)
    _, sym_invariants = construct_f_50()
    print(f"F.50: Altitudes, Mitchell's Reciprocal Heron Formula, and the Symphonic Theorem")
    print(f"  Elements in model: {len(model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for k, v in sym_invariants.items():
        print(f"  {k} = {v}")
