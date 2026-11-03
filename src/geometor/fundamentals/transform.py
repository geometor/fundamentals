"""3-Track Book Codex compiler for GEOMETOR Fundamentals (`docsrc/topics/`).

Compiles the 55 topics (`F.1` through `F.55`) into Sphinx ReStructuredText
folders (`docsrc/topics/f-01/` through `docsrc/topics/f-55/`) with:

- Track 1 (`index.rst`): Mathematical synthesis, `.. enunciation::`, interactive
  Explorer SVG (`f-NN.svg`), `.. signature::` block, SymPy derivations, cross-repo
  links (`euclid`, `elements`, `etc`), spreadsheet dropdowns, and Graphviz DAG.
- Track 2 (`folios.rst`): Fred W. Seelig's scanned notebook pages (`<NNNN>.jpg`)
  paired with `.. folio:: <NNNN>` diplomatic transcriptions and editorial notes.
- Track 3 (`code.rst`): Executable `geometor.model` / SymPy script (`model.py`).
"""

from __future__ import annotations

import json
from pathlib import Path
import shutil

from .apparatus import enrich_text, generate_apparatus_rst
from .catalog import TOPICS_CATALOG
from .spreadsheets import format_sheet_rst_dropdown, generate_spreadsheets_rst


def _build_reverse_dependencies(
    topics: list[dict[str, object]],
) -> dict[str, list[dict[str, object]]]:
    """Compute reverse dependency list (`required_for`) for each topic ID.

    Args:
        topics: List of topic dictionaries from `TOPICS_CATALOG`.

    Returns:
        Mapping from `F.<k>` to list of dependent topic dictionaries.
    """
    by_id = {str(t["id"]): t for t in topics}
    rev: dict[str, list[dict[str, object]]] = {str(t["id"]): [] for t in topics}
    for t in topics:
        for dep_id in t.get("depends_on", []):  # type: ignore[union-attr]
            dep_str = str(dep_id)
            if dep_str in rev and dep_str in by_id:
                rev[dep_str].append(t)
    return rev


def _render_graphviz_dag(
    topic: dict[str, object],
    by_id: dict[str, dict[str, object]],
    required_for: list[dict[str, object]],
) -> list[str]:
    """Generate a `.. graphviz::` block for a topic's internal dependency DAG.

    Args:
        topic: Current topic dictionary.
        by_id: Lookup mapping from topic ID (`F.N`) to topic dictionary.
        required_for: List of topics that depend on `topic`.

    Returns:
        List of RST lines containing the `.. graphviz::` directive.
    """
    tid = str(topic["id"])
    t_num = int(topic["num"])
    t_title = str(topic["title"]).replace('"', "'")
    deps = [str(d) for d in topic.get("depends_on", []) if str(d) in by_id]  # type: ignore[union-attr]

    lines: list[str] = [
        ".. graphviz::",
        "",
        "   digraph dependency {",
        "       rankdir=TB;",
        '       bgcolor="transparent";',
        '       node [fontname="Helvetica,Arial,sans-serif", fontsize=10, shape=box, style="rounded,filled", margin="0.15,0.08"];',
        '       edge [color="#888888", arrowsize=0.7];',
        f'       "{tid}" [label="{tid}\\n{t_title}", fillcolor="#ffff99", color="#d4a017", penwidth=2.0, URL="../f-{t_num:02d}/index.html"];',
    ]

    for dep_id in deps:
        d_obj = by_id[dep_id]
        d_num = int(d_obj["num"])
        d_title = str(d_obj["title"]).replace('"', "'")
        lines.append(
            f'       "{dep_id}" [label="{dep_id}\\n{d_title}", fillcolor="#90ee90", color="#2e8b57", URL="../f-{d_num:02d}/index.html"];'
        )
        lines.append(f'       "{dep_id}" -> "{tid}";')

    for child in required_for[:8]:
        c_id = str(child["id"])
        c_num = int(child["num"])
        c_title = str(child["title"]).replace('"', "'")
        lines.append(
            f'       "{c_id}" [label="{c_id}\\n{c_title}", fillcolor="#e0e0e0", color="#777777", URL="../f-{c_num:02d}/index.html"];'
        )
        lines.append(f'       "{tid}" -> "{c_id}";')

    lines.extend(["   }", ""])
    return lines


