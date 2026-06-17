"""Part V, Chapter 38 entries — approximations and asymptotic expansions (curated LaTeX)."""

from __future__ import annotations

TOPICS_C38 = ["approximations-and-asymptotic-expansions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C38}


CHAPTER_38 = [
    rec(
        "RN-P5-C38-Entry01",
        r"Let $\gamma$ denote Euler's constant. Then "
        r"$\displaystyle\sum_{k\ge 2}\frac{1}{k\log k}=\log\log(x^2+x+\theta)+0.1015314$ as $x\to\infty$; "
        r"when $x=1$ and $\theta=0.46811$, the right side is approximately $0$; "
        r"and more than $1.30489\times 10^{23}$ terms are required for the partial sum to exceed $5$.",
    ),
    rec(
        "RN-P5-C38-Entry02",
        r"For $p>0$, "
        r"$\displaystyle\frac{1-e^{-p}}{p}=\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{k!\,(p+k)^k}"
        r"\sum_{m=0}^{k-1}\sum_{n=0}^{m}\binom{m}{n}\frac{(-1)^n(p+k)^{m-n}}{(m-n)!}$.",
    ),
    rec(
        "RN-P5-C38-Entry03",
        r"Let $1\le k\le |p|$, where $k$ is an integer and $p$ is complex. For integers $m\ge 0$ and $n\ge 1$, define "
        r"$a_n(m,k):=\sum_{r=0}^{m}\binom{m}{r}s(r-m+n,r+1)$, where $s(a,b)$ are Stirling numbers of the first kind. Then "
        r"$\displaystyle\sum_{m=0}^{\infty}\frac{(-1)^m(p+k)^m}{m!}\sum_{n=1}^{k}\frac{a_n(m,k)}{p^n}"
        r"=\sum_{m=0}^{\infty}\frac{(-1)^m(p+k)^m}{m!}\sum_{n=1}^{k}\frac{s(m+n,n)}{p^n}$.",
    ),
    rec(
        "RN-P5-C38-Entry04",
        r"For each $p>-1$, define $\theta_p$ by "
        r"$\displaystyle\frac{1-e^{-p}}{p}=\theta_p\left\{\frac{1}{p+1}-\frac{1}{(p+1)(p+2)}"
        r"+\frac{4}{3(p+1)(p+2)(p+4)}-\frac{1}{(p+1)(p+2)(p+4)(3p+23)}\right\}$. "
        r"Then $\theta_{-1}=-2.5856$, $\theta_0=0.0069$, $\theta_1=0.4137$, and $\theta_2=1$; moreover, $\theta_1=\tfrac45$ exactly.",
    ),
    rec(
        "RN-P5-C38-Entry05",
        r"Let $0<p<a$. Then "
        r"$\displaystyle\frac{(a+n)^{n-1}}{(-p)^n}=u_n(a)$, where, for $n>0$, "
        r"$u_n(a):=\sum_{k=0}^{\infty}\frac{1}{(a+k)^{n+2}\,\Gamma(k+1)}$. "
        r"Furthermore, for $n>1$, "
        r"$\displaystyle\frac{u_{n-1}(a)-u_n(a+1)}{u_n(a)-u_n(a+1)}=\frac{a}{n}$.",
    ),
    rec(
        "RN-P5-C38-Entry06",
        r"Let $u_n(a)$ be defined by Entry 5. As $a\to\infty$, "
        r"$\displaystyle u_n(a)\sim\frac{1}{a}+\frac{n}{2a^2}+\frac{n(n-1)}{8a^3}"
        r"+\frac{n(n-1)(n-2)}{48a^4}+\frac{5n(n-1)(n-2)(n-3)}{384a^5}+\cdots$.",
    ),
    rec(
        "RN-P5-C38-Entry07",
        r"Let $a,p>0$. As $p\to\infty$, "
        r"$\displaystyle e^p S(a,p/2)\sim\sum_{n=0}^{\infty}\frac{(-1)^n P_{2n}(p)}{(a+p/2)^{2n+1}}$, "
        r"where $P_{2n}=P_{2n}(p)$, $n\ge 1$, is a polynomial in $p$ of degree $n-1$. In particular, "
        r"$P_2(p)=\tfrac{p}{30}+\tfrac{1}{12}$, $P_4(p)=\tfrac{691p^4}{2730}+\tfrac{691p^3}{210}+\tfrac{616p^2}{45}+\tfrac{451p}{18}+\tfrac{385}{54}$, "
        r"and $P_6(p)=\tfrac{7p^6}{90}+\tfrac{35p^5}{135}+\tfrac{7709p^4}{135}+\tfrac{26026p^3}{9}+\tfrac{2002p^2}{54}+\tfrac{7007p}{162}$.",
    ),
    rec(
        "RN-P5-C38-Entry08",
        r"Let $n$ be a nonnegative integer and suppose that $0<p<a$. Then "
        r"$\displaystyle\frac{(a-p+n)^{n-1}}{(a+p+n)^{n+1}(a+n)^p}"
        r"=\frac{p^2}{2np^2}\left\{1+\frac{2ap}{a+n}+\frac{p^2}{3(a+n)^2}+\frac{2np^3}{3(a+n)^3}\right."
        r"+\frac{p^4}{2(a+n)^4}+\frac{4p^5}{15(a+n)^5}+\frac{2a^2p^2+10a^3p+23a^2/2+5a/4}{4(a+n)^4}+\cdots\right\}$.",
    ),
    rec(
        "RN-P5-C38-Entry09",
        r"Let $m=\tfrac12 n(n+1)$, where $n$ is a positive integer. As $m\to\infty$, "
        r"$\displaystyle\sum_{k=1}^{n}\frac{1}{k}=\log m+\gamma+\frac{1}{2m}-\frac{1}{12m^2}"
        r"+\frac{191}{360360m^6}+\frac{29}{30030m^7}+\frac{2833}{1166880m^8}+\frac{140051}{17459442m^9}+\cdots$.",
    ),
    rec(
        "RN-P5-C38-Entry10",
        r"Ramanujan records a property relating the function "
        r"$F(x):=\displaystyle\sum_{n=1}^{\infty}\frac{\log n}{n^2+x^2}$ "
        r"and the integral "
        r"$G(x):=\displaystyle\int_0^{\infty}\frac{t\,dt}{(e^{2\pi t}-1)((t+x)^2)}$.",
    ),
    rec(
        "RN-P5-C38-Entry11",
        r"Let $a>1$ and let $\gamma$ denote Euler's constant. As $x\to 0+$, Ramanujan claims an asymptotic formula "
        r"for a double-logarithmic series whose first three nonconstant terms agree with those in Hardy's evaluation "
        r"$\displaystyle\sum_{m=0}^{\infty}\sum_{n=0}^{\infty}\frac{(-1)^{m+n}}{m!\,n!\,(m+n+2)(\log a)^{m+n+2}}$.",
    ),
    rec(
        "RN-P5-C38-Entry12",
        r"Let $a,b>1$. Suppose that $\dfrac{2\pi n i}{\log a}\neq\dfrac{2\pi m i}{\log b}$ for every pair of nonzero integers $m,n$. "
        r"Then, for $x>0$, "
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{(-x)^k}{k^2(a^k-1)(b^k-1)}"
        r"=\frac{\pi^2}{6\log a\log b}+\frac{\log x}{2\log a\log b}"
        r"+\frac{(\log x)^2}{4\log a\log b}+\frac{\gamma}{2\log a\log b}"
        r"+\sum_{n=1}^{\infty}\frac{n!\,(a^n-1)(b^n-1)}{\log a\log b}\left\{\sum_{\substack{m\\2\pi m i/\log a}}\frac{(-x)^m}{m^2}+\sum_{\substack{m\\2\pi m i/\log b}}\frac{(-x)^m}{m^2}\right\}$.",
    ),
    rec(
        "RN-P5-C38-Entry13",
        r"Let $a,b,c>1$, and assume that no two of the numbers $\dfrac{2\pi n i}{\log a}$, $\dfrac{2\pi m i}{\log b}$, and "
        r"$\dfrac{2\pi k i}{\log c}$ are equal, where $n,m,k$ are nonzero integers. Then, for $x>0$, "
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{(-x)^k}{k^2(a^k-1)(b^k-1)(c^k-1)}$ equals a combination of "
        r"$\log^2 x$, $\log x$, $\gamma$, and residue sums over the three logarithmic progressions.",
    ),
    rec(
        "RN-P5-C38-Entry14",
        r"Let the perimeter of an ellipse be $L=4(a+b)(1+h)$, where $h$ is small. Then "
        r"$\displaystyle h\approx\frac{\lambda^4}{4}+\frac{16-4\lambda^2}{49}\lambda^6+\frac{\lambda^8-8\lambda^6}{576}+\cdots$, "
        r"where $\lambda=(a-b)/(a+b)$, very nearly. According to this approximation, the perimeter of a parabola is "
        r"$\approx 3.99944(a+b)$ for $4(a+b)$.",
    ),
    rec(
        "RN-P5-C38-Entry15",
        r"Define $S:=\displaystyle\sum_{k=1}^{n}\frac{x^k-1}{k}$, where $n=\left\lfloor(p+\tfrac12)\log_p x-\tfrac12\right\rfloor$ is a positive integer. "
        r"Then, as $p\to\infty$, $S=\log p+O(p^{-2})$.",
    ),
    rec(
        "RN-P5-C38-Entry16",
        r"As $t\to 0+$, "
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n e^{-(n+1/2)^2/(4t)}}{\sqrt{\pi t}}"
        r"\sim 1+\frac{1}{6t}+\frac{1}{120t^2}+\frac{1}{5040t^3}+\frac{1}{272160t^4}+\frac{1}{19958400t^5}+\cdots$.",
    ),
    rec(
        "RN-P5-C38-Entry17",
        r"For $n>0$ and $x>0$, define "
        r"$u_n(x):=\Gamma(n+1)\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(n+2k)(n+1)^{k-1}}{k!}"
        r"\exp\!\left\{-\frac{(n+2k)^2}{4x}\right\}$. Then "
        r"$\displaystyle u_{n+2}=\frac{1}{x}\frac{du_n}{dx}+\frac{n(n-1)}{4x^2}u_n+\frac{2n+1}{2x^{3/2}}u_n$, "
        r"and $u_n(x)=\sqrt{\pi}\,x^{(n+1)/2}e^{-x/4}L_n^{(-1/2)}\!\left(\tfrac{x}{4}\right)$, where $L_n^{(\alpha)}$ is a Laguerre polynomial.",
    ),
    rec(
        "RN-P5-C38-Entry18",
        r"Let $S(x,n):=\displaystyle\sum_{k=0}^{n-1}\varphi(x-n+1+2k)$. Then $S(x,n)/n$ has the successive approximations "
        r"$\varphi(x)$, "
        r"$\tfrac12\{\varphi(x+\tfrac{n-1+\sqrt{n-1}}{2})+\varphi(x+\tfrac{n-1-\sqrt{n-1}}{2})\}$, "
        r"$\tfrac{n}{7}\{\varphi(x-\tfrac{5(n-1)}{6(3n-7)})+\varphi(x)+\varphi(x+\tfrac{5(n-1)}{6(3n-7)})\}$, and "
        r"a four-term formula involving $\varphi$ at $x\pm\tfrac{5(n-1)}{6(3n-7)}$ and $x\pm\tfrac{8(n-1)}{6(3n-7)}$ with weights determined by Gaussian quadrature for Hahn polynomials.",
    ),
    rec(
        "RN-P5-C38-Entry18-Corollary01",
        r"We have the approximations "
        r"$\displaystyle\sum_{k=1}^{7}u_k\approx 7\{\tfrac12 u_2+u_8\}$, "
        r"$\displaystyle\sum_{k=1}^{26}u_k\approx 13\{u_6+u_{21}\}$, "
        r"$\displaystyle\sum_{k=1}^{13}u_k\approx 13\{7u_2+11u_7+7u_{12}\}$, "
        r"$\displaystyle\sum_{k=1}^{22}u_k\approx 22\{16u_3+256u_{23/2}+161u_{20}\}$, and "
        r"$\displaystyle\sum_{k=1}^{21}u_k\approx 21\{506(\varphi(2)+\varphi(20))+931(\varphi(11+2\sqrt{22/7})+\varphi(11-2\sqrt{22/7}))\}$.",
    ),
    rec(
        "RN-P5-C38-Entry19",
        r"Let $f$ be a continuous function on $[0,\infty)$. Then "
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{f(n)}{n!}\approx e^{-x}f(x)$; "
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{f(n)}{n!}\approx e^{-x}\left\{f(x)+\tfrac12 f\!\left(x-\tfrac12+\tfrac{\sqrt{1+4x}}{2}\right)+\tfrac12 f\!\left(x-\tfrac12-\tfrac{\sqrt{1+4x}}{2}\right)\right\}$; "
        r"and a three-point formula with interpolation nodes including $x$ that is exact for all polynomials of degree $4$ or less.",
    ),
    rec(
        "RN-P5-C38-Entry20",
        r"Assume that the product on the left side of "
        r"$\displaystyle\prod_{k=1}^{\infty}\left(1+\frac{x}{\varphi(k)}\right)$ converges, $\varphi(x)$ is monotonically increasing, and $\varphi(0)>0$. "
        r"Then, as $a\to\infty$, "
        r"$\displaystyle x\prod_{k=1}^{\infty}\left(1+\frac{x}{\varphi(k)/a}\right)\approx c\exp\!\left(\int_0^{x_a}\frac{\varphi'(ax)}{x(1-x)}\,dx\right)$, "
        r"where $c$ is given approximately by $c\approx\sqrt{\varphi(0)/a}\,\exp(-I_2)$ and $x_a$ satisfies $\log(1+x_a/\varphi(0))=I_2/a$.",
    ),
    rec(
        "RN-P5-C38-Entry21",
        r"Consider the equation "
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{(-x^3)^n}{n!}+\sum_{n=1}^{\infty}e^{-nx^{3/2}}\cos\!\left(\frac{(2n-1)x\sqrt3}{2}\right)=0$, "
        r"where $\omega:=e^{2\pi i/3}$. There exist infinitely many positive roots, close to the zeros $\pi(2n+1)/\sqrt3$ of $\cos(x\sqrt3/2)$. "
        r"More precisely, if $x\approx e^{-n}(3n+1)^{1/3}/\sqrt3$, then these roots are given by a series in powers of $n^{-1/3}$ with coefficients involving products of primes. "
        r"All roots are given by $x$, $\omega x$, and $\omega^2 x$, where $x$ is as above.",
    ),
    rec(
        "RN-P5-C38-Entry22",
        r"Let $x_0,x_1,x_2,\ldots$ be the real roots of Entry 21. Then "
        r"$\displaystyle F(x)=\prod_{n=0}^{\infty}\left(1+\frac{x}{x_n}\right)\left(1+\frac{x}{\omega x_n}\right)\left(1+\frac{x}{\omega^2 x_n}\right)$, "
        r"where $F(x)$ is defined by Entry 21.",
    ),
    rec(
        "RN-P5-C38-Entry23",
        r"As $x\to 1-$, "
        r"$\displaystyle\sum_{n=1}^{\infty}\frac{x^{n(n+1)/2}}{(1-x)(1-x^2)\cdots(1-x^n)}"
        r"\sim\frac{\pi}{\sqrt2\,(1-x)}+\frac{\sqrt2}{8}\log\!\left(\frac{2+\sqrt2}{2-\sqrt2}\right)+\frac{\sqrt2}{3\pi}\log\!\left(\frac{2+\sqrt2}{2-\sqrt2}\right)+\cdots$.",
    ),
]
