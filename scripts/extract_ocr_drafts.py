#!/usr/bin/env python3
"""Extract OCR draft records from a Berndt PDF into drafts/_pN_chNN_* files.

Does not modify scripts/entries/ or data/train.jsonl.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

try:
    import fitz
except ImportError as exc:
    raise SystemExit("Install pymupdf: pip install pymupdf") from exc

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
DATA = ROOT / "data"
DRAFTS = ROOT / "drafts"
DEFAULT_PDFS = {
    1: Path.home() / "Downloads" / "Ramanujans Notebooks Part I.pdf",
    2: Path.home() / "Downloads" / "Ramanujans Notebooks Part II.pdf",
    3: Path.home() / "Downloads" / "Ramanujans Notebooks Part III.pdf",
    4: Path.home() / "Downloads" / "Ramanujans Notebooks Part IV.pdf",
    5: Path.home() / "Downloads" / "Ramanujans Notebooks Part V.pdf",
}

sys.path.insert(0, str(SCRIPTS))
from extract_pdf import chapter_page_ranges, dump_chapter_text  # noqa: E402


def artifact_prefix(part: int, chapter: int) -> str:
    if part == 1:
        return f"_ch{chapter:02d}"
    return f"_p{part}_ch{chapter:02d}"


def run_extractor(part: int, chapter: int, text_path: Path, topic_slug: str) -> int:
    prefix = artifact_prefix(part, chapter)
    cmd = [
        sys.executable,
        str(SCRIPTS / "extract_entries.py"),
        "--input",
        str(text_path),
        "--part",
        str(part),
        "--chapter",
        str(chapter),
        "--topics",
        topic_slug,
        "--stop-chapter",
        str(chapter + 1),
        "--jsonl",
        str(DRAFTS / f"{prefix}_records.jsonl"),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    print(result.stdout, end="")
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)
    return int(result.stdout.split("extracted")[1].split("records")[0].strip())


def chapter_range_for_part(part: int) -> range:
    if part == 1:
        return range(3, 10)
    if part == 2:
        return range(10, 16)
    if part == 3:
        return range(16, 22)
    if part == 4:
        return range(22, 32)
    if part == 5:
        return range(32, 40)
    raise SystemExit(f"Unsupported part: {part}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Batch OCR draft extraction from Berndt PDF")
    parser.add_argument("--part", type=int, default=1, choices=[1, 2, 3, 4, 5])
    parser.add_argument("--pdf", type=Path, help="Override default PDF path")
    parser.add_argument(
        "--chapters",
        type=int,
        nargs="*",
        help="Chapter numbers (default: Part I 3–9, Part II 10–15, Part III 16–21, Part IV 22–31, Part V 32–39)",
    )
    args = parser.parse_args()

    pdf_path = args.pdf or DEFAULT_PDFS[args.part]
    chapters = args.chapters or list(chapter_range_for_part(args.part))
    topics = json.loads((DATA / "chapter_topics.json").read_text(encoding="utf-8"))

    doc = fitz.open(pdf_path)
    ranges = chapter_page_ranges(doc, part=args.part)
    counts: dict[int, int] = {}

    for chapter in chapters:
        if chapter not in ranges:
            raise SystemExit(f"Chapter {chapter} not found in {pdf_path}")
        start, end = ranges[chapter]
        key = f"RN-P{args.part}-C{chapter:02d}"
        if key not in topics:
            raise SystemExit(f"Missing topic slug for {key} in chapter_topics.json")
        slug = topics[key][0]
        prefix = artifact_prefix(args.part, chapter)
        DRAFTS.mkdir(parents=True, exist_ok=True)
        text_path = DRAFTS / f"{prefix}_extract.txt"
        dump_chapter_text(doc, chapter, text_path, part=args.part)
        print(f"\n--- Part {args.part} Ch.{chapter} (PDF pages {start + 1}-{end}) topic={slug} ---")
        counts[chapter] = run_extractor(args.part, chapter, text_path, slug)

    print("\nSummary:")
    for ch, n in counts.items():
        print(f"  Ch.{ch}: {n} records")
    print(f"  Total: {sum(counts.values())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
