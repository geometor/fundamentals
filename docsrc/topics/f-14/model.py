"""GEOMETOR Fundamentals construction model for F.14: Conway Notation.

Enunciation:
    In John H. Conway's triangle notation, setting S = 2K (twice the area of triangle ABC), S_omega = (a^2 + b^2 + c^2)/2, and S_A = (b^2 + c^2 - a^2)/2, S_B = (c^2 + a^2 - b^2)/2, S_C = (a^2 + b^2 - c^2)/2 reduces trigonometric and barycentric identities to polynomial expressions satisfying S_B S_C + S_C S_A + S_A S_B = S^2.
"""
from __future__ import annotations

from pathlib import Path

import sympy as sp
from geometor.fundamentals.construct import build_topic_model
from geometor.fundamentals.render import render_svg
from geometor.model import Model


def construct_f_14() -> tuple[Model, dict[str, sp.Expr]]:
    """Construct the exact symbolic/geometric model for F.14 (Conway Notation).

    Returns:
        Tuple of the populated `geometor.model.Model` and a dictionary of
        symbolic SymPy invariants for the reference configuration.
    """
    model, _ = build_topic_model(14, 'Conway Notation')

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
    model, extra_curves = build_topic_model(14, 'Conway Notation')
    svg_out = render_svg(model, here / "f-14.svg", extra_curves=extra_curves)
    _, sym_invariants = construct_f_14()
    print(f"F.14: Conway Notation")
    print(f"  Elements in model: {len(model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for k, v in sym_invariants.items():
        print(f"  {k} = {v}")
