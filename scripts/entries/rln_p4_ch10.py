"""RLN Part 4, Chapter 10 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C10 = ["zeta-function-identities"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C10}


CHAPTER_10 = [
    rec(
        "RLN-P4-C10-Entry10-2-1",
        r"Let $\operatorname{Re}x\ge0$. Then "
        r"$\displaystyle\sum_{n=1}^{\infty}\dfrac{e^{-n^2\pi x}}{n^2}"
        r"=\dfrac{\pi^2}{6}-\pi\sqrt{x}+\dfrac{1}{2}\pi x"
        r"-2\pi^2 x^{3/2}\displaystyle\sum_{n=1}^{\infty}\int_0^{\infty}te^{-\pi(n+tx)^2/x}\,dt$, "
        r"where the principal value of the square root is taken.",
    ),
    rec(
        "RLN-P4-C10-Entry10-2-2",
        r"Let $\operatorname{Re}x\ge0$. Then "
        r"$\displaystyle\sum_{n=1}^{\infty}\dfrac{\cos(n^2\pi x)}{n^2}"
        r"=\dfrac{\pi^2}{6}-\dfrac{\pi\sqrt{x}}{2}+2\pi^2 x^{3/2}"
        r"\displaystyle\sum_{n=1}^{\infty}\int_0^{\infty}te^{-2n\pi t}"
        r"\cos\!\left(\dfrac{\pi}{4}-\dfrac{\pi n^2}{x}+\pi t^2 x\right)dt$ "
        r"and "
        r"$\displaystyle\sum_{n=1}^{\infty}\dfrac{\sin(n^2\pi x)}{n^2}"
        r"=\dfrac{\pi\sqrt{x}}{2}-\dfrac{1}{2\pi x}+2\pi^2 x^{3/2}"
        r"\displaystyle\sum_{n=1}^{\infty}\int_0^{\infty}te^{-2n\pi t}"
        r"\sin\!\left(\dfrac{\pi}{4}-\dfrac{\pi n^2}{x}+\pi t^2 x\right)dt$, "
        r"where the principal value of the square root is taken.",
    ),
    rec(
        "RLN-P4-C10-Entry10-2-3",
        r"For $x\ge0$, "
        r"$\displaystyle\sum_{n=0}^{\infty}\dfrac{(-1)^n e^{-(2n+1)^2\pi x/4}}{2n+1}"
        r"=\dfrac{\pi}{4}-\pi\sqrt{x}\displaystyle\sum_{n=0}^{\infty}(-1)^n"
        r"\int_0^{\infty}e^{-\pi(2n+1+2tx)^2/(4x)}\,dt$.",
    ),
    rec(
        "RLN-P4-C10-Entry10-3-1",
        r"Let $a$ be an even positive integer. Then "
        r"$\displaystyle\sum_{n=1}^{\infty}\dfrac{\cos(\pi n^2/a)}{n^2}"
        r"=\dfrac{\pi^2}{6}-\dfrac{\pi^2}{\sqrt{a}\,a}\displaystyle\sum_{r=1}^{a}"
        r"\dfrac{r}{a}\!\left(1-\dfrac{r}{a}\right)\sin\!\left(\dfrac{\pi}{4}+\dfrac{\pi r^2}{a}\right)$, "
        r"$\displaystyle\sum_{n=1}^{\infty}\dfrac{\sin(\pi n^2/a)}{n^2}"
        r"=-\dfrac{\pi^2}{\sqrt{a}\,a}\displaystyle\sum_{r=1}^{a}"
        r"\dfrac{r}{a}\!\left(1-\dfrac{r}{a}\right)\cos\!\left(\dfrac{\pi}{4}+\dfrac{\pi r^2}{a}\right)$, "
        r"and "
        r"$\displaystyle\sum_{n=1}^{\infty}\dfrac{\sin\!\left(\dfrac{\pi}{4}+\dfrac{\pi n^2}{a}\right)}{n^2}"
        r"=\dfrac{\pi^2}{6\sqrt{2}}-\dfrac{\pi^2}{\sqrt{a}\,a}\displaystyle\sum_{r=1}^{a}"
        r"\dfrac{r}{a}\!\left(1-\dfrac{r}{a}\right)\cos\!\left(\dfrac{\pi r^2}{a}\right)$.",
    ),
    rec(
        "RLN-P4-C10-Entry10-3-2",
        r"If $a$ is an even positive integer, then "
        r"$\dfrac{4\pi^2}{a^{3/2}}\left(\dfrac{1}{8\pi}+\displaystyle\sum_{n=1}^{\infty}"
        r"\dfrac{n\cos(\pi n^2/a)}{e^{2n\pi}-1}\right)"
        r"-\dfrac{2^{3/2}\pi^2}{8\pi a}\left(\dfrac{1}{8\pi a}+\displaystyle\sum_{n=1}^{\infty}"
        r"\dfrac{n}{e^{2n\pi a}-1}\right)"
        r"=-\dfrac{\pi^2}{a^{5/2}}\displaystyle\sum_{r=1}^{a}r(a-r)\cos\!\left(\dfrac{\pi r^2}{a}\right)$.",
    ),
]
