"""RLN Part 4, Chapter 4 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C04 = ["gamma-function-theorems"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C04}


CHAPTER_4 = [
    rec(
        "RLN-P4-C04-Entry4-2-1",
        r"If $a>0$ and $k\ge0$, then "
        r"$\displaystyle\int_0^{\infty}\dfrac{a^x x^k}{\Gamma(x+1)}\,dx"
        r"+\displaystyle\int_0^{\infty}\dfrac{e^{-ax}x^{k-1}}{\pi^2+\log^2 x}"
        r"\left(\cos(\pi k)-\dfrac{1}{\pi}\sin(\pi k)\log x\right)dx=e^a$.",
    ),
    rec(
        "RLN-P4-C04-Entry4-2-2",
        r"If $a>0$ and $k\ge0$, then "
        r"$\displaystyle\int_0^{\infty}\dfrac{a^x x^k}{\Gamma(x+1)}\,dx"
        r"+\dfrac{1}{2\pi}\displaystyle\int_0^{\infty}"
        r"\left(\dfrac{e^{i\pi(k+ix)}a^{k+ix}}{\Gamma(k+ix)}"
        r"+\dfrac{e^{-i\pi(k-ix)}a^{k-ix}}{\Gamma(k-ix)}\right)dx=e^a$.",
    ),
    rec(
        "RLN-P4-C04-Entry4-2-3",
        r"If $a>0$, $0\le\lambda<\epsilon$, and $1/\epsilon$ is a positive integer, then "
        r"$\epsilon\displaystyle\sum_{n=0}^{\infty}\dfrac{a^{\lambda+n\epsilon}}{\Gamma(1+\lambda+n\epsilon)}"
        r"=e^a-\dfrac{\epsilon}{\pi}\displaystyle\int_0^{\infty}e^{-ax}x^{-\lambda-1}"
        r"\dfrac{\sin(\pi(\lambda-\epsilon))-x^\epsilon\sin(\pi\lambda)}{2\cos(\pi\epsilon)-(x^\epsilon+x^{-\epsilon})}\,dx$.",
    ),
    rec(
        "RLN-P4-C04-Entry4-5-1",
        r"If $x\ge0$, then "
        r"$\Gamma(1+x)=\sqrt{\pi}\left(\dfrac{x}{e}\right)^x\bigl(8x^3+4x^2+x+\theta_x\bigr)^{1/6}$, "
        r"where $\theta_0=\tfrac{30}{\pi^3}$, $\theta_{1/12}=0.8071$, $\theta_{7/12}=0.3058$, "
        r"$\theta_{2/12}=0.6160$, $\theta_{8/12}=0.3014$, $\theta_{3/12}=0.4867$, $\theta_{9/12}=0.3041$, "
        r"$\theta_{4/12}=0.4029$, $\theta_{10/12}=0.3118$, $\theta_{5/12}=0.3509$, $\theta_{11/12}=0.3227$, "
        r"$\theta_{6/12}=0.3207$, $\theta_1=0.3359$, and $\theta_\infty=1$. "
        r"Moreover, "
        r"$\sqrt{\pi}\left(\dfrac{x}{e}\right)^x\bigl(8x^3+4x^2+x+\tfrac{1}{100}\bigr)^{1/6}"
        r"<\Gamma(x+1)"
        r"<\sqrt{\pi}\left(\dfrac{x}{e}\right)^x\bigl(8x^3+4x^2+x+\tfrac{1}{30}\bigr)^{1/6}$.",
    ),
    rec(
        "RLN-P4-C04-Entry4-9-1",
        r"If $0<a<b-\tfrac{1}{2}$, then "
        r"$\displaystyle\int_0^{\infty}"
        r"\dfrac{1+x^2/b^2}{1+x^2/a^2}\cdot\dfrac{1+x^2/(b+1)^2}{1+x^2/(a+1)^2}"
        r"\cdot\dfrac{1+x^2/(b+2)^2}{1+x^2/(a+2)^2}\cdots\,dx"
        r"=\dfrac{\sqrt{\pi}}{2}\,"
        r"\dfrac{\Gamma(a+\tfrac{1}{2})\Gamma(b)\Gamma(b-a-\tfrac{1}{2})}"
        r"{\Gamma(a)\Gamma(b-\tfrac{1}{2})\Gamma(b-a)}$.",
    ),
    rec(
        "RLN-P4-C04-Entry4-9-2",
        r"If $a,b>0$, then "
        r"$\displaystyle\int_0^{\infty}\dfrac{dx}"
        r"\{1+x^2/a^2\}\{1+x^2/(a+1)^2\}\cdots\{1+x^2/b^2\}\{1+x^2/(b+1)^2\}\cdots}"
        r"=\dfrac{\sqrt{\pi}}{2}\,"
        r"\dfrac{\Gamma(a+\tfrac{1}{2})\Gamma(b+\tfrac{1}{2})\Gamma(a+b)}"
        r"{\Gamma(a)\Gamma(b)\Gamma(a+b+\tfrac{1}{2})}$.",
    ),
    rec(
        "RLN-P4-C04-Entry4-9-3",
        r"If either $\operatorname{Re}(a+b)>\tfrac{3}{2}$, or $2(a-b)$ is an odd integer and "
        r"$\operatorname{Re}(a+b)>1$, then "
        r"$\displaystyle\int_0^{\infty}\dfrac{dx}{\Gamma(a+x)\Gamma(a-x)\Gamma(b+x)\Gamma(b-x)}"
        r"=\dfrac{\Gamma(2a+2b-3)}{2\Gamma(2a-1)\Gamma(2b-1)\{\Gamma(a+b-1)\}^2}$.",
    ),
    rec(
        "RLN-P4-C04-Entry4-9-4",
        r"If $\operatorname{Re}\,a>\tfrac{1}{2}$, then "
        r"$\displaystyle\int_0^{\infty}\dfrac{dx}{\Gamma(a+x)\Gamma(a-x)}=\dfrac{2^{2a-3}}{\Gamma(2a-1)}$.",
    ),
    rec(
        "RLN-P4-C04-Entry4-9-5",
        r"If $n>0$, then the principal value "
        r"$\displaystyle\int_0^{\infty}\dfrac{\cos(nx)}{1-x^2}\,dx=\dfrac{\pi}{2\sin n}$.",
    ),
]
