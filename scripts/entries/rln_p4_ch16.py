"""RLN Part 4, Chapter 16 — mined manuscript fragments (preliminary product paper).

No Entry labels in Berndt; results extracted from Ramanujan's preliminary manuscript
on the product $\prod_{n=0}^\infty(1+x/(a+nd))^3$ (book eqs. 16.2.1–16.6.7).
"""

from __future__ import annotations

TOPICS_C16 = ["product-formula-preliminary-paper"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C16}


CHAPTER_16 = [
    rec(
        "RLN-P4-C16-Formula1601",
        r"Ramanujan defines "
        r"$\varphi(\alpha,\beta)=\prod_{n=1}^\infty \left(1+\dfrac{\alpha+\beta}{n+\alpha}\right)^3$ "
        r"and factors each factor as "
        r"$\left(1+\dfrac{\alpha+\beta}{n+\alpha}\right)^3"
        r"=\left(1+\dfrac{\alpha+2\beta}{n}\right)\!\left(1+\dfrac{2\alpha+\beta}{n}\right)"
        r"\left(1+\dfrac{\alpha}{n}\right)^3\!\left(1+\dfrac{\beta}{n}\right)^3"
        r"\left\{1-\left(\dfrac{(\alpha-\beta)+i(\alpha+\beta)/\sqrt{3}}{2n}\right)^2\right\}"
        r"\left\{1-\left(\dfrac{(\alpha-\beta)-i(\alpha+\beta)/\sqrt{3}}{2n}\right)^2\right\}$.",
    ),
    rec(
        "RLN-P4-C16-Formula1602",
        r"Ramanujan evaluates "
        r"$\prod_{n=1}^\infty \left(1+\dfrac{\alpha+2\beta}{n}\right)\!\left(1+\dfrac{2\alpha+\beta}{n}\right)"
        r"\left(1+\dfrac{\alpha}{n}\right)^3\!\left(1+\dfrac{\beta}{n}\right)^3"
        r"=\dfrac{\{\Gamma(1+\alpha)\Gamma(1+\beta)\}^3}{\Gamma(1+\alpha+2\beta)\Gamma(1+\beta+2\alpha)}$.",
    ),
    rec(
        "RLN-P4-C16-Formula1603",
        r"Ramanujan gives "
        r"$\prod_{n=1}^\infty \left\{1-\left(\dfrac{(\alpha-\beta)+i(\alpha+\beta)/\sqrt{3}}{2n}\right)^2\right\}"
        r"\left\{1-\left(\dfrac{(\alpha-\beta)-i(\alpha+\beta)/\sqrt{3}}{2n}\right)^2\right\}"
        r"=\dfrac{\cosh\!\left(\pi(\alpha+\beta)/\sqrt{3}\right)-\cos\pi(\alpha-\beta)}"
        r"{2\pi^2(\alpha^2+\alpha\beta+\beta^2)}$, "
        r"hence "
        r"$\dfrac{\varphi(\alpha,\beta)}{\varphi(\beta,\alpha)}"
        r"=\dfrac{\{\Gamma(1+\alpha)\Gamma(1+\beta)\}^3}{\Gamma(1+\alpha+2\beta)\Gamma(1+\beta+2\alpha)}"
        r"\cdot\dfrac{\cosh\!\left(\pi(\alpha+\beta)/\sqrt{3}\right)-\cos\pi(\alpha-\beta)}"
        r"{2\pi^2(\alpha^2+\alpha\beta+\beta^2)}$.",
    ),
    rec(
        "RLN-P4-C16-Formula1604",
        r"For $\alpha=\beta$, Ramanujan obtains "
        r"$\prod_{n=1}^\infty \left(1+\dfrac{2\alpha}{n+\alpha}\right)^3"
        r"=\dfrac{\{\Gamma(1+\alpha)\}^3}{\Gamma(1+3\alpha)}"
        r"\cdot\dfrac{\sinh(\pi\alpha/\sqrt{3})}{\pi\alpha/\sqrt{3}}$; "
        r"for $\beta=\alpha+1$, "
        r"$\prod_{n=1}^\infty \left(1+\dfrac{1+2\alpha}{n+\alpha}\right)^3"
        r"=\dfrac{\{\Gamma(1+\alpha)\}^3}{\Gamma(2+3\alpha)}"
        r"\cdot\dfrac{\cosh\!\left(\pi(\tfrac12+\alpha)/\sqrt{3}\right)}{\pi}$.",
    ),
    rec(
        "RLN-P4-C16-Formula1605",
        r"Using Binet's formula for $\log\Gamma(\alpha)$, Ramanujan deduces "
        r"$\tfrac12\log(2\pi\alpha)+\log\prod_{n=1}^\infty\left(1+\dfrac{\alpha}{n}\right)^3"
        r"=\log\!\left(\dfrac{\cosh(\pi\alpha/\sqrt{3})-\cos\pi\alpha}{\pi\alpha}\right)"
        r"-\dfrac{\pi\alpha}{\sqrt{3}}+2\int_0^\infty \dfrac{(\tan^{-1}(x/\alpha))^3}{e^{2\pi x}-1}\,dx$, "
        r"so $\int_0^\infty \dfrac{(\tan^{-1} x)^3}{e^{2\pi\alpha x}-1}\,dx$ is finite for positive integers $\alpha$.",
    ),
    rec(
        "RLN-P4-C16-Formula1606",
        r"Ramanujan gives "
        r"$\sum_{n=1}^\infty \dfrac{(-1)^{n-1}n^2}{n^3+\alpha^3}"
        r"=\dfrac13\sum_{n=1}^\infty \dfrac{(-1)^{n-1}}{n+\alpha}"
        r"+\dfrac43\sum_{n=1}^\infty \dfrac{(-1)^{n-1}(2n-\alpha)}{(2n-\alpha)^2+3\alpha^2}$, "
        r"expressible in finite terms when $\alpha$ is an odd integer; for $\alpha=1$, "
        r"$\sum_{n=1}^\infty \dfrac{(-1)^{n-1}n^2}{n^3+1}"
        r"=\dfrac13\left(1-\log 2+\pi\,\mathrm{sech}\!\dfrac{\pi}{2\sqrt{3}}\right)$.",
    ),
    rec(
        "RLN-P4-C16-Formula1607",
        r"Ramanujan states "
        r"$\sum_{n=1}^\infty \dfrac{n}{n^4+4\alpha^4}=\dfrac{1}{4\alpha}\sum_{n=1}^{2\alpha}\dfrac{1}{(n-\alpha)^2+\alpha^2}$ "
        r"when $2\alpha$ is a positive integer, and "
        r"$\dfrac{1}{16\pi\alpha^4}+\sum_{n=1}^\infty \dfrac{n\coth(n\pi)}{n^4+4\alpha^4}"
        r"=\dfrac{\pi}{8\alpha^2}\cdot\dfrac{\cosh(2\pi\alpha)+\cos(2\pi\alpha)}"
        r"{\cosh(2\pi\alpha)-\cos(2\pi\alpha)}$.",
    ),
    rec(
        "RLN-P4-C16-Formula1608",
        r"For positive integer $\alpha$, Ramanujan gives "
        r"$\sum_{n=0}^\infty \dfrac{2n+1}{(2n+1)^4+4\alpha^4}"
        r"=\dfrac{1}{4\alpha}\sum_{n=0}^{\alpha-1}\dfrac{1}{(2n+1-\alpha)^2+\alpha^2}$, "
        r"and the example "
        r"$\sum_{n=1}^\infty \dfrac{1}{(n^2+(n+1)^2)(\cosh((2n+1)\pi)-\cosh\pi)}"
        r"=\dfrac{1}{2\sinh\pi}\!\left(\dfrac{1}{\pi}+\coth\pi-\dfrac{\pi}{2}\tanh^2\!\dfrac{\pi}{2}\right)$.",
    ),
]
