"""RLN Part 2, Chapter 4 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C04 = ["well-poised-series"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C04}


CHAPTER_4 = [
    rec(
        "RLN-P2-C04-Entry4-2-1",
        r"For any complex $a$, $(aq)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{a^nq^{n^2}}{(q)_n}=\sum_{n=0}^{\infty}\frac{(-1)^n(a)_n(1-aq^{2n})}{(q)_n(1-a)}a^{2n}q^{n(5n-1)/2}=\sum_{n=0}^{\infty}\frac{(-1)^n(aq)_n(1-a^2q^{4n+2})}{(q)_n}a^{2n}q^{n(5n+1)/2}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-2",
        r"For any complex $a$, $(aq)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{a^nq^{n^2+n}}{(q)_n}=\sum_{n=0}^{\infty}\frac{(-1)^n(aq)_n(1-aq^{2n+1})}{(q)_n}a^{2n}q^{n(5n+3)/2}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-3",
        r"For arbitrary complex numbers $a$, $b$, and $c$, $(aq)_\infty(-bq)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{(-aq/b)_nb^nq^{n(n+1)/2}}{(q)_n(-cq)_n}=\sum_{n=0}^{\infty}\frac{(-1)^n(aq)_n(-aq/b)_n(-aq/c)_n(1-aq^{2n+1})b^nc^nq^{n(3n+1)/2}}{(q)_n(-bq)_n(-cq)_n}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-4",
        r"For arbitrary $a$ and $b$, $(-aq)_\infty(-bq)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{(aq/b)_nb^nq^{n(n+1)/2}}{(q)_n}=\sum_{n=0}^{\infty}\frac{(aq/b)_n(-aq)_n(1+aq^{2n+1})a^nb^nq^{2n^2+n}}{(q)_n(-bq)_n}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-5",
        r"For complex numbers $a$ and $\lambda$, $(\lambda q)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{\lambda^nq^{n^2}}{(q)_n(aq)_n}=1+\sum_{n=0}^{\infty}\frac{(\lambda/a)_n(\lambda q)_{n-1}(1-\lambda q^{2n})\lambda^na^nq^{2n^2}}{(q)_n(aq)_n}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-6",
        r"With $\psi(q)$ as in (1.4.10), $\dfrac{1}{\psi(q)}=\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n(q;q^2)_nq^{n^2}}{(q^2;q^2)_{2n}}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-7",
        r"With $\varphi(q)$ and $\psi(q)$ as in (1.4.9) and (1.4.10), $\dfrac{\varphi(q^3)}{\psi(q)}=\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n(q;q^2)_nq^{n^2}}{(q^4;q^4)_n}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-8",
        r"$\dfrac{\varphi(-q^3)}{\varphi(-q)}=\displaystyle\sum_{n=0}^{\infty}\frac{(-1;q)_nq^{n^2}}{(q;q)_n(q;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-9",
        r"$\dfrac{\varphi(-q^3)}{\varphi(-q)}=\displaystyle\sum_{n=0}^{\infty}\frac{(-q;q)_nq^{n^2}}{(q;q)_n(q;q^2)_{n+1}}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-10",
        r"$\dfrac{\varphi(q^3)}{\varphi(-q^2)}=\displaystyle\sum_{n=0}^{\infty}\frac{(-1;q^2)_nq^{n(n+1)}}{(q;q)_{2n}}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-11",
        r"With $f(a,b)$ as in (1.4.8) and $\psi(q)$ as in (1.4.10), $\dfrac{f(q,q^5)}{\psi(q)}=\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n(q;q^2)_nq^{n(n+2)}}{(q^4;q^4)_n}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-12",
        r"$\dfrac{f(-q,-q^5)}{\varphi(-q)}=\displaystyle\sum_{n=0}^{\infty}\frac{(-q;q)_nq^{n^2+n}}{(q;q)_n(q;q^2)_{n+1}}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-13",
        r"$\dfrac{f(q,q^5)}{\varphi(-q^2)}=\displaystyle\sum_{n=0}^{\infty}\frac{(-q^2;q^2)_nq^{n(n+1)}}{(q;q)_{2n+1}}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-14",
        r"$\dfrac{1}{\psi(q)}\displaystyle\sum_{n=0}^{\infty}(-1)^nq^{3n^2+2n}(1+q^{2n+1})=\sum_{n=0}^{\infty}\frac{(-1)^n(q;q^2)_nq^{n(n+2)}}{(q^2;q^2)_{2n}}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-15",
        r"$\dfrac{\psi(q^4)}{f(q,q^7)}=\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n(q;q^2)_nq^{n^2}}{(q^2;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-2-16",
        r"For complex numbers $a$ and $b$, $(abq)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{a^nb^nq^{n^2}}{(-aq)_n(-bq)_n}=(1+a)(1+b)\sum_{n=0}^{\infty}\frac{(-1)^n(abq)_{n-1}(1-abq^{2n})a^nb^nq^{n(3n+1)/2}}{(q)_n(1+aq^n)(1+bq^n)}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-3-1",
        r"For complex numbers $a$ and $b$, $\displaystyle\sum_{n=0}^{\infty}\frac{(-aq/b;q)_nb^nq^{n(n+1)/2}}{(q;q)_n(aq^2;q^2)_n}=\dfrac{(-bq;q)_\infty}{(aq;q)_\infty}\sum_{n=0}^{\infty}\frac{(-1)^n(aq;q^2)_n(-aq/b;q)_{2n}(1-aq^{4n+1})a^nb^{2n}q^{5n^2+n}}{(q^2;q^2)_n(-bq;q)_{2n}}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-3-2",
        r"For any complex $a$, $\displaystyle\sum_{n=0}^{\infty}\frac{a^nq^{n(n+1)/2}}{(-aq^2;q^2)_n}=\sum_{n=0}^{\infty}\frac{(q;q^2)_n(1+aq^{4n+1})a^{3n}q^{5n^2+n}}{(-aq^2;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-3-3",
        r"For arbitrary complex numbers $a$ and $b$, $\displaystyle\sum_{n=0}^{\infty}\frac{(-bq;q^2)_na^nq^{n(n+1)/2}}{(-aq^2;q^2)_n(-bq;q)_n}=\sum_{n=0}^{\infty}\frac{(-1)^n(aq/b;q^2)_n(q;q^2)_n(1+aq^{4n+1})a^{2n}b^nq^{4n^2+n}}{(-aq^2;q^2)_n(-bq^2;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-3-4",
        r"For $|aq|<1$, $\displaystyle\sum_{n=0}^{\infty}\frac{(q;q^2)_n(aq;q^2)_na^nq^n}{(-aq;q)_{2n+1}}=\sum_{n=0}^{\infty}(-1)^na^nq^{n(n+1)}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-3-5",
        r"For arbitrary complex numbers $a$ and $b$, $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n(a^2q^2/b;q^2)_nb^nq^{n(n+1)}}{(q^2;q^2)_n(-aq;q)_{2n+1}}=\dfrac{(bq^2;q^2)_\infty}{(a^2q^2;q^2)_\infty}\sum_{n=0}^{\infty}\frac{(aq;q)_n(a^2q^2/b;q^2)_n(1-aq^{2n+1})a^nb^nq^{n(5n+3)/2}}{(q;q)_n(bq^2;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-3-6",
        r"For arbitrary $a$, $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^na^{2n}q^{n(n+1)}}{(-aq)_{2n+1}}=\sum_{n=0}^{\infty}\frac{(-q)_n(1-aq^{2n+1})a^{3n}q^{n(5n+3)/2}}{(-aq)_n}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-3-7",
        r"For complex numbers $a$ and $b$, $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n(a^2q^2/b;q^2)_nb^nq^{n^2+n}}{(q^2;q^2)_n(-aq;q)_{2n}}=\dfrac{(bq^2;q^2)_\infty}{(a^2q^2;q^2)_\infty}\sum_{n=0}^{\infty}\frac{(aq;q)_n(a^2q^2/b;q^2)_n(1-a^2q^{4n+2})a^nb^nq^{n(5n+1)/2}}{(q;q)_n(bq^2;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-3-8",
        r"For any complex $a$, $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^na^{2n}q^{n(n+1)}}{(-aq)_{2n}}=\sum_{n=0}^{\infty}\frac{(-q)_n(1-a^2q^{4n+2})a^{3n}q^{n(5n+1)/2}}{(-aq)_n}$.",
    ),
    rec(
        "RLN-P2-C04-Entry4-3-9",
        r"For arbitrary complex $a$, $(aq;q)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{a^nq^{n^2}}{(q;q)_n(aq;q^2)_n}=\sum_{n=0}^{\infty}\frac{(-1)^n(aq;q^2)_n(1-a^2q^{8n+2})a^{3n}q^{7n^2}}{(q^2;q^2)_n}$.",
    ),
]
