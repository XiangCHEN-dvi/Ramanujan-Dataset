#!/usr/bin/env python3
"""Extract raw text from Berndt notebook PDFs for manual curation."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

try:
    import fitz
except ImportError as exc:
    raise SystemExit("Install pymupdf: pip install pymupdf") from exc

DEFAULT_PDF = Path.home() / "Downloads" / "Ramanujans Notebooks Part I.pdf"
DEFAULT_PDFS = {
    1: DEFAULT_PDF,
    2: Path.home() / "Downloads" / "Ramanujans Notebooks Part II.pdf",
    3: Path.home() / "Downloads" / "Ramanujans Notebooks Part III.pdf",
    4: Path.home() / "Downloads" / "Ramanujans Notebooks Part IV.pdf",
    5: Path.home() / "Downloads" / "Ramanujans Notebooks Part V.pdf",
}


def _ranges_from_starts(starts: list[tuple[int, int]], page_count: int) -> dict[int, tuple[int, int]]:
    ranges: dict[int, tuple[int, int]] = {}
    for i, (number, start) in enumerate(starts):
        end = starts[i + 1][1] if i + 1 < len(starts) else page_count
        ranges[number] = (start, end)
    return ranges


def chapter_page_ranges(doc: fitz.Document, part: int | None = None) -> dict[int, tuple[int, int]]:
    """Map chapter number to half-open 0-based page index range [start, end)."""
    if part == 4:
        return chapter_page_ranges_running_headers(doc, 22, 31)
    if part == 5:
        return chapter_page_ranges_running_headers(doc, 32, 39)

    starts: list[tuple[int, int]] = []
    for index in range(doc.page_count):
        text = doc[index].get_text().strip()
        match = re.match(r"^CHAPTER (\d+)\s*\n", text, re.M)
        if match:
            starts.append((int(match.group(1)), index))

    if starts:
        return _ranges_from_starts(starts, doc.page_count)

    return {}


def chapter_page_ranges_running_headers(
    doc: fitz.Document, min_ch: int, max_ch: int
) -> dict[int, tuple[int, int]]:
    """Parts IV–V use running headers like '22. Elementary Results' instead of CHAPTER."""
    first_seen: dict[int, int] = {}
    for index in range(doc.page_count):
        lines = [line.strip() for line in doc[index].get_text().splitlines() if line.strip()]
        for line in lines[:6]:
            match = re.match(r"^(\d+)\.\s+.+", line)
            if match:
                chapter = int(match.group(1))
                if min_ch <= chapter <= max_ch and chapter not in first_seen:
                    first_seen[chapter] = index
                break
    starts = sorted((chapter, page) for chapter, page in first_seen.items())
    return _ranges_from_starts(starts, doc.page_count)


def chapter_page_ranges_part4(doc: fitz.Document) -> dict[int, tuple[int, int]]:
    return chapter_page_ranges_running_headers(doc, 22, 31)


def chapter_starts(doc: fitz.Document) -> list[tuple[int, str, int]]:
    chapters: list[tuple[int, str, int]] = []
    for index in range(doc.page_count):
        text = doc[index].get_text().strip()
        match = re.match(r"^CHAPTER (\d+)\s*\n(.+)", text, re.M)
        if match:
            chapters.append((int(match.group(1)), match.group(2).strip(), index + 1))
    return chapters


def extract_chapter(doc: fitz.Document, chapter: int, output: Path, part: int | None = None) -> None:
    ranges = chapter_page_ranges(doc, part=part)
    if chapter not in ranges:
        raise SystemExit(f"Chapter {chapter} not found in PDF")
    start, end = ranges[chapter]

    chunks: list[str] = []
    for page_number in range(start, end):
        chunks.append(f"\n{'=' * 72}\nPDF page {page_number + 1}\n{'=' * 72}\n")
        chunks.append(doc[page_number].get_text())

    output.write_text("".join(chunks), encoding="utf-8")
    print(f"Wrote chapter {chapter} (PDF pages {start + 1}-{end}) to {output}")


def dump_chapter_text(doc: fitz.Document, chapter: int, output: Path, part: int | None = None) -> None:
    """Write plain chapter text (no page markers) for OCR extraction."""
    ranges = chapter_page_ranges(doc, part=part)
    if chapter not in ranges:
        raise SystemExit(f"Chapter {chapter} not found in PDF")
    start, end = ranges[chapter]
    text = "\n".join(doc[i].get_text() for i in range(start, end))
    output.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract Berndt PDF chapter text")
    parser.add_argument("--part", type=int, default=1, choices=[1, 2, 3, 4, 5])
    parser.add_argument("--pdf", type=Path, help="Override default PDF path")
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    pdf_path = args.pdf or DEFAULT_PDFS[args.part]
    doc = fitz.open(pdf_path)
    extract_chapter(doc, args.chapter, args.output, part=args.part)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
