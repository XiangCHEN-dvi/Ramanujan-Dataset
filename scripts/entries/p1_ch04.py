"""Part I, Chapter 4 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C04 = ["exponential-iterates-and-formal-technique"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C04}


CHAPTER_4 = [
    rec(
        "RN-P1-C04-Entry02",
        r"Let $F_0(x)=x$ and $F_{r+1}(x)=e^{F_r(x)}-1$ for each integer $r$ (1.1). "
        r"For each integer $r$, differentiating $F_{-1}(x)=\log(1+F_r(x))$ yields "
        r"$\varphi'_{r+1}(x)=[1+F_{r+1}(x)]\varphi'_{-r-1}(x)$, "
        r"where $F_r(x)=\sum_{k=1}^\infty\varphi_k(r)x^k=\sum_{k=0}^\infty f_k(x)r^k$ as formal power series (2.1).",
    ),
    rec(
        "RN-P1-C04-Entry02-Corollary01",
        r"If $r$ is a positive integer, then "
        r"$F'_r(x)=\prod_{k=1}^r\{1+F_k(x)\}$.",
    ),
    rec(
        "RN-P1-C04-Entry02-Corollary02",
        r"Let $r$ be any integer and let $n$ be a positive integer. Then "
        r"$n\{\varphi_n(r)-\varphi_n(r-1)\}=\sum_{k=1}^{n-1}(n-k)\varphi_k(r)\varphi_{n-k}(r-1)$ (2.2).",
    ),
    rec(
        "RN-P1-C04-Entry03",
        r"For each real number $x$, "
        r"$f'_0(x)=x+\sum_{n=1}^\infty B_n f_n(x)$, "
        r"where $B_n$ are Bernoulli numbers and $f_n$ are defined by (1.2).",
    ),
    rec(
        "RN-P1-C04-Entry03-Corollary",
        r"If $x$ is real, then "
        r"$\displaystyle f'_0(x)=\int_0^x\frac{t-f'_0(t)}{f_1(t)}\,dt$.",
    ),
    rec(
        "RN-P1-C04-Entry04",
        r"For each positive integer $n$, "
        r"$f'_{n+1}(x)=f_1(x)f'_n(x)$, "
        r"where $f_n$ is defined by (1.2) and (4.3).",
    ),
    rec(
        "RN-P1-C04-Entry04-Corollary01",
        r"If $n$ and $r$ are positive integers, then "
        r"(i) $\displaystyle n\psi_n(n)=\sum_{k=1}^n(n+k-1)\psi_k(n-1)\psi_{n-k+1}(1)$, and "
        r"(ii) $\displaystyle\varphi_n(2r)=\sum_{k=1}^n(-1)^{k-1}r^{n-k}\psi_k(n-k)$, "
        r"where $\displaystyle f_n(x)=\frac{x}{n!}\sum_{k=1}^\infty(-1)^{k-1}\psi_k(n)x^k$ (4.3).",
    ),
    rec(
        "RN-P1-C04-Entry04-Corollary02",
        r"We have $\psi_1(1)=1$, and for $n\ge 2$, "
        r"$\displaystyle(n+1)\psi_n(1)=n\psi_{n-1}(1)+\sum_{k=1}^N B_{2k}2^{1-2k}\psi_{n-2k}(2k)$, "
        r"where $N$ denotes $(n-1)/2$ or $(n-2)/2$ according as $n$ is odd or even.",
    ),
    rec(
        "RN-P1-C04-Entry05",
        r"For each number $x>-1$, "
        r"$f_1(x)=(1+x)f_1\{\log(1+x)\}$.",
    ),
    rec(
        "RN-P1-C04-Entry06i",
        r"For $n\ge 1$, "
        r"$\varphi_n(1)=1/n!$ (6.1) and $\varphi_n(-1)=(-1)^{n-1}/n$ (6.2).",
    ),
    rec(
        "RN-P1-C04-Entry06ii",
        r"For $n\ge 1$, "
        r"$\displaystyle\psi_2(n)=-\frac{n+1}{6}-\sum_{k=2}^{n+1}\frac{1}{k}$. "
        r"Furthermore, $\psi_1(2r)=1$ (6.3), "
        r"$\displaystyle\psi_4(2r)=r-\frac{3^2}{12}r+\frac{5^2}{24}r$ (6.4), "
        r"$\displaystyle\psi_5(2r)=r-\frac{4^3}{12}r+\frac{6^3}{36}r-\frac{5^3}{72}r$, and "
        r"$\displaystyle\psi_3(n)=(n+1)(n+2)\left[\frac{1}{432}+\frac{1}{72}\left\{\left(\sum_{m=2}^n\frac{1}{m}\right)^2"
        r"-\sum_{m=2}^n\frac{1}{m^2}\right\}+\frac{1}{72}\left(\frac{1}{n+2}-\frac{1}{3}\right)\right]$ (6.5).",
    ),
    rec(
        "RN-P1-C04-Entry07",
        r"Let $y=x/(1-rx)$ and $z=1-rx$. Then "
        r"$F_{2r}(x)=y+\frac{x^2}{6}\log z+\frac{x^3}{72}\{\log^2 z+(1-\log z)^2-z\}+\cdots$ (7.1).",
    ),
    rec(
        "RN-P1-C04-Entry07-Example01",
        r"For each real number $x$, "
        r"$\displaystyle f_1(x)f'_0(x)=f_1(x)-f_2(x)+\sum_{k=1}^\infty(2k+1)B_{2k}f_{2k+1}(x)$.",
    ),
    rec(
        "RN-P1-C04-Entry08",
        r"Let $H_n=\sum_{k=1}^n 1/k$. If $x$ is a positive integer, then "
        r"(i) $\displaystyle\sum_{k=1}^x H_k=(x+1)H_x-x$; "
        r"(ii) $\displaystyle\sum_{k=1}^x H_k^2=(x+1)H_x^2-(2x+1)H_x+2x$; and "
        r"(iii) $\displaystyle\sum_{k=1}^x H_k^3=(x+1)H_x^3-\tfrac12(2x+1)H_x^2+\tfrac13(2x+1)H_x-6x+\tfrac12\pi^2$.",
    ),
    rec(
        "RN-P1-C04-Entry08-Example01",
        r"Let $\varphi(z)$ be entire. Suppose there exists a sequence $r_n$, $1\le n<\infty$, of positive "
        r"numbers tending to $\infty$ such that "
        r"$\displaystyle I_n=\frac{1}{2\pi i}\int_{|z|=r_n}\frac{\varphi(z)\,dz}{z\cos(nz/2)}=o(1)$ as $r_n\to\infty$. Then "
        r"$\displaystyle\lim_{N\to\infty}\sum_{k=-N}^N\frac{(-1)^k\varphi(2k+1)}{2k+1}=\tfrac12\varphi(0)$.",
    ),
    rec(
        "RN-P1-C04-Entry08-Example02",
        r"Let $\varphi(z)$ be entire. Suppose there is a sequence of positive numbers $r_n$, $1\le n<\infty$, "
        r"tending to $\infty$ such that "
        r"$\displaystyle I_n=\frac{1}{2\pi i}\int_{|z|=r_n}\frac{\varphi(z)\,dz}{\sin(nz)}=o(1)$ as $n\to\infty$. Then "
        r"$\displaystyle\lim_{N\to\infty}\sum_{\substack{k=-N\\ k\neq 0}}^N(-1)^{k-1}\varphi(k)=\varphi(0)$.",
    ),
    rec(
        "RN-P1-C04-Entry08-Example03",
        r"Let $\varphi(z)$ be entire. Suppose there exists a sequence of positive numbers $r_n$, $1\le n<\infty$, "
        r"tending to $\infty$ such that "
        r"$\displaystyle I_n=\frac{1}{2\pi i}\int_{|z|=r_n}\frac{\varphi(z)\,dz}{z\sin(nz)}=o(1)$ as $n\to\infty$. Then "
        r"$\displaystyle\lim_{N\to\infty}\sum_{\substack{k=-N\\ k\neq 0}}^N\frac{(-1)^{k-1}\varphi(k)}{k}=\varphi'(0)$.",
    ),
    rec(
        "RN-P1-C04-Entry08-Example04",
        r"Let $\varphi(z)=\psi(z)/\Gamma(z+1)$ satisfy the hypotheses of Example 3, where $\psi$ is entire. Then "
        r"$\displaystyle\sum_{k=1}^\infty\frac{(-1)^k}{k\cdot k!}\psi(k)\approx\gamma\psi(0)+\psi'(0)$ (9.1), "
        r"where $\gamma$ denotes Euler's constant.",
    ),
    rec(
        "RN-P1-C04-Entry08-Corollary01",
        r"As $x\to\infty$, "
        r"$\displaystyle\sum_{k=1}^\infty\frac{(-1)^{k-1}x^k}{k!\,k}\sim\log x+\gamma$, "
        r"where $\gamma$ denotes Euler's constant.",
    ),
    rec(
        "RN-P1-C04-Entry08-Corollary02",
        r"Let $n$ be positive. Then as $x\to\infty$, "
        r"$\displaystyle\sum_{k=1}^\infty\frac{(-1)^{k-1}x^{nk}}{k(k!)^n}\sim n\log x+n\gamma$. "
        r"(Berndt notes Ramanujan's claim is false for $n>2$.)",
    ),
    rec(
        "RN-P1-C04-Entry10",
        r"Let $n$ be complex and let $\varphi$ be entire. Suppose there exists a sequence $r_j$, $1\le j<\infty$, "
        r"of positive numbers tending to $\infty$ such that "
        r"$\displaystyle I_j=\frac{1}{2\pi i}\int_{|z|=r_j}\frac{n\varphi(z)\cot(nz)\cot\{n(z-n)\}\,dz}"
        r"{\Gamma(z+1)\Gamma(n-z+1)}=o(1)$ as $r_j\to\infty$. Then "
        r"$\displaystyle\sum_{k=0}^\infty\binom{n}{k}\varphi(k)=\sum_{k=0}^\infty\binom{n}{k}\varphi(n-k)$, "
        r"provided each series converges.",
    ),
    rec(
        "RN-P1-C04-Entry10-Corollary",
        r"Let the hypotheses of Entry 10 be satisfied with $n$ replaced by $r$ and $\varphi(z)$ replaced by "
        r"$x^{-z}\varphi(z)$, where $x>0$. If "
        r"$\displaystyle f(x)=\sum_{k=0}^\infty\binom{r}{k}x^{r-k}\varphi(k)$ (10.1) "
        r"represents a function in a neighborhood of $\infty$, then $f(0)=\varphi(r)$.",
    ),
    rec(
        "RN-P1-C04-Entry10-Example01",
        r"Let the hypotheses of the Corollary above be satisfied with $r=-1$ and $\varphi(z)$ replaced by "
        r"$\varphi(z+1)$. Then $f(0)=\varphi(0)$.",
    ),
    rec(
        "RN-P1-C04-Entry10-Example02",
        r"For $x>0$, let "
        r"$\displaystyle f(x)=e^x\int_x^\infty\frac{1-e^{-t}}{t}\,dt$. "
        r"Then as $x\to\infty$, "
        r"$\displaystyle f(x)\sim e^x\sum_{k=1}^\infty\frac{(-1)^{k-1}\psi(k)x^k}{k!\,k}$, "
        r"where $\displaystyle\psi(k)=\sum_{n\le k}\frac{1}{n}$ and $\gamma$ denotes Euler's constant. "
        r"Also, $f(0^+)=\infty$.",
    ),
    rec(
        "RN-P1-C04-Entry10-Example03",
        r"For $\operatorname{Re} n>-1$ and $x\ge 0$, let "
        r"$\displaystyle f(x)=\int_0^\infty e^{-t}(x+t)^n\,dt$. "
        r"Then as $x\to\infty$, "
        r"$\displaystyle f(x)\sim\sum_{k=0}^\infty\frac{\Gamma(n+1)\,x^{n-k}}{\Gamma(n-k+1)\,k!}$, "
        r"and $f(0)=\Gamma(n+1)$.",
    ),
    rec(
        "RN-P1-C04-Entry10-Example04",
        r"For $x\ge 0$, let $\displaystyle f(x)=\int_x^\infty\frac{\sin(t-x)}{t}\,dt$. Then "
        r"$\displaystyle\frac{\pi}{2}\cos x+(\gamma+\log x)\sin x-\sum_{k=0}^\infty\frac{(-1)^k\psi(2k+1)x^{2k+1}}{(2k+1)!}"
        r"=f(x)\sim\sum_{k=0}^\infty\frac{(-1)^k(2k)!}{(2k+1)x^{2k+1}}$ as $x\to\infty$, "
        r"where $\psi$ is defined in the third version of Example 2. Furthermore, $f(0)=\pi/2$.",
    ),
    rec(
        "RN-P1-C04-Entry11",
        r"If $n>0$, then "
        r"$\displaystyle\int_0^\infty x^{n-1}\sum_{k=0}^{n-1}\frac{\varphi(k)(-x)^k}{k!}\,dx"
        r"=\frac{\Gamma(n)\varphi(-n)}{n!}$.",
    ),
    rec(
        "RN-P1-C04-Entry11-Corollary01",
        r"If $n>0$, then "
        r"$\displaystyle\int_0^\infty x^{n-1}\sum_{k=0}^\infty\frac{\varphi(k)(-x)^k}{k!}\,dx"
        r"=\frac{n\varphi(-n)}{\sin(\pi n)}$.",
    ),
    rec(
        "RN-P1-C04-Entry11-Corollary02",
        r"If $n>0$, then "
        r"$\displaystyle\int_0^\infty x^{n-1}\sum_{k=0}^\infty\frac{\varphi(2k)(x^2)^k}{(2k)!}\,dx"
        r"=\Gamma(n)\varphi(-n)\cos\frac{\pi n}{2}$.",
    ),
    rec(
        "RN-P1-C04-Entry11-Corollary03",
        r"If $n$ is real, then "
        r"$\displaystyle\int_0^\infty\sum_{k=0}^\infty\frac{\varphi(k)(-x)^k}{k!}\cos(nx)\,dx"
        r"=\sum_{k=0}^\infty\frac{\varphi(-2k-1)(-n^2)^k}{k!}$.",
    ),
    rec(
        "RN-P1-C04-Entry11-Corollary04",
        r"If $n$ is real, then "
        r"$\displaystyle\int_0^\infty\sum_{k=0}^\infty\frac{\varphi(2k)(-x^2)^k}{(2k)!}\cos(nx)\,dx"
        r"=\frac{\pi}{2}\sum_{k=0}^\infty\frac{\varphi(-k-1)(-n)^k}{k!}$.",
    ),
    rec(
        "RN-P1-C04-Entry11-Corollary05",
        r"If $m,n>-1$, then "
        r"$\displaystyle\int_0^1 x^m(1-x)^n\,dx=\frac{\Gamma(m+1)\Gamma(n+1)}{\Gamma(m+n+2)}$.",
    ),
    rec(
        "RN-P1-C04-Entry12",
        r"If $\displaystyle\psi(n)=\int_0^\infty\varphi(x)\cos(nx)\,dx$, then "
        r"(i) $\displaystyle\int_0^\infty\psi(x)\cos(nx)\,dx=\frac{\pi}{2}\varphi(n)$, and "
        r"(ii) $\displaystyle\varphi(x)=\frac{2}{\pi}\int_0^\infty\psi(n)\cos(nx)\,dn$.",
    ),
    rec(
        "RN-P1-C04-Entry13i",
        r"If $m,n>-1$, then "
        r"$\displaystyle\int_0^{\pi/2}\sin^m x\cos^n x\,dx"
        r"=\frac{\Gamma\bigl(\frac{m+1}{2}\bigr)\Gamma\bigl(\frac{n+1}{2}\bigr)}"
        r"{2\Gamma\bigl(\frac{m+n+2}{2}\bigr)}$.",
    ),
    rec(
        "RN-P1-C04-Entry13ii",
        r"If $m>-1$ and $n$ is any complex number, then "
        r"$\displaystyle\int_0^{\pi/2}\cos^m x\cos(nx)\,dx"
        r"=\frac{\pi\,\Gamma(m+1)}{2^{m+1}\Gamma\bigl(\frac{m+n+2}{2}\bigr)\Gamma\bigl(\frac{m-n+2}{2}\bigr)}$.",
    ),
    rec(
        "RN-P1-C04-Entry14",
        r"If $x$ is any complex number, then "
        r"$\displaystyle\prod_{n=1}^\infty\left(1+\frac{x^6}{n^6\pi^6}\right)"
        r"=\frac{\sinh(2\pi x)-2\sinh(\pi x)\cos(\pi x\sqrt{3})}{4\pi^4 x^4}$.",
    ),
    rec(
        "RN-P1-C04-Entry15",
        r"For each positive integer $k$, let $\displaystyle G_k=\sum_{0\le 2n+1\le k}\frac{1}{2n+1}$. "
        r"Then for all complex $x$, "
        r"$\displaystyle\sum_{k=1}^\infty\frac{(-1)^{k+1}x^k}{k!\,k}=\sum_{k=1}^\infty\frac{G_k x^k}{k!}$ (15.1).",
    ),
]
