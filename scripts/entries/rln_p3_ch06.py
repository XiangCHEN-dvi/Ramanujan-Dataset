"""RLN Part 3, Chapter 6 — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C06 = ["partition-function-pages-189-182"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C06}


CHAPTER_6 = [
    rec(
        "RLN-P3-C06-Entry6-2-1",
        r"If $p(n)$ denotes the ordinary partition function, then "
        r"$\displaystyle\sum_{n=0}^{\infty} p(5n+4)q^n "
        r"= 5\frac{(q^5;q^5)_{\infty}^5}{(q;q)_{\infty}^6}$.",
    ),
    rec(
        "RLN-P3-C06-Entry6-2-2",
        r"If $q_5(n)$, $n\ge 0$, is defined by (6.1.3), then "
        r"$\displaystyle\sum_{n=0}^{\infty} q_5(5n)q^n "
        r"= \frac{(q;q)_{\infty}^6}{(q^5;q^5)_{\infty}}$.",
    ),
    rec(
        "RLN-P3-C06-Entry6-3-1",
        r"$\displaystyle\sum_{n=0}^{\infty} p(7n+5)q^n "
        r"= 7\frac{(q^7;q^7)_{\infty}^3}{(q;q)_{\infty}^4} "
        r"+ 49q\frac{(q^7;q^7)_{\infty}^7}{(q;q)_{\infty}^8}$.",
    ),
    rec(
        "RLN-P3-C06-Entry6-3-2",
        r"If $q_7(n)$, $n\ge 0$, is defined by (6.1.3), then "
        r"$\displaystyle\sum_{n=0}^{\infty} q_7(7n)q^n "
        r"= \frac{(q;q)_{\infty}^8}{(q^7;q^7)_{\infty}} "
        r"+ 49q\frac{(q;q)_{\infty}^4}{(q^7;q^7)_{\infty}^3}$.",
    ),
    rec(
        "RLN-P3-C06-Entry6-4-1",
        r"Let $n$ be the least positive integer such that $24n-1$ is divisible by a "
        r"positive integer $k$. Then $p(n+vk)-p(n)q(v)$ is divisible by $k$ for all "
        r"positive integral values of $v$, where "
        r"$(x;x)_{\infty}^{(24n-1)/k}=\displaystyle\sum_{\lambda=0}^{\infty} "
        r"q(\lambda)x^{\lambda}$. Here $q(v)$ depends on $n$ and $k$.",
    ),
    rec(
        "RLN-P3-C06-Entry6-4-2",
        r"For each positive integer $s$, define the coefficients $u_n=u_n(s)$ by "
        r"$\displaystyle\frac{1}{(q;q)_{\infty}^{24s}} "
        r"= \sum_{n=0}^{\infty} u_n q^n = \sum_{n=0}^{\infty} u_n(s)q^n$. "
        r"Let $B_j$, $0\le j<\infty$, denote the $j$th Bernoulli number, and let "
        r"$\sigma_k(n)=\sum_{d|n} d^k$. If $s$ is any positive integer, then "
        r"$\dfrac{B_{12s+2}}{24s}+4u_s(s) "
        r"= \displaystyle\sum_{k=0}^{s-1}\sigma_{12s+1}(k+1)u_k(s)$.",
    ),
    rec(
        "RLN-P3-C06-Entry6-4-3",
        r"For any positive integer $s$, "
        r"$\dfrac{B_{12s+2}}{24s}+4u_s(s) "
        r"= \displaystyle\sum_{k=0}^{s-1}\sigma_{12s+1}(s-k)u_k(s)$, "
        r"where $u_n(s)$ is defined in (6.4.2). Equivalently, if "
        r"$[q^n]\sum_{k=0}^{\infty}a_k q^k$ denotes $a_n$ and "
        r"$\Delta(\tau)=q(q;q)_{\infty}^{24}$, where $q=e^{2\pi i\tau}$, then "
        r"$[q^s]E_{12s+2}(\tau)/(q;q)_{\infty}^{24s} "
        r"= [q^0]E_{12s+2}(\tau)/\Delta^s(\tau)=0$.",
    ),
    rec(
        "RLN-P3-C06-Entry6-5-1",
        r"Let $\delta$ denote any integer, and let $n$ denote a nonnegative integer. "
        r"Suppose that $\varpi$ is a prime of the form $6\lambda-1$. Then "
        r"$p_{\delta\varpi-4}\!\left(n\varpi-\dfrac{\varpi+1}{6}\right)\equiv 0 "
        r"(\mathrm{mod}\,\varpi)$.",
    ),
    rec(
        "RLN-P3-C06-Entry6-5-2",
        r"For each positive integer $n$, $p_6(5n-1)\equiv 0$ $(\mathrm{mod}\,5)$ and "
        r"$p_7(11n-2)\equiv 0$ $(\mathrm{mod}\,11)$.",
    ),
    rec(
        "RLN-P3-C06-Entry6-5-3",
        r"Under the hypotheses of Entry 6.5.1, "
        r"$p_{-6}\!\left(\dfrac{n\varpi-\varpi+1}{4}\right)\equiv 0 "
        r"(\mathrm{mod}\,\varpi^2)$.",
    ),
    rec(
        "RLN-P3-C06-Entry6-6-1",
        r"The coefficient of $x^n$ in "
        r"$(1-2x+2x^4-2x^9+\cdots)^{-1}$ is nearly "
        r"$\dfrac{1}{4n}\left(\dfrac{\cosh(\pi\sqrt{n})-\sinh(\pi\sqrt{n})}"
        r"{\pi\sqrt{n}}\right)$.",
    ),
    rec(
        "RLN-P3-C06-Entry6-6-2",
        r"If $c_n$, $n\ge 0$, is defined by "
        r"$\displaystyle\sum_{n=0}^{\infty} c_n q^n = \frac{1}{\varphi(-q)}$, then "
        r"$c_n=\dfrac{d}{dn}\frac{\cosh(\pi\sqrt{n})-1}{2\pi\sqrt{n}} "
        r"+ \sqrt{3}\cdot 2\cos\!\left(\dfrac{2n\pi}{3}-\dfrac{\pi}{6}\right) "
        r"\dfrac{d}{dn}\frac{\cosh(\frac{1}{3}\pi\sqrt{n})-1}{2\pi\sqrt{n}} "
        r"+ \cdots$.",
    ),
    rec(
        "RLN-P3-C06-Entry6-6-3",
        r"If $c_n$, $n\ge 0$, is defined by "
        r"$\displaystyle\sum_{n=0}^{\infty} c_n q^n = \frac{1}{(q;q^2)_{\infty}} "
        r"= \frac{1}{(-q;q)_{\infty}}$, then "
        r"$\sqrt{2}\,c_n=\dfrac{d}{dn}J_0\!\left(i\pi\sqrt{\frac{n+1}{24}}\right) "
        r"+ 2\cos\!\left(\dfrac{2n\pi}{3}-\dfrac{\pi}{9}\right) "
        r"\dfrac{d}{dn}J_0\!\left(\frac{1}{3}i\pi\sqrt{\frac{n+1}{24}}\right) "
        r"+ \cdots$, where $J_0(x)$ denotes the ordinary Bessel function of order $0$.",
    ),
    rec(
        "RLN-P3-C06-Entry6-6-4",
        r"If $c_n$, $n\ge 0$, is defined by "
        r"$\displaystyle\sum_{n=0}^{\infty} c_n q^n = (-q;q^2)_{\infty}$, then "
        r"$c_n=\dfrac{d}{dn}J_0\!\left(i\pi\sqrt{\frac{n-1}{24}}\right) "
        r"+ 2\cos\!\left(\dfrac{2n\pi}{3}-\dfrac{2\pi}{9}\right) "
        r"\dfrac{d}{dn}J_0\!\left(\frac{1}{3}i\pi\sqrt{\frac{n-1}{24}}\right) "
        r"+ \cdots$.",
    ),
    rec(
        "RLN-P3-C06-Entry6-6-5",
        r"If $c_n$, $n\ge 0$, is defined by "
        r"$\displaystyle\sum_{n=0}^{\infty} c_n q^n = \frac{1}{(aq;q)_{\infty}}$, then "
        r"$c_n\sim \dfrac{\sqrt{1-a}(kn)^{1/4}}{2n\sqrt{\pi}}e^{2\sqrt{kn}}$, "
        r"where $k=\displaystyle\sum_{m=1}^{\infty}\frac{a^m}{m^2}=:\mathrm{Li}_2(a)$ "
        r"and $\mathrm{Li}_2(a)$ is the dilogarithm.",
    ),
]
