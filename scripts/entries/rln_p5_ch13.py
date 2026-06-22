"""RLN Part 5, Chapter 13 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C13 = ["mordell-integral-appell-lerch"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C13}


CHAPTER_13 = [
    rec(
        "RLN-P5-C13-Entry13-1-1",
        r"If $q_1=e^{-\pi/(3n)}$ and $q=e^{-3\pi n}$, then "
        r"$2\sqrt{3}\displaystyle\int_0^{\infty}\dfrac{e^{-\pi n x^2/3}\cos(\pi t x)}"
        r"{e^{2\pi x/3}+1+e^{-2\pi x/3}}\,dx"
        r"=q_1^{1/18}\displaystyle\sum_{m=1}^{\infty}\dfrac{q^{(2m-1)^2/6}}"
        r"{(-e^{\pi t}q_1^{1/3};q^{2/3})_m\,(-e^{-\pi t}q_1^{1/3};q^{2/3})_m}"
        r"+e^{-3\pi t^2/(4n)}\,\dfrac{q_1^{1/2}}{\sqrt{n}}"
        r"\displaystyle\sum_{m=1}^{\infty}\dfrac{q^{3(2m-1)^2/2}}"
        r"{(-e^{\pi i t/n}q_1^3;q_1^6)_m\,(-e^{-\pi i t/n}q_1^3;q_1^6)_m}"
        r"=q^{-1/36}\,\dfrac{1}{(q^{2/3};q^{2/3})_\infty}"
        r"\displaystyle\sum_{m=1}^{\infty}(-1)^{m+1}q^{(2m-1)^2/4}"
        r"\left(\dfrac{1}{1+e^{\pi t}q^{(2m-1)/3}}+\dfrac{1}{1+e^{-\pi t}q^{(2m-1)/3}}-1\right)"
        r"+e^{-3\pi t^2/(4n)}\,\dfrac{1}{n}"
        r"\displaystyle\sum_{m=1}^{\infty}(-1)^{m+1}q^{9(2m-1)^2/4}"
        r"\left(\dfrac{1}{1+e^{\pi i t/n}q_1^{3(2m-1)}}+\dfrac{1}{1+e^{-\pi i t/n}q_1^{3(2m-1)}}-1\right)$.",
    ),
]
