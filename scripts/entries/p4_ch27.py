"""Part IV, Chapter 27 entries — q-series (curated LaTeX)."""

from __future__ import annotations

TOPICS_C27 = ["q-series"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C27}


CHAPTER_27 = [
    rec(
        "RN-P4-C27-Entry01",
        r"Let $|q|<1$. Suppose that $a\ne 0$ and $1-bq^n\ne 0$ for $n\ge 1$. Then "
        r"$\displaystyle(-aq;q)_\infty=\frac{(-b/a;q)_\infty}{(-bq;q)_\infty}"
        r"\sum_{n=0}^\infty\frac{(-b/a)_n a^n q^{n(n+1)/2}}{(q)_n}$.",
    ),
    rec(
        "RN-P4-C27-Entry02",
        r"Let $|q|<1$, and suppose that $(aq)_n\ne 0$ for $n\ge 1$. Then "
        r"$\displaystyle\sum_{n=0}^\infty\frac{(-1)^n q^{n(n-1)/2}}{(aq)_n(1-q^n)}"
        r"$=\frac{1}{(aq;q)_\infty}\sum_{n=0}^\infty\frac{(-1)^n a^n q^{n^2}}{(q)_n}$.",
    ),
    rec(
        "RN-P4-C27-Entry03",
        r"Let $|q|<1$, $a\ne 0$, and $(b)_n\ne 0$ for $n\ge 1$. Then "
        r"$\displaystyle\sum_{n=0}^\infty\frac{(-1)^n(b/a)_n a^n q^{n(n+1)/2}}{(q)_n(b)_n}"
        r"$=\frac{1}{(b/a;q)_\infty}\left\{\frac{a}{1-a}-\frac{b}{1-b}+\sum_{n=0}^\infty\frac{(-1)^n(b/a)_n a^n q^{n(n+1)/2}}{(q)_n(bq)_n}\right\}$.",
    ),
    rec(
        "RN-P4-C27-Entry04",
        r"For $|q|<1$ and $(aq)_n\ne 0$, $n\ge 1$, "
        r"$\displaystyle\sum_{n=1}^\infty\frac{(-1)^{n-1}q^{n(n-1)/2}}{(aq)_n(1-q^n)}"
        r"$=\frac{1}{(aq;q)_\infty}\sum_{n=0}^\infty\frac{q^{n^2}}{(q)_n}$.",
    ),
    rec(
        "RN-P4-C27-Entry05",
        r"For $|q|<1$ and $(a)_n\ne 0$, $n\ge 1$, "
        r"$\displaystyle\sum_{n=1}^\infty\frac{(-1)^{n-1}q^{n(n-1)/2}}{(a)_n(1-q^n)}"
        r"$=\frac{1}{(a;q)_\infty}\sum_{n=0}^\infty\frac{q^{n(n+1)/2}}{(q)_n}$.",
    ),
    rec(
        "RN-P4-C27-Entry06",
        r"Let $|a|,|q|<1$. Then as $q\to 1^-$, "
        r"$\displaystyle\log\sum_{n=0}^\infty\frac{(-1)^n q^{n(n+1)/2}}{(a)_n(1-q^n)}"
        r"$\sim\frac{1}{1-q}\left\{\frac{\pi^2}{6}+\frac{1}{2}\left(\frac{1+a}{1-a}\right)\log^2 q\right\}"
        r"$+\frac{B_2}{2!}\log q+\frac{B_4}{4!}\left(a-\frac{1}{a^2}+\frac{1}{a^3}-a^3\right)\log^3 q+\cdots$, "
        r"where $B_n$, $n>0$, and $\mathrm{Li}_2$ are defined by (0.2) and (0.3), respectively.",
    ),
    rec(
        "RN-P4-C27-Entry07",
        r"Let $a>0$, $|q|<1$, and $b$ and $c$ be integers with $b>0$. "
        r"Let $z$ denote the positive root of $az^{2b}+z=1$. Then as $q\to 1^-$, "
        r"$\displaystyle\log\sum_{n=0}^\infty\frac{q^{n(n+1)/2}}{(q)_n(a;q)_n}"
        r"$\sim\frac{1}{1-q}\left\{\mathrm{Li}_2(az^{2b})+b\log^2 z\right\}"
        r"$+c\log z-\tfrac12\log\{z+2\sqrt{z(1-z)}\}$.",
    ),
    rec(
        "RN-P4-C27-Entry08",
        r"Let $\mathrm{Li}_2$ denote the dilogarithm defined by (0.3). Suppose that $a>0$ and $|q|<1$. "
        r"Let $x$ denote the positive root of $x^2+x=a$. Then as $q\to 1^-$, "
        r"$\displaystyle\log\sum_{n=0}^\infty\frac{a^n q^{n^2}}{(q)_n(a;q)_n}"
        r"$\sim\frac{1}{1-q}\left\{\mathrm{Li}_2(-x)-\tfrac12\log^2(1+x)\right\}$ "
        r"(equivalently, when $a=1$, "
        r"$\displaystyle\log\sum_{n=0}^\infty\frac{q^{n^2}}{(q)_n}\sim\frac{\pi}{\sqrt{15(1-q)}}$).",
    ),
    rec(
        "RN-P4-C27-Entry09",
        r"As $q\to 1^-$, "
        r"$\displaystyle\log\sum_{n=0}^\infty\frac{q^{n(n+1)/2}}{(q)_n}"
        r"$\sim\frac{\pi}{\sqrt{15(1-q)}}$; "
        r"this is the asymptotic expansion for the logarithm of the second Rogers–Ramanujan identity "
        r"$\displaystyle\sum_{n=0}^\infty\frac{q^{n(n+1)/2}}{(q)_n}=\frac{1}{(q;q^5)_\infty(q^4;q^5)_\infty}$.",
    ),
]