def generate_codex(repo_root: Path) -> None:
    """Compile the complete Sphinx `docsrc/` Book Codex, spreadsheets, and apparatus.

    Args:
        repo_root: Root directory of `/home/phi/PROJECTS/geometor/fundamentals`.
    """
    from .construct import build_topic_model, generate_topic_model_code
    from .render import render_svg

    resources_dir = repo_root / "resources"
    docsrc_dir = repo_root / "docsrc"
    topics_dir = docsrc_dir / "topics"
    topics_dir.mkdir(parents=True, exist_ok=True)

    topics_json_path = resources_dir / "topics.json"
    if topics_json_path.exists():
        manifest = json.loads(topics_json_path.read_text(encoding="utf-8"))
        topics_list: list[dict[str, object]] = list(manifest.get("topics", []))
    else:
        topics_list = list(TOPICS_CATALOG)

    worksheets_json_path = resources_dir / "spreadsheets" / "worksheets.json"
    spreadsheets_payload: dict[str, object] = {}
    sheets_by_name: dict[str, dict[str, object]] = {}
    if worksheets_json_path.exists():
        spreadsheets_payload = json.loads(
            worksheets_json_path.read_text(encoding="utf-8")
        )
        raw_sheets = spreadsheets_payload.get("sheets", {})
        if isinstance(raw_sheets, dict):
            sheets_by_name = raw_sheets

    by_id = {str(t["id"]): t for t in topics_list}
    rev_deps = _build_reverse_dependencies(topics_list)

    sheet_to_topics: dict[str, list[tuple[str, str]]] = {}
    for t in topics_list:
        tid = str(t["id"])
        ttitle = str(t["title"])
        for sh_name in t.get("spreadsheets", []):  # type: ignore[union-attr]
            sheet_to_topics.setdefault(str(sh_name), []).append((tid, ttitle))

    # 1. Generate apparatus RSTs (glossary.rst, persons.rst, bibliography.rst)
    generate_apparatus_rst(docsrc_dir)

    # 2. Generate spreadsheets RST (docsrc/spreadsheets/index.rst)
    generate_spreadsheets_rst(spreadsheets_payload, sheet_to_topics, docsrc_dir)

    # 3. Generate per-topic 3-Track Book Codex folders (docsrc/topics/f-01 .. f-55)
    for topic in topics_list:
        num = int(topic["num"])
        tid = str(topic["id"])
        slug_dir = f"f-{num:02d}"
        t_dir = topics_dir / slug_dir
        t_dir.mkdir(parents=True, exist_ok=True)

        title = str(topic["title"])
        subtitle = str(topic["subtitle"])
        category = str(topic["category"])
        tags_list = [str(x) for x in topic.get("tags", [])]  # type: ignore[union-attr]
        enunciation = str(topic["enunciation"])
        sig_given = [str(x) for x in topic.get("signature_given", [])]  # type: ignore[union-attr]
        sig_steps = [str(x) for x in topic.get("signature_steps", [])]  # type: ignore[union-attr]
        synthesis_blocks = [str(x) for x in topic.get("synthesis", [])]  # type: ignore[union-attr]
        equations = [str(x) for x in topic.get("equations", [])]  # type: ignore[union-attr]
        euclid_refs = [str(x) for x in topic.get("euclid_refs", [])]  # type: ignore[union-attr]
        elements_refs = [str(x) for x in topic.get("elements_refs", [])]  # type: ignore[union-attr]
        etc_refs = [str(x) for x in topic.get("etc_refs", [])]  # type: ignore[union-attr]
        sheet_names = [str(x) for x in topic.get("spreadsheets", [])]  # type: ignore[union-attr]
        folios = list(topic.get("folios", []))  # type: ignore[arg-type]

        # Build model, SVG, and model.py
        model, extra_curves = build_topic_model(num, title)
        svg_filename = f"{slug_dir}.svg"
        render_svg(model, t_dir / svg_filename, extra_curves=extra_curves)

        model_code = generate_topic_model_code(num, title, enunciation)
        (t_dir / "model.py").write_text(model_code, encoding="utf-8")

        # ------------------------------------------------------------------
        # Track 1: index.rst (Synthesis)
        # ------------------------------------------------------------------
        heading = f"{tid} {title}"
        overline = "=" * len(heading)
        seen_terms: set[str] = set()
        seen_persons: set[str] = set()

        safe_enunciation = enunciation.replace("|", r"\|")
        idx_lines: list[str] = [
            f":order: {num}",
            ":type: topic",
            f":category: {category}",
            f":tags: {', '.join(tags_list)}",
            "",
            f".. _{slug_dir}:",
            "",
            overline,
            heading,
            overline,
            "",
            f"*{subtitle}*",
            "",
            ".. enunciation::",
            "",
            f"   {safe_enunciation}",
            "",
            f".. figure:: {svg_filename}",
            "   :align: center",
            "   :width: 100%",
            "",
            f"   Interactive GEOMETOR construction for **{tid} ({title})**. "
            "Hover any geometric label in the text or figure to highlight the corresponding element.",
            "",
            ".. signature::",
            "",
        ]
        for g_line in sig_given:
            idx_lines.append(f"   {g_line}")
        idx_lines.append("   =====")
        for s_line in sig_steps:
            idx_lines.append(f"   {s_line}")
        idx_lines.extend(["", "Mathematical Synthesis", "----------------------", ""])

        for para in synthesis_blocks:
            idx_lines.append(enrich_text(para, seen_terms, seen_persons))
            idx_lines.append("")

        if equations:
            idx_lines.extend(
                ["Key Algebraic Identities", "------------------------", ""]
            )
            for eq in equations:
                idx_lines.append(".. math::")
                idx_lines.append("")
                for eq_line in eq.splitlines():
                    idx_lines.append(f"   {eq_line}")
                idx_lines.append("")

        # Cross-Repository Canon Links
        idx_lines.extend(
            [
                "Cross-Repository Canon & Archival Provenance",
                "--------------------------------------------",
                "",
                ".. list-table::",
                "   :widths: 28 72",
                "",
                "   * - **Seelig Archive Folios**",
                f"     - :doc:`folios` (Folios ``{topic.get('folio_range', '')}``, "
                f"{len(folios)} scanned manuscript page{'s' if len(folios) != 1 else ''} in ``{topic.get('archive_folder', '')}``)",
                "   * - **Euclid's Elements**",
                f"     - {', '.join(f':ref:`{r}`' for r in euclid_refs) if euclid_refs else 'Classical Euclidean synthesis'} (:cite:`EuclidElements`)",
                "   * - **GEOMETOR Elements (G-Index)**",
                f"     - {', '.join(f':ref:`{g}`' for g in elements_refs) if elements_refs else 'Foundational construction'}",
                "   * - **Encyclopedia of Triangle Centers**",
                f"     - {', '.join(f':ref:`{x}`' for x in etc_refs) if etc_refs else 'General projective / metric locus'} (:cite:`Kimberling1998`)",
                "   * - **Seelig Spreadsheets**",
                f"     - {', '.join(f'``{s}``' for s in sheet_names) if sheet_names else 'General Reference'} (:ref:`Spreadsheets <spreadsheets>`)",
                "",
            ]
        )

        # Spreadsheet Dropdowns
        matched_sheets = [
            sheets_by_name[sh] for sh in sheet_names if sh in sheets_by_name
        ]
        if matched_sheets:
            idx_lines.extend(
                [
                    "Computational Workbook Verification",
                    "-----------------------------------",
                    "",
                    "The following worksheets from :person:`seelig`'s ``Triangles and Circles.ods``",
                    "workbook verify the numerical and symbolic formulas for this topic on",
                    "the canonical :math:`(a, b, c) = (5, 6, 7)` triangle:",
                    "",
                ]
            )
            for sh_dict in matched_sheets:
                idx_lines.extend(
                    format_sheet_rst_dropdown(sh_dict, open_by_default=False)
                )

        # Dependency DAG
        idx_lines.extend(
            [
                "Constructive Dependency Graph",
                "-----------------------------",
                "",
            ]
        )
        req_for = rev_deps.get(tid, [])
        idx_lines.extend(_render_graphviz_dag(topic, by_id, req_for))

        deps_list = [str(d) for d in topic.get("depends_on", []) if str(d) in by_id]  # type: ignore[union-attr]
        if deps_list:
            dep_links = ", ".join(
                f":ref:`{d} {by_id[d]['title']} <f-{int(by_id[d]['num']):02d}>`"
                for d in deps_list
            )
            idx_lines.append(f"**Prerequisites**: {dep_links}")
            idx_lines.append("")

        if req_for:
            req_links = ", ".join(
                f":ref:`{c['id']} {c['title']} <f-{int(c['num']):02d}>`"
                for c in req_for
            )
            idx_lines.append(f"**Required for**: {req_links}")
            idx_lines.append("")

        idx_lines.extend(
            [
                ".. toctree::",
                "   :hidden:",
                "",
                "   folios",
                "   code",
                "",
            ]
        )
        (t_dir / "index.rst").write_text("\n".join(idx_lines), encoding="utf-8")

        # ------------------------------------------------------------------
        # Track 2: folios.rst (Folios)
        # ------------------------------------------------------------------
        f_heading = f"{tid} {title} — Folios"
        f_overline = "=" * len(f_heading)
        f_lines: list[str] = [
            f_overline,
            f_heading,
            f_overline,
            "",
            f"Archival manuscript scans and diplomatic transcriptions from :person:`seelig`'s",
            f"notebooks for **{tid} ({title})** (:cite:`SeeligNotebooks`).",
            "",
        ]

        for f_entry in folios:
            if not isinstance(f_entry, dict):
                continue
            fid = str(f_entry["folio_id"])
            p_idx = int(f_entry["page_index"])
            orig_fn = str(f_entry["original_filename"])
            rel_img = str(f_entry["relative_image"])
            f_head = str(f_entry["heading"])
            dip_rst = str(f_entry["diplomatic_rst"])
            notes_rst = str(f_entry["notes_rst"])

            src_jpg = resources_dir / rel_img
            dst_jpg = t_dir / f"{fid}.jpg"
            if src_jpg.exists() and not dst_jpg.exists():
                shutil.copy2(src_jpg, dst_jpg)

            sub_h = f"Folio {fid} (Page {p_idx} of {len(folios)}): {f_head}"
            f_lines.extend(
                [
                    sub_h,
                    "-" * len(sub_h),
                    "",
                    f".. folio:: {fid}",
                    "",
                    f".. figure:: {fid}.jpg",
                    "   :align: center",
                    "   :width: 92%",
                    "",
                    f"   Folio ``{fid}`` (original scan ``{orig_fn}``) from ``{topic.get('archive_folder', '')}``.",
                    "",
                    "**Diplomatic Mathematical & Geometric Transcription**",
                    "",
                    dip_rst,
                    "",
                    ".. admonition:: Editorial & Symbolic Notes",
                    "",
                ]
            )
            for n_line in notes_rst.splitlines():
                f_lines.append(f"   {n_line}" if n_line.strip() else "")
            f_lines.append("")

        (t_dir / "folios.rst").write_text("\n".join(f_lines), encoding="utf-8")

        # ------------------------------------------------------------------
        # Track 3: code.rst (Code)
        # ------------------------------------------------------------------
        c_heading = f"{tid} {title} — Code"
        c_overline = "=" * len(c_heading)
        c_lines: list[str] = [
            c_overline,
            c_heading,
            c_overline,
            "",
            ".. enunciation::",
            "",
            f"   {safe_enunciation}",
            "",
            f".. figure:: {svg_filename}",
            "   :align: center",
            "   :width: 88%",
            "",
            f"   Output of ``model.py`` for **{tid} ({title})**.",
            "",
            "Symbolic Construction Script (``model.py``)",
            "-------------------------------------------",
            "",
            ".. literalinclude:: model.py",
            "   :language: python",
            "",
        ]
        (t_dir / "code.rst").write_text("\n".join(c_lines), encoding="utf-8")

    # 4. Generate docsrc/topics/index.rst (Book Codex Collection Index)
    _generate_topics_index_rst(topics_dir, topics_list)


