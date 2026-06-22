"""RLN Part 4, Chapter 7 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C07 = ["diophantine-approximation"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C07}


CHAPTER_7 = [
    rec(
        "RLN-P4-C07-Entry7-3-1",
        r"Let $\epsilon>0$ be given. If $a$ is any nonzero integer, then there exist infinitely many "
        r"positive integers $N$ such that "
        r"$Ne^{2/a}-[Ne^{2/a}]<\dfrac{(1+\epsilon)\log\log N}{|a|N\log N}$, "
        r"and for all sufficiently large positive integers $N$, "
        r"$Ne^{2/a}-[Ne^{2/a}]>\dfrac{(1-\epsilon)\log\log N}{|a|N\log N}$.",
    ),
    rec(
        "RLN-P4-C07-Entry7-3-2",
        r"If $a$ is any odd integer and $\epsilon>0$ is given, then there exist infinitely many positive "
        r"integers $N$ such that "
        r"$1+[Ne^{2/a}]-Ne^{2/a}<\dfrac{(1+\epsilon)\log\log N}{4|a|N\log N}$, "
        r"and for all positive integers $N$ sufficiently large, "
        r"$1+[Ne^{2/a}]-Ne^{2/a}>\dfrac{(1-\epsilon)\log\log N}{4|a|N\log N}$.",
    ),
]
