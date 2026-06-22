"""RLN Part 2, Chapter 9 — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C09 = ["ramanujan-cubic-class-invariant"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C09}


CHAPTER_9 = [
    rec(
        "RLN-P2-C09-Entry9-1-1",
        "The cubic class invariant \\lambda_n is defined by "
        "\\lambda_n = \\frac{e^{\\pi/2\\sqrt{n/3}}}{3\\sqrt{3}}"
        "\\left\\{(1+e^{-\\pi\\sqrt{n/3}})(1-e^{-2\\pi\\sqrt{n/3}})"
        "(1-e^{-4\\pi\\sqrt{n/3}})\\cdots\\right\\}^6. "
        "Ramanujan records the following values for n \\equiv 1 \\pmod{8}: "
        "\\lambda_1 = 1; "
        "\\lambda_9 = 3; "
        "\\lambda_{17} = 4 + \\sqrt{17}; "
        "\\lambda_{25} = (2 + \\sqrt{5})^2; "
        "\\lambda_{33} = 18 + 3\\sqrt{33}; "
        "\\lambda_{41} = 32 + 5\\sqrt{41}; "
        "\\lambda_{49} = 55 + 12\\sqrt{21}; "
        "\\lambda_{57} \\text{ (unstated)}; "
        "\\lambda_{65} \\text{ (unstated)}; "
        "\\lambda_{81} \\text{ (unstated)}; "
        "\\lambda_{89} = 500 + 53\\sqrt{89}; "
        "\\lambda_{73} = \\left(\\sqrt{\\frac{11+\\sqrt{73}}{8}}"
        "+ \\sqrt{\\frac{3+\\sqrt{73}}{8}}\\right)^6; "
        "\\lambda_{97} = \\left(\\sqrt{\\frac{17+\\sqrt{97}}{8}}"
        "+ \\sqrt{\\frac{9+\\sqrt{97}}{8}}\\right)^6; "
        "\\lambda_{121} = \\left(\\sqrt{\\frac{3\\sqrt{3}+\\sqrt{11}}{4}}"
        "+ \\sqrt{\\frac{11+3\\sqrt{33}}{8}}\\right)^6; "
        "\\lambda_{169} \\text{ (unstated)}; "
        "\\lambda_{193} \\text{ (unstated)}; "
        "\\lambda_{217} \\text{ (unstated)}; "
        "\\lambda_{241} \\text{ (unstated)}; "
        "\\lambda_{265} \\text{ (unstated)}; "
        "\\lambda_{289} \\text{ (unstated)}; "
        "\\lambda_{361} \\text{ (unstated)}.",
    ),
]
