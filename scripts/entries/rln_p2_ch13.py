"""RLN Part 2, Chapter 13 — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C13 = ["eisenstein-series-modular-equations"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C13}


CHAPTER_13 = [
    rec(
        "RLN-P2-C13-Entry13-3-1",
        "For Q(q) and f(-q) defined by (13.1.2) and (13.2.1), respectively, "
        "Q(q) = \\frac{f^{10}(-q)}{f^2(-q^5)} + 250q f^4(-q)f^4(-q^5) "
        "+ 3125q^2 \\frac{f^{10}(-q^5)}{f^2(-q)} "
        "and Q(q^5) = \\frac{f^{10}(-q)}{f^2(-q^5)} + 10q f^4(-q)f^4(-q^5) "
        "+ 5q^2 \\frac{f^{10}(-q^5)}{f^2(-q)}.",
    ),
    rec(
        "RLN-P2-C13-Entry13-3-2",
        "For f(-q) and R(q) defined by (13.2.1) and (13.1.3), respectively, "
        "R(q) = \\left(\\frac{f^{15}(-q)}{f^3(-q^5)} - 500q f^9(-q)f^3(-q^5) "
        "- 15625q^2 f^3(-q)f^9(-q^5)\\right) "
        "\\sqrt{1 + 22q \\frac{f^6(-q^5)}{f^6(-q)} "
        "+ 125q^2 \\frac{f^{12}(-q^5)}{f^{12}(-q)}} "
        "and R(q^5) = \\left(\\frac{f^{15}(-q)}{f^3(-q^5)} + 4q f^9(-q)f^3(-q^5) "
        "- q^2 f^3(-q)f^9(-q^5)\\right) "
        "\\sqrt{1 + 22q \\frac{f^6(-q^5)}{f^6(-q)} "
        "+ 125q^2 \\frac{f^{12}(-q^5)}{f^{12}(-q)}}.",
    ),
    rec(
        "RLN-P2-C13-Entry13-3-3",
        "Let A = Q(q) and B = Q(q^5). Then "
        "\\sqrt{A^2 + 94AB + 625B^2} = 12\\sqrt{5} "
        "\\left(\\frac{f^{10}(-q)}{f^2(-q^5)} + 26q f^4(-q)f^4(-q^5) "
        "+ 125q^2 \\frac{f^{10}(-q^5)}{f^2(-q)}\\right).",
    ),
    rec(
        "RLN-P2-C13-Entry13-3-4",
        "Let A = R(q) and B = R(q^5). Then "
        "\\sqrt{5(A + 125B)^2 - 126^2 AB} = 252\\sqrt{5} "
        "\\left(\\frac{f^{10}(-q)}{f^2(-q^5)} + 62q f^4(-q)f^4(-q^5) "
        "+ 125q^2 \\frac{f^{10}(-q^5)}{f^2(-q)}\\right) "
        "\\sqrt{\\frac{f^{10}(-q)}{f^2(-q^5)} + 22q f^4(-q)f^4(-q^5) "
        "+ 125q^2 \\frac{f^{10}(-q^5)}{f^2(-q)}}.",
    ),
    rec(
        "RLN-P2-C13-Entry13-3-5",
        "Let P(q) be defined by (13.1.1). Then "
        "P(q) = \\frac{f^5(-q)}{f(-q^5)} "
        "\\left(1 + 22\\lambda + 125\\lambda^2 - 30F(\\lambda)\\right) "
        "and P(q^5) = \\frac{f^5(-q)}{f(-q^5)} "
        "\\left(1 + 22\\lambda + 125\\lambda^2 - 6F(\\lambda)\\right), "
        "where \\lambda = q \\left(\\frac{f(-q^5)}{f(-q)}\\right)^6 "
        "and F(\\lambda) satisfies the nonlinear first-order differential equation "
        "1 + \\frac{25}{2}\\lambda + \\frac{5}{2}\\lambda F^2(\\lambda) "
        "= F'(\\lambda)\\left(1 + 22\\lambda + 125\\lambda^2\\right).",
    ),
    rec(
        "RLN-P2-C13-Entry13-5-1",
        "For |q| < 1, "
        "Q(q) = \\left(\\frac{f^7(-q)}{f(-q^7)} + 5 \\cdot 7^2 q f^3(-q)f^3(-q^7) "
        "+ 7^4 q^2 \\frac{f^7(-q^7)}{f(-q)}\\right) "
        "\\left(\\frac{f^7(-q)}{f(-q^7)} + 13q f^3(-q)f^3(-q^7) "
        "+ 49q^2 \\frac{f^7(-q^7)}{f(-q)}\\right)^{1/3} "
        "and Q(q^7) = \\left(\\frac{f^7(-q)}{f(-q^7)} + 5q f^3(-q)f^3(-q^7) "
        "+ q^2 \\frac{f^7(-q^7)}{f(-q)}\\right) "
        "\\left(\\frac{f^7(-q)}{f(-q^7)} + 13q f^3(-q)f^3(-q^7) "
        "+ 49q^2 \\frac{f^7(-q^7)}{f(-q)}\\right)^{1/3}.",
    ),
    rec(
        "RLN-P2-C13-Entry13-5-2",
        "For |q| < 1, "
        "R(q) = \\left(\\frac{f^7(-q)}{f(-q^7)} - 7^2(5 + 2\\sqrt{7})q f^3(-q)f^3(-q^7) "
        "- 7^3(21 + 8\\sqrt{7})q^2 \\frac{f^7(-q^7)}{f(-q)}\\right) "
        "\\left(\\frac{f^7(-q)}{f(-q^7)} - 7^2(5 - 2\\sqrt{7})q f^3(-q)f^3(-q^7) "
        "- 7^3(21 - 8\\sqrt{7})q^2 \\frac{f^7(-q^7)}{f(-q)}\\right) "
        "and R(q^7) = \\left(\\frac{f^7(-q)}{f(-q^7)} + (7 + 2\\sqrt{7})q f^3(-q)f^3(-q^7) "
        "+ (21 + 8\\sqrt{7})q^2 \\frac{f^7(-q^7)}{f(-q)}\\right) "
        "\\left(\\frac{f^7(-q)}{f(-q^7)} + (7 - 2\\sqrt{7})q f^3(-q)f^3(-q^7) "
        "+ (21 - 8\\sqrt{7})q^2 \\frac{f^7(-q^7)}{f(-q)}\\right).",
    ),
]