def _generate_topics_index_rst(
    topics_dir: Path,
    topics_list: list[dict[str, object]],
) -> None:
    """Write `docsrc/topics/index.rst` with `:layout: book` and the 55-topic master table.

    Args:
        topics_dir: Path to `docsrc/topics/`.
        topics_list: List of 55 topic dictionaries.
    """
    lines: list[str] = [
        ":layout: book",
        ":navigation: header",
        ":order: 10",
        "",
        ".. _topics:",
        "",
        "======",
        "Topics",
        "======",
        "",
        "The **GEOMETOR Fundamentals Codex** synthesizes **55 foundational topics**",
        "(:math:`\\text{F.1}` through :math:`\\text{F.55}`) across **353 manuscript folios**",
        "and **59 computational worksheets** compiled by :person:`seelig` (:cite:`SeeligNotebooks`,",
        ":cite:`SeeligSpreadsheets`).",
        "",
        "Each topic is organized as a **3-Track Book Codex**:",
        "",
        "- **Track 1 — Synthesis**: Formal enunciation, interactive Explorer SVG",
        "  construction, constructive signature (`given` / `steps`), symbolic SymPy",
        "  derivations on the canonical :math:`(a, b, c) = (5, 6, 7)` triangle,",
        "  OpenDocument spreadsheet formulas, and Graphviz dependency DAG.",
        "- **Track 2 — Folios**: High-resolution archival scans (``0001.jpg``–``0353.jpg``)",
        "  paired with diplomatic mathematical transcriptions and editorial commentary.",
        "- **Track 3 — Code**: Standalone executable Python script (``model.py``) using",
        "  ``geometor.model`` and ``sympy``.",
        "",
        ".. collection::",
        "   :type: topic",
        "   :sort: order",
        "",
        "Master Index of Topics (F.1 – F.55)",
        "-----------------------------------",
        "",
        ".. list-table::",
        "   :widths: 9 29 22 14 26",
        "   :header-rows: 1",
        "",
        "   * - ID",
        "     - Topic",
        "     - Category",
        "     - Folios",
        "     - Canon Links (Euclid / Elements / ETC)",
    ]

    for t in topics_list:
        num = int(t["num"])
        tid = str(t["id"])
        title = str(t["title"])
        cat = str(t["category"])
        f_range = str(t.get("folio_range", ""))
        f_cnt = int(t.get("folio_count", 0))
        canon_parts: list[str] = []
        for e in list(t.get("euclid_refs", []))[:2]:  # type: ignore[arg-type]
            canon_parts.append(str(e))
        for g in list(t.get("elements_refs", []))[:2]:  # type: ignore[arg-type]
            canon_parts.append(str(g))
        for x in list(t.get("etc_refs", []))[:2]:  # type: ignore[arg-type]
            canon_parts.append(str(x))
        canon_str = ", ".join(f"``{c}``" for c in canon_parts) if canon_parts else "—"
        lines.extend(
            [
                f"   * - :ref:`{tid} <f-{num:02d}>`",
                f"     - :ref:`{title} <f-{num:02d}>`",
                f"     - {cat}",
                f"     - ``{f_range}`` ({f_cnt})",
                f"     - {canon_str}",
            ]
        )

    lines.append("")
    (topics_dir / "index.rst").write_text("\n".join(lines), encoding="utf-8")
