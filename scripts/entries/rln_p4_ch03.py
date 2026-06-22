"""RLN Part 4, Chapter 3 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C03 = ["koshliakov-guinand-formulas"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C03}


CHAPTER_3 = [
    rec(
        "RLN-P4-C03-Entry3-1-1",
        r"Let $\sigma_k(n):=\sum_{d\mid n}d^k$ and let $\zeta(s)$ denote the Riemann zeta function. "
        r"If $\alpha$ and $\beta$ are positive with $\alpha\beta=\pi^2$ and $s$ is any complex number, then "
        r"$\sqrt{\alpha}\displaystyle\sum_{n=1}^{\infty}\sigma_{-s}(n)\,n^{s/2}K_{s/2}(2n\alpha)"
        r"-\sqrt{\beta}\displaystyle\sum_{n=1}^{\infty}\sigma_{-s}(n)\,n^{s/2}K_{s/2}(2n\beta)"
        r"=\dfrac{1}{4\Gamma\!\bigl(\tfrac{s}{2}\bigr)}\,\zeta(s)\bigl(\beta^{(1-s)/2}-\alpha^{(1-s)/2}\bigr)"
        r"+\dfrac{1}{4\Gamma\!\bigl(-\tfrac{s}{2}\bigr)}\,\zeta(-s)\bigl(\beta^{(1+s)/2}-\alpha^{(1+s)/2}\bigr)$.",
    ),
    rec(
        "RLN-P4-C03-Entry3-3-1",
        r"Let $\sigma_k(n):=\sum_{d\mid n}d^k$ and let $\zeta(s)$ denote the Riemann zeta function. "
        r"If $\alpha$ and $\beta$ are positive with $\alpha\beta=\pi^2$ and $s$ is any complex number, then "
        r"$\sqrt{\alpha}\displaystyle\sum_{n=1}^{\infty}\sigma_{-s}(n)\,n^{s/2}K_{s/2}(2n\alpha)"
        r"-\sqrt{\beta}\displaystyle\sum_{n=1}^{\infty}\sigma_{-s}(n)\,n^{s/2}K_{s/2}(2n\beta)"
        r"=\dfrac{1}{4\Gamma\!\bigl(\tfrac{s}{2}\bigr)}\,\zeta(s)\bigl(\beta^{(1-s)/2}-\alpha^{(1-s)/2}\bigr)"
        r"+\dfrac{1}{4\Gamma\!\bigl(-\tfrac{s}{2}\bigr)}\,\zeta(-s)\bigl(\beta^{(1+s)/2}-\alpha^{(1+s)/2}\bigr)$.",
    ),
    rec(
        "RLN-P4-C03-Entry3-3-2",
        r"Let $\alpha$ and $\beta$ be positive with $\alpha\beta=\pi^2$. Then "
        r"$\displaystyle\sum_{n=1}^{\infty}\sigma_{-1}(n)e^{-2n\alpha}"
        r"-\displaystyle\sum_{n=1}^{\infty}\sigma_{-1}(n)e^{-2n\beta}"
        r"=\dfrac{\beta-\alpha}{12}+\dfrac{1}{4}\log\dfrac{\alpha}{\beta}$.",
    ),
    rec(
        "RLN-P4-C03-Entry3-3-3",
        r"Let $\alpha$ and $\beta$ be positive with $\alpha\beta=\pi^2$, and let $\gamma$ denote Euler's constant. Then "
        r"$\sqrt{\alpha}\left(\dfrac{1}{4}\gamma-\dfrac{1}{4}\log(4\beta)+\displaystyle\sum_{n=1}^{\infty}d(n)K_0(2n\alpha)\right)"
        r"=\sqrt{\beta}\left(\dfrac{1}{4}\gamma-\dfrac{1}{4}\log(4\alpha)+\displaystyle\sum_{n=1}^{\infty}d(n)K_0(2n\beta)\right)$.",
    ),
    rec(
        "RLN-P4-C03-Entry3-4-1",
        r"If $a>0$, then "
        r"$\displaystyle\int_0^{\infty}\dfrac{dx}{x(e^{2\pi x}-1)(e^{2\pi a/x}-1)}"
        r"=2\displaystyle\sum_{n=1}^{\infty}d(n)K_0(4\pi\sqrt{an})"
        r"=\dfrac{a}{\pi^2}\displaystyle\sum_{n=1}^{\infty}\dfrac{d(n)\log(a/n)}{a^2-n^2}"
        r"-\dfrac{1}{2}\gamma-\left(\dfrac{1}{4}+\dfrac{1}{4\pi^2 a}\right)\log a"
        r"-\dfrac{\log(2\pi)}{2\pi^2 a}$.",
    ),
    rec(
        "RLN-P4-C03-Entry3-4-2",
        r"If $a>0$, then "
        r"$\displaystyle\sum_{n=1}^{\infty}\sigma_{-1/2}(n)e^{-2\pi\sqrt{an}}"
        r"=K\,\displaystyle\sum_{n=1}^{\infty}\dfrac{\sigma_{-1/2}(n)}{(n+a)(\sqrt{n}+\sqrt{a})}$ "
        r"plus two unspecified trivial terms, where $K$ is an unspecified constant.",
    ),
    rec(
        "RLN-P4-C03-Entry3-4-3",
        r"If $a>0$, then "
        r"$\displaystyle\sum_{n=1}^{\infty}\sigma_{-1/2}(n)e^{-4\pi\sqrt{an}}"
        r"-\dfrac{a}{\pi}\displaystyle\sum_{n=1}^{\infty}\dfrac{\sigma_{-1/2}(n)}{(n+a)(\sqrt{n}+\sqrt{a})}"
        r"=\dfrac{1}{2\zeta\!\left(\tfrac{1}{2}\right)}\left(\dfrac{1}{\pi\sqrt{a}}-1\right)"
        r"+\dfrac{1}{2\zeta\!\left(-\tfrac{1}{2}\right)}\left(\dfrac{4\pi\sqrt{a}-1}{\pi a}\right)$.",
    ),
    rec(
        "RLN-P4-C03-Entry3-4-4",
        r"If $a>0$, then "
        r"$\displaystyle\int_0^{\infty}\dfrac{dx}{(e^{2\pi x}-1)(e^{2\pi a/x}-1)}"
        r"=2\sqrt{a}\displaystyle\sum_{n=1}^{\infty}\sigma_{-1}(n)\sqrt{n}\,K_1(4\pi\sqrt{an})$.",
    ),
    rec(
        "RLN-P4-C03-Entry3-4-5",
        r"If $a>0$ and $\gamma$ denotes Euler's constant, then "
        r"$2\sqrt{a}\displaystyle\sum_{n=1}^{\infty}\sigma_{-1}(n)\sqrt{n}\,K_1(4\pi\sqrt{an})"
        r"=-\dfrac{a^2}{2\pi}\displaystyle\sum_{n=1}^{\infty}\dfrac{\sigma_{-1}(n)}{n(n+a)}"
        r"+\dfrac{a}{2\pi}\bigl((\log a+\gamma)\zeta(2)+\zeta'(2)\bigr)"
        r"+\dfrac{1}{4\pi}(\log(2a\pi)+\gamma)+\dfrac{1}{48a\pi}$.",
    ),
]
