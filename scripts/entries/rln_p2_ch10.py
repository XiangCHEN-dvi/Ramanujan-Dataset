"""RLN Part 2, Chapter 10 — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C10 = ["miscellaneous-elliptic-theta-functions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C10}


CHAPTER_10 = [
    rec(
        "RLN-P2-C10-Entry10-1-1",
        "\\prod_{n=0}^{\\infty}\\left(1-\\frac{(-1)^nq^{(2n+1)/2}}"
        "{1+(-1)^nq^{(2n+1)/2}}\\right)^{2n+1}\\log q "
        "\\prod_{n=1}^{\\infty}\\left(1+\\frac{(-1)^niq'^n}"
        "{1-(-1)^niq'^n}\\right)^n 2\\pi i "
        "= \\exp\\left(\\frac{\\pi^2}{4}"
        "-\\frac{k\\,{}_3F_2(1,1,1;\\tfrac32,\\tfrac32;k^2)}"
        "{{}_2F_1(\\tfrac12,\\tfrac12;1;k^2)}\\right), "
        "where q = \\exp(-\\pi K'/K), q' = \\exp(-\\pi K/K'), and 0 < k < 1.",
    ),
    rec(
        "RLN-P2-C10-Entry10-4-1",
        "For each positive integer s and x > 0, define "
        "\\varphi_s(x) := \\sqrt{2\\pi x}\\,e^{\\pi x\\zeta(-s)}"
        "\\prod_{n=1}^{\\infty}(1-e^{-2\\pi x n^s}). Then "
        "\\varphi_s(x) = (2\\pi)^{s/2}\\exp\\left(\\frac{\\pi\\zeta(-1/s)}"
        "{x^{1/s}}\\sin\\frac{\\pi}{2s}\\right)"
        "\\prod_{j=0}^{s-1}\\prod_{n=1}^{\\infty}"
        "\\left[1-2\\exp\\left(-2\\pi n^{1/s}x^{1/s}"
        "\\sin\\frac{\\pi(2j+1)}{2s}\\right)"
        "\\cos\\left(2\\pi n^{1/s}x^{1/s}"
        "\\cos\\frac{\\pi(2j+1)}{2s}\\right)"
        "+\\exp\\left(-4\\pi n^{1/s}x^{1/s}"
        "\\sin\\frac{\\pi(2j+1)}{2s}\\right)\\right]^{1/2}.",
    ),
    rec(
        "RLN-P2-C10-Entry10-4-2",
        "The special cases s = 1, 2, 3 of Entry 10.4.1 are "
        "\\sqrt{x}\\,e^{-\\pi x/12}\\prod_{n=1}^{\\infty}(1-e^{-2\\pi n x})"
        "= e^{-\\pi/(12x)}\\prod_{n=1}^{\\infty}(1-e^{-2\\pi n/x}); "
        "\\frac12\\sqrt{\\frac{x}{\\pi}}\\exp\\left(-2\\pi\\zeta(-1/2)\\sqrt{x}\\right)"
        "\\prod_{n=1}^{\\infty}(1-e^{-\\pi x n^2})"
        "= \\prod_{n=1}^{\\infty}\\left(1-2e^{-2\\pi\\sqrt{n/x}}"
        "\\cos\\left(2\\pi\\sqrt{n/x}\\right)+e^{-4\\pi\\sqrt{n/x}}\\right); "
        "\\sqrt{x}\\exp\\left(\\frac{\\pi x}{120}-2\\pi\\zeta(-1/3)\\sqrt[3]{x}\\right)"
        "\\prod_{n=1}^{\\infty}(1-e^{-2\\pi n^3 x})"
        "= 2\\pi\\prod_{n=1}^{\\infty}\\left[\\left(1-e^{-2\\pi\\sqrt[3]{n/x}}\\right)"
        "\\left(1-2e^{-\\pi\\sqrt[3]{n/x}}\\cos\\left(\\frac{\\pi}{\\sqrt{3}}"
        "\\sqrt[3]{n/x}\\right)+e^{-2\\pi\\sqrt[3]{n/x}}\\right)\\right].",
    ),
    rec(
        "RLN-P2-C10-Entry10-4-3",
        "For each positive even integer s and x > 0, "
        "\\varphi_s(x) = (2\\pi)^{s/2}\\exp\\left(\\frac{\\pi\\zeta(-1/s)}"
        "{x^{1/s}}\\sin\\frac{\\pi}{2s}\\right)"
        "\\prod_{j=0}^{s/2-1}\\prod_{n=1}^{\\infty}"
        "\\left[1-2\\exp\\left(-2\\pi n^{1/s}x^{1/s}"
        "\\sin\\frac{\\pi(2j+1)}{2s}\\right)"
        "\\cos\\left(2\\pi n^{1/s}x^{1/s}"
        "\\cos\\frac{\\pi(2j+1)}{2s}\\right)"
        "+\\exp\\left(-4\\pi n^{1/s}x^{1/s}"
        "\\sin\\frac{\\pi(2j+1)}{2s}\\right)\\right]^{1/2}. "
        "For each positive odd integer s and x > 0, "
        "\\varphi_s(x) = (2\\pi)^{s/2}\\exp\\left(\\frac{\\pi\\zeta(-1/s)}"
        "{x^{1/s}}\\sin\\frac{\\pi}{2s}\\right)"
        "(1-e^{-2\\pi(n/x)^{1/s}})"
        "\\prod_{j=0}^{(s-3)/2}\\prod_{n=1}^{\\infty}"
        "\\left[1-2\\exp\\left(-2\\pi n^{1/s}x^{1/s}"
        "\\sin\\frac{\\pi(2j+1)}{2s}\\right)"
        "\\cos\\left(2\\pi n^{1/s}x^{1/s}"
        "\\cos\\frac{\\pi(2j+1)}{2s}\\right)"
        "+\\exp\\left(-4\\pi n^{1/s}x^{1/s}"
        "\\sin\\frac{\\pi(2j+1)}{2s}\\right)\\right]^{1/2}.",
    ),
    rec(
        "RLN-P2-C10-Entry10-5-1",
        "Let q = e^{-y} with y = \\pi\\,{}_2F_1(\\tfrac12,\\tfrac12;1;1-k^2)"
        "/\\,{}_2F_1(\\tfrac12,\\tfrac12;1;k^2), and let z\\theta = "
        "\\int_0^{\\varphi}\\!du/\\sqrt{1-k^2\\sin^2 u}. Then "
        "\\log\\tan\\left(\\frac{\\pi}{4}+\\frac{\\theta}{2}\\right)"
        "+ 4\\sum_{n=0}^{\\infty}\\frac{(-1)^nq^{2n+1}\\sin(2n+1)\\theta}"
        "{(2n+1)(1-q^{2n+1})}"
        "= \\log\\tan\\left(\\frac{\\pi}{4}+\\frac{\\varphi}{2}\\right).",
    ),
    rec(
        "RLN-P2-C10-Entry10-5-2",
        "With k' = \\sqrt{1-k^2} and z\\theta^* = "
        "\\int_0^{\\varphi}\\!du/\\sqrt{1-k'^2\\sin^2 u}, "
        "\\theta^* + 2\\sum_{n=1}^{\\infty}\\frac{q^n\\sinh(2n\\theta^*)}"
        "{n(1+q^{2n})}"
        "= \\log\\tan\\left(\\frac{\\pi}{4}+\\frac{\\varphi}{2}\\right).",
    ),
    rec(
        "RLN-P2-C10-Entry10-6-1",
        "Let K = K(k) denote the complete elliptic integral of the first kind "
        "for modulus k, and K' = K(k') for the complementary modulus "
        "k' = \\sqrt{1-k^2}. For n > 0, "
        "\\frac{\\pi n K}{2}\\left\\{\\frac{1}{n^2K^2}"
        "+ 4\\sum_{j=1}^{\\infty}\\frac{q^j}{1+q^{2j}}"
        "\\cdot\\frac{1}{n^2K^2+\\pi^2 j^2}\\right\\}"
        "= \\frac{1}{n}+\\frac{k^2}{n}+\\frac{2^2}{n}+\\frac{(3k)^2}{n}"
        "+\\frac{4^2}{n}+\\frac{(5k)^2}{n}+\\cdots.",
    ),
    rec(
        "RLN-P2-C10-Entry10-7-1",
        "Ramanujan records the following class invariants and modular equations: "
        "f_1(\\sqrt{-20}) = t^{1/(8\\sqrt{8})}, t^8-1+\\frac{\\sqrt{5}}{2}(2t^4+1)=0; "
        "f(\\sqrt{-27}) = t^{1/(3\\sqrt{2})}, t^9-3t^6-3t^3-1=0; "
        "f_1(\\sqrt{-26}) = t^{1/(4\\sqrt{2})}, "
        "t^6-t^4-3+\\frac{\\sqrt{13}}{2}(t^2+1)=0; "
        "f(\\sqrt{-29}) = t^{1/(4\\sqrt{2})}, "
        "2t^{12}-9t^8-8t^4-5=\\sqrt{29}(t^4+1)^2; "
        "f(\\sqrt{-35}) = t, t^3-2=(1+\\sqrt{5})(t^2-t); "
        "f_1(\\sqrt{-36}) = t^{1/(8\\sqrt{2})}, "
        "t^6-4t^3-2=2\\sqrt{3}(t^3+1); "
        "f_1(\\sqrt{-38}) = t^{1/(4\\sqrt{2})}, "
        "t^6-2t^4-(2t^2+1)(1+\\sqrt{2})=0; "
        "f(\\sqrt{-39}) = t^{1/\\sqrt{2}}, "
        "t^6-3+\\frac{\\sqrt{13}}{2}(t^3+1)=0; "
        "f(\\sqrt{-41}) = t^{1/(4\\sqrt{2})}, "
        "\\left(\\frac{t^2+1}{t^2}\\right)^2-\\frac{5+\\sqrt{41}}{2}"
        "\\left(\\frac{t^2+1}{t^2}\\right)+\\frac{7+\\sqrt{41}}{2}=0; "
        "f_1(\\sqrt{-44}) = t^{1/(8\\sqrt{8})}, "
        "t^{12}-(6+2\\sqrt{11})t^8+(8+2\\sqrt{11})t^4-(3+\\sqrt{11})=0; "
        "f_1(\\sqrt{-50}) = t^{1/(4\\sqrt{2})}, "
        "t^3-t^2=\\frac{1+\\sqrt{5}}{2}(t+1); "
        "f(\\sqrt{-51}) = t^{1/(3\\sqrt{2})}, "
        "t^9-(4+\\sqrt{17})t^6-t^3-1=0; "
        "f_1(\\sqrt{-52}) = t^{1/(8\\sqrt{8})}, "
        "t^8-2(4+\\sqrt{13})t^4-\\frac{3+\\sqrt{13}}{2}=0; "
        "f(\\sqrt{-63}) = t^{1/\\sqrt{2}}, "
        "\\frac{t^6+3t^3-1}{t^6-t^3+1}=\\sqrt{\\frac{7}{3}}; "
        "f(\\sqrt{-99}) = t^{1/(3\\sqrt{2})}, "
        "t^9-(12+2\\sqrt{33})t^6-(4+\\sqrt{33})t^3-1=0.",
    ),
]
