"""OpenDocument Spreadsheet (.ods) parser and RST generator for the Seelig archive.

Extracts worksheet metadata, cell values, and OpenFormula expressions from
Fred W. Seelig's computational geometry workbooks (`Triangles and Circles.ods`,
`circumcircle-circumcenter.ods`, and `triangle-basics-draw.ods`) and compiles
both structured JSON (`resources/spreadsheets/worksheets.json`) and Sphinx
ReStructuredText documentation (`docsrc/spreadsheets/index.rst`).
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile

ODS_NS: dict[str, str] = {
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
}


def clean_formula(formula: str) -> str:
    """Normalize an OpenFormula string into clean human-readable notation.

    Args:
        formula: Raw `table:formula` attribute from an `.ods` cell.

    Returns:
        Cleaned formula string starting with `=`.
    """
    if not formula:
        return ""
    cleaned = formula
    if cleaned.startswith("of:="):
        cleaned = "=" + cleaned[4:]
    elif cleaned.startswith("oooc:="):
        cleaned = "=" + cleaned[6:]
    cleaned = re.sub(r"\[\.([A-Z]+\d+)\]", r"\1", cleaned)
    cleaned = re.sub(r"\[\.([A-Z]+\d+):\.([A-Z]+\d+)\]", r"\1:\2", cleaned)
    cleaned = re.sub(r"\[\$([^.\]]+)\.([A-Z]+\d+)\]", r"\1!\2", cleaned)
    return cleaned


def parse_ods_file(
    ods_path: Path,
    max_rows: int = 45,
    max_cols: int = 12,
) -> list[dict[str, object]]:
    """Parse an OpenDocument Spreadsheet (`.ods`) into worksheet dictionaries.

    Args:
        ods_path: Path to the `.ods` file on disk.
        max_rows: Maximum number of rows to inspect per sheet.
        max_cols: Maximum number of columns to inspect per row.

    Returns:
        List of dictionaries describing each worksheet, its dimensions,
        extracted formulas, and preview table rows.
    """
    sheets: list[dict[str, object]] = []
    if not ods_path.exists():
        return sheets

    with zipfile.ZipFile(ods_path, "r") as archive:
        xml_bytes = archive.read("content.xml")
    root = ET.fromstring(xml_bytes)

    for idx, table in enumerate(root.findall(".//table:table", ODS_NS), start=1):
        sheet_name = table.attrib.get(f"{{{ODS_NS['table']}}}name", f"Sheet_{idx}")
        rows_el = table.findall("table:table-row", ODS_NS)
        preview_rows: list[list[str]] = []
        formulas: list[dict[str, str]] = []
        non_empty_row_count = 0

        for r_idx, row_el in enumerate(rows_el[:max_rows], start=1):
            row_cells: list[str] = []
            col_cursor = 0
            for cell in row_el.findall("table:table-cell", ODS_NS):
                repeat = int(
                    cell.attrib.get(
                        f"{{{ODS_NS['table']}}}number-columns-repeated", "1"
                    )
                )
                texts = [
                    "".join(p.itertext()).strip()
                    for p in cell.findall("text:p", ODS_NS)
                ]
                val = " ".join(t for t in texts if t)
                raw_formula = cell.attrib.get(f"{{{ODS_NS['table']}}}formula", "")
                cleaned_f = clean_formula(raw_formula)

                cell_display = val
                if cleaned_f and len(formulas) < 16:
                    col_letter = chr(65 + min(col_cursor, 25))
                    cell_ref = f"{col_letter}{r_idx}"
                    label = row_cells[-1] if row_cells and row_cells[-1] else cell_ref
                    formulas.append(
                        {
                            "cell": cell_ref,
                            "label": label[:40],
                            "value": val[:32],
                            "formula": cleaned_f[:80],
                        }
                    )
                for _ in range(min(repeat, max_cols - col_cursor)):
                    if col_cursor >= max_cols:
                        break
                    row_cells.append(cell_display)
                    col_cursor += 1
                if col_cursor >= max_cols:
                    break

            while row_cells and not row_cells[-1]:
                row_cells.pop()
            if any(row_cells):
                non_empty_row_count += 1
                if len(preview_rows) < 12:
                    preview_rows.append(row_cells[:8])

        sheets.append(
            {
                "index": idx,
                "name": sheet_name,
                "workbook": ods_path.name,
                "non_empty_rows": non_empty_row_count,
                "formulas": formulas[:10],
                "preview_rows": preview_rows,
            }
        )
    return sheets


def build_spreadsheets_index(
    spreadsheets_dir: Path,
    output_json: Path,
) -> dict[str, object]:
    """Parse all `.ods` workbooks in `spreadsheets_dir` and write `worksheets.json`.

    Args:
        spreadsheets_dir: Directory containing migrated `.ods` files.
        output_json: Destination path for `worksheets.json`.

    Returns:
        Dictionary mapping workbook names and worksheet names to extracted data.
    """
    workbooks: dict[str, list[dict[str, object]]] = {}
    by_sheet_name: dict[str, dict[str, object]] = {}

    ods_files = [
        spreadsheets_dir / "Triangles and Circles.ods",
        spreadsheets_dir / "00.triangle-basics" / "circumcircle-circumcenter.ods",
        spreadsheets_dir / "00.triangle-basics" / "triangle-basics-draw.ods",
    ]
    for ods_path in ods_files:
        if ods_path.exists():
            parsed = parse_ods_file(ods_path)
            workbooks[ods_path.name] = parsed
            for sheet in parsed:
                name_str = str(sheet["name"])
                if name_str not in by_sheet_name:
                    by_sheet_name[name_str] = sheet

    payload: dict[str, object] = {
        "workbooks": workbooks,
        "sheets": by_sheet_name,
    }
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return payload


def format_sheet_rst_dropdown(
    sheet: dict[str, object],
    open_by_default: bool = False,
) -> list[str]:
    """Render a collapsible RST `.. dropdown::` summarizing a single worksheet.

    Args:
        sheet: Parsed worksheet dictionary from :func:`parse_ods_file`.
        open_by_default: Whether to add `:open:` to the dropdown directive.

    Returns:
        List of RST lines representing the collapsible worksheet table.
    """
    name = str(sheet.get("name", "Sheet"))
    workbook = str(sheet.get("workbook", "Triangles and Circles.ods"))
    formulas = list(sheet.get("formulas", []))  # type: ignore[arg-type]
    preview_rows = list(sheet.get("preview_rows", []))  # type: ignore[arg-type]

    lines: list[str] = [
        f".. admonition:: Worksheet: ``{name}`` (*{workbook}*)",
        "",
    ]

    if formulas:
        lines.append("   **Key Formulas & Parameters**")
        lines.append("")
        lines.append("   .. list-table::")
        lines.append("      :widths: 12 28 20 40")
        lines.append("      :header-rows: 1")
        lines.append("")
        lines.append("      * - Cell")
        lines.append("        - Label / Context")
        lines.append("        - Value")
        lines.append("        - OpenFormula")
        for f_item in formulas[:8]:
            if isinstance(f_item, dict):
                cell = str(f_item.get("cell", "")).replace("`", "'")
                label = (
                    str(f_item.get("label", "")).replace("`", "'").replace("|", r"\|")
                )
                val = str(f_item.get("value", "")).replace("`", "'")
                form = str(f_item.get("formula", "")).replace("`", "'")
                lines.append(f"      * - ``{cell}``")
                lines.append(f"        - {label or '—'}")
                lines.append(f"        - ``{val}``" if val else "        - —")
                lines.append(f"        - ``{form}``")
        lines.append("")

    if preview_rows:
        max_cols = max((len(r) for r in preview_rows if isinstance(r, list)), default=0)
        max_cols = min(max(max_cols, 1), 6)
        lines.append("   **Cell Excerpt**")
        lines.append("")
        lines.append("   .. list-table::")
        lines.append("")
        for r in preview_rows[:6]:
            if not isinstance(r, list):
                continue
            padded = [
                str(c).replace("`", "'").replace("|", r"\|")[:36] for c in r[:max_cols]
            ]
            while len(padded) < max_cols:
                padded.append("")
            for c_idx, cell_text in enumerate(padded):
                prefix = "      * - " if c_idx == 0 else "        - "
                lines.append(f"{prefix}{cell_text if cell_text else '—'}")
        lines.append("")

    if not formulas and not preview_rows:
        lines.append("   *Auxiliary layout or scratch worksheet in workbook.*")
        lines.append("")

    return lines


def generate_spreadsheets_rst(
    spreadsheets_payload: dict[str, object],
    sheet_to_topics: dict[str, list[tuple[str, str]]],
    docsrc_dir: Path,
) -> Path:
    """Generate `docsrc/spreadsheets/index.rst` documenting all Seelig workbooks.

    Args:
        spreadsheets_payload: Dictionary returned by :func:`build_spreadsheets_index`.
        sheet_to_topics: Mapping of worksheet name to list of `(topic_id, title)`.
        docsrc_dir: Path to `docsrc/`.

    Returns:
        Path to the generated `docsrc/spreadsheets/index.rst`.
    """
    target_dir = docsrc_dir / "spreadsheets"
    target_dir.mkdir(parents=True, exist_ok=True)
    out_path = target_dir / "index.rst"

    workbooks = spreadsheets_payload.get("workbooks", {})
    lines: list[str] = [
        ":navigation: header",
        ":order: 25",
        "",
        ".. _spreadsheets:",
        "",
        "============",
        "Spreadsheets",
        "============",
        "",
        "Alongside his 353 handwritten notebook pages, :person:`seelig` constructed",
        "an extensive suite of computational geometry workbooks in OpenDocument",
        "Spreadsheet (``.ods``) format. These sheets test algebraic identities,",
        "verify homogeneous :term:`barycentric coordinates`, and compute exact",
        "and numerical coordinates for the canonical :math:`(a, b, c) = (5, 6, 7)`",
        "reference triangle.",
        "",
        "Workbooks in Archive",
        "--------------------",
        "",
        "1. ``resources/spreadsheets/Triangles and Circles.ods`` — Master workbook",
        "   containing **59 worksheets** spanning triangle centers, circle families,",
        "   harmonic conjugates, projective theorems, and special triangles.",
        "2. ``resources/spreadsheets/00.triangle-basics/circumcircle-circumcenter.ods``",
        "   — Step-by-step derivation of the :term:`circumcenter` and :term:`circumcircle`",
        "   from side lengths :math:`(5, 6, 7)` (also exported as ``.csv``, ``.html``,",
        "   ``.fods``, and ``.xlsx``).",
        "3. ``resources/spreadsheets/00.triangle-basics/triangle-basics-draw.ods`` —",
        "   Coordinate plotting workbook for basic triangle vertices and centers.",
        "",
        "Master Worksheet Index (``Triangles and Circles.ods``)",
        "------------------------------------------------------",
        "",
        ".. list-table::",
        "   :widths: 8 28 14 50",
        "   :header-rows: 1",
        "",
        "   * - #",
        "     - Worksheet",
        "     - Active Rows",
        "     - Linked Codex Topics",
    ]

    tc_sheets = (
        workbooks.get("Triangles and Circles.ods", [])
        if isinstance(workbooks, dict)
        else []
    )
    for sheet in tc_sheets:
        if not isinstance(sheet, dict):
            continue
        idx = sheet.get("index", "")
        name = str(sheet.get("name", ""))
        row_cnt = sheet.get("non_empty_rows", 0)
        linked = sheet_to_topics.get(name, [])
        if linked:
            refs = ", ".join(
                f":ref:`{tid} <f-{int(tid.split('.')[1]):02d}>`" for tid, _ in linked
            )
        else:
            refs = "General Reference"
        lines.extend(
            [
                f"   * - {idx}",
                f"     - ``{name}``",
                f"     - {row_cnt}",
                f"     - {refs}",
            ]
        )

    lines.extend(
        [
            "",
            "Worksheet Formula Inspector",
            "---------------------------",
            "",
            "Expand any worksheet below to inspect its OpenFormula expressions and",
            "computed values.",
            "",
        ]
    )

    for sheet in tc_sheets:
        if isinstance(sheet, dict):
            lines.extend(format_sheet_rst_dropdown(sheet, open_by_default=False))

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_path
