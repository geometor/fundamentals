"""Test suite for the GEOMETOR Fundamentals archive, construction engine, and Book Codex."""

from __future__ import annotations

import json
from pathlib import Path

from geometor.fundamentals import (
    __version__,
    build_topic_model,
    generate_topic_model_code,
    render_svg,
)
from geometor.fundamentals.apparatus import (
    CITATIONS_REGISTRY,
    GLOSSARY_REGISTRY,
    PERSONS_REGISTRY,
    enrich_text,
)
from geometor.fundamentals.catalog import TOPICS_CATALOG

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_version_and_registries() -> None:
    """Verify package version and scholarly apparatus registries."""
    assert __version__ == "0.1.0"
    assert len(GLOSSARY_REGISTRY) >= 35
    assert "seelig" in PERSONS_REGISTRY
    assert "SeeligNotebooks" in CITATIONS_REGISTRY

    enriched = enrich_text(
        "Fred W. Seelig analyzed the centroid and harmonic conjugate using Conway triangle notation."
    )
    assert ":person:`Fred W. Seelig <seelig>`" in enriched
    assert ":term:`centroid`" in enriched
    assert ":term:`harmonic conjugate`" in enriched


def test_catalog_completeness() -> None:
    """Verify all 55 topics exist in TOPICS_CATALOG with valid DAG dependencies."""
    assert len(TOPICS_CATALOG) == 55
    ids = {str(t["id"]) for t in TOPICS_CATALOG}
    assert ids == {f"F.{i}" for i in range(1, 56)}

    for idx, topic in enumerate(TOPICS_CATALOG, start=1):
        assert int(topic["num"]) == idx
        assert str(topic["id"]) == f"F.{idx}"
        assert str(topic["title"])
        assert str(topic["enunciation"])
        assert list(topic["signature_given"])  # type: ignore[arg-type]
        assert list(topic["signature_steps"])  # type: ignore[arg-type]
        assert list(topic["synthesis"])  # type: ignore[arg-type]
        for dep in topic.get("depends_on", []):  # type: ignore[union-attr]
            assert str(dep) in ids
            assert str(dep) != str(topic["id"])


def test_build_and_render_models(tmp_path: Path) -> None:
    """Verify construction models and SVG rendering across representative topics."""
    sample_nums = [1, 4, 6, 7, 11, 12, 14, 15, 18, 21, 23, 25, 28, 34, 42, 46, 52]
    for num in sample_nums:
        model, extra_curves = build_topic_model(num, f"Topic {num}")
        assert len(model) >= 4
        svg_path = render_svg(
            model, tmp_path / f"f-{num:02d}.svg", extra_curves=extra_curves
        )
        assert svg_path.exists()
        content = svg_path.read_text(encoding="utf-8")
        assert "<svg" in content
        assert 'class="svg-controls"' in content
        assert "data-ref=" in content

        code = generate_topic_model_code(num, f"Topic {num}", "Test enunciation.")
        assert f"def construct_f_{num:02d}()" in code


def test_ingested_resources_and_codex() -> None:
    """Verify the ingested resources/ archive and compiled docsrc/topics/ Book Codex."""
    topics_json = REPO_ROOT / "resources" / "topics.json"
    worksheets_json = REPO_ROOT / "resources" / "spreadsheets" / "worksheets.json"
    reviews_json = REPO_ROOT / "resources" / "seelig" / "folio_reviews.json"

    assert topics_json.exists()
    assert worksheets_json.exists()
    assert reviews_json.exists()

    manifest = json.loads(topics_json.read_text(encoding="utf-8"))
    assert manifest["total_topics"] == 55
    assert manifest["total_folios"] == 353

    ws_data = json.loads(worksheets_json.read_text(encoding="utf-8"))
    assert len(ws_data["workbooks"]["Triangles and Circles.ods"]) == 59

    # Verify 3-Track Book Codex in docsrc/topics/
    topics_index = REPO_ROOT / "docsrc" / "topics" / "index.rst"
    assert topics_index.exists()
    assert ":layout: book" in topics_index.read_text(encoding="utf-8")

    for num in range(1, 56):
        t_dir = REPO_ROOT / "docsrc" / "topics" / f"f-{num:02d}"
        assert (t_dir / "index.rst").exists()
        assert (t_dir / "folios.rst").exists()
        assert (t_dir / "code.rst").exists()
        assert (t_dir / "model.py").exists()
        assert (t_dir / f"f-{num:02d}.svg").exists()
