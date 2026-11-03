"""Command-line interface and pipeline runner for GEOMETOR Fundamentals.

Supports subcommands:

- `ingest`: Migrate and index Fred Seelig's 55 notebook folders (353 folios) and
  OpenDocument spreadsheets into `resources/`.
- `transform`: Compile the 3-Track Book Codex (`docsrc/topics/f-01`..`f-55`),
  spreadsheets index (`docsrc/spreadsheets/`), and scholarly apparatus
  (`docsrc/glossary.rst`, `docsrc/persons.rst`, `docsrc/bibliography.rst`).
- `build`: Execute both `ingest` and `transform` in sequence.
- `status`: Display a Rich summary table of all 55 topics and 353 folios.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from rich.console import Console

from .folio_review import summarize_folios
from .ingest import ingest_archive
from .transform import generate_codex


def get_repo_root() -> Path:
    """Resolve the repository root path for `geometor/fundamentals`.

    Returns:
        Absolute `Path` to the repository root.
    """
    return Path(__file__).resolve().parents[3]


def run(argv: list[str] | None = None) -> int:
    """Execute the `fundamentals` CLI pipeline.

    Args:
        argv: Optional list of CLI argument strings.

    Returns:
        Exit status code (`0` on success).
    """
    parser = argparse.ArgumentParser(
        prog="fundamentals",
        description="GEOMETOR Fundamentals — Constructive Geometry Codex & Fred W. Seelig Archive.",
    )
    sub = parser.add_subparsers(dest="command")
    sub.add_parser(
        "ingest", help="Ingest Seelig notebooks and spreadsheets into resources/"
    )
    sub.add_parser("transform", help="Compile 3-Track Book Codex and SVGs into docsrc/")
    sub.add_parser("build", help="Run both ingest and transform")
    sub.add_parser(
        "status", help="Display summary table of the 55 topics and 353 folios"
    )

    args = parser.parse_args(argv)
    cmd = args.command or "status"
    root = get_repo_root()
    console = Console()

    if cmd in {"ingest", "build"}:
        console.print(
            "[bold cyan]Ingesting Fred W. Seelig archive into resources/...[/bold cyan]"
        )
        manifest = ingest_archive(root)
        console.print(
            f"[green]Ingested {manifest['total_topics']} topics and "
            f"{manifest['total_folios']} folios.[/green]"
        )

    if cmd in {"transform", "build"}:
        console.print(
            "[bold cyan]Compiling 3-Track Book Codex and interactive SVGs into docsrc/...[/bold cyan]"
        )
        generate_codex(root)
        console.print(
            "[green]Compiled 55 topics (index.rst, folios.rst, code.rst, f-NN.svg, model.py).[/green]"
        )

    if cmd == "status":
        summarize_folios(root)

    return 0


def main(argv: list[str] | None = None) -> int:
    """Main entry point for `project.scripts` in `pyproject.toml`.

    Args:
        argv: Optional list of CLI argument strings.

    Returns:
        Exit status code (`0` on success).
    """
    return run(argv)
