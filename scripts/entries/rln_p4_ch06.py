"""RLN Part 4, Chapter 6 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C06 = ["euler-constant-manuscripts"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C06}


CHAPTER_6 = [
    rec(
        "RLN-P4-C06-Entry6-2-1",
        r"Let $p$, $q$, and $r$ be positive. Then "
        r"$\displaystyle\int_0^1\left(\dfrac{x^{p-1}}{1-x}-\dfrac{r x^{q-1}}{1-x^r}\right)dx"
        r"=\psi(q/r)-\psi(p)+\log r$.",
    ),
    rec(
        "RLN-P4-C06-Entry6-2-2",
        r"Suppose $a$, $b$, and $c$ are positive with $b>1$. Then "
        r"$\displaystyle\int_0^1\left(\dfrac{x^{c-1}}{1-x}-\dfrac{b x^{bc-1}}{1-x^b}\right)"
        r"\sum_{k=0}^{\infty}x^{abk}\,dx=\psi\!\left(\dfrac{a}{b}+c\right)-\log\dfrac{a}{b}$.",
    ),
    rec(
        "RLN-P4-C06-Entry6-2-3",
        r"We have "
        r"$\displaystyle\int_0^1\dfrac{1}{1+x}\sum_{k=1}^{\infty}x^{2k}\,dx=1-\gamma$, "
        r"$\displaystyle\int_0^1\dfrac{1+2x}{1+x+x^2}\sum_{k=1}^{\infty}x^{3k}\,dx=1-\gamma$, and "
        r"$\displaystyle\int_0^1\dfrac{1+\tfrac{1}{2\sqrt{x}}}{(1+\sqrt{x})(1+\sqrt{x}+x)}"
        r"\sum_{k=1}^{\infty}x^{(3/2)k}\,dx=1-\gamma$.",
    ),
    rec(
        "RLN-P4-C06-Entry6-3-1",
        r"If $a$, $b$, and $c$ are positive with $b>1$, then "
        r"$\displaystyle\int_0^1\dfrac{x^{c-1}-x^{bc-1}}{\log x}\sum_{k=0}^{\infty}x^{abk}\,dx"
        r"=-\log\!\left(1+\dfrac{bc}{a}\right)$.",
    ),
    rec(
        "RLN-P4-C06-Entry6-3-2",
        r"We have "
        r"$\displaystyle\int_0^1\dfrac{1-x}{\log x}\sum_{k=1}^{\infty}x^{2k}\,dx=-\log 2$.",
    ),
    rec(
        "RLN-P4-C06-Entry6-4-1",
        r"$\displaystyle\gamma=\log 2-\sum_{n=1}^{\infty}\dfrac{2n}{3^{n-1}}"
        r"\sum_{k=(3^{n-1}+1)/2}^{(3^n-1)/2}\dfrac{1}{(3k)^3-3k}$.",
    ),
]
