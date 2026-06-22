"""RLN Part 1, Chapter 7 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C07 = ["asymptotic-formulas-continued-fractions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C07}


CHAPTER_7 = [
    rec("RLN-P1-C07-Entry7-3-1", "As $x\\to 0^+$, $\\displaystyle\\frac{(3x)^{1/3}}{1-\\cfrac{e^x}{1+e^{2x}-1+e^{3x}-\\cdots}}=\\dfrac{\\Gamma(\\tfrac13)}{\\Gamma(\\tfrac23)}\\,e^{G(x)}$, where $G(x)\\sim a_2 x^2+a_4 x^4+a_6 x^6+\\cdots$, with $a_\\nu=\\dfrac{4\\Gamma(\\nu)\\zeta(\\nu)L(\\nu+1,\\chi)}{(2\\pi/\\sqrt{3})^{2\\nu+1}}$, where $\\chi(n)=\\left(\\dfrac{n}{3}\\right)$. In particular, $a_2=\\tfrac{1}{108}$, $a_4=\\tfrac{1}{4320}$, and $a_6=\\tfrac{1}{38880}$. Furthermore, as $x\\to 0^+$, the minimum value of $a_\\nu x^\\nu$ is asymptotic to $\\dfrac{3}{\\pi}\\sqrt{\\dfrac{2x}{\\pi}}\\,e^{-4\\pi^2/(3x)}$."),
    rec("RLN-P1-C07-Entry7-3-2", "As $x\\to 0^+$, $2\\sqrt{x}-e^x+e^{-x}-e^{2x}+e^{-2x}-e^{3x}+e^{-3x}-\\cdots=\\dfrac{\\Gamma(\\tfrac14)}{\\Gamma(\\tfrac34)}\\,e^{G(x)}$, where $G(x)\\sim a_2 x^2+a_4 x^4+a_6 x^6+\\cdots$, with $a_\\nu=\\dfrac{4\\Gamma(\\nu)\\zeta(\\nu)L(\\nu+1,\\chi)}{\\pi^{2\\nu+1}}$, where $\\chi$ is the nonprincipal, primitive character modulo $4$. Furthermore, $a_2=\\tfrac{1}{48}$, $a_4=\\tfrac{1}{1152}$, and $a_6=\\tfrac{1}{362880}$, and, as $x\\to 0^+$, the minimum value of $a_\\nu x^\\nu$ is asymptotic to $\\dfrac{4}{\\pi}\\sqrt{\\dfrac{2x}{\\pi}}\\,e^{-\\pi^2/x}$."),
    rec("RLN-P1-C07-Entry7-4-1", "As $x\\to 0^+$, $R(a,e^{-x})=\\dfrac{-1+\\sqrt{1+4a}}{2a}\\exp\\!\\left(\\dfrac{ax}{1+4a}-\\dfrac{a(1-a)x^2}{2(1+4a)^{5/2}}+\\dfrac{a(1-a)(1-14a)x^3}{6(1+4a)^4}-\\cdots\\right)$. Moreover, each term of the asymptotic expansion beginning with the second has a factor of $a(1-a)$."),
]
