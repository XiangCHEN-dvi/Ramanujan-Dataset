"""Part IV, Chapter 24 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C24 = ['ramanujan-theory-of-prime-numbers']


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C24}


CHAPTER_24 = [
    rec("RN-P4-C24-Entry01",
        r"For $A<B$, $\pi(B)-\pi(A)\approx\displaystyle\int_A^B\frac{dt}{\log t}$.",
    ),
    rec("RN-P4-C24-Entry02",
        r"For $x$ sufficiently large, $\pi'(x)<\dfrac{ex}{\log x}\,\pi(x/e)$.",
    ),
    rec("RN-P4-C24-Entry03",
        r"For $|x|<1$, $\displaystyle\sum_{k=1}^{\infty}x^k\log k=\sum_{p}\log p\sum_{i=1}^{\infty}\frac{x^{ip}}{1-x^p}$, where the outer sum is over all primes $p$.",
    ),
    rec("RN-P4-C24-Entry04",
        r"For $x>0$, $\displaystyle\sum_{k=1}^{\infty}(-1)^{k-1}e^{-kx}\log k=-\log2+2\sum_{\substack{p\\ p\text{ odd}}}\log p\sum_{r=1}^{\infty}\frac{e^{-prx}}{1-e^{-2prx}}$.",
    ),
    rec("RN-P4-C24-Entry05",
        r"As $s\to1^+$, $\displaystyle\sum_{p}\frac{\log p}{p^s}\sim\frac1{s-1}$, where the sum is over all primes $p$.",
    ),
    rec("RN-P4-C24-Entry06",
        r"Let $\mu(n)$ denote the Möbius function. For $\Re s>1$, $\displaystyle\sum_{n=1}^{\infty}\frac{\mu(n)}{n^s}+\sum_{n=1}^{\infty}\frac{\mu(n)}{n^s(n^s-1)}=\sum_{p}\frac{\log p}{p^s}+\sum_{n=1}^{\infty}\frac{\mu(n)}{n^s(n^s-1)}+f(s)$, where $f(s)$ is analytic for $\Re s>1$.",
    ),
    rec("RN-P4-C24-Entry07",
        r"For $\Re s>1$, $\displaystyle\int_1^x\frac{dt}{t^s}=\sum_{p}\frac{\log p}{p^s}+\sum_{n=1}^{\infty}\frac{\mu(n)}{n^s(n^s-1)}+f(s)$, where $f(s)$ is analytic for $\Re s>1$.",
    ),
    rec("RN-P4-C24-Entry08",
        r"As $x\to a$, $\dfrac{d}{dx}\sum_{n=1}^{\infty}\dfrac1{n\log x^{1/n}}=-\dfrac1{(x-a)^2\log x}$.",
    ),
    rec("RN-P4-C24-Entry09",
        r"If $x$ is a function of $n$ such that $\displaystyle\int_1^x e^{-at}\log x\,d\eta(x)=\dfrac1{a^2}$, then there are $n$ prime numbers between $1$ and $x$.",
    ),
    rec("RN-P4-C24-Entry10",
        r"For $x>0$, define $\varphi(x)=\sum_{p}\log p\sum_{k=1}^{\infty}e^{-pkx}=\log2+2\sum_{k=1}^{\infty}(-1)^{k-1}e^{-2kx}+\psi(x)$, where the sum on the left is over all primes $p$. Then $\displaystyle\sum_{k=1}^{\infty}(-1)^{k-1}\varphi(kx)=\sum_{n=1}^{\infty}(-1)^{n-1}e^{-nx}\log p_n$.",
    ),
    rec("RN-P4-C24-Entry11",
        r"As $x\to\infty$, $\pi(x)\approx\displaystyle\sum_{n=1}^{\infty}\dfrac{\mu(n)}{n}\,\Li(x^{1/n})=:R(x)$, where $\Li(x)=\int_\mu^x\dfrac{dt}{\log t}$ and $\mu=1.4513692349\ldots$ is Soldner's constant.",
    ),
    rec("RN-P4-C24-Entry12",
        r"As $x\to\infty$, $\pi(x)\approx\dfrac{x}{\log x}+\sum_{k=1}^{\infty}\dfrac{2k-1}{2k}\,\dfrac{B_{2k}}{2k}\,\left(\dfrac{x}{\log x}\right)^{2k}=:G(x)$, where $B_{2k}$ are Bernoulli numbers.",
    ),
    rec("RN-P4-C24-Entry13",
        r"Let $n$ be a positive integer, $\mu$ Soldner's constant, and $\delta=n-\log x$. Define $\theta=\theta(n)$ by $\Li(x^{1/n})=\dfrac{\log x}{n}+\dfrac{\theta}{n\log^{n-1}x}$. Then as $x\to\infty$, $\theta\approx\delta-\tfrac12\delta^2+\tfrac{1}{6}\delta^3-\tfrac{1}{12}\delta^4+\tfrac{1}{5}\delta^5-\tfrac{1}{6}\delta^6$.",
    ),
    rec("RN-P4-C24-Entry14",
        r"Let $\mu$ be Soldner's constant and $\gamma$ Euler's constant. Then $\Li(x)=\gamma+\log\log x+\sum_{k=1}^{\infty}\dfrac{\log^k x}{k!\,k}-\log\mu$.",
    ),
    rec("RN-P4-C24-Entry15",
        r"We have $\displaystyle\int_0^{\log x}\dfrac{(\log t)^k\,dt}{\Gamma(k+1)\,\zeta(k+1)}=:J(x)$, where $\zeta$ is the Riemann zeta-function.",
    ),
    rec("RN-P4-C24-Entry16",
        r"Let $\mu$ be Soldner's constant and $\gamma$ Euler's constant. Then $\Li(\sqrt x)=\sqrt x\sum_{k=0}^{\infty}\dfrac{(-1)^k\log^k x}{(2k)!}\left(\gamma-1+\log4+\sum_{j=1}^{k}\dfrac1j\right)$.",
    ),
    rec("RN-P4-C24-Entry17",
        r"For $x>1$, $\dfrac{2\pi}{\log2}\,\log x\approx\Bigl(1+0.0000098844\cos\bigl(\dfrac{2\pi\log x}{\log2}+0.872711\bigr)\Bigr)\sum_{k=\pm1}\dfrac{x^{-2k\pi i/\log2}}{1+2k\pi i/\log2}$.",
    ),
]
