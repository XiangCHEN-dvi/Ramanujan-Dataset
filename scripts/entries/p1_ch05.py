"""Part I, Chapter 5 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C05 = ["eulerian-polynomials-bernoulli-zeta"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C05}


CHAPTER_5 = [
    rec(
        "RN-P1-C05-Entry01i",
        r"Assume that for $|h|$ sufficiently small, $f$ can be expanded as "
        r"$f(x)=\sum_{n=0}^\infty a_n h^n \varphi^{(n)}(x)$, where each $a_n$ is independent of "
        r"$\varphi$. If $f(x+h)-f(x)=h\varphi'(x)$, then $a_n=B_n/n!$ for $0\le n<\infty$, where "
        r"$B_n$ denotes the $n$th Bernoulli number.",
    ),
    rec(
        "RN-P1-C05-Entry01ii",
        r"Under the expansion hypothesis of Entry 1(i), if $f(x+h)+f(x)=h\varphi'(x)$, then "
        r"$a_n=(1-2^n)B_n/n!$ for $0\le n<\infty$.",
    ),
    rec(
        "RN-P1-C05-Entry02i",
        r"For a polynomial $\varphi$, define for each nonnegative integer $n$ "
        r"$F_{2n+1}(x)=\varphi(x)+\sum_{k=1}^n(-1)^k\binom{n}{k}^2\bigl\{\varphi(x+k)+\varphi(x-k)\bigr\}$. "
        r"If $f(x+1)-f(x-1)=2\varphi'(x)$, then there exists a polynomial solution "
        r"$f(x)=\sum_{n=0}^\infty F_{2n+1}(x)/(2n+1)$.",
    ),
    rec(
        "RN-P1-C05-Entry02ii",
        r"With $F_{2n+1}$ as in Entry 2(i), if $f(x+1)+f(x-1)=2\varphi(x)$ for a polynomial "
        r"$\varphi$, then there exists a polynomial solution "
        r"$f(x)=\sum_{n=0}^\infty F_{2n+1}(x)/(2n+1)$.",
    ),
    rec(
        "RN-P1-C05-Entry03",
        r"Define the Eulerian polynomials $\psi_n(p)$, $0\le n<\infty$, $p\ne -1$, by "
        r"$\displaystyle\frac{e^x+p}{p+1}=\sum_{n=0}^\infty\frac{(-1)^n\psi_n(p)x^n}{n!(p+1)^{n+1}}$ "
        r"for $|x|<|\log(-p)|$. If $f(x+h)+pf(x)=\varphi(x)$ with $p\ne -1$, then in the notation of "
        r"Entry 1(i), $a_n=(-1)^n\psi_n(p)/\{n!(p+1)^{n+1}\}$ for $0\le n<\infty$.",
    ),
    rec(
        "RN-P1-C05-Entry04",
        r"For $|p|<1$ and $n\ge 0$, "
        r"$\displaystyle(p+1)^{-n-1}\psi_n(p)=\sum_{k=0}^\infty(k+1)^n(-p)^k$.",
    ),
    rec(
        "RN-P1-C05-Entry05",
        r"$\psi_0(p)=1$, and for $n\ge 1$, "
        r"$\displaystyle(-1)^{n+1}p(p+1)^{-n}\psi_n(p)=\sum_{k=0}^n(-1)^k\binom{n}{k}(p+1)^{-k}\psi_k(p)$.",
    ),
    rec(
        "RN-P1-C05-Entry06",
        r"Let $1\le r\le n$, and let $F_k(n)$ denote the Eulerian numbers defined by "
        r"$\displaystyle\psi_n(p)=\sum_{k=0}^{n-1}F_{k+1}(n)(-p)^k$. Then "
        r"(i) $\displaystyle\sum_{j=0}^{r-1}\binom{n+j}{j}F_{r-j}(n)=r^n$; "
        r"(ii) $\displaystyle\sum_{k=1}^{n+1}k^n=\sum_{j=0}^{r-1}\binom{n+1}{j}F_{r-j}(n)$; "
        r"(iii) $\displaystyle F_r(n)=\sum_{k=0}^{r-1}(-1)^k\binom{r}{k}(r-k)^n$.",
    ),
    rec(
        "RN-P1-C05-Entry07",
        r"If $n\ge 0$ and $0<x<1-e^{-2\pi}$, then "
        r"$\displaystyle\frac{x^{n+1}}{1-x}\,\psi_n(x-1)=\frac{n!}{(1-x)^{n+1}}\left(\log\frac{1}{1-x}\right)^{n+1}"
        r"+(-1)^n\sum_{k=n+1}^\infty\frac{B_k}{k(k-n-1)!}\left(\log\frac{1}{1-x}\right)^{k-n-1}$, "
        r"where $B_k$ denotes the $k$th Bernoulli number.",
    ),
    rec(
        "RN-P1-C05-Entry08",
        r"For $n\ge 1$, $\psi_n(-1)=n!$ and "
        r"$\displaystyle\psi_n(1)=\frac{2^{n+1}(2^{n+1}-1)B_{n+1}}{n+1}$. Also "
        r"$\psi_0(p)=\psi_1(p)=1$, $\psi_2(p)=1-p$, $\psi_3(p)=1-4p+p^2$, "
        r"$\psi_4(p)=1-11p+11p^2-p^3$, $\psi_5(p)=1-26p+66p^2-26p^3+p^4$, and "
        r"$\psi_6(p)=1-57p+302p^2-302p^3+57p^4-p^5$.",
    ),
    rec(
        "RN-P1-C05-Entry08-Corollary01",
        r"Let $f(x)$ denote the solution found in Entry 3. Then $f(x)$ is the term independent of "
        r"$n$ in $\displaystyle\sum_{k=0}^\infty\varphi^{(k)}(x)/n^k$, provided the series in the "
        r"numerator converges.",
    ),
    rec(
        "RN-P1-C05-Entry08-Corollary03",
        r"If $n$ is even and positive, then $\psi_n(p)$ is divisible by $1-p$.",
    ),
    rec(
        "RN-P1-C05-Entry08-Corollary04",
        r"For $|x|<|\log(-p)|$, "
        r"$\displaystyle\frac{\cos x+p}{p^2+2p\cos x+1}=\sum_{n=0}^\infty\frac{(-1)^n\psi_{2n}(p)x^{2n}}{(2n)!(p+1)^{2n+1}}$.",
    ),
    rec(
        "RN-P1-C05-Entry08-Corollary05",
        r"For $|x|<|\log(-p)|$, "
        r"$\displaystyle\frac{\sin x}{p^2+2p\cos x+1}=\sum_{n=0}^\infty\frac{(-1)^n\psi_{2n+1}(p)x^{2n+1}}{(2n+1)!(p+1)^{2n+2}}$.",
    ),
    rec(
        "RN-P1-C05-Entry08-Corollary06",
        r"Define $A_k$ by $\displaystyle\psi_n(p-1)=\sum_{k=0}^{n-1}A_k\binom{n}{k}(-p)^k$. "
        r"For $1\le r\le n$: "
        r"(i) $\displaystyle\sum_{k=1}^r\binom{r}{k}A_k=r^n$; "
        r"(ii) $\displaystyle A_r=\sum_{k=0}^{r-1}(-1)^k\binom{r}{k}(r-k)^n$; "
        r"(iii) $A_r/n!$ is the coefficient of $x^n/n!$ in $(e^x-1)^r$; "
        r"(iv) $\displaystyle\sum_{k=1}^\infty(-1)^{k+1}k^n\bigl(\zeta(k+1)^{-1}\bigr)"
        r"=(-1)^n+(-1)^n2^{-n-1}\psi_n(1)+\sum_{k=1}^n(-1)^{k+1}A_k(k+1)$.",
    ),
    rec(
        "RN-P1-C05-Entry11",
        r"For $|x|<2\pi$, "
        r"$\displaystyle\log\frac{x}{e^x-1}=\sum_{n=1}^\infty\frac{(-1)^{n-1}B_n x^n}{n\,n!}$.",
    ),
    rec(
        "RN-P1-C05-Entry12",
        r"For $|x|<\pi$, "
        r"$\displaystyle\log\frac{2}{e^x+1}=\sum_{n=1}^\infty\frac{(-1)^{n-1}(2n-1)B_n x^n}{n\,n!}$.",
    ),
    rec(
        "RN-P1-C05-Entry12-Example01",
        r"If $e^P+e^Q+e^R=2+e^{P+Q+R}$, then "
        r"$P+Q+R+\tfrac{1}{12}(P+Q+R)^3\approx\tfrac{1}{2}$.",
    ),
    rec(
        "RN-P1-C05-Entry12-Example02",
        r"If "
        r"$\displaystyle\frac{e^{P+Q+R+S}}{e^P+e^Q+e^R+e^S-e^{-P}-e^{-Q}-e^{-R}-e^{-S}-2}=2$, "
        r"then $P+Q+R+S+\tfrac{1}{12}(P+Q+R+S)^3\approx 0$.",
    ),
    rec(
        "RN-P1-C05-Entry12-Example03",
        r"If "
        r"$\displaystyle\frac{2e^{P+Q+R+S+T}}{(e^P+e^Q+e^R+e^S+e^T-2)^2-(e^{2P}+e^{2Q}+e^{2R}+e^{2S}+e^{2T}-2)}=2$, "
        r"then "
        r"$\displaystyle\frac{1}{P}+\frac{1}{Q}+\frac{1}{R}+\frac{1}{S}+\frac{1}{T}+\frac{1}{12}(P+Q+R+S+T)\approx-\tfrac{1}{2}$.",
    ),
    rec(
        "RN-P1-C05-Entry13",
        r"For $|x|<\pi$, "
        r"$\displaystyle x\cot x=\sum_{n=0}^\infty\frac{(-1)^n B_{2n}(2x)^{2n}}{(2n)!}$.",
    ),
    rec(
        "RN-P1-C05-Entry14",
        r"For $|x|<\pi$, "
        r"$\displaystyle x\csc x=\sum_{n=0}^\infty\frac{(-1)^n(2-2^{2n})B_{2n}x^{2n}}{(2n)!}$.",
    ),
    rec(
        "RN-P1-C05-Entry15",
        r"For $|x|<\pi/2$, "
        r"$\displaystyle x\tan x=\sum_{n=1}^\infty\frac{(-1)^{n-1}2^{2n}(2^{2n}-1)B_{2n}x^{2n}}{(2n)!}$.",
    ),
    rec(
        "RN-P1-C05-Entry16",
        r"For $|x|<\pi$, "
        r"$\displaystyle\log\frac{x}{\sin x}=\sum_{n=1}^\infty\frac{(-1)^{n+1}B_{2n}(2x)^{2n}}{(2n)(2n)!}$.",
    ),
    rec(
        "RN-P1-C05-Entry17",
        r"For $|x|<\pi/2$, "
        r"$\displaystyle\log(\sec x)=\sum_{n=1}^\infty\frac{(-1)^n2^{2n}(1-2^{2n})B_{2n}x^{2n}}{(2n)(2n)!}$.",
    ),
    rec(
        "RN-P1-C05-Entry18",
        r"If $n$ is an integer exceeding $1$, then "
        r"$\displaystyle-(2n+1)B_{2n}=\sum_{k=1}^{n-1}\binom{2n}{2k}B_{2k}B_{2n-2k}$.",
    ),
    rec(
        "RN-P1-C05-Entry19i",
        r"For each positive integer $n$, $2(2^{2n}-1)B_{2n}$ is an integer.",
    ),
    rec(
        "RN-P1-C05-Entry19ii",
        r"The numerator of $B_{2n}$ is divisible by the largest factor of $2n$ that is relatively "
        r"prime to the denominator of $B_{2n}$.",
    ),
    rec(
        "RN-P1-C05-Entry19iii",
        r"For each positive integer $n$, the Bernoulli number $B_{2n}$ equals an integer minus "
        r"$\displaystyle\sum_{\substack{p\ \mathrm{prime}\\ (p-1)\mid 2n}}\frac{1}{p}$ "
        r"(von Staudt–Clausen theorem). Equivalently, the denominator of $B_{2n}$ in lowest terms "
        r"is the product of all primes $p$ with $(p-1)\mid 2n$.",
    ),
    rec(
        "RN-P1-C05-Entry20",
        r"For each nonnegative integer $n$, "
        r"$\displaystyle(-1)^{n-1}B_{2n}+(-1)^n\bigl(1-F_{2n}\bigr)$ is an integer divisible by "
        r"$1/(2n)$, where $F_{2n}$ is the sum of the reciprocals of those primes $p$ such that "
        r"$(p-1)\mid 2n$.",
    ),
    rec(
        "RN-P1-C05-Entry20-Example01",
        r"$B_{22}=\dfrac{854513}{138}$.",
    ),
    rec(
        "RN-P1-C05-Entry20-Example02",
        r"The fractional part of $B_{200}$ is $216641/1366530$.",
    ),
    rec(
        "RN-P1-C05-Entry22",
        r"If $n$ is a natural number, then "
        r"$\displaystyle2^{2n}(2^{2n}-1)B_{2n}=2n\sum_{k=0}^n\binom{2n}{2k}E_{2k}E_{2n-2k-2}$, "
        r"where $E_j$ denotes the $j$th Euler number.",
    ),
    rec(
        "RN-P1-C05-Entry25",
        r"For a positive integer $n$, with $\lambda(s)=\sum_{k=0}^\infty(2k+1)^{-s}$, "
        r"$\eta(s)=\sum_{k=1}^\infty(-1)^{k+1}k^{-s}$, and "
        r"$L(s)=\sum_{k=0}^\infty(-1)^k(2k+1)^{-s}$: "
        r"(i) $\displaystyle\zeta(2n)=\frac{(-1)^{n-1}(2\pi)^{2n}}{2(2n)!}\,B_{2n}$; "
        r"(ii) $\displaystyle\lambda(2n)=\frac{(-1)^{n-1}(1-2^{-2n})(2\pi)^{2n}}{2(2n)!}\,B_{2n}$; "
        r"(iii) $\displaystyle\eta(2n)=\frac{(-1)^{n-1}(1-2^{1-2n})(2\pi)^{2n}}{2(2n)!}\,B_{2n}$; "
        r"(iv) $\displaystyle L(2n-1)=\frac{(-1)^{n-1}(\pi/2)^{2n-1}}{2(2n-2)!}\,E_{2n-2}$.",
    ),
    rec(
        "RN-P1-C05-Entry25-Corollary01",
        r"Using Ramanujan's extension $B^*_s=(-1)^{s+1}2(2s)!\,\zeta(s)/(2\pi)^{2s}$, "
        r"$B^*_{1/2}=\infty$, $B^*_{3/2}=\zeta(3/2)/(4\pi\sqrt{2})$, and "
        r"$B^*_3=-2\zeta(3)/(4\pi\sqrt{2})$.",
    ),
    rec(
        "RN-P1-C05-Entry25-Corollary02",
        r"With Ramanujan's extensions $B^*_s$ and $E^*_s=2\Gamma(s)\,L(s)/(\pi/2)^s$: "
        r"$B^*_0=-1$, $B^*_{1/2}=-(1+1/\sqrt{3})\,\eta(1/2)$, $E^*_0=\infty$, "
        r"$E^*_{1/2}=2\sqrt{\pi}\,L(1/2)$, and $E^*_1=8L(2)/\pi^2$.",
    ),
    rec(
        "RN-P1-C05-Entry26",
        r"For $a,b>0$ and $n>1$, let "
        r"$\displaystyle f(a)=\sum_{k=1}^\infty(a+bk)^{-n}$. As $b/a\to 0$, "
        r"$\displaystyle a^n f(a)\sim\frac{a}{b^{n-1}}-\frac{1}{2}"
        r"+\sum_{k=1}^\infty\frac{B_{2k}(n+2k-2)!}{(n-1)!\,2k\,b^{n+2k-1}}$.",
    ),
    rec(
        "RN-P1-C05-Entry26-Corollary01",
        r"The Riemann zeta-function has a simple pole at $s=1$ with residue $1$, and the constant "
        r"term in the Laurent expansion of $\zeta(s)$ about $s=1$ is Euler's constant $\gamma$.",
    ),
    rec(
        "RN-P1-C05-Entry26-Corollary02",
        r"Euler's constant satisfies "
        r"$\displaystyle\gamma-\frac{1}{2}\sim\sum_{n=1}^\infty\frac{B_{2n}}{2n\cdot 2n}$.",
    ),
    rec(
        "RN-P1-C05-Entry27",
        r"Suppose $|a_p|\le p^{-c}$ for each prime $p$ and some constant $c>1$. Then "
        r"$\displaystyle\prod_p(1-a_p)^{-1}=1+\sum_{n=2}^\infty a_{p_1}\cdots a_{p_k}$, "
        r"where the product is over all primes and the suffixes on the right are the (not necessarily "
        r"distinct) primes in the canonical factorization of $n$.",
    ),
    rec(
        "RN-P1-C05-Entry28",
        r"For $\Re s>1$, $\displaystyle\zeta(s)=\prod_p(1-p^{-s})^{-1}$.",
    ),
    rec(
        "RN-P1-C05-Entry28-Corollary01",
        r"For $\Re s>1$, "
        r"$\displaystyle\prod_p(1+p^{-s})^{-1}=\frac{\zeta(s)}{\zeta(2s)}$.",
    ),
    rec(
        "RN-P1-C05-Entry28-Corollary02",
        r"For $\Re s>1$, "
        r"$\displaystyle\prod_p(1+p^{-s})=\frac{\zeta(2s)}{\zeta(s)}$.",
    ),
    rec(
        "RN-P1-C05-Entry28-Corollary03",
        r"For $\Re s>1$, define "
        r"$\displaystyle T(s)=\sum_{\substack{n\ge 1\\ \omega(n)\ \mathrm{odd}}}n^{-s}$. Then "
        r"$\displaystyle T(s)=\frac{\zeta(2s)-\zeta(s)}{2\zeta(s)}$, "
        r"where the sum is over positive integers with an odd number of prime factors.",
    ),
    rec(
        "RN-P1-C05-Entry28-Corollary04",
        r"For $\Re s>1$, "
        r"$\displaystyle L(s)=\sum_{k=0}^\infty(2k+1)^{-s}"
        r"=\prod_p\left(1-\frac{(-1)^{(p-1)/2}}{p^s}\right)^{-1}$.",
    ),
    rec(
        "RN-P1-C05-Entry28-Corollary05",
        r"For $\Re s>1$, "
        r"$\displaystyle\sum_{k=1}^\infty k^{-s}\log k=\frac{\zeta'(s)}{\zeta(s)}"
        r"=\sum_p\frac{\log p}{p^s-1}$.",
    ),
    rec(
        "RN-P1-C05-Entry28-Example02",
        r"(i) $\displaystyle\prod_p(1+p^{-2})=\frac{\zeta(4)}{\zeta(2)}=\frac{\pi^2}{15}$; "
        r"(ii) $\displaystyle\prod_p(1+p^{-2})^{-1}=\frac{\zeta(2)}{\zeta(4)}=\frac{15}{\pi^2}$.",
    ),
    rec(
        "RN-P1-C05-Entry28-Example03",
        r"$T(2)=\pi^2/20$ and $T(4)=\pi^4/1260$, where $T(s)$ is as in Entry 28, Corollary 3.",
    ),
    rec(
        "RN-P1-C05-Entry29",
        r"For $|x|<1$, with $p_1,p_2,\ldots$ the primes in ascending order, Ramanujan claimed "
        r"$\displaystyle\prod_{k=1}^\infty(1-x^{p_k})^{-1}"
        r"=1+\sum_{k=1}^\infty\frac{x^{p_1+\cdots+p_k}}{(1-x)(1-x^2)\cdots(1-x^k)}$. "
        r"This identity is false: if $c_n$ and $d_n$ denote the coefficients of $x^n$ on the left "
        r"and right, then $c_n=d_n$ for $2\le n\le 20$, but $c_{21}=30$ and $d_{21}=31$.",
    ),
    rec(
        "RN-P1-C05-Entry30",
        r"Suppose $|a_p|\le p^{-c}$ for each prime $p$ and some constant $c>1$. Then "
        r"$\displaystyle\prod_p(1+a_p)=1+\sum_{\substack{n\ge 1\\ n\ \mathrm{squarefree}}} a_{p_1}\cdots a_{p_k}$, "
        r"where $n=p_1\cdots p_k$ with distinct primes.",
    ),
    rec(
        "RN-P1-C05-Entry30-Corollary01",
        r"The sum of the reciprocals of the primes diverges.",
    ),
    rec(
        "RN-P1-C05-Entry30-Corollary02",
        r"$\displaystyle\lim_{s\to 1+}\left\{\log(s-1)+\sum_p p^{-s}\right\}$ exists.",
    ),
    rec(
        "RN-P1-C05-Entry30-Corollary03",
        r"If $p_n$ denotes the $n$th prime, then $p_n/n-\log n$ tends to a limit as $n\to\infty$ "
        r"(Ramanujan struck this statement out; in fact $p_n\sim n\log n$).",
    ),
]
