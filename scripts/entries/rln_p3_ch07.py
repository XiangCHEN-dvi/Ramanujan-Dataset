"""RLN Part 3, Chapter 7 — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C07 = ["generalized-tau-congruences"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C07}


CHAPTER_7 = [
    rec(
        "RLN-P3-C07-Entry7-1-1",
        r"$\tau_2(n)-\sigma_{15}(n)\equiv 0$ $(\mathrm{mod}\,3617)$, "
        r"where $\displaystyle\sum_{n=1}^{\infty}\tau_2(n)q^n=Q(q)\Delta(\tau)$.",
    ),
    rec(
        "RLN-P3-C07-Entry7-1-2",
        r"$\tau_2(n)-n\sigma_{13}(n)\equiv 0$ $(\mathrm{mod}\,16170)$.",
    ),
    rec(
        "RLN-P3-C07-Entry7-1-3",
        r"$\tau_2(n)-2n\sigma_9(n)+n^2\sigma_3(n)\equiv 0$ $(\mathrm{mod}\,600)$.",
    ),
    rec(
        "RLN-P3-C07-Entry7-1-4",
        r"$\tau_3(n)-\sigma_{17}(n)\equiv 0$ $(\mathrm{mod}\,43867)$, "
        r"where $\displaystyle\sum_{n=1}^{\infty}\tau_3(n)q^n=R(q)\Delta(\tau)$.",
    ),
    rec(
        "RLN-P3-C07-Entry7-1-5",
        r"$\tau_3(n)-n\sigma_{15}(n)\equiv 0$ $(\mathrm{mod}\,6006)$.",
    ),
    rec(
        "RLN-P3-C07-Entry7-1-6",
        r"$\tau_3(n)-n^2\sigma_1(n)\equiv 0$ $(\mathrm{mod}\,540)$.",
    ),
    rec(
        "RLN-P3-C07-Entry7-1-7",
        r"$\tau_3(n)-6n^2\sigma_9(n)+5n\sigma_3(n)\equiv 0$ $(\mathrm{mod}\,150)$.",
    ),
    rec(
        "RLN-P3-C07-Entry7-1-8",
        r"$\tau_3(n)+n\sigma_9(n)+n\sigma_3(n)-3\tau(n)\equiv 0$ $(\mathrm{mod}\,588)$.",
    ),
    rec(
        "RLN-P3-C07-Entry7-1-9",
        r"$\tau_4(n)-\sigma_{19}(n)\equiv 0$ $(\mathrm{mod}\,174611)$, "
        r"where $\displaystyle\sum_{n=1}^{\infty}\tau_4(n)q^n=Q^2(q)\Delta(\tau)$.",
    ),
]
