"""Archival ingestion pipeline for Fred W. Seelig's notebooks and spreadsheets.

Migrates the 55 handwritten topic folders (353 scanned `.jpg` pages) into a
normalized `resources/seelig/<NN_slug>/` hierarchy with sequential 4-digit
folio identifiers (`0001` through `0353`), generates diplomatic `<NNNN>.rst`
and `<NNNN>.notes.rst` files compatible with `publish folio`, migrates the
OpenDocument Spreadsheets into `resources/spreadsheets/`, and exports
`resources/topics.json` and `resources/seelig/folio_reviews.json`.
"""

from __future__ import annotations

import json
from pathlib import Path
import shutil

from .apparatus import export_apparatus_json
from .catalog import TOPICS_CATALOG, get_folio_transcription
from .spreadsheets import build_spreadsheets_index


def ingest_archive(repo_root: Path) -> dict[str, object]:
    """Ingest or refresh `resources/seelig/`, `resources/spreadsheets/`, and `resources/*.json`.

    Idempotent: if `pages/` still exists, copies scans and spreadsheets from
    `pages/03.projects/`; otherwise operates directly on the migrated
    `resources/seelig/` and `resources/spreadsheets/` directories.

    Args:
        repo_root: Root directory of `/home/phi/PROJECTS/geometor/fundamentals`.

    Returns:
        Master dictionary written to `resources/topics.json`.
    """
    resources_dir = repo_root / "resources"
    seelig_dir = resources_dir / "seelig"
    spreadsheets_dir = resources_dir / "spreadsheets"
    seelig_dir.mkdir(parents=True, exist_ok=True)
    spreadsheets_dir.mkdir(parents=True, exist_ok=True)

    legacy_topics_dir = repo_root / "pages" / "03.projects" / "02.topics"
    legacy_sheets_dir = repo_root / "pages" / "03.projects" / "03.spreadsheets"

    # 1. Migrate spreadsheets if legacy directory is present
    if legacy_sheets_dir.exists():
        for item in legacy_sheets_dir.iterdir():
            if item.name == "chapter.md":
                continue
            dest = spreadsheets_dir / item.name
            if item.is_dir():
                shutil.copytree(item, dest, dirs_exist_ok=True)
                marker = dest / "default.md"
                if marker.exists():
                    marker.unlink()
            elif item.is_file():
                shutil.copy2(item, dest)

    # 2. Parse spreadsheets into resources/spreadsheets/worksheets.json
    build_spreadsheets_index(
        spreadsheets_dir=spreadsheets_dir,
        output_json=spreadsheets_dir / "worksheets.json",
    )

    # 3. Export scholarly apparatus JSONs
    export_apparatus_json(resources_dir)

    # 4. Ingest 55 topics and 353 folios
    folio_counter = 1
    topics_manifest: list[dict[str, object]] = []
    folio_reviews: dict[str, dict[str, object]] = {}

    for topic in TOPICS_CATALOG:
        num = int(topic["num"])
        topic_id = str(topic["id"])
        slug = str(topic["slug"])
        legacy_folder = str(topic["legacy_folder"])
        title = str(topic["title"])
        folder_name = f"{num:02d}_{slug}"
        target_topic_dir = seelig_dir / folder_name
        target_topic_dir.mkdir(parents=True, exist_ok=True)

        src_dir = legacy_topics_dir / legacy_folder
        source_images: list[Path] = []
        if src_dir.exists():
            source_images = sorted(
                p
                for p in src_dir.iterdir()
                if p.suffix.lower() in {".jpg", ".jpeg", ".png"}
            )

        existing_folios = sorted(
            p for p in target_topic_dir.glob("[0-9][0-9][0-9][0-9].jpg")
        )

        topic_folios: list[dict[str, object]] = []
        count = len(source_images) if source_images else len(existing_folios)

        for local_idx in range(1, count + 1):
            folio_id = f"{folio_counter:04d}"
            dest_img = target_topic_dir / f"{folio_id}.jpg"
            orig_name = f"{slug}-{local_idx:03d}.jpg"

            if source_images:
                src_img = source_images[local_idx - 1]
                orig_name = src_img.name
                if not dest_img.exists():
                    shutil.copy2(src_img, dest_img)
            elif existing_folios and local_idx - 1 < len(existing_folios):
                orig_name = existing_folios[local_idx - 1].name

            folio_data = get_folio_transcription(
                topic=topic,
                folio_id=folio_id,
                page_index=local_idx,
                total_pages=count,
                original_filename=orig_name,
            )

            # Write <NNNN>.rst for `publish folio`
            rst_path = target_topic_dir / f"{folio_id}.rst"
            rst_lines = [
                f".. folio:: {folio_id}",
                f"   :topic: {topic_id}",
                f"   :title: {folio_data['heading']}",
                f"   :source: {orig_name}",
                "",
                str(folio_data["diplomatic_rst"]),
                "",
            ]
            rst_path.write_text("\n".join(rst_lines), encoding="utf-8")

            # Write <NNNN>.notes.rst for `publish folio`
            notes_path = target_topic_dir / f"{folio_id}.notes.rst"
            notes_lines = [
                f"**Editorial & Symbolic Notes — Folio {folio_id}**",
                "",
                str(folio_data["notes_rst"]),
                "",
            ]
            notes_path.write_text("\n".join(notes_lines), encoding="utf-8")

            folio_entry = {
                "folio_id": folio_id,
                "page_index": local_idx,
                "original_filename": orig_name,
                "relative_image": f"seelig/{folder_name}/{folio_id}.jpg",
                "heading": folio_data["heading"],
                "diplomatic_rst": folio_data["diplomatic_rst"],
                "notes_rst": folio_data["notes_rst"],
            }
            topic_folios.append(folio_entry)
            folio_reviews[folio_id] = {
                "folio_id": folio_id,
                "topic_id": topic_id,
                "topic_title": title,
                "folder": folder_name,
                "original_filename": orig_name,
                "status": "verified",
            }
            folio_counter += 1

        topic_record = {
            **topic,
            "archive_folder": f"resources/seelig/{folder_name}",
            "folio_count": len(topic_folios),
            "folio_range": (
                f"{topic_folios[0]['folio_id']}–{topic_folios[-1]['folio_id']}"
                if topic_folios
                else ""
            ),
            "folios": topic_folios,
        }
        topics_manifest.append(topic_record)

    reviews_path = seelig_dir / "folio_reviews.json"
    reviews_path.write_text(
        json.dumps(folio_reviews, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    manifest_payload: dict[str, object] = {
        "total_topics": len(topics_manifest),
        "total_folios": folio_counter - 1,
        "topics": topics_manifest,
    }
    (resources_dir / "topics.json").write_text(
        json.dumps(manifest_payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return manifest_payload
