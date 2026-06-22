"""RLN Part 3, Chapter 2 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C02 = ["ranks-cranks-part-i"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C02}


CHAPTER_2 = [
    rec(
        "RLN-P3-C02-Entry2-1-1",
        r"Let $\zeta_5$ be a primitive fifth root of unity, and let $F_5(q):=\dfrac{(q;q)_\infty}{(\zeta_5 q;q)_\infty(\zeta_5^{-1}q;q)_\infty}$. Then $F_5(q)=A(q^5)-(\zeta_5+\zeta_5^{-1})^2 q B(q^5)+(\zeta_5^2+\zeta_5^{-2})q^2 C(q^5)-(\zeta_5+\zeta_5^{-1})q^3 D(q^5)$, where $A(q):=\dfrac{(q^5;q^5)_\infty G(q)^2}{H(q)}$, $B(q):=(q^5;q^5)_\infty G(q)$, $C(q):=(q^5;q^5)_\infty H(q)$, $D(q):=\dfrac{(q^5;q^5)_\infty H(q)^2}{G(q)}$, with $G(q):=\dfrac{1}{(q;q^5)_\infty(q^4;q^5)_\infty}$ and $H(q):=\dfrac{1}{(q^2;q^5)_\infty(q^3;q^5)_\infty}$.",
    ),
    rec(
        "RLN-P3-C02-Entry2-1-2",
        r"Let $\zeta_5$ be a primitive fifth root of unity, and let $f_5(q):=\displaystyle\sum_{n=0}^{\infty}\dfrac{q^{n^2}}{(\zeta_5 q;q)_n(\zeta_5^{-1}q;q)_n}$. Then $f_5(q)=A(q^5)+(\zeta_5+\zeta_5^{-1}-2)\varphi(q^5)+q B(q^5)+(\zeta_5+\zeta_5^{-1})q^2 C(q^5)-(\zeta_5+\zeta_5^{-1})q^3\bigl(D(q^5)-(\zeta_5^2+\zeta_5^{-2}-2)\psi(q^5)/q^5\bigr)$, where $A(q)$, $B(q)$, $C(q)$, and $D(q)$ are as in Entry 2.1.1, $\varphi(q):=-1+\displaystyle\sum_{n=0}^{\infty}\dfrac{q^{5n^2}}{(q;q^5)_{n+1}(q^4;q^5)_n}$, and $\psi(q)/q:=-1/q+\displaystyle\sum_{n=0}^{\infty}\dfrac{q^{5n^2-1}}{(q^2;q^5)_{n+1}(q^3;q^5)_n}$.",
    ),
    rec(
        "RLN-P3-C02-Entry2-1-3",
        r"Write $\displaystyle\sum_{n=0}^{\infty}\lambda_n q^n=\sum_{n=0}^{\infty}\dfrac{q^{n^2}}{\prod_{k=1}^{n}\bigl(1+\dfrac{1+\sqrt{5}}{2}q^k+q^{2k}\bigr)}$. Then $\displaystyle\sum_{n=0}^{\infty}\lambda_{5n+1}q^n=\dfrac{(q^5;q^5)_\infty}{(q;q^5)_\infty(q^4;q^5)_\infty}=(q^5;q^5)_\infty G(q)$, $\displaystyle\sum_{n=0}^{\infty}\lambda_{5n+2}q^n=-\dfrac{1+\sqrt{5}}{2}\dfrac{(q^5;q^5)_\infty}{(q^2;q^5)_\infty(q^3;q^5)_\infty}=-\dfrac{1+\sqrt{5}}{2}(q^5;q^5)_\infty H(q)$, and $\lambda_{5n-1}=0$ for every integer $n$.",
    ),
    rec(
        "RLN-P3-C02-Entry2-1-4",
        r"Let $\zeta_7$ be a primitive seventh root of unity, and let $F_7(q):=\dfrac{(q;q)_\infty}{(\zeta_7 q;q)_\infty(\zeta_7^{-1}q;q)_\infty}$. Then $F_7(q)=(q^7;q^7)_\infty\Bigl(X^2(q^7)+(\zeta_7+\zeta_7^{-1}-1)q X(q^7)Y(q^7)+(\zeta_7^2+\zeta_7^{-2})q^2 Y^2(q^7)+(\zeta_7^3+\zeta_7^{-3}+1)q^3 X(q^7)Z(q^7)-(\zeta_7+\zeta_7^{-1})q^4 Y(q^7)Z(q^7)-(\zeta_7^2+\zeta_7^{-2}+1)q^6 Z^2(q^7)\Bigr)$, where $X(q):=\prod_{\substack{n\ge1\\ n\not\equiv0,\pm3\,(7)}}(1-q^n)^{-1}$, $Y(q):=\prod_{\substack{n\ge1\\ n\not\equiv0,\pm2\,(7)}}(1-q^n)^{-1}$, and $Z(q):=\prod_{\substack{n\ge1\\ n\not\equiv0,\pm1\,(7)}}(1-q^n)^{-1}$.",
    ),
    rec(
        "RLN-P3-C02-Entry2-1-5",
        r"Let $\zeta_7$ be a primitive seventh root of unity, and let $f_7(q):=\displaystyle\sum_{n=0}^{\infty}\dfrac{q^{n^2}}{(\zeta_7 q;q)_n(\zeta_7^{-1}q;q)_n}$. With $P_7(a):=(q^{7a},q^{49-7a};q^{49})_\infty$ for $a\neq0$, $P_7(0):=(q^{49};q^{49})_\infty$, $Q_m(q^7):=\Sigma_7(m,0)/P_7(0)$, and $T_m(q^7):=P_7(0)/P_7(m)$ for $m=1,2,3$, where $\Sigma_7(a,b):=\displaystyle\sum_{n=-\infty}^{\infty}\dfrac{(-1)^n q^{7b} q^{147n(n+1)/2}}{1-q^{49n+7a}}$ for $a\neq0$, $f_7(q)=(2-\zeta_7-\zeta_7^{-1})\bigl(1-A_7(q^7)+q^7 Q_1(q^7)\bigr)+A_7(q^7)+q T_1(q^7)+q^2\bigl((\zeta_7+\zeta_7^{-1})B_7(q^7)+q^{14}Q_3(q^7)(\zeta_7+\zeta_7^{-1}-\zeta_7^{-2}-\zeta_7^2)\bigr)+q^3 T_2(q^7)(1+\zeta_7^2+\zeta_7^{-2})-q^4(\zeta_7^2+\zeta_7^{-2})T_3(q^7)+q^6\bigl(q^7 Q_2(q^7)(\zeta_7^2+\zeta_7^{-2}-\zeta_7^3-\zeta_7^{-3})-C_7(q^7)(1+\zeta_7^3+\zeta_7^{-3})\bigr)$, where $A_7(q):=\dfrac{(q^7,q^3,q^4;q^7)_\infty}{(q,q^2,q^5,q^6;q^7)_\infty}$, $B_7(q):=\dfrac{(q^7,q^2,q^5;q^7)_\infty}{(q,q^3,q^4,q^6;q^7)_\infty}$, and $C_7(q):=\dfrac{(q^7,q,q^6;q^7)_\infty}{(q^2,q^3,q^4,q^5;q^7)_\infty}$.",
    ),
]
