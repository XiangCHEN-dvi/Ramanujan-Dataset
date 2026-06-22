"""RLN Part 2, Chapter 15 — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C15 = ["eisenstein-series-approximations-pi"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C15}


CHAPTER_15 = [
    rec(
        "RLN-P2-C15-Entry15-2-1",
        "539Q_{11}^3 - 512R_{11}^2 = 0, "
        "(8^3 + 1)Q_{19}^3 - 8^3 R_{19}^2 = 0, "
        "(40^3 + 9)Q_{27}^3 - 40^3 R_{27}^2 = 0, "
        "(80^3 + 1)Q_{43}^3 - 80^3 R_{43}^2 = 0, "
        "(440^3 + 1)Q_{67}^3 - 440^3 R_{67}^2 = 0, "
        "(53360^3 + 1)Q_{163}^3 - 53360^3 R_{163}^2 = 0, "
        "((60 + 28\\sqrt{5})^3 + 27)Q_{35}^3 - (60 + 28\\sqrt{5})^3 R_{35}^2 = 0, "
        "and ((4(4 + \\sqrt{17})^{2/3}(5 + \\sqrt{17}))^3 + 1)Q_{51}^3 "
        "- (4(4 + \\sqrt{17})^{2/3}(5 + \\sqrt{17}))^3 R_{51}^2 = 0.",
    ),
    rec(
        "RLN-P2-C15-Entry15-3-1",
        "\\frac{1}{\\sqrt{Q_{11}}}\\left(\\sqrt{11}P_{11} - \\frac{6}{\\pi}\\right) "
        "= \\sqrt{2}, "
        "\\frac{1}{\\sqrt{Q_{19}}}\\left(\\sqrt{19}P_{19} - \\frac{6}{\\pi}\\right) "
        "= \\sqrt{6}, "
        "\\frac{1}{\\sqrt{Q_{27}}}\\left(\\sqrt{27}P_{27} - \\frac{6}{\\pi}\\right) "
        "= 3\\sqrt{\\frac{6}{5}}, "
        "\\frac{1}{\\sqrt{Q_{43}}}\\left(\\sqrt{43}P_{43} - \\frac{6}{\\pi}\\right) "
        "= 6\\sqrt{\\frac{3}{5}}, "
        "\\frac{1}{\\sqrt{Q_{67}}}\\left(\\sqrt{67}P_{67} - \\frac{6}{\\pi}\\right) "
        "= 19\\sqrt{\\frac{6}{55}}, "
        "\\frac{1}{\\sqrt{Q_{163}}}\\left(\\sqrt{163}P_{163} - \\frac{6}{\\pi}\\right) "
        "= 362\\sqrt{\\frac{3}{3335}}, "
        "\\frac{1}{\\sqrt{Q_{35}}}\\left(\\sqrt{35}P_{35} - \\frac{6}{\\pi}\\right) "
        "= (2 + \\sqrt{5})\\sqrt{2\\sqrt{5}}, "
        "and \\frac{1}{\\sqrt{Q_{51}}}\\left(\\sqrt{51}P_{51} - \\frac{6}{\\pi}\\right) "
        "is not recorded by Ramanujan.",
    ),
    rec(
        "RLN-P2-C15-Entry15-6-1",
        "Recall from (15.6.3) that A_k := \\frac{(\\frac{1}{2})_k^3}{k!^3}, k \\ge 0. "
        "Then \\frac{4}{\\pi} = \\sum_{k=0}^{\\infty} \\frac{(6k+1)A_k}{4^k}.",
    ),
    rec(
        "RLN-P2-C15-Entry15-6-2",
        "If A_k, k \\ge 0, is defined by (15.6.3), then "
        "\\frac{16}{\\pi} = \\sum_{k=0}^{\\infty} \\frac{(42k+5)A_k}{26^k}.",
    ),
    rec(
        "RLN-P2-C15-Entry15-6-3",
        "If A_k, k \\ge 0, is defined by (15.6.3), then "
        "\\frac{32}{\\pi} = \\sum_{k=0}^{\\infty} "
        "\\frac{\\left((42\\sqrt{5} + 30)^k + 5\\sqrt{5} - 1\\right)A_k}{26^k "
        "\\left(\\frac{\\sqrt{5}-1}{2}\\right)^{8k}}.",
    ),
]
