"""RLN Part 4, Chapter 17 — mined manuscript fragments (arctan integral preliminary).

No Entry labels in Berndt; results extracted from Ramanujan's preliminary manuscript
on $\int_0^x (\tan^{-1}t/t)\,dt$ (book eqs. 17.2.1–17.2.23).
"""

from __future__ import annotations

TOPICS_C17 = ["arctan-integral-preliminary-paper"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C17}


CHAPTER_17 = [
    rec(
        "RLN-P4-C17-Formula1701",
        r"Let $\Phi(x)=\int_0^x \dfrac{\tan^{-1}t}{t}\,dt$. For $x>0$, "
        r"$\Phi(x)-\Phi(1/x)=\tfrac12\pi\log x$; for $-1\le x\le 1$, "
        r"$\Phi(x)=\sum_{n=0}^\infty \dfrac{(-1)^n x^{2n+1}}{(2n+1)^2}$.",
    ),
    rec(
        "RLN-P4-C17-Formula1702",
        r"For $0<x<\tfrac12\pi$, Ramanujan gives "
        r"$\sum_{n=0}^\infty \dfrac{\sin((4n+2)x)}{(2n+1)^2}=\Phi(\tan x)-x\log(\tan x)$, "
        r"$\sum_{n=0}^\infty \dfrac{(-1)^n}{(4n+1)^2}"
        r"=\Phi(\sqrt{2}-1)+\dfrac{\pi}{8}\log(1+\sqrt{2})+\dfrac{\pi^2}{16}$, "
        r"and $\Phi(1)=\tfrac32\Phi(2-\sqrt{3})+\tfrac18\pi\log(2+\sqrt{3})$.",
    ),
    rec(
        "RLN-P4-C17-Formula1703",
        r"For $0<x<\tfrac12\pi$, Ramanujan has "
        r"$\sum_{n=0}^\infty \dfrac{(\tfrac12)_n}{n!}\,\dfrac{\cos^{2n+1}x+\sin^{2n+1}x}{(2n+1)^2}"
        r"=\Phi(\tan x)+\tfrac12\pi\log(2\cos x)$, "
        r"$\sum_{n=1}^\infty \dfrac{\sin(nx)}{n^2\cos^n x}=\Phi(\tan x)+\tfrac12\pi\log(\cos x)-x\log(\sin x)$, "
        r"and "
        r"$\sum_{n=1}^\infty \dfrac{\sin(nx)}{n^2}\!\left(1-\dfrac{1}{\alpha}\right)^n\!\cos^{-n}x"
        r"+\sum_{n=1}^\infty \dfrac{\sin(n(x+\pi/2))}{n^2}(1-\alpha)^n\sin^n x"
        r"=\Phi(\tan x)-\Phi(\alpha\tan x)+x\log\alpha$.",
    ),
    rec(
        "RLN-P4-C17-Formula1704",
        r"Ramanujan gives "
        r"$\prod_{n=0}^\infty \left(1-\dfrac{x^2}{(2n+1)^2}\right)^{(-1)^n(2n+1)}"
        r"=\dfrac{\pi}{8}\exp\!\left(\dfrac{4}{\pi}\Phi(1)\right)$, "
        r"$\prod_{n=0}^\infty \left(1+\dfrac{x^2}{(2n+1)^2}\right)^{(-1)^n(2n+1)}"
        r"=\exp\!\left(\dfrac{4}{\pi}\left\{\Phi(1)-\Phi(e^{-\pi x/2})-2x\tan^{-1}(e^{-\pi x/2})\right\}\right)$, "
        r"and for $\alpha\beta=\pi^2$, "
        r"$\sum_{n=0}^\infty \dfrac{1}{(2n+1)^2(e^{(2n+1)\alpha}-1)}"
        r"+\dfrac{\pi}{4\beta}\sum_{n=1}^\infty \dfrac{1}{n^2(e^{n\beta}+e^{-n\beta})}"
        r"=\dfrac{\pi}{16}\!\left(\alpha^3+\beta^3\right)-\dfrac12\Phi(1)$.",
    ),
    rec(
        "RLN-P4-C17-Formula1705",
        r"From $\alpha=\beta=\pi$ in the residue formula, Ramanujan calculates "
        r"$\Phi(1)\approx 0.9159655942$; for $0<x<\tfrac12\pi$, "
        r"$\sum_{n=0}^\infty \dfrac{n!}{(\tfrac32)_n}\,\dfrac{\sin^{2n+1}x}{2n+1}=2\Phi(\tan\tfrac{x}{2})$.",
    ),
]
