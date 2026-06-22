"""RLN Part 1, Chapter 11 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C11 = ["rogers-ramanujan-slater-type-identities"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C11}


CHAPTER_11 = [
    rec("RLN-P1-C11-Entry11-2-1", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{q^{n^2}}{(q)_{2n}}=\\frac{G(q^4)}{(q;q^2)_\\infty}$, $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{q^{n^2+n}}{(q)_{2n+1}}=\\frac{H(-q)}{(q;q^2)_\\infty}$, $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{q^{n^2+n}}{(q)_{2n}}=\\frac{G(-q)}{(q;q^2)_\\infty}$, and $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{q^{n^2+2n}}{(q)_{2n+1}}=\\frac{H(q^4)}{(q;q^2)_\\infty}$."),
    rec("RLN-P1-C11-Entry11-2-2", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^nq^{3n^2}}{(q^4;q^4)_n(-q;q^2)_n}=\\frac{G(q)}{(-q;q)_\\infty}$, $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^nq^{3n^2-2n}}{(q^4;q^4)_n(-q;q^2)_n}=\\frac{H(q)}{(-q;q)_\\infty}$, and $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^nq^{3n^2+2n}}{(q^4;q^4)_{n+1}(-q;q^2)_n}=\\frac{H(q)}{(-q;q)_\\infty}$."),
    rec("RLN-P1-C11-Entry11-3-1", "If $G_6(q):=(q^3;q^6)_\\infty^2(q^6;q^6)_\\infty=\\sum_{n=-\\infty}^{\\infty}(-1)^nq^{3n^2}=\\varphi(-q^3)$, then $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-q;q^2)_nq^{n^2}}{(q;q)_{2n}}=\\frac{G_6(q^2)}{(q;q)_\\infty}$."),
    rec("RLN-P1-C11-Entry11-3-2", "If $H_6(q):=(q;q^6)_\\infty(q^5;q^6)_\\infty(q^6;q^6)_\\infty=\\sum_{n=-\\infty}^{\\infty}(-1)^nq^{3n^2-2n}=f(-q,-q^5)$ and $\\varphi(q)$ is given by (1.1.6) in Chapter 1, then $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-q^2;q^2)_nq^{n(n+1)}}{(q;q)_{2n+1}}=\\frac{H_6(-q)}{\\varphi(-q^2)}$."),
    rec("RLN-P1-C11-Entry11-3-3", "If $H_6(q)$ is defined by (11.3.2) and $\\varphi(q)$ is given by (1.1.6) in Chapter 1, then $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-q^2;q^2)_nq^n}{(q;q)_{2n+1}}=\\frac{H_6(q^2)}{\\varphi(-q)}$."),
    rec("RLN-P1-C11-Entry11-3-4", "If $H_6(q)$ is defined by (11.3.2) and $\\varphi(q)$ is given by (1.1.6) in Chapter 1, then $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-q;q)_{2n}q^n}{(q;q)_n(-q;q)_n}=\\frac{H_6(q)}{\\varphi(-q)}$."),
    rec("RLN-P1-C11-Entry11-3-5", "If $J_6(q):=(-q;q^3)_\\infty(-q^2;q^3)_\\infty(q^3;q^3)_\\infty=\\sum_{n=-\\infty}^{\\infty}q^{n(3n+1)/2}=f(q,q^2)$ and $\\varphi(q)$ is given by (1.1.6) in Chapter 1, then $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-q;q^2)_nq^n}{(q;q)_{2n}}=\\frac{J_6(-q)}{\\varphi(-q)}$."),
    rec("RLN-P1-C11-Entry11-4-1", "Recall that Ramanujan's general theta function $f(a,b)$ is defined in (1.1.5) of Chapter 1. Then $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{q^{2n(n+1)}}{(-q;q^2)_n(q^4;q^4)_n}=\\frac{f(-q^{5/2},-q)}{(q^2;q^2)_\\infty}$, $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{q^{2n^2}}{(-q;q^2)_n(q^4;q^4)_n}=\\frac{f(-q^2,-q^{3/2})}{(q^2;q^2)_\\infty}$, and $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{q^{2n(n+1)}}{(-q;q^2)_{n+1}(q^4;q^4)_n}=\\frac{f(-q^3,-q^{1/2})}{(q^2;q^2)_\\infty}$."),
    rec("RLN-P1-C11-Entry11-5-1", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n(-q;q^2)_nq^{n(n+1)/2}}{(q^{n+1};q)_{n+1}}=\\sum_{n=0}^{\\infty}(-1)^nq^{4n^2+n}(1+q^{6n+3})$, $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n(-q;q^2)_nq^{n(n+3)/2}}{(q^{n+1};q)_{n+1}}=\\sum_{n=0}^{\\infty}(-1)^nq^{4n^2+3n}(1+q^{2n+1})$, and $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n(q^{4n+6};q^4)_nq^{2n(n+1)}}{(-q;q)_{4n+2}}=\\sum_{n=0}^{\\infty}q^{4n^2+3n}(1-q^{2n+1})$."),
]
