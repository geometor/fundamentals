"""GEOMETOR Fundamentals construction model for F.48: Verisimilitude, Corner Subtriangles, and Excircle Homothety.

Enunciation:
    If lines parallel to the sides of triangle ABC are drawn tangent to the incircle, the three corner subtriangles are homothetic to ABC with scale factors x/s, y/s, z/s (where x = s - a, y = s - b, z = s - c), so their inradii satisfy r_A + r_B + r_C = r.
"""
from __future__ import annotations

from pathlib import Path

import sympy as sp
from geometor.fundamentals.construct import build_topic_model
from geometor.fundamentals.render import render_svg
from geometor.model import Model


def construct_f_48() -> tuple[Model, dict[str, sp.Expr]]:
    """Construct the exact symbolic/geometric model for F.48 (Verisimilitude, Corner Subtriangles, and Excircle Homothety).

    Returns:
        Tuple of the populated `geometor.model.Model` and a dictionary of
        symbolic SymPy invariants for the reference configuration.
    """
    model, _ = build_topic_model(48, 'Verisimilitude, Corner Subtriangles, and Excircle Homothety')

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
    model, extra_curves = build_topic_model(48, 'Verisimilitude, Corner Subtriangles, and Excircle Homothety')
    svg_out = render_svg(model, here / "f-48.svg", extra_curves=extra_curves)
    _, sym_invariants = construct_f_48()
    print(f"F.48: Verisimilitude, Corner Subtriangles, and Excircle Homothety")
    print(f"  Elements in model: {len(model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for k, v in sym_invariants.items():
        print(f"  {k} = {v}")
