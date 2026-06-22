"""RLN Part 5, Chapter 16 — AI curated LaTeX (Entry only).

Continued fractions in Ramanujan's Lost Notebook; Ramanujan statements only.
"""

from __future__ import annotations

TOPICS_C16 = ["continued-fractions-lost-notebook-p5"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C16}


CHAPTER_16 = [
    rec(
        "RLN-P5-C16-Entry16-2-1",
        r"With $Q(q):=q\dfrac{f^5(-q^5)}{f(-q)}$ and $F(q)=R(q)$ the Rogers–Ramanujan "
        r"continued fraction, Ramanujan gives "
        r"$\dfrac{Q(q^{1/5})}{Q(q)}=\dfrac{F(q)+\dfrac{\sqrt{5}-1}{2}}{F(q)^5}"
        r"\Big/\dfrac{F(q^{1/5})+\dfrac{\sqrt{5}-1}{2}}{F(q^{1/5})^5}$.",
    ),
    rec(
        "RLN-P5-C16-Entry16-2-2",
        r"If $x^6=1+x^4$, then Ramanujan claims "
        r"$\dfrac{1-ix}{1-x^2}\dfrac{1+ix^3}{1+x^4}\dfrac{1-ix^5}{1-x^6}=0$.",
    ),
    rec(
        "RLN-P5-C16-Entry16-2-3",
        r"If $x$ is a primitive $n$th root of unity with $n\equiv 2,3\,(5)$, then "
        r"$\dfrac{1+x}{1+x^2}\dfrac{1+x^3}{1+x^4}\cdots\dfrac{1+x^{n-1}}{1+x^n}=0$.",
    ),
    rec(
        "RLN-P5-C16-Entry16-2-4",
        r"If $x$ is a primitive $n$th root of unity with $n\equiv 1,4\,(5)$, then "
        r"$\dfrac{1+x}{1+x^2}\dfrac{1+x^3}{1+x^4}\cdots\dfrac{1+x^{n-2}}{1+x^{n-1}}=0$.",
    ),
    rec(
        "RLN-P5-C16-Entry16-2-5",
        r"If $x$ is a primitive $n$th root of unity with $n\equiv 0\,(5)$, then "
        r"$\dfrac{1+x}{1+x^2}\cdots\dfrac{1+x^{n-2}}{1+x^{n-1}}=0$ and "
        r"$\dfrac{1+x}{1+x^2}\cdots\dfrac{1+x^{n-1}}{1+x^n}=0$.",
    ),
    rec(
        "RLN-P5-C16-Entry16-2-6",
        r"With $t:=R(e^{-\pi\sqrt{2}})$ and $t':=R(e^{-2\pi\sqrt{2}})$, Ramanujan gives "
        r"$\dfrac{1}{t}-t=\dfrac{1+\xi}{\sqrt{5}}$ and $\dfrac{1}{t'}-t'=\dfrac{1+\sqrt{5}}{\xi}$, "
        r"where $\dfrac{\xi^2}{1+\xi}\dfrac{1}{1-\xi}=\dfrac{\sqrt{5}-1}{2}$.",
    ),
]
