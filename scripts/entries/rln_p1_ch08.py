"""RLN Part 1, Chapter 8 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C08 = ["continued-fraction-q2-q3-over-q-q3"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C08}


CHAPTER_8 = [
    rec("RLN-P1-C08-Entry8-2-1", "Let $\\omega=e^{2\\pi i/3}$. Then $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-\\omega)^n q^{n(n+1)/2}(\\omega q;q)_n}{(q^3;q^3)_n}=(\\omega q)_{\\infty}(q^2;q^3)_{\\infty}$."),
    rec("RLN-P1-C08-Entry8-2-2", "Let $N-1=3v+\\epsilon$, where $\\epsilon=0$ or $\\pm 1$. Then $\\displaystyle\\lim_{N\\to\\infty}\\cfrac{1}{1-\\cfrac{1}{1+q}-\\cfrac{1}{1+q^2}-\\cdots-\\cfrac{1}{1+q^{N-1}+a}}=-\\dfrac{\\omega^2}{\\Omega-\\omega^{\\epsilon+1}}\\dfrac{\\Omega-\\omega^{\\epsilon-1}}{(q^2;q^3)_{\\infty}(q;q^3)_{\\infty}}$, where $\\Omega=\\dfrac{1-a\\omega^2}{1-a\\omega}\\dfrac{(\\omega^2 q)_{\\infty}}{(\\omega q)_{\\infty}}$."),
    rec("RLN-P1-C08-Entry8-3-1", "For a cube root of unity $\\omega$, $\\displaystyle\\lim_{n\\to\\infty}\\cfrac{1}{1-\\cfrac{1}{1+q}-\\cfrac{1}{1+q^2}-\\cdots-\\cfrac{1}{1+q^n+\\omega}}=-\\dfrac{\\omega\\,(q^2;q^3)_{\\infty}}{(q;q^3)_{\\infty}}$."),
    rec("RLN-P1-C08-Entry8-4-1", "Let $\\omega$ be a cube root of unity. Then $-\\omega^2+\\omega\\,\\dfrac{(q;q^3)_{\\infty}}{(q^2;q^3)_{\\infty}}=\\cfrac{1}{1-\\cfrac{\\omega q}{1-\\omega^2 q}-\\cfrac{\\omega q^2}{1-\\omega^2 q^2}-\\cfrac{\\omega q^3}{1-\\omega^2 q^3}-\\cdots}}$=\\cfrac{1+\\omega}{1+q^{-1}-\\cfrac{1}{1+q^{-2}-\\cfrac{1}{1+q^{-3}-\\cdots}}}$."),
    rec("RLN-P1-C08-Entry8-5-1", "Let $u_\\lambda:=\\cfrac{1}{1+e^{(\\lambda+1)x}-\\cfrac{1}{1+e^{(\\lambda+2)x}-\\cdots}}$. Then, as $x\\to 0$, $u_\\lambda+\\dfrac{1}{u_{\\lambda-1}}=1+e^{\\lambda x}$ and $u_\\lambda=1-\\dfrac{\\varphi_0}{1-\\lambda\\varphi_0}+x\\left(\\dfrac{\\lambda+1}{2}+\\varphi_1+\\dfrac{(\\lambda^2-1)\\left(\\tfrac12-\\tfrac{2}{3\\lambda}\\varphi_0+\\tfrac14\\lambda^2\\varphi_0^2\\right)}{(1-\\lambda\\varphi_0)^2}\\right)+x^2\\left(\\lambda(\\lambda+1)(\\lambda+2)-\\varphi_2+\\cdots\\right)+\\cdots$, where $\\varphi_0,\\varphi_1,\\varphi_2,\\ldots$ are independent of $\\lambda$."),
]
