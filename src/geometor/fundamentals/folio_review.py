"""Interactive Folio Review server and CLI inspector for the Fred W. Seelig archive.

Provides a lightweight Flask web interface and Rich CLI summary for inspecting
the 353 scanned folios (`0001.jpg`–`0353.jpg`), their diplomatic `.rst`
transcriptions, `.notes.rst` commentary, and review status in
`resources/seelig/folio_reviews.json`.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from rich.console import Console
from rich.table import Table


def get_repo_root() -> Path:
    """Resolve the root directory of `geometor/fundamentals`.

    Returns:
        Absolute `Path` to the repository root.
    """
    return Path(__file__).resolve().parents[3]


def summarize_folios(repo_root: Path | None = None) -> dict[str, int]:
    """Print a Rich summary table of the 55 topic folders and 353 folios.

    Args:
        repo_root: Optional repository root path.

    Returns:
        Dictionary of summary counts (`topics`, `folios`, `verified`).
    """
    root = repo_root or get_repo_root()
    topics_path = root / "resources" / "topics.json"
    reviews_path = root / "resources" / "seelig" / "folio_reviews.json"

    console = Console()
    if not topics_path.exists():
        console.print(
            "[yellow]resources/topics.json not found. Run `fundamentals ingest` first.[/yellow]"
        )
        return {"topics": 0, "folios": 0, "verified": 0}

    manifest = json.loads(topics_path.read_text(encoding="utf-8"))
    reviews = (
        json.loads(reviews_path.read_text(encoding="utf-8"))
        if reviews_path.exists()
        else {}
    )

    table = Table(title="GEOMETOR Fundamentals — Fred W. Seelig Folio Archive")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Topic", style="bold")
    table.add_column("Category", style="magenta")
    table.add_column("Folios", style="green")
    table.add_column("Count", justify="right")

    topics = list(manifest.get("topics", []))
    for t in topics:
        table.add_row(
            str(t.get("id", "")),
            str(t.get("title", "")),
            str(t.get("category", "")),
            str(t.get("folio_range", "")),
            str(t.get("folio_count", 0)),
        )
    console.print(table)

    verified = sum(
        1
        for r in reviews.values()
        if isinstance(r, dict) and r.get("status") == "verified"
    )
    total_folios = int(manifest.get("total_folios", 0))
    console.print(
        f"[bold green]Total Topics:[/bold green] {len(topics)} | "
        f"[bold green]Total Folios:[/bold green] {total_folios} | "
        f"[bold green]Verified:[/bold green] {verified}"
    )
    return {
        "topics": len(topics),
        "folios": total_folios,
        "verified": verified,
    }


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for `fundamentals-review`.

    Args:
        argv: Optional list of command-line arguments.

    Returns:
        Process exit code (`0` on success).
    """
    parser = argparse.ArgumentParser(
        prog="fundamentals-review",
        description="Inspect and review the 353 Fred W. Seelig manuscript folios.",
    )
    parser.add_argument(
        "--folio",
        type=str,
        default="",
        help="Inspect a specific 4-digit folio ID (e.g., 0001).",
    )
    args = parser.parse_args(argv)
    root = get_repo_root()

    if args.folio:
        fid = f"{int(args.folio):04d}" if args.folio.isdigit() else args.folio
        matches = list((root / "resources" / "seelig").glob(f"*/{fid}.rst"))
        console = Console()
        if not matches:
            console.print(f"[red]Folio {fid} not found in resources/seelig/.[/red]")
            return 1
        rst_file = matches[0]
        notes_file = rst_file.with_name(f"{fid}.notes.rst")
        console.rule(f"[bold cyan]Folio {fid}[/bold cyan] ({rst_file.parent.name})")
        console.print(rst_file.read_text(encoding="utf-8"))
        if notes_file.exists():
            console.rule(f"[bold yellow]Notes {fid}[/bold yellow]")
            console.print(notes_file.read_text(encoding="utf-8"))
        return 0

    summarize_folios(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
