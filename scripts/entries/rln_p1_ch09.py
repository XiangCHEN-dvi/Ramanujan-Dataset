"""RLN Part 1, Chapter 9 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C09 = ["rogers-fine-identity"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C09}


CHAPTER_9 = [
    rec("RLN-P1-C09-Entry9-2-1", "If $\\varphi(a):=\\displaystyle\\sum_{n=0}^{\\infty}\\frac{a^n q^{n(n+1)/2}}{(bq;q)_n}$, then $\\varphi(a)=(b+aq)\\varphi(aq)+1-b$."),
    rec("RLN-P1-C09-Entry9-2-2", "If $\\varphi(a)$ is defined by Entry 9.2.1, then $\\displaystyle\\varphi(a)=\\sum_{n=0}^{\\infty}\\frac{(-aq/b;q)_n a^n b^n q^{n(3n+1)/2}(1+aq^{2n+1})}{(bq;q)_n}$."),
    rec("RLN-P1-C09-Entry9-2-3", "If $\\varphi(a)$ is defined by Entry 9.2.1, then $\\displaystyle\\varphi(a)=1+\\sum_{n=1}^{\\infty}\\frac{(-aq/b;q)_{n-1}a^n b^{n-1}q^{n(3n-1)/2}(1+aq^{2n})}{(bq;q)_n}$."),
    rec("RLN-P1-C09-Entry9-2-4", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n a^{2n} q^{n^2}}{(a^2q^2;q^2)_n}=(1-a)\\sum_{n=1}^{\\infty}\\frac{a^n q^n}{(-aq;q)_n}$."),
    rec("RLN-P1-C09-Entry9-2-5", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n a^n q^n}{(aq;q^2)_{n+1}}=\\sum_{n=0}^{\\infty}\\frac{(-1)^n a^{2n} q^{2n^2+2n}}{(a^2q^2;q^4)_{n+1}}$."),
    rec("RLN-P1-C09-Entry9-2-6", "$\\displaystyle aq(-aq;q^2)_{\\infty}\\sum_{n=0}^{\\infty}\\frac{(-1)^n a^n q^{n(n+1)/2}}{(-a;q)_{n+1}}=\\sum_{n=0}^{\\infty}\\frac{a^{n+1}q^{(n+1)^2}}{(q^2;q^2)_n(1+aq^{2n})}$."),
    rec("RLN-P1-C09-Entry9-3-1", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-aq;q^2)_n(-aq)_n}{(-aq^2;q^2)_n}=\\sum_{n=0}^{\\infty}(-a)^n q^{n(n+1)/2}$."),
    rec("RLN-P1-C09-Entry9-3-2", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n q^{n^2+n}(q;q^2)_n}{(-q;q)_{2n+1}}=\\sum_{n=0}^{\\infty}(-1)^n q^{n(n+1)/2}$."),
    rec("RLN-P1-C09-Entry9-3-3", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(q;q^2)_n q^n}{(-q;q^2)_{n+1}}=\\sum_{n=0}^{\\infty}(-1)^n q^{2n(n+1)}$."),
    rec("RLN-P1-C09-Entry9-3-4", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(q;q^2)_n^2 q^n}{(-q;q)_{2n+1}}=\\sum_{n=0}^{\\infty}(-1)^n q^{n^2+n}$."),
    rec("RLN-P1-C09-Entry9-3-5", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-aq^{n+1};q)_n q^n}{(q;q)_n}=(q;q)_{\\infty}\\sum_{n=0}^{\\infty}a^n q^{3n(n+1)/2}$."),
    rec("RLN-P1-C09-Entry9-3-6", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(q;q^2)_n q^n}{(-q;q)_{2n+1}}=\\sum_{n=0}^{\\infty}(-1)^n q^{3n(n+1)/2}$."),
    rec("RLN-P1-C09-Entry9-3-7", "With $q$ replaced by $-q$ in Ramanujan's formulation, $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n(-q;q)_n q^n}{(q;q^2)_{n+1}}=\\sum_{n=0}^{\\infty}(-1)^n q^{3n(n+1)}$."),
    rec("RLN-P1-C09-Entry9-4-2", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n q^{n(n+1)/2}}{(-q;q)_n}=\\sum_{n=0}^{\\infty}q^{n(3n+1)/2}(1-q^{2n+1})$."),
    rec("RLN-P1-C09-Entry9-4-1", "For any complex number $a$, $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n a^{2n} q^{n(n+1)/2}}{(-aq;q)_n}=\\sum_{n=0}^{\\infty}a^{3n}q^{n(3n+1)/2}(1-a^2q^{2n+1})$."),
    rec("RLN-P1-C09-Entry9-4-3", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{q^{n(2n+1)}}{(-q;q)_{2n+1}}=\\sum_{n=0}^{\\infty}q^{n(3n+1)/2}(1-q^{2n+1})$."),
    rec("RLN-P1-C09-Entry9-4-4", "$\\displaystyle 2-\\sum_{n=0}^{\\infty}\\frac{q^{n(2n-1)}}{(-q;q)_{2n}}=\\sum_{n=0}^{\\infty}q^{n(3n+1)/2}(1-q^{2n+1})$."),
    rec("RLN-P1-C09-Entry9-4-5", "If $g(a):=\\displaystyle\\sum_{n=0}^{\\infty}a^{3n}q^{n(3n+1)/2}(1-a^2q^{2n+1})$, then $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n a^{4n+3}q^{2(n+1)^2}}{(-a^2q^3;q^4)_{n+1}}=\\tfrac12(g(a)-g(-a))$."),
    rec("RLN-P1-C09-Entry9-4-6", "If $g(a)$ is defined by Entry 9.4.5, then $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n a^{4n}q^{2n^2}}{(-a^2q;q^4)_{n+1}}=\\tfrac12(g(a)+g(-a))$."),
    rec("RLN-P1-C09-Entry9-4-7", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n q^n}{(-q^2;q^2)_n}=\\sum_{n=0}^{\\infty}q^{n(3n+1)/2}(1-q^{2n+1})$."),
    rec("RLN-P1-C09-Entry9-4-8", "$\\displaystyle 1+2\\sum_{n=1}^{\\infty}\\frac{q^{n^2+2n}}{(q^2;q^2)_{n-1}(1-q^{4n})}=(-q;q^2)_{\\infty}\\sum_{n=0}^{\\infty}q^{n(3n+1)/2}(1-q^{2n+1})$."),
    rec("RLN-P1-C09-Entry9-4-9", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(q;q^2)_n q^n}{(-q;q)_{2n}}=\\sum_{n=0}^{\\infty}(-1)^n q^{n(3n+1)/2}(1+q^{2n+1})$."),
    rec("RLN-P1-C09-Entry9-5-1", "For any complex number $a$, $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n a^{2n} q^{n(n+1)}}{(-aq;q^2)_{n+1}}=\\sum_{n=0}^{\\infty}a^{3n}q^{3n^2+2n}(1-aq^{2n+1})$."),
    rec("RLN-P1-C09-Entry9-5-2", "$\\displaystyle\\sum_{n=0}^{\\infty}(q;q^2)_n q^n=\\sum_{n=0}^{\\infty}(-1)^n q^{3n^2+2n}(1+q^{2n+1})$."),
    rec("RLN-P1-C09-Entry9-5-3", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{q^n}{(-q;q^2)_{n+1}}=\\sum_{n=0}^{\\infty}(-1)^n q^{6n^2+4n}(1+q^{4n+2})$."),
    rec("RLN-P1-C09-Entry9-5-4", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n q^n}{(q;q^2)_{n+1}}=\\sum_{n=0}^{\\infty}(-1)^n q^{6n^2+4n}(1+q^{4n+2})$."),
    rec("RLN-P1-C09-Entry9-5-5", "$\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-q^2)^{n(n+1)/2}}{(-q;-q^2)_n}=\\sum_{n=0}^{\\infty}(-1)^{n(n+1)/2}q^{3n^2+2n}\\left(1-(-1)^n q^{2n+1}\\right)$."),
]
