"""RLN Part 1, Chapter 14 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C14 = ["integrals-theta-functions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C14}


CHAPTER_14 = [
    rec("RLN-P1-C14-Entry14-3-1", "For $0<q<1$, $\\displaystyle\\frac{\\varphi(-q^3)}{\\varphi(-q)}=\\exp\\!\\left(2\\int_0^q\\psi^2(t)\\psi^2(t^3)\\,dt\\right)$."),
    rec("RLN-P1-C14-Entry14-3-2", "For $0<q<1$, $\\displaystyle q^{1/4}\\frac{\\psi(-q^3)}{\\psi(-q)}=\\exp\\!\\left(\\frac{1}{4}\\int\\frac{\\varphi^2(t)\\varphi^2(t^3)}{t}\\,dt\\right)$."),
    rec("RLN-P1-C14-Entry14-3-3", "For $0<q<1$, $\\displaystyle\\frac{\\psi(-q)}{\\psi(q)}=\\exp\\!\\left(-2\\int_0^q\\psi^4(t^2)\\,dt\\right)$."),
    rec("RLN-P1-C14-Entry14-3-4", "For $0<q<1$, $\\displaystyle\\frac{\\psi(-q)}{\\psi(q^2)}=q^{1/8}\\exp\\!\\left(-\\frac{1}{8}\\int\\frac{\\varphi^4(t)}{t}\\,dt\\right)$."),
    rec("RLN-P1-C14-Entry14-3-5", "If $0<q<1$ and $\\bigl(\\tfrac{n}{3}\\bigr)$ denotes the Legendre symbol, $\\displaystyle q^{1/9}\\prod_{n=1}^{\\infty}(1-q^n)^{n(n/3)}=\\exp\\!\\left(\\frac{1}{9}\\int\\frac{f^9(-t)}{f^3(-t^3)}\\,\\frac{dt}{t}\\right)$."),
    rec("RLN-P1-C14-Entry14-3-6", "For $0<q<1$, $\\displaystyle q^{1/9}\\prod_{n=1}^{\\infty}(1-q^n)^{n\\chi(n)}=\\exp\\!\\left(-C-\\frac{1}{9}\\int_1^q\\frac{f^9(-t)}{f^3(-t^3)}\\,\\frac{dt}{t}\\right)$, where $C:=\\dfrac{3\\sqrt{3}}{4\\pi}L(2,\\chi)=L'(-1,\\chi)$, $\\chi(n)$ denotes the Legendre symbol $\\bigl(\\tfrac{n}{3}\\bigr)$, and $L(s,\\chi)$ denotes the Dirichlet $L$-function associated with $\\chi$."),
    rec("RLN-P1-C14-Entry14-3-7", "Let $\\omega:=e^{2\\pi i/3}$ and $0<q<1$. Then $\\displaystyle\\prod_{n=1}^{\\infty}\\left(\\frac{1-q^n\\omega}{1-q^n\\omega^2}\\right)^n=\\exp\\!\\left(-(\\omega-\\omega^2)\\int_0^q\\frac{f^9(-t^3)}{f^3(-t)}\\,dt\\right)$."),
    rec("RLN-P1-C14-Entry14-4-1", "$\\displaystyle R(q)=\\frac{\\sqrt{5}-1}{2}\\exp\\!\\left(-\\frac{1}{5}\\int_1^q\\frac{f^5(-t)}{f(-t^5)}\\,\\frac{dt}{t}\\right)$, where $R(q)$ is the Rogers–Ramanujan continued fraction."),
    rec("RLN-P1-C14-Entry14-4-2", "For $0\\leq q<1$, $\\displaystyle R(q)=\\frac{\\sqrt{5}-1}{2}-\\frac{\\sqrt{5}}{1+3+\\frac{\\sqrt{5}}{2}}\\exp\\!\\left(\\frac{1}{\\sqrt{5}}\\int_0^q\\frac{f^5(-t)}{f(-t^{1/5})}\\,\\frac{dt}{t^{4/5}}\\right)$."),
]
