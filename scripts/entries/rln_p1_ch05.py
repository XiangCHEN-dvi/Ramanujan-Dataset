"""RLN Part 1, Chapter 5 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C05 = ["finite-rogers-ramanujan-continued-fractions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C05}


CHAPTER_5 = [
    rec("RLN-P1-C05-Entry5-2-1", "Let $q$ be a primitive $m$th root of unity and $|a|<1/4$. Let $R(a)$ be the continued fraction defined in (5.1.5). Then $R(a)=\\dfrac{P_{m-1}(a)+\\dfrac{1}{2}\\left(-1+\\sqrt{1+4am}\\right)}{Q_{m-1}(a)}$, where $\\dfrac{P_{m-1}(a)}{Q_{m-1}(a)}=\\dfrac{a}{1+\\dfrac{aq}{1+\\cdots+\\dfrac{aq^{m-2}}{1}}}$."),
    rec("RLN-P1-C05-Entry5-3-1", "Let $A_0\\equiv 1$, $A_{-1}\\equiv 1$, and $A_{-2}\\equiv 0$. For $n\\ge 1$, let $A_n(a)=\\sum_{j=0}^{\\lfloor(n+1)/2\\rfloor}a^j\\binom{n-j+1}{j}_q$. Then for $n\\ge 0$: (i) $A_{n-1}(a)A_{n-1}(aq)-A_n(a)A_{n-2}(aq)=(-a)^n q^{n(n+1)/2}$; (ii) $A_n(a)=A_{n-1}(aq)+aqA_{n-2}(aq^2)$; (iii) $A_n(a)=A_{n-1}(a)+aq^n A_{n-2}(a)$; (iv) $1+\\dfrac{aq}{1+\\dfrac{aq^2}{1+\\cdots+\\dfrac{aq^n}{1+\\eta}}}=\\dfrac{A_{n-1}(aq)+\\eta A_{n-2}(aq)}{A_n(a)+\\eta A_{n-1}(a)}$."),
    rec("RLN-P1-C05-Entry5-3-2", "Let $|a|<1/4$, $|\\lambda|<1/4$, and $|q|\\le 1$. If $\\varepsilon$ is the continued fraction defined in (5.3.1), then $\\varepsilon=\\dfrac{A_{n-2}(aq)+Z}{A_{n-1}(a)}$, where $Z$ is a root of $\\lambda Z^2+\\{A_n(a)+\\lambda A_{n-2}(aq)\\}Z=(-a)^n q^{n(n+1)/2}$, and the ambiguous sign in the solution is always positive."),
    rec("RLN-P1-C05-Entry5-3-3", "Let $A(a):=\\lim_{n\\to\\infty}A_n(a)$. If $q^n=1$ with $q$ primitive, then $A_{n-1}(a)+aA_{n-3}(aq)=1$ and $A_{n-2}(a)A(aq)-A_{n-3}(aq)A(a)=(-a)^{n-1}q^{n(n-1)/2}A(aq^n)$."),
    rec("RLN-P1-C05-Entry5-4-1", "If $K'/K=\\sqrt{47}$ and $t:=t_{47}:=2^{1/3}(k_{47}k'_{47})^{1/12}$, then $\\dfrac{1-t}{1-t^2}\\dfrac{1}{1-t^3}\\dfrac{1}{1-t^4}=0$. Furthermore, $t_{47}=\\sqrt{2}\\,e^{-\\pi\\sqrt{47}/24}(q_{47};-q_{47})_\\infty$."),
    rec("RLN-P1-C05-Entry5-4-2", "If $K'/K=\\sqrt{39}$, $L'/L=\\sqrt{13/3}$, and $t:=t_{39}:=(k_{39}k'_{39}/(\\ell^{13/3}\\ell'^{13/3}))^{1/12}$, then $\\dfrac{1-t}{1-t^2}\\dfrac{1}{1-t^3}=0$. Moreover, $t_{39}=\\dfrac{e^{-\\pi\\sqrt{13/3}/12}}{(-q_{13/3};q_{13/3}^2)_\\infty(-q_{13/3}^3;q_{13/3}^6)_\\infty}$."),
    rec("RLN-P1-C05-Entry5-4-3", "If $t:=t_{23}:=2^{1/3}(k_{23}k'_{23})^{1/12}$, then $\\dfrac{1-t^2}{1-t^3}=0$."),
    rec("RLN-P1-C05-Entry5-4-4", "If $t:=t_{31}:=2^{1/3}(k_{31}k'_{31})^{1/12}$, then $\\dfrac{1-t}{1-t^3}=0$."),
    rec("RLN-P1-C05-Entry5-5-1", "For each positive integer $n$, $1+\\dfrac{aq}{1+\\dfrac{a^2q^4}{1+\\dfrac{a^2q^8}{1+\\cdots+\\dfrac{a^2q^{4(n-1)}}{1}}}=\\dfrac{1}{1-\\dfrac{aq}{1+\\dfrac{aq}{1-\\dfrac{aq^3}{1+\\cdots-aq^{2n-1}+aq^{2n-1}}}}}$, where for $n=1$ the left side equals $1+aq$."),
    rec("RLN-P1-C05-Entry5-5-2", "Let $\\{a_i\\}$ be an arbitrary sequence. Then $\\dfrac{1-a_1}{1+a_1}\\dfrac{1-a_2}{1+a_2}\\dfrac{1-a_3}{1+a_3}\\cdots=1+\\dfrac{a_1}{1+a_1a_2+a_2a_3+\\cdots}$."),
    rec("RLN-P1-C05-Entry5-5-3", "Let $\\{a_i\\}$ be an arbitrary sequence. Then $1-a_1+\\dfrac{1-a_2}{1-a_3+\\cdots}=1+\\dfrac{1}{a_1+\\dfrac{1}{a_2+a_3+\\cdots}}$."),
    rec("RLN-P1-C05-Entry5-5-4", "Let $\\omega$ be a cube root of unity and let $\\{a_i\\}$ be an arbitrary sequence. Then $\\dfrac{1-\\omega}{a_1-\\omega^2}\\dfrac{1-\\omega}{a_2-\\omega^2}\\dfrac{1-\\omega}{a_3-\\omega^2}\\cdots=1+\\dfrac{\\omega}{1+a_1-\\dfrac{1+a_2}{1+a_3-\\cdots}}$."),
]
