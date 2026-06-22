"""RLN Part 4, Chapter 15 — mined manuscript fragments (Mellin transform functional equations).

No Entry labels in Berndt; results extracted from Ramanujan's manuscript on functional
equations for products of Mellin transforms (book eqs. 15.2.1–15.5.4).
"""

from __future__ import annotations

TOPICS_C15 = ["mellin-transform-functional-equations"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C15}


CHAPTER_15 = [
    rec(
        "RLN-P4-C15-Problem1501",
        r"Let $X_1(s)=\int_0^\infty x^{s-1}\chi_1(x)\,dx$ and "
        r"$X_2(s)=\int_0^\infty x^{s-1}\chi_2(x)\,dx$. Ramanujan's main problem is to choose "
        r"$\chi_1,\chi_2$ so that $X_1(s)X_2(1-s)=\lambda^2$ for a constant $\lambda$ independent of $s$.",
    ),
    rec(
        "RLN-P4-C15-Formula1502",
        r"Ramanujan claims that the integral equations "
        r"$\int_0^\infty \varphi(x)\chi_1(nx)\,dx=\lambda\psi(n)$ and "
        r"$\int_0^\infty \psi(x)\chi_2(nx)\,dx=\lambda\varphi(n)$ imply each other; equivalently, "
        r"with $Z_1(s)=\int_0^\infty x^{s-1}\varphi(x)\,dx$ and $Z_2(s)=\int_0^\infty x^{s-1}\psi(x)\,dx$, "
        r"$\dfrac{Z_1(s)}{Z_2(1-s)}=\dfrac{X_2(s)}{\lambda}=\dfrac{\lambda}{X_1(1-s)}$.",
    ),
    rec(
        "RLN-P4-C15-Formula1503",
        r"If $\chi_1(x)=\chi_2(x)=\cos x$ or $\chi_1(x)=\chi_2(x)=\sin x$, then "
        r"$X_1(s)X_2(1-s)=\lambda^2=\dfrac{1}{2\pi}$. "
        r"If $\chi_1(x)=\chi_2(x)=J_\nu(x)/\sqrt{x}$ with $\Re\nu>-1$, then $\lambda=1$. "
        r"If $\chi_1(x)=\chi_2(x)=\dfrac{x^\nu}{1+x^2}$ with $\nu$ an integer, then $\lambda=\dfrac{\pi}{2}$.",
    ),
    rec(
        "RLN-P4-C15-Formula1504",
        r"Ramanujan gives self-reciprocal transform examples: "
        r"$\int_0^\infty e^{-x^2}\cos(2nx)\,dx=\dfrac{\sqrt{\pi}}{2}e^{-n^2}$, "
        r"$\int_0^\infty xe^{-x^2}\sin(2nx)\,dx=\dfrac{n\sqrt{\pi}}{2}e^{-n^2}$, "
        r"$\int_0^\infty x^{\nu+1/2}e^{-x^2}\sqrt{nx}\,J_\nu(2nx)\,dx=\dfrac{1}{2}n^{\nu+1/2}e^{-n^2}$, "
        r"and $\mathrm{PV}\int_0^\infty \dfrac{dx}{(1+x^2)(1-n^2x^2)}=\dfrac{\pi}{2(1+n^2)}$.",
    ),
    rec(
        "RLN-P4-C15-Formula1505",
        r"Given $X_1(s)$ with $X_1(s)X_2(1-s)$ constant, Ramanujan inverts by "
        r"$\chi_j(x)=\dfrac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty} x^{-s}X_j(s)\,ds$. "
        r"For $X_1(s)=X_2(s)=\Gamma(s)\cos\!\dfrac{\pi s}{2}$ or $\Gamma(s)\sin\!\dfrac{\pi s}{2}$, "
        r"$\chi_1(x)=\chi_2(x)=\cos x$ or $\sin x$, using "
        r"$\dfrac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty} x^{-s}\Gamma(s)\,ds=e^{-x}$.",
    ),
    rec(
        "RLN-P4-C15-Formula1506",
        r"Partitioning $0,1,\ldots,2g-1$ into $a_1,\ldots,a_g$ and $b_1,\ldots,b_g$, Ramanujan sets "
        r"$X_1(s)=\Gamma(s)\prod_{r=1}^g \sin\!\dfrac{\pi(s+a_r)}{2g}$ and "
        r"$X_2(s)=\Gamma(s)\prod_{r=1}^g \sin\!\dfrac{\pi(s-b_r+2g-1)}{2g}$, "
        r"so that $X_1(s)X_2(1-s)=\dfrac{\pi}{2^{2g-1}}$.",
    ),
    rec(
        "RLN-P4-C15-Formula1507",
        r"Ramanujan counts solutions of class $g$ by "
        r"$\omega_g=\sum_\delta \mu(\delta)\,\dfrac{(2g/\delta)!}{((g/\delta)!)^2}$, "
        r"where $\delta$ runs over divisors of $g$ and $\mu$ is the Möbius function; "
        r"for example $\omega_1=2$, $\omega_2=4$, $\omega_3=18$, $\omega_4=64$, $\omega_5=250$.",
    ),
    rec(
        "RLN-P4-C15-Formula1508",
        r"When $\chi_1(x)=\chi_2(x)=\chi(x)$ and $\varphi(x)=\psi(x)$ with $X(s)X(1-s)=\lambda^2$, "
        r"Ramanujan deduces $\int_0^\infty \varphi(x)\chi(nx)\,dx=\lambda\varphi(n)$, so "
        r"$\varphi$ is a self-reciprocal function with respect to the kernel $\chi$. "
        r"For $g=2$ with $a_1=0$, $a_2=1$, he finds "
        r"$\chi_1(x)=\chi_2(x)=e^{-x}-\cos x+\sin x$ with $\lambda=\sqrt{\pi}$.",
    ),
]
