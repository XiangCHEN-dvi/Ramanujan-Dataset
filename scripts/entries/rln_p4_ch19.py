"""RLN Part 4, Chapter 19 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C19 = ["miscellaneous-analysis"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C19}


CHAPTER_19 = [
    rec(
        "RLN-P4-C19-Entry19-2-1",
        r"Let $\sigma_s(n)=\sum_{d\mid n}d^s$, and let $\zeta(s)$ denote the Riemann zeta function. Then "
        r"$\Gamma\!\left(s+\dfrac{1}{2}\right)\left\{\dfrac{\zeta(1-s)}{s-\frac{1}{2}}x^{s-\frac{1}{2}}"
        r"+\dfrac{\zeta(-s)}{2}\tan\!\left(\dfrac{\pi s}{2}\right)x^{s+\frac{1}{2}}\right."
        r"+\sum_{n=1}^{\infty}\dfrac{\sigma_s(n)}{2i}\left[(x-in)^{-s-\frac{1}{2}}"
        r"-(x+in)^{-s-\frac{1}{2}}\right]\right\}=(2\pi)^s\left\{\dfrac{\zeta(1-s)}{2\sqrt{\pi x}}"
        r"-\pi\sqrt{\pi x}\,\zeta(-s)\tan\!\left(\dfrac{\pi s}{2}\right)"
        r"+\sqrt{\pi}\sum_{n=1}^{\infty}\dfrac{\sigma_s(n)}{\sqrt{n}}"
        r"e^{-2\pi\sqrt{2n}\,x}\sin\!\left(\dfrac{\pi}{4}+2\pi\sqrt{2n}\,x\right)\right\}$.",
    ),
    rec(
        "RLN-P4-C19-Entry19-2-2",
        r"Let $\sigma_s(n)$ and $\zeta(s)$ be as in the preceding entry. If $\alpha$ and $\beta$ are "
        r"positive numbers such that $\alpha\beta=4\pi^2$, then "
        r"$\alpha^{(s+1)/2}\left\{\dfrac{1}{\alpha}\zeta(1-s)+\dfrac{1}{2}\zeta(-s)"
        r"\tan\!\left(\dfrac{\pi s}{2}\right)+\sum_{n=1}^{\infty}\sigma_s(n)\sin(n\alpha)\right\}"
        r"=\beta^{(s+1)/2}\left\{\dfrac{1}{\beta}\zeta(1-s)+\dfrac{1}{2}\zeta(-s)"
        r"\tan\!\left(\dfrac{\pi s}{2}\right)+\sum_{n=1}^{\infty}\sigma_s(n)\sin(n\beta)\right\}$.",
    ),
    rec(
        "RLN-P4-C19-Entry19-7-1",
        r"Let $n>0$ and let $t>0$. Then "
        r"$\displaystyle\int_0^{\infty}\dfrac{\sin(\pi t x)}{x\cosh(\pi x)}e^{-i\pi n x^2}\,dx"
        r"=\dfrac{\pi}{2}-2\sum_{k=0}^{\infty}\dfrac{(-1)^k e^{-(2k+1)\pi t/2+(2k+1)^2 i\pi n/4}}{2k+1}"
        r"-\pi\sqrt{n}\,e^{-i\pi/4}\int_0^{\infty}\sum_{k=0}^{\infty}"
        r"(-1)^k e^{(t+u+(2k+1)i)^2 i\pi/(4n)}\,du$.",
    ),
    rec(
        "RLN-P4-C19-Entry19-8-1",
        r"For $x>0$, define $r>0$ and $0<\theta<\dfrac{\pi}{2}$ by "
        r"$r\cos\theta=\displaystyle\int_0^{\infty}\dfrac{e^{-xt}}{1+t^2}\,dt$ and "
        r"$r\sin\theta=\displaystyle\int_0^{\infty}\dfrac{te^{-xt}}{1+t^2}\,dt$. Then "
        r"$r^2=\displaystyle\int_0^{\infty}\dfrac{e^{-xt}}{t}\log(1+t^2)\,dt$.",
    ),
    rec(
        "RLN-P4-C19-Entry19-8-2",
        r"For $x>0$, with $r$ and $\theta$ as in Entry 19.8.1, "
        r"$\displaystyle\int_0^x\dfrac{\sin u}{u}\,du=\dfrac{\pi}{2}-r\cos(x-\theta)$ and "
        r"$\displaystyle\int_0^x\dfrac{1-\cos u}{u}\,du=\gamma+\log x-r\sin(x-\theta)$, "
        r"where $\gamma$ denotes Euler's constant.",
    ),
    rec(
        "RLN-P4-C19-Entry19-8-3",
        r"Let $S(x):=\displaystyle\int_0^x\dfrac{\sin u}{u}\,du$ for $x>0$. Then $S(x)$ has local maxima "
        r"at $x=(2n+1)\pi$, $n\ge 0$, with maximum values "
        r"$S(2n+1)=\dfrac{\pi}{2}+\displaystyle\int_0^{\infty}\dfrac{e^{-(2n+1)\pi t}}{1+t^2}\,dt$, "
        r"while the local minima are at $x=2n\pi$, $n\ge 1$, with minimum values "
        r"$S(2n)=\dfrac{\pi}{2}-\displaystyle\int_0^{\infty}\dfrac{e^{-2n\pi t}}{1+t^2}\,dt$.",
    ),
    rec(
        "RLN-P4-C19-Entry19-9-1",
        r"If $|\operatorname{Re}\beta|<1$, $|\operatorname{Im}\alpha|<1$, and "
        r"$\cosh\!\left(\dfrac{\pi\beta}{2}\right)=\sec\!\left(\dfrac{\pi\alpha}{2}\right)$, then "
        r"$\displaystyle\prod_{n=0}^{\infty}\left(\dfrac{(2n+1)^2+\alpha^2}{(2n+1)^2-\beta^2}\right)"
        r"^{(-1)^n(2n+1)}=e^{\pi\alpha\beta/2}$.",
    ),
    rec(
        "RLN-P4-C19-Entry19-9-2",
        r"For $|x|<1$, "
        r"$\displaystyle\prod_{n=1}^{\infty}\left[\left(1+\dfrac{x}{n^2}\right)^{n^2}e^{-x}\right]"
        r"=e^{x/2}$, provided that "
        r"$x=\dfrac{1}{\pi}\log\!\left[\left(1+\dfrac{\sqrt{5}}{2}\right)^2\right]$.",
    ),
    rec(
        "RLN-P4-C19-Entry19-10-1",
        r"Let $0<k<1$, $K=K(k)$ the complete elliptic integral of the first kind, "
        r"$q=\exp\!\left(-\pi K'/K\right)$ with $K'=K(k')$ and $k'=\sqrt{1-k^2}$, and for "
        r"$0<\varphi\le\dfrac{\pi}{2}$ set $\theta=\dfrac{2K}{\pi}\displaystyle\int_0^{\varphi}"
        r"\dfrac{dt}{\sqrt{1-k^2\sin^2 t}}$. Then "
        r"$\log\tan\!\left(\dfrac{\pi}{4}+\dfrac{\theta}{2}\right)"
        r"+4\sum_{n=0}^{\infty}\dfrac{(-1)^n q^{2n+1}\sin\{(2n+1)\theta\}}{(2n+1)(1-q^{2n+1})}"
        r"=\log\tan\!\left(\dfrac{\pi}{4}+\dfrac{\varphi}{2}\right)$.",
    ),
    rec(
        "RLN-P4-C19-Entry19-10-2",
        r"With the notation of Entry 19.10.1, also put "
        r"$\theta'=\dfrac{2K}{\pi}\displaystyle\int_0^{\varphi}\dfrac{dt}{\sqrt{1-k'^2\sin^2 t}}$. Then "
        r"$\theta'+2\sum_{n=1}^{\infty}\dfrac{q^n\sinh(2n\theta')}{n(1+q^{2n})}"
        r"=\log\tan\!\left(\dfrac{\pi}{4}+\dfrac{\varphi}{2}\right)$.",
    ),
]
