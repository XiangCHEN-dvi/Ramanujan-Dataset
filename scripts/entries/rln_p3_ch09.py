"""RLN Part 3, Chapter 9 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C09 = ["circular-summation"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C09}


CHAPTER_9 = [
    rec(
        "RLN-P3-C09-Entry9-1-1",
        r"For each positive integer $n$ and $|ab| < 1$, $\displaystyle\sum_{-n/2 < r \leq n/2} \left(\sum_{\substack{k=-\infty \\ k \equiv r \pmod{n}}}^{\infty} a^{k(k+1)/(2n)} b^{k(k-1)/(2n)}\right)^n = f(a,b)\, F_n(ab)$, where $F_n(q) := 1 + 2n q^{(n-1)/2} + \cdots$ for $n \geq 3$.",
    ),
    rec(
        "RLN-P3-C09-Entry9-4-1",
        r"$f^2(a^{3/2}b^{1/2}, a^{1/2}b^{3/2}) + a f^2(a^{5/2}b^{3/2}, a^{-1/2}b^{1/2}) = f(a,b)\,\varphi(\sqrt{ab})$ and $R_2(q) = \varphi(q^2)$.",
    ),
    rec(
        "RLN-P3-C09-Entry9-4-2",
        r"$f^3(a^2b, ab^2) + a f^3(b, a^3b^2) + b f^3(a, a^2b^3) = f(a,b)\, F_3(ab)$, where $F_3(q) = \left(\dfrac{f^9(-q)}{f^3(-q^3)} + \dfrac{27q f^9(-q^3)}{f^3(-q)}\right)^{1/3} = \dfrac{\psi^3(q)}{\psi(q^3)} + \dfrac{3q\,\psi^3(q^3)}{\psi(q)}$, and $R_3(q) = a(q^2) = \varphi(q^2)\varphi(q^6) + 4q^2\psi(q^4)\psi(q^{12})$.",
    ),
    rec(
        "RLN-P3-C09-Entry9-4-3",
        r"$F_4(q) = \varphi^3(q^2) + (2\sqrt{q})^3 \psi^3(q^4)$ and $R_4(q) = \dfrac{1}{2}\bigl(\varphi^3(q) + \varphi^3(-q)\bigr)$.",
    ),
    rec(
        "RLN-P3-C09-Entry9-4-4",
        r"$F_5(q) = \dfrac{f^5(-q)}{f(-q^5)} + \dfrac{5q f^5(-q^5)}{f(-q)}$ and $R_5(q) = \dfrac{f^5(-q^2)}{f(-q^{10})} + \dfrac{25q^2 f^5(-q^{10})}{f(-q^2)}$.",
    ),
    rec(
        "RLN-P3-C09-Entry9-4-5",
        r"$F_7(q) = \dfrac{f^7(-q)}{f(-q^7)} + 7q f^3(-q)f^3(-q^7) + \dfrac{7q^2 f^7(-q^7)}{f(-q)}$.",
    ),
]
