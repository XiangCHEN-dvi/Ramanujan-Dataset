"""Part I, Chapter 9 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C09 = ["infinite-series-identities"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C09}


CHAPTER_9 = [
    rec(
        "RN-P1-C09-Entry01i",
        r"For each positive integer $r$, define $S_r=\sum_{k=0}^{\infty}\bigl\{(2k+1-a)^{-r}-(2k+1+a)^{-r}\bigr\}$, where $a$ is real but not an odd integer. Assume that $|x|<\pi$. "
        r"If $r$ is an odd positive integer, then $c_r(x)=\sum_{k=0}^{\infty}\frac{\cos(2k+1-a)x-\cos(2k+1+a)x}{(2k+1-a)^r}=\sum_{k=0}^{(r-1)/2}\frac{(-1)^k S_{r-2k}\,x^{2k}}{(2k)!}$.",
    ),
    rec(
        "RN-P1-C09-Entry01ii",
        r"With $S_r$ as in Entry 1(i), if $r$ is an even positive integer, then $s_r(x)=\sum_{k=0}^{\infty}\frac{\sin(2k+1-a)x-\sin(2k+1+a)x}{(2k+1-a)^r}=\sum_{k=0}^{r/2-1}\frac{(-1)^k S_{r-2k-1}\,x^{2k+1}}{(2k+1)!}$.",
    ),
    rec(
        "RN-P1-C09-Entry02i",
        r"For each integer $r\ge 2$, define $S_r=\sum_{k=0}^{\infty}\bigl\{(2k+1-a)^{-r}+(2k+1+a)^{-r}\bigr\}$, where $a$ is real but not an odd integer. Assume that $0<x<\pi$. "
        r"If $r$ is an even positive integer, then $c_r(x)=\sum_{k=0}^{\infty}\frac{\cos(2k+1-a)x+\cos(2k+1+a)x}{(2k+1-a)^r}=\sum_{k=0}^{r/2-1}\frac{(-1)^k S_{r-2k}\,x^{2k}}{(2k)!}+\frac{(-1)^{r/2}\pi x^{r-1}}{2(r-1)!}$.",
    ),
    rec(
        "RN-P1-C09-Entry02ii",
        r"With $S_r$ as in Entry 2(i), if $r$ is an odd positive integer, then $s_r(x)=\sum_{k=0}^{\infty}\frac{\sin(2k+1-a)x+\sin(2k+1+a)x}{(2k+1-a)^r}=\sum_{k=0}^{(r-3)/2}\frac{(-1)^k S_{r-1-2k}\,x^{2k+1}}{(2k+1)!}+\frac{(-1)^{(r-1)/2}\pi x^{r-1}}{2(r-1)!}$.",
    ),
    rec(
        "RN-P1-C09-Entry03",
        r"Let $H_n=\sum_{k=1}^{n}1/k$, and for a natural number $n$ and real $x$ define $\delta_n(x)=\sum_{k=0}^{\infty}\frac{(-1)^k\sin(2k+1)x}{(2k+1)^n}$, $C_n(x)=\sum_{k=0}^{\infty}\frac{(-1)^k\cos(2k+1)x}{(2k+1)^n}$, and $\varphi_n(x)=\sum_{k=0}^{\infty}\frac{(-1)^k H_{k+1}\cos(2k+1)x}{(2k+1)^n}$. "
        r"If $n$ is an odd integer at least equal to $3$, then $\varphi_{n-2}(x)-\varphi_n(x)=x\delta_{n-2}(x)-x\delta_n(x)+nC_{n-1}(x)-nC_{n+1}(x)$ (3.2). "
        r"(Berndt notes this claim is false for $n$ sufficiently large.)",
    ),
    rec(
        "RN-P1-C09-Entry04i",
        r"For each nonnegative integer $n$, define "
        r"$F_n(x)=\sum_{k=0}^{\infty}\binom{2k}{k}\frac{(-1)^k\sin(2k+1)x}{2^{2k}(2k+1)^n}"
        r"-(-1)^n\sum_{k=0}^{\infty}\binom{2k}{k}\frac{(-1)^k\sin(2k+2)x}{2^{2k}(2k+2)^n}$, "
        r"$\psi_n(x)=\sum_{k=0}^{\infty}\binom{2k}{k}\frac{(-1)^k\cos(2k+1)x}{2^{2k}(2k+1)^n}"
        r"+(-1)^n\sum_{k=0}^{\infty}\binom{2k}{k}\frac{(-1)^k\cos(2k+2)x}{2^{2k}(2k+2)^n}"
        r"-(-1)^n\sum_{k=0}^{\infty}\binom{2k}{k}\frac{(-1)^k\cos(2k+2)x}{2^{2k}(2k+2)^{n+1}}$, and "
        r"$\varphi(n)=\sum_{k=0}^{\infty}\binom{2k}{k}\frac{1}{2^{2k}(2k+1)^{n+1}}$, where $\zeta$ denotes the Riemann zeta-function. "
        r"Let $|x|<\pi/2$ and let $n$ be an integer. If $n\ge 0$, then "
        r"$\displaystyle\sum_{k=0}^{\lfloor n/2\rfloor}\frac{(-1)^k x^{n-2k}}{(n-2k)!}\sum_{j=0}^{k}2^{-2j}S_{2j}\,\varphi(2k-2j)"
        r"=\begin{cases}\sin(n\pi/2)\,F_n(x),&n\text{ odd},\\"
        r"\cos(n\pi/2)\,\psi_n(x),&n\text{ even},\end{cases}$ (4.1).",
    ),
    rec(
        "RN-P1-C09-Entry04ii",
        r"With the notation of Entry 4(i), if $n\ge -1$, then $\displaystyle\sum_{k=0}^{\lfloor n/2\rfloor}\frac{(-1)^k x^{n-2k}}{(n-2k)!}\sum_{j=0}^{k}2^{-2j}S_{2j}\,\varphi(2k+1-2j)=\begin{cases}\sin(n\pi/2)\,F_{n+1}(x),&n\text{ odd},\cos(n\pi/2)\,\psi_{n+1}(x),&n\text{ even},\end{cases}$ (4.2).",
    ),
    rec(
        "RN-P1-C09-Entry05i",
        r"Let $a$, $n$, and $\theta$ be real with $n\ge 0$ and $|\theta|\le\pi/2$. Then $\displaystyle\sum_{k=0}^{n}\binom{n}{k}\sin(a+2k\theta)=2^n\cos^n\theta\sin(a+n\theta)$.",
    ),
    rec(
        "RN-P1-C09-Entry05ii",
        r"Let $a$, $n$, and $\theta$ be real with $n\ge 0$ and $|\theta|\le\pi/2$. Then $\displaystyle\sum_{k=0}^{n}\binom{n}{k}\cos(a+2k\theta)=2^n\cos^n\theta\cos(a+n\theta)$.",
    ),
    rec(
        "RN-P1-C09-Entry06i",
        r"For $|z|\le 1$, with $\operatorname{Li}_2$ and $\chi_2$ as in Berndt (6.1)--(6.2), $\operatorname{Li}_2(1-z)+\operatorname{Li}_2\!\bigl(1-\tfrac{1}{z}\bigr)=-\tfrac{1}{2}\log^2 z$.",
    ),
    rec(
        "RN-P1-C09-Entry06ii",
        r"For $|z|\le 1$, $\operatorname{Li}_2(-z)+\operatorname{Li}_2\!\bigl(\tfrac{-1}{z}\bigr)=-\tfrac{\pi^2}{6}-\tfrac{1}{2}\log^2 z$.",
    ),
    rec(
        "RN-P1-C09-Entry06iii",
        r"For $|z|\le 1$, $\operatorname{Li}_2(z)+\operatorname{Li}_2(1-z)=\tfrac{\pi^2}{6}-\log z\,\log(1-z)$.",
    ),
    rec(
        "RN-P1-C09-Entry06iv",
        r"For $|z|\le 1$, $\operatorname{Li}_2(z)+\operatorname{Li}_2(-z)=\tfrac{1}{2}\operatorname{Li}_2(z^2)$.",
    ),
    rec(
        "RN-P1-C09-Entry06v",
        r"For $|z|\le 1$, $\chi_2(z)+\chi_2\!\bigl(\tfrac{1+z}{1-z}\bigr)=\tfrac{\pi^2}{8}+\tfrac{\pi^2}{2}\log z\,\log\!\bigl(\tfrac{1-z}{1+z}\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry06vi",
        r"For $|z|\le 1$, $\operatorname{Li}_2\!\bigl(\tfrac{z}{1-w}\bigr)+\operatorname{Li}_2\!\bigl(\tfrac{w}{1-z}\bigr)=\operatorname{Li}_2(z)+\operatorname{Li}_2(w)+\operatorname{Li}_2\!\bigl(\tfrac{1-zw}{(1-z)(1-w)}\bigr)+\log(1-z)\log(1-w)$.",
    ),
    rec(
        "RN-P1-C09-Entry06vii",
        r"For $|z|<2\pi$, $\operatorname{Li}_2(e^{i\theta})=\tfrac{\pi^2}{12}+\tfrac{i\theta}{2}\bigl(\theta-2\pi\bigr)+\sum_{n=1}^{\infty}\frac{B_n}{(n+1)!n}\,(i\theta)^{n+1}$.",
    ),
    rec(
        "RN-P1-C09-Entry06viii",
        r"For $|z|<2\pi$, $\operatorname{Li}_2(1-e^{-z})=\tfrac{\pi^2}{12}-\log|2\sin(\tfrac{z}{2})|$.",
    ),
    rec(
        "RN-P1-C09-Entry06-Example01",
        r"$\displaystyle\operatorname{Li}_2\!\bigl(\tfrac{1}{2}\bigr)=\tfrac{\pi^2}{12}-\tfrac{1}{2}\log^2 2$.",
    ),
    rec(
        "RN-P1-C09-Entry06-Example02",
        r"$\displaystyle\operatorname{Li}_2\!\bigl(\tfrac{\sqrt5-1}{2}\bigr)=-\tfrac{\pi^2}{10}-\log^2\!\bigl(\tfrac{\sqrt5-1}{2}\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry06-Example03",
        r"$\displaystyle\operatorname{Li}_2\!\bigl(\tfrac{3-\sqrt5}{2}\bigr)=\tfrac{\pi^2}{15}-\log^2\!\bigl(\tfrac{\sqrt5-1}{2}\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry06-Example04",
        r"$\displaystyle\chi_2(\sqrt2-1)=\tfrac{\pi^2}{12}-\tfrac{1}{2}\log^2\!\bigl(\tfrac{\sqrt5-1}{2}\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry06-Example05",
        r"$\displaystyle\chi_2\!\bigl(\sqrt{\tfrac{5-\sqrt5}{2}}\bigr)=\tfrac{5\pi^2}{24}-\tfrac{1}{2}\log^2\!\bigl(\tfrac{\sqrt5-1}{2}\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry06-Example06",
        r"$\displaystyle\chi_2(\sqrt5-2)=\tfrac{3\pi^2}{8}-\tfrac{3}{4}\log^2\!\bigl(\tfrac{\sqrt5-1}{2}\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry07i",
        r"Let $\operatorname{Li}_3(z)$ be defined by (6.1). Then $\operatorname{Li}_3(1-z)+\operatorname{Li}_3\!\bigl(1-\tfrac{1}{z}\bigr)+\operatorname{Li}_3(z)=\zeta(3)+\tfrac{\pi^2}{6}\log z+\tfrac{1}{2}\log^3 z-\tfrac{1}{2}\log^2 z\,\log(1-z)$.",
    ),
    rec(
        "RN-P1-C09-Entry07ii",
        r"Let $\operatorname{Li}_3(z)$ be defined by (6.1). Then $\operatorname{Li}_3(1-z)-\operatorname{Li}_3\!\bigl(1-\tfrac{1}{z}\bigr)=\tfrac{\pi^2}{6}\log z+\tfrac{1}{2}\log^3 z$.",
    ),
    rec(
        "RN-P1-C09-Entry07iii",
        r"Let $\operatorname{Li}_3(z)$ be defined by (6.1). Then $\operatorname{Li}_3(z)+\operatorname{Li}_3(-z)=\tfrac{1}{4}\operatorname{Li}_3(z^2)$.",
    ),
    rec(
        "RN-P1-C09-Entry07-Example01",
        r"If $\chi_3$ is defined by (6.2), then $\displaystyle\operatorname{Li}_3\!\bigl(\tfrac{1}{2}\bigr)=\tfrac{1}{2}\log^3 2-\tfrac{\pi^2}{12}\log 2+\chi_3(1)$.",
    ),
    rec(
        "RN-P1-C09-Entry07-Example02",
        r"If $\chi_3$ is defined by (6.2), then $\displaystyle\operatorname{Li}_3\!\bigl(\tfrac{3-\sqrt5}{2}\bigr)=\tfrac{1}{2}\log^3\!\bigl(\tfrac{\sqrt5+1}{2}\bigr)-\tfrac{2\pi^2}{3}\log\!\bigl(\tfrac{\sqrt5+1}{2}\bigr)+\tfrac{4}{5}\zeta(3)$.",
    ),
    rec(
        "RN-P1-C09-Entry08",
        r"For $|x|<1$, define $f(x)=\sum_{k=1}^{\infty}\frac{H_k x^{2k}}{2k}$, where $H_k$ is defined by (3.1). Then, for $|x|<1$, $\displaystyle f\!\bigl(\frac{2x}{2-x}\bigr)=\tfrac{1}{2}\log^2(1-x)+\tfrac{1}{2}\operatorname{Li}_2(x)$.",
    ),
    rec(
        "RN-P1-C09-Entry08-Example01",
        r"With $f$ as in Entry 8, $\displaystyle f\!\bigl(\tfrac{1}{3}\bigr)=\tfrac{\pi^2}{24}-\tfrac{1}{8}\log^2 2$.",
    ),
    rec(
        "RN-P1-C09-Entry08-Example02",
        r"With $f$ as in Entry 8, $\displaystyle f(\sqrt5-2)=\tfrac{\pi^2}{30}-\tfrac{\pi^2}{8}\log^2\!\bigl(\tfrac{\sqrt5-1}{2}\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry08-Example03",
        r"With $f$ as in Entry 8, $\displaystyle f\!\bigl(\tfrac{3-\sqrt5}{2}\bigr)=\tfrac{\pi^2}{30}-\tfrac{\pi^2}{24}\log^2\!\bigl(\tfrac{\sqrt5-1}{2}\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry09i",
        r"For $|z|\le 1$, define $g(z)=\sum_{k=1}^{\infty}\frac{H_k z^{k+1}}{(k+1)^2}$, where $H_k$ is defined by (3.1). Then $g$ can be analytically continued to the entire complex plane, and $g(1-z)=\tfrac{1}{2}\log^2 z\,\log(1-z)+\operatorname{Li}_2(z)\log z-\operatorname{Li}_3(z)+\zeta(3)$.",
    ),
    rec(
        "RN-P1-C09-Entry09ii",
        r"For $g$ as in Entry 9(i), $g(1-z)-g\!\bigl(1-\tfrac{1}{z}\bigr)=\tfrac{1}{6}\log^3 z$.",
    ),
    rec(
        "RN-P1-C09-Entry09iii",
        r"For $g$ as in Entry 9(i), $g(1-z)=\tfrac{1}{2}\log^2 z\,\log(z-1)-\tfrac{1}{6}\log^3 z-\operatorname{Li}_2\!\bigl(\tfrac{1}{z}\bigr)\log z-\operatorname{Li}_3\!\bigl(\tfrac{1}{z}\bigr)+\zeta(3)$.",
    ),
    rec(
        "RN-P1-C09-Entry09iv",
        r"For $g$ as in Entry 9(i), $g(-z)+g\!\bigl(\tfrac{-1}{z}\bigr)=-\tfrac{1}{6}\log^3 z-\operatorname{Li}_2(-z)\log z+\operatorname{Li}_3(-z)+\zeta(3)$.",
    ),
    rec(
        "RN-P1-C09-Entry10i",
        r"For $|z|\le 1$, define $h(z)=\sum_{k=1}^{\infty}\frac{H_k z^{k+1}}{(k+1)^3}$. Then $h(z)$ can be analytically continued into the entire complex $z$-plane, and $h(1-z)-h\!\bigl(1-\tfrac{1}{z}\bigr)=-\tfrac{1}{4}\log^4 z+\tfrac{1}{6}\log^3 z\,\log(1-z)+\zeta(3)\log z-2\operatorname{Li}_4(z)+\operatorname{Li}_3(z)\log z+\tfrac{\pi^4}{45}$.",
    ),
    rec(
        "RN-P1-C09-Entry10ii",
        r"For $h$ as in Entry 10(i), $h(-z)-h\!\bigl(\tfrac{-1}{z}\bigr)=-\tfrac{1}{4}\log^4 z-\operatorname{Li}_3(-z)\log z+2\operatorname{Li}_4(-z)+\zeta(3)\log z+\tfrac{7\pi^4}{360}$.",
    ),
    rec(
        "RN-P1-C09-Entry11i",
        r"For $-1\le x\le 1$, define $F(x)=\sum_{k=1}^{\infty}\frac{h_k x^{2k}}{(2k)^2}$, where $h_k$ is defined by (8.2). Then for $0\le x\le 1$, $\displaystyle F\!\bigl(\frac{1-x}{1+x}\bigr)=\tfrac{1}{2}\log^2 x\,\log\!\bigl(\tfrac{1-x}{1+x}\bigr)+h_2(x)\log x+\tfrac{1}{2}\chi_3(1)-\tfrac{1}{2}\chi_3(x)$.",
    ),
    rec(
        "RN-P1-C09-Entry11ii",
        r"For $F$ as in Entry 11(i) and $G$ defined by $xG'(x)=F(x)$, for $0\le x\le 1$, $\displaystyle G(x)+G\!\bigl(\frac{1-x}{1+x}\bigr)=F(x)\log x+F\!\bigl(\tfrac{1-x}{1+x}\bigr)\log\!\bigl(\tfrac{1-x}{1+x}\bigr)-\tfrac{1}{6}\log^2 x\,\log^2\!\bigl(\tfrac{1-x}{1+x}\bigr)+G(1)$.",
    ),
    rec(
        "RN-P1-C09-Entry12",
        r"For $|x|<1$, define $H(x)=\sum_{k=1}^{\infty}\frac{H_k x^{2k-1}}{2k-1}$, where $H_k$ is defined by (3.1). Then for $0<x<1$, $\displaystyle H\!\bigl(\frac{1-x}{1+x}\bigr)=(\log 2-1)\log x+\tfrac{1}{2}\log\frac{1-x^2}{4}+\tfrac{\pi^2}{12}+\tfrac{1}{2}\log^2 x+\operatorname{Li}_2(-x)$.",
    ),
    rec(
        "RN-P1-C09-Entry13",
        r"If $n$ is a positive integer, then $\displaystyle\int_0^x u^n\cot\!\bigl(\tfrac{u}{2}\bigr)\,du=\cos\!\bigl(\tfrac{n\pi}{2}\bigr)\,n!\,\zeta(n+1)-\tfrac{1}{2}\sum_{j=0}^{n}(-1)^{j}\frac{(j+1)^{-1}\Gamma(n+1)}{\Gamma(n+1-j)}\,x^{n-j}\operatorname{Cl}_{j+1}(x)$, where $\operatorname{Cl}_m$ is defined by (13.1)--(13.2).",
    ),
    rec(
        "RN-P1-C09-Entry14",
        r"If $n$ is a positive integer, then $\displaystyle\int_0^x\frac{u^n}{2\csc u}\,du=\cos\!\bigl(\tfrac{n\pi}{2}\bigr)\,n!\,x^{n+1}\chi_n(1)-\tfrac{1}{2}\sum_{j=0}^{n}(-1)^{j}\frac{(j+1)^{-1}\Gamma(n+1)}{\Gamma(n+1-j)}\,x^{n-j}D_{j+1}(x)$, where $\chi_n$ is defined by (6.2) and $D_m$ by (14.1)--(14.2).",
    ),
    rec(
        "RN-P1-C09-Entry15",
        r"For each nonnegative integer $n$, define $f_n(x)=\int x^n\cot x\,dx$. Then if $n\ge 0$, $\displaystyle 2^n f_n(1-x)=\sum_{k=0}^{n}(-1)^k\binom{n}{k}n^{n-k}\bigl\{f_k(2x)-2^k f_k(x)\bigr\}$.",
    ),
    rec(
        "RN-P1-C09-Entry15-Example01",
        r"$\displaystyle\int x^n\cot x\,dx=\int_0^{\sin x}\frac{(\sin^{-1}y)^n}{y}\,dy$ (15.1).",
    ),
    rec(
        "RN-P1-C09-Entry15-Example02",
        r"$\displaystyle\int\frac{2x^n}{\sin^2 x}\,dx=\int_0^{\tan x}\frac{(\tan^{-1}z)^n}{z}\,dz$ (15.2).",
    ),
    rec(
        "RN-P1-C09-Entry16",
        r"For $|x|\le\pi/2$, $\displaystyle\sum_{k=0}^{\infty}\binom{2k}{k}\frac{\sin^{2k+1}x}{k\,2^{2k}(2k+1)^2}=x\log\!\bigl|2\sin x\bigr|+\tfrac{1}{2}\sum_{k=1}^{\infty}\frac{\sin(2kx)}{k^2}$ (16.1).",
    ),
    rec(
        "RN-P1-C09-Entry16-Example01",
        r"$\displaystyle\sum_{k=0}^{\infty}\binom{2k}{k}\frac{3^k}{2^{4k}(2k+1)^2}=\tfrac{\sqrt3}{3}\log 3-\tfrac{2\pi^2}{27}+\sum_{k=0}^{\infty}\frac{1}{(3k+1)^2}$.",
    ),
    rec(
        "RN-P1-C09-Entry16-Example02",
        r"$\displaystyle\sum_{k=0}^{\infty}\binom{2k}{k}\frac{1}{2^{4k}(2k+1)^2}=\tfrac{\pi^2}{8}-\tfrac{1}{2}\log^2\!\bigl(\tfrac{\sqrt2+1}{2}\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry16-Example03",
        r"$\displaystyle\sum_{k=0}^{\infty}\binom{2k}{k}\frac{3^k}{2^{4k}(2k+1)^2}=-\tfrac{3\sqrt3}{4}\sum_{k=0}^{\infty}\frac{1}{(3k+1)^2}-\tfrac{\sqrt3}{2}\Bigl\{\sum_{k=0}^{\infty}\frac{1}{(2k+1)^2}-\tfrac{1}{9}\sum_{k=0}^{\infty}\frac{1}{(2k+1)^2}\Bigr\}+\tfrac{4\sqrt3\,\pi^2}{9}$.",
    ),
    rec(
        "RN-P1-C09-Entry16-Example04",
        r"$\displaystyle\sum_{k=0}^{\infty}\binom{2k}{k}\frac{1}{2^{4k}(2k+1)^2}=-\tfrac{1}{3\sqrt3}\log 3+\sum_{k=0}^{\infty}\frac{1}{(3k+1)^2}-\tfrac{1}{2}\sum_{k=1}^{\infty}\frac{1}{k^2}+\tfrac{1}{9}\sum_{k=1}^{\infty}\frac{1}{(3k)^2}$.",
    ),
    rec(
        "RN-P1-C09-Entry17",
        r"For $|x|<\pi/2$, $\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k\tan^{2k+1}x}{(2k+1)^2}=x\log|\tan x|+\sum_{k=0}^{\infty}\frac{\sin(4k+2)x}{(2k+1)^2}$ (17.1).",
    ),
    rec(
        "RN-P1-C09-Entry17-Example01",
        r"$\displaystyle\int_0^{\pi/6}\frac{\tan^{-1}t}{t}\,dt=-\tfrac{\pi}{12}\log 3-\tfrac{5\pi^2}{18\sqrt3}+\tfrac{5\sqrt3}{4}\sum_{k=0}^{\infty}\frac{1}{(3k+1)^2}$.",
    ),
    rec(
        "RN-P1-C09-Entry17-Example02",
        r"$\displaystyle\int_0^{\sqrt2-1}\frac{\tan^{-1}t}{t}\,dt=\tfrac{\pi}{8}\log(\sqrt2-1)-\tfrac{\pi^2}{16}+\sqrt2\sum_{k=0}^{\infty}\frac{(-1)^k}{(4k+1)^2}$.",
    ),
    rec(
        "RN-P1-C09-Entry17-Example03",
        r"$\displaystyle\int_0^{2-\sqrt3}\frac{\tan^{-1}t}{t}\,dt=\tfrac{\pi}{12}\log(2-\sqrt3)+\tfrac{2}{3}\int_0^1\frac{\tan^{-1}t}{t}\,dt$, where $\displaystyle\int_0^1\frac{\tan^{-1}t}{t}\,dt=G$ and $G$ denotes Catalan's constant.",
    ),
    rec(
        "RN-P1-C09-Entry18",
        r"For $0\le x\le\pi/4$, $\displaystyle\sum_{k=0}^{\infty}\binom{2k}{k}\frac{\cos^{2k+1}x-\sin^{2k+1}x}{k\,2^{2k}(2k+1)^2}=-\log(2\cos x)-\tfrac{1}{2}\sum_{k=0}^{\infty}\binom{2k}{k}\frac{\sin^{2k+1}(2x)}{k\,2^{2k}(2k+1)^2}$ (18.1).",
    ),
    rec(
        "RN-P1-C09-Entry18-Example",
        r"For $|x|\le 1$, define $\psi(x)=\int_0^x\frac{\sin^{-1}t}{t}\,dt$. Then $\displaystyle\psi\!\bigl(\tfrac{\sqrt5-1}{2}\bigr)+\psi\!\bigl(\tfrac{\sqrt5+1}{2}\bigr)=\tfrac{\pi}{2}\log 2+\tfrac{\pi}{2}\log\!\bigl(\tfrac{\sqrt5+1}{2}\bigr)-\tfrac{1}{2}\psi\!\bigl(\tfrac{1}{2}\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry19",
        r"For $0\le x<\pi/2$, $\displaystyle\sum_{k=0}^{\infty}\binom{2k}{k}\frac{\cos^{2k+1}x+\sin^{2k+1}x}{k\,2^{2k}(2k+1)^2}=-\tfrac{\pi}{2}\log(2\cos x)+\sum_{k=0}^{\infty}\frac{(-1)^k\tan^{2k+1}x}{(2k+1)^2}$.",
    ),
    rec(
        "RN-P1-C09-Entry19-Example",
        r"$\displaystyle\sum_{k=0}^{\infty}\binom{2k}{k}\frac{1}{2^{2k+1}5^k(2k+1)^2}=\tfrac{1}{2\sqrt5}\log\sqrt5+\tfrac{1}{\sqrt5}\sum_{k=0}^{\infty}\frac{(-1)^k}{2^{2k+1}(2k+1)^2}$.",
    ),
    rec(
        "RN-P1-C09-Entry20",
        r"Let $|x|\le\pi/2$. Then $\displaystyle\sum_{k=0}^{\infty}\frac{2^{2k}(k!)^2\sin^{2k+2}x}{(2k+1)!(2k+2)^2}=\tfrac{x^2}{2}\log|2\sin x|+\tfrac{x}{2}\sum_{k=1}^{\infty}\frac{\sin(2kx)}{k^2}+\tfrac{1}{4}\sum_{k=1}^{\infty}\frac{\cos(2kx)}{k^3}-\tfrac{\zeta(3)}{4}$ (20.1).",
    ),
    rec(
        "RN-P1-C09-Entry20-Example01",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{2^{2k}(k!)^2}{(2k+1)!(2k+2)^2}=\tfrac{\pi^2}{8}\log 2-\tfrac{1}{2}\chi_3(1)$.",
    ),
    rec(
        "RN-P1-C09-Entry20-Example02",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{2^{2k-1}(k!)^2}{(2k+1)!(2k+2)^2}=\tfrac{\pi^2}{64}\log 2+\tfrac{\pi}{8}G-\tfrac{5}{16}\chi_3(1)$, where $G$ denotes Catalan's constant and $\chi_3$ is defined by (6.2).",
    ),
    rec(
        "RN-P1-C09-Entry21",
        r"For $|x|\le\pi/4$, $\displaystyle\sum_{k=1}^{\infty}\frac{(-1)^{k-1}h_k}{(2k)^2}\tan^{2k}x=\tfrac{x^2}{2}\log|\tan x|+x\sum_{k=0}^{\infty}\frac{\sin(4k+2)x}{(2k+1)^2}+\tfrac{1}{2}\sum_{k=0}^{\infty}\frac{\cos(4k+2)x}{(2k+1)^3}-\tfrac{1}{2}\chi_3(1)$ (21.1), where $h_k$ is defined by (8.2).",
    ),
    rec(
        "RN-P1-C09-Entry21-Example",
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{(-1)^{k-1}h_k}{(2k)^2}=2G$, where $G$ denotes Catalan's constant.",
    ),
    rec(
        "RN-P1-C09-Entry22",
        r"Let $0\le x\le\pi/2$. Then $\displaystyle\sum_{k=0}^{\infty}\frac{2^{2k}(k!)^2\{\cos^{2k+2}x+\sin^{2k+2}x\}}{(2k+1)!(2k+2)^2}=-\tfrac{\pi^2}{8}\log(2\cos x)+\tfrac{\pi}{2}\sum_{k=0}^{\infty}\binom{2k}{k}\frac{\cos^{2k+1}x}{k\,2^{2k}(2k+1)^2}+\tfrac{\pi}{4}\sum_{k=0}^{\infty}\frac{2^{2k}(k!)^2\sin^{2k+2}(2x)}{(2k+1)!(2k+2)^2}-\tfrac{1}{2}\chi_3(1)$.",
    ),
    rec(
        "RN-P1-C09-Entry23",
        r"For $|x|\le\pi/4$, $\displaystyle\sum_{k=1}^{\infty}\frac{(-1)^{k-1}h_k}{(2k)^2}\tan^{2k}x=2\sum_{k=0}^{\infty}\frac{2^{2k}(k!)^2\sin^{2k+2}x}{(2k+1)!(2k+2)^2}-\tfrac{1}{4}\sum_{k=0}^{\infty}\frac{2^{2k}(k!)^2\sin^{2k+2}(2x)}{(2k+1)!(2k+2)^2}$ (23.1), where $h_k$ is defined by (8.2).",
    ),
    rec(
        "RN-P1-C09-Entry24i",
        r"Let $x$, $y$, $\theta$, and $\varphi$ be real with $xe^{i\theta}+ye^{i\varphi}=1$, $0\le x,y\le 1$, and $-\pi<\theta,\varphi\le\pi$. Then $\displaystyle\sum_{k=1}^{\infty}\frac{x^k\cos(k\theta)}{k^2}+\sum_{k=1}^{\infty}\frac{y^k\cos(k\varphi)}{k^2}=\tfrac{\pi^2}{6}-\log x\,\log y+\theta\varphi$.",
    ),
    rec(
        "RN-P1-C09-Entry24ii",
        r"Under the hypotheses of Entry 24(i), $\displaystyle\sum_{k=1}^{\infty}\frac{x^k\sin(k\theta)}{k^2}+\sum_{k=1}^{\infty}\frac{y^k\sin(k\varphi)}{k^2}=-\varphi\log x-\theta\log y$.",
    ),
    rec(
        "RN-P1-C09-Entry25i",
        r"Let $x$, $y$, $\theta$, and $\varphi$ be real with $xe^{i\theta}+ye^{i\varphi}=xye^{i(\theta+\varphi)}$, $0\le x,y\le 1$, and $-\pi<\theta,\varphi\le\pi$. Then $\displaystyle\sum_{k=1}^{\infty}\frac{x^k\cos(k\theta)}{k^2}+\sum_{k=1}^{\infty}\frac{y^k\cos(k\varphi)}{k^2}=\tfrac{1}{2}\log(1-2x\cos\theta+x^2)\,\log(1-2y\cos\varphi+y^2)-\tan^{-1}\!\bigl(\tfrac{x\sin\theta}{1-x\cos\theta}\bigr)\tan^{-1}\!\bigl(\tfrac{y\sin\varphi}{1-y\cos\varphi}\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry25ii",
        r"Under the hypotheses of Entry 25(i), $\displaystyle\sum_{k=1}^{\infty}\frac{x^k\sin(k\theta)}{k^2}+\sum_{k=1}^{\infty}\frac{y^k\sin(k\varphi)}{k^2}=-\tfrac{1}{2}\log(1-2x\cos\theta+x^2)\tan^{-1}\!\bigl(\tfrac{y\sin\varphi}{1-y\cos\varphi}\bigr)-\tfrac{1}{2}\log(1-2y\cos\varphi+y^2)\tan^{-1}\!\bigl(\tfrac{x\sin\theta}{1-x\cos\theta}\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry26i",
        r"Let $x$, $y$, $\theta$, and $\varphi$ be real with $xe^{i\theta}+ye^{i\varphi}+xye^{i(\theta+\varphi)}=1$, $0\le x,y\le 1$, and $-\pi<\theta,\varphi\le\pi$. Then $\displaystyle\sum_{k=0}^{\infty}\frac{x^{2k+1}\cos(2k+1)\theta}{(2k+1)^2}+\sum_{k=0}^{\infty}\frac{y^{2k+1}\cos(2k+1)\varphi}{(2k+1)^2}=\tfrac{\pi^2}{8}-\tfrac{1}{2}\log x\,\log y+\tfrac{1}{2}\theta\varphi$.",
    ),
    rec(
        "RN-P1-C09-Entry26ii",
        r"Under the hypotheses of Entry 26(i), $\displaystyle\sum_{k=0}^{\infty}\frac{x^{2k+1}\sin(2k+1)\theta}{(2k+1)^2}+\sum_{k=0}^{\infty}\frac{y^{2k+1}\sin(2k+1)\varphi}{(2k+1)^2}=-\tfrac{1}{2}\varphi\log x-\tfrac{1}{2}\theta\log y$.",
    ),
    rec(
        "RN-P1-C09-Entry27a",
        r"Let $\varphi_r(x)=\sum_{k=1}^{x}k^r\log k$ for $r>-1$. For each nonnegative integer $k$, let $M_k(r)=\sum_{j=0}^{k}\frac{1}{r-j}$. "
        r"Then there exists a constant $C_r$ such that as $x\to\infty$, $\displaystyle\varphi_r(x)-\log x\Bigl\{\sum_{k=1}^{x}k^r-\zeta(-r)\Bigr\}\sim C_r-\frac{x^{r+1}}{(r+1)^2}+\sum_{k=1}^{\infty}\frac{B_{2k}\Gamma(r+1)M_{2k-2}(r)\,x^{r-2k+1}}{(2k)!\,\Gamma(r-2k+2)}$, where $B_k$ denotes the $k$th Bernoulli number.",
    ),
    rec(
        "RN-P1-C09-Entry27b",
        r"Let $C_r$ be as in Entry 27(a). Then if $r>0$, $\displaystyle C_r=\frac{2\Gamma(r+1)\zeta(r+1)}{(2\pi)^{r+1}}\Bigl\{\sin\!\bigl(\tfrac{\pi r}{2}\bigr)\log(2\pi)-\frac{\Gamma'(r+1)}{\Gamma(r+1)}-\tfrac{\pi}{2}\cos\!\bigl(\tfrac{\pi r}{2}\bigr)\Bigr\}+\frac{2\Gamma(r+1)\sin(\pi r/2)}{(2\pi)^{r+1}}\sum_{k=1}^{\infty}\frac{\log k}{k^{r+1}}$.",
    ),
    rec(
        "RN-P1-C09-Entry27-Corollary",
        r"If $r$ is an even positive integer, then $\displaystyle C_r=-\frac{\cos(\pi r/2)\Gamma(r+1)\zeta(r+1)}{2(2\pi)^r}$. In particular, $C_0=\tfrac{1}{2}\log(2\pi)$, $C_4=-\tfrac{3\zeta(5)}{4\pi^4}$, and $C_6=-\tfrac{45\zeta(7)}{32\pi^6}$.",
    ),
    rec(
        "RN-P1-C09-Entry27-Example01",
        r"$\displaystyle\lim_{x\to\infty}\frac{\exp(x^2-\tfrac{1}{2}\log x+\tfrac{1}{8}-\gamma)\prod_{k=1}^{x}k^{2k}}{\bigl(x^x(x+3)\sqrt[3]{x^2+1}\bigr)^{2x/(x+3)}}=\exp\!\Bigl\{-\tfrac{1}{2\pi^2}\sum_{k=1}^{\infty}\frac{\log k}{k^2}\Bigr\}$ (27.13). (Berndt notes Ramanujan's notebook version is misprinted; the factor $i$ in a denominator may be omitted.)",
    ),
    rec(
        "RN-P1-C09-Entry27-Example02",
        r"$\displaystyle\lim_{x\to\infty}\exp\!\bigl(\tfrac{x^3}{9}-\tfrac{x}{12}\bigr)\sum_{k=1}^{x}\Bigl(\tfrac{x}{k}\Bigr)^{k^2}=\exp\!\bigl(\tfrac{\zeta(3)}{4\pi^2}\bigr)$ (27.16).",
    ),
    rec(
        "RN-P1-C09-Entry28a",
        r"For $r\ge 2$, with $f(r,x)$ and $H_n$ as in (28.1)--(3.1), $\displaystyle f(r,x)=\frac{B_{r+1}(x+1)}{r+1}-\frac{H_{r-1}B_{r+1}}{r+1}=\frac{H_{r-1}B_{r+1}(x+1)}{r+1}-\sum_{1\le k\le r/2}\frac{B_{2k}r!\,H_{2k-1}x^{r-2k+1}}{(2k)!(r+1-2k)!}=\int_0^x f(r-1,t)\,dt$ (28.2).",
    ),
    rec(
        "RN-P1-C09-Entry28b",
        r"If $|x|<1$ and $r$ is any positive integer, with $\varphi_r$ defined by (28.3), then $\displaystyle\varphi_r(x)=\frac{H_{r-1}}{r+1}\bigl\{B_{r+1}(x+1)-B_{r+1}\bigr\}+\gamma x^{r+1}-\sum_{1\le k\le(r+1)/2}\frac{B_{2k}H_{2k-1}x^{r+1-2k}}{2k(2k-1)(r+1)}-r!\sum_{k=0}^{r}\zeta(-k)\,c_k x^{r-k}+\sum_{k=2}^{\infty}(-1)^k\frac{r!}{(k-1)!}\,\zeta(k)\,x^{r+k}$ (28.8), where $\gamma$ denotes Euler's constant and $c_k=-\zeta(-k)$ for $k\ge 0$.",
    ),
    rec(
        "RN-P1-C09-Entry29",
        r"Let $\varphi_r(x)$ be defined by (28.3), let $C_r$ be defined by (27.7), let $-1<x\le 0$, and let $n$ and $r$ be natural numbers. Then $\displaystyle\varphi_r(x)-n^r\sum_{k=0}^{n-1}\varphi_r\!\bigl(x-\tfrac{k}{n}\bigr)=\frac{B_{r+1}(x+1)}{r+1}\log n+\Bigl(1-\tfrac{1}{n^{r+1}}\Bigr)C_r$.",
    ),
    rec(
        "RN-P1-C09-Entry29-Corollary01",
        r"If $n$ and $r$ are any positive integers, then $\displaystyle\sum_{k=1}^{n-1}\binom{k}{r}\log n-r\sum_{k=1}^{n-1}\varphi_r\!\bigl(-\tfrac{k}{n}\bigr)=-\frac{B_{r+1}}{(r+1)}\Bigl(1-\tfrac{1}{n^{r+1}}\Bigr)C_r$.",
    ),
    rec(
        "RN-P1-C09-Entry29-Corollary02",
        r"If $r$ is any positive integer, then $\displaystyle\varphi_r\!\bigl(-\tfrac{1}{2}\bigr)=-\frac{B_{r+1}\log 2}{(r+1)2^r}+\Bigl(2-\tfrac{1}{2^r}\Bigr)C_r$.",
    ),
    rec(
        "RN-P1-C09-Entry30i",
        r"Let $0<x<1$. If $r$ is positive and even, then $\displaystyle\varphi_r(x-1)+\varphi_r(-x)=2C_r+\frac{r!\zeta(r+1)}{(2\pi)^r}\cos\!\bigl(\tfrac{\pi r}{2}\bigr)\sum_{k=1}^{\infty}\frac{\cos(2\pi kx)}{k^{r+1}}$.",
    ),
    rec(
        "RN-P1-C09-Entry30ii",
        r"Let $0<x<1$. If $r$ is positive and odd, then $\displaystyle\varphi_r(x-1)-\varphi_r(-x)=\frac{r!\zeta(r+1)}{(2\pi)^r}\sin\!\bigl(\tfrac{\pi r}{2}\bigr)\sum_{k=1}^{\infty}\frac{\sin(2\pi kx)}{k^{r+1}}$.",
    ),
    rec(
        "RN-P1-C09-Entry31a",
        r"Suppose that $\varphi_1(x)$ is defined by (28.3), and define $\psi(x)=\sum_{k=0}^{\infty}\binom{2k}{k}\frac{\sin^{2k+1}(\pi x)}{k\,2^{2k}(2k+1)^2}$. Then if $0<x\le\tfrac{1}{2}$, $\displaystyle\psi(x)=\pi\{\varphi_1(x-1)-\varphi_1(-x)\}+\pi x\log\!\bigl(2\sin(\pi x)\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry31bi",
        r"Let $\psi(x)$ be defined by (31.1) and let $h_k$ be defined by (8.2). Then $\displaystyle\psi(x)=\sum_{k=0}^{\infty}\frac{(-1)^k h_{k+1}}{2k+1}\tan^{2k+1}(\pi x)$.",
    ),
    rec(
        "RN-P1-C09-Entry31bii",
        r"With $\psi$ as in Entry 31(b), for $0\le x<\tfrac{1}{2}$, $\displaystyle\psi(x)+\psi(\tfrac{1}{2}-x)=\tfrac{\pi}{2}\log\!\bigl(2\cos(\pi x)\bigr)+\sum_{k=0}^{\infty}\frac{(-1)^k\tan^{2k+1}(\pi x)}{(2k+1)^2}$.",
    ),
    rec(
        "RN-P1-C09-Entry31biii",
        r"With $\psi$ as in Entry 31(b), for $0\le x\le\tfrac{1}{4}$, $\displaystyle\psi(\tfrac{1}{4}-x)+\tfrac{1}{2}\psi(2x)-\psi(x)=\tfrac{\pi}{2}\log\!\bigl(2\cos(\pi x)\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry31biv",
        r"With $\psi$ as in Entry 31(b), for $0\le x\le 1$, $\displaystyle\psi(\tfrac{1}{4}-x)+\psi(\tfrac{1}{4}+x)=\pi(1-2x)\log|2\cos(\pi x)|+\sum_{k=1}^{\infty}\frac{(-1)^{k+1}\sin(2\pi kx)}{k^2}$ (Berndt's corrected form; Ramanujan's notebook omits the series term).",
    ),
    rec(
        "RN-P1-C09-Entry31-Example01",
        r"$\displaystyle\psi\!\bigl(\tfrac{1}{4}\bigr)=\tfrac{\pi}{2}\log 2$.",
    ),
    rec(
        "RN-P1-C09-Entry31-Example02",
        r"$\displaystyle\psi\!\bigl(\tfrac{1}{3}\bigr)=\tfrac{1}{2}G+\tfrac{\pi}{8}\log 2$, where $G$ denotes Catalan's constant.",
    ),
    rec(
        "RN-P1-C09-Entry31-Example03",
        r"$\displaystyle\psi\!\bigl(\tfrac{1}{6}\bigr)=\tfrac{\pi}{12}\log(2+\sqrt3)$.",
    ),
    rec(
        "RN-P1-C09-Entry31-Example04",
        r"$\displaystyle\psi\!\bigl(\tfrac{1}{8}\bigr)=\tfrac{\pi}{4}\log(2+\sqrt2)$.",
    ),
    rec(
        "RN-P1-C09-Entry31-Example05",
        r"$\displaystyle 2\psi(x)-\tfrac{1}{2}\psi(2x)=\sum_{k=0}^{\infty}\frac{(-1)^k\tan^{2k+1}(\pi x)}{(2k+1)^2}$.",
    ),
    rec(
        "RN-P1-C09-Entry32",
        r"For $|x|\le\pi/4$, $\displaystyle\sum_{k=0}^{\infty}\frac{2^{2k}(k!)^2\sin^{2k+1}(2x)}{(2k)!(2k+1)^2}=2\sum_{k=0}^{\infty}\frac{(-1)^k\tan^{2k+1}x}{(2k+1)^2}$ (32.1).",
    ),
    rec(
        "RN-P1-C09-Entry32-Corollary01",
        r"For $|x|\le 1$, $\displaystyle\sum_{k=0}^{\infty}\frac{2^{2k}(k!)^2}{(2k)!(2k+1)^2}\Bigl(\frac{4x}{(1+x)^2}\Bigr)^k=\frac{1}{1+x}\sum_{k=0}^{\infty}\frac{(-x)^k}{(2k+1)^2}$ (32.2).",
    ),
    rec(
        "RN-P1-C09-Entry32-Corollary02",
        r"If $|x|\le\pi/4$, then $\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k 2^{2k}(k!)^2\tan^{2k+1}(2x)}{(2k)!(2k+1)^2}=2\sum_{k=0}^{\infty}\frac{\tan^{2k+1}x}{(2k+1)^2}$.",
    ),
    rec(
        "RN-P1-C09-Entry32-Example01",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{2^{2k}(k!)^2}{(2k)!(2k+1)^2}=2G$, where $G$ denotes Catalan's constant.",
    ),
    rec(
        "RN-P1-C09-Entry32-Example02",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{3^k(k!)^2}{(2k)!(2k+1)^2}=-\tfrac{\sqrt3}{3}\log 3-\tfrac{\pi^2}{3}+5\sum_{k=0}^{\infty}\frac{1}{(3k+1)^2}$.",
    ),
    rec(
        "RN-P1-C09-Entry32-Example03",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(k!)^2}{(2k)!(2k+1)^2}=\tfrac{8}{3}G-\tfrac{\pi}{3}\log(2+\sqrt3)$.",
    ),
    rec(
        "RN-P1-C09-Entry32-Example04",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{2^k(k!)^2}{(2k)!(2k+1)^2}=-\tfrac{\pi}{2\sqrt2}\log(1+\sqrt2)+\tfrac{\pi^2}{4\sqrt2}+4\sqrt2\sum_{k=0}^{\infty}\frac{(-1)^k}{(4k+1)^2}$.",
    ),
    rec(
        "RN-P1-C09-Entry32-Example05",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{2^{2k}(k!)^2}{(2k)!(2k+1)^2}\Bigl(1-\frac{3}{4k+1}\Bigr)=\tfrac{\pi}{4}\log(2+\sqrt3)$.",
    ),
    rec(
        "RN-P1-C09-Entry32-Example06",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k 2^{2k}(k!)^2}{(2k)!(2k+1)^2}=\tfrac{\pi^2}{8}-\tfrac{\pi^2}{2}\log(1+\sqrt2)$.",
    ),
    rec(
        "RN-P1-C09-Entry32-Example07",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(k!)^2}{(2k)!(2k+1)^2}=-\tfrac{\pi^2}{6}-\tfrac{3}{2}\log\!\bigl(\tfrac{\sqrt5+1}{2}\bigr)$.",
    ),
    rec(
        "RN-P1-C09-Entry33i",
        r"If $n$ is a positive integer, then $\displaystyle\int_0^{\pi/2}x\cos^n x\sin(nx)\,dx=\frac{\pi}{2^{n+2}}\sum_{k=1}^{n}(-1)^{k+1}\binom{n}{k}\frac{1}{k}$.",
    ),
    rec(
        "RN-P1-C09-Entry33ii",
        r"If $n$ is a positive integer, then $\displaystyle\int_0^{\pi/2}\cos^n x\sin(nx)\,dx=2^{n+1}\sum_{k=1}^{n}\frac{1}{k}$.",
    ),
    rec(
        "RN-P1-C09-Entry33-Corollary01",
        r"If $a_k=\int_1^2\frac{(\log t)^k}{t-1}\,dt$, then $a_1=\tfrac{1}{2}\zeta(2)$ and $a_2=\tfrac{1}{2}\zeta(3)$.",
    ),
    rec(
        "RN-P1-C09-Entry33-Corollary02",
        r"For each positive integer $n$, with $\varphi(x)=\int_1^2\frac{t^x-1}{t-1}\,dt$ as in (33.1), $\displaystyle\varphi(-n)=-\sum_{k=n}^{\infty}\frac{1}{k\,2^k}-H_{n-1}$.",
    ),
    rec(
        "RN-P1-C09-Entry34",
        r"Let $-\tfrac{1}{2}<x<1$. Then $\displaystyle\sum_{k=0}^{\infty}\frac{1}{(2k+1)^2}\binom{-x}{k+1}=\sum_{k=0}^{\infty}\frac{(-1)^k 2^{2k}(k!)^2 h_{k+1}}{(2k+1)!}\,x^{k+1}$ (34.1), where $h_k$ is defined by (8.2).",
    ),
    rec(
        "RN-P1-C09-Entry35",
        r"Define $K_r=\sum_{k=1}^{\infty}\frac{1}{k^r(k+1)}$ and $A_n=(1+\cos(\pi n))\zeta(n)$, where $r$ is a positive integer and $n$ is any integer (with $A_1=0$, $A_n=0$ for $n<0$, and $A_0=-1$). Then for each positive integer $r$, $\displaystyle K_r=\sum_{k=0}^{r-1}\frac{A_{r-k}}{\binom{-k-1}{r}}$ (35.1).",
    ),
    rec(
        "RN-P1-C09-Entry35-Example01",
        r"$\displaystyle K_2=\tfrac{\pi^2}{3}$.",
    ),
    rec(
        "RN-P1-C09-Entry35-Example02",
        r"$\displaystyle K_3=10-\pi^2$.",
    ),
    rec(
        "RN-P1-C09-Entry35-Example03",
        r"$\displaystyle K_4=\tfrac{\pi^4}{45}+\tfrac{10\pi^2}{3}-35$.",
    ),
    rec(
        "RN-P1-C09-Entry35-Example04",
        r"$\displaystyle K_5=126-\tfrac{35\pi^2}{3}-\tfrac{\pi^4}{9}$.",
    )
]
