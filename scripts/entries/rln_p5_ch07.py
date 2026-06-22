"""RLN Part 5, Chapter 7 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C07 = ["sixth-order-mock-theta-functions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C07}


CHAPTER_7 = [
    rec(
        "RLN-P5-C07-Entry7-4-1",
        r"We have "
        r"$(q;q)_\infty\,\varphi_6(q)"
        r"=1-2\displaystyle\sum_{n=-\infty}^{\infty}\dfrac{q^{(2n+1)(3n+1)}}{1+q^{3n+1}}"
        r"+2\displaystyle\sum_{n=1}^{\infty}\dfrac{q^{n(6n+1)}}{1-q^n+q^{2n}}$, "
        r"$(-q,-q^2,q^3;q^3)_\infty\,\varphi_6(q)"
        r"=2\displaystyle\sum_{n=-\infty}^{\infty}\dfrac{q^{n(3n+1)/2}}{1+q^{3n}}$, "
        r"$\psi(q^3)\,\varphi_6(q)"
        r"=\displaystyle\sum_{n=-\infty}^{\infty}\dfrac{q^{3n(n+1)/2}}{1+q^{3n+1}}$, "
        r"and $(-q,-q^2,q^3;q^3)_\infty\,\psi_6(q)"
        r"=\displaystyle\sum_{n=-\infty}^{\infty}\dfrac{q^{(n+1)(3n+2)/2}}{1+q^{3n+1}}$.",
    ),
    rec(
        "RLN-P5-C07-Entry7-4-2",
        r"If $\omega=e^{2\pi i/3}$, then "
        r"$\dfrac{\psi_6(\omega q)-\psi_6(\omega^2 q)}{(\omega-\omega^2)q}"
        r"=\dfrac{\psi(q)\,\psi(q^9)\,(q^6;q^6)_\infty^2}{\psi(q^3)}$ "
        r"and "
        r"$\varphi_6(q^9)-\psi_6(q)-q^{-3}\psi_6(q^9)"
        r"=\dfrac{\psi(q^3)\,(q^6;q^6)_\infty^2}{\psi(q)\,\psi(q^9)}$.",
    ),
    rec(
        "RLN-P5-C07-Entry7-5-1",
        r"We have "
        r"$q^{-1}\psi_6(q^2)+\rho_6(q)=(-q;q^2)_\infty^2\,(-q,-q^5,q^6;q^6)_\infty$, "
        r"$\varphi_6(q^2)+2\sigma_6(q)=(-q;q^2)_\infty^2\,(-q^3,-q^3,q^6;q^6)_\infty$, "
        r"and "
        r"$\rho_6(q)=2q^{-1}\Phi_6(q^3)+\dfrac{\psi^2(q)}{\phi(-q^3)}$.",
    ),
    rec(
        "RLN-P5-C07-Entry7-5-2",
        r"We have "
        r"$2\varphi_6(q^2)-2\mu_6(-q)=(-q;q^2)_\infty^2\,(-q^3,-q^3,q^6;q^6)_\infty$ "
        r"and "
        r"$2q^{-1}\psi_6(q^2)+\lambda_6(-q)=(-q;q^2)_\infty^2\,(-q,-q^5,q^6;q^6)_\infty$.",
    ),
    rec(
        "RLN-P5-C07-Entry7-5-3",
        r"$2\gamma_6(q)=3\varphi_6(q)-\dfrac{\phi^2(-q)}{(-q,-q^2,q^3;q^3)_\infty}$.",
    ),
    rec(
        "RLN-P5-C07-Entry7-6-1",
        r"If $\psi_6(q)$ is defined by (7.1.2), then "
        r"$\displaystyle\sum_{n=0}^{\infty}\dfrac{(-1)^n(q^3;q^6)_n}{(-q^3;q^3)_{2n}}"
        r"-2\psi_6(q)=\dfrac{\phi^2(-q)}{2\psi(q^3)}$.",
    ),
    rec(
        "RLN-P5-C07-Entry7-6-2",
        r"If $\varphi_6(q)$ is defined by (7.1.1), then "
        r"$\varphi_6(q)+2\displaystyle\sum_{n=1}^{\infty}\dfrac{(-q;q)_{2n-1}\,q^n}{(q;q^2)_n}"
        r"=\dfrac{1}{(q;q)_\infty}\left("
        r"1+6\displaystyle\sum_{n=1}^{\infty}\left(\dfrac{n}{3}\right)\dfrac{q^{2n}}{1-q^{2n}}\right)$, "
        r"where $\left(\dfrac{n}{3}\right)$ denotes the Legendre symbol.",
    ),
]
