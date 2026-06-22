"""RLN Part 2, Chapter 14 — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C14 = ["series-representable-eisenstein-series"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C14}


CHAPTER_14 = [
    rec(
        "RLN-P2-C14-Entry14-2-1",
        "If T_{2k} is defined by (14.1.1) and P, Q, and R are defined by "
        "(14.1.2)--(14.1.4), then "
        "\\frac{T_2(q)}{(q;q)_\\infty} = P, "
        "\\frac{T_4(q)}{(q;q)_\\infty} = 3P^2 - 2Q, "
        "\\frac{T_6(q)}{(q;q)_\\infty} = 15P^3 - 30PQ + 16R, "
        "\\frac{T_8(q)}{(q;q)_\\infty} = 105P^4 - 420P^2Q + 448PR - 132Q^2, "
        "\\frac{T_{10}(q)}{(q;q)_\\infty} = 945P^5 - 6300P^3Q + 10080P^2R "
        "- 5940PQ^2 + 1216QR, "
        "and \\frac{T_{12}(q)}{(q;q)_\\infty} = 10395P^6 - 103950P^4Q + 221760P^3R "
        "- 196020P^2Q^2 + 80256PQR - 2712Q^3 - 9728R^2.",
    ),
    rec(
        "RLN-P2-C14-Entry14-2-2",
        "Define the polynomials f_{2k}(P, Q, R), k \\ge 1, by "
        "f_{2k}(P, Q, R) := \\frac{T_{2k}(q)}{(q;q)_\\infty}. "
        "Then, for k \\ge 1, "
        "f_{2k}(P, Q, R) = 1 \\cdot 3 \\cdots (2k-1) "
        "\\left(P^k - \\frac{k(k-1)}{3}P^{k-2}Q "
        "+ \\frac{8k(k-1)(k-2)}{45}P^{k-3}R "
        "- \\frac{11k(k-1)(k-2)(k-3)}{210}P^{k-4}Q^2 "
        "+ \\frac{152k(k-1)(k-2)(k-3)(k-4)}{14175}P^{k-5}QR + \\cdots\\right), "
        "where the missing terms contain all products P^a Q^b R^c such that "
        "2a + 4b + 6c = 2k.",
    ),
    rec(
        "RLN-P2-C14-Entry14-3-1",
        "For each nonnegative integer n, "
        "U_{n+2}(q) = P(q)U_n(q) + 8qU_n'(q).",
    ),
    rec(
        "RLN-P2-C14-Entry14-3-2",
        "If U_n(q) is defined by (14.1.5), then "
        "U_0(q) = 1, U_2(q) = P, "
        "U_4(q) = \\frac{1}{3}\\left(5P^2 - 2Q\\right), "
        "U_6(q) = \\frac{1}{9}\\left(35P^3 - 42PQ + 16R\\right), "
        "U_8(q) = \\frac{1}{3}\\left(35P^4 - 84P^2Q - 12Q^2 + 64PR\\right), "
        "and U_{10}(q) = \\frac{1}{9}\\left(385P^5 - 1540P^3Q - 660PQ^2 "
        "+ 1760P^2R + 64QR\\right).",
    ),
    rec(
        "RLN-P2-C14-Entry14-3-3",
        "For any positive integer s, "
        "U_{2s} = \\sum K_{\\ell,m,n} P^\\ell Q^m R^n, "
        "where the sum is over all nonnegative triples of integers "
        "\\ell, m, n such that \\ell + 2m + 3n = s.",
    ),
]
