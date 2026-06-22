"""RLN Part 5, Chapter 4 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C04 = ["third-order-mock-theta-partial-fractions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C04}


CHAPTER_4 = [
    rec(
        "RLN-P5-C04-Entry4-1-1",
        r"Suppose that $a$ and $b$ are real numbers such that $a^2+b^2=4$, and let "
        r"$f_a(q):=\displaystyle\sum_{n=0}^{\infty}\dfrac{q^{n^2}}{\prod_{j=1}^{n}(1+aq^j+q^{2j})}$. "
        r"Then "
        r"$\dfrac{b-a+2}{4}f_a(-q)+\dfrac{b+a+2}{4}f_{-a}(-q)-\dfrac{b}{2}f_b(q)"
        r"=\dfrac{(q^4;q^4)_\infty}{(-q;q^2)_\infty}"
        r"\displaystyle\prod_{n=1}^{\infty}\dfrac{1-bq^n+q^{2n}}{1+(a^2b^2-2)q^{4n}+q^{8n}}$.",
    ),
    rec(
        "RLN-P5-C04-Entry4-1-2",
        r"Let $a$ and $b$ be real numbers with $a^2+ab+b^2=3$, and let $f_a(q)$ be defined by (4.1.3). "
        r"Then "
        r"$(a+1)f_{-a}(q)+(b+1)f_{-b}(q)-(a+b-1)f_{a+b}(q)"
        r"=\dfrac{3(q^3;q^3)_\infty^2}{(q;q)_\infty}"
        r"\displaystyle\prod_{n=1}^{\infty}\dfrac{1}{1+ab(a+b)q^{3n}+q^{6n}}$.",
    ),
    rec(
        "RLN-P5-C04-Entry4-1-3",
        r"Let $f_a(q)$ and $\psi(q)$ be defined by (4.1.3) and (4.1.2), respectively. Then "
        r"$\dfrac{1+\sqrt{3}}{2}f_{-1}(-q)+\dfrac{3+\sqrt{3}}{6}f_1(-q)"
        r"=\displaystyle\sum_{n=0}^{\infty}\dfrac{q^{n^2}}{\prod_{j=1}^{n}(1+\sqrt{3}q^j+q^{2j})}"
        r"+\dfrac{2\sqrt{3}\,\psi(-q)(q^4;q^4)_\infty}{(q^6;q^6)_\infty}"
        r"\displaystyle\prod_{n=1}^{\infty}\dfrac{1}{1+\sqrt{3}q^n+q^{2n}}$.",
    ),
    rec(
        "RLN-P5-C04-Entry4-1-4",
        r"Let $\widetilde{\varphi}(q):=\displaystyle\sum_{n=0}^{\infty}\dfrac{q^{n^2}}{(-q^2;q^2)_n}$ "
        r"and let $\psi(q)$ be defined by (4.1.2). Then "
        r"$\dfrac{1}{2}(1+e^{\pi i/4})\widetilde{\varphi}(iq)+\dfrac{1}{2}(1+e^{-\pi i/4})\widetilde{\varphi}(-iq)"
        r"=f_{\sqrt{2}}(q)+\dfrac{1}{\sqrt{2}}\dfrac{\psi(-q)(-q^2;q^4)_\infty}"
        r"{\displaystyle\prod_{n=1}^{\infty}(1+\sqrt{2}q^n+q^{2n})}$.",
    ),
]
