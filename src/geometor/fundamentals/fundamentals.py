"""Core application class for GEOMETOR Fundamentals."""

from __future__ import annotations

from pathlib import Path

from .app import run


class Fundamentals:
    """High-level interface to the GEOMETOR Fundamentals archive and codex pipeline."""

    def __init__(self, repo_root: Path | None = None) -> None:
        """Initialize the Fundamentals manager.

        Args:
            repo_root: Optional root directory of `geometor/fundamentals`.
        """
        self.repo_root = repo_root or Path(__file__).resolve().parents[3]

    def run(self, argv: list[str] | None = None) -> int:
        """Execute the CLI pipeline.

        Args:
            argv: Optional list of CLI argument strings.

        Returns:
            Exit code (`0` on success).
        """
        return run(argv)
