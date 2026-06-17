"""Part I, Chapter 7 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C07 = ["sums-of-powers-bernoulli-gamma"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C07}


CHAPTER_7 = [
    rec(
        "RN-P1-C07-Entry01",
        r"Let $\displaystyle\varphi_r(x)=\sum_{k=1}^x k^r$ (1.1), where $r$ is any complex number. "
        r"If $r\ne -1$, then as $x\to\infty$, "
        r"$\displaystyle\varphi_r(x)\sim\zeta(-r)+\frac{x^{r+1}}{r+1}+\frac{x^r}{2}"
        r"+\sum_{k=1}^\infty\frac{B_{2k}r(r+1)x^{r-2k+1}}{(2k)!\,r(r-2k+2)}$ (1.2).",
    ),
    rec(
        "RN-P1-C07-Entry02",
        r"For each complex number $r$, "
        r"$\displaystyle\eta(-r)=\frac{(2^{r+1}-1)B^*_r\sin(\pi r/2)}{r+1}$.",
    ),
    rec(
        "RN-P1-C07-Entry02-Corollary",
        r"If $r$ is complex and $r\ne -1$, then "
        r"$\displaystyle\varphi_r\!\left(-\tfrac12\right)"
        r"=\frac{(2-2^{-r})B^*_r\cos\{\pi(r+1)/2\}}{r+1}$.",
    ),
    rec(
        "RN-P1-C07-Entry03",
        r"Let $\varphi_r(x)$ be defined by (2.4) and let $a$ and $b$ be complex numbers with $b\ne 0$. Then "
        r"$\displaystyle\sum_{k=1}^x(a+kb)^r=b^r\left\{\varphi_r\!\left(x+\frac{a}{b}\right)"
        r"-\varphi_r\!\left(\frac{a}{b}\right)\right\}$.",
    ),
    rec(
        "RN-P1-C07-Entry04",
        r"For any complex number $r$, "
        r"$\displaystyle\frac{\sin(\pi r/2)B^*_{1-r}}{\zeta(-r)}"
        r"=\frac{(2\pi)^r B^*_r}{2^r(r+1)}$ (4.1).",
    ),
    rec(
        "RN-P1-C07-Entry04-Corollary01",
        r"We have $B^*_{1/2}=2\zeta(3)$, $B^*_{3/2}=-4\zeta(5)$, $B^*_{5/2}=6\zeta(7)$, and "
        r"$B^*_{7/2}=-8\zeta(9)$.",
    ),
    rec(
        "RN-P1-C07-Entry04-Corollary02",
        r"$\displaystyle\zeta\!\left(\tfrac12\right)=\pi$.",
    ),
    rec(
        "RN-P1-C07-Entry04-Corollary03",
        r"For every complex number $z$, "
        r"$\displaystyle\Gamma(z)\Gamma(1-z)=\frac{\pi}{\sin(\pi z)}$.",
    ),
    rec(
        "RN-P1-C07-Entry04-Corollary04",
        r"$\displaystyle\sum_{k=0}^\infty\frac{(-1)^k}{\sqrt{2k}+\sqrt{2k+2}}"
        r"=\sum_{k=0}^\infty\frac{1}{(2k+1)^{3/2}}$.",
    ),
    rec(
        "RN-P1-C07-Entry04-Corollary05",
        r"Let $\eta(s)$ be defined by (2.1). Then "
        r"$\displaystyle(2\pi)^{1/3}\eta\!\left(\tfrac13\right)=(1+2^{1/3})\Gamma\!\left(\tfrac13\right)\zeta\!\left(\tfrac13\right)$.",
    ),
    rec(
        "RN-P1-C07-Entry04-Corollary06",
        r"As $x\to\infty$, "
        r"$\displaystyle\sum_{k=1}^x\frac{1}{\sqrt{k}}\sim\sqrt{2x}+\frac{1}{2\sqrt{2x}}"
        r"-\frac{1}{24x^{3/2}}+\sum_{k=2}^\infty\frac{B_{2k}\,1\cdot 3\cdots(4k-3)}{2^{2k-1}(2k)!\,x^{2k-1/2}}$ (4.3). "
        r"(Berndt notes Ramanujan's notebook approximation $\sum_{k=1}^x k^{-1/2}\sim\sqrt{2+4x}+\zeta(-\tfrac12)$ "
        r"is incompatible with (4.3).)",
    ),
    rec(
        "RN-P1-C07-Entry04-Corollary07",
        r"As $x\to\infty$, "
        r"$\displaystyle\sum_{k=1}^x k^{1/2}\sim\frac{2x^{3/2}}{3}+\frac{x^{1/2}}{2}"
        r"-\frac{\zeta(-\tfrac12)}{4x^{1/2}}+\sum_{k=2}^\infty\frac{B_{2k}\,1\cdot 3\cdots(4k-5)}{2^{2k}(2k)!\,x^{2k-3/2}}$ (4.5). "
        r"(Berndt notes Ramanujan's claim $\sum_{k=1}^x k^{1/2}\sim\sqrt{(x+\tfrac12)(x+\tfrac14)(x+\tfrac34)-\tfrac14\zeta(-\tfrac12)}$ "
        r"is incompatible with (4.5), though it gives a good numerical approximation.)",
    ),
    rec(
        "RN-P1-C07-Entry04-Corollary08",
        r"As $x\to\infty$, "
        r"$\displaystyle\sum_{k=1}^x k^{3/2}\sim\frac{2x^{5/2}}{5}+\frac{x^{3/2}}{2}+\frac{x^{1/2}}{8}"
        r"-\frac{3\zeta(-\tfrac12)}{16\pi^2}-\sum_{k=2}^\infty\frac{B_{2k}\,1\cdot 3\cdots(4k-7)}{2^{2k-1}(2k)!\,x^{2k-5/2}}$ (4.7). "
        r"(Berndt notes Ramanujan's polynomial radical approximation for this sum is incompatible with (4.7).)",
    ),
    rec(
        "RN-P1-C07-Entry05",
        r"Let $a$ and $b$ be complex numbers with $b\ne 0$ and $a/b$ not a negative integer. "
        r"If $\Re(r)<-1$, then "
        r"$\displaystyle\sum_{k=1}^\infty(-1)^{k+1}(a+kb)^r=(2b)^r\left\{\varphi_r\!\left(\frac{a}{b}\right)"
        r"-\varphi_r\!\left(\frac{a}{2b}\right)\right\}$ (5.1).",
    ),
    rec(
        "RN-P1-C07-Entry06i",
        r"Let $x$ be a positive integer and assume that $n>0$. Then "
        r"$\displaystyle(x^2+x)^n=2\sum_{k=0}^n\binom{n}{2k+1}\varphi_{2n-2k-1}(x)$.",
    ),
    rec(
        "RN-P1-C07-Entry06ii",
        r"Under the same hypotheses as Entry 6(i), "
        r"$\displaystyle\left(x+\tfrac12\right)(x^2+x)^n"
        r"=\sum_{k=0}^n\left\{2\binom{n}{2k+1}+\binom{n}{2k}\right\}\varphi_{2n-2k}(x)$.",
    ),
    rec(
        "RN-P1-C07-Entry06-Corollary01",
        r"Let $y=x^2+x$ and $a=x+\tfrac12$. Then "
        r"$\varphi_1(x)=\tfrac12 y$, "
        r"$\varphi_2(x)=\tfrac16 ay$, "
        r"$\varphi_3(x)=\tfrac12 y^2$, "
        r"$\varphi_4(x)=\tfrac16 ay(y-\tfrac12)$, "
        r"$\varphi_5(x)=\tfrac12(y-\tfrac12)$, "
        r"$\varphi_6(x)=\tfrac16 ay(y^3-2y^2+\tfrac14-\tfrac12)$, "
        r"$\varphi_9(x)=\tfrac{1}{30}y^2(y-1)(y^2-\tfrac12+1)$, "
        r"$\varphi_{10}(x)=\tfrac{1}{42}ay(y-1)(y^3-\tfrac12 y^2+\tfrac{1}{30}y-\tfrac16)$, and "
        r"$\varphi_{11}(x)=\tfrac{1}{12}y^2(y^4-4y^3+\tfrac{127}{30}y^2-10y+5)$.",
    ),
    rec(
        "RN-P1-C07-Entry06-Corollary02",
        r"For each positive integer $n$, "
        r"(i) $\displaystyle\sum_{k=1}^n(2k-1+\sqrt5)^9=\varphi_9\!\left(2n-1+\sqrt5\right)$; "
        r"(ii) $\displaystyle\sum_{k=1}^n(2k-1+\sqrt5)^{10}"
        r"=(2n-1+\sqrt5)\,\varphi_{10}\!\left(\tfrac{2n-1+\sqrt5}{2}\right)$; and "
        r"(iii) if $p$ and $n$ are positive integers with $n$ even, then "
        r"$\displaystyle\sum_{k=1}^p(2k-1)^n=2^n\varphi_n\!\left(p+\tfrac12\right)$.",
    ),
    rec(
        "RN-P1-C07-Entry07",
        r"If $r$ is a positive integer, then "
        r"$\varphi_r(x-1)+(-1)^r\varphi_r(-x)=0$.",
    ),
    rec(
        "RN-P1-C07-Entry07-Corollary",
        r"If $r$ is a positive integer exceeding $1$, then $\varphi_r(x)$ is divisible by "
        r"$x^2(x+1)^2$ or $x(x+\tfrac12)(x+1)$ according as $r$ is odd or even.",
    ),
    rec(
        "RN-P1-C07-Entry08",
        r"If $r$ is a positive integer, then "
        r"$\displaystyle\varphi_r(x)=\frac1{r+1}\sum_{k=0}^{r+1}\binom{r+1}{k}B_k x^{r+1-k}+x^r"
        r"=\frac{x}{r+1}+\frac{x^r}{2}-\frac{2}{r}\sum_{k=1}^{\lfloor r/2\rfloor}"
        r"\binom{r+1}{2k}\frac{B_{2k}}{2k}\{(1-2k)x^{r+1-2k}-2k\}$ (8.1).",
    ),
    rec(
        "RN-P1-C07-Entry10",
        r"For each complex number $r$ and each positive integer $n$, "
        r"$\displaystyle\varphi_r(x)-n^r\sum_{k=0}^{n-1}\varphi_r\!\left(\frac{x-k}{n}\right)"
        r"=(1-n^{r+1})\zeta(-r)"
        r"=\frac{n^{r+1}-1}{r+1}\,\sin\!\left(\frac{\pi r}{2}\right)B^*_r$ (10.1).",
    ),
    rec(
        "RN-P1-C07-Entry10-Corollary",
        r"Under the hypotheses of Entry 10, "
        r"$\displaystyle\sum_{k=1}^{n-1}\varphi_r\!\left(-\frac{k}{n}\right)=(n-n^{-r})\zeta(-r)$.",
    ),
    rec(
        "RN-P1-C07-Entry11",
        r"If $r$ is a positive integer, then "
        r"$\displaystyle\varphi_{-r}(x-1)+(-1)^r\varphi_{-r}(-x)"
        r"=\{1+(-1)^r\}\zeta(r)+\frac{(-1)^r}{(r-1)!}\frac{d^{r-1}}{dx^{r-1}}\bigl(\pi\cot(\pi x)\bigr)$ (11.1), "
        r"where if $r=1$, the first expression on the right side of (11.1) is understood to be $0$.",
    ),
    rec(
        "RN-P1-C07-Entry11-Corollary01",
        r"If $r$ is any complex number, then "
        r"$\displaystyle\varphi_r(x)-2^r\left\{\varphi_r\!\left(\frac{x}{2}\right)+\varphi_r\!\left(\frac{x-1}{2}\right)\right\}"
        r"=(1-2^{r+1})\zeta(-r)$.",
    ),
    rec(
        "RN-P1-C07-Entry11-Corollary02",
        r"If $r$ is any complex number, then "
        r"$\displaystyle\varphi_r\!\left(-\tfrac12\right)=(2-2^{-r})\zeta(-r)$.",
    ),
    rec(
        "RN-P1-C07-Entry11-Corollary03",
        r"If $r$ is any complex number, then "
        r"$\displaystyle\varphi_r(-1)+\varphi_r\!\left(-\tfrac12\right)=(3-3^{-r})\zeta(-r)$.",
    ),
    rec(
        "RN-P1-C07-Entry11-Corollary04",
        r"If $r$ is any complex number, then "
        r"$\displaystyle\varphi_r\!\left(-\tfrac13\right)+\varphi_r\!\left(-\tfrac23\right)"
        r"=(2+2^{-r}-4^{-r})\zeta(-r)$.",
    ),
    rec(
        "RN-P1-C07-Entry11-Corollary05",
        r"If $r$ is any complex number, then "
        r"$\displaystyle\varphi_r\!\left(-\tfrac16\right)+\varphi_r\!\left(-\tfrac12\right)"
        r"=(1+2^{-r}+3^{-r}-6^{-r})\zeta(-r)$.",
    ),
    rec(
        "RN-P1-C07-Entry11-Example01",
        r"If $r$ is a positive odd integer, then "
        r"$\displaystyle\varphi_r(-1)=\frac{(3-3^{-r})\zeta(-r)}{2}$.",
    ),
    rec(
        "RN-P1-C07-Entry11-Example02",
        r"If $r$ is a positive odd integer, then "
        r"$\displaystyle\varphi_r\!\left(-\tfrac12\right)=(2^{-r}-2^{2r-1})\zeta(-r)$.",
    ),
    rec(
        "RN-P1-C07-Entry11-Example03",
        r"If $r$ is a positive odd integer, then "
        r"$\displaystyle\varphi_r\!\left(-\tfrac13\right)=\frac{(1+2^{-r}+3^{-r}-6^{-r})\zeta(-r)}{2}$.",
    ),
    rec(
        "RN-P1-C07-Entry11-Example04",
        r"If $r$ is a positive odd integer, then "
        r"$\displaystyle\varphi_r\!\left(-\tfrac12\right)+\varphi_r\!\left(-\tfrac23\right)=\frac{(5-5^{-r})\zeta(-r)}{2}$.",
    ),
    rec(
        "RN-P1-C07-Entry11-Example05",
        r"If $r$ is a positive odd integer, then "
        r"$\displaystyle\varphi_r\!\left(-\tfrac14\right)+\varphi_r\!\left(-\tfrac34\right)"
        r"=(2+2^{-2r-1}-2^{-3r-1})\zeta(-r)$.",
    ),
    rec(
        "RN-P1-C07-Entry11-Example06",
        r"If $r$ is a positive odd integer, then "
        r"$\displaystyle\varphi_r\!\left(-\tfrac{11}{30}\right)+\varphi_r\!\left(-\tfrac{13}{30}\right)"
        r"=\frac{(3+2^r+5^{-r}-10^{-r})\zeta(-r)}{2}$ "
        r"(Berndt notes Ramanujan's notebook value for this example is incorrect).",
    ),
    rec(
        "RN-P1-C07-Entry11-Example07",
        r"If $r$ is a positive odd integer, then "
        r"$\displaystyle\varphi_r\!\left(-\tfrac{11}{12}\right)+\varphi_r\!\left(-\tfrac{13}{12}\right)"
        r"=\frac{(4-2^{-r}+4^{-r}+6^{-r}-12^{-r})\zeta(-r)}{2}$ "
        r"(Berndt notes Ramanujan's notebook value for this example is incorrect).",
    ),
    rec(
        "RN-P1-C07-Entry12",
        r"For every complex number $r$, "
        r"$\displaystyle 2^r\bigl\{\varphi_r\!\left(-\tfrac13\right)-\varphi_r\!\left(-\tfrac23\right)\bigr\}"
        r"=(2^r+1)\bigl\{\varphi_r\!\left(-\tfrac16\right)-\varphi_r\!\left(-\tfrac56\right)\bigr\}$ (12.1).",
    ),
    rec(
        "RN-P1-C07-Entry12-Example01",
        r"Example 1 is the trivial case of the general formulae for extended Bernoulli numbers "
        r"$B^*_r$ cited below.",
    ),
    rec(
        "RN-P1-C07-Entry12-Example02",
        r"For a positive odd integer $p$, the value $B^*_{p-2n-1}\!\left(-\tfrac12\right)$ is given by "
        r"Hansen's tables [6.3.10].",
    ),
    rec(
        "RN-P1-C07-Entry12-Example03",
        r"For a positive odd integer $p$, the value $B^*_{p-2n-1}\!\left(-\tfrac13\right)$ is given by "
        r"Hansen's tables [6.3.18].",
    ),
    rec(
        "RN-P1-C07-Entry12-Example04",
        r"For a positive odd integer $p$, the value $B^*_{p-2n-1}\!\left(-\tfrac16\right)$ is given by "
        r"Hansen's tables [6.3.23].",
    ),
    rec(
        "RN-P1-C07-Entry13",
        r"For each nonnegative integer $k$, define "
        r"$\displaystyle c_k=\lim_{m\to\infty}\sum_{j=1}^m\left\{\frac{(\log j)^k}{j}-\frac{(\log j)^{k+1}}{j(k+1)}\right\}$. "
        r"Then for all $s$, "
        r"$\displaystyle\zeta(s)=\frac{1}{s-1}+\sum_{k=0}^\infty\frac{(-1)^k c_k(s-1)^k}{k!}$ (13.2). "
        r"In particular, if $A_k=(-1)^k c_k/k!$, $0\le k<\infty$, then "
        r"$A_0=\gamma=0.5772156649$, $A_1=0.0728158455$, $A_2=-0.00485$, and $A_3=-0.00034$, "
        r"where $\gamma$ denotes Euler's constant (13.3).",
    ),
    rec(
        "RN-P1-C07-Entry13-Example01",
        r"For $|\eta|$ sufficiently small, "
        r"$\zeta(1+\eta)+\zeta(1-\eta)=1+0.00839\eta^2-0.0001\eta^4+\cdots$.",
    ),
    rec(
        "RN-P1-C07-Entry13-Example02",
        r"$\zeta\!\left(\tfrac65\right)=10.58444842$.",
    ),
    rec(
        "RN-P1-C07-Entry13-Example03",
        r"$\zeta(3)=2.6123752$.",
    ),
    rec(
        "RN-P1-C07-Entry13-Example04",
        r"$\zeta\!\left(\tfrac32\right)=1.341490$.",
    ),
    rec(
        "RN-P1-C07-Entry13-Example05",
        r"$B^*_{1/2}=0.4409932$ and $B^*_{3/2}=-1.032627$.",
    ),
    rec(
        "RN-P1-C07-Entry13-Example06",
        r"$B^*_{5/3}=-0.9420745$ and $B^*_{11/3}=-1.3841347$.",
    ),
    rec(
        "RN-P1-C07-Entry13-Example07",
        r"$B^*_{11/2}=-1.847228$.",
    ),
    rec(
        "RN-P1-C07-Entry14",
        r"Let $\eta>0$. Then as $\eta\to 0$, "
        r"$\displaystyle\sum_{k=2}^\infty\frac{1}{k(k\eta-1)}\sim\frac{a_0}{\eta}-\log\eta"
        r"+a_1+\sum_{k=1}^\infty a_{k+1}\eta^{2k-1}$ (14.1), "
        r"where $\displaystyle a_0=\lim_{m\to\infty}\left(\sum_{k=2}^m\frac{1}{k\log k}-\log\log m\right)=0.7946786$ (14.2), "
        r"$a_1=\tfrac12(1-\gamma)=0.2113922$, and "
        r"$\displaystyle a_{k+1}=-\frac{B_{2k}(2k-1)}{2k}$ for $k\ge 1$, "
        r"where $B_j$ denotes the $j$th Bernoulli number and $A_j$ is defined in Entry 13, $0\le j<\infty$. "
        r"In particular, $a_2=-0.0060680$ and $a_3=-0.000000475$ "
        r"(Berndt notes Ramanujan's value $-0.0000028$ for $a_3$ is incorrect).",
    ),
    rec(
        "RN-P1-C07-Entry14-Corollary01",
        r"$\displaystyle a_0=\lim_{m\to\infty}\left(\sum_{k=2}^m\frac{1}{k\log k}-\log\log m\right)=0.7946786$ (14.2).",
    ),
    rec(
        "RN-P1-C07-Entry14-Corollary02",
        r"For $s>0$, "
        r"$\displaystyle\sum_{k=2}^\infty\frac{1}{k^{s+1}\log k}=-\log s+C+(1-\gamma)s-\sum_{k=2}^\infty\frac{A_{k-1}s^k}{k!}$ (14.11), "
        r"where "
        r"$\displaystyle C=\sum_{k=2}^\infty\frac{1}{k^2\log k}-1+\gamma+\sum_{k=2}^\infty\frac{A_{k-1}}{k!}$ (14.12), "
        r"and where $A_k$, $1\le k<\infty$, is defined in Entry 13. Furthermore, "
        r"$C=0.2174630$, $1-\gamma=0.4227843$, $-\tfrac12 A_1=-0.0364079$, $-\tfrac14 A_2=0.001615$, "
        r"$-\tfrac18 A_3=0.000086$, and $-\tfrac1{16}A_4=-0.00002$.",
    ),
    rec(
        "RN-P1-C07-Entry15",
        r"Let $\Re(r)>-1$ and $0<x<1$. Then "
        r"$\displaystyle\frac{\varphi_r(x-1)-\varphi_r(-x)}{4\Gamma(r+1)}"
        r"=-\cos\!\left(\frac{\pi r}{2}\right)\sum_{k=1}^\infty\frac{\sin(2\pi k x)}{(2\pi k)^{r+1}}$.",
    ),
    rec(
        "RN-P1-C07-Entry16",
        r"Let $\Re(r)>-1$ and $0<x<1$. Then "
        r"$\displaystyle\frac{\varphi_r(x-1)+\varphi_r(-x)-2\zeta(-r)}{4\Gamma(r+1)}"
        r"=\sin\!\left(\frac{\pi r}{2}\right)\sum_{k=1}^\infty\frac{\cos(2\pi k x)}{(2\pi k)^{r+1}}$.",
    ),
    rec(
        "RN-P1-C07-Entry16-Corollary16i",
        r"Let $p$ and $q$ be integers with $0<p<q$. Then if $r$ is any complex number, "
        r"$\displaystyle\frac{(2\pi q)^r}{4\Gamma(r)}\left\{\varphi_{r-1}\!\left(\frac{p}{q-1}\right)"
        r"-\varphi_{r-1}\!\left(-\frac{p}{q}\right)\right\}"
        r"=-\sin\!\left(\frac{\pi r}{2}\right)\sum_{j=1}^{q-1}\sin\!\left(\frac{2\pi jp}{q}\right)"
        r"\left\{\zeta(r)-\varphi_{-r}\!\left(\frac{j}{q}\right)\right\}$ (16.1).",
    ),
    rec(
        "RN-P1-C07-Entry16-Corollary16ii",
        r"Let $p$ and $q$ be integers with $0<p<q$. For any complex number $r$, "
        r"$\displaystyle\frac{(2\pi q)^r}{4\Gamma(r)}\left\{\varphi_{r-1}\!\left(\frac{p}{q-1}\right)"
        r"+\varphi_{r-1}\!\left(-\frac{p}{q}\right)-2(1-q^{-r})\zeta(1-r)\right\}"
        r"=-\cos\!\left(\frac{\pi p}{q}\right)\sum_{j=1}^{q-1}\cos\!\left(\frac{2\pi jp}{q}\right)"
        r"\left\{\zeta(r)-\varphi_{-r}\!\left(\frac{j}{q}\right)\right\}$ (16.2).",
    ),
    rec(
        "RN-P1-C07-Entry17",
        r"For each complex number $r$, "
        r"$\displaystyle\varphi_r\!\left(-\tfrac14\right)-\varphi_r\!\left(-\tfrac34\right)"
        r"=\frac{2\cos(\pi r/2)E^*_{r+1}}{4^{r+1}}$.",
    ),
    rec(
        "RN-P1-C07-Entry17-Corollary",
        r"For $\Re(r)<0$, "
        r"$\displaystyle\frac{2\cos(\pi r/2)E^*_{r+1}}{4^{r+1}}"
        r"=\varphi_r\!\left(-\tfrac14\right)-\varphi_r\!\left(-\tfrac34\right)"
        r"=4^{-r}\sum_{k=0}^\infty(-1)^k(2k+1)^r$.",
    ),
    rec(
        "RN-P1-C07-Entry18",
        r"For each complex number $r$, "
        r"$\displaystyle\frac{\cos(\pi r/2)E^*_{1-r}}{2^r}=2L(r)=\frac{(\pi/2)^r E^*_r}{\Gamma(r)}$ (18.1).",
    ),
    rec(
        "RN-P1-C07-Entry18-Corollary",
        r"$\displaystyle\sum_{k=1}^\infty\frac{(-1)^k}{\sqrt{2k-1}+\sqrt{2k+1}}=L\!\left(\tfrac12\right)$.",
    ),
    rec(
        "RN-P1-C07-Entry19i",
        r"Assume the hypotheses of Corollary 16(i) with the additional assumption that $q$ is odd. Then "
        r"$\displaystyle\frac{(2\pi q)^r}{4\Gamma(r)}\left\{\varphi_{r-1}\!\left(\frac{p}{q-1}\right)"
        r"-\varphi_{r-1}\!\left(\frac{p}{q}\right)\right\}"
        r"=\sin\!\left(\frac{\pi r}{2}\right)^{(q-1)/2}\sum_{j=1}^{q-1}\sin\!\left(\frac{2\pi jp}{q}\right)"
        r"\left\{\varphi_{-r}\!\left(\frac{j}{q-1}\right)-\varphi_{-r}\!\left(\frac{j}{q}\right)\right\}$.",
    ),
    rec(
        "RN-P1-C07-Entry19ii",
        r"Suppose that all hypotheses of Corollary 16(ii) hold and that $q$ is odd. Then "
        r"$\displaystyle\frac{(2\pi q)^r}{4\Gamma(r)}\left\{\varphi_{r-1}\!\left(\frac{p}{q-1}\right)"
        r"+\varphi_{r-1}\!\left(\frac{p}{q}\right)-2\zeta(1-r)\right\}"
        r"=\cos\!\left(\frac{\pi r}{2}\right)^{(q-1)/2}\sum_{j=1}^{q-1}\cos\!\left(\frac{2\pi jp}{q}\right)"
        r"\left\{\varphi_{-r}\!\left(\frac{j}{q-1}\right)+\varphi_{-r}\!\left(-\frac{j}{q}\right)\right\}$ "
        r"(Berndt notes Ramanujan's notebook version is incorrect).",
    ),
    rec(
        "RN-P1-C07-Entry19-Corollary01",
        r"Let $\Re(r)>0$ and suppose that $0\le x<1$. Then "
        r"$\displaystyle\frac{2^{r-1}\pi^{r+1}}{\Gamma(r+1)}\varphi_r(-x)"
        r"=\sum_{k=1}^\infty\frac{\sin(\pi k x)\cos(\pi k x+\pi r/2)}{k^{r+1}}$.",
    ),
    rec(
        "RN-P1-C07-Entry19-Corollary02",
        r"If $0<x<1$, then "
        r"$\displaystyle\sum_{k=0}^\infty\left(\frac{1}{k+\tfrac12-x}-\frac{1}{k+\tfrac12+x}\right)"
        r"=2\sum_{k=1}^\infty\frac{\sin(2\pi k x)}{\pi k}$.",
    ),
    rec(
        "RN-P1-C07-Entry20",
        r"If $r$ is any complex number, then "
        r"$\displaystyle\frac{(6\pi)^r}{2\sqrt3\,\Gamma(r)}\left\{\varphi_{r-1}\!\left(-\tfrac13\right)"
        r"-\varphi_{r-1}\!\left(-\tfrac23\right)\right\}"
        r"=\sin\!\left(\frac{\pi r}{2}\right)\left\{\varphi_{-r}\!\left(-\tfrac13\right)-\varphi_{-r}\!\left(-\tfrac23\right)\right\}$.",
    ),
    rec(
        "RN-P1-C07-Entry21-Corollary",
        r"Let $u$ and $n$ be fixed, where $0\le u\le n$ and $n$ is an integer. Let $\varphi(z)$ be "
        r"analytic in a disc centered at $u$ and containing the segment $[0,n]$. If $\varphi_\infty(u)$ is "
        r"defined by (21.2), then "
        r"$\displaystyle\varphi_\infty(u)=\sum_{j=0}^\infty\frac{\varphi^{(j)}(u)}{j!}"
        r"\sum_{k=0}^n\binom{n}{k}(k-u)^j p^k(1-p)^{n-k}$ (21.3), "
        r"where $p=u/n$ and $\varphi_\infty(u)=\sum_{k=0}^n\binom{n}{k}\varphi(k)p^k(1-p)^{n-k}$ (21.2).",
    ),
    rec(
        "RN-P1-C07-Entry22",
        r"Let $A_1=0$. For each nonnegative integer $r$, $r\ne 1$, set $A_r=\{1+(-1)^r\}\zeta(r)$. "
        r"If $n$ is a natural number, then "
        r"$\displaystyle\sum_{k=1}^\infty\frac{k^n}{(k-\tfrac12)^n}=\sum_{k=0}^{n-1}A_{n-k}\!\left(-\tfrac12\right)$.",
    ),
    rec(
        "RN-P1-C07-Entry22-Example",
        r"If $n=3$ in Entry 22 (equivalently Entry 35 of Chapter 9), then "
        r"$\displaystyle\sum_{k=1}^\infty\frac{k^3}{(k-\tfrac12)^3}=K_3=10-\pi^2$.",
    ),
    rec(
        "RN-P1-C07-Entry23",
        r"Let $|\arg z|<\pi$. Then as $|z|\to\infty$, "
        r"$\displaystyle\log\Gamma(z+1)\sim\left(z+\tfrac12\right)\log z-z+\tfrac12\log(2\pi)"
        r"+\sum_{k=1}^\infty\frac{B_{2k}}{2k(2k-1)z^{2k-1}}$.",
    ),
    rec(
        "RN-P1-C07-Entry23-Corollary",
        r"When $x$ is large, $e^x\Gamma(x+1)/x^x\approx\sqrt{2\pi x+\pi/3}$ "
        r"(Ramanujan's notebook approximation; Berndt notes the $x^{-2}$ correction terms "
        r"have opposite sign to Stirling's expansion).",
    ),
    rec(
        "RN-P1-C07-Entry25",
        r"For every complex number $z$ and positive integer $n$, "
        r"$\displaystyle\prod_{k=1}^n\Gamma\!\left(z+\frac{k}{n}\right)"
        r"=(2\pi)^{(n-1)/2}n^{-nz-1/2}\Gamma(nz+1)$.",
    ),
    rec(
        "RN-P1-C07-Entry25-Corollary01",
        r"For every positive integer $n$, "
        r"$\displaystyle\prod_{k=1}^n\Gamma\!\left(\frac{k}{n}\right)=(2\pi)^{(n-1)/2}n^{-1/2}(n-1)!$.",
    ),
    rec(
        "RN-P1-C07-Entry25-Corollary02",
        r"$\displaystyle\Gamma\!\left(\tfrac13\right)=\Gamma\!\left(\tfrac23\right)^{1/2}2^{1/3}$.",
    ),
    rec(
        "RN-P1-C07-Entry25-Corollary03",
        r"For every complex number $z$, "
        r"$\displaystyle\Gamma(z+1)=\Gamma\!\left(\frac{z}{2}\right)\Gamma\!\left(\frac{z+1}{2}\right)2^{1-z}\sqrt\pi$ "
        r"(Legendre's duplication formula).",
    ),
    rec(
        "RN-P1-C07-Entry25-Corollary04",
        r"Let $|\arg z|<\pi$. Then as $|z|\to\infty$, "
        r"$\displaystyle\log\Gamma\!\left(z+\tfrac12\right)\sim z\log z-z+\tfrac12\log(2\pi)"
        r"+\sum_{k=1}^\infty\frac{B_{2k}(2^{1-2k}-1)}{2k(2k-1)z^{2k-1}}$.",
    ),
    rec(
        "RN-P1-C07-Entry26",
        r"For $|z|<1$, "
        r"$\displaystyle\log\Gamma(z+1)=-\gamma z+\sum_{k=2}^\infty(-1)^k\zeta(k)\frac{z^k}{k}$, "
        r"where $\gamma$ denotes Euler's constant.",
    ),
    rec(
        "RN-P1-C07-Entry26-Corollary",
        r"For $|z|<1$, "
        r"$\displaystyle\log\{\Gamma(z+3)\}=0.9227843351z+0.1974670334z^2-0.0256856344z^3"
        r"+0.0049558084z^4-0.0011355510z^5+0.0002863437z^6-0.0000766825z^7"
        r"+0.0000213883z^8-0.0000061409z^9+0.0000018013z^{10}+\cdots$ (26.1).",
    ),
    rec(
        "RN-P1-C07-Entry26-Example01",
        r"$\displaystyle\log\Gamma\!\left(\tfrac43\right)=0.3031502752$.",
    ),
    rec(
        "RN-P1-C07-Entry26-Example02",
        r"$\displaystyle\log\Gamma\!\left(\tfrac53\right)=0.1211436313$.",
    ),
    rec(
        "RN-P1-C07-Entry26-Example03",
        r"$\displaystyle\log\Gamma\!\left(\tfrac{10}{3}\right)=0.0663762397$.",
    ),
    rec(
        "RN-P1-C07-Entry27i",
        r"Suppose that $n$ is a natural number and that $|z|>n$. Then "
        r"$\displaystyle\frac{(n!)^2}{2\pi z}\prod_{k=1}^n\left\{1+\left(\frac{z}{n+k}\right)^2\right\}"
        r"=\frac{2}{\pi}\sinh(\pi z)\exp\left\{\sum_{k=1}^\infty\frac{(-1)^k\varphi_{2k}(n)}{k z^{2k}}\right\}$ (27.1).",
    ),
    rec(
        "RN-P1-C07-Entry27ii",
        r"Under the same hypotheses as Entry 27(i), "
        r"$\displaystyle\frac{(n!)^2}{2\pi z}\prod_{k=1}^n\left\{1+\left(\frac{z}{n+k}\right)^2\right\}"
        r"=2(n!)^2\sinh(nz)\exp\left\{2n-2z\tan^{-1}\!\left(\frac{n}{z}\right)"
        r"+\sum_{j=1}^\infty\frac{(-1)^j B_{2j}S_{2j}}{jz^{2j}}\right\}$ (27.6), "
        r"where "
        r"$\displaystyle S_{2j}=\sum_{k=0}^\infty\frac{(-1)^k(2k+2j-1)!(n)^{2k+1}}{(2j-1)!(2k+1)!\,n^{2k+1}}$, $j\ge 1$.",
    ),
    rec(
        "RN-P1-C07-Entry27iii",
        r"Let $n$ be a positive integer and suppose that $x>0$. Write $r^2=n^2+x^2$ with $r>0$ "
        r"and put $\rho=\tan^{-1}(x/n)$. Then as $x\to\infty$, "
        r"$\displaystyle\log\left\{2n(x^2+n^2)^{n-1/2}\prod_{k=0}^n\left(1+\frac{x^2}{(n+k)^2}\right)\right\}"
        r"\sim 2\log\Gamma(n)+2n+2x\rho"
        r"-\sum_{k=1}^\infty\frac{B_{2k}\cos\{(2k-1)\rho\}}{k(2k-1)r^{2k}}$.",
    ),
]
