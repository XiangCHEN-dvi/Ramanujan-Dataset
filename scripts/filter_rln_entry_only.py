#!/usr/bin/env python3
"""Keep only formal Entry records in scripts/entries/rln_p1_chNN.py modules."""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES = ROOT / "scripts" / "entries"
ENTRY_ID = re.compile(r"^RLN-P\d+-C\d+-Entry\d+-\d+-\d+$")


def py_str(s: str) -> str:
    return __import__("json").dumps(s, ensure_ascii=False)


def write_module(path: Path, chapter: int, records: list[dict], topic_slug: str) -> None:
    part = 1
    var = f"CHAPTER_{chapter}"
    topics_var = f"TOPICS_C{chapter:02d}"
    lines = [
        f'"""RLN Part {part}, Chapter {chapter} — AI curated LaTeX (Entry only)."""',
        "",
        "from __future__ import annotations",
        "",
        f"{topics_var} = [{py_str(topic_slug)}]",
        "",
        "",
        "def rec(entry_id: str, content: str) -> dict:",
        f'    return {{"id": entry_id, "content": content, "topics": {topics_var}}}',
        "",
        "",
        f"{var} = [",
    ]
    for record in records:
        lines.append(f"    rec({py_str(record['id'])}, {py_str(record['content'])}),")
    lines.append("]")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def load_chapter(path: Path, chapter: int) -> list[dict]:
    spec = importlib.util.spec_from_file_location(f"rln_ch{chapter}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(ENTRIES))
    spec.loader.exec_module(module)
    return list(getattr(module, f"CHAPTER_{chapter}"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapter", type=int, nargs="*", help="Chapters to filter (default: all)")
    args = parser.parse_args()

    chapters = args.chapter or list(range(1, 19))
    total_before = total_after = 0

    for chapter in chapters:
        path = ENTRIES / f"rln_p1_ch{chapter:02d}.py"
        if not path.exists():
            print(f"Skip missing {path.name}")
            continue
        records = load_chapter(path, chapter)
        kept = [r for r in records if ENTRY_ID.match(r["id"])]
        if not kept and chapter != 10:
            print(f"Ch.{chapter}: {len(records)} -> 0 (empty after filter)")
        else:
            print(f"Ch.{chapter}: {len(records)} -> {len(kept)}")
        total_before += len(records)
        total_after += len(kept)
        if kept:
            slug = kept[0]["topics"][0]
            write_module(path, chapter, kept, slug)

    print(f"Total: {total_before} -> {total_after}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
