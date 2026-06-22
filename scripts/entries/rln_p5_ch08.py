"""RLN Part 5, Chapter 8 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C08 = ["tenth-order-mock-theta-part-i"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C08}


CHAPTER_8 = [
    rec(
        "RLN-P5-C08-Entry8-4-1",
        r"If $\varphi_{10}(q)$ and $\psi_{10}(q)$ are defined by (8.1.1) and (8.1.2), "
        r"respectively, and $\omega$ is a primitive cube root of unity, then "
        r"$q^{2/3}\varphi_{10}(q^3)-\dfrac{1}{\omega-\omega^2}"
        r"\bigl(\psi_{10}(\omega q^{1/3})-\psi_{10}(\omega^2 q^{1/3})\bigr)"
        r"=-\dfrac{q^{1/3}\,\displaystyle\sum_{n=-\infty}^{\infty}(-1)^n q^{n^2/3}"
        r"\displaystyle\sum_{m=-\infty}^{\infty}(-1)^m q^{m(5m+3)/2}}"
        r"}{(q;q^2)_\infty\,\displaystyle\sum_{n=-\infty}^{\infty}(-1)^n q^{n^2}}$.",
    ),
    rec(
        "RLN-P5-C08-Entry8-4-2",
        r"Under the same hypotheses as Entry 8.4.1, "
        r"$q^{-2/3}\psi_{10}(q^3)+\dfrac{1}{\omega-\omega^2}"
        r"\bigl(\omega\varphi_{10}(\omega q^{1/3})-\omega^2\varphi_{10}(\omega^2 q^{1/3})\bigr)"
        r"=\dfrac{\displaystyle\sum_{n=-\infty}^{\infty}(-1)^n q^{n^2/3}"
        r"\displaystyle\sum_{m=-\infty}^{\infty}(-1)^m q^{m(5m+1)/2}}"
        r"}{(q;q^2)_\infty\,\displaystyle\sum_{n=-\infty}^{\infty}(-1)^n q^{n^2}}$.",
    ),
    rec(
        "RLN-P5-C08-Entry8-4-3",
        r"If $X_{10}(q)$ and $\chi_{10}(q)$ are defined in (8.1.3) and (8.1.4), "
        r"respectively, and $\omega$ is a primitive cube root of unity, then "
        r"$X_{10}(q^3)-\dfrac{1}{\omega-\omega^2}"
        r"\bigl(\omega\chi_{10}(\omega q^{1/3})-\omega^2\chi_{10}(\omega^2 q^{1/3})\bigr)"
        r"=\dfrac{\displaystyle\sum_{n=-\infty}^{\infty}q^{n(n+1)/6}"
        r"\displaystyle\sum_{m=-\infty}^{\infty}(-1)^m q^{m(5m+1)}}"
        r"{(-q;q^2)_\infty\,\displaystyle\sum_{n=-\infty}^{\infty}q^{n(n+1)}}$.",
    ),
    rec(
        "RLN-P5-C08-Entry8-4-4",
        r"With the same hypotheses as Entry 8.4.3, "
        r"$\chi_{10}(q^3)+\dfrac{q^{2/3}}{\omega-\omega^2}"
        r"\bigl(X_{10}(\omega q^{1/3})-X_{10}(\omega^2 q^{1/3})\bigr)"
        r"=-\dfrac{q\,\displaystyle\sum_{n=-\infty}^{\infty}q^{n(n+1)/6}"
        r"\displaystyle\sum_{m=-\infty}^{\infty}(-1)^m q^{m(5m+3)}}"
        r"{(-q;q^2)_\infty\,\displaystyle\sum_{n=-\infty}^{\infty}q^{n(n+1)/2}}$.",
    ),
]
