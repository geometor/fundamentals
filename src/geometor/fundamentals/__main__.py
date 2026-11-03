"""The package entry point into the GEOMETOR Fundamentals application."""

from __future__ import annotations

from .app import main, run

__all__ = ["main", "run"]

if __name__ == "__main__":
    raise SystemExit(main())
