"""GEOMETOR Fundamentals construction model for F.29: Inradius.

Enunciation:
    The inradius r = K / s = (1/2) sqrt(((b+c-a)(c+a-b)(a+b-c))/(a+b+c)) = 4 R sin(alpha/2) sin(beta/2) sin(gamma/2) takes integer values on primitive Pythagorean triples and partitions the perimeter into Conway segments x, y, z whose touchpoints T_A, T_B, T_C concur at the Gergonne point Ge = X(7).
"""
from __future__ import annotations

from pathlib import Path

import sympy as sp
from geometor.fundamentals.construct import build_topic_model
from geometor.fundamentals.render import render_svg
from geometor.model import Model


def construct_f_29() -> tuple[Model, dict[str, sp.Expr]]:
    """Construct the exact symbolic/geometric model for F.29 (Inradius).

    Returns:
        Tuple of the populated `geometor.model.Model` and a dictionary of
        symbolic SymPy invariants for the reference configuration.
    """
    model, _ = build_topic_model(29, 'Inradius')

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
    model, extra_curves = build_topic_model(29, 'Inradius')
    svg_out = render_svg(model, here / "f-29.svg", extra_curves=extra_curves)
    _, sym_invariants = construct_f_29()
    print(f"F.29: Inradius")
    print(f"  Elements in model: {len(model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for k, v in sym_invariants.items():
        print(f"  {k} = {v}")
