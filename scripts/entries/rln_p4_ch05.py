"""RLN Part 4, Chapter 5 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C05 = ["hypergeometric-series-lost-notebook"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C05}


CHAPTER_5 = [
    rec(
        "RLN-P4-C05-Entry5-1-1",
        r"Let $\alpha$, $\beta$, $\gamma$, $\delta$, and $\xi$ be complex numbers with "
        r"$\operatorname{Re}(\alpha+\beta+\gamma+\delta)>3$. Then "
        r"$\displaystyle\sum_{n=-\infty}^{\infty}"
        r"\dfrac{\xi+2n}{\Gamma(\alpha+\xi+n)\Gamma(\beta-\xi-n)\Gamma(\gamma+\xi+n)\Gamma(\delta-\xi-n)}"
        r"\cdot\dfrac{1}{\Gamma(\beta+n)\Gamma(\gamma-n)\Gamma(\delta+n)}"
        r"=\dfrac{\sin(\pi\xi)\,\Gamma(\alpha+\beta+\gamma+\delta-3)}{\pi\,\Gamma(\alpha+\gamma+\xi-1)\Gamma(\beta+\delta-\xi-1)}"
        r"\cdot\dfrac{1}{\Gamma(\alpha+\beta-1)\Gamma(\beta+\gamma-1)\Gamma(\gamma+\delta-1)\Gamma(\delta+\alpha-1)}$.",
    ),
    rec(
        "RLN-P4-C05-Entry5-1-2",
        r"Define, for real $s$ and $\theta$ with $0<\theta<2\pi$ and complex $\alpha$, $\beta$, $\gamma$, $\delta$ "
        r"with $\operatorname{Re}(\alpha+\beta+\gamma+\delta)>4$, "
        r"$\phi_s(\theta):=\displaystyle\sum_{n=-\infty}^{\infty}"
        r"\dfrac{e^{(n+s)i\theta}}{\Gamma(\alpha+s+n)\Gamma(\beta-s-n)\Gamma(\gamma+s+n)\Gamma(\delta-s-n)}$. "
        r"Then "
        r"$\dfrac{d}{d\theta}\dfrac{\phi_s(\theta)}{\phi_t(\theta)}"
        r"=i\sin\{\pi(s-t)\}\left(2\sin\dfrac{\theta}{2}\right)^{\alpha+\beta+\gamma+\delta-4}"
        r"\dfrac{e^{i(\pi-\theta)(\alpha-\beta+\gamma-\delta+2s+2t)/2}}"
        r"{\pi\,\phi_t^2(\theta)\,\Gamma(\alpha+\beta-1)\Gamma(\beta+\gamma-1)\Gamma(\gamma+\delta-1)\Gamma(\delta+\alpha-1)}$.",
    ),
    rec(
        "RLN-P4-C05-Entry5-1-3",
        r"Let $\phi(a,x):=\dfrac{1}{1+\dfrac{x}{a+1}\left(1+\dfrac{x}{a+3}\left(1+\dfrac{x}{a+5}\left(1+\cdots\right)\right)\right)}$. "
        r"If $a+1>0$, $b+1>0$, and $s$ is not purely imaginary, then "
        r"$\displaystyle\int_0^{\infty}\dfrac{\phi(a,x)\phi(b,x)}{1+s^2x^2}\,dx"
        r"=\dfrac{2\sqrt{\pi}\,\Gamma\!\bigl(\tfrac{1+a}{2}\bigr)\Gamma\!\bigl(\tfrac{1+b}{2}\bigr)\Gamma\!\bigl(\tfrac{1+a+b}{2}\bigr)}"
        r"{\Gamma\!\bigl(\tfrac{a}{2}\bigr)\Gamma\!\bigl(\tfrac{b}{2}\bigr)\Gamma\!\bigl(\tfrac{a+b}{2}\bigr)}"
        r"\times\dfrac{1}{a+b+1+\dfrac{1\cdot(a+1)(b+1)(a+b+1)s^2}{a+b+3+\dfrac{2(a+2)(b+2)(a+b+2)s^2}{a+b+5+\cdots}}}$.",
    ),
    rec(
        "RLN-P4-C05-Entry5-1-4",
        r"If $s=1$, the continued fraction in Entry 5.1.3 equals "
        r"$\dfrac{1}{a+b+1+\dfrac{1\cdot(a+1)(b+1)(a+b+1)}{a+b+3+\dfrac{2(a+2)(b+2)(a+b+2)}{a+b+5+\cdots}}}"
        r"$=\dfrac{1}{a+b+1}\bigl(1-A_1+A_1A_2-A_1A_2A_3+\cdots\bigr)$, "
        r"where "
        r"$A_t:=\dfrac{(a+t)(b+t)-ab\cos^2(\pi t/2)}{(a+1+t)(b+1+t)-ab\cos^2(\pi t/2)}$.",
    ),
    rec(
        "RLN-P4-C05-Entry5-1-5",
        r"Let $\varphi(\alpha,x):=\dfrac{1}{1+\bigl(\tfrac{x}{\alpha}\bigr)^2\left(1+\bigl(\tfrac{x}{\alpha+1}\bigr)^2\left(1+\bigl(\tfrac{x}{\alpha+2}\bigr)^2\left(1+\cdots\right)\right)\right)}$. "
        r"If $\alpha>0$, $\beta>0$, and $s$ is not purely imaginary, then "
        r"$\displaystyle\int_0^{\infty}\dfrac{\varphi(\alpha,x)\varphi(\beta,x)}{1+4s^2x^2}\,dx"
        r"=\dfrac{\sqrt{\pi}\,\Gamma\!\bigl(\alpha+\tfrac{1}{2}\bigr)\Gamma\!\bigl(\beta+\tfrac{1}{2}\bigr)\Gamma(\alpha+\beta)}"
        r"{\Gamma(\alpha)\Gamma(\beta)\Gamma(\alpha+\beta+\tfrac{1}{2})}\,\chi_1(s)$, "
        r"where "
        r"$\chi_1(s):=\dfrac{1}{2}+\dfrac{2\cdot1\cdot(2\alpha)(2\beta)s^2}{2\alpha+2\beta+1}"
        r"+\dfrac{2(2\alpha+1)(2\beta+1)(2\alpha+2\beta)s^2}{2\alpha+2\beta+3}"
        r"+\dfrac{3(2\alpha+2)(2\beta+2)(2\alpha+2\beta+1)s^2}{2\alpha+2\beta+5}+\cdots$.",
    ),
    rec(
        "RLN-P4-C05-Entry5-5-1",
        r"Let $W_N(x):=\dfrac{\Gamma(\alpha+\beta+\tfrac{1}{2})\,|\Gamma(\alpha+ix)\Gamma(\beta+ix)|^2}"
        r"{\sqrt{\pi}\,\Gamma(\alpha)\Gamma(\alpha+\tfrac{1}{2})\Gamma(\beta)\Gamma(\beta+\tfrac{1}{2})\Gamma(\alpha+\beta)}$. "
        r"If $\alpha>0$ and $\beta>0$, then "
        r"$\displaystyle\int_0^{\infty}\dfrac{W_N(x)}{1+4s^2x^2}\,dx"
        r"=\dfrac{1}{2}+\dfrac{2(2\alpha)(2\beta)s^2}{2\alpha+2\beta+1}"
        r"+\dfrac{2(2\alpha+1)(2\beta+1)(2\alpha+2\beta)s^2}{2\alpha+2\beta+3}+\cdots$.",
    ),
]
