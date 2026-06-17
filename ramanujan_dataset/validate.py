from __future__ import annotations

import json
import re
from pathlib import Path

from .load import data_dir

try:
    import jsonschema
except ImportError:
    jsonschema = None

_CHAPTER_PREFIX = re.compile(r"^((?:RN|RLN)-P[1-5]-C[0-9]{2})-")


def schema_path() -> Path:
    return data_dir() / "schema.json"


def chapter_topics_path() -> Path:
    return data_dir() / "chapter_topics.json"


def load_schema() -> dict:
    with schema_path().open(encoding="utf-8") as handle:
        return json.load(handle)


def load_chapter_topics() -> dict[str, list[str]]:
    with chapter_topics_path().open(encoding="utf-8") as handle:
        return json.load(handle)


def chapter_prefix(entry_id: str) -> str | None:
    match = _CHAPTER_PREFIX.match(entry_id)
    return match.group(1) if match else None


def validate_jsonl(path: Path | str | None = None) -> list[str]:
    if jsonschema is None:
        raise ImportError(
            "Install the optional validation dependency: pip install 'ramanujan-dataset[dev]'"
        )

    path = Path(path) if path is not None else data_dir() / "train.jsonl"
    schema = load_schema()
    chapter_topics = load_chapter_topics()
    known_slugs = {slug for slugs in chapter_topics.values() for slug in slugs}
    errors: list[str] = []
    seen_ids: set[str] = set()

    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            validation_errors = sorted(
                jsonschema.Draft202012Validator(schema).iter_errors(record),
                key=lambda err: list(err.path),
            )
            for error in validation_errors:
                errors.append(f"line {line_no}: {error.message}")

            entry_id = record.get("id")
            if entry_id in seen_ids:
                errors.append(f"line {line_no}: duplicate id '{entry_id}'")
            seen_ids.add(entry_id)

            prefix = chapter_prefix(entry_id)
            if prefix is None:
                errors.append(f"line {line_no}: cannot parse chapter prefix from id '{entry_id}'")
                continue

            expected_topics = chapter_topics.get(prefix)
            if expected_topics is None:
                errors.append(f"line {line_no}: unknown chapter prefix '{prefix}' in chapter_topics.json")
            elif record.get("topics") != expected_topics:
                errors.append(
                    f"line {line_no}: topics {record.get('topics')!r} != expected {expected_topics!r} for {prefix}"
                )

            for slug in record.get("topics", []):
                if slug not in known_slugs:
                    errors.append(f"line {line_no}: unknown topic slug '{slug}'")

    return errors
