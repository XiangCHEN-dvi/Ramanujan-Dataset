"""RLN Part 4, Chapter 21 — mined manuscript fragments (enigmatic partial manuscript).

No Entry labels in Berndt; results extracted from Ramanujan's strange partial manuscript
on analytic number theory (book eqs. 21.2.1–21.2.13).
"""

from __future__ import annotations

TOPICS_C21 = ["enigmatic-partial-manuscript"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C21}


CHAPTER_21 = [
    rec(
        "RLN-P4-C21-Formula2101",
        r"Ramanujan claims "
        r"$\sum_{k=1}^n d(k)=n(2\gamma-1+\log n)+O(\max d(n))$, "
        r"and that $a_1+a_2+\cdots+a_n$ can be expressed in terms of $n$ with error "
        r"$O(\max a_n-\min a_n)$, perhaps even with the maximum and minimum of the error term determined.",
    ),
    rec(
        "RLN-P4-C21-Formula2102",
        r"Ramanujan asserts that the sum of the first $n$ prime logarithms can be expressed in "
        r"terms of $n$ with error $o(1)$ or even $O(n^{-1/2+\varepsilon})$, and defines the "
        r"maximum order of $a_n$ as $\max_r(\text{average order of }a_r n)$; "
        r"for example $\max d(n)=2^{\log n/\log\log n}(1+\varepsilon)$.",
    ),
    rec(
        "RLN-P4-C21-Formula2103",
        r"If $b_n$ is steadily increasing, $\max a_n>b_n$, and "
        r"$\sum_{k=1}^\infty a_k e^{-kx}-\sum_{k=1}^\infty b_k e^{-kx}=O(1)$ as $x\to 0$, "
        r"then Ramanujan claims "
        r"$\sum_{k=1}^m a_k e^{-kx}-\sum_{k=1}^m b_k e^{-kx}=O(\max a_n-\min a_n)$, "
        r"and if $a_n$ is also steadily increasing, then $a_n\sim b_n$.",
    ),
    rec(
        "RLN-P4-C21-Formula2104",
        r"Ramanujan states that if $a_n$ and $b_n$ are steadily increasing and "
        r"$\sum_{n=1}^\infty a_n^{-s}$ and $\sum_{n=1}^\infty b_n^{-s}$ both converge for $s>k$ "
        r"and both diverge for $s=k$ with difference $O(1)$ at $s=k$, then $a_n\sim b_n$; "
        r"analogous results hold for $\sum_{n=1}^\infty a_n/n^s$.",
    ),
    rec(
        "RLN-P4-C21-Formula2105",
        r"Ramanujan claims that if $a_n$ and $b_n$ are steadily increasing and "
        r"$\sum_{n=1}^\infty e^{-a_n x}\sim\sum_{n=1}^\infty e^{-b_n x}$ as $x\to 0$, "
        r"then (conclusion missing in the manuscript) $a_n\sim b_n$.",
    ),
    rec(
        "RLN-P4-C21-Formula2106",
        r"The number of integers of the form $2^m3^n$ less than $x$ equals "
        r"$\tfrac12\cdot\dfrac{\log(2x)}{\log 2}\cdot\dfrac{\log(3x)}{\log 3}+O(1)$.",
    ),
    rec(
        "RLN-P4-C21-Formula2107",
        r"The number of integers of the form $a^2+b^2$ less than $x$ equals "
        r"$C\int^x \dfrac{dt}{\sqrt{\log t}}+O(x^{1/2+\varepsilon})$, where "
        r"$C=\sqrt{2}\prod_{p\equiv 3\pmod 4}\!\left(1-\dfrac{1}{p^2}\right)^{-1/2}"
        r"=\sqrt{2}\left(1+\dfrac{1}{7}\right)\!\left(1+\dfrac{1}{11}\right)\!\left(1+\dfrac{1}{19}\right)\cdots$.",
    ),
    rec(
        "RLN-P4-C21-Formula2108",
        r"The number of integers of the form $a^2b^3$ less than $x$ equals "
        r"$\sqrt{4.723034}\,x^{1/2}-\sqrt[3]{3.10227}\,x^{1/3}+O(x^{1/6+\varepsilon})$ "
        r"(Ramanujan's constants; the correct values are "
        r"$\zeta(\tfrac32)\sqrt{x}+\zeta(\tfrac23)\sqrt[3]{x}+O(x^{1/5})$).",
    ),
]
