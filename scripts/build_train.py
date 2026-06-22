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
from entries.rln_p1_ch01 import CHAPTER_1 as RLN_CHAPTER_1
from entries.rln_p1_ch02 import CHAPTER_2 as RLN_CHAPTER_2
from entries.rln_p1_ch03 import CHAPTER_3 as RLN_CHAPTER_3
from entries.rln_p1_ch04 import CHAPTER_4 as RLN_CHAPTER_4
from entries.rln_p1_ch05 import CHAPTER_5 as RLN_CHAPTER_5
from entries.rln_p1_ch06 import CHAPTER_6 as RLN_CHAPTER_6
from entries.rln_p1_ch07 import CHAPTER_7 as RLN_CHAPTER_7
from entries.rln_p1_ch08 import CHAPTER_8 as RLN_CHAPTER_8
from entries.rln_p1_ch09 import CHAPTER_9 as RLN_CHAPTER_9
from entries.rln_p1_ch10 import CHAPTER_10 as RLN_CHAPTER_10
from entries.rln_p1_ch11 import CHAPTER_11 as RLN_CHAPTER_11
from entries.rln_p1_ch12 import CHAPTER_12 as RLN_CHAPTER_12
from entries.rln_p1_ch13 import CHAPTER_13 as RLN_CHAPTER_13
from entries.rln_p1_ch14 import CHAPTER_14 as RLN_CHAPTER_14
from entries.rln_p1_ch15 import CHAPTER_15 as RLN_CHAPTER_15
from entries.rln_p1_ch16 import CHAPTER_16 as RLN_CHAPTER_16
from entries.rln_p1_ch17 import CHAPTER_17 as RLN_CHAPTER_17
from entries.rln_p1_ch18 import CHAPTER_18 as RLN_CHAPTER_18
from entries.rln_p2_ch01 import CHAPTER_1 as RLN2_CHAPTER_1
from entries.rln_p2_ch02 import CHAPTER_2 as RLN2_CHAPTER_2
from entries.rln_p2_ch03 import CHAPTER_3 as RLN2_CHAPTER_3
from entries.rln_p2_ch04 import CHAPTER_4 as RLN2_CHAPTER_4
from entries.rln_p2_ch05 import CHAPTER_5 as RLN2_CHAPTER_5
from entries.rln_p2_ch06 import CHAPTER_6 as RLN2_CHAPTER_6
from entries.rln_p2_ch07 import CHAPTER_7 as RLN2_CHAPTER_7
from entries.rln_p2_ch08 import CHAPTER_8 as RLN2_CHAPTER_8
from entries.rln_p2_ch09 import CHAPTER_9 as RLN2_CHAPTER_9
from entries.rln_p2_ch10 import CHAPTER_10 as RLN2_CHAPTER_10
from entries.rln_p2_ch11 import CHAPTER_11 as RLN2_CHAPTER_11
from entries.rln_p2_ch12 import CHAPTER_12 as RLN2_CHAPTER_12
from entries.rln_p2_ch13 import CHAPTER_13 as RLN2_CHAPTER_13
from entries.rln_p2_ch14 import CHAPTER_14 as RLN2_CHAPTER_14
from entries.rln_p2_ch15 import CHAPTER_15 as RLN2_CHAPTER_15
from entries.rln_p2_ch16 import CHAPTER_16 as RLN2_CHAPTER_16
from entries.rln_p3_ch02 import CHAPTER_2 as RLN3_CHAPTER_2
from entries.rln_p3_ch03 import CHAPTER_3 as RLN3_CHAPTER_3
from entries.rln_p3_ch04 import CHAPTER_4 as RLN3_CHAPTER_4
from entries.rln_p3_ch05 import CHAPTER_5 as RLN3_CHAPTER_5
from entries.rln_p3_ch06 import CHAPTER_6 as RLN3_CHAPTER_6
from entries.rln_p3_ch07 import CHAPTER_7 as RLN3_CHAPTER_7
from entries.rln_p3_ch08 import CHAPTER_8 as RLN3_CHAPTER_8
from entries.rln_p3_ch09 import CHAPTER_9 as RLN3_CHAPTER_9
from entries.rln_p3_ch10 import CHAPTER_10 as RLN3_CHAPTER_10
from entries.rln_p4_ch02 import CHAPTER_2 as RLN4_CHAPTER_2
from entries.rln_p4_ch03 import CHAPTER_3 as RLN4_CHAPTER_3
from entries.rln_p4_ch04 import CHAPTER_4 as RLN4_CHAPTER_4
from entries.rln_p4_ch05 import CHAPTER_5 as RLN4_CHAPTER_5
from entries.rln_p4_ch06 import CHAPTER_6 as RLN4_CHAPTER_6
from entries.rln_p4_ch07 import CHAPTER_7 as RLN4_CHAPTER_7
from entries.rln_p4_ch08 import CHAPTER_8 as RLN4_CHAPTER_8
from entries.rln_p4_ch09 import CHAPTER_9 as RLN4_CHAPTER_9
from entries.rln_p4_ch10 import CHAPTER_10 as RLN4_CHAPTER_10
from entries.rln_p4_ch11 import CHAPTER_11 as RLN4_CHAPTER_11
from entries.rln_p4_ch12 import CHAPTER_12 as RLN4_CHAPTER_12
from entries.rln_p4_ch13 import CHAPTER_13 as RLN4_CHAPTER_13
from entries.rln_p4_ch14 import CHAPTER_14 as RLN4_CHAPTER_14
from entries.rln_p4_ch15 import CHAPTER_15 as RLN4_CHAPTER_15
from entries.rln_p4_ch16 import CHAPTER_16 as RLN4_CHAPTER_16
from entries.rln_p4_ch17 import CHAPTER_17 as RLN4_CHAPTER_17
from entries.rln_p4_ch18 import CHAPTER_18 as RLN4_CHAPTER_18
from entries.rln_p4_ch19 import CHAPTER_19 as RLN4_CHAPTER_19
from entries.rln_p4_ch20 import CHAPTER_20 as RLN4_CHAPTER_20
from entries.rln_p4_ch21 import CHAPTER_21 as RLN4_CHAPTER_21
from entries.rln_p5_ch02 import CHAPTER_2 as RLN5_CHAPTER_2
from entries.rln_p5_ch03 import CHAPTER_3 as RLN5_CHAPTER_3
from entries.rln_p5_ch04 import CHAPTER_4 as RLN5_CHAPTER_4
from entries.rln_p5_ch05 import CHAPTER_5 as RLN5_CHAPTER_5
from entries.rln_p5_ch06 import CHAPTER_6 as RLN5_CHAPTER_6
from entries.rln_p5_ch07 import CHAPTER_7 as RLN5_CHAPTER_7
from entries.rln_p5_ch08 import CHAPTER_8 as RLN5_CHAPTER_8
from entries.rln_p5_ch09 import CHAPTER_9 as RLN5_CHAPTER_9
from entries.rln_p5_ch10 import CHAPTER_10 as RLN5_CHAPTER_10
from entries.rln_p5_ch11 import CHAPTER_11 as RLN5_CHAPTER_11
from entries.rln_p5_ch12 import CHAPTER_12 as RLN5_CHAPTER_12
from entries.rln_p5_ch13 import CHAPTER_13 as RLN5_CHAPTER_13
from entries.rln_p5_ch14 import CHAPTER_14 as RLN5_CHAPTER_14
from entries.rln_p5_ch15 import CHAPTER_15 as RLN5_CHAPTER_15
from entries.rln_p5_ch16 import CHAPTER_16 as RLN5_CHAPTER_16
from entries.rln_p5_ch17 import CHAPTER_17 as RLN5_CHAPTER_17
from entries.rln_p5_ch18 import CHAPTER_18 as RLN5_CHAPTER_18
from entries.rln_p5_ch19 import CHAPTER_19 as RLN5_CHAPTER_19
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
    ("RLN P1 Ch.1", RLN_CHAPTER_1),
    ("RLN P1 Ch.2", RLN_CHAPTER_2),
    ("RLN P1 Ch.3", RLN_CHAPTER_3),
    ("RLN P1 Ch.4", RLN_CHAPTER_4),
    ("RLN P1 Ch.5", RLN_CHAPTER_5),
    ("RLN P1 Ch.6", RLN_CHAPTER_6),
    ("RLN P1 Ch.7", RLN_CHAPTER_7),
    ("RLN P1 Ch.8", RLN_CHAPTER_8),
    ("RLN P1 Ch.9", RLN_CHAPTER_9),
    ("RLN P1 Ch.10", RLN_CHAPTER_10),
    ("RLN P1 Ch.11", RLN_CHAPTER_11),
    ("RLN P1 Ch.12", RLN_CHAPTER_12),
    ("RLN P1 Ch.13", RLN_CHAPTER_13),
    ("RLN P1 Ch.14", RLN_CHAPTER_14),
    ("RLN P1 Ch.15", RLN_CHAPTER_15),
    ("RLN P1 Ch.16", RLN_CHAPTER_16),
    ("RLN P1 Ch.17", RLN_CHAPTER_17),
    ("RLN P1 Ch.18", RLN_CHAPTER_18),
    ("RLN P2 Ch.1", RLN2_CHAPTER_1),
    ("RLN P2 Ch.2", RLN2_CHAPTER_2),
    ("RLN P2 Ch.3", RLN2_CHAPTER_3),
    ("RLN P2 Ch.4", RLN2_CHAPTER_4),
    ("RLN P2 Ch.5", RLN2_CHAPTER_5),
    ("RLN P2 Ch.6", RLN2_CHAPTER_6),
    ("RLN P2 Ch.7", RLN2_CHAPTER_7),
    ("RLN P2 Ch.8", RLN2_CHAPTER_8),
    ("RLN P2 Ch.9", RLN2_CHAPTER_9),
    ("RLN P2 Ch.10", RLN2_CHAPTER_10),
    ("RLN P2 Ch.11", RLN2_CHAPTER_11),
    ("RLN P2 Ch.12", RLN2_CHAPTER_12),
    ("RLN P2 Ch.13", RLN2_CHAPTER_13),
    ("RLN P2 Ch.14", RLN2_CHAPTER_14),
    ("RLN P2 Ch.15", RLN2_CHAPTER_15),
    ("RLN P2 Ch.16", RLN2_CHAPTER_16),
    ("RLN P3 Ch.2", RLN3_CHAPTER_2),
    ("RLN P3 Ch.3", RLN3_CHAPTER_3),
    ("RLN P3 Ch.4", RLN3_CHAPTER_4),
    ("RLN P3 Ch.5", RLN3_CHAPTER_5),
    ("RLN P3 Ch.6", RLN3_CHAPTER_6),
    ("RLN P3 Ch.7", RLN3_CHAPTER_7),
    ("RLN P3 Ch.8", RLN3_CHAPTER_8),
    ("RLN P3 Ch.9", RLN3_CHAPTER_9),
    ("RLN P3 Ch.10", RLN3_CHAPTER_10),
    ("RLN P4 Ch.2", RLN4_CHAPTER_2),
    ("RLN P4 Ch.3", RLN4_CHAPTER_3),
    ("RLN P4 Ch.4", RLN4_CHAPTER_4),
    ("RLN P4 Ch.5", RLN4_CHAPTER_5),
    ("RLN P4 Ch.6", RLN4_CHAPTER_6),
    ("RLN P4 Ch.7", RLN4_CHAPTER_7),
    ("RLN P4 Ch.8", RLN4_CHAPTER_8),
    ("RLN P4 Ch.9", RLN4_CHAPTER_9),
    ("RLN P4 Ch.10", RLN4_CHAPTER_10),
    ("RLN P4 Ch.11", RLN4_CHAPTER_11),
    ("RLN P4 Ch.12", RLN4_CHAPTER_12),
    ("RLN P4 Ch.13", RLN4_CHAPTER_13),
    ("RLN P4 Ch.14", RLN4_CHAPTER_14),
    ("RLN P4 Ch.15", RLN4_CHAPTER_15),
    ("RLN P4 Ch.16", RLN4_CHAPTER_16),
    ("RLN P4 Ch.17", RLN4_CHAPTER_17),
    ("RLN P4 Ch.18", RLN4_CHAPTER_18),
    ("RLN P4 Ch.19", RLN4_CHAPTER_19),
    ("RLN P4 Ch.20", RLN4_CHAPTER_20),
    ("RLN P4 Ch.21", RLN4_CHAPTER_21),
    ("RLN P5 Ch.2", RLN5_CHAPTER_2),
    ("RLN P5 Ch.3", RLN5_CHAPTER_3),
    ("RLN P5 Ch.4", RLN5_CHAPTER_4),
    ("RLN P5 Ch.5", RLN5_CHAPTER_5),
    ("RLN P5 Ch.6", RLN5_CHAPTER_6),
    ("RLN P5 Ch.7", RLN5_CHAPTER_7),
    ("RLN P5 Ch.8", RLN5_CHAPTER_8),
    ("RLN P5 Ch.9", RLN5_CHAPTER_9),
    ("RLN P5 Ch.10", RLN5_CHAPTER_10),
    ("RLN P5 Ch.11", RLN5_CHAPTER_11),
    ("RLN P5 Ch.12", RLN5_CHAPTER_12),
    ("RLN P5 Ch.13", RLN5_CHAPTER_13),
    ("RLN P5 Ch.14", RLN5_CHAPTER_14),
    ("RLN P5 Ch.15", RLN5_CHAPTER_15),
    ("RLN P5 Ch.16", RLN5_CHAPTER_16),
    ("RLN P5 Ch.17", RLN5_CHAPTER_17),
    ("RLN P5 Ch.18", RLN5_CHAPTER_18),
    ("RLN P5 Ch.19", RLN5_CHAPTER_19),
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
