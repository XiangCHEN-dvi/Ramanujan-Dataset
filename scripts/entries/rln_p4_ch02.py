"""RLN Part 4, Chapter 2 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C02 = ["double-series-bessel-functions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C02}


CHAPTER_2 = [
    rec(
        "RLN-P4-C02-Entry2-1-1",
        r"Let $F(x):=[x]$ if $x$ is not an integer and $F(x):=x-\tfrac{1}{2}$ if $x$ is an integer. "
        r"If $0<\theta<1$ and $x>0$, then "
        r"$\displaystyle\sum_{n=1}^{\infty}F\!\left(\dfrac{x}{n}\right)\sin(2\pi n\theta)"
        r"=\dfrac{\pi x}{1/2-\theta}-\dfrac{1}{4}\cot(\pi\theta)"
        r"+\dfrac{1}{2\sqrt{x}}\displaystyle\sum_{m=1}^{\infty}\sum_{n=0}^{\infty}"
        r"\left(\dfrac{J_1\!\bigl(4\pi\sqrt{m(n+\theta)x}\bigr)}{\sqrt{m(n+\theta)}}"
        r"-\dfrac{J_1\!\bigl(4\pi\sqrt{m(n+1-\theta)x}\bigr)}{\sqrt{m(n+1-\theta)}}\right)$.",
    ),
    rec(
        "RLN-P4-C02-Entry2-1-2",
        r"Let $F(x):=[x]$ if $x$ is not an integer and $F(x):=x-\tfrac{1}{2}$ if $x$ is an integer, "
        r"and let $I_\nu(z):=-Y_\nu(z)-\dfrac{2}{\pi}K_\nu(z)$. "
        r"If $x>0$ and $0<\theta<1$, then "
        r"$\displaystyle\sum_{n=1}^{\infty}F\!\left(\dfrac{x}{n}\right)\cos(2\pi n\theta)"
        r"=\dfrac{1}{4}-x\log(2\sin(\pi\theta))"
        r"+\dfrac{1}{2\sqrt{x}}\displaystyle\sum_{m=1}^{\infty}\sum_{n=0}^{\infty}"
        r"\left(\dfrac{I_1\!\bigl(4\pi\sqrt{m(n+\theta)x}\bigr)}{\sqrt{m(n+\theta)}}"
        r"+\dfrac{I_1\!\bigl(4\pi\sqrt{m(n+1-\theta)x}\bigr)}{\sqrt{m(n+1-\theta)}}\right)$.",
    ),
]
