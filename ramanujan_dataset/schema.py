from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass
class Entry:
    id: str
    content: str
    topics: list[str]

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Entry":
        return cls(**data)
