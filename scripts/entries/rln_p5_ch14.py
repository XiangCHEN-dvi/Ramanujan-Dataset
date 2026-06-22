"""RLN Part 5, Chapter 14 — mined Ramanujan's last letter to Hardy.

No Entry labels in Berndt; propositions extracted from Ramanujan's letter of
12 January 1920 (book §14.2), excluding Hardy/editor commentary.
"""

from __future__ import annotations

TOPICS_C14 = ["ramanujan-last-letter"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C14}


CHAPTER_14 = [
    rec(
        "RLN-P5-C14-Letter01",
        r"Ramanujan defines mock $\vartheta$-functions: unlike Rogers's false "
        r"$\vartheta$-functions, mock $\vartheta$-functions enter mathematics as "
        r"beautifully as ordinary $\vartheta$-functions, yet are not ordinary "
        r"$\vartheta$-functions.",
    ),
    rec(
        "RLN-P5-C14-Letter02",
        r"Ramanujan gives an Eulerian $\vartheta$-series of type (A): "
        r"$1+\dfrac{q}{(1-q)^2}+\dfrac{q^4}{(1-q)^2(1-q^2)^2}"
        r"+\dfrac{q^9}{(1-q)^2(1-q^2)^2(1-q^3)^2}+\cdots$.",
    ),
    rec(
        "RLN-P5-C14-Letter03",
        r"Ramanujan gives an Eulerian $\vartheta$-series of type (B): "
        r"$1+\dfrac{q}{1-q}+\dfrac{q^4}{(1-q)(1-q^2)}"
        r"+\dfrac{q^9}{(1-q)(1-q^2)(1-q^3)}+\cdots$.",
    ),
    rec(
        "RLN-P5-C14-Letter04",
        r"For series (A) with $q=e^{-t}$ and $t\to 0$, Ramanujan claims "
        r"$(\mathrm{A})=\sqrt{\dfrac{t}{2\pi}}\exp\!\left(\dfrac{\pi^2}{6t}-\dfrac{t}{24}\right)"
        r"+o(1)$.",
    ),
    rec(
        "RLN-P5-C14-Letter05",
        r"For series (B) with $q=e^{-t}$ and $t\to 0$, Ramanujan claims "
        r"$(\mathrm{B})=\exp\!\left(\dfrac{\pi^2}{15t}-\dfrac{t}{60}\right)"
        r"\sqrt{\dfrac{5-\sqrt{5}}{2}}+o(1)$.",
    ),
    rec(
        "RLN-P5-C14-Letter06",
        r"Ramanujan states that near $q=1$ the function "
        r"$\bigl\{(1-q)(1-q^2)(1-q^3)\cdots\bigr\}^{-120}$ is equivalent to the "
        r"sum of five terms of the closed exponential form above, together with "
        r"$O(1)$ instead of $o(1)$.",
    ),
    rec(
        "RLN-P5-C14-Letter07",
        r"Ramanujan gives an unclosed Eulerian series (C): "
        r"$1+\dfrac{q}{(1-q)^2}+\dfrac{q^3}{(1-q)^2(1-q^2)^2}"
        r"+\dfrac{q^6}{(1-q)^2(1-q^2)^2(1-q^3)^2}+\cdots$. "
        r"With $q=e^{-t}$ and $t\to 0$, "
        r"$(\mathrm{C})=\sqrt{\dfrac{t}{2\sqrt{5}}}\exp\!\left(\dfrac{\pi^2}{5t}"
        r"+a_1 t+a_2 t^2+\cdots+O(a_k t^k)\right)$ where $a_1=\dfrac{1}{8\sqrt{5}}$.",
    ),
    rec(
        "RLN-P5-C14-Letter08",
        r"Ramanujan defines a mock $\vartheta$-function: if a function in Eulerian "
        r"form has exponential singularities at every $q=e^{2\pi i m/n}$ whose "
        r"asymptotics close as neatly as in types (A) and (B), yet the function is "
        r"not the sum of an ordinary $\vartheta$-function and a trivial $O(1)$ "
        r"function at all such points, then it is a mock $\vartheta$-function.",
    ),
    rec(
        "RLN-P5-C14-Letter09",
        r"Ramanujan defines the third-order mock theta function "
        r"$f_3(q):=1+\dfrac{q}{(1+q)^2}+\dfrac{q^4}{(1+q)^2(1+q^2)^2}+\cdots$.",
    ),
    rec(
        "RLN-P5-C14-Letter10",
        r"Ramanujan claims $f_3(q)+(1-q)(1-q^3)(1-q^5)\cdots"
        r"(1-2q+2q^4-2q^9+\cdots)=O(1)$ at $q=-1,q^3=-1,q^5=-1,\ldots$, and "
        r"$f_3(q)-(1-q)(1-q^3)(1-q^5)\cdots(1-2q+2q^4-\cdots)=O(1)$ at "
        r"$q^2=-1,q^4=-1,\ldots$, while $f_3(q)=O(1)$ at $q=1,q^3=1,\ldots$; "
        r"hence $f_3$ is a mock $\vartheta$-function.",
    ),
    rec(
        "RLN-P5-C14-Letter11",
        r"When $q=-e^{-t}$ and $t\to 0$, Ramanujan claims "
        r"$f_3(q)+\sqrt{\dfrac{\pi}{t}}\exp\!\left(\dfrac{\pi^2}{24t}-\dfrac{t}{24}\right)\to 4$.",
    ),
    rec(
        "RLN-P5-C14-Letter12",
        r"Ramanujan claims the coefficient of $q^n$ in $f_3(q)$ equals "
        r"$(-1)^{n-1}\exp\!\left(\pi\sqrt{\bigl(\dfrac{n}{6}-\dfrac{1}{144}\bigr)^2"
        r"\bigl(n-\dfrac{1}{24}\bigr)}\right)+O\!\left(\exp\!\left(\dfrac{1}{2\pi}"
        r"\bigl(\dfrac{n}{6}-\dfrac{1}{144}\bigr)^2\bigl(n-\dfrac{1}{24}\bigr)\right)\right)$.",
    ),
    rec(
        "RLN-P5-C14-Letter13",
        r"Ramanujan defines third-order mock $\vartheta$-functions "
        r"$\varphi_3(q):=1+\dfrac{q}{1+q^2}+\dfrac{q^4}{(1+q^2)(1+q^4)}+\cdots$, "
        r"$\psi_3(q):=\dfrac{q}{1-q}+\dfrac{q^4}{(1-q)(1-q^3)}+\cdots$, and "
        r"$\chi_3(q):=1+\dfrac{q}{1-q+q^2}+\dfrac{q^4}{(1-q+q^2)(1-q^2+q^4)}+\cdots$.",
    ),
    rec(
        "RLN-P5-C14-Letter14",
        r"Ramanujan relates third-order mock functions by "
        r"$2\varphi_3(-q)-f_3(q)=f_3(q)+4\psi_3(-q)=1-2q+2q^4-2q^9+\cdots$, "
        r"$(1+q)(1+q^2)(1+q^3)\cdots$, and "
        r"$4\chi_3(q)-f_3(q)=\dfrac{(1-2q^3+2q^{12}+\cdots)^2}{(1-q)(1-q^2)(1-q^3)\cdots}$.",
    ),
    rec(
        "RLN-P5-C14-Letter15",
        r"Ramanujan defines fifth-order mock $\vartheta$-functions "
        r"$f_0(q):=1+\dfrac{q}{1+q}+\dfrac{q^4}{(1+q)(1+q^2)}+\cdots$, "
        r"$\varphi_0(q):=1+q(1+q)+q^4(1+q)(1+q^3)+\cdots$, "
        r"$\psi_0(q):=q+q^3(1+q)+q^6(1+q)(1+q^2)+\cdots$, "
        r"$\chi_0(q):=1+\dfrac{q}{1-q^2}+\dfrac{q^2}{(1-q^3)(1-q^4)}+\cdots$, and "
        r"$F_0(q):=1+\dfrac{q^2}{1-q}+\dfrac{q^8}{(1-q)(1-q^3)}+\cdots$.",
    ),
    rec(
        "RLN-P5-C14-Letter16",
        r"Ramanujan gives fifth-order identities "
        r"$\varphi_0(-q)+\chi_0(q)=2F_0(q)$, "
        r"$f_0(-q)+2F_0(q^2)-2=\varphi_0(-q^2)+\psi_0(-q)=2\varphi_0(-q^2)-f_0(q)"
        r"$=1-2q+2q^4-2q^9+\cdots$ over $(1-q)(1-q^4)(1-q^6)\cdots$, and "
        r"$\psi_0(q)-F_0(q^2)+1=\dfrac{q}{1+q^2+q^6+q^{12}+\cdots}$ over "
        r"$(1-q^8)(1-q^{12})(1-q^{28})\cdots$.",
    ),
    rec(
        "RLN-P5-C14-Letter17",
        r"Ramanujan defines fifth-order mock $\vartheta$-functions "
        r"$f_1(q):=1+\dfrac{q^2}{1+q}+\dfrac{q^6}{(1+q)(1+q^2)}+\cdots$, "
        r"$\varphi_1(q):=q+q^4(1+q)+q^9(1+q)(1+q^3)+\cdots$, "
        r"$\psi_1(q):=1+q(1+q)+q^3(1+q)(1+q^2)+q^6((1+q)(1+q^2)(1+q^3)+\cdots)$, "
        r"$\chi_1(q):=\dfrac{1}{1-q}+\dfrac{q}{(1-q^2)(1-q^3)}+\cdots$, and "
        r"$F_1(q):=\dfrac{1}{1-q}+\dfrac{q^4}{(1-q)(1-q^3)}+\dfrac{q^{12}}{(1-q)(1-q^3)(1-q^5)}+\cdots$.",
    ),
    rec(
        "RLN-P5-C14-Letter18",
        r"Ramanujan states that the fifth-order functions $f_1,\varphi_1,\psi_1,\chi_1,F_1$ "
        r"have similar relations to those of $f_0,\varphi_0,\psi_0,\chi_0,F_0$.",
    ),
    rec(
        "RLN-P5-C14-Letter19",
        r"Ramanujan defines seventh-order mock $\vartheta$-functions: "
        r"(i) $1+\dfrac{q}{1-q^2}+\dfrac{q^4}{(1-q^3)(1-q^4)}+\dfrac{q^9}{(1-q^4)(1-q^5)(1-q^6)}+\cdots$, "
        r"(ii) $\dfrac{q}{1-q}+\dfrac{q^4}{(1-q^2)(1-q^3)}+\dfrac{q^9}{(1-q^3)(1-q^4)(1-q^5)}+\cdots$, "
        r"(iii) $\dfrac{1}{1-q}+\dfrac{q^2}{(1-q^2)(1-q^3)}+\dfrac{q^6}{(1-q^3)(1-q^4)(1-q^5)}+\cdots$.",
    ),
    rec(
        "RLN-P5-C14-Letter20",
        r"Ramanujan states that the three seventh-order mock $\vartheta$-functions "
        r"are not related to each other.",
    ),
]
