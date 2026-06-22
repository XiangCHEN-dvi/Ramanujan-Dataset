#!/usr/bin/env python3
"""Extract OCR draft records from RLN PDF into drafts/_rln_pN_chNN_* files."""

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
DEFAULT_PDF = Path.home() / "Downloads" / "RLN_PartI.pdf"
DEFAULT_PDFS = {
    1: DEFAULT_PDF,
    2: Path.home() / "Downloads" / "RLN_PartII.pdf",
    3: Path.home() / "Downloads" / "RLN_PartIII.pdf",
    4: Path.home() / "Downloads" / "RLN_PartIV.pdf",
    5: Path.home() / "Downloads" / "RLN_PartV.pdf",
}

sys.path.insert(0, str(SCRIPTS))
from extract_pdf_rln import DEFAULT_PDF as _DEFAULT, dump_chapter_text_rln  # noqa: E402


def artifact_prefix(part: int, chapter: int) -> str:
    return f"_rln_p{part}_ch{chapter:02d}"


def run_extractor(part: int, chapter: int, text_path: Path, topic_slug: str) -> int:
    prefix = artifact_prefix(part, chapter)
    cmd = [
        sys.executable,
        str(SCRIPTS / "extract_entries_rln.py"),
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
    from extract_pdf_rln import RLN_PART_CHAPTERS

    if part in RLN_PART_CHAPTERS:
        return RLN_PART_CHAPTERS[part]
    raise SystemExit(f"Unsupported RLN part: {part}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Batch OCR draft extraction from RLN PDF")
    parser.add_argument("--part", type=int, default=1, choices=[1, 2, 3, 4, 5])
    parser.add_argument("--pdf", type=Path, help="Path to RLN PDF")
    parser.add_argument("--chapters", type=int, nargs="*", help="Chapter numbers (default: 1–18)")
    args = parser.parse_args()

    chapters = args.chapters or list(chapter_range_for_part(args.part))
    topics = json.loads((DATA / "chapter_topics.json").read_text(encoding="utf-8"))
    pdf_path = args.pdf or DEFAULT_PDFS[args.part]

    doc = fitz.open(pdf_path)
    counts: dict[int, int] = {}
    DRAFTS.mkdir(parents=True, exist_ok=True)

    for chapter in chapters:
        key = f"RLN-P{args.part}-C{chapter:02d}"
        if key not in topics:
            raise SystemExit(f"Missing topic slug for {key} in chapter_topics.json")
        slug = topics[key][0]
        prefix = artifact_prefix(args.part, chapter)
        text_path = DRAFTS / f"{prefix}_extract.txt"
        dump_chapter_text_rln(doc, chapter, text_path, part=args.part)
        print(f"\n--- RLN Part {args.part} Ch.{chapter} topic={slug} ---")
        counts[chapter] = run_extractor(args.part, chapter, text_path, slug)

    print("\nSummary:")
    for ch, n in counts.items():
        print(f"  Ch.{ch}: {n} records")
    print(f"  Total: {sum(counts.values())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
