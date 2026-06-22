"""RLN Part 5, Chapter 19 — AI curated LaTeX (Entry only).

The continuing mystery; Ramanujan statements only.
"""

from __future__ import annotations

TOPICS_C19 = ["continuing-mystery"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C19}


CHAPTER_19 = [
    rec(
        "RLN-P5-C19-Entry19-2-1",
        r"Let $\zeta_5$ be a primitive fifth root of unity and "
        r"$f_5(q):=\sum_{n=0}^{\infty}\dfrac{q^{n^2}}{(\zeta_5 q;q)_n(\zeta_5^{-1}q;q)_n}$. "
        r"With $G(q):=\dfrac{1}{(q;q^5)_\infty(q^4;q^5)_\infty}$, "
        r"$H(q):=\dfrac{1}{(q^2;q^5)_\infty(q^3;q^5)_\infty}$, "
        r"$A(q):=(q^5;q^5)_\infty\dfrac{G^2(q)}{H(q)}$, $B(q):=(q^5;q^5)_\infty G(q)$, "
        r"$C(q):=(q^5;q^5)_\infty H(q)$, $D(q):=(q^5;q^5)_\infty\dfrac{H^2(q)}{G(q)}$, "
        r"$\Phi(q):=-1+\sum_{n=0}^{\infty}\dfrac{q^{5n^2}}{(q;q^5)_{n+1}(q^4;q^5)_n}$, and "
        r"$\dfrac{\Psi(q)}{q}:=\sum_{n=0}^{\infty}\dfrac{q^{5n^2-1}}{(q^2;q^5)_{n+1}(q^3;q^5)_n}$, "
        r"Ramanujan gives "
        r"$f_5(q)=A(q^5)+(\zeta_5+\zeta_5^{-1}-2)\Phi(q^5)+qB(q^5)"
        r"+(\zeta_5+\zeta_5^{-1})q^2 C(q^5)-(\zeta_5+\zeta_5^{-1})q^3\!\left(D(q^5)"
        r"-(\zeta_5^2+\zeta_5^{-2}-2)\dfrac{\Psi(q^5)}{q^5}\right)$.",
    ),
    rec(
        "RLN-P5-C19-Entry19-9-1",
        r"Let $F(x)=[x]$ if $x$ is not an integer and $F(x)=x-\tfrac{1}{2}$ if $x$ is an integer. "
        r"If $0<\theta<1$ and $x>0$, then Ramanujan gives "
        r"$\sum_{n=1}^{\infty}F\!\left(\dfrac{x}{n}\right)\sin(2\pi n\theta)"
        r"=\dfrac{\pi x}{\tfrac{1}{2}-\theta}-\dfrac{1}{4}\cot(\pi\theta)"
        r"+\dfrac{1}{2\sqrt{x}}\sum_{m=1}^{\infty}\sum_{n=0}^{\infty}"
        r"\left(\dfrac{J_1\!\bigl(4\pi\sqrt{m(n+\theta)x}\bigr)}{\sqrt{m(n+\theta)}}"
        r"-\dfrac{J_1\!\bigl(4\pi\sqrt{m(n+1-\theta)x}\bigr)}{\sqrt{m(n+1-\theta)}}\right)$.",
    ),
    rec(
        "RLN-P5-C19-Entry19-11-1",
        r"For $|q|<1$ and complex $a,b,\lambda$, define "
        r"$G(a,b,\lambda):=\sum_{n=0}^{\infty}\dfrac{(-\lambda/a;q)_n a^n q^{n(n+1)/2}}"
        r"{(q;q)_n(-bq;q)_n}$. Ramanujan gives "
        r"$\dfrac{G(aq,b,\lambda q)}{G(a,b,\lambda)}="
        r"\cfrac{1}{1+\dfrac{aq+\lambda q}{1+\dfrac{bq+\lambda q^2}{1+\dfrac{aq^2+\lambda q^3}"
        r"{1+\dfrac{bq^2+\lambda q^4}{1+\cdots}}}}$.",
    ),
]
