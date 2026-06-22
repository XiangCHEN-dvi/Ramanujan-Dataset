"""RLN Part 4, Chapter 11 — mined manuscript fragments (sums involving primes).

No Entry labels in Berndt; results extracted from Ramanujan's two partial unpublished
manuscripts on sums involving primes (book eqs. 11.2.1–11.11.4).
"""

from __future__ import annotations

TOPICS_C11 = ["sums-involving-primes"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C11}


CHAPTER_11 = [
    rec(
        "RLN-P4-C11-Formula1101",
        r"Let $p$ be the greatest prime not exceeding $x$, $\pi(x)$ the number of primes "
        r"$\le x$, and $\vartheta(x)=\log 2+\log 3+\log 5+\cdots+\log p$. With $\pi(x)=n$, "
        r"Ramanujan has $\pi(x)\log x-\vartheta(x)=\int_2^x \dfrac{\pi(t)}{t}\,dt$.",
    ),
    rec(
        "RLN-P4-C11-Formula1102",
        r"Without assuming the prime number theorem, if $p$ is the greatest prime not exceeding "
        r"$x$ and $\pi(x)=n$, then $\log x=\log n+\log\log n+O(1)$, and hence "
        r"$\log 2+\log 3+\log 5+\cdots+\log p=n\log n+n\log\log n+O(n)$.",
    ),
    rec(
        "RLN-P4-C11-Formula1103",
        r"Assuming the Riemann hypothesis, Ramanujan gives "
        r"$\vartheta(x)=x-\sqrt{x}-\sum_\rho \dfrac{x^\rho}{\rho}+O(x^{1/3})$, "
        r"where $\rho$ runs over the nontrivial zeros of the zeta function, and "
        r"$\pi(x)=\mathrm{Li}\!\left(x-\sqrt{x}-\sum_\rho \dfrac{x^\rho}{\rho}+O\!\left(\dfrac{\sqrt{x}}{\log x}\right)\right)$ "
        r"with $\mathrm{Li}(x)=\int_0^x \dfrac{dt}{\log t}$.",
    ),
    rec(
        "RLN-P4-C11-Formula1104",
        r"Under the Riemann hypothesis, with $\pi(x)=n$, Ramanujan claims "
        r"$\limsup\dfrac{\vartheta(x)-\mathrm{Li}^{-1}(n)}{\sqrt{\log n/n}}=4+\gamma-\log(4\pi)$ "
        r"and $\liminf\dfrac{\vartheta(x)-\mathrm{Li}^{-1}(n)}{\sqrt{\log n/n}}=\log(4\pi)-\gamma$.",
    ),
    rec(
        "RLN-P4-C11-Formula1105",
        r"If $\varphi'(t)$ is continuous between $2$ and $x$, then "
        r"$\varphi(2)+\varphi(3)+\varphi(5)+\cdots+\varphi(p)=\pi(x)\varphi(x)-\int_2^x \varphi'(t)\pi(t)\,dt$, "
        r"and "
        r"$\varphi(2)\log 2+\varphi(3)\log 3+\cdots+\varphi(p)\log p"
        r"=\vartheta(x)\varphi(x)-\int_2^x \varphi'(t)\vartheta(t)\,dt$.",
    ),
    rec(
        "RLN-P4-C11-Formula1106",
        r"For $s>1$, Ramanujan gives "
        r"$\sum_{p\le x}\dfrac{\log p}{p^s-1}=-\dfrac{\zeta'(s)}{\zeta(s)}+\dfrac{x^{1-s}}{1-s}+O(x^{1-s}e^{-a\sqrt{\log x}})$; "
        r"for $s=1$, $\sum_{p\le x}\dfrac{\log p}{p^s-1}=\log x-\gamma+O(e^{-a\sqrt{\log x}})$; "
        r"and for $s<1$, "
        r"$\prod_{p\le x}(1-p^{-s})=e^{\mathrm{Li}(x^{1-s})}+O(x^{1-s}e^{-a\sqrt{\log x}})$.",
    ),
    rec(
        "RLN-P4-C11-Formula1107",
        r"For monotonic continuous $\varphi$ with $\log|\varphi'(x)|=O(x)$, Ramanujan defines a "
        r"continuous function $F(x)$ and deduces "
        r"$\sum_{p\le x}\varphi(\vartheta(p))\log p=\int_0^{\vartheta(x)}\varphi(z)\,dz"
        r"+\tfrac12\varphi(\vartheta(x))\log x-\tfrac12\int_1^x \dfrac{\varphi(\vartheta(z))}{z}\,dz+R(x)$, "
        r"where $R(x)=O\!\left(\dfrac{1}{|\varphi'(\vartheta(x))|\,(\log x)^2}\right)$.",
    ),
    rec(
        "RLN-P4-C11-Formula1108",
        r"Ramanujan gives "
        r"$\sum_{p\le x}e^{-s\vartheta(p)}\log p"
        r"=\dfrac1s-\dfrac{\log x}{x^s-1}e^{-s\vartheta(x)}"
        r"-\int_1^x \dfrac{1-z^s+sz^s\log z}{z(z^s-1)^2}\,e^{-s\vartheta(z)}\,dz$, "
        r"and the generalization "
        r"$\sum_{p\le x}e^{-s\vartheta(p)}f(p)=\dfrac{f(2)}{2^s-1}-\dfrac{f(x)}{x^s-1}e^{-s\vartheta(x)}"
        r"+\int_2^x e^{-s\vartheta(z)}\!\left(\dfrac{f'(z)}{z^s-1}-\dfrac{sz^{s-1}f(z)}{(z^s-1)^2}\right)dz$.",
    ),
    rec(
        "RLN-P4-C11-Formula1109",
        r"Ramanujan obtains "
        r"$2^{-s}\log 2+6^{-s}\log 3+30^{-s}\log 5+\cdots"
        r"=\dfrac1s-\int_1^\infty e^{-s\vartheta(x)}\dfrac{1-x^s+sx^s\log x}{x(1-x^s)^2}\,dx$, "
        r"and as $s\to 0$ claims "
        r"$(1-2^{-s})(1-6^{-s})(1-30^{-s})(1-210^{-s})\cdots"
        r"=\exp\!\left(\dfrac{\pi^2}{6s\log s}\right)+O\!\left(\dfrac{1}{s(\log s)^2}\right)$.",
    ),
    rec(
        "RLN-P4-C11-Formula1110",
        r"Letting $x\to\infty$ in the prime-sum formulas, Ramanujan gives "
        r"$\varphi(\vartheta(2))\log 2+\varphi(\vartheta(3))\log 3+\cdots"
        r"=\int_0^\infty \varphi(x)\,dx-\tfrac12\int_1^\infty \dfrac{\varphi(\vartheta(x))}{x}\,dx+R_\infty$, "
        r"and "
        r"$2^{-s}+6^{-s}+30^{-s}+\cdots=\dfrac{1}{2^s-1}-s\int_2^\infty \dfrac{x^{s-1}e^{-s\vartheta(x)}}{(x^s-1)^2}\,dx$.",
    ),
]
