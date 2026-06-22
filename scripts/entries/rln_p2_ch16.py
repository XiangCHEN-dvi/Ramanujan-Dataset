"""RLN Part 2, Chapter 16 — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C16 = ["miscellaneous-eisenstein-series"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C16}


CHAPTER_16 = [
    rec(
        "RLN-P2-C16-Entry16-1-1",
        "Ramanujan records the series "
        "\\frac{1^r}{e^{sx} - 1} + \\frac{2^r}{e^{2sx} - 1} "
        "+ \\frac{3^r}{e^{3sx} - 1} + \\cdots, "
        "where s is a positive integer and r - s is any even integer. "
        "With q = e^{-x}, this is equivalent to "
        "\\sum_{k=0}^{\\infty} \\frac{k^r q^{ks}}{1 - q^{ks}}.",
    ),
    rec(
        "RLN-P2-C16-Entry16-2-1",
        "Let z := 2K/\\pi, where K is the complete elliptic integral of the first "
        "kind, \\alpha = k^2 with 0 < k < 1 the modulus, and k' = \\sqrt{1-k^2} "
        "the complementary modulus. Then "
        "Q(q) = \\left(\\frac{2K}{\\pi}\\right)^4 \\left(1 + 14k^2 + k^4\\right), "
        "Q(q^4) = \\left(\\frac{K}{\\pi}\\right)^4 \\left(1 + 14k'^2 + k'^4\\right), "
        "Q(q^2) = \\left(\\frac{2K}{\\pi}\\right)^4 \\left(1 - (kk')^2\\right), "
        "R(q) = \\left(\\frac{2K}{\\pi}\\right)^6 (1 + k^2)(1 - 34k^2 + k^4), "
        "R(q^4) = \\left(\\frac{K}{\\pi}\\right)^6 (1 + k'^2)"
        "\\left(1 - 34k'^2 + k'^4\\right), "
        "and R(q^2) = \\left(\\frac{2K}{\\pi}\\right)^6 (k'^2 - k^2)"
        "\\left(1 + \\frac{1}{2}(kk')^2\\right).",
    ),
    rec(
        "RLN-P2-C16-Entry16-3-1",
        "Define the function S_s by "
        "\\sum_{k=1}^{\\infty} \\frac{k^{1-s}}{e^{2k\\pi} - 1} "
        "= S_s - \\frac{1}{2}\\zeta(s-1) + \\frac{3}{4\\pi}\\zeta(s) "
        "+ \\frac{\\pi}{12}\\zeta(s-2), "
        "where \\zeta denotes the Riemann zeta function. Then, if n is a positive "
        "integer, S_{4n} = 0, S_0 = \\frac{1}{4\\pi}, S_4 = -\\frac{\\pi^3}{360}, "
        "S_8 = 0, S_{12} = -\\frac{\\pi^{11}}{232186500}, "
        "S_{16} = \\frac{\\pi^{15}}{21470872500}, "
        "S_{20} = \\frac{191\\pi^{19}}{398240480137500}, "
        "and S_{24} = \\frac{907\\pi^{23}}{184177171143590625}.",
    ),
    rec(
        "RLN-P2-C16-Entry16-4-1",
        "If s is a positive integer and B_n denotes the nth Bernoulli number, then "
        "(2s-1)\\frac{B_s}{2s} + \\sum_{k=1}^{\\infty} \\frac{k^{s-1}q^k}{1 + (-q)^k} "
        "= 2^s\\left(\\frac{B_s}{2s} - \\sum_{k=1}^{\\infty} "
        "\\frac{k^{s-1}q^{4k}}{1 - q^{4k}}\\right) "
        "- \\left(\\frac{B_s}{2s} - \\sum_{k=1}^{\\infty} "
        "\\frac{k^{s-1}q^k}{1 - q^k}\\right) "
        "and (2s-1)\\frac{B_s}{2s} + \\sum_{k=1}^{\\infty} "
        "\\frac{k^{s-1}q^k}{1 + (-q)^k} "
        "= 2^s\\left(\\frac{B_s}{2s} + \\sum_{k=1}^{\\infty} "
        "\\frac{k^{s-1}q^{4k}}{1 - q^{4k}}\\right) "
        "+ \\left(\\frac{B_s}{2s} + \\sum_{k=1}^{\\infty} "
        "\\frac{k^{s-1}q^k}{1 - q^k}\\right) "
        "- 2\\left(\\frac{B_s}{2s} + \\sum_{k=1}^{\\infty} "
        "\\frac{k^{s-1}q^{2k}}{1 - q^{2k}}\\right).",
    ),
]
