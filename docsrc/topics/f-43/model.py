"""GEOMETOR Fundamentals construction model for F.43: Radical Axes and Radical Center.

Enunciation:
    The radical axis of two circles of radii r_1, r_2 with center separation d cuts the line of centers at x = d/2 + (r_1^2 - r_2^2)/(2 d) from O_1, and the three radical axes of the vertex-altitude circles Gamma_A(h_A), Gamma_B(h_B), Gamma_C(h_C) concur at the radical center W.
"""
from __future__ import annotations

from pathlib import Path

import sympy as sp
from geometor.fundamentals.construct import build_topic_model
from geometor.fundamentals.render import render_svg
from geometor.model import Model


def construct_f_43() -> tuple[Model, dict[str, sp.Expr]]:
    """Construct the exact symbolic/geometric model for F.43 (Radical Axes and Radical Center).

    Returns:
        Tuple of the populated `geometor.model.Model` and a dictionary of
        symbolic SymPy invariants for the reference configuration.
    """
    model, _ = build_topic_model(43, 'Radical Axes and Radical Center')

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
    model, extra_curves = build_topic_model(43, 'Radical Axes and Radical Center')
    svg_out = render_svg(model, here / "f-43.svg", extra_curves=extra_curves)
    _, sym_invariants = construct_f_43()
    print(f"F.43: Radical Axes and Radical Center")
    print(f"  Elements in model: {len(model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for k, v in sym_invariants.items():
        print(f"  {k} = {v}")
