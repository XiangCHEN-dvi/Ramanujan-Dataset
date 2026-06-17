"""Part V, Chapter 39 entries — miscellaneous results in the first notebook (curated LaTeX)."""

from __future__ import annotations

TOPICS_C39 = ["miscellaneous-results-first-notebook"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C39}


CHAPTER_39 = [
    rec(
        "RN-P5-C39-Entry01",
        r"If $\displaystyle f(x):=\sum_{n=1}^{\infty}\varphi(nx)$, then "
        r"$\displaystyle\sum_{n=1}^{\infty}\varphi(nh)=\sum_{r=1}^{\infty}\Omega(r)\,\varphi(rh)$, "
        r"where $\Omega(1)=0$ and, for $n>1$, $\Omega(n)$ denotes the total number of prime factors of $n$ counting multiplicities.",
    ),
    rec(
        "RN-P5-C39-Entry02",
        r"If $n$ is a positive integer, then "
        r"$\displaystyle\int_0^{\infty}\frac{\sin^n x}{x^n}\,dx"
        r"=\frac{\sqrt{\pi}\,\Gamma\bigl(\tfrac{n-1}{2}\bigr)}{2\,\Gamma\bigl(\tfrac{n}{2}\bigr)}$, "
        r"where the plus sign is taken if $n$ is even and the minus sign if $n$ is odd.",
    ),
    rec(
        "RN-P5-C39-Entry03",
        r"For $0<x<1$, "
        r"${}_2F_1\!\left(\tfrac13,\tfrac23;1;-x\right)=\tfrac{3}{2\sqrt3}\left\{\left(\sqrt{1+x}+\sqrt{x}\right)^{-1/3}+\left(\sqrt{1+x}-\sqrt{x}\right)^{-1/3}\right\}$ "
        r"and "
        r"${}_2F_1\!\left(\tfrac13,\tfrac23;1;x\right)=\tfrac{3}{2\sqrt3}\left\{\left(\sqrt{1+x}+\sqrt{x}\right)^{1/3}+\left(\sqrt{1+x}-\sqrt{x}\right)^{1/3}\right\}$.",
    ),
    rec(
        "RN-P5-C39-Entry04",
        r"Let $x$ and $y$ be complex numbers such that $x/y$ is not purely imaginary. Let $\varphi(z)$ be an entire function such that "
        r"$f(z):=\pi\sec(\pi xz)\,\mathrm{sech}(\pi yz)\{\varphi(xyz)-\varphi(-xyz)\}$ tends to $0$ as $z\to\infty$. Then "
        r"$\displaystyle\pi\sec(\pi x)\,\mathrm{sech}(\pi y)\{\varphi(xy)-\varphi(-xy)\}"
        r"=\sum_{n=0}^{\infty}(-1)^n\,\mathrm{sech}\!\left(\frac{\pi(2n+1)y}{2x}\right)\frac{\varphi((2n+1)y)-\varphi(-(2n+1)y)}{(2n+1)^2-x^2}"
        r"+\sum_{n=0}^{\infty}(-1)^n\,\mathrm{sech}\!\left(\frac{\pi(2n+1)x}{2y}\right)\frac{\varphi(i(2n+1)x)-\varphi(-i(2n+1)x)}{(2n+1)^2+y^2}$.",
    ),
    rec(
        "RN-P5-C39-Entry05",
        r"If $x$ is not an integer and $0<\theta<2\pi$, then "
        r"$\displaystyle\pi\{\cot(\pi x)\cos(\theta x)+\sin(\theta x)\}=\theta-2\sum_{n=1}^{\infty}\frac{(-1)^n\cos(n\theta)}{n^2-x^2}$.",
    ),
    rec(
        "RN-P5-C39-Entry06",
        r"The maximum value of $a^x/\Gamma(x+1)$ equals "
        r"$\displaystyle\frac{a^{a-1/2}}{\Gamma(a+\tfrac12)}\left\{1+\frac{1}{1152\pi a^3}+\frac{323.2}{a}+\cdots\right\}$ very nearly.",
    ),
    rec(
        "RN-P5-C39-Entry07",
        r"Let $m$ and $n$ be integers with $0<m<n$, and let $\rho$ be real. Then "
        r"$\displaystyle\frac{\Gamma(m+\rho)\,\Gamma(n-m-i\rho)}{\Gamma(m)\,\Gamma(n-m)}"
        r"=\exp\!\left(i\sum_{k=0}^{m-1}\arctan\frac{\rho}{m+k}-i\sum_{k=0}^{n-m-1}\arctan\frac{\rho}{n-m-k}\right)$.",
    ),
    rec(
        "RN-P5-C39-Entry08",
        r"Formally, "
        r"$\displaystyle\int_0^{\infty}e^{-x^2}\varphi(x)\cos(2\pi x)\,dx=\int_0^{\infty}e^{-x^2}\varphi(x)\,dx$.",
    ),
    rec(
        "RN-P5-C39-Entry09",
        r"If $\Re\beta>\Re\alpha$, then "
        r"$\displaystyle\int_0^{\infty}\frac{\psi(x+\alpha+1)-\psi(x+\beta+1)}{\Gamma(x+\beta+1)}\,dx"
        r"=\frac{\Gamma(\alpha+1)}{\Gamma(\beta+1)}$, where $\psi(z)=\Gamma'(z)/\Gamma(z)$.",
    ),
    rec(
        "RN-P5-C39-Entry10",
        r"For each nonnegative integer $n$, "
        r"$\displaystyle\sum_{k=0}^{n}\frac{\Gamma(n+1)}{2\,\Gamma(n+2)}\,\frac{1}{(k!)^2}=\frac{\Gamma(n+1)}{2\,\Gamma(n+2)}$.",
    ),
    rec(
        "RN-P5-C39-Entry11",
        r"If $0<\Re n<\inf(\Re\alpha+1,\Re\beta+1)$, then "
        r"$\displaystyle\int_0^{\infty}\frac{x^{n-1}\,{}_2F_1(\alpha,\beta;\alpha+\beta;-x)}{1+x}\,dx"
        r"=\sum_{k=0}^{\infty}\frac{\Gamma(\alpha-n+1)\,\Gamma(\beta-n+1)\,(\alpha)_k(\beta)_k}{\Gamma(\alpha+\beta-n)\,(\alpha+\beta)_k\,k!}"
        r"=\sum_{k=0}^{\infty}\frac{\Gamma(\alpha-n+1)\,\Gamma(n)\,(\alpha)_k(\beta)_k}{\Gamma(\alpha)\,(\alpha+\beta)_k\,k!}$.",
    ),
    rec(
        "RN-P5-C39-Entry12",
        r"Define $F_m(x)$, $m=2^r$ where $r$ is a nonnegative integer, by $F_1(x)=x$, $F_2(x)=\sqrt{2-x}$, and "
        r"$F_{2m}(x)=F_m(F_m(x))$. Then "
        r"$F_{2^{r+1}}(x)=\dfrac{\{(1+\sqrt{1-x})^{2^r}+(1-\sqrt{1-x})^{2^r}\}}{2^{2^r}}$.",
    ),
    rec(
        "RN-P5-C39-Entry13",
        r"If $\varphi(x)$ is any polynomial, then formally "
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{\varphi(n/2)}{2^n}=\sum_{n=0}^{\infty}\frac{\varphi(-n/2)}{2^n}$.",
    ),
    rec(
        "RN-P5-C39-Entry14",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi^2$. Then "
        r"$\displaystyle\sum_{j=0}^{\infty}\sum_{n=0}^{\infty}\frac{L_{2j+1}}{(2n+1)^2(2j+1)^2}"
        r"=\frac{\pi}{4}\sum_{j=0}^{\infty}\sum_{n=0}^{\infty}\frac{1}{(2n+1)(2j+1)}$, "
        r"where $L(s)$ is the Dirichlet $L$-function associated with the character modulo $4$.",
    ),
    rec(
        "RN-P5-C39-Entry15",
        r"If $\displaystyle\psi(n)=\int_0^{\infty}\varphi(x)\cos(nx)\,dx$, then, formally, for even nonnegative integers $r$, "
        r"$\displaystyle\psi^{(r)}(n)=\cos\!\left(\tfrac{r\pi}{2}\right)\int_0^{\infty}x^r\varphi(x)\cos(nx)\,dx$ "
        r"and "
        r"$\displaystyle\varphi^{(r)}(n)=(-1)^{r/2}\cos\!\left(\tfrac{r\pi}{2}\right)\int_0^{\infty}x^r\Gamma(x)\cos(nx)\,dx$.",
    ),
    rec(
        "RN-P5-C39-Entry16",
        r"Let $\alpha>0$ with $\alpha_0=\pi/4$. Then "
        r"$\displaystyle\alpha^2\sum_{n=0}^{\infty}(-1)^n(2n+1)\exp\!\left\{-\frac{\alpha^2(2n+1)^2}{4}\right\}"
        r"=\frac{\sqrt{\pi}}{2}\sum_{n=0}^{\infty}(-1)^n(2n+1)\exp\!\left\{-\frac{(2n+1)^2}{4\alpha^2}\right\}$.",
    ),
    rec(
        "RN-P5-C39-Entry17",
        r"If $I_\nu$ denotes the modified Bessel function of imaginary argument of order $\nu$, then, if $n$ is an integer, "
        r"$I_n(2x)-I_{-n}(2x)=0$.",
    ),
    rec(
        "RN-P5-C39-Entry18",
        r"$\displaystyle\frac{1}{540\sqrt{T_m/T_w}}-\frac{1}{90\sqrt{T_m/T_w}}+\frac{1}{25\sqrt{T_m/T_w}}\approx e^{-2\sqrt{T_m/T_w}}$.",
    ),
    rec(
        "RN-P5-C39-Entry19",
        r"$\displaystyle\sum_{n=1}^{\infty}\frac{\varphi(n)}{n}=\int_1^{\infty}\frac{\varphi(x)}{x}\,dx+\sum_{n=1}^{\infty}c_n$, "
        r"where Ramanujan does not specify $\varphi$ or the constants $c_n$; the series on the right is probably an asymptotic Euler-Maclaurin remainder.",
    ),
    rec(
        "RN-P5-C39-Entry20",
        r"$\displaystyle\sum_{k=2}^{\infty}\frac{2n+k}{k^n+k^{-n}}\cdot\frac{(k-1)^k}{k}\approx\pi\cot(\pi n)$, "
        r"where the meaning of Ramanujan's dots on the right side is unclear and the left-hand series diverges.",
    ),
]
