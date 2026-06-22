"""RLN Part 2, Chapter 12 — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C12 = ["letters-from-matlock-house"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C12}


CHAPTER_12 = [
    rec(
        "RLN-P2-C12-Entry12-1-1",
        "Let 1/R(q^2) = \\sum_{n=0}^{\\infty}\\gamma_n q^{2n}. Then "
        "\\gamma_n = \\frac{2}{C}\\sum_{(\\mu)}\\frac{W_{\\mu}(n)}{\\mu^4}"
        "e^{2n\\pi/\\mu}, where C is as in Entry 11.5.1, \\mu runs over integers "
        "of the form (11.4.4), and W_{\\mu}(n) is as in Entry 11.5.1. Distinct "
        "solutions (c,d) to \\mu=c^2+d^2 give distinct terms in the sum.",
    ),
    rec(
        "RLN-P2-C12-Entry12-2-1",
        "Define \\ell(n) = \\left\\lfloor\\frac{3}{4}n(1-\\epsilon)\\log^{3/2}n"
        "\\prod_{p\\equiv 1\\,(4)}\\left(1-\\frac{1}{p^2}\\right)\\right\\rfloor, "
        "where 0\\le\\epsilon\\le 1 and p runs over primes \\equiv 1\\pmod{4}. "
        "Let \\Sigma_n denote the sum on the right of Entry 12.1.1, and "
        "\\Sigma_n^{(\\ell(n))} the sum of its first \\ell(n) terms (counting all "
        "summands for one value of \\mu as one term). "
        "As n\\to\\infty, there are terms in \\Sigma_n not in \\Sigma_n^{(\\ell(n))} "
        "that are arbitrarily large.",
    ),
    rec(
        "RLN-P2-C12-Entry12-3-1",
        "With the notation of Entry 12.2.1, let u(n) be defined analogously to "
        "\\ell(n) and let \\Sigma_n^{(u(n))} denote the corresponding partial sum. "
        "For n sufficiently large, the coefficient \\gamma_n of Entry 12.1.1 is the "
        "nearest integer to \\Sigma_n^{(u(n))}.",
    ),
]
