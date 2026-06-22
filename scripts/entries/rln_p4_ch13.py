"""RLN Part 4, Chapter 13 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C13 = ["fourier-laplace-transforms"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C13}


CHAPTER_13 = [
    rec(
        "RLN-P4-C13-Entry13-2-1",
        r"If $\displaystyle\int_0^{\infty}f(x)\sin(nx)\,dx=:\varphi(n)$ and "
        r"$\displaystyle\int_0^{\infty}f(x)e^{-nx}\,dx=:\psi(n)$, then "
        r"$\displaystyle\int_0^{\infty}\varphi(x)e^{-nx}\,dx=\int_0^{\infty}\psi(x)\cos(nx)\,dx$ and "
        r"$\displaystyle\int_0^{\infty}\varphi\!\left(\frac{1}{x}\right)e^{-nx}\,dx"
        r"=-\int_0^{\infty}\psi\!\left(\frac{1}{x}\right)\cos(nx)\,dx$.",
    ),
    rec(
        "RLN-P4-C13-Entry13-2-2",
        r"If $\displaystyle\int_0^{\infty}f(x)\cos(nx)\,dx=:\varphi(n)$ and "
        r"$\displaystyle\int_0^{\infty}f(x)e^{-nx}\,dx=:\psi(n)$, then "
        r"$\displaystyle\int_0^{\infty}\varphi(x)e^{-nx}\,dx=\int_0^{\infty}\psi(x)\sin(nx)\,dx$ and "
        r"$\displaystyle\int_0^{\infty}\varphi\!\left(\frac{1}{x}\right)e^{-nx}\,dx"
        r"=\int_0^{\infty}\psi\!\left(\frac{1}{x}\right)\sin(nx)\,dx$.",
    ),
    rec(
        "RLN-P4-C13-Entry13-2-3",
        r"If $\displaystyle\int_0^{\infty}\varphi(x)\sin(nx)\,dx=\sqrt{\frac{\pi}{2}}\,\varphi(n)$ and "
        r"$\displaystyle\int_0^{\infty}\varphi(x)e^{-nx}\,dx=:\psi(n)$, then "
        r"$\displaystyle\int_0^{\infty}\psi(x)\cos(nx)\,dx=\sqrt{\frac{\pi}{2}}\,\psi(n)$. "
        r"If $\displaystyle\int_0^{\infty}\varphi(x)\cos(nx)\,dx=\sqrt{\frac{\pi}{2}}\,\varphi(n)$ and "
        r"$\displaystyle\int_0^{\infty}\varphi(x)e^{-nx}\,dx=:\psi(n)$, then "
        r"$\displaystyle\int_0^{\infty}\psi(x)\sin(nx)\,dx=\sqrt{\frac{\pi}{2}}\,\psi(n)$.",
    ),
    rec(
        "RLN-P4-C13-Entry13-2-4",
        r"For $n>0$, "
        r"$\displaystyle\int_0^{\infty}\left(\frac{1}{e^{2\pi x}-1}-\frac{1}{2\pi x}\right)\sin(2\pi nx)\,dx"
        r"=\frac{1}{2}\left(\frac{1}{e^{2\pi n}-1}-\frac{1}{2\pi n}\right)$.",
    ),
    rec(
        "RLN-P4-C13-Entry13-2-5",
        r"For $n>0$, "
        r"$\displaystyle\int_0^{\infty}\left(\frac{1}{e^{2\pi x}-1}-\frac{1}{2\pi x}\right)e^{-2\pi nx}\,dx"
        r"=\frac{1}{2\pi}(\log n-\psi(1+n))$, where $\psi$ denotes the digamma function.",
    ),
    rec(
        "RLN-P4-C13-Entry13-2-6",
        r"If $n>0$, "
        r"$\displaystyle\int_0^{\infty}(\psi(1+x)-\log x)\cos(2\pi nx)\,dx"
        r"=\frac{1}{2}(\psi(1+n)-\log n)$, where $\psi$ denotes the digamma function.",
    ),
    rec(
        "RLN-P4-C13-Entry13-2-7",
        r"For real $n$, "
        r"$\displaystyle\int_0^{\infty}\frac{\cos(\pi nx/2)}{\cosh(\pi x/2)}\,dx=\frac{1}{\cosh(\pi n/2)}$.",
    ),
    rec(
        "RLN-P4-C13-Entry13-2-8",
        r"For $n>0$, "
        r"$\displaystyle\int_0^{\infty}\frac{e^{-\pi nx/2}}{\cosh(\pi x/2)}\,dx"
        r"=\frac{4}{\pi}\sum_{k=0}^{\infty}\frac{(-1)^k}{n+2k+1}$.",
    ),
    rec(
        "RLN-P4-C13-Entry13-2-9",
        r"For $n>0$, "
        r"$\displaystyle\int_0^{\infty}\sum_{k=0}^{\infty}\frac{(-1)^k}{x+2k+1}\sin\!\left(\frac{\pi nx}{2}\right)\,dx"
        r"=\sum_{k=0}^{\infty}\frac{(-1)^k}{n+2k+1}$.",
    ),
    rec(
        "RLN-P4-C13-Entry13-3-1",
        r"Define $\varphi(x):=\psi(x)+\dfrac{1}{2x}-\log x$, where $\psi$ denotes the digamma function. "
        r"If $\alpha$ and $\beta$ are positive numbers such that $\alpha\beta=1$, then "
        r"$\sqrt{\alpha}\!\left(\dfrac{\gamma-\log(2\pi\alpha)}{2\alpha}+\displaystyle\sum_{n=1}^{\infty}\varphi(n\alpha)\right)"
        r"=\sqrt{\beta}\!\left(\dfrac{\gamma-\log(2\pi\beta)}{2\beta}+\sum_{n=1}^{\infty}\varphi(n\beta)\right)"
        r"=-\dfrac{1}{\pi^{3/2}}\displaystyle\int_0^{\infty}"
        r"\frac{\left|\Xi\!\left(\dfrac{1}{2t}\right)\Gamma\!\left(-\dfrac{1}{4}+\dfrac{it}{4}\right)\right|^2"
        r"\cos\!\left(\dfrac{t}{2}\log\alpha\right)}{1+t^2}\,dt$, "
        r"where $\gamma$ denotes Euler's constant and $\Xi(t):=\xi\!\left(\dfrac{1}{2}+it\right)$ with "
        r"$\xi(s):=(s-1)\pi^{-s/2}\Gamma\!\left(1+\dfrac{s}{2}\right)\zeta(s)$.",
    ),
]
