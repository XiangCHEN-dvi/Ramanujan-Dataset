"""RLN Part 2, Chapter 6 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C06 = ["partial-theta-functions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C06}


CHAPTER_6 = [
    rec("RLN-P2-C06-Entry6-3-1", r"For $a \neq 0$ and any complex number $b$, $\sum_{n=0}^{\infty}\frac{q^n}{(-aq)_n(-bq)_n}=\frac{1}{(-aq)_{\infty}(-bq)_{\infty}}\sum_{m=0}^{\infty}(-1)^{m+1}a^{-m-1}b^m q^{m(m+1)/2}+\left(1+\frac{1}{a}\right)\sum_{m=0}^{\infty}\frac{(-1)^m a^{-m}b^m q^{m(m+1)/2}}{(-bq)_m}$."),
    rec("RLN-P2-C06-Entry6-3-2", r"For $a \neq 0$, $\sum_{n=0}^{\infty}\frac{q^n}{(-aq)_n(-q/a)_n}=(1+a)\sum_{n=0}^{\infty}a^{3n}q^{n(3n+1)/2}(1-a^2 q^{2n+1})-\frac{1}{(-aq)_{\infty}(-q/a)_{\infty}}\sum_{n=0}^{\infty}(-1)^n a^{2n+1}q^{n(n+1)/2}$."),
    rec("RLN-P2-C06-Entry6-3-3", r"For $ab \neq 0$, $\left(1+\frac{1}{b}\right)\sum_{n=0}^{\infty}\frac{(-1)^n a^n b^{-n}q^{n(n+1)/2}}{(-aq)_n}-\left(1+\frac{1}{a}\right)\sum_{n=0}^{\infty}\frac{(-1)^n a^{-n}b^n q^{n(n+1)/2}}{(-bq)_n}=\left(\frac{1}{b}-\frac{1}{a}\right)\frac{(aq/b)_{\infty}(bq/a)_{\infty}(q)_{\infty}}{(-aq)_{\infty}(-bq)_{\infty}}$."),
    rec("RLN-P2-C06-Entry6-3-4", r"For $a \neq 0$, $\sum_{n=0}^{\infty}\frac{q^{2n+1}}{(-aq;q^2)_{n+1}(-q/a;q^2)_{n+1}}=\sum_{n=0}^{\infty}a^{3n+1}q^{3n^2+2n}(1-aq^{2n+1})-\frac{1}{(-aq;q^2)_{\infty}(-q/a;q^2)_{\infty}}\sum_{n=0}^{\infty}(-1)^n a^{2n+1}q^{n(n+1)}$."),
    rec("RLN-P2-C06-Entry6-3-5", r"For any complex number $a$, $\sum_{n=0}^{\infty}\frac{(aq;q^2)_n q^n}{(-q;q)_n}=2\sum_{n=0}^{\infty}(-1)^n a^n q^{n(n+1)}-\frac{1}{(q;q^2)_{\infty}(aq;q^2)_{\infty}}\sum_{n=0}^{\infty}\frac{(-1)^n a^n q^{n(n+1)}}{(aq;q^2)_{n+1}}$."),
    rec("RLN-P2-C06-Entry6-3-6", r"For $a \neq 0$, with $f(a,b)$ as in (1.4.8), $\left(1+\frac{1}{a}\right)\sum_{n=0}^{\infty}\frac{(q;q^2)_n q^{2n+1}}{(-aq;q^2)_{n+1}(-q/a;q^2)_{n+1}}=\sum_{n=0}^{\infty}(-1)^n a^n q^{n(n+1)/2}-\frac{f(aq,q/a)}{(q;q)_{\infty}}\sum_{n=0}^{\infty}a^{3n}q^{3n^2+n}(1-a^2 q^{4n+2})$."),
    rec("RLN-P2-C06-Entry6-3-7", r"For $a \neq 0$, with $f(a,b)$ and $\psi(q)$ as in (1.4.8) and (1.4.10), $\left(1+\frac{1}{a}\right)\sum_{n=0}^{\infty}\frac{(-q;q)_{2n}q^{2n+1}}{(aq;q^2)_{n+1}(q/a;q^2)_{n+1}}=\psi(q)f(-aq,-q/a)\sum_{n=0}^{\infty}(-a)^n q^{n(n+1)/2}-\sum_{n=0}^{\infty}(-a)^n q^{n(n+1)}$."),
    rec("RLN-P2-C06-Entry6-3-8", r"$\sum_{n=0}^{\infty}\frac{(-q;q)_{2n}q^{2n+1}}{(q;q^2)_{n+1}^2}=2(q;q^2)_{\infty}^3\sum_{n=0}^{\infty}(-1)^n q^{n(n+1)/2}-\sum_{n=0}^{\infty}(-1)^n q^{n(n+1)}$."),
    rec("RLN-P2-C06-Entry6-3-9", r"For $a \neq 0$, $\sum_{n=0}^{\infty}\frac{(q;q^2)_n q^{2n}}{(-aq^2;q^2)_n(-q^2/a;q^2)_n}=(1+a)\sum_{n=0}^{\infty}(-a)^n q^{n(n+1)/2}-\frac{a(q;q^2)_{\infty}}{(-aq^2;q^2)_{\infty}(-q^2/a;q^2)_{\infty}}\sum_{n=0}^{\infty}a^{3n}q^{3n^2+2n}(1-aq^{2n+1})$."),
    rec("RLN-P2-C06-Entry6-3-10", r"$\sum_{n=0}^{\infty}\frac{(-q;q^2)_n q^{2n}}{(-q^4;q^4)_n}=\sum_{n=0}^{\infty}(-1)^n q^{n(n+1)/2}+\frac{q\psi(q)}{(q^8;q^8)_{\infty}}\sum_{n=0}^{\infty}(-1)^n q^{12n^2+8n}(1+q^{8n+4})$."),
    rec("RLN-P2-C06-Entry6-3-11", r"For $a \neq 0$, $\sum_{n=0}^{\infty}\frac{(q;q^2)_n q^n}{(-aq;q)_n(-q/a;q)_n}=(1+a)\sum_{n=0}^{\infty}(-a)^n q^{n(n+1)/2}-\frac{a(q;q^2)_{\infty}}{(-aq;q)_{\infty}(-q/a;q)_{\infty}}\sum_{n=0}^{\infty}(-1)^n a^{2n}q^{n(n+1)}$."),
    rec("RLN-P2-C06-Entry6-3-12", r"For nonzero complex $a$, $b$, and $c$, $\sum_{n=0}^{\infty}\frac{(-aq)_n(-bq)_n q^{n+1}}{(-cq)_n}=\sum_{n=1}^{\infty}\frac{(-1/c)^n(ab/c)^{n-1}q^{n(n+1)/2}}{(aq/c)_n(bq/c)_n}-\frac{1}{(-aq)_{\infty}(-bq)_{\infty}c(-cq)_{\infty}}\sum_{n=1}^{\infty}\frac{(ab/c^2)^{n-1}q^{n^2}}{(aq/c)_n(bq/c)_n}$."),
    rec("RLN-P2-C06-Entry6-3-13", r"For $a \neq 0$, $(1+a)\sum_{n=0}^{\infty}\frac{(-1)^n(cq)^n a^{-n-1}b^n q^{n(n+1)/2}}{(-cq/a)_{n+1}(-bq)_n}=\sum_{n=0}^{\infty}\frac{(cq)_n q^n}{(-aq)_n(-bq)_n}+\frac{(cq)_{\infty}}{(-aq)_{\infty}(-bq)_{\infty}}\sum_{n=0}^{\infty}\frac{(-1)^n a^{-n-1}b^n q^{n(n+1)/2}}{(-cq/a)_{n+1}}$."),
    rec("RLN-P2-C06-Entry6-3-14", r"For $a \neq 0$, $\sum_{n=0}^{\infty}\frac{(-1)^n(q;q^2)_n q^{n^2}}{(-aq^2;q^2)_n(-q^2/a;q^2)_n}=(1+a)\sum_{n=0}^{\infty}\frac{(q;q^2)_n q^{2n+1}}{(-aq;q)_{2n+1}}+\frac{(q;q^2)_{\infty}}{(-aq;q)_{\infty}}\sum_{n=0}^{\infty}\frac{(-1)^n q^{n^2}}{(-q^2/a;q^2)_n}$."),
    rec("RLN-P2-C06-Entry6-3-15", r"$\sum_{n=0}^{\infty}\frac{(q;q)_{2n}q^{2n}}{(q^6;q^6)_n}=3\sum_{n=0}^{\infty}q^{18n^2+3n}(1-q^{12n+3}+q^{18n+6}-q^{30n+15})-\frac{1}{(q;q)_{\infty}(q^6;q^6)_{\infty}}\sum_{n=0}^{\infty}(-1)^n q^{3n^2+2n}(1+q^{2n+1})$."),
    rec("RLN-P2-C06-Entry6-3-16", r"$\sum_{n=0}^{\infty}\frac{(-q^2;q^4)_n q^{2n+1}}{(-q;q)_{2n+1}}=2q\sum_{n=0}^{\infty}\frac{(-1)^n(q;-q)_{2n}q^n}{(-q^2;q^4)_{n+1}}-q(-q^2;q^4)_{\infty}(-q;q)_{\infty}\sum_{n=0}^{\infty}\frac{(-q^4;q^4)_n q^{2n^2+2n}(1-q^{4n+3})}{(-q^2;q^4)_{n+1}}$."),
    rec("RLN-P2-C06-Entry6-4-1", r"If $\omega=e^{2\pi i/3}$, then $\psi(a,q)+\omega\psi(a,\omega q)+\omega^2\psi(a,\omega^2 q)=0$."),
    rec("RLN-P2-C06-Entry6-4-2", r"If $\omega=e^{2\pi i/3}$, then $\psi(a,q)+\omega^2\psi(a,\omega q)+\omega\psi(a,\omega^2 q)=3aq\psi(a^3,q^9)$."),
    rec("RLN-P2-C06-Entry6-4-3", r"For any complex number $a$, $\sum_{n=0}^{\infty}\frac{(-1)^n a^{2n}q^{n(3n+1)/2}}{(-aq;q^3)_{n+1}}=\frac{1}{2}\sum_{n=0}^{\infty}a^{3n}q^{3n(3n+1)/2}(1-a^2 q^{6n+3})+\frac{1}{2}\psi(a,q)-3aq\psi(a^3,q^9)$."),
    rec("RLN-P2-C06-Entry6-4-4", r"For any complex number $a$, $\sum_{n=0}^{\infty}\frac{(-1)^n a^{2n+1}q^{(n+1)(3n+1)/2}}{(-aq^2;q^3)_{n+1}}=\frac{1}{2}\sum_{n=0}^{\infty}a^{3n}q^{3n(3n+1)/2}(1-a^2 q^{6n+3})-\frac{1}{2}\psi(a,q)-3aq\psi(a^3,q^9)$."),
    rec("RLN-P2-C06-Entry6-4-5", r"For any complex number $a$, $\sum_{n=0}^{\infty}\frac{(-1)^n a^{2n}q^{n(3n+1)/2}}{(-aq;q^3)_{n+1}}+\sum_{n=0}^{\infty}\frac{(-1)^n a^{2n+1}q^{(n+1)(3n+2)/2}}{(-aq^2;q^3)_{n+1}}=\sum_{n=0}^{\infty}a^{3n}q^{3n(3n+1)/2}(1-a^2 q^{6n+3})$."),
    rec("RLN-P2-C06-Entry6-4-6", r"Formally, for $a \neq 0$, $\left(1+\frac{1}{a}\right)\sum_{n=0}^{\infty}\frac{(-1)^n(-aq;q)_n(-q/a;q)_n}{(q;q^2)_{n+1}}=\frac{1}{2}\sum_{n=0}^{\infty}(-1)^n(a^n+a^{-n-1})q^{n(n+1)/2}$."),
    rec("RLN-P2-C06-Entry6-5-1", r"$\sum_{n=0}^{\infty}\frac{q^n}{(-q;q)_{2n}}=\sum_{n=0}^{\infty}q^{12n^2+n}(1-q^{22n+11})+q\sum_{n=0}^{\infty}q^{12n^2+7n}(1-q^{10n+5})$, and $\sum_{n=0}^{\infty}\frac{q^n}{(-q;q)_{2n+1}}=\sum_{n=0}^{\infty}q^{12n^2+5n}(1-q^{14n+7})+q^2\sum_{n=0}^{\infty}q^{12n^2+11n}(1-q^{2n+1})$."),
    rec("RLN-P2-C06-Entry6-5-2", r"With $\varphi(q)$, $f(-q)$, and $f(a,b)$ as in (1.4.9), (1.4.11), and (1.4.8), $\sum_{n=0}^{\infty}\frac{q^n}{(q)_{2n}}=\frac{1}{\varphi(-q)}\left(\sum_{n=-\infty}^{\infty}q^{12n^2+n}-q\sum_{n=-\infty}^{\infty}q^{12n^2+7n}\right)=\frac{f(q^5,q^3)}{f(-q)}$, and $\sum_{n=0}^{\infty}\frac{q^n}{(q)_{2n+1}}=\frac{1}{\varphi(-q)}\left(\sum_{n=-\infty}^{\infty}q^{12n^2+5n}-q^2\sum_{n=-\infty}^{\infty}q^{12n^2+11n}\right)=\frac{f(q^7,q)}{f(-q)}$."),
    rec("RLN-P2-C06-Entry6-5-3", r"For any complex number $a$, $\sum_{n=0}^{\infty}\frac{q^n}{(-q;q)_n(aq;q^2)_n}=2\sum_{n=0}^{\infty}a^n q^{2n^2}(aq;q^2)_n-\frac{1}{(q;q^2)_{\infty}(aq;q^2)_{\infty}}\sum_{n=0}^{\infty}(-1)^n(q;q^2)_n a^n q^{n^2}$."),
    rec("RLN-P2-C06-Entry6-6-1", r"For $a \neq 0$, $\sum_{n=0}^{\infty}\frac{(q^{n+1})_n q^n}{(-aq)_n(-q/a)_n}=(1+a)\sum_{n=0}^{\infty}(-1)^n a^n q^{n(n+1)}-\frac{a}{(-aq)_{\infty}(-q/a)_{\infty}}\sum_{n=0}^{\infty}(-1)^n a^{3n}q^{3n^2+2n}(1+aq^{2n+1})$."),
]
