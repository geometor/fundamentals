"""Sphinx configuration for GEOMETOR Fundamentals."""
from __future__ import annotations

from pathlib import Path
import re
import sys
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.fundamentals as module  # noqa: E402

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "fundamentals"
repo_name = "fundamentals"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

html_theme = "foundation"
html_static_path: list[str] = []
html_logo = None
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]

_IMG_SVG_RE = re.compile(
    r'<img\b[^>]*?\bsrc="(?P<src>[^"]*?f-\d{2}\.svg)"[^>]*?>'
)


def _inline_fundamentals_svgs(
    app: Any,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Any,
) -> None:
    """Replace `<img src="...f-NN.svg">` with inline `<svg>` markup for interactive controls.

    Args:
        app: Sphinx application instance.
        pagename: Current document page name.
        templatename: Template name used to render the page.
        context: HTML template context dictionary.
        doctree: Document tree node.
    """
    body = context.get("body")
    if not body or ".svg" not in body:
        return

    outdir = Path(app.outdir)
    srcdir = Path(app.srcdir)

    def _repl(match: re.Match[str]) -> str:
        src = match.group("src")
        svg_name = Path(src).name
        candidates = [
            outdir / pagename / ".." / src,
            srcdir / Path(pagename).parent / svg_name,
            outdir / "_images" / svg_name,
        ]
        for cand in candidates:
            try:
                resolved = cand.resolve()
                if resolved.exists() and resolved.suffix == ".svg":
                    raw_svg = resolved.read_text(encoding="utf-8")
                    idx = raw_svg.find("<svg")
                    if idx != -1:
                        return raw_svg[idx:]
            except OSError:
                continue
        return match.group(0)

    context["body"] = _IMG_SVG_RE.sub(_repl, body)


def setup(app: Any) -> None:
    """Register Sphinx build event hooks for GEOMETOR Fundamentals.

    Args:
        app: Sphinx application instance.
    """
    app.connect("html-page-context", _inline_fundamentals_svgs)
