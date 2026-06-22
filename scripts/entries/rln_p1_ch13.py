"""RLN Part 1, Chapter 13 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C13 = ["hadamard-products-two-q-series"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C13}


CHAPTER_13 = [
    rec("RLN-P1-C13-Entry13-6-1", "Identity (13.1.1) holds for all complex $a$ and real $q$ with $0<q<1/4$, where $\\displaystyle\\sum_{n=0}^{\\infty}a^nq^{n^2}=\\prod_{n=1}^{\\infty}\\left(1+\\frac{aq^{2n-1}}{1-q^ny_1-q^{2n}y_2-q^{3n}y_3-\\cdots}\\right)$. The zeros $z_n$ of $K_\\infty(z)$ satisfy, for example, $z_1=-q^{-2}(1-q+q^2-2q^3+4q^4-\\cdots)$, $z_2=-q^{-4}(1-q^2+q^3-2q^4+4q^5-7q^6+11q^7-18q^8+33q^9-\\cdots)$, $z_3=-q^{-6}(1-q^3+q^4-2q^5+4q^6-7q^7+11q^8-17q^9+27q^{10}-43q^{11}+68q^{12}-112q^{13}+196q^{14}-\\cdots)$, $z_4=-q^{-8}(1-q^4+q^5-2q^6+4q^7-7q^8+11q^9-17q^{10}+27q^{11}-42q^{12}+62q^{13}-91q^{14}+138q^{15}-213q^{16}+334q^{17}-549q^{18}+957q^{19}-\\cdots)$, and $z_5=-q^{-10}(1-q^5+q^6-2q^7+4q^8+7q^9+11q^{10}-17q^{11}+27q^{12}-42q^{13}+62q^{14}-90q^{15}+132q^{16}-192q^{17}+275q^{18}-398q^{19}+591q^{20}-900q^{21}+1417q^{22}-2327q^{23}+3971q^{24}-\\cdots)$."),
    rec("RLN-P1-C13-Entry13-11-1", "The expansion (13.1.7) holds for $0<q<1/4$."),
]
