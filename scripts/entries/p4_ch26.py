"""Part IV, Chapter 26 entries — inversion formulas (curated LaTeX)."""

from __future__ import annotations

TOPICS_C26 = ["inversion-formulas-lemniscate-and-allied-functions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C26}


CHAPTER_26 = [
    rec(
        "RN-P4-C26-Entry01",
        r"Let $0\le\theta\le\pi/2$ and $0\le v\le 1$. Define $\mu$ to be the constant obtained by setting "
        r"$\theta=\pi/2$ and $v=1$ in "
        r"$\displaystyle\frac{\theta\mu}{\sqrt{2}}=\int_0^v\frac{dt}{\sqrt{1-t^4}}"
        r"$=\displaystyle\sum_{n=0}^\infty\frac{(1/4)_n v^{4n+1}}{n!(4n+1)}$. "
        r"Then for $0<\theta\le\pi/2$, "
        r"$\displaystyle v=\frac{1}{\sqrt{2}}\,\mathrm{sd}(z\theta)=\frac{\mathrm{sn}(z\theta)}{\sqrt{2}\,\mathrm{dn}(z\theta)}$, "
        r"where $z=2K/\pi$ and $q=e^{-\pi}$.",
    ),
    rec(
        "RN-P4-C26-Entry02",
        r"With $\theta$, $v$, and $\mu$ as in Entry 1 and $0<\theta<\pi/2$, "
        r"$\displaystyle\frac{v}{\sqrt{2}}=\sum_{n=1}^\infty\frac{(4n)!}{(4n-1)!\,n!}\sin(2n\theta)$.",
    ),
    rec(
        "RN-P4-C26-Entry03",
        r"With $\theta$, $v$, and $\mu$ as in Entry 1 and $0<\theta\le\pi/2$, "
        r"$\displaystyle\log v+\frac{\pi}{6}-\log 2+\sum_{n=1}^\infty\frac{(1/4)_n v^{4n}}{(3/4)_n\,4n}"
        r"$=\log(\sin\theta)+\frac{\theta^2}{2\pi}-2\sum_{n=1}^\infty\frac{\cos(2n\theta)}{n(e^{2\pi n}-1)}"
        r"$+2\log f(-e^{-\pi})$, where $f(-q):=\prod_{n=1}^\infty(1-q^n)$ for $|q|<1$.",
    ),
    rec(
        "RN-P4-C26-Entry04",
        r"With $\theta$, $v$, and $\mu$ as in Entry 1 and $0\le\theta\le\pi/2$, "
        r"$\displaystyle\frac{1}{\sqrt{2}}\,\mathrm{sn}(z\theta)=\sum_{n=0}^\infty\frac{(-1)^n\cos\{(2n+1)\theta\}}{(2n+1)\cosh\{(2n+1)\pi/2\}}$.",
    ),
    rec(
        "RN-P4-C26-Entry05",
        r"With $\theta$, $v$, and $\mu$ as in Entry 1 and $0\le\theta\le\pi/2$, "
        r"$\displaystyle\frac{1}{\sqrt{2}}\,\mathrm{dn}(z\theta)=\sum_{n=0}^\infty\frac{(-1)^n\sin\{(2n+1)\theta\}}{(2n+1)\cosh\{(2n+1)\pi/2\}}$.",
    ),
    rec(
        "RN-P4-C26-Entry06",
        r"With $\theta$, $v$, and $\mu$ as in Entry 1 and $0<\theta\le\pi/2$, "
        r"$\displaystyle\frac{{}_2F_1(\tfrac14,\tfrac34;\tfrac32;v^4)}{\sqrt{1-v^4}}-\frac{\pi\theta}{2\mu}"
        r"$=\sum_{n=0}^\infty\frac{(-1)^n\sin\{(2n+1)\theta\}}{(2n+1)!(4n+3)}\frac{8}{(2n+1)^2\cosh\{(2n+1)\pi/2\}}$.",
    ),
    rec(
        "RN-P4-C26-Entry07",
        r"Let $0\le\theta\le\pi/2$ and $0\le v\le 1$. Put "
        r"$\displaystyle\frac{\theta\mu}{2}=\int_0^v\frac{dt}{\sqrt{1+t^4}}$, "
        r"where $\mu$ is the constant obtained by setting $\theta=\pi/2$ and $v=1$. Then "
        r"$\displaystyle\mathrm{am}(z\theta)=2\tan^{-1}v$, "
        r"equivalently "
        r"$\displaystyle 2\tan^{-1}v=\theta+\sum_{n=1}^\infty\frac{\sin(2n\theta)}{n\cosh(n\pi)}$, "
        r"where $z=2K/\pi$ and $q=e^{-\pi}$.",
    ),
    rec(
        "RN-P4-C26-Entry08",
        r"With $\theta$, $v$, and $\mu$ as in Entry 7 and $0<\theta\le\pi/2$, "
        r"$\displaystyle\frac{2\tan^{-1}v}{\sqrt{1+v^4}}=\sum_{n=0}^\infty\frac{(-1)^n\cos\{(2n+1)\theta\}}{(2n+1)\cosh\{(2n+1)\pi/2\}}$.",
    ),
    rec(
        "RN-P4-C26-Entry09",
        r"With $\theta$, $v$, and $\mu$ as in Entry 7 and $0<\theta\le\pi/2$, "
        r"$\displaystyle\frac{\sqrt{1+v^4}}{\sqrt{1-v^4}}=\sum_{n=0}^\infty\frac{(-1)^n\sin\{(2n+1)\theta\}}{(2n+1)(e^{(2n+1)\pi/2}-1)}$.",
    ),
    rec(
        "RN-P4-C26-Entry10",
        r"Let $0\le\theta\le\pi/2$ and $0\le x$. Define $\mu$ by setting $\theta=\pi/2$ and $x=\infty$ in "
        r"$\displaystyle\theta\mu=\int_0^x\frac{dt}{\sqrt{1-t^2+t^4}}$. "
        r"Let $\rho=e^{2\pi i/3}$. Then for $0<\theta\le\pi/2$, "
        r"$\displaystyle\wp(\theta;\pi,\rho\pi)=\frac{\pi^2}{6}+\csc^2\theta\sum_{n=1}^\infty\frac{n e^{-n\pi/3}\cos(2n\theta)}{1-e^{-2n\pi/3}}$.",
    ),
]
