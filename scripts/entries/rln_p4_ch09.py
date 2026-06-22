"""RLN Part 4, Chapter 9 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C09 = ["divisor-sums"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C09}


CHAPTER_9 = [
    rec(
        "RLN-P4-C09-Entry9-4-1",
        r"If $s>1$, then, as $n\to\infty$, "
        r"$\sigma_s(n)=n^s\sin(\pi n)\left\{\dfrac{1}{1^{s+1}}\sin(\pi n)"
        r"+\dfrac{1}{2^{s+1}}\tan\!\left(\tfrac{1}{2}\pi n\right)"
        r"+\dfrac{1}{3^{s+1}}\sin\!\left(\tfrac{1}{3}\pi n\right)"
        r"+\dfrac{1}{4^{s+1}}\tan\!\left(\tfrac{1}{4}\pi n\right)"
        r"+\dfrac{1}{5^{s+1}}\sin\!\left(\tfrac{1}{5}\pi n\right)"
        r"+\dfrac{1}{6^{s+1}}\tan\!\left(\tfrac{1}{6}\pi n\right)+\cdots\right\}$.",
    ),
    rec(
        "RLN-P4-C09-Entry9-4-2",
        r"Let $s$ be an integer greater than $1$, let $r_{2s}(n)$ denote the number of "
        r"representations of the positive integer $n$ as a sum of $2s$ squares, and set "
        r"$R(s):=\displaystyle\sum_{k=0}^{\infty}\dfrac{\cos(k\pi s)}{(2k+1)^s}$, $s>1$. "
        r"Then, as $n\to\infty$, "
        r"$r_{2s}(n)=\dfrac{\pi n^{s-1}}{(s-1)!}\,R(s)\sin(\pi n)\left\{\dfrac{1}{1^s}\sin(\pi n)"
        r"+\dfrac{1}{2^s}\sin\!\left(\tfrac{1}{2}\pi n+\tfrac{1}{2}\pi s\right)"
        r"+\dfrac{1}{3^s}\sin\!\left(\tfrac{1}{3}\pi n+\pi s\right)"
        r"+\dfrac{1}{4^s}\sin\!\left(\tfrac{1}{4}\pi n+\tfrac{3}{2}\pi s\right)"
        r"+\dfrac{1}{5^s}\sin\!\left(\tfrac{1}{5}\pi n+2\pi s\right)+\cdots\right\}$.",
    ),
    rec(
        "RLN-P4-C09-Entry9-4-3",
        r"If $s\ge5$, then, as $n\to\infty$, "
        r"$r_s(n)=\dfrac{(\pi n)^{\frac{1}{2}s}}{n\,\Gamma\!\left(\tfrac{1}{2s}\right)}"
        r"\displaystyle\sum_{p,q}\left(\dfrac{e^{-2n\pi ip/q}}{q}\displaystyle\sum_{\lambda=0}^{q-1}"
        r"e^{2\pi i\lambda^2 p/q}\right)^{\!s}+O\!\left(n^{\frac{1}{4}s}\right)$, "
        r"where the outer sum is over all positive integers $p$ and $q$ with $(p,q)=1$ and $p<q$.",
    ),
    rec(
        "RLN-P4-C09-Entry9-4-4",
        r"Let $s$ be an integer at least $5$. For $(p,q)=1$ and $0<p<q$, set "
        r"$c_{p,q}=\dfrac{1}{\sqrt{q}}\displaystyle\sum_{\lambda=0}^{q-1}e^{2\pi i\lambda^2 p/q}$. "
        r"Then, as $n\to\infty$, "
        r"$r_s(n)=\dfrac{(\pi n)^{\frac{1}{2}s}}{n\,\Gamma\!\left(\tfrac{1}{2s}\right)}"
        r"\displaystyle\sum_{p,q}\left(\dfrac{e^{-2n\pi ip/q}}{q^{\frac{1}{2}s}}(c_{p,q})^s\right)"
        r"+O\!\left(n^{\frac{1}{4}s}\right)$. "
        r"Furthermore, $c_{1,1}=0$; $c_{1,2}=0$; $c_{1,3}=i$, $c_{2,3}=-i$; "
        r"$c_{1,4}=1+i$, $c_{3,4}=1-i$; $c_{1,5}=1$, $c_{2,5}=-1$, $c_{3,5}=-1$, $c_{4,5}=1$; "
        r"$c_{1,6}=0$, $c_{5,6}=0$; $c_{1,7}=i$, $c_{2,7}=i$, $c_{3,7}=-i$, $c_{4,7}=i$, "
        r"$c_{5,7}=-i$, $c_{6,7}=-i$; $c_{1,8}=1+i$, $c_{3,8}=-1+i$, $c_{5,8}=-1-i$, $c_{7,8}=1-i$.",
    ),
    rec(
        "RLN-P4-C09-Entry9-4-5",
        r"If $s\ge5$, then, as $n\to\infty$, "
        r"$r_s(n)=\dfrac{(\pi n)^{\frac{1}{2}s}}{n\,\Gamma\!\left(\tfrac{1}{2s}\right)}\left\{\dfrac{1}{1^{\frac{1}{2}s}}"
        r"+2\dfrac{\cos\!\left(\tfrac{1}{2}n\pi-\tfrac{1}{4s}\pi\right)}{2^{\frac{1}{2}s}}"
        r"+2\dfrac{\cos\!\left(\tfrac{2}{3}n\pi-\tfrac{1}{2s}\pi\right)}{3^{\frac{1}{2}s}}"
        r"+2\dfrac{\cos\!\left(\tfrac{1}{4}n\pi-\tfrac{1}{4s}\pi\right)+2\cos\!\left(\tfrac{3}{4}n\pi-\tfrac{3}{4s}\pi\right)}{4^{\frac{1}{2}s}}"
        r"+2\dfrac{\cos\!\left(\tfrac{2}{5}n\pi\right)+2\cos\!\left(\tfrac{4}{5}n\pi-s\pi\right)}{5^{\frac{1}{2}s}}"
        r"+\cdots\right\}+O\!\left(n^{\frac{1}{4}s}\right)$.",
    ),
    rec(
        "RLN-P4-C09-Entry9-5-1",
        r"$\displaystyle\sum_{k=1}^{n}k^s\sigma_r(k)$ lies between "
        r"$\zeta(-s)\zeta(-r-s)+\dfrac{n^{1+s}}{1+s}\zeta(1-r)+\dfrac{n^{1+r+s}}{1+r+s}\zeta(1+r)"
        r"+\dfrac{1}{2}n^s\zeta(-r)+\dfrac{1}{2}n^{r+s}\zeta(r)+\dfrac{n^{s+(r+1)/2}}{1-r^2}$ "
        r"and "
        r"$\zeta(-s)\zeta(-r-s)+\dfrac{n^{1+s}}{1+s}\zeta(1-r)+\dfrac{n^{1+r+s}}{1+r+s}\zeta(1+r)"
        r"+\dfrac{1}{2}n^s\{2\zeta(1-r)-\zeta(-r)\}+\dfrac{1}{2}n^{r+s}\{2\zeta(1+r)-\zeta(r)\}"
        r"-\dfrac{n^{s+(r+1)/2}}{1-r^2}$.",
    ),
    rec(
        "RLN-P4-C09-Entry9-5-2",
        r"Let $s$ and $r$ be real numbers satisfying $s+\tfrac{1}{2}r<0$, $s+r<1$, and $s<1$. "
        r"Define $S(s,r):=\displaystyle\sum_{k=1}^{n}k^s\sigma_r(k)$. Then, for $n$ sufficiently large, "
        r"$S(s,r)\le\zeta(-s)\zeta(-s-r)+\dfrac{n^{s+1}}{s+1}\zeta(1-r)+\dfrac{n^{s+r+1}}{s+r+1}\zeta(r+1)"
        r"+\dfrac{n^{s+\frac{1}{2}(r+1)}}{1-r^2}+\dfrac{n^s}{2}\zeta(-r)+\dfrac{n^{s+r}}{2}\zeta(r)$, "
        r"provided that either $s>0$ or $s+r>0$. Furthermore, if $n$ is sufficiently large, "
        r"$S(s,r)\ge\zeta(-s)\zeta(-s-r)+\dfrac{n^{s+1}}{s+1}\zeta(1-r)+\dfrac{n^{s+r+1}}{s+r+1}\zeta(r+1)"
        r"-\dfrac{n^{s+\frac{1}{2}(r+1)}}{1-r^2}-\dfrac{n^s}{2}\zeta(-r)-\dfrac{n^{s+r}}{2}\zeta(r)+o(1)$.",
    ),
    rec(
        "RLN-P4-C09-Entry9-5-3",
        r"For unspecified parameters $r$ and $s$ and $t=[\sqrt{n}]$, "
        r"$n^\alpha\displaystyle\sum_{k=1}^{n}k^{s-\alpha}\sigma_r(k)-\displaystyle\sum_{k=1}^{n}k^s\sigma_r(k)"
        r"=n^\alpha\zeta(\alpha-s)\zeta(\alpha-r-s)-\zeta(-s)\zeta(-r-s)"
        r"+\dfrac{\alpha n^{1+s}}{(1+s)(1-\alpha+s)}\zeta(1-r)"
        r"+\dfrac{\alpha n^{1+r+s}}{(1+r+s)(1-\alpha+r+s)}\zeta(1+r)"
        r"-\dfrac{\alpha}{2}n^{s-1}\displaystyle\sum_{m=1}^{t}\left(\tfrac{1}{6}-\epsilon_m+\epsilon_m^2\right)"
        r"\left(\dfrac{n^r}{m^{r+1}}+\dfrac{n}{m^{r-1}}\right)+O(\cdots)$, "
        r"which lies between "
        r"$n^\alpha\zeta(\alpha-s)\zeta(\alpha-r-s)-\zeta(-s)\zeta(-r-s)"
        r"+\dfrac{\alpha n^{1+s}}{(1+s)(1-\alpha+s)}\zeta(1-r)"
        r"+\dfrac{\alpha n^{1+r+s}}{(1+r+s)(1-\alpha+r+s)}\zeta(1+r)"
        r"-\dfrac{\alpha}{12}n^{s-1}\zeta(-r-1)-\dfrac{\alpha}{12}n^{r+s-1}\zeta(r-1)"
        r"-\dfrac{\alpha n^{s+r/2}}{3(4-r^2)}$ "
        r"and "
        r"$n^\alpha\zeta(\alpha-s)\zeta(\alpha-r-s)-\zeta(-s)\zeta(-r-s)"
        r"+\dfrac{\alpha n^{1+s}}{(1+s)(1-\alpha+s)}\zeta(1-r)"
        r"+\dfrac{\alpha n^{1+r+s}}{(1+r+s)(1-\alpha+r+s)}\zeta(1+r)"
        r"-\dfrac{\alpha}{24}n^{s-1}\left\{\dfrac{5}{3(1-2r^{-1})}\zeta(1-r)-\zeta(-r-1)\right\}"
        r"-\dfrac{\alpha}{24}n^{r+s-1}\left\{3\left(1-\dfrac{1}{2r+1}\right)\zeta(1+r)-\zeta(r-1)\right\}"
        r"+\dfrac{\alpha n^{s+r/2}}{6(4-r^2)}$.",
    ),
    rec(
        "RLN-P4-C09-Entry9-7-1",
        r"If $\gamma$ denotes Euler's constant, then, as $x\to\infty$, "
        r"$\displaystyle\sum_{n\le x}\dfrac{2\gamma+\log n}{\sqrt{n}}"
        r"=2\sqrt{x}(\log x+2\gamma-2)+C+o(1)$, "
        r"where $C=\zeta\!\left(\tfrac{1}{2}\right)\!\left\{\tfrac{3}{2}\gamma-\tfrac{1}{4\pi}-\tfrac{1}{2}\log(8\pi)\right\}$.",
    ),
    rec(
        "RLN-P4-C09-Entry9-7-2",
        r"Let $d'(n)=d(n)-2\gamma-\log n$. Then "
        r"$\displaystyle\sum_{n=1}^{\infty}\dfrac{d'(n)}{\sqrt{n}}=\zeta^2\!\left(\tfrac{1}{2}\right)-C$, "
        r"where $C$ is defined as in Entry 9.7.1.",
    ),
    rec(
        "RLN-P4-C09-Entry9-7-3",
        r"Let $C$ be defined as in Entry 9.7.1. If $w$ is any positive number except $2\sqrt{n}$, then "
        r"$\displaystyle\sum_{2\sqrt{n}<w}d(n)\!\left(1-\dfrac{w}{\pi\sqrt{n}}\right)"
        r"+\displaystyle\sum_{2\sqrt{n}>w}d(n)\!\left(\dfrac{2}{\pi}\sin^{-1}\!\dfrac{w}{2\sqrt{n}}-\dfrac{w}{\pi\sqrt{n}}\right)"
        r"=\displaystyle\sum_{2\sqrt{n}<w}d(n)-\dfrac{w}{\pi}\!\left\{\zeta^2\!\left(\tfrac{1}{2}\right)-C\right\}"
        r"+\displaystyle\sum_{2\sqrt{n}>w}d'(n)\!\left(\dfrac{2}{\pi}\sin^{-1}\!\dfrac{w}{2\sqrt{n}}-\dfrac{w}{\pi}\right)"
        r"-\displaystyle\sum_{2\sqrt{n}<w}\dfrac{(2\gamma+\log n)w}{\pi\sqrt{n}}"
        r"+\displaystyle\sum_{2\sqrt{n}>w}(2\gamma+\log n)\!\left(\dfrac{2}{\pi}\sin^{-1}\!\dfrac{w}{2\sqrt{n}}-\dfrac{w}{\pi\sqrt{n}}\right)$.",
    ),
    rec(
        "RLN-P4-C09-Entry9-7-4",
        r"For $w>0$, "
        r"$\displaystyle\sum_{2\sqrt{n}<w}d(n)\!\left(1-\dfrac{w}{\pi\sqrt{n}}\right)"
        r"+\displaystyle\sum_{2\sqrt{n}>w}d(n)\!\left(\dfrac{2}{\pi}\sin^{-1}\!\dfrac{w}{2\sqrt{n}}-\dfrac{w}{\pi\sqrt{n}}\right)"
        r"+\dfrac{w}{\pi}\zeta^2\!\left(\tfrac{1}{2}\right)"
        r"=\dfrac{1}{2}w^2+\dfrac{1}{4}-\dfrac{1}{2}\displaystyle\sum_{n=1}^{\infty}\dfrac{d(n)}{n}e^{-2\pi w\sqrt{n}}"
        r"+\dfrac{1}{2}\displaystyle\sum_{n=1}^{\infty}\dfrac{d(n)}{n}\cos(2\pi w\sqrt{n})$.",
    ),
]
