#!/usr/bin/env python3
"""Extract Entry / Theorem / Lemma / Corollary blocks from RLN chapter text (OCR drafts)."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

RLN_KIND_RE = re.compile(
    r"^(Entry|Theorem|Lemma|Corollary)\s+(\d+)\.(\d+)\.(\d+)"
    r"(?:\s*\([^)]*\))?"
    r"\.?\s*(.*)$",
    re.I,
)

STOP = re.compile(
    r"^(Proof\.?|First proof|Second proof|Third proof|"
    r"Proof of (?:Entry|Theorem|Lemma|Corollary)|"
    r"Before commencing the proof|An independent proof)",
    re.I,
)

PAGE_HEADER = re.compile(r"^\d+\s*$|^\d+\.\d+\s+[A-Z]|^={10,}|^PDF page \d+")


def normalize_line(line: str) -> str:
    line = line.strip()
    line = re.sub(r"\blO\b", "10", line)
    line = line.replace("ﬁ", "fi").replace("ﬂ", "fl")
    return line


def ocr_to_latex(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    subs = [
        (r"\bLog\b", r"\\log"),
        (r"\bIzl\b", r"|z|"),
        (r"\bIxl\b", r"|x|"),
        (r"r\(", r"\\Gamma("),
        (r"cp\(", r"\\varphi("),
        (r"qJ\(", r"\\varphi("),
        (r"t/J", r"\\psi"),
        (r"~=", r"\\sim"),
        (r"::;", r"\\leq"),
        (r":=:;;", r"\\leq"),
        (r"2::", r"\\geq"),
        (r"\(q2;\s*q3\)", r"(q^2;q^3)"),
        (r"\(q;\s*q3\)", r"(q;q^3)"),
        (r"∞", r"\\infty"),
        (r"π", r"\\pi"),
        (r"λ", r"\\lambda"),
        (r"χ", r"\\chi"),
        (r"ψ", r"\\psi"),
        (r"φ", r"\\varphi"),
        (r"Γ", r"\\Gamma"),
    ]
    for old, new in subs:
        text = re.sub(old, new, text)
    return text


def make_id(part: int, chapter: int, kind: str, nums: tuple[str, str, str]) -> str:
    ch = f"C{chapter:02d}"
    label = f"{kind.capitalize()}{nums[0]}-{nums[1]}-{nums[2]}"
    return f"RLN-P{part}-{ch}-{label}"


def parse_line(line: str) -> dict | None:
    line = normalize_line(line)
    if not line or PAGE_HEADER.match(line):
        return None

    m = RLN_KIND_RE.match(line)
    if not m:
        return None

    kind = m.group(1).capitalize()
    if kind != "Entry":
        return None
    rest = (m.group(5) or "").strip()
    if rest.lower().startswith(("has also found", "follows from", "is due to")):
        return None

    return {
        "kind": kind,
        "nums": (m.group(2), m.group(3), m.group(4)),
        "rest": rest,
    }


def label_matches_chapter(nums: tuple[str, str, str], chapter: int) -> bool:
    """RLN labels are chapter.section.number; keep only items for this chapter."""
    return int(nums[0]) == chapter


def find_start(lines: list[str]) -> int | None:
    for i, raw in enumerate(lines):
        if parse_line(raw.strip()):
            return i
    return None


def extract_blocks(
    text: str,
    *,
    part: int = 1,
    chapter: int = 1,
    topics: list[str],
    stop_chapter: int | None = None,
) -> list[dict]:
    lines = text.splitlines()
    start = find_start(lines)
    if start is None:
        return []
    lines = lines[start:]

    stop_res: list[re.Pattern[str]] = []
    if stop_chapter:
        stop_res.append(re.compile(rf"^{stop_chapter}\.1\s+"))

    def should_stop(line: str) -> bool:
        return any(pattern.match(line) for pattern in stop_res)

    blocks: list[dict] = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if should_stop(line):
            break
        parsed = parse_line(line)
        if not parsed:
            i += 1
            continue
        if not label_matches_chapter(parsed["nums"], chapter):
            i += 1
            continue

        parts = [parsed["rest"]] if parsed["rest"] else []
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt:
                i += 1
                continue
            if PAGE_HEADER.match(nxt):
                i += 1
                continue
            if should_stop(nxt):
                break
            if parse_line(nxt) or STOP.match(nxt):
                break
            if nxt.startswith(
                (
                    "Note that ",
                    "Ramanujan ",
                    "We remark ",
                    "It is curious ",
                    "In Entry ",
                    "In Theorem ",
                )
            ):
                i += 1
                continue
            parts.append(nxt)
            i += 1

        content = ocr_to_latex(" ".join(parts))
        if len(content) < 10:
            continue
        blocks.append(
            {
                "id": make_id(part, chapter, parsed["kind"], parsed["nums"]),
                "content": content,
                "topics": topics,
            }
        )
    return blocks


def dedupe_ids(records: list[dict]) -> list[dict]:
    """Keep first occurrence per id (heading match); drop OCR re-parses in proof text."""
    seen: set[str] = set()
    out: list[dict] = []
    for record in records:
        rid = record["id"]
        if rid in seen:
            continue
        seen.add(rid)
        out.append(record)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract RLN chapter records from text dump")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--topics", nargs="+", required=True)
    parser.add_argument("--stop-chapter", type=int)
    parser.add_argument("--jsonl", type=Path)
    args = parser.parse_args()

    text = args.input.read_text(encoding="utf-8")
    stop = args.stop_chapter or (args.chapter + 1)
    records = dedupe_ids(
        extract_blocks(
            text,
            part=args.part,
            chapter=args.chapter,
            topics=args.topics,
            stop_chapter=stop,
        )
    )
    print(f"Chapter {args.chapter}: extracted {len(records)} records")
    for record in records:
        print(record["id"])

    if args.jsonl:
        args.jsonl.write_text(
            "\n".join(json.dumps(record, ensure_ascii=False) for record in records) + "\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
