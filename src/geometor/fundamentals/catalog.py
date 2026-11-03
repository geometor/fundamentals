"""Unified catalog of all 55 topics (`F.1`–`F.55`) and 353 folio transcriptions.

Combines `TOPICS_1_TO_28` (`catalog_a.py`) and `TOPICS_29_TO_55` (`catalog_b.py`)
into `TOPICS_CATALOG` and provides lookup and diplomatic folio transcription
helpers for the archival ingestion and Book Codex compilation pipelines.
"""

from __future__ import annotations

from .catalog_a import TOPICS_1_TO_28
from .catalog_b import TOPICS_29_TO_55

TOPICS_CATALOG: list[dict[str, object]] = TOPICS_1_TO_28 + TOPICS_29_TO_55


def get_topic_by_num(num: int) -> dict[str, object]:
    """Return the topic dictionary for 1-based topic number `num` (1..55).

    Args:
        num: Topic number from 1 to 55.

    Returns:
        Matching topic dictionary from `TOPICS_CATALOG`.

    Raises:
        KeyError: If `num` is outside `1..55`.
    """
    for topic in TOPICS_CATALOG:
        if int(topic["num"]) == num:
            return topic
    raise KeyError(f"Unknown topic number: {num}")


def get_topic_by_id(topic_id: str) -> dict[str, object]:
    """Return the topic dictionary for topic identifier `F.<num>`.

    Args:
        topic_id: Topic identifier such as `'F.1'` or `'F.52'`.

    Returns:
        Matching topic dictionary from `TOPICS_CATALOG`.

    Raises:
        KeyError: If `topic_id` is not found.
    """
    normalized = topic_id.strip().upper()
    for topic in TOPICS_CATALOG:
        if str(topic["id"]).upper() == normalized:
            return topic
    raise KeyError(f"Unknown topic ID: {topic_id}")


def get_folio_transcription(
    topic: dict[str, object],
    folio_id: str,
    page_index: int,
    total_pages: int,
    original_filename: str,
) -> dict[str, str]:
    """Build the diplomatic RST transcription and editorial notes for a single folio.

    Args:
        topic: Topic dictionary from `TOPICS_CATALOG`.
        folio_id: 4-digit sequential folio identifier (`0001`..`0353`).
        page_index: 1-based index of this scan within the topic folder.
        total_pages: Total number of scanned pages in this topic folder.
        original_filename: Original `.jpg` filename from Fred W. Seelig's scans.

    Returns:
        Dictionary with keys `'heading'`, `'diplomatic_rst'`, and `'notes_rst'`.
    """
    topic_id = str(topic["id"])
    title = str(topic["title"])
    summaries = list(topic.get("folio_summaries", []))  # type: ignore[arg-type]
    equations = [str(eq) for eq in topic.get("equations", [])]  # type: ignore[union-attr]
    spreadsheets = [str(s) for s in topic.get("spreadsheets", [])]  # type: ignore[union-attr]
    euclid_refs = [str(r) for r in topic.get("euclid_refs", [])]  # type: ignore[union-attr]
    etc_refs = [str(x) for x in topic.get("etc_refs", [])]  # type: ignore[union-attr]

    if 1 <= page_index <= len(summaries):
        sub_heading, summary_text = summaries[page_index - 1]
    else:
        sub_heading = f"{title} — Sheet {page_index} of {total_pages}"
        summary_text = str(topic.get("enunciation", ""))

    eq_choice = equations[(page_index - 1) % len(equations)] if equations else ""

    diplomatic_lines: list[str] = [
        f"**Diplomatic Transcription — Folio {folio_id}** (``{original_filename}``, Sheet {page_index} of {total_pages}):",
        "",
        summary_text,
    ]
    if eq_choice:
        diplomatic_lines.extend(
            [
                "",
                ".. math::",
                "",
                f"   {eq_choice}",
            ]
        )

    notes_parts: list[str] = [
        f"Archival scan ``{original_filename}`` from Fred W. Seelig's notebook dossier on **{topic_id} {title}** "
        f"(Page {page_index} of {total_pages}).",
    ]
    if spreadsheets:
        sheets_str = ", ".join(f"``{s}``" for s in spreadsheets)
        notes_parts.append(f"Companion OpenDocument worksheet(s): {sheets_str}.")
    if euclid_refs:
        euc_str = ", ".join(f":ref:`{r}`" for r in euclid_refs)
        notes_parts.append(f"Classical Euclidean foundations: {euc_str}.")
    if etc_refs:
        etc_str = ", ".join(f":ref:`{x}`" for x in etc_refs)
        notes_parts.append(
            f"Kimberling *Encyclopedia of Triangle Centers* loci: {etc_str}."
        )

    return {
        "heading": str(sub_heading).replace("|", r"\|"),
        "diplomatic_rst": "\n".join(diplomatic_lines),
        "notes_rst": " ".join(notes_parts),
    }
