"""Part 5, Chapter 33 entries — elliptic functions to alternative bases (curated LaTeX).

Only the two enigmatic notebook entries from Section 13 (p. 392) are included;
Berndt's ~62 theorems and corollaries in this chapter are excluded.
"""

from __future__ import annotations

TOPICS = ["elliptic-functions-alternative-bases"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS}


CHAPTER_33 = [

    rec(
        "RN-P5-C33-Entry13-01",
        r"Entry 13.1 (p. 392). Let $0 < x < \tfrac12$. If $y$ is given by (1.8) and "
        r"$z={}_2F_1(\tfrac12,\tfrac12;1;4x(1-x))$, then "
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{(4n+1)(4)_n(3)_n}{(n!)^3}\,[4x(1-x)]^n "
        r"=\frac{1}{1-2x}\left\{\frac{d}{dx}\log f(-e^{-y})-\frac12\frac{d}{dx}\log f(-e^{-2y})\right\}$, "
        r"where $f(q):=\sum_{n=1}^{\infty}q^{n^2}$. "
        r"If $y$ is given by (1.7) and $z={}_2F_1(1,2;1;x)$, then "
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{(3n+1)(7)_n(3)_n(\tfrac13)_n}{(n!)^3}\,[4x(1-x)]^n "
        r"=\frac{1}{1-2x}\left\{\frac{d}{dx}\log f(-e^{-y})+\frac13\frac{d}{dx}\log f(-e^{-3y})\right\}$.",
    )
,
    rec(
        "RN-P5-C33-Entry13-02",
        r"Entry 13.2 (p. 392). At the bottom of page 392, Ramanujan recorded "
        r"$\displaystyle\frac{1-2x}{1+x}+\frac{x^2}{1+x}+\frac{x^4}{1+x}+\cdots "
        r"=\frac{2}{3}\frac{2-(GG')^{1/3}}{(GG')^{1/3}}+\frac{2+(gg')^{1/3}}{3(gg')^{1/3}}$ "
        r"and $\displaystyle\frac{2}{3}\frac{2-(GG')^{1/3}}{(GG')^{1/3}}=\frac{2}{3}\frac{2+(gg')^{1/3}}{(gg')^{1/3}}$ "
        r"(Berndt's interpretation of Ramanujan's enigmatic notation; $G$, $G'$, $g$, and $g'$ are undetermined invariants).",
    )
,
]
