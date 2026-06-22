"""RLN Part 2, Chapter 2 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C02 = ["sears-thomae-transformation"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C02}


CHAPTER_2 = [
    rec(
        "RLN-P2-C02-Entry2-2-1",
        r"For $0<|aq|<1$, $\displaystyle\sum_{n=0}^{\infty}\frac{(-q;q)_{2n}q^n}{(aq;q^2)_{n+1}(q/a;q^2)_{n+1}}=\sum_{n=0}^{\infty}\frac{(-q/a;q)_{2n}a^nq^n}{(q;q^2)_{n+1}(q/a;q^2)_{n+1}}$.",
    ),
    rec(
        "RLN-P2-C02-Entry2-2-2",
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{(-q^2;q^2)_nq^{n+1}}{(q;q^2)_{n+1}}=\sum_{n=0}^{\infty}\frac{(-q;q^2)_nq^{(n+1)^2}}{(q;q^2)_{2n+1}}$.",
    ),
    rec(
        "RLN-P2-C02-Entry2-2-3",
        r"For arbitrary complex numbers $a$, $b$, and $c$, $(aq)_\infty(-bq)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{(-aq/b)_nb^nq^{n(n+1)/2}}{(q)_n(-cq)_n}=(aq)_\infty\sum_{n=0}^{\infty}\frac{(bc/a)_na^nq^{n^2+n}}{(q)_n(-bq)_n(-cq)_n}$.",
    ),
    rec(
        "RLN-P2-C02-Entry2-2-4",
        r"For arbitrary complex numbers $a$ and $b$, $\displaystyle\sum_{n=0}^{\infty}\frac{a^nq^{n(n+1)/2}}{(q)_n(-bq)_n}=(-aq)_\infty\sum_{n=0}^{\infty}\frac{(-1)^n(ab)_nq^{n(3n+1)/2}}{(q)_n(-aq)_n(-bq)_n}$.",
    ),
    rec(
        "RLN-P2-C02-Entry2-3-1",
        r"For arbitrary $a$ with $|bq|<1$, $\displaystyle\sum_{n=0}^{\infty}\frac{(ab)_nq^{n^2}}{(aq)_n(bq)_n}=1+a\sum_{n=1}^{\infty}\frac{b^nq^n}{(aq)_n}$ and $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^na^{2n}q^{n^2}}{(a^2q^2;q^2)_n}=1-a\sum_{n=1}^{\infty}\frac{a^nq^n}{(-aq)_n}$.",
    ),
    rec(
        "RLN-P2-C02-Entry2-3-2",
        r"With $\varphi(q)$ as in (1.4.9), $\displaystyle\sum_{n=0}^{\infty}\frac{(-1;q)_n^2q^{n(n+1)/2}}{(q;q)_n(q;q^2)_n}=\dfrac{\varphi(q)}{\varphi(-q)}$.",
    ),
    rec(
        "RLN-P2-C02-Entry2-3-3",
        r"With $\varphi(q)$ and $\psi(q)$ as in (1.4.9) and (1.4.10), $\displaystyle\sum_{n=0}^{\infty}\frac{(-q;q)_n^2q^{n(n+1)/2}}{(q;q)_n(q;q^2)_{n+1}}=\dfrac{\psi(q^2)}{\varphi(-q)}$.",
    ),
    rec(
        "RLN-P2-C02-Entry2-3-4",
        r"With $f(a,b)$ as in (1.4.8), $\displaystyle\sum_{n=0}^{\infty}\frac{(-q^2;q^4)_nq^{n^2+n}}{(q^2;q^2)_n(q^2;q^4)_n(1-q^{2n+1})}=\dfrac{f(-q^6,-q^{10})+qf(-q^2,-q^{14})}{\varphi(-q^2)}$.",
    ),
    rec(
        "RLN-P2-C02-Entry2-3-5",
        r"For any complex $b$ and $|aq|<1$, $\displaystyle\sum_{n=0}^{\infty}\frac{(q;q^2)_n(b^2q/a;q^2)_na^nq^n}{(-bq;q)_{2n+1}}=\sum_{n=0}^{\infty}\frac{(-1)^n(-aq/b)_nb^nq^{n(n+1)/2}}{(aq;q^2)_{n+1}}$.",
    ),
]
