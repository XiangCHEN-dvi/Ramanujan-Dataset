#!/usr/bin/env python3
"""Extract Entry / Corollary / Example blocks from a Berndt chapter text dump (OCR drafts)."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PAGE_REF = r"(?:\s*\(p+\.\s*\d+(?:-\d+)?\))?"
ENTRY_RE = re.compile(
    rf"^Entry\s+(\d+)(?:\(([ivx]+|[a-z])\))?{PAGE_REF}\.\s*(.*)$",
    re.I,
)
COROLLARY_RE = re.compile(
    rf"^Corollary(?:\s+(\d+)(?:\(([ivx]+|[a-z])\))?)?{PAGE_REF}\.\s*(.*)$",
    re.I,
)
EXAMPLE_RE = re.compile(
    rf"^Example\s+(?:(\d+)(?:\(([ivx]+|[a-z]\d?)\))?{PAGE_REF}|\(([ivx]+|[a-z]\d?)\){PAGE_REF})\.\s*(.*)$",
    re.I,
)

PROSE_SKIP = re.compile(
    r"(?i)^(Entry|Corollary|Example)\s+\d+.*\s("
    r"is enormously|is central|is obviously|is actually|is identical|is the same|"
    r"was incorrectly|follows from|or equivalent|and allied|Thus,|amd because|"
    r"below is a problem|must be corrected|with x replaced|In the former|"
    r"is simply an alternative|is simply another|is simply the definition|"
    r"is simply a consequence|simply records the familiar|is used only to make|"
    r"offers the trivial|in somewhat disguised|is stated without proof|"
    r"was first established|was first stated|is known as|can be found in|"
    r"can be derived from|do not seem to have|can be traced|appears to have|"
    r"constitutes a warning|merely gives the definition|is an illustration of|"
    r"is readily obtained|gives the well-known|and using \(|Recall that|"
    r"directly\. For|of Chapter \d|in Chapter \d"
    r")",
)

PROSE_SKIP_UNNUMBERED = re.compile(
    r"(?i)^(Corollary|Example)\s+\d+.*\s("
    r"is a complete triviality|is the special case|which follows easily|"
    r"follows from Example|follows from the identity"
    r")",
)

STOP = re.compile(
    r"^(Proof\.?|First proof|Second proof|CHAPTER \d|"
    r"Proof of Theorem|Before commencing the proof|"
    r"An independent proof|Both Examples \d|We omit the details)",
    re.I,
)

PAGE_HEADER = re.compile(r"^\d+\s*$|^\d+\.\s+[A-Z]|^={10,}|^PDF page \d+")


def normalize_line(line: str) -> str:
    line = line.strip()
    line = re.sub(r"\(([ivx]+)\}\.", r"(\1).", line)
    line = re.sub(r"\blO\b", "10", line)
    return line


def ocr_to_latex(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    subs = [
        (r"\bLog\b", r"\\log"),
        (r"\bIzl\b", r"|z|"),
        (r"\bIxl\b", r"|x|"),
        (r"\bIaI\b", r"|a|"),
        (r"\bInI\b", r"|n|"),
        (r"r\(", r"\\Gamma("),
        (r"cp\(", r"\\varphi("),
        (r"qJ\(", r"\\varphi("),
        (r"t/J", r"\\psi"),
        (r"ljJ", r"\\psi"),
        (r"~=", r"\\sim"),
        (r"::;", r"\\leq"),
        (r":=:;;", r"\\leq"),
        (r"2::", r"\\geq"),
        (r"Lk=O", r"\\sum_{k=0}"),
        (r"Lf=o", r"\\sum_{j=0}"),
        (r"I:,=", r"\\sum_{n=1}"),
        (r"If'= 1", r"\\sum_{k=1}"),
        (r"If'=l", r"\\sum_{k=1}"),
        (r"I\. ", r"\\sum "),
    ]
    for old, new in subs:
        text = re.sub(old, new, text)
    return text


def fmt_entry(num: str, sub: str | None = None) -> str:
    base = f"Entry{int(num):02d}"
    return base + sub if sub else base


def fmt_example(num: str | None, sub: str | None) -> str:
    if num and sub:
        return f"Example{int(num):02d}{sub}"
    if num:
        return f"Example{int(num):02d}"
    if sub:
        return f"Example{sub}"
    return "Example"


def fmt_corollary(num: str | None, sub: str | None) -> str:
    if num and sub:
        return f"Corollary{int(num):02d}{sub}"
    if num:
        return f"Corollary{int(num):02d}"
    return "Corollary"


def make_id(part: int, chapter: int, parsed: dict, ctx: dict) -> str:
    ch = f"C{chapter:02d}"
    kind = parsed["kind"]

    if kind == "Entry":
        body = fmt_entry(parsed["num"], parsed.get("sub"))
        ctx["entry"] = body
        ctx["entry_base"] = f"Entry{int(parsed['num']):02d}"
        return f"RN-P{part}-{ch}-{body}"

    if kind == "Corollary":
        parent = ctx.get("entry_base", ctx.get("entry", "Entry00"))
        return f"RN-P{part}-{ch}-{parent}-{fmt_corollary(parsed.get('num'), parsed.get('sub'))}"

    if "entry_base" in ctx:
        parent = ctx["entry_base"]
        ex = fmt_example(parsed.get("num"), parsed.get("sub"))
        return f"RN-P{part}-{ch}-{parent}-{ex}"

    ctx.setdefault("example_seq", 0)
    ctx["example_seq"] += 1
    ex = fmt_example(parsed.get("num"), parsed.get("sub"))
    if parsed.get("num") or parsed.get("sub"):
        return f"RN-P{part}-{ch}-{ex}"
    return f"RN-P{part}-{ch}-Example{ctx['example_seq']:02d}"


def parse_line(line: str) -> dict | None:
    line = normalize_line(line)
    if not line or PAGE_HEADER.match(line):
        return None
    if PROSE_SKIP.match(line) or PROSE_SKIP_UNNUMBERED.match(line):
        return None

    m = ENTRY_RE.match(line)
    if m:
        rest = (m.group(3) or "").strip()
        if rest.lower().startswith(("and using", "recall that", "directly.")):
            return None
        return {"kind": "Entry", "num": m.group(1), "sub": m.group(2), "rest": rest}

    m = COROLLARY_RE.match(line)
    if m:
        rest = (m.group(3) or "").strip()
        if rest.startswith("is simply"):
            return None
        return {
            "kind": "Corollary",
            "num": m.group(1),
            "sub": m.group(2),
            "rest": rest,
        }

    m = EXAMPLE_RE.match(line)
    if m:
        rest = (m.group(4) or "").strip()
        if rest.startswith(("is an illustration", "is readily obtained", "follows from")):
            return None
        return {
            "kind": "Example",
            "num": m.group(1) or None,
            "sub": m.group(2) or m.group(3),
            "rest": rest,
        }
    return None


def find_start(lines: list[str]) -> int:
    for i, raw in enumerate(lines):
        if parse_line(raw.strip()):
            return i
    raise ValueError("No formal Entry/Corollary/Example heading found")


def extract_blocks(
    text: str,
    *,
    part: int = 1,
    chapter: int = 3,
    topics: list[str],
    stop_chapter: int | None = None,
) -> list[dict]:
    lines = text.splitlines()
    start = find_start(lines)
    lines = lines[start:]
    stop_res: list[re.Pattern[str]] = []
    if stop_chapter:
        stop_res.append(re.compile(rf"^CHAPTER\s+{stop_chapter}\b", re.I))
        stop_res.append(re.compile(rf"^{stop_chapter}\.\s+[A-Z]"))

    def should_stop(line: str) -> bool:
        return any(pattern.match(line) for pattern in stop_res)

    blocks: list[dict] = []
    ctx: dict = {}
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if should_stop(line):
            break
        parsed = parse_line(line)
        if not parsed:
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
                    "In the corollary ",
                    "In Entry ",
                    "We remark ",
                    "It is curious ",
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
                "id": make_id(part, chapter, parsed, ctx),
                "content": content,
                "topics": topics,
            }
        )
    return blocks


def dedupe_ids(records: list[dict]) -> list[dict]:
    seen: dict[str, int] = {}
    out: list[dict] = []
    for r in records:
        rid = r["id"]
        if rid in seen:
            seen[rid] += 1
            rid = f"{rid}-dup{seen[rid]}"
        else:
            seen[rid] = 0
        out.append({**r, "id": rid})
    return out


def to_python_module(records: list[dict], path: Path, chapter: int, topic_slug: str) -> None:
    var = f"CHAPTER_{chapter}"
    topics_var = f"TOPICS_C{chapter:02d}"
    lines = [
        f'"""Auto-generated Chapter {chapter} entries — OCR draft, needs human review."""',
        "",
        "from __future__ import annotations",
        "",
        f'{topics_var} = ["{topic_slug}"]',
        "",
        "",
        "def rec(entry_id: str, content: str) -> dict:",
        f'    return {{"id": entry_id, "content": content, "topics": {topics_var}}}',
        "",
        "",
        f"{var} = [",
    ]
    for r in records:
        cid = r["id"]
        content = r["content"].replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'    rec("{cid}", r"{content}"),')
    lines.append("]")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--part", type=int, default=1)
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--topics", nargs="+", required=True)
    parser.add_argument("--stop-chapter", type=int)
    parser.add_argument("--jsonl", type=Path)
    parser.add_argument("--python", type=Path)
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
    for r in records:
        print(r["id"])

    if args.jsonl:
        args.jsonl.write_text(
            "\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n",
            encoding="utf-8",
        )
    if args.python:
        to_python_module(records, args.python, args.chapter, args.topics[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
