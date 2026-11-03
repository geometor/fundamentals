"""GEOMETOR Fundamentals construction model for F.26: Harmonic Conjugate Inversion.

Enunciation:
    For a circle Gamma of center M and radius r on diameter AB, internal point C at x = |MC| and its harmonic conjugate D at y = |MD| are inverses satisfying x*y = r^2, while the tangent DT = T forms a parallelogram M D M_T T whose long diagonal z satisfies z^2 = y^2 + 3*r^2 by Stewart's Theorem.
"""
from __future__ import annotations

from pathlib import Path

import sympy as sp
from geometor.fundamentals.construct import build_topic_model
from geometor.fundamentals.render import render_svg
from geometor.model import Model


def construct_f_26() -> tuple[Model, dict[str, sp.Expr]]:
    """Construct the exact symbolic/geometric model for F.26 (Harmonic Conjugate Inversion).

    Returns:
        Tuple of the populated `geometor.model.Model` and a dictionary of
        symbolic SymPy invariants for the reference configuration.
    """
    model, _ = build_topic_model(26, 'Harmonic Conjugate Inversion')

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
    model, extra_curves = build_topic_model(26, 'Harmonic Conjugate Inversion')
    svg_out = render_svg(model, here / "f-26.svg", extra_curves=extra_curves)
    _, sym_invariants = construct_f_26()
    print(f"F.26: Harmonic Conjugate Inversion")
    print(f"  Elements in model: {len(model)}")
    print(f"  Rendered SVG:      {svg_out.name}")
    for k, v in sym_invariants.items():
        print(f"  {k} = {v}")
