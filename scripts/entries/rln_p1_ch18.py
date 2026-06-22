"""RLN Part 1, Chapter 18 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C18 = ["fragments-lambert-series"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C18}


CHAPTER_18 = [
    rec("RLN-P1-C18-Entry18-2-1", "$\\displaystyle\\varphi^4(q)=1+8\\sum_{n=1}^{\\infty}\\frac{nq^n}{1+(-q)^n}$."),
    rec("RLN-P1-C18-Entry18-2-2", "$\\displaystyle\\varphi^6(q)=1-4\\sum_{n=0}^{\\infty}\\frac{(-1)^n(2n+1)^2 q^{2n+1}}{1-q^{2n+1}}+16\\sum_{n=1}^{\\infty}\\frac{n^2 q^n}{1+q^{2n}}$."),
    rec("RLN-P1-C18-Entry18-2-3", "$\\displaystyle\\varphi^8(q)=1+16\\sum_{n=1}^{\\infty}\\frac{n^3 q^n}{1-(-q)^n}$."),
    rec("RLN-P1-C18-Entry18-2-4", "$\\displaystyle\\psi^2(q^4)=\\sum_{n=0}^{\\infty}\\frac{(-1)^n q^{2n}}{1-q^{4n+2}}$."),
    rec("RLN-P1-C18-Entry18-2-5", "$\\displaystyle q\\psi^4(q^2)=\\sum_{n=0}^{\\infty}\\frac{(2n+1)q^{2n+1}}{1-q^{4n+2}}$."),
    rec("RLN-P1-C18-Entry18-2-6", "$\\displaystyle q^{3/2}\\psi^6(q^2)=\\frac{1}{16}\\sum_{n=0}^{\\infty}\\frac{(2n+1)^2 q^{(2n+1)/2}}{1+q^{2n+1}}-\\frac{1}{16}\\sum_{n=0}^{\\infty}\\frac{(-1)^n(2n+1)^2 q^{(2n+1)/2}}{1-q^{2n+1}}$."),
    rec("RLN-P1-C18-Entry18-2-7", "$\\displaystyle q\\psi^8(q)=\\sum_{n=1}^{\\infty}\\frac{n^3 q^n}{1-q^{2n}}$."),
    rec("RLN-P1-C18-Entry18-2-8", "If $\\left(\\frac{n}{p}\\right)$ denotes the Legendre symbol, then $\\displaystyle a(q)=1+6\\sum_{n=1}^{\\infty}\\frac{\\left(\\frac{n}{p}\\right)q^n}{1-q^n}$."),
    rec("RLN-P1-C18-Entry18-2-9", "If $\\chi_0$ denotes the principal character modulo $3$, then $\\displaystyle a^2(q)=1+12\\sum_{n=1}^{\\infty}\\frac{\\chi_0(n)\\,n q^n}{1-q^n}$."),
    rec("RLN-P1-C18-Entry18-2-10", "If $\\left(\\frac{n}{p}\\right)$ denotes the Legendre symbol, then $\\displaystyle a^3(q)=1-9\\sum_{n=1}^{\\infty}\\frac{\\left(\\frac{n}{p}\\right)n^2 q^n}{1-q^n}+27\\sum_{n=1}^{\\infty}\\frac{n^2 q^n}{1+q^n+q^{2n}}$."),
    rec("RLN-P1-C18-Entry18-2-11", "$\\displaystyle a^4(q)=1+24\\sum_{n=1}^{\\infty}\\frac{n^3 q^n}{1-q^n}+8\\sum_{n=1}^{\\infty}\\frac{(3n)^3 q^{3n}}{1-q^{3n}}$."),
    rec("RLN-P1-C18-Entry18-2-12", "If $\\left(\\frac{n}{p}\\right)$ denotes the Legendre symbol, then $\\displaystyle\\varphi(q)\\varphi(q^7)=1+2\\sum_{n=1}^{\\infty}\\frac{\\left(\\frac{n}{p}\\right)q^n}{1-(-q)^n}$."),
    rec("RLN-P1-C18-Entry18-2-13", "If $\\left(\\frac{n}{p}\\right)$ denotes the Legendre symbol, then $\\displaystyle q\\psi(q)\\psi(q^7)=\\sum_{n=1}^{\\infty}\\frac{(2n-1)q^{2n-1}}{1-q^{2n-1}}$."),
    rec("RLN-P1-C18-Entry18-2-14", "If $\\left(\\frac{n}{p}\\right)$ denotes the Legendre symbol, then $\\displaystyle T(q)=1+2\\sum_{n=1}^{\\infty}\\frac{\\left(\\frac{n}{p}\\right)q^n}{1-q^n}$."),
    rec("RLN-P1-C18-Entry18-2-15", "If $T(q)$ is defined by Entry 18.2.14 and if $\\chi_0(n)$ denotes the principal character modulo $7$, then $\\displaystyle T^2(q)=1+4\\sum_{n=1}^{\\infty}\\frac{\\chi_0(n)\\,n q^n}{1-q^n}$."),
    rec("RLN-P1-C18-Entry18-2-16", "If $\\left(\\frac{n}{p}\\right)$ denotes the Legendre symbol, then $\\displaystyle\\frac{\\varphi^3(-q)}{\\varphi(-q^3)}=1-6\\sum_{n=1}^{\\infty}\\frac{\\left(\\frac{n}{p}\\right)q^n}{1+q^n}$."),
    rec("RLN-P1-C18-Entry18-2-17", "If $\\left(\\frac{n}{p}\\right)$ denotes the Legendre symbol, then $\\displaystyle\\frac{\\varphi^3(q^3)}{\\varphi(q)}=1-2\\sum_{n=1}^{\\infty}\\frac{\\left(\\frac{n}{p}\\right)q^n}{1-(-q)^n}$."),
    rec("RLN-P1-C18-Entry18-2-18", "$\\displaystyle\\frac{\\psi^3(q)}{\\psi(q^3)}=1+3\\sum_{n=0}^{\\infty}\\left(\\frac{q^{6n+1}}{1-q^{6n+1}}-\\frac{q^{6n+5}}{1-q^{6n+5}}\\right)$."),
    rec("RLN-P1-C18-Entry18-2-19", "If $\\left(\\frac{n}{p}\\right)$ denotes the Legendre symbol, then $\\displaystyle\\frac{q\\psi^3(q^3)}{\\psi(q)}=\\sum_{n=1}^{\\infty}\\frac{\\left(\\frac{n}{p}\\right)q^n}{1-q^{2n}}$."),
    rec("RLN-P1-C18-Entry18-2-20", "If $\\left(\\frac{n}{p}\\right)$ denotes the Legendre symbol, then $\\displaystyle\\frac{f^3(-q)}{f(-q^3)}=1-3\\sum_{n=1}^{\\infty}\\frac{\\left(\\frac{n}{p}\\right)q^n}{1-q^n}+9\\sum_{n=1}^{\\infty}\\frac{\\left(\\frac{n}{p}\\right)q^{3n}}{1-q^{3n}}$."),
    rec("RLN-P1-C18-Entry18-2-21", "If $\\left(\\frac{n}{p}\\right)$ denotes the Legendre symbol, then $\\displaystyle\\frac{qf^3(-q^9)}{f(-q^3)}=\\sum_{n=1}^{\\infty}\\frac{\\left(\\frac{n}{p}\\right)q^n}{1-q^n}-\\sum_{n=1}^{\\infty}\\frac{\\left(\\frac{n}{p}\\right)q^{3n}}{1-q^{3n}}$."),
    rec("RLN-P1-C18-Entry18-2-22", "If $\\left(\\frac{n}{p}\\right)$ denotes the Legendre symbol, then $\\displaystyle\\frac{f^5(-q)}{f(-q^5)}=1-5\\sum_{n=1}^{\\infty}\\frac{\\left(\\frac{n}{p}\\right)n q^n}{1-q^n}$."),
    rec("RLN-P1-C18-Entry18-2-23", "If $\\left(\\frac{n}{p}\\right)$ denotes the Legendre symbol, then $\\displaystyle\\frac{q f^5(-q^5)}{f(-q)}=\\sum_{n=1}^{\\infty}\\frac{\\left(\\frac{n}{p}\\right)q^n}{(1-q^n)^2}$."),
    rec("RLN-P1-C18-Entry18-2-24", "If $\\left(\\frac{n}{p}\\right)$ denotes the Legendre symbol, then $\\displaystyle\\varphi(q)\\varphi(q^3)=1+2\\sum_{n=1}^{\\infty}\\frac{\\left(\\frac{n}{p}\\right)q^n}{1+(-q)^n}$."),
    rec("RLN-P1-C18-Entry18-2-25", "If $\\chi_0(n)$ denotes the principal character modulo $3$, then $\\displaystyle\\varphi^2(q)\\varphi^2(q^3)=1+4\\sum_{n=1}^{\\infty}\\frac{\\chi_0(n)\\,n q^n}{1-(-q)^n}$."),
]
