"""RLN Part 5, Chapter 5 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C05 = ["mock-theta-conjectures-equivalence"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C05}


CHAPTER_5 = [
    rec(
        "RLN-P5-C05-Entry5-1-1",
        r"Let $A(q):=\dfrac{G^2(q)(q^5;q^5)_\infty}{H(q)}$, where $G(q)$ and $H(q)$ are defined in "
        r"(3.1.16) and (3.1.17), and let "
        r"$\Phi(q):=-1+\displaystyle\sum_{n=0}^{\infty}\dfrac{q^{5n^2}}{(q;q^5)_{n+1}(q^4;q^5)_n}$. "
        r"Then "
        r"$M_1(q):=\chi_0(q)-2-3\Phi(q)+A(q)=0$, "
        r"$M_2(q):=F_0(q)-1-\Phi(q)+q\psi(q^5)H(q^2)=0$, "
        r"$M_3(q):=\varphi_0(-q)+\Phi(q)-\dfrac{(q^5;q^5)_\infty G(q^2)H(q)}{H(q^2)}=0$, "
        r"$M_4(q):=\psi_0(q)-\Phi(q^2)-qH(q)f(-q^9,-q)=0$, "
        r"and $M_5(q):=f_0(q)+2\Phi(q^2)-\phi(-q^5)G(q)=0$.",
    ),
    rec(
        "RLN-P5-C05-Entry5-1-2",
        r"Let $D(q):=\dfrac{H^2(q)(q^5;q^5)_\infty}{G(q)}$ and "
        r"$\Psi(q):=-1+\displaystyle\sum_{n=0}^{\infty}\dfrac{q^{5n^2}}{(q^2;q^5)_{n+1}(q^3;q^5)_n}$. "
        r"Then "
        r"$M_6(q):=q\chi_1(q)-3\Psi(q)-qD(q)=0$, "
        r"$M_7(q):=qF_1(q)-\Psi(q)-q\psi(q^5)G(q^2)=0$, "
        r"$M_8(q):=-\varphi_1(-q)+\Psi(q)-\dfrac{q(q^5;q^5)_\infty G(q)H(q^2)}{G(q^2)}=0$, "
        r"$M_9(q):=\psi_1(q)-\dfrac{1}{q}\Psi(q^2)-G(q)f(-q^7,-q^3)=0$, "
        r"and $M_{10}(q):=f_1(q)+\dfrac{2}{q}\Psi(q^2)-\phi(-q^5)H(q)=0$.",
    ),
]
