"""RLN Part 3, Chapter 4 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C04 = ["ranks-cranks-part-iii"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C04}


CHAPTER_4 = [
    rec(
        "RLN-P3-C04-Entry4-2-1",
        r"If $a_n:=a^n+a^{-n}$ and $|q|<\min(|a|,1/|a|)$, then $\dfrac{(q;q)_\infty^2}{(aq;q)_\infty(q/a;q)_\infty}=1-\displaystyle\sum_{m=1,n=0}^{\infty}(-1)^m q^{m(m+1)/2+mn}(a_{n+1}-a_n)$.",
    ),
    rec(
        "RLN-P3-C04-Entry4-2-2",
        r"Let $\rho_k=(-1)^k q^{k(k+1)/2}$. Then $\dfrac{(q;q)_\infty^2}{(aq;q)_\infty(q/a;q)_\infty}=\displaystyle\sum_{k=-\infty}^{\infty}\dfrac{\rho_k(1-a)}{1-aq^k}$. Also $S_1(a,q):=\dfrac{1}{1+a}+\displaystyle\sum_{n=1}^{\infty}\Bigl(\dfrac{(-1)^n q^{n(n+1)/2}}{1+aq^n}+\dfrac{(-1)^n q^{n(n+1)/2}}{a+q^n}\Bigr)$ and $S_2(a,q):=1+\displaystyle\sum_{m=1,n=0}^{\infty}(-1)^{m+n}q^{m(m+1)/2+mn}(a_{n+1}+a_n)$, where $a_0:=1$.",
    ),
    rec(
        "RLN-P3-C04-Entry4-2-3",
        r"With $S_1(a,q)$ and $S_2(a,q)$ as in Entry 4.2.2 and $F_a(q):=\dfrac{(q;q)_\infty}{(aq;q)_\infty(q/a;q)_\infty}$, $(1+a)S_1(a,q)=S_2(a,q)=F_{-a}(q)$.",
    ),
]
