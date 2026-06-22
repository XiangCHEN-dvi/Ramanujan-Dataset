"""RLN Part 4, Chapter 18 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C18 = ["definite-integrals-partial-manuscript"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C18}


CHAPTER_18 = [
    rec(
        "RLN-P4-C18-Entry18-5-1",
        r"Let $\chi_4(n)=(-1)^m$ if $n=2m+1$ and $\chi_4(n)=0$ if $n$ is even, and let "
        r"$\chi_3(n)=\left(\dfrac{n}{3}\right)$ denote the Legendre symbol. Let $\zeta(s)$ "
        r"denote the Riemann zeta function, and let $L(s,\chi_4)$ and $L(s,\chi_3)$ denote "
        r"the Dirichlet $L$-functions associated with $\chi_4$ and $\chi_3$. Then "
        r"$\dfrac{(1-2^{2/3})\zeta(1/3)}{(1-2^{1/3})\zeta(2/3)}="
        r"\dfrac{\pi^{1/3}}{\Gamma(1/3)}\dfrac{2^{1/3}+4^{1/3}}{\sqrt{3}}$, "
        r"$\dfrac{L(1/3,\chi_4)}{L(2/3,\chi_4)}=\dfrac{\pi^{1/3}}{\Gamma(1/3)}\cdot 4^{1/3}$, "
        r"$\dfrac{L(1/3,\chi_3)}{L(2/3,\chi_3)}="
        r"\dfrac{\pi^{1/3}}{\Gamma(1/3)}\cdot 2^{1/3}\cdot 3^{1/6}$, "
        r"$\dfrac{(1-2^{3/4})\zeta(1/4)}{(1-2^{1/4})\zeta(3/4)}="
        r"\dfrac{\pi^{1/4}}{\Gamma(1/4)}\sqrt{3+2^{5/4}}$, "
        r"$\dfrac{L(1/4,\chi_4)}{L(3/4,\chi_4)}="
        r"\dfrac{\pi^{1/4}}{\Gamma(1/4)}\sqrt{2+2\sqrt{2}}$, and "
        r"$\dfrac{L(1/4,\chi_3)}{L(3/4,\chi_3)}="
        r"\dfrac{\pi^{1/4}}{\Gamma(1/4)}\sqrt{3+\sqrt{6}}$.",
    ),
]
