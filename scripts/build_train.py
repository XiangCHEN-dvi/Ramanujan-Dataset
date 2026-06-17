#!/usr/bin/env python3
"""Build data/train.jsonl from scripts/entries/pN_chNN.py and validate."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(SCRIPTS))

from entries.p1_ch01 import CHAPTER_1
from entries.p1_ch02 import CHAPTER_2
from entries.p1_ch03 import CHAPTER_3
from entries.p1_ch04 import CHAPTER_4
from entries.p1_ch05 import CHAPTER_5
from entries.p1_ch06 import CHAPTER_6
from entries.p1_ch07 import CHAPTER_7
from entries.p1_ch08 import CHAPTER_8
from entries.p1_ch09 import CHAPTER_9
from entries.p2_ch10 import CHAPTER_10
from entries.p2_ch11 import CHAPTER_11
from entries.p2_ch12 import CHAPTER_12
from entries.p2_ch13 import CHAPTER_13
from entries.p2_ch14 import CHAPTER_14
from entries.p2_ch15 import CHAPTER_15
from entries.p3_ch16 import CHAPTER_16
from entries.p3_ch17 import CHAPTER_17
from entries.p3_ch18 import CHAPTER_18
from entries.p3_ch19 import CHAPTER_19
from entries.p3_ch20 import CHAPTER_20
from entries.p3_ch21 import CHAPTER_21
from entries.p4_ch22 import CHAPTER_22
from entries.p4_ch23 import CHAPTER_23
from entries.p4_ch24 import CHAPTER_24
from entries.p4_ch25 import CHAPTER_25
from entries.p4_ch26 import CHAPTER_26
from entries.p4_ch27 import CHAPTER_27
from entries.p4_ch28 import CHAPTER_28
from entries.p4_ch29 import CHAPTER_29
from entries.p4_ch30 import CHAPTER_30
from entries.p4_ch31 import CHAPTER_31
from entries.p5_ch32 import CHAPTER_32
from entries.p5_ch33 import CHAPTER_33
from entries.p5_ch34 import CHAPTER_34
from entries.p5_ch35 import CHAPTER_35
from entries.p5_ch36 import CHAPTER_36
from entries.p5_ch37 import CHAPTER_37
from entries.p5_ch38 import CHAPTER_38
from entries.p5_ch39 import CHAPTER_39
from ramanujan_dataset import validate_jsonl

CHAPTERS: list[tuple[str, list[dict]]] = [
    ("P1 Ch.1", CHAPTER_1),
    ("P1 Ch.2", CHAPTER_2),
    ("P1 Ch.3", CHAPTER_3),
    ("P1 Ch.4", CHAPTER_4),
    ("P1 Ch.5", CHAPTER_5),
    ("P1 Ch.6", CHAPTER_6),
    ("P1 Ch.7", CHAPTER_7),
    ("P1 Ch.8", CHAPTER_8),
    ("P1 Ch.9", CHAPTER_9),
    ("P2 Ch.10", CHAPTER_10),
    ("P2 Ch.11", CHAPTER_11),
    ("P2 Ch.12", CHAPTER_12),
    ("P2 Ch.13", CHAPTER_13),
    ("P2 Ch.14", CHAPTER_14),
    ("P2 Ch.15", CHAPTER_15),
    ("P3 Ch.16", CHAPTER_16),
    ("P3 Ch.17", CHAPTER_17),
    ("P3 Ch.18", CHAPTER_18),
    ("P3 Ch.19", CHAPTER_19),
    ("P3 Ch.20", CHAPTER_20),
    ("P3 Ch.21", CHAPTER_21),
    ("P4 Ch.22", CHAPTER_22),
    ("P4 Ch.23", CHAPTER_23),
    ("P4 Ch.24", CHAPTER_24),
    ("P4 Ch.25", CHAPTER_25),
    ("P4 Ch.26", CHAPTER_26),
    ("P4 Ch.27", CHAPTER_27),
    ("P4 Ch.28", CHAPTER_28),
    ("P4 Ch.29", CHAPTER_29),
    ("P4 Ch.30", CHAPTER_30),
    ("P4 Ch.31", CHAPTER_31),
    ("P5 Ch.32", CHAPTER_32),
    ("P5 Ch.33", CHAPTER_33),
    ("P5 Ch.34", CHAPTER_34),
    ("P5 Ch.35", CHAPTER_35),
    ("P5 Ch.36", CHAPTER_36),
    ("P5 Ch.37", CHAPTER_37),
    ("P5 Ch.38", CHAPTER_38),
    ("P5 Ch.39", CHAPTER_39),
]


def all_entries() -> list[dict]:
    entries: list[dict] = []
    for _, chapter in CHAPTERS:
        entries.extend(chapter)
    return entries


def write_train_jsonl(path: Path) -> int:
    entries = all_entries()
    with path.open("w", encoding="utf-8") as handle:
        for record in entries:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return len(entries)


def run_validate() -> int:
    errors = validate_jsonl()
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("Validation passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build and validate data/train.jsonl")
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Validate existing train.jsonl without rebuilding",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "data" / "train.jsonl",
        help="Output JSONL path (default: data/train.jsonl)",
    )
    args = parser.parse_args()

    if args.check_only:
        return run_validate()

    count = write_train_jsonl(args.output)
    breakdown = ", ".join(f"{len(ch)} from {label}" for label, ch in CHAPTERS)
    print(f"Wrote {count} entries ({breakdown})")
    return run_validate()


if __name__ == "__main__":
    raise SystemExit(main())
