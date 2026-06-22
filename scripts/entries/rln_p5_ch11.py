"""RLN Part 5, Chapter 11 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C11 = ["tenth-order-mock-theta-part-iv"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C11}


CHAPTER_11 = [
    rec(
        "RLN-P5-C11-Entry11-1-1",
        r"$\varphi_{10}(q)-q^{-1}\psi_{10}(-q^4)+q^{-2}\chi_{10}(q^8)"
        r"=\dfrac{\phi(q)\,h(-q^2)}{\psi(-q)}$, "
        r"where $h(q):=\displaystyle\sum_{n=-\infty}^{\infty}(-1)^n q^{n(5n+3)/2}$.",
    ),
    rec(
        "RLN-P5-C11-Entry11-1-2",
        r"$\psi_{10}(q)+q\,\varphi_{10}(-q^4)+q^{-2}X_{10}(q^8)"
        r"=\dfrac{\phi(q)\,g(-q^2)}{\psi(-q)}$, "
        r"where $g(q):=\displaystyle\sum_{n=-\infty}^{\infty}(-1)^n q^{n(5n+1)/2}$.",
    ),
]
