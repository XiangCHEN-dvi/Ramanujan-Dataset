"""RLN Part 5, Chapter 2 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C02 = ["third-order-mock-theta-elementary"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C02}


CHAPTER_2 = [
    rec(
        "RLN-P5-C02-Entry2-3-1",
        r"With $\phi(-q)$, $f_3(q)$, $\varphi_3(q)$, and $\psi_3(q)$ defined in (2.3.1), (2.1.1), "
        r"(2.1.2), and (2.1.3), respectively, "
        r"$2\varphi_3(-q)-f_3(q)=f_3(q)+4\psi_3(-q)=\dfrac{\phi^2(-q)}{(q;q)_\infty}$.",
    ),
    rec(
        "RLN-P5-C02-Entry2-3-2",
        r"With $\rho_3(q)$, $\omega_3(q)$, and $\psi(q)$ defined in (2.1.7), (2.1.5), and (2.3.6), "
        r"$\sqrt{q}\left(\dfrac{2}{3}\rho_3(-q)+\dfrac{1}{3}\omega_3(-q)\right)"
        r"=\sqrt{q}\,\dfrac{\psi^2(-q^3)}{(q^2;q^2)_\infty}$.",
    ),
    rec(
        "RLN-P5-C02-Entry2-3-3",
        r"If $f_3(q)$ is defined by (2.1.1), $\phi(-q)$ by (2.3.1), and $\chi_3(q)$ by (2.1.4), then "
        r"$\chi_3(q)=\dfrac{1}{4}f_3(q)+\dfrac{3}{4}\dfrac{\phi^2(-q^3)}{(q;q)_\infty}$.",
    ),
    rec(
        "RLN-P5-C02-Entry2-3-4",
        r"If $f_3(q)$ is defined by (2.1.1) and $\phi(-q)$ by (2.3.1), then "
        r"$\displaystyle\sum_{n=0}^{\infty}\dfrac{q^{3n^2}}{(-q;q^3)_{n+1}(-q^2;q^3)_n}"
        r"=\dfrac{1}{4}-\dfrac{1}{4}f_3(q^3)+\dfrac{1}{4}\dfrac{\phi^2(-q)}{(q^3;q^3)_\infty}$.",
    ),
    rec(
        "RLN-P5-C02-Entry2-3-5",
        r"For $\omega_3(q)$ defined by (2.1.5) and $\psi(q)$ defined by (2.3.6), "
        r"$\displaystyle\sum_{n=0}^{\infty}\dfrac{q^{6n^2}}{(q;q^6)_{n+1}(q^5;q^6)_n}"
        r"=\dfrac{1}{2}\left(1+q^2\omega_3(q^3)+\dfrac{\psi^2(q)}{(q^6;q^6)_\infty}\right)$.",
    ),
    rec(
        "RLN-P5-C02-Entry2-3-6",
        r"If $f_3(q)$ is given by (2.1.1) and $\phi(-q)$ by (2.3.1), then "
        r"$\displaystyle\sum_{n=0}^{\infty}\dfrac{(-1)^n(q;q)_{2n}q^{n^2}}{(q^6;q^6)_n}"
        r"=\dfrac{3}{4}f_3(q^3)+\dfrac{1}{4}\dfrac{\phi^2(-q)}{(q^3;q^3)_\infty}$.",
    ),
    rec(
        "RLN-P5-C02-Entry2-3-7",
        r"$\displaystyle\sum_{n=0}^{\infty}\dfrac{(q;q^2)_n(-q^2;q^2)_nq^{2n}}{(-q^6;q^6)_n}"
        r"=\dfrac{3}{2}\displaystyle\sum_{n=0}^{\infty}(-1)^nq^{(3n+2)(3n+1)/2}"
        r"+\dfrac{1}{2}\displaystyle\sum_{n=0}^{\infty}(-1)^nq^{n(n+1)/2}"
        r"+\dfrac{1}{2}\dfrac{(q;-q)_\infty}{(-q^6;q^6)_\infty}"
        r"\displaystyle\sum_{n=0}^{\infty}q^{3n^2+2n}(1-q^{2n+1})$.",
    ),
    rec(
        "RLN-P5-C02-Entry2-3-8",
        r"If $\nu_3(q)$ is given by (2.1.6), $\omega_3(q)$ by (2.1.5), and $\psi(q)$ by (2.3.6), then "
        r"$\nu_3(-q)=q\,\omega_3(q^2)+\dfrac{\psi(q^2)}{(q^2;q^4)_\infty}$.",
    ),
    rec(
        "RLN-P5-C02-Entry2-3-9",
        r"With $\phi(-q)$ defined by (2.3.1), "
        r"$\displaystyle\sum_{n=0}^{\infty}\dfrac{(-1)^nq^{n^2}}{(-aq^2;q^2)_n}"
        r"=\dfrac{1}{2}\displaystyle\sum_{n=0}^{\infty}\dfrac{a^nq^{n^2}}{(-q;q)_n(-aq;q)_n}"
        r"+\dfrac{1}{2}\dfrac{\phi(-q)}{(-aq;q)_\infty}$, "
        r"and "
        r"$\displaystyle\sum_{n=0}^{\infty}\dfrac{(-1)^nq^{n^2}}{(-aq^2;q^2)_n}"
        r"=(1+a)\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}\dfrac{q^{n^2}}{(-aq;q^2)_n}"
        r"+\dfrac{\phi(-q)}{(-aq;q)_\infty}$.",
    ),
]
