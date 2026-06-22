"""RLN Part 5, Chapter 12 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C12 = ["tenth-order-mock-theta-transformations"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C12}


CHAPTER_12 = [
    rec(
        "RLN-P5-C12-Entry12-1-1",
        r"If $\varphi_{10}(q)$ and $\psi_{10}(q)$ are defined by (12.1.1) and $n>0$, then "
        r"$\displaystyle\int_0^{\infty}e^{-\pi n x^2}\cosh\!\left(\dfrac{2\pi x}{\sqrt{5}+1}+\dfrac{\sqrt{5}}{4}\right)\,dx"
        r"+\dfrac{1}{\sqrt{n}}\,e^{\pi/(5n)}\,\psi_{10}(-e^{-\pi/n})"
        r"=\dfrac{\sqrt{5+\sqrt{5}}}{2}\,e^{-\pi n/5}\,\varphi_{10}(-e^{-\pi n})"
        r"-\dfrac{\sqrt{5}+1}{2\sqrt{n}}\,e^{-\pi/(5n)}\,\varphi_{10}(-e^{-\pi/n})$.",
    ),
    rec(
        "RLN-P5-C12-Entry12-1-2",
        r"If $\varphi_{10}(q)$ and $\psi_{10}(q)$ are defined by (12.1.1) and $n>0$, then "
        r"$\displaystyle\int_0^{\infty}e^{-\pi n x^2}\cosh\!\left(\dfrac{2\pi x}{\sqrt{5}+1}-\dfrac{\sqrt{5}}{4}\right)\,dx"
        r"+\dfrac{1}{\sqrt{n}}\,e^{\pi/(5n)}\,\psi_{10}(-e^{-\pi/n})"
        r"=-\dfrac{\sqrt{5-\sqrt{5}}}{2}\,e^{\pi n/5}\,\psi_{10}(-e^{-\pi n})"
        r"+\dfrac{\sqrt{5}-1}{2\sqrt{n}}\,e^{-\pi/(5n)}\,\varphi_{10}(-e^{-\pi/n})$.",
    ),
    rec(
        "RLN-P5-C12-Entry12-3-1",
        r"If $\varphi_{10}(q)$ and $\psi_{10}(q)$ are defined by (12.1.1) and $n>0$, then "
        r"$\displaystyle\int_0^{\infty}e^{-\pi n x^2}\cosh\!\left(\dfrac{2\pi x}{\sqrt{5}+1}+\dfrac{\sqrt{5}}{4}\right)\,dx"
        r"+\dfrac{1}{\sqrt{n}}\,e^{\pi/(5n)}\,\psi_{10}(-e^{-\pi/n})"
        r"=\dfrac{\sqrt{5+\sqrt{5}}}{2}\,e^{-\pi n/5}\,\varphi_{10}(-e^{-\pi n})"
        r"-\dfrac{\sqrt{5}+1}{2\sqrt{n}}\,e^{-\pi/(5n)}\,\varphi_{10}(-e^{-\pi/n})$.",
    ),
    rec(
        "RLN-P5-C12-Entry12-4-1",
        r"If $\varphi_{10}(q)$ and $\psi_{10}(q)$ are defined by (12.1.1) and $n>0$, then "
        r"$\displaystyle\int_0^{\infty}e^{-\pi n x^2}\cosh\!\left(\dfrac{2\pi x}{\sqrt{5}+1}-\dfrac{\sqrt{5}}{4}\right)\,dx"
        r"+\dfrac{1}{\sqrt{n}}\,e^{\pi/(5n)}\,\psi_{10}(-e^{-\pi/n})"
        r"=-\dfrac{\sqrt{5-\sqrt{5}}}{2}\,e^{\pi n/5}\,\psi_{10}(-e^{-\pi n})"
        r"+\dfrac{\sqrt{5}-1}{2\sqrt{n}}\,e^{-\pi/(5n)}\,\varphi_{10}(-e^{-\pi/n})$.",
    ),
]
