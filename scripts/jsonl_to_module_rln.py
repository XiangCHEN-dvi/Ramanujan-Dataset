#!/usr/bin/env python3
"""Generate scripts/entries/rln_pN_chNN.py from RLN OCR draft JSONL."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DRAFTS = ROOT / "drafts"
ENTRIES = ROOT / "scripts" / "entries"


def py_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def write_module(part: int, chapter: int, records: list[dict], topic_slug: str) -> Path:
    var = f"CHAPTER_{chapter}"
    topics_var = f"TOPICS_C{chapter:02d}"
    out = ENTRIES / f"rln_p{part}_ch{chapter:02d}.py"
    lines = [
        f'"""RLN Part {part}, Chapter {chapter} — AI curated LaTeX."""',
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
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Bootstrap RLN entry module from OCR JSONL")
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--chapter", type=int, required=True)
    args = parser.parse_args()

    prefix = f"_rln_p{args.part}_ch{args.chapter:02d}"
    jsonl_path = DRAFTS / f"{prefix}_records.jsonl"
    topics = json.loads((DATA / "chapter_topics.json").read_text(encoding="utf-8"))
    key = f"RLN-P{args.part}-C{args.chapter:02d}"
    slug = topics[key][0]

    records = [
        json.loads(line)
        for line in jsonl_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    out = write_module(args.part, args.chapter, records, slug)
    print(f"Wrote {len(records)} entries to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
