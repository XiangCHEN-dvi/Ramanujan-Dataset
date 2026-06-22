"""RLN Part 2, Chapter 5 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C05 = ["baileys-lemma-theta-expansions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C05}


CHAPTER_5 = [
    rec("RLN-P2-C05-Entry5-3-1", r"For $a \neq 0$, $\sum_{n=0}^{\infty}\frac{(-aq;q^2)_n(-q/a;q^2)_n}{(q^2;q^2)_{2n}}q^{2n^2}=\frac{f(aq^3,q^3/a)}{(q^2;q^2)_{\infty}}$."),
    rec("RLN-P2-C05-Entry5-3-2", r"If $f(a,b)$ and $\psi(q)$ are defined by (1.4.8) and (1.4.10), then $\sum_{n=0}^{\infty}\frac{(-q;q^2)_n}{(q;q)_{2n}}q^{n^2}=\frac{f(q^2,q^4)}{\psi(-q)}$."),
    rec("RLN-P2-C05-Entry5-3-3", r"If $f(a,b)$ and $\psi(q)$ are defined by (1.4.8) and (1.4.10), then $\sum_{n=0}^{\infty}\frac{(q;q^2)_n^2}{(q^2;q^2)_{2n}}q^{2n^2}=\frac{f(q,q^2)}{\psi(q)}$."),
    rec("RLN-P2-C05-Entry5-3-4", r"If $f(a,b)$ and $f(-q)$ are defined by (1.4.8) and (3.1.3), then $\sum_{n=0}^{\infty}\frac{(q^3;q^6)_n}{(q;q^2)_n(q^2;q^2)_{2n}}q^{2n^2}=\frac{f(-q,-q^5)}{f(-q)(q^9;q^{18})_{\infty}}$."),
    rec("RLN-P2-C05-Entry5-3-5", r"If $f(a,b)$ and $\psi(q)$ are defined by (1.4.8) and (1.4.10), and if $a \neq 0$, then $\sum_{n=0}^{\infty}\frac{(-aq;q^2)_n(-a^{-1}q;q^2)_n}{(q;q^2)_n(q^4;q^4)_n}q^{n^2}=\frac{f(aq^2,q^2/a)}{\psi(-q)}$."),
    rec("RLN-P2-C05-Entry5-3-6", r"If $f(-q)$ is defined by (3.1.3), then $\sum_{n=0}^{\infty}\frac{(\pm 1)^n(-q;q^2)_n}{(q^4;q^4)_n}q^{n^2}=\frac{f(\pm q,\pm q^2)}{f(-q^4)}$."),
    rec("RLN-P2-C05-Entry5-3-7", r"If $\psi(q)$ is defined by (1.4.10) and $f(-q)$ is defined by (3.1.3), then $\sum_{n=0}^{\infty}\frac{(-q;q^2)_n}{(q^4;q^4)_n}q^{n^2+2n}=\frac{\psi(q^3)}{f(-q^4)}$."),
    rec("RLN-P2-C05-Entry5-3-8", r"$\sum_{n=0}^{\infty}\frac{(-q^3;q^6)_n}{(q^2;q^2)_{2n}}q^{n^2}=\frac{\psi(-q^2)}{\psi(-q)(-q^6;q^{12})_{\infty}}$."),
    rec("RLN-P2-C05-Entry5-3-9", r"$\sum_{n=0}^{\infty}\frac{(q^3;q^6)_n q^{n^2}}{(q;q^2)_{2n}(q^4;q^4)_n}=\frac{\psi(q^2)}{\psi(-q)(q^6;q^{12})_{\infty}}$."),
    rec("RLN-P2-C05-Entry5-3-10", r"Formally, for $a \neq 0$, $\sum_{n=0}^{\infty}\frac{(-1)^n(-aq;q^2)_n(-q/a;q^2)_n}{(q^4;q^4)_n}=\frac{f(-aq,-q/a)}{2\psi(q^2)}$."),
    rec("RLN-P2-C05-Entry5-4-1", r"For $a \neq 0,-1$, $\frac{1}{a^{1/2}+a^{-1/2}}\sum_{n=0}^{\infty}(-1)^n(a^{n+1/2}+a^{-n-1/2})q^{n(n+1)}=\sum_{n=0}^{\infty}\frac{(-1)^n(-aq)_n(-q/a)_n}{(q^{n+1})_{n+1}}q^{n(n+1)/2}$."),
    rec("RLN-P2-C05-Entry5-4-2", r"$\sum_{n=0}^{\infty}\frac{(-1)^n(q^3;q^3)_n}{(q;q)_{2n+1}}q^{n(n+1)/2}=f(q^{12},q^6)$."),
    rec("RLN-P2-C05-Entry5-4-3", r"Formally, $\left(1+\frac{1}{a}\right)\sum_{n=0}^{\infty}\frac{(-1)^n(-aq;q)_n(-q/a;q)_n}{(q;q^2)_{n+1}}=\frac{1}{2}\sum_{n=0}^{\infty}(-1)^n(a^n+a^{-n-1})q^{n(n+1)/2}$."),
    rec("RLN-P2-C05-Entry5-4-4", r"For $a \neq 0$, $\left(1+\frac{1}{a}\right)\sum_{n=0}^{\infty}\frac{(aq;q^2)_n(q/a;q^2)_n}{(-q;q)_{2n+1}}q^n=\sum_{n=0}^{\infty}(-1)^n(a^n+a^{-n-1})q^{n^2+n}$."),
]
