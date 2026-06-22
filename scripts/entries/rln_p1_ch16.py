"""RLN Part 1, Chapter 16 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C16 = ["infinite-integrals-q-products"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C16}


CHAPTER_16 = [
    rec("RLN-P1-C16-Entry16-1-1", "If $|a|<1$ and $m$ and $k$ are real numbers, then $\\displaystyle\\int_{-\\infty}^{\\infty} e^{-x^2+2mx}(-aqe^{2kx};q)_{\\infty}\\,dx=\\sqrt{\\pi}\\sum_{n=0}^{\\infty}\\frac{e^{(m+nk)^2}a^n q^{n(n+1)/2}}{(q;q)_n}$."),
    rec("RLN-P1-C16-Entry16-1-2", "If $|a|<1$ and $m$ and $k$ are real numbers, then $\\displaystyle\\int_{-\\infty}^{\\infty} e^{-x^2+2mx}(-ae^{-k^2+2kx};e^{-2k^2})_{\\infty}\\,dx=\\sqrt{\\pi}\\,e^{m^2}(ae^{2mk};e^{-2k^2})_{\\infty}$."),
    rec("RLN-P1-C16-Entry16-1-3", "If $|a|<1$ and $m$ and $k$ are real numbers, then $\\displaystyle\\int_{-\\infty}^{\\infty}\\frac{e^{-x^2+2mx}\\,dx}{(ae^{2ikx};e^{-2k^2})_{\\infty}}=\\sqrt{\\pi}\\,e^{m^2}(-ae^{-k^2+2imk};e^{-2k^2})_{\\infty}$."),
    rec("RLN-P1-C16-Entry16-1-4", "If $|a|,|b|<1$ and $m$ and $k$ are real numbers, then $\\displaystyle\\int_{-\\infty}^{\\infty} e^{-x^2+2mx}(-ae^{-2k^2+2kx};e^{-2k^2})_{\\infty}(-be^{-2k^2-2kx};e^{-2k^2})_{\\infty}\\,dx=\\frac{\\sqrt{\\pi}\\,e^{m^2}(abe^{-2k^2};e^{-2k^2})_{\\infty}}{(ae^{-k^2+2mk};e^{-2k^2})_{\\infty}(be^{-k^2-2mk};e^{-2k^2})_{\\infty}}$."),
    rec("RLN-P1-C16-Entry16-1-5", "If $|a|,|b|<1$ and $m$ and $k$ are real numbers, then $\\displaystyle\\int_{-\\infty}^{\\infty}\\frac{e^{-x^2+2mx}\\,dx}{(ae^{-k^2+2ikx};e^{-2k^2})_{\\infty}(be^{-k^2-2ikx};e^{-2k^2})_{\\infty}}=\\frac{\\sqrt{\\pi}\\,e^{m^2}(-ae^{-2k^2+2imk};e^{-2k^2})_{\\infty}(-be^{-2k^2-2imk};e^{-2k^2})_{\\infty}}{(abe^{-2k^2};e^{-2k^2})_{\\infty}}$."),
]
