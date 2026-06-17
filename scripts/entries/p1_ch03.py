"""Part I, Chapter 3 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C03 = ["combinatorial-analysis-and-series-inversions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C03}


CHAPTER_3 = [
    rec(
        "RN-P1-C03-Entry01",
        r"Let $f(z)$ be analytic on $|z|<R_1$ with $R_1>1$, and let "
        r"$g(z)=\sum_{k=0}^\infty Q_k z^k$ be analytic on $|z|<R_2$ with $R_2>0$. "
        r"Define $P_k$, $0\le k<\infty$, by $\sum_{k=0}^\infty P_k z^k=e^{zg(z)}$ for $|z|<R_2$. "
        r"Suppose $\sum_{j=0}^\infty Q_j\sum_{k=0}^\infty f^{(j+k)}(0)/(j!k!)$ converges and this repeated "
        r"summation may be replaced by a diagonal summation $j+k=n$, $0\le n<\infty$. Then "
        r"$\displaystyle\sum_{n=0}^\infty P_n f^{(n)}(0)=\sum_{n=0}^\infty Q_n f^{(n)}(1)$.",
    ),
    rec(
        "RN-P1-C03-Entry01-Corollary01",
        r"Suppose the hypotheses of Entry 1 hold for $f(z)=(1+xz)^n$ with $|x|<1$ and $n$ arbitrary. Then "
        r"$\displaystyle\sum_{k=0}^\infty P_k\frac{x^k}{\Gamma(n-k+1)}"
        r"=\sum_{k=0}^\infty Q_k\frac{x^k(1+x)^{n-k}}{\Gamma(n-k+1)}$.",
    ),
    rec(
        "RN-P1-C03-Entry02",
        r"For all complex $x$ and $z$, define "
        r"$\displaystyle\varphi(z)=e^x\sum_{k=1}^\infty\frac{(-1)^{k-1}x^k}{z(z+1)\cdots(z+k-1)}$, "
        r"where $\displaystyle\sum_{k=1}^\infty\frac{x^k}{(z+k-1)(k-1)!}$ defines the auxiliary function $q_1(z)$.",
    ),
    rec(
        "RN-P1-C03-Entry02-Corollary01",
        r"Let $f$ satisfy the hypotheses of Entry 1. Then for all $z$, "
        r"$\displaystyle\sum_{k=0}^\infty\frac{f^{(k)}(0)}{(z+k)k!}"
        r"=\sum_{k=0}^\infty\frac{(-1)^k f^{(k)}(1)}{z(z+1)\cdots(z+k)}$.",
    ),
    rec(
        "RN-P1-C03-Entry02-Corollary02",
        r"For each complex $x$, "
        r"$\displaystyle\sum_{k=1}^\infty\left(1+\frac{1}{2}+\cdots+\frac{1}{k}\right)\frac{x^k}{k!}"
        r"=e^x\sum_{k=1}^\infty\frac{(-1)^{k-1}x^k}{(z+k)(k-1)!}$ (obtained from Entry 2 by $x\to -x$, $z\to z+1$, "
        r"differentiating, and setting $z=0$).",
    ),
    rec(
        "RN-P1-C03-Entry03",
        r"Let $\varphi$ and $f_n$ be defined by (3.1) and (3.3), respectively. As $z\to\infty$ in the region "
        r"$R_e=\{z:-\pi+\delta\le\arg z\le\pi-\delta\}$, $\delta>0$, "
        r"$\displaystyle\sum_{k=0}^n\frac{(-1)^k f_k(x)}{z^{k+1}}"
        r"=\sum_{k=1}^{n+1}\frac{(-1)^{k-1}x^k}{(z+1)(z+2)\cdots(z+k)}+O(z^{-n-2})$.",
    ),
    rec(
        "RN-P1-C03-Entry04",
        r"Let $a$ and $x$ be arbitrary complex numbers. Then "
        r"$\displaystyle\Gamma(e^a-1)=\sum_{n=0}^\infty\frac{a^n}{n!}\,f_{n-1}(x)$, "
        r"where $f_{-1}(x)=1$ and $f_n$ is defined by (3.3).",
    ),
    rec(
        "RN-P1-C03-Entry05",
        r"For each nonnegative integer $n$, "
        r"$\displaystyle\sum_{k=0}^n\binom{n}{k}f_k(x)=f_{n+1}(x)$, "
        r"where $f_n$ is defined by (3.3).",
    ),
    rec(
        "RN-P1-C03-Entry06",
        r"Let $n$ be a nonnegative integer and $r$ a positive integer with $r\le n+1$. Then "
        r"$\displaystyle\sum_{k=0}^{r-1}\frac{1}{k!}\binom{n}{k}r^{n-k}=\frac{r^n}{(r-1)!}$.",
    ),
    rec(
        "RN-P1-C03-Entry07",
        r"Let $r$ and $n$ be nonnegative integers with $r\le n$. Then "
        r"$\displaystyle r!\,\varphi_{r+1}(n)=\sum_{k=0}^r(-1)^k\binom{r+1}{k}(r+1-k)^n$, "
        r"where $\varphi_k(n)$ are the coefficients in (6.1).",
    ),
    rec(
        "RN-P1-C03-Entry08",
        r"Let $n$ and $r$ be integers with $1\le r\le n+1$. Then "
        r"$\varphi_r(n+1)=r\,\varphi_r(n)+\varphi_{r-1}(n)$, where $\varphi_0(n)=0$.",
    ),
    rec(
        "RN-P1-C03-Entry08-Corollary",
        r"The first seven Bell polynomials $f_n(x)=\sum_{k=1}^{n+1}\varphi_k(n)x^k$ are "
        r"$f_0(x)=x$, $f_1(x)=x+x^2$, $f_2(x)=x+3x^2+x^3$, $f_3(x)=x+7x^2+6x^3+x^4$, "
        r"$f_4(x)=x+15x^2+25x^3+10x^4+x^5$, $f_5(x)=x+31x^2+90x^3+65x^4+15x^5+x^6$, "
        r"$f_6(x)=x+63x^2+301x^3+350x^4+140x^5+21x^6+x^7$.",
    ),
    rec(
        "RN-P1-C03-Entry08-Example01",
        r"Let $\varphi_1(n),\ldots,\varphi_{n+1}(n)$ be defined by (6.1). Let $\{a_k\}$, $1\le k<\infty$, be any "
        r"sequence of complex numbers such that "
        r"$\displaystyle\psi(z)=\sum_{k=1}^\infty\frac{(-1)^{k-1}a_k}{(z+1)(z+2)\cdots(z+k)}$ "
        r"has abscissa of convergence $A<\infty$. Define $F(j)=\sum_{k=1}^j a_k\varphi_k(j-1)$. "
        r"Let $R_E$ be as in (3.2) if $A=-\infty$, and if $A$ is finite let "
        r"$R_E=\{z:-\tfrac12\pi+\beta\le\arg(z-A)\le\tfrac12\pi-\beta\}$, $\beta>0$. "
        r"Then as $z\to\infty$ in $R_E$, "
        r"$\displaystyle\psi(z)\sim\sum_{k=0}^n\frac{(-1)^k F(k)}{z^{k+1}}$.",
    ),
    rec(
        "RN-P1-C03-Entry08-Example02",
        r"Let $r$ and $n$ be integers with $0\le r\le n$. Then $r!\,\varphi_{r+1}(n)$ is the coefficient of "
        r"$x^n/n!$ in the Maclaurin series of $e^x(e^x-1)^r$.",
    ),
    rec(
        "RN-P1-C03-Entry08-Example03",
        r"Let $n$ be a positive integer. Then "
        r"$\displaystyle f_{n-1}(x)=\sum_{k=0}^n\binom{n}{k}f_{k-1}(x)$.",
    ),
    rec(
        "RN-P1-C03-Entry08-Example04",
        r"Let $n\ge -1$ be an integer. Then "
        r"$\displaystyle\int_0^x f_n(t)\,dt=\sum_{k=0}^n\frac{n!}{(k+1)!}\,B_{n+1-k}\,\varphi_k(x)$, "
        r"where $B_m$ are Bernoulli numbers in Berndt's convention (11). "
        r"(Ramanujan's original statement used $n$ in place of $n+1$ on the right except in the subscripts.)",
    ),
    rec(
        "RN-P1-C03-Entry08-Example05i",
        r"For each nonnegative integer $n$, define $A_n$ by "
        r"$\displaystyle e^{A_n}=\sum_{k=1}^n\frac{k^n}{(k-1)!}=e^{f_n(1)}$. "
        r"Then $A_0=1$, $A_1=2$, $A_2=5$, $A_3=15$, $A_4=52$, $A_5=203$, $A_6=877$, $A_7=4140$, $A_8=21147$ "
        r"(Bell numbers $B(n)=A_{n-1}$, $n\ge 1$).",
    ),
    rec(
        "RN-P1-C03-Entry08-Example05ii",
        r"For each nonnegative integer $n$, define $C_n=\displaystyle\sum_{k=1}^n\frac{(-1)^k k^n}{e\,k!}$. "
        r"Then $C_0=-1$, $C_1=0$, $C_2=C_3=1$, $C_4=-2$, $C_5=C_6=-9$, $C_7=50$, $C_8=267$.",
    ),
    rec(
        "RN-P1-C03-Entry08-Example06",
        r"(i) $f_3(1)=3f_2(1)=15$; (ii) $f_5(1)+f_2(1)=4f_4(1)=208$; "
        r"(iii) $f_3(-1)=f_2(-1)=1$; (iv) $f_6(-1)=f_5(-1)=-9$; "
        r"(v) $f_5(-1)+f_6(-1)+f_8(-1)+f_3(-1)=5f_7(-1)=250$.",
    ),
    rec(
        "RN-P1-C03-Entry09i",
        r"As $z\to\infty$ in $R_e$ (defined by (3.2)), "
        r"$\displaystyle\sum_{k=0}^n\frac{(-1)^k F_k(x)}{z^{k+1}}"
        r"=\sum_{k=1}^{n+1}\frac{(-1)^{k-1}x^k}{(z+a+b)(z+a+2b)\cdots(z+a+kb)}+O(z^{-n-2})$, "
        r"where $F_n(a,b;x)$ is defined by (9.1).",
    ),
    rec(
        "RN-P1-C03-Entry09ii",
        r"If $a$, $b$, $x$, and $y$ are complex, then "
        r"$\displaystyle\Gamma(e^{by}-1)=\sum_{n=0}^\infty\frac{(by)^n}{n!}\,F_{n-1}(x)$.",
    ),
    rec(
        "RN-P1-C03-Entry09iii",
        r"For each nonnegative integer $n$, "
        r"$\displaystyle\sum_{k=0}^n\binom{n}{k}F_k(x)=F_{n+1}(x)$.",
    ),
    rec(
        "RN-P1-C03-Entry09iv",
        r"Suppose $r$ and $n$ are integers with $0<r\le n+1$. Then "
        r"$\displaystyle r!\sum_{k=0}^r\varphi_{r-k}(n)=\frac{(a+br)^n}{(r-1)!}$.",
    ),
    rec(
        "RN-P1-C03-Entry09v",
        r"Let $r$ and $n$ be as in Entry 9(iv). Then "
        r"$\displaystyle(r-1)!\,\varphi_r(n)=\sum_{k=0}^{r-1}(-1)^k\binom{r-1}{k}\{a+(r-k)b\}^n$.",
    ),
    rec(
        "RN-P1-C03-Entry09vi",
        r"Let $n$ and $r$ be integers with $1\le r\le n+1$. Then "
        r"$\varphi_r(n+1)=(a+br)\varphi_r(n)+b\,\varphi_{r-1}(n)$, where $\varphi_0(n)=0$.",
    ),
    rec(
        "RN-P1-C03-Entry09vii",
        r"Let $r$ and $n$ be integers with $0\le r\le n$. Then $r!\,\varphi_{r+1}(n)$ is the coefficient of "
        r"$x^n/n!$ in the Maclaurin series of $e^{(a+b)x}(e^{bx}-1)^r$.",
    ),
    rec(
        "RN-P1-C03-Entry09-Examplei",
        r"$\displaystyle\sum_{k=1}^\infty\frac{(-1)^k(2k+1)^2}{k!\,k}"
        r"=-\tfrac12\{F_3(-1,2;-1)+F_2(-1,2;-1)\}$.",
    ),
    rec(
        "RN-P1-C03-Entry09-Exampleii",
        r"$\displaystyle\sum_{k=1}^\infty\frac{(2k+1)!}{(k-1)!}=4\sum_{k=0}^\infty\frac{1}{k!}=4e$.",
    ),
    rec(
        "RN-P1-C03-Entry09-Exampleiii",
        r"$\displaystyle\sum_{k=1}^\infty\frac{(-1)^k(2k+1)^6}{k!\,k}"
        r"=\frac{F_4(-1,2;-1)}{e}=-\frac{41}{e}$ "
        r"(in Ramanujan's second notebook either side should be multiplied by $-1$).",
    ),
    rec(
        "RN-P1-C03-Entry09-Exampleiv",
        r"$\displaystyle\sum_{k=1}^\infty\frac{(-1)^k(2k+1)^4}{k!\,k}"
        r"=\sum_{k=1}^\infty\frac{(-1)^k}{k!\,k}-8$ "
        r"(Berndt notes: in the second notebook replace $-4$ by $-8$ on the right).",
    ),
    rec(
        "RN-P1-C03-Entry10",
        r"Let $\varphi(x)$ have at most polynomial growth as real $x\to\infty$. Suppose there exist $A\ge 1$ "
        r"and $G(x)$ of at most polynomial growth such that for each $m\ge 0$ and all large $x$, "
        r"$\varphi^{(m)}(x)$ exists and $|\varphi^{(m)}(x)|\le G(x)(A/x)^m m!$. Define "
        r"$\displaystyle\varphi_\infty(x)=\varphi(x)+\sum_{k=1}^\infty\frac{x^k}{k!}\varphi^{(k)}(k)$ "
        r"(the prime on the sum omits terms where $\varphi^{(k)}$ is undefined). "
        r"Then for any fixed $M>0$, as $x\to\infty$, "
        r"$\displaystyle\varphi_\infty(x)=\varphi(x)+\sum_{k=2}^M\sum_{n=k}^{2k-2}\frac{b_{kn}x^{n-k+1}}{n!}\varphi^{(n)}(x)"
        r"+O(G(x)x^{-M})$, "
        r"where $b_{kk}=1$, $b_{kn}=0$ for $n<k$ or $n>2k-2$, and "
        r"$b_{k+1,n+1}=nb_{k,n-1}+(n-k+1)b_{kn}$ for $k\le n\le 2k-1$.",
    ),
    rec(
        "RN-P1-C03-Entry10-Example01",
        r"As $x\to\infty$, "
        r"$\displaystyle\log\sum_{k=1}^\infty\frac{x^k\sqrt{k}}{k!}"
        r"=\tfrac12\log x-\frac{1}{8x}-\frac{7}{128x^2}+O(x^{-3})$.",
    ),
    rec(
        "RN-P1-C03-Entry10-Example02",
        r"As $x\to\infty$, "
        r"$\displaystyle e^{-x}\sum_{k=1}^\infty\frac{x^k\log(k+1)}{k!}"
        r"=\log x+\frac{1}{2x}+\frac{1}{12x^2}+O(x^{-3})$.",
    ),
    rec(
        "RN-P1-C03-Entry10-Example03",
        r"Ramanujan asserts that "
        r"$\displaystyle\log\sum_{k=0}^{100}\frac{(\log k)!}{k!}\approx 100\log\Bigl(\frac{\varphi(110)+\varphi(90)}{2}\Bigr)$ "
        r"using $\varphi(100!)\approx\varphi(100)$ and a midpoint approximation.",
    ),
    rec(
        "RN-P1-C03-Entry10-Example04",
        r"Let $\psi(x)=\sum_{k=1}^\infty x^{1/k}$. As $x\to\infty$, "
        r"$\displaystyle\sum_{k=1}^\infty\frac{x^k\psi(k)}{k!}=e^x\Bigl(\log x+\gamma+o(1/x)\Bigr)$, "
        r"where $\gamma$ is Euler's constant.",
    ),
    rec(
        "RN-P1-C03-Entry11",
        r"Suppose $f(x)=\sum_{n=1}^\infty A_n x^n/n$ is analytic for $|x|<R$. Define $P_n$, $0\le n<\infty$, by "
        r"$\displaystyle\sum_{n=0}^\infty P_n x^n=\exp\{f(x)\}$ for $|x|<R$. Then for $n\ge 1$, "
        r"$\displaystyle nP_n=\sum_{k=1}^n A_k P_{n-k}$.",
    ),
    rec(
        "RN-P1-C03-Entry11-Corollary",
        r"Let $\{a_k\}$, $1\le k<\infty$, satisfy $\sum_{k=1}^\infty|a_k|<\infty$. Let $S_n=\sum_{k=1}^\infty a_k^n$ "
        r"for positive integer $n$. For $n\ge 1$, let $P_n$ be the sum of all products of $n$ distinct terms "
        r"from $\{a_k\}$, with $P_0=1$. Then $\displaystyle nP_n=\sum_{k=1}^n(-1)^{k-1}S_k P_{n-k}$ for $n\ge 1$.",
    ),
    rec(
        "RN-P1-C03-Entry12",
        r"For integral $r$ and complex $n$, with $F_r(n)=\sum_{k=0}^\infty(n+k)^{r+k}a^k/k!$ convergent as in (12.1), "
        r"$\displaystyle F_{r+1}(n)=nF_r(n)+\frac{1}{a}F_{r+1}(n+1)$.",
    ),
    rec(
        "RN-P1-C03-Entry12-Corollary",
        r"Let $p$ and $q$ be constants. The polynomials $f_0(x)=1$, $f_1(x)=x$, and "
        r"$\displaystyle f_n(x)=\frac{1}{n!}\sum_{k=1}^{n-1}\prod_{j=1}^{k-1}(x+np-jq)$ for $n\ge 2$ "
        r"satisfy $\displaystyle f_n(x+y)=\sum_{k=0}^n f_k(x)f_{n-k}(y)$ (Gould polynomials).",
    ),
    rec(
        "RN-P1-C03-Entry13",
        r"Let $f(n)=nF_{-1}(n)$, where $F_{-1}$ is defined by (12.1). If $a$ is real with $|a|\ge e$, "
        r"there exists a positive real $x$ with $x=a\log x$ such that $x^n=f(n)$ for every real $n$.",
    ),
    rec(
        "RN-P1-C03-Entry13-Corollary",
        r"Let $z$ be complex and $w$ complex with $|e^w-1|\ge|w|$. Then "
        r"$\displaystyle e^z=\sum_{k=0}^\infty\frac{z(z+kw)^{k-1}e^{-kw}}{k!}$.",
    ),
    rec(
        "RN-P1-C03-Entry14",
        r"Let $\varphi$ be defined by (14.2) with $c_k(n)$ as in (14.1). If $x$ is a root of $aqx^p-x^q+1=0$, "
        r"then $\varphi(n)=x^n$ for every real $n$.",
    ),
    rec(
        "RN-P1-C03-Entry14-Corollary01",
        r"Let $n$ be real with $|a|\le 1/4$. Then "
        r"$\displaystyle\left(\frac{1+\sqrt{1-4a}}{2}\right)^n"
        r"=1+na+n\sum_{k=2}^\infty\frac{\Gamma(n+2k)}{\Gamma(n+k+1)k!}"
        r"\binom{2k-1}{k,k-1,\ldots,1,1}a^k$.",
    ),
    rec(
        "RN-P1-C03-Entry14-Corollary02",
        r"Let $n$ be real with $|a|\le 1$. Then "
        r"$\displaystyle(a+\sqrt{a^2+1})^n=1+na+\sum_{k=2}^\infty b_k(n)a^k$, "
        r"where $b_k(n)=n^2(n^2-2^2)\cdots(n^2-(k-2)^2)$ if $k$ is even and "
        r"$b_k(n)=n(n^2-1^2)\cdots(n^2-(k-2)^2)$ if $k$ is odd.",
    ),
    rec(
        "RN-P1-C03-Entry15",
        r"Define $u$, $0<u<1$, by $u-\log u=1+x^2/2$ where $x$ is real. Then "
        r"$\displaystyle e^{-k(1+x^2/2)/u}=\sum_{k=0}^\infty\frac{(k+1)^{k-1}}{k!}e^{-k(1+x^2/2)}$. "
        r"For sufficiently small $x>0$, $\displaystyle u=\sum_{k=0}^\infty b_k x^k$ with $b_0=1$, $b_1=-1$, "
        r"$b_2=1/3$, $b_3=-1/36$, $b_4=-1/270$, and higher $b_k$ from "
        r"$\tfrac12 x^2=\sum_{i=2}^\infty(1-u)^i/i$.",
    ),
    rec(
        "RN-P1-C03-Entry15-Example01",
        r"Let $m$ be real and $0<n\le 2$. Then "
        r"$\displaystyle 2^m=\sum_{k=0}^\infty\frac{m\,\Gamma(m+kn)}{\Gamma(m+kn-k+1)^2\,n^k k!}$. "
        r"The series converges for $0<n<\infty$ but equals $2^m$ only for $0<n\le 2$.",
    ),
    rec(
        "RN-P1-C03-Entry15-Example02",
        r"Let $a>0$ and $m,n,p$ be real and nonzero. Define $x>0$ by $(\log x)^m=ax^n$. "
        r"Then for $|m/n|a^{-1/m}\ge e$, "
        r"$\displaystyle x^p=\sum_{k=0}^\infty\frac{m\Gamma(mp/n+k)}{\Gamma(mp/n+k-1+1)\,(ma^{-1/m}/n)^k k!}$.",
    ),
    rec(
        "RN-P1-C03-Entry15-Example03iii",
        r"Let $a$ be real with $|a|\le e$ and $x$ defined by $x=ae^{\pm x}$. Then "
        r"$\displaystyle e^{-x}=\sum_{k=0}^\infty\frac{(k+1)^{k-1}(-a)^k}{k!}$ "
        r"(with $+$ on the exponent for $x=ae^x$ and $-$ for $x=ae^{-x}$).",
    ),
    rec(
        "RN-P1-C03-Entry15-Example03v",
        r"Let $a>0$ with $|\log a|\le e$ and $x>0$ defined by $x\pm x=a$. Then "
        r"$\displaystyle\frac{1}{x}=\sum_{k=0}^\infty\frac{(k+1)^{k-1}(\pm\log a)^k}{k!}$.",
    ),
    rec(
        "RN-P1-C03-Entry15-Example03vii",
        r"Let $a$ be real and $x$ defined by $e^x\pm x=a$. If $a\le -1$, "
        r"$\displaystyle e^x=\sum_{k=0}^\infty\frac{(k+1)^{k-1}(-a)^k}{k!}$; "
        r"if $a\ge 1$, $\displaystyle e^x=\sum_{k=0}^\infty\frac{(k+1)^{k-1}e^{-ak}}{k!}$.",
    ),
    rec(
        "RN-P1-C03-Entry15-Example04i",
        r"Let $x>0$ and $v=x^x$. For $|\log x|\le 1/e$, "
        r"$\displaystyle v=\sum_{k=0}^\infty\frac{(k+1)^{k-1}(\log x)^k}{k!}$.",
    ),
    rec(
        "RN-P1-C03-Entry16a",
        r"If $r$ is an integer and $n$ any complex number, with $\varphi_r(n)$ defined by $x^r\varphi_r(n)=F_r(n)$ "
        r"and $x=a\log x$, then "
        r"$n\varphi_r(n)=\varphi_{r+1}(n)-(\log x)\varphi_{r+1}(n+1)$.",
    ),
    rec(
        "RN-P1-C03-Entry16b",
        r"Let $r$ and $t$ be integers with $1\le t\le r+2$. Then "
        r"$\psi_t(r+1,n)=(n-1)\psi_t(r,n-1)+\psi_{t-1}(r+1,n)-\psi_{t-1}(r+1,n-1)$, "
        r"where $\psi_t(r,n)=0$ unless $1\le t\le r+1$, and $\varphi_r(n)=\sum_{k=1}^{r+1}\psi_k(r,n)/(1-\log x)^{r+k}$.",
    ),
    rec(
        "RN-P1-C03-Entry16-Corollary01",
        r"Let $x$ be complex. If $-p<n<1$ where $p\approx 0.27846$ is the unique real root of $ye^{y+1}=1$, then "
        r"$\displaystyle e^x=\sum_{k=0}^\infty\frac{(x/n)^k(x/n+k)^{k-1}}{k!}$. "
        r"If $n>1$ and $0<m<1$ with $e^m/m=e^n/n$, then "
        r"$\displaystyle 1-\frac{1}{m}=\sum_{k=0}^\infty\frac{(yn+kn)^k}{e^{kn}k!}$.",
    ),
    rec(
        "RN-P1-C03-Entry16-Corollary02",
        r"For each nonnegative integer $r$, "
        r"$\displaystyle n^r=\lim_{a\to\infty}\varphi_r(n)=\sum_{k=1}^{r+1}\psi_k(r,n)$.",
    ),
    rec(
        "RN-P1-C03-Entry17",
        r"For $r\ge 2$, with $A_k$ the coefficients in $x-a=\sum_{k=1}^\infty(-1)^{k-1}A_k(h/a)^k/k!$ "
        r"from $x^x=aa^h$ (so $A_1=n=1/(1+\log a)$), "
        r"$\displaystyle\frac{A_r}{(r-1)!}=n(r-2)A_{r-1}+n\sum_{k=1}^{r-1}\frac{k}{k!}A_k A_{r-k}$.",
    ),
    rec(
        "RN-P1-C03-Entry17-Example01",
        r"For $n=1$ and $r\ge 2$, $\displaystyle\sum_{k=0}^{r-2}a(r,k)=A_r=(r-1)r!$.",
    ),
    rec(
        "RN-P1-C03-Entry17-Example02",
        r"Fix $a$, $0<a<e$. For real $h$, define $x>0$ by $x^x=a^{1/a}e^h$. Then for small $|h|$, "
        r"$\displaystyle\frac{a}{x}=1-\sum_{k=1}^\infty\frac{A_k(ah)^k}{k!}$.",
    ),
]
