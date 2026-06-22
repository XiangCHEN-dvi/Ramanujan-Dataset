"""RLN Part 2, Chapter 7 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C07 = ["special-identities"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C07}


CHAPTER_7 = [
    rec("RLN-P2-C07-Entry7-2-1", r"For any complex numbers $a$ and $b$, $\sum_{n=0}^{\infty}\frac{a^n b^n q^{n^2}}{(-aq)_n(-bq)_n}=\sum_{n=0}^{\infty}\frac{(-1)^n a^{2n}b^n q^{2n^2}}{(-aq)_n(-bq)_{2n}}+\sum_{n=0}^{\infty}\frac{(-1)^n a^{2n+1}b^{n+1} q^{2n^2+3n+1}}{(-aq)_n(-bq)_{2n+1}}$."),
    rec("RLN-P2-C07-Entry7-2-2", r"For complex numbers $a$ and $b$ with $a \neq 0$, $\sum_{n=0}^{\infty}\frac{a^n b^n q^{n^2/4}}{(q)_n}\sum_{m=0}^{\infty}a^{-2m}q^{m^2}(bq)_m+\sum_{n=0}^{\infty}\frac{a^n b^n q^{(n+1)^2/4}}{(q)_n}\sum_{m=0}^{\infty}a^{-2m-1}q^{m^2+m}(bq)_m=\frac{1}{(bq)_{\infty}}\sum_{n=-\infty}^{\infty}a^n q^{n^2/4}-(1-b)\sum_{n=1}^{\infty}a^n q^{n^2/4}\sum_{j=0}^{n-1}\frac{b^j}{(q)_j}$."),
    rec("RLN-P2-C07-Entry7-2-3", r"For $a \neq 0$, $\left(\sum_{n=0}^{\infty}\frac{a^n q^{n^2/4}}{(q)_n}\right)\left(\sum_{n=0}^{\infty}\frac{a^{-2n}q^{n^2}}{(q)_n}\right)+\left(\sum_{n=0}^{\infty}\frac{a^n q^{(n+1)^2/4}}{(q)_n}\right)\left(\sum_{n=0}^{\infty}\frac{a^{-2n-1}q^{n^2+n}}{(q)_n}\right)=\frac{1}{(q)_{\infty}}\sum_{n=-\infty}^{\infty}a^n q^{n^2/4}$."),
    rec("RLN-P2-C07-Entry7-2-4", r"For $a \neq 0$, $\left(\sum_{n=-\infty}^{\infty}a^n q^{n^2/4}\right)\left(\sum_{n=0}^{\infty}\frac{(-1)^n a^n q^{n^2/4}}{(q)_n}\right)-\left(\sum_{n=-\infty}^{\infty}(-1)^n a^n q^{n^2/4}\right)\left(\sum_{n=0}^{\infty}\frac{a^n q^{n^2/4}}{(q)_n}\right)=2(q)_{\infty}\sum_{n=0}^{\infty}a^{-2n-1}q^{(2n+1)^2/4}(q)_n$."),
    rec("RLN-P2-C07-Entry7-2-5", r"For $a \neq 0$, $\left(1+\frac{1}{a}\right)\sum_{n=0}^{\infty}\frac{(-1)^n(b/a)^n q^{n(n+1)/2}}{(-bq)_n}=\frac{1}{a}\sum_{n=0}^{\infty}\frac{(-1)^n(b/a)^n q^{n(n+1)/2}}{(-aq)_n(-bq)_{2n+1}}+\sum_{n=0}^{\infty}\frac{(-1)^n(b/a)^n q^{n(n+3)/2}}{(-aq)_n(-bq)_{2n}}$."),
    rec("RLN-P2-C07-Entry7-3-1", r"$\sum_{n=0}^{\infty}\frac{q^{n(n+1)/2}}{(-q)_n}=1+q\sum_{n=0}^{\infty}(-1)^n(q)_n q^n$."),
    rec("RLN-P2-C07-Entry7-3-2", r"If $S:=(-q)_{\infty}$, then $\sum_{n=0}^{\infty}\frac{q^{n(n+1)/2}}{(-q)_n}=\frac{2}{S^2}+\sum_{n=0}^{\infty}(S-(-q)^n)-S\sum_{n=1}^{\infty}\frac{q^n}{1-q^n}$."),
    rec("RLN-P2-C07-Entry7-3-3", r"Let $S:=1/(q;q^2)_{\infty}$. Then $\sum_{n=0}^{\infty}\frac{q^{n(n+1)/2}}{(-q;q)_n}=\frac{2}{S^2}+\sum_{n=0}^{\infty}\bigl(S-(q;q^2)_{n+1}\bigr)-2S\sum_{n=1}^{\infty}\frac{q^{2n}}{1-q^{2n}}$."),
    rec("RLN-P2-C07-Entry7-4-1", r"$\sum_{n=0}^{\infty}\frac{(-1)^n q^{n(n+1)/2}}{(-q;q)_{2n}}=\sum_{n=0}^{\infty}\frac{(-q)^{n(n+1)/2}}{(-q^2;q^2)_n}-2\sum_{n=1}^{\infty}\frac{(-1)^n q^{2n^2}}{(-q;q^2)_{2n}}$, and $\varphi(-q)\sum_{n=0}^{\infty}\frac{q^{n(n+1)/2}}{(q^2;q^2)_n}=\sum_{n=0}^{\infty}\frac{(-q)^{n(n+1)/2}}{(-q^2;q^2)_n}+2\sum_{n=1}^{\infty}\frac{(-1)^n q^{2n^2}}{(-q;q^2)_{2n}}$."),
]
