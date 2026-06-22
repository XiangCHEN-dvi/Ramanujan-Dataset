"""RLN Part 2, Chapter 3 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C03 = ["bilateral-series"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C03}


CHAPTER_3 = [
    rec(
        "RLN-P2-C03-Entry3-1-1",
        r"For $|\lambda q|,|q^2|,|\lambda q^3|<1$, $\dfrac{f(-\lambda q,-q^2)}{f(-q,-\lambda q^2)f(-\lambda q^3)}=f(-\lambda^2q^3,-\lambda q^6)+qf(-\lambda,-\lambda^2q^9)$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-3-1",
        r"For $|abq^2/c|<|bq|<1$, $\displaystyle\sum_{n=0}^{\infty}\frac{(cq/b;q^2)_nb^nq^n}{(aq;q^2)_{n+1}}-\sum_{n=0}^{\infty}\frac{(q/a;q^2)_na^nq^n}{c^{n+1}(bq/c;q^2)_{n+1}}=(1-c^{-1})\dfrac{(q^2/c,abq^2/c,q^2,cq^2;q^2)_\infty}{(aq/c,bq/c,aq,bq;q^2)_\infty}$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-3-2",
        r"If $k=ab$, $|k|<1$, and $n$ is any complex number, then $\dfrac{(-a/n;k)_\infty(-bn;k)_\infty(k;k)_\infty^2}{(a;k)_\infty(b;k)_\infty(-nk;k)_\infty(-k/n;k)_\infty}=1+(n+1)\displaystyle\sum_{j=1}^{\infty}\left(\dfrac{a^j}{n+k^j}+\dfrac{b^j}{1+nk^j}\right)$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-3-3",
        r"For $|x|<1$, let $F(x,y):=\sum_{k=-\infty}^{\infty}x^{k^2}y^k$. For $|ab|<1$, $\dfrac{F(\sqrt{ab},n\sqrt{b/a})(ab;ab)_\infty^3}{n\,F(\sqrt{ab},-n\sqrt{b/a})F(\sqrt{ab},n\sqrt{ab})}=\dfrac{1}{n+1}+\sum_{j=1}^{\infty}\left(\dfrac{a^j}{n+(ab)^j}+\dfrac{b^j}{1+n(ab)^j}\right)$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-3-4",
        r"$\dfrac{(q^3;q^3)_\infty^3}{(q;q)_\infty}=\displaystyle\sum_{n=0}^{\infty}\frac{q^n}{1-q^{3n+1}}-\sum_{n=0}^{\infty}\frac{q^{2n+1}}{1-q^{3n+2}}=\sum_{n=0}^{\infty}\frac{1+q^{3n+1}}{1-q^{3n+1}}q^{3n^2+2n}-\sum_{n=0}^{\infty}\frac{1+q^{3n+2}}{1-q^{3n+2}}q^{3n^2+4n+1}$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-3-5",
        r"For $|q/a|<|1/b|<1$ and $abc\neq0$, $\displaystyle\sum_{n=0}^{\infty}\frac{(-q/c;q)_n}{(-q/a;q)_n(-q/b;q)_n}\left(\dfrac{c}{ab}\right)^nq^{n(n-1)/2}+(1+a^{-1})(1+b^{-1})\sum_{n=1}^{\infty}\frac{(-q/c;q)_{n-1}(aq/c;q)_n(bq/c;q)_n}{(ab/c)_n}q^{n(n+1)/2}=\dfrac{(-q/c;q)_\infty}{(aq/c,bq/c,-q/a,-q/b;q)_\infty}\sum_{n=0}^{\infty}\left(\dfrac{a^nb^n}{c^n}+\dfrac{c^{n+1}}{a^{n+1}b^{n+1}}\right)q^{n(n+1)/2}$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-4-1",
        r"For any complex $a$, with $f(a,b)$ and $\psi(q)$ as in (1.4.8) and (1.4.10), $\displaystyle\sum_{n=0}^{\infty}\frac{(-aq;q^2)_n}{(aq;q)_{2n}}a^nq^{n^2}+\sum_{n=1}^{\infty}\frac{(1/a;q)_{2n}}{(-q/a;q^2)_n}q^n=\dfrac{\psi(q)\bigl(f(a^3q^2,a^{-3}q^4)+af(a^3q^4,a^{-3}q^2)\bigr)}{(aq;q)_\infty(-q/a;q^2)_\infty f(a,q^2/a)}$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-4-2",
        r"For any complex $a$, with $f(a,b)$ and $\psi(q)$ as in (1.4.8) and (1.4.10), $\displaystyle\sum_{n=0}^{\infty}\frac{(-aq;q^2)_n}{(aq;q)_{2n+1}}a^{n+1}q^{(n+1)^2}-\sum_{n=1}^{\infty}\frac{(1/a;q)_{2n-1}}{(-q/a;q^2)_n}q^n=\dfrac{q\psi(q)f(q^6/a^3,a^3)}{a(aq;q)_\infty(-q/a;q^2)_\infty f(q^2/a,a)}$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-4-3",
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n(q;q^2)_n}{(-q;q)_{2n}}q^{n^2}+2\sum_{n=1}^{\infty}\frac{(-q;q)_{2n-1}}{(q;q^2)_n}q^n=\dfrac{(-q;q^2)_\infty}{\varphi(-q^2)}\left(1+6\sum_{n=0}^{\infty}\frac{q^{6n+2}}{1-q^{6n+2}}-6\sum_{n=0}^{\infty}\frac{q^{6n+4}}{1-q^{6n+4}}\right)$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-4-4",
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{(-q;q^2)_n}{(q;q)_{2n+1}}q^{(n+1)^2}=\dfrac{q\psi(q^6)}{\psi(-q)}$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-4-5",
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{(-q;q^2)_n}{(q;q)_{2n+1}}q^n=\dfrac{\psi(-q^3)}{\varphi(-q)}$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-4-6",
        r"$\displaystyle\sum_{n=1}^{\infty}\frac{q^{2n^2-n}}{(q;q^2)_n}+\sum_{n=0}^{\infty}(-1)^n(q;q^2)_nq^{n^2+n}=\dfrac{(q^2;q^2)_\infty^2}{(q;q)_\infty^2}\sum_{n=0}^{\infty}\frac{q^{n(n+1)/2}}{(q;q)_{2n}}$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-4-7",
        r"For $a,b\neq0$, $\displaystyle\sum_{n=0}^{\infty}\frac{a^{-n-1}b^{-n}}{(-1/a;q)_{n+1}(-q/b;q)_n}q^{n^2}+\sum_{n=1}^{\infty}(-aq;q)_{n-1}(-b;q)_nq^n=\dfrac{(-aq;q)_\infty}{(q;q)_\infty(-q/b;q)_\infty}\left(\sum_{n=0}^{\infty}\frac{b^nq^{n(n+1)/2}}{1+aq^n}+\dfrac{1}{a}\sum_{n=1}^{\infty}\frac{b^{-n}q^{n(n+1)/2}}{1+q^n/a}\right)$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-4-8",
        r"For $a\neq0$, $\displaystyle\sum_{n=1}^{\infty}(-1;q)_n(-aq;q)_{n-1}q^n+\dfrac{1}{1+a}\sum_{n=0}^{\infty}\frac{a^{-n}q^{n^2}}{(-q;q)_n(-q/a;q)_n}=\dfrac{(-aq;q)_\infty}{(q^2;q^2)_\infty}\left(\sum_{n=0}^{\infty}\frac{q^{n(n+1)/2}}{1+aq^n}+\dfrac{1}{a}\sum_{n=1}^{\infty}\frac{q^{n(n+1)/2}}{1+q^n/a}\right)$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-5-1",
        r"$\dfrac{(q^2;q^2)_\infty}{(q;q)_\infty}\displaystyle\sum_{n=0}^{\infty}\frac{q^{n^2}}{(q;q)_n}=\sum_{n=-\infty}^{\infty}(-1)^nq^{15n^2+2n}(1+q^{6n+1})$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-5-2",
        r"$\dfrac{(q^2;q^2)_\infty}{(q;q)_\infty}\displaystyle\sum_{n=0}^{\infty}\frac{q^{n^2+n}}{(q;q)_n}=\sum_{n=-\infty}^{\infty}(-1)^nq^{15n^2+4n}(1+q^{10n+3})$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-5-3",
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^nq^{(5n^2+7n+2)/2}}{(-q^3;q^5)_{n+1}}=\dfrac{1}{2}\sum_{n=0}^{\infty}q^{n(15n+7)/2}(1-q^{8n+4})+\dfrac{1}{2}\sum_{n=0}^{\infty}q^{(15n^2+13n+2)/2}(1-q^{2n+1})-\dfrac{f(-q^2,-q^8)}{2(-q;q)_\infty}$ and $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^nq^{(5n^2+3n)/2}}{(-q^2;q^5)_{n+1}}=\dfrac{1}{2}\sum_{n=0}^{\infty}q^{n(15n+7)/2}(1-q^{8n+4})+\dfrac{1}{2}\sum_{n=0}^{\infty}q^{(15n^2+13n+2)/2}(1-q^{2n+1})+\dfrac{f(-q^2,-q^8)}{2(-q;q)_\infty}$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-5-4",
        r"With $f(a,b)$ as in (1.4.8), $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^nq^{n^2}}{(q^4;q^4)_n(-q;q^2)_n}=\dfrac{f(q^{10},q^{11})-qf(q^4,q^{17})}{(q^2;q^2)_\infty}=\dfrac{(q^7;q^7)_\infty f(-q^2,-q^5)}{(q^2;q^2)_\infty f(q,q^6)}$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-5-5",
        r"With $f(a,b)$ as in (1.4.8), $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^nq^{n^2+2n}}{(q^4;q^4)_n(-q;q^2)_n}=\dfrac{f(q^8,q^{13})-q^2f(q,q^{20})}{(q^2;q^2)_\infty}=\dfrac{(q^7;q^7)_\infty f(-q^3,-q^4)}{(q^2;q^2)_\infty f(q^2,q^5)}$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-5-6",
        r"With $f(a,b)$ as in (1.4.8), $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^nq^{n^2+2n}}{(q^4;q^4)_n(-q;q^2)_{n+1}}=\dfrac{f(q^5,q^{16})-qf(q^2,q^{19})}{(q^2;q^2)_\infty}=\dfrac{(q^7;q^7)_\infty f(-q,-q^6)}{(q^2;q^2)_\infty f(q^3,q^4)}$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-6-1",
        r"$\dfrac{(-q;-q)_\infty}{(q^2;q^2)_\infty}\displaystyle\sum_{n=0}^{\infty}\frac{q^{n(n+1)/2}}{(q^2;q^2)_n}=\sum_{n=0}^{\infty}\frac{q^{2n^2+n}}{(-q^2;q^2)_n}+\sum_{n=1}^{\infty}(-1;q^2)_nq^{n^2}$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-6-2",
        r"$\dfrac{(q^4;q^4)_\infty}{(q^2;q^2)_\infty}\displaystyle\sum_{n=0}^{\infty}\frac{q^{n(n+1)/2}}{(q^2;q^2)_n}=\sum_{n=0}^{\infty}(-q;q^2)_nq^{n^2+n}+\sum_{n=1}^{\infty}\frac{q^{2n^2-n}}{(-q;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-6-3",
        r"For $a\neq0$, $\displaystyle\sum_{n=-\infty}^{\infty}a^nq^{n^2/4}\sum_{m=0}^{\infty}\frac{(-1)^ma^mb^mq^{m^2/4}}{(q)_m}=(bq)_\infty\left(a^{-1}q^{1/4}\sum_{n=0}^{\infty}\frac{a^{-2n}q^{n^2+n}}{(bq)_n}+a^{-1}q^{1/4}\sum_{n=1}^{\infty}(-1)^na^{2n}b^nq^{n(n-1)/2}(1/b)_n\right)+(bq^{1/2})_\infty\left(\sum_{n=1}^{\infty}\frac{a^{-2n}q^{n^2}}{(bq^{1/2})_n}+\sum_{n=0}^{\infty}(-1)^na^{2n}b^nq^{n^2/2}(q^{1/2}/b)_n\right)$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-6-4",
        r"With $\varphi(q)$ and $\psi(q)$ as in (1.4.9) and (1.4.10), $\varphi(q)\left(2\sum_{n=-\infty}^{\infty}\dfrac{q^{n^2+n}}{1+q^{2n}}\right)-8\psi(q^2)\left(\sum_{n=1}^{\infty}\dfrac{q^{n^2}}{1+q^{2n-1}}\right)=\varphi^3(-q)$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-6-5",
        r"For any positive integer $k$, $\displaystyle\sum_{j=0}^{2k-1}(-1)^j\left(\sum_{m=-\infty}^{\infty}q^{km^2+jm}\right)\sum_{n=-\infty}^{\infty}\frac{q^{(2kn+j+1)(2kn+j)/2-kn^2-jn}}{1+q^{2kn+j}}=\varphi^2(-q)\varphi(-q^k)$.",
    ),
    rec(
        "RLN-P2-C03-Entry3-6-6",
        r"With $\varphi(q)$ and $\psi(q)$ as in (1.4.9) and (1.4.10), $\displaystyle\sum_{n=0}^{\infty}\frac{(-q;q^2)_nq^{n^2}}{(-q^4;q^4)_n}=\dfrac{1}{2}\sum_{n=0}^{\infty}\frac{(-1)^n(q;q^2)_nq^{n^2}}{(-q^2;q^2)_{2n}}+\dfrac{1}{2}\dfrac{\varphi^2(q)}{\psi(q)}$.",
    ),
]
