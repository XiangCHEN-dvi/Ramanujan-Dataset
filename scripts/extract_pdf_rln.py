#!/usr/bin/env python3
"""Chapter page ranges for Andrews & Berndt, Ramanujan's Lost Notebook."""

from __future__ import annotations

import re

try:
    import fitz
except ImportError as exc:
    raise SystemExit("Install pymupdf: pip install pymupdf") from exc

DEFAULT_PDF = __import__("pathlib").Path.home() / "Downloads" / "RLN_PartI.pdf"
DEFAULT_PDFS = {
    1: DEFAULT_PDF,
    2: __import__("pathlib").Path.home() / "Downloads" / "RLN_PartII.pdf",
    3: __import__("pathlib").Path.home() / "Downloads" / "RLN_PartIII.pdf",
    4: __import__("pathlib").Path.home() / "Downloads" / "RLN_PartIV.pdf",
    5: __import__("pathlib").Path.home() / "Downloads" / "RLN_PartV.pdf",
}
RLN_PART_CHAPTERS = {
    1: range(1, 19),
    2: range(1, 17),
    3: range(2, 11),
    4: range(2, 22),
    5: range(2, 20),
}


def _ranges_from_starts(starts: list[tuple[int, int]], page_count: int) -> dict[int, tuple[int, int]]:
    ranges: dict[int, tuple[int, int]] = {}
    for i, (number, start) in enumerate(starts):
        end = starts[i + 1][1] if i + 1 < len(starts) else page_count
        ranges[number] = (start, end)
    return ranges


def chapter_page_ranges_rln(doc: fitz.Document, part: int = 1) -> dict[int, tuple[int, int]]:
    """Map chapter number to half-open 0-based page index range [start, end)."""
    if part not in RLN_PART_CHAPTERS:
        raise ValueError(f"RLN chapter detection not implemented for part {part}")

    starts: list[tuple[int, int]] = []
    for index in range(doc.page_count):
        lines = [line.strip() for line in doc[index].get_text().splitlines() if line.strip()]
        for line in lines[:12]:
            match = re.match(r"^(\d+)\.1\s+(.+)", line)
            if match and len(match.group(2)) > 3:
                chapter = int(match.group(1))
                if chapter not in {ch for ch, _ in starts}:
                    starts.append((chapter, index))
                break

    if part == 3 and 10 not in {ch for ch, _ in starts}:
        for index in range(doc.page_count):
            lines = [line.strip() for line in doc[index].get_text().splitlines() if line.strip()]
            if lines and lines[0] == "10" and any("Highly Composite" in line for line in lines[:6]):
                starts.append((10, index))
                break

    if part == 4 and 16 not in {ch for ch, _ in starts}:
        for index in range(doc.page_count):
            lines = [line.strip() for line in doc[index].get_text().splitlines() if line.strip()]
            if lines and lines[0] == "16" and any("Preliminary" in line for line in lines[:5]):
                starts.append((16, index))
                break

    return _ranges_from_starts(sorted(starts), doc.page_count)


def dump_chapter_text_rln(doc: fitz.Document, chapter: int, output, part: int = 1) -> None:
    ranges = chapter_page_ranges_rln(doc, part=part)
    if chapter not in ranges:
        raise SystemExit(f"Chapter {chapter} not found in RLN PDF")
    start, end = ranges[chapter]
    text = "\n".join(doc[i].get_text() for i in range(start, end))
    output.write_text(text, encoding="utf-8")
