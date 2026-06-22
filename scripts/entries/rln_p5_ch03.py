"""RLN Part 5, Chapter 3 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C03 = ["fifth-order-mock-theta-elementary"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C03}


CHAPTER_3 = [
    rec(
        "RLN-P5-C03-Entry3-4-1",
        r"$\psi_1(q)-q^{-1}\varphi_1(-q^2)=\phi(q)H(-q)$.",
    ),
    rec(
        "RLN-P5-C03-Entry3-4-2",
        r"$f_1(q)+2qF_1(q^2)=\phi(q)H(-q)$.",
    ),
    rec(
        "RLN-P5-C03-Entry3-4-3",
        r"$f_1(q)+2q^{-1}\varphi_1(-q^2)=\phi(-q)H(q)$.",
    ),
    rec(
        "RLN-P5-C03-Entry3-4-4",
        r"$\psi_1(q)-qF_1(q^2)=\psi(q^2)G(q^4)$.",
    ),
    rec(
        "RLN-P5-C03-Entry3-4-5",
        r"$\psi_0(q)+\varphi_0(-q^2)=\phi(q)G(-q)$.",
    ),
    rec(
        "RLN-P5-C03-Entry3-4-6",
        r"$f_0(q)+2F_0(q^2)-2=\phi(q)G(-q)$.",
    ),
    rec(
        "RLN-P5-C03-Entry3-4-7",
        r"$f_0(q)-2\varphi_0(-q^2)=-\phi(-q)G(q)$.",
    ),
    rec(
        "RLN-P5-C03-Entry3-4-8",
        r"$\psi_0(q)-F_0(q^2)+1=q\psi(q^2)H(q^4)$.",
    ),
    rec(
        "RLN-P5-C03-Entry3-4-9",
        r"$\chi_0(q)+\varphi_0(-q)=2F_0(q)$.",
    ),
    rec(
        "RLN-P5-C03-Entry3-4-10",
        r"$\chi_0(q)=\widehat{\chi}_0(q)$.",
    ),
    rec(
        "RLN-P5-C03-Entry3-4-11",
        r"$\chi_1(q)-q^{-1}\varphi_1(-q)=2F_1(q)$.",
    ),
    rec(
        "RLN-P5-C03-Entry3-4-12",
        r"$W_1(q)=\dfrac{\varphi_0(-q)}{\phi(-q)}$.",
    ),
    rec(
        "RLN-P5-C03-Entry3-4-13",
        r"$W_2(q)=-\dfrac{\varphi_1(-q)}{\phi(-q)}$.",
    ),
    rec(
        "RLN-P5-C03-Entry3-4-14",
        r"$W_3(q)=1-\dfrac{\varphi_0(-q)}{\phi(-q)}$.",
    ),
]
