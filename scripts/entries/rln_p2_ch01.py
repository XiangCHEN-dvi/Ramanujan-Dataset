"""RLN Part 2, Chapter 1 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C01 = ["heine-transformation"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C01}


CHAPTER_1 = [
    rec(
        "RLN-P2-C01-Entry1-3-1",
        r"If $|abc|<1$ and $bc\neq0$, then $\dfrac{(ac)_\infty}{(abc)_\infty}=\dfrac{(a)_\infty}{(ab)_\infty}\sum_{n=0}^{\infty}\dfrac{(1/b)_n(1/c)_n(a)_n(q)_n}{(abc)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-3-2",
        r"For any complex numbers $a$ and $b$, $\dfrac{(-aq)_\infty}{(bq)_\infty}=\sum_{n=0}^{\infty}\dfrac{(-b/a)_na^nq^{n(n+1)/2}}{(q)_n(bq)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-1",
        r"For $0<|aq|,|k|<1$, $\dfrac{(aq;q)_\infty(cq;q^2)_\infty}{(-bq;q)_\infty(kq^2;q^2)_\infty}\sum_{n=0}^{\infty}\frac{(kq^2;q^2)_n(-bq/a;q)_n}{(cq;q^2)_{n+1}(q;q)_n}a^nq^n=\sum_{n=0}^{\infty}\frac{(cq/k;q^2)_n(aq;q)_{2n}}{(q^2;q^2)_n(-bq;q)_{2n+1}}k^nq^{2n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-2",
        r"For $|bq|<1$, $(q;q^2)_\infty(aq;q^2)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{(-q;q)_n(-bq;q)_n}{(aq;q^2)_{n+1}}q^n=(-bq;q)_\infty\sum_{n=0}^{\infty}\frac{(q;q^2)_n(aq;q^2)_n}{(-bq;q)_{2n+1}}q^{2n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-3",
        r"For $|aq|,|b|<1$, $\displaystyle\sum_{n=0}^{\infty}\frac{a^nq^n}{(q;q)_n(bq;q^2)_n}=\dfrac{1}{(aq;q)_\infty(bq;q^2)_\infty}\sum_{n=0}^{\infty}\frac{(-1)^n(aq;q)_{2n}b^nq^{n^2}}{(q^2;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-4",
        r"For $|a|,|b|<1$, $\displaystyle\sum_{n=0}^{\infty}\frac{a^nq^{2n}}{(q^2;q^2)_n(bq;q)_{2n}}=\dfrac{1}{(aq^2;q^2)_\infty(bq;q)_\infty}\sum_{n=0}^{\infty}\frac{(-1)^n(aq^2;q^2)_nb^nq^{n(n+1)/2}}{(q;q)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-5",
        r"For any complex $a$, $\displaystyle\sum_{n=0}^{\infty}(-aq;q)_n(-q;q)_nq^n=(-q;q)_\infty(-aq;q)_\infty\sum_{n=0}^{\infty}\frac{(q;q^2)_nq^{2n}}{(-aq;q)_{2n+1}}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-6",
        r"For any complex $a$, $\dfrac{(-aq;q)_\infty}{(-q;q)_\infty}\sum_{n=0}^{\infty}\frac{(aq;q)_nq^{n^2}}{(q^2;q^2)_n}=\sum_{n=0}^{\infty}\frac{(-1)^n(a^2q^2;q^2)_{2n}q^{2n^2}}{(q^4;q^4)_n}-a\sum_{n=1}^{\infty}\frac{(a^2q^2;q^2)_{n-1}(-q)^{n(n+1)/2}}{(-q;-q)_{n-1}}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-7",
        r"For any complex $a$, $\dfrac{(-aq;q)_\infty}{(-q;q)_\infty}\sum_{n=0}^{\infty}\frac{(aq;q)_nq^{n(n+1)}}{(q^2;q^2)_n}=\sum_{n=0}^{\infty}\frac{(a^2q^2;q^2)_n(-q)^{n(n+1)/2}}{(-q;-q)_n}+a\sum_{n=0}^{\infty}\frac{(-1)^n(a^2q^2;q^2)_{2n}q^{2n^2+4n+1}}{(q^4;q^4)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-8",
        r"For arbitrary complex numbers $a$ and $b$, $\dfrac{1}{(aq;q)_\infty}\sum_{n=0}^{\infty}\frac{(aq;q)_nb^nq^{n^2}}{(q^2;q^2)_n}=(-bq;q^2)_\infty\sum_{n=0}^{\infty}\frac{(aq)_{2n}}{(q;q)_{2n}(-bq;q^2)_n}+(-bq^2;q^2)_\infty\sum_{n=0}^{\infty}\frac{(aq)_{2n+1}}{(q;q)_{2n+1}(-bq^2;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-9",
        r"With $\varphi(-q)$ as in (1.4.9), $\varphi(-q)\displaystyle\sum_{n=0}^{\infty}\frac{q^{n(n+1)/2}}{(q;q)_{2n}}=\sum_{n=0}^{\infty}\frac{(-1)^nq^{n(n+1)/2}}{(q^2;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-10",
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{q^n}{(q)_{2n}}=\dfrac{1}{(q)_\infty^2}\sum_{n=0}^{\infty}(-1)^nq^{n(n+1)/2}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-11",
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{q^{2n}}{(q)_{2n}}=\dfrac{1}{(q)_\infty^2}\left(1+2\sum_{n=1}^{\infty}(-1)^nq^{n(n+1)/2}\right)$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-12",
        r"For $|a|,|b|<1$ and any positive integer $n$, $\dfrac{(-bq^n;q^n)_\infty}{(-aq;q)_\infty}\sum_{m=0}^{\infty}\frac{a^mq^{m(m+1)/2}}{(q;q)_m(-bq^n;q^n)_m}=\sum_{m=0}^{\infty}\frac{b^mq^{nm(m+1)/2}}{(q^n;q^n)_m(-aq;q)_{nm}}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-13",
        r"For $|a|<1$, $\displaystyle\sum_{n=0}^{\infty}\frac{(aq)_n}{(q^2;q^2)_n(bq)_n}=\dfrac{1}{(aq;q^2)_\infty(bq;q)_\infty}\sum_{n=0}^{\infty}\frac{(aq;q^2)_nb^{2n}q^{2n^2+n}}{(q;q)_{2n}}-\dfrac{1}{(aq^2;q^2)_\infty(bq;q)_\infty}\sum_{n=0}^{\infty}\frac{(aq^2;q^2)_nb^{2n+1}q^{2n^2+3n+1}}{(q;q)_{2n+1}}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-14",
        r"For any complex $a$, $(q^2;q^4)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{(aq^2;q^2)_nq^{n(n+1)/2}}{(q;q)_n}=(aq^4;q^4)_\infty\sum_{n=0}^{\infty}\frac{(aq^2;q^4)_nq^{4n^2}}{(q^2;q^2)_{2n}}+(aq^2;q^4)_\infty\sum_{n=0}^{\infty}\frac{(aq^4;q^4)_nq^{4n^2+4n+1}}{(q^2;q^2)_{2n+1}}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-15",
        r"For any complex $a$, $(q^2;q^4)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{(aq^2;q^2)_nq^{(n+1)(n+2)/2}}{(q;q)_n}=(aq^4;q^4)_\infty\sum_{n=0}^{\infty}\frac{(aq^2;q^4)_nq^{4n^2+4n+1}}{(q^2;q^2)_{2n}}+(aq^2;q^4)_\infty\sum_{n=0}^{\infty}\frac{(aq^4;q^4)_nq^{4n^2+8n+4}}{(q^2;q^2)_{2n+1}}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-16",
        r"For any complex $a$, $(q;q^2)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n(aq;q)_{2n}q^{n(n+1)}}{(q^2;q^2)_n}=(aq^2;q^2)_\infty\sum_{n=0}^{\infty}\frac{(aq;q^2)_nq^{2n^2+n}}{(q;q)_{2n}}-(aq;q^2)_\infty\sum_{n=0}^{\infty}\frac{(aq^2;q^2)_nq^{2n^2+3n+1}}{(q;q)_{2n+1}}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-17",
        r"For each positive integer $n$, the series $(-aq)_\infty\displaystyle\sum_{m=0}^{\infty}\frac{b^mq^{m(m+1)/2}}{(q)_m(-aq)_{nm}}$ is symmetric in $a$ and $b$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-4-18",
        r"For complex numbers $a$ and $b$ with $b\neq0$, $\displaystyle\sum_{n=0}^{\infty}\frac{(-a/b;q^2)_nb^nq^{n(n+1)/2}}{(q;q)_n(aq^2;q^2)_n}=\dfrac{(-bq;q)_\infty}{(aq;q)_\infty}\left(\dfrac{(-a/b;q^2)_\infty(aq;q)_\infty}{(aq^2;q^2)_\infty}\sum_{n=0}^{\infty}\frac{(-bq^2;q^2)_n}{(q^2;q^2)_n(-bq;q)_{2n}}\left(-\dfrac{a}{b}\right)^n\right)$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-5-1",
        r"For any complex $a$, $\displaystyle\sum_{n=0}^{\infty}\frac{a^nq^{n^2}}{(q;q)_n}=(-aq^2;q^2)_\infty\sum_{n=0}^{\infty}\frac{a^nq^{n^2}}{(q^2;q^2)_n(-aq^2;q^2)_n}=(-aq;q^2)_\infty\sum_{n=0}^{\infty}\frac{a^nq^{n^2+n}}{(q^2;q^2)_n(-aq;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-5-2",
        r"For any complex $a$, $\displaystyle\sum_{n=0}^{\infty}\frac{a^{2n}q^{4n^2}}{(q^4;q^4)_n}=(aq;q^2)_\infty\sum_{n=0}^{\infty}\frac{a^nq^{n^2}}{(q^2;q^2)_n(aq;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-5-3",
        r"$(q;q^2)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{q^{2n^2+n}}{(q^2;q^2)_n}=\sum_{n=0}^{\infty}\frac{(-1)^nq^{n(n+1)/2}}{(q^2;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-5-4",
        r"$(q;q^2)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{q^{2n^2-n}}{(q^2;q^2)_n}=\sum_{n=0}^{\infty}\frac{(-1)^nq^{n(n+3)/2}}{(q^2;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-6-1",
        r"For complex numbers $a$ and $b$, $(aq)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{b^nq^{n^2}}{(q)_n(aq)_n}=\sum_{n=0}^{\infty}\frac{(-1)^n(b/a)_na^nq^{n(n+1)/2}}{(q)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-6-2",
        r"For any complex $a$, $\displaystyle\sum_{n=0}^{\infty}a^nq^{n^2}=1+\sum_{n=1}^{\infty}\frac{(-q;q)_{n-1}a^nq^{n(n+1)/2}}{(-aq^2;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-6-3",
        r"For any complex $a$, $\displaystyle\sum_{n=0}^{\infty}(-1)^na^nq^{n(n+1)/2}=\sum_{n=0}^{\infty}\frac{(-1)^n(q;q^2)_na^{2n}q^{n(n+1)}}{(-aq;q)_{2n+1}}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-6-4",
        r"For $|aq|<1$, $\displaystyle\sum_{n=0}^{\infty}\frac{(-aq)_n}{(-aq^2;q^2)_n}=\sum_{n=0}^{\infty}\frac{(-1)^na^nq^{n(n+1)/2}}{(-aq;q)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-6-5",
        r"For any complex $a$, $\displaystyle\sum_{m=0}^{\infty}\frac{a^mq^{m(m+1)}}{(q^2;q^2)_m(1+aq^{2m+1})}=(-aq^2;q^2)_\infty\sum_{n=0}^{\infty}\frac{(-a)_nq^{n(n+1)/2}}{(-aq;q)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-6-6",
        r"With $\psi(q)$ as in (1.4.10), $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^nq^{n^2+n}}{(q^2;q^2)_n(1-q^{2n+1})}=\psi(q)$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-6-7",
        r"For $|a|<1$, $(a)_\infty\displaystyle\sum_{n=0}^{\infty}\frac{a^n}{(q)_n(bq)_n}=\sum_{n=0}^{\infty}\frac{a^nb^nq^{n^2}}{(q)_n(bq)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-1",
        r"For any complex $a$, $\displaystyle\sum_{n=0}^{\infty}\frac{(-a;q)_{2n+1}q^{2n+1}}{(q;q^2)_{n+1}}+\sum_{n=0}^{\infty}(-a)_nq^{n(n+1)/2}=\dfrac{(-aq;q)_\infty}{(q;q^2)_\infty}\sum_{n=0}^{\infty}\frac{(-a)_nq^{n(n+1)/2}}{(-aq;q)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-2",
        r"For $|b|<1$ and arbitrary $a$, $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n(-q;q)_n(-aq/b;q)_nb^n}{(aq;q^2)_{n+1}}=\sum_{n=0}^{\infty}\frac{(-1)^n(-aq/b;q)_nb^nq^{n(n+1)/2}}{(-b;q)_{n+1}}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-3",
        r"For complex numbers $a$ and $c$, $\displaystyle\sum_{n=0}^{\infty}\frac{(c/a;q)_na^nq^{n(n+1)/2}}{(q;q)_n(aq;q)_n}=\dfrac{(cq;q^2)_\infty}{(aq;q)_\infty}\sum_{n=0}^{\infty}\frac{(-1)^n(a^2q/c;q^2)_nc^nq^{n^2+n}}{(q^2;q^2)_n(cq;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-4",
        r"With $\varphi(-q)$ as in (1.4.9), $\displaystyle\sum_{n=0}^{\infty}\frac{(-1;q^2)_nq^{n(n+1)/2}}{(q;q)_n(q;q^2)_n}=\dfrac{\varphi(-q^4)}{\varphi(-q)}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-5",
        r"With $\varphi(-q)$ and $\psi(q)$ as in (1.4.9) and (1.4.10), $\displaystyle\sum_{n=0}^{\infty}\frac{(-q^2;q^2)_nq^{n(n+1)/2}}{(q;q)_n(q;q^2)_{n+1}}=\dfrac{\psi(-q^2)}{\varphi(-q)}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-6",
        r"With $f(a,b)$ as in (1.4.8), $\displaystyle\sum_{n=0}^{\infty}\frac{(-q;q^2)_nq^{(n+1)(n+2)/2}}{(q;q)_n(q;q^2)_{n+1}}=\dfrac{qf(-q,-q^7)}{\varphi(-q)}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-7",
        r"With $f(a,b)$ as in (1.4.8), $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^nq^{(n+1)(n+2)/2}}{(q)_n(1-q^{2n+1})}=qf(q,q^7)$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-8",
        r"With $f(a,b)$ as in (1.4.8), $\displaystyle\sum_{n=0}^{\infty}\frac{(-q;q^2)_nq^{n(n+1)/2}}{(q;q)_n(q;q^2)_{n+1}}=\dfrac{f(-q^3,-q^5)}{\varphi(-q)}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-9",
        r"With $f(a,b)$ as in (1.4.8), $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^nq^{n(n+1)/2}}{(q)_n(1-q^{2n+1})}=f(q^3,q^5)$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-10",
        r"With $\psi(q)$ as in (1.4.10), $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n(q;q^2)_nq^{n^2}}{(q^2;q^2)_{2n}}=\dfrac{1}{\psi(q)}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-11",
        r"With $f(a,b)$ as in (1.4.8) and $\psi(q)$ as in (1.4.10), $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n(q;q^2)_nq^{n^2}}{(q^2;q^2)_n}=\dfrac{\psi(q^4)}{f(q,q^7)}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-12",
        r"With $\psi(q)$ and $f(a,b)$ as in (1.4.10) and (1.4.8), $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n(q;q^2)_nq^{n^2+2n}}{(q^2;q^2)_n}=\dfrac{\psi(q^4)}{f(q^3,q^5)}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-13",
        r"With $\varphi(-q)$ as in (1.4.9), $\displaystyle\sum_{n=0}^{\infty}\frac{(-q^2;q^2)_nq^{n^2}}{(q;q)_{2n+1}}=\dfrac{\varphi(-q^2)}{\varphi(-q)}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-14",
        r"With $\varphi(q)$ as in (1.4.9), $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^nq^{n(n+1)/2}}{(q)_n}=\dfrac{\varphi(-q^2)}{\varphi(-q)}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-15",
        r"If $\varphi(a,q):=\sum_{n=0}^{\infty}\dfrac{a^nq^{n^2}}{(q;q)_n}$, then $\varphi(a,q)\varphi(b,1/q)=\sum_{n=0}^{\infty}\dfrac{(b/(aq^n);1/q)_na^nq^{n^2}}{(q;q)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-16",
        r"For $|xy|<1$, if $\varphi(a,x,y):=\sum_{n=0}^{\infty}\dfrac{a^nx^{n(n+1)/2}}{(xy;xy)_n}$, then $\varphi(a,x,y)\varphi(b,y,x)=\sum_{n=0}^{\infty}\dfrac{(ax+b y^n)(ax^2+b y^{n-1})\cdots(ax^n+by)}{(xy;xy)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-17",
        r"If $\varphi(a):=\sum_{n=0}^{\infty}\dfrac{a^nq^{n(n+1)/2}}{(q^2;q^2)_n}$, then $\varphi(a)\varphi(b)=\sum_{n=0}^{\infty}\dfrac{(a+bq^{n-1})(a+bq^{n-3})\cdots(a+bq^{1-n})q^{n(n+1)/2}}{(q^2;q^2)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-18",
        r"The expression $\dfrac{1}{1-\alpha}+\sum_{n=1}^{\infty}\dfrac{\beta^n}{(1-\alpha x^n)(1-\alpha x^{n-1}y)\cdots(1-\alpha y^n)}$ is symmetric in $\alpha$ and $\beta$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-19",
        r"Define $c_n$ for $n\geq0$ by $\sum_{n=0}^{\infty}c_n\lambda^n:=\dfrac{(-a\lambda)_\infty}{(b\lambda)_\infty(c\lambda)_\infty}$. Then $\displaystyle\sum_{n=0}^{\infty}c_nq^{n(n+1)/2}=(-cq)_\infty\sum_{n=0}^{\infty}\frac{(-a/b)_nb^nq^{n(n+1)/2}}{(q)_n(-cq)_n}$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-20",
        r"For nonnegative integers $m$ and $n$, let $\varphi(a):=\sum_{j=0}^{\infty}\dfrac{a^jq^{mj^2+nj}}{(q)_j}$ and $\psi(a):=\varphi(aq)/\varphi(a)$. Then $\varphi(a)=\varphi(aq)+aq^{m+n}\varphi(aq^{2m})$ and $1=\psi(a)+aq^{m+n}\psi(a)\psi(aq)\psi(aq^2)\cdots\psi(aq^{2m-1})$.",
    ),
    rec(
        "RLN-P2-C01-Entry1-7-21",
        r"For $|xy|<1$ and arbitrary $a$ and $b$, $\displaystyle\sum_{n=0}^{\infty}\frac{(ab)^n(xy)^{n(n+1)/2}y^{-n}}{(ax;x)_n(by;y)_n}=1-b+b\sum_{n=0}^{\infty}\frac{(ab)^n(xy)^{n(n+1)/2}}{(ax;x)_{n+1}(by;y)_n}$.",
    ),
]
