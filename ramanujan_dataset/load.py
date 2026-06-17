from __future__ import annotations

import json
from pathlib import Path

from .schema import Entry

DEFAULT_DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def data_dir() -> Path:
    return DEFAULT_DATA_DIR


def load_jsonl(path: Path | str | None = None) -> list[Entry]:
    path = Path(path) if path is not None else data_dir() / "train.jsonl"
    entries: list[Entry] = []
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(Entry.from_dict(json.loads(line)))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_no} of {path}") from exc
    return entries


def to_records(path: Path | str | None = None) -> list[dict]:
    return [entry.to_dict() for entry in load_jsonl(path)]


def to_hf_dataset(path: Path | str | None = None, split: str = "train"):
    try:
        from datasets import Dataset, DatasetDict
    except ImportError as exc:
        raise ImportError(
            "Install the optional Hugging Face dependency: pip install 'ramanujan-dataset[hf]'"
        ) from exc

    records = to_records(path)
    dataset = Dataset.from_list(records)
    return DatasetDict({split: dataset})
