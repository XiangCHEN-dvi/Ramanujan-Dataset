"""Part I, Chapter 6 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C06 = ["divergent-series"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C06}


CHAPTER_6 = [
    rec(
        "RN-P1-C06-Example01",
        r"The Euler--Maclaurin constant of the divergent series $\displaystyle\sum_{k=1}^\infty 1$ "
        r"is $-\tfrac{1}{12}$.",
    ),
    rec(
        "RN-P1-C06-Example02",
        r"The Euler--Maclaurin constant of the divergent series $\displaystyle\sum_{k=1}^\infty k$ "
        r"is $-\tfrac{1}{2}$ (equivalently, the Abel sum "
        r"$\displaystyle\sum_{k=1}^\infty (-1)^{k+1}k=\tfrac{1}{4}$).",
    ),
    rec(
        "RN-P1-C06-Entry04ii",
        r"If $h$ and $n$ are positive integers with $h>n$ and $f$ is analytic for all real numbers, then "
        r"$\displaystyle\varphi(h)=\varphi(n)-\sum_{k=1}^n f(k+h)"
        r"+\sum_{j=0}^h\sum_{k=1}^n\frac{k^j f^{(j)}(n)}{j!}$.",
    ),
    rec(
        "RN-P1-C06-Entry04-Example01",
        r"Let $h$ and $n$ be positive integers with $h$ fixed. Then as $n\to\infty$, "
        r"$\displaystyle\sum_{k=1}^h\frac{1}{k}\sim\gamma+\log n-\sum_{k=1}^{n-h}\frac{1}{k+h}$, "
        r"where $\gamma$ denotes Euler's constant.",
    ),
    rec(
        "RN-P1-C06-Entry04-Example02",
        r"If $h$ is not a negative integer, then "
        r"$\displaystyle\Gamma(h+1)=\lim_{n\to\infty}\frac{n^h n!}{(h+1)(h+2)\cdots(h+n)}$.",
    ),
    rec(
        "RN-P1-C06-Entry04-Example03",
        r"Let $\displaystyle\varphi(x)=\sum_{k\le x}\frac{1}{k}$. Then as $x\to\infty$, "
        r"$\displaystyle\varphi'(x)\sim\sum_{k=1}^\infty\frac{1}{(x+k)^2}$.",
    ),
    rec(
        "RN-P1-C06-Entry04-Example04",
        r"If $x$ is a nonnegative integer, then "
        r"$\displaystyle\frac{\Gamma'(x+1)}{\Gamma(x+1)}=-\gamma+\sum_{n\le x}\frac{1}{n}$, "
        r"where $\gamma$ denotes Euler's constant.",
    ),
    rec(
        "RN-P1-C06-Entry04-Example05",
        r"For $x\ge 0$, with $S_n(x)$ defined by "
        r"$\displaystyle S_n(x)=\frac{B_{n+1}(x+1)-B_{n+1}}{n+1}$ "
        r"and $S_{-1}(x)$ defined by "
        r"$\displaystyle S_{-1}(x)=\frac{\Gamma'(x+1)}{\Gamma(x+1)}+\gamma$, "
        r"$\displaystyle\int_0^x S_{-1}(t)\,dt=\log\Gamma(x+1)+\gamma x$.",
    ),
    rec(
        "RN-P1-C06-Entry04-Example06",
        r"If $S_{13}(x)$ is defined by "
        r"$\displaystyle S_n(x)=\frac{B_{n+1}(x+1)-B_{n+1}}{n+1}$ with $n=13$, then "
        r"$\displaystyle\int_0^x S_{13}(t)\,dt=\frac{S_{14}(x)}{14}-\frac{1}{12}$.",
    ),
    rec(
        "RN-P1-C06-Entry06",
        r"Suppose that $\varphi$ is analytic at the origin. If $C_n$ denotes the constant of "
        r"$\displaystyle\sum_{k=1}^\infty f^{(n)}(k)$, then in some neighborhood of the origin, "
        r"$\displaystyle\varphi(x)=-\sum_{n=1}^\infty\frac{C_n x^n}{n!}$.",
    ),
    rec(
        "RN-P1-C06-Entry06-Example01",
        r"For $|x|<1$, "
        r"$\displaystyle\log\Gamma(x+1)=-\gamma x+\sum_{k=2}^\infty\frac{(-1)^k\zeta(k)x^k}{k}$.",
    ),
    rec(
        "RN-P1-C06-Entry06-Example02",
        r"For $|x|<1$, with $S_{-1}(x)=\displaystyle\frac{\Gamma'(x+1)}{\Gamma(x+1)}+\gamma$, "
        r"$\displaystyle S_{-1}(x)=\sum_{k=1}^\infty\frac{(-1)^{k+1}\zeta(k+1)x^k}{k+1}$.",
    ),
    rec(
        "RN-P1-C06-Entry07",
        r"Let $c_n'$ be the constant of $\displaystyle\sum_{k=1}^\infty f(k/n)$; in particular, $c_1'=c$. "
        r"Define $\displaystyle\psi(x)=\sum_{k=0}^n\varphi(x-k)$ and "
        r"$\displaystyle\eta(x)=\sum_{k=1}^n f(k/n)$. Then "
        r"$\psi(x)-nc=\eta(x)-c_n'$.",
    ),
    rec(
        "RN-P1-C06-Entry07-Corollary01",
        r"$\displaystyle\sum_{k=1}^{n-1}\varphi\!\left(-\frac{k}{n}\right)=nc-c_n'$.",
    ),
    rec(
        "RN-P1-C06-Entry07-Corollary02i",
        r"$\displaystyle\varphi\!\left(-\tfrac{1}{2}\right)=2c-c_2'$.",
    ),
    rec(
        "RN-P1-C06-Entry07-Corollary02ii",
        r"The constant $c$ of $\displaystyle\sum_{k=1}^\infty\frac{1}{k}$ equals $c_0=c'_{1/2}$.",
    ),
    rec(
        "RN-P1-C06-Entry07-Corollary02iii",
        r"$\displaystyle\varphi\!\left(-\tfrac{1}{3}\right)+\varphi\!\left(-\tfrac{2}{3}\right)=3c-c_3'$.",
    ),
    rec(
        "RN-P1-C06-Entry07-Corollary02iv",
        r"$\displaystyle\varphi\!\left(-\tfrac{1}{2}\right)+\varphi\!\left(-\tfrac{1}{4}\right)=2c+c_2'-c_4'$.",
    ),
    rec(
        "RN-P1-C06-Entry07-Corollary02v",
        r"$\displaystyle\varphi\!\left(-\tfrac{1}{2}\right)+\varphi\!\left(-\tfrac{1}{3}\right)"
        r"=c+c_2'+c_3'-c_6'$.",
    ),
    rec(
        "RN-P1-C06-Entry10ii",
        r"In general, if "
        r"$\displaystyle\sum_{k=1}^\infty(a_{2k-1}-a_{2k})>\sum_{k=1}^\infty(a_{2k}-a_{2k+1})$, then "
        r"$\displaystyle\sum_{k=1}^\infty(-1)^{k+1}a_k=a_1-\sum_{k=1}^\infty(a_{2k}-a_{2k+1})$; "
        r"otherwise "
        r"$\displaystyle\sum_{k=1}^\infty(-1)^{k+1}a_k=a_1-\sum_{k=1}^\infty(-1)^{k+1}a_{k+1}$. "
        r"For instance, the divergent series constants "
        r"$\displaystyle\sum_{k=1}^\infty\{(2k-1)-2k\}=\tfrac{1}{4}$ and "
        r"$1-\displaystyle\sum_{k=1}^\infty\{2k-(2k+1)\}=\tfrac{1}{4}$.",
    ),
    rec(
        "RN-P1-C06-Entry10iii",
        r"Define the sum of two alternating series by "
        r"$\displaystyle\sum_{k=1}^\infty(-1)^{k+1}a_k+\sum_{k=1}^\infty(-1)^{k+1}b_k"
        r":=a_1+\sum_{k=1}^\infty(-1)^{k+1}(b_k-a_{k+1})$.",
    ),
    rec(
        "RN-P1-C06-Entry10-Example01",
        r"$\displaystyle\sum_{k=1}^\infty(-1)^{k+1}a_k+\sum_{k=1}^\infty(-1)^{k+1}b_k"
        r"=a_1+\sum_{k=1}^\infty(-1)^{k+1}(b_k-a_{k+1})$.",
    ),
    rec(
        "RN-P1-C06-Entry10-Example02",
        r"$\displaystyle\sum_{k=1}^\infty(-1)^{k+1}a_k"
        r"=\tfrac{1}{2}a_1+\tfrac{1}{2}\sum_{k=1}^\infty(-1)^{k+1}(a_k-a_{k+1})$.",
    ),
    rec(
        "RN-P1-C06-Entry10-Example03",
        r"$\displaystyle\sum_{k=1}^\infty(-1)^{k+1}a_k"
        r"=\tfrac{1}{2}(3a_1-a_2)+\tfrac{1}{2}\sum_{k=1}^\infty(-1)^{k+1}(a_k-2a_{k+1}+a_{k+2})$.",
    ),
    rec(
        "RN-P1-C06-Entry10-Example04",
        r"$\displaystyle\sum_{k=1}^\infty(-1)^{k+1}a_k"
        r"=\tfrac{1}{4}(7a_1-4a_2+a_3)"
        r"+\tfrac{1}{4}\sum_{k=1}^\infty(-1)^{k+1}(a_k-3a_{k+1}+3a_{k+2}-a_{k+3})$.",
    ),
    rec(
        "RN-P1-C06-Entry11",
        r"Put $\Delta a_k=a_k-a_{k+1}$ and $\Delta^n a_1=\Delta(\Delta^{n-1}a_1)$ for $n\ge 2$. "
        r"If $\displaystyle\sum_{k=1}^\infty(-1)^{k+1}a_k$ converges, then "
        r"$\displaystyle\sum_{k=1}^\infty(-1)^{k+1}a_k=\sum_{n=0}^\infty\frac{(-1)^n\Delta^n a_1}{2^{n+1}}$ "
        r"(Euler's transformation of series).",
    ),
    rec(
        "RN-P1-C06-Entry11-Examplea",
        r"If $y=x/(1+x/2)$, $|x|<1$, and $|y|<2$, then "
        r"$\displaystyle\sum_{k=1}^\infty\frac{(-1)^{k+1}x^k}{k}"
        r"=2\sum_{k=0}^\infty\frac{(y/2)^k}{2k+1}$.",
    ),
    rec(
        "RN-P1-C06-Entry11-Exampleb1",
        r"For $|x|<\pi^2/4$, "
        r"$\displaystyle\sum_{k=1}^\infty\frac{2^{2k}(2^{2k}-1)B_{2k}x^k}{(2k)!}"
        r"=\sqrt{x}\,\tanh\sqrt{x}"
        r"=\cfrac{x}{1+\cfrac{3}{1+\cfrac{-x}{5+\cfrac{-x}{7+\cdots}}}}$.",
    ),
    rec(
        "RN-P1-C06-Entry11-Exampleb2",
        r"Let $x$ be any complex number which is not nonpositive. Then formally "
        r"$\displaystyle\sum_{k=0}^\infty\frac{(-1)^k k!}{x^{k+1}}"
        r"=\cfrac{1}{x+1-\cfrac{1}{x+3-\cfrac{2^2}{x+5-\cfrac{3^2}{x+7-\cdots}}}}$ "
        r"(as an asymptotic expansion of $\displaystyle\int_0^\infty\frac{e^{-u}}{x+u}\,du$).",
    ),
    rec(
        "RN-P1-C06-Entry11-Examplec",
        r"As $x\to\infty$, "
        r"$\displaystyle\sum_{k=1}^\infty\frac{(-1)^{k+1}}{(x+1)(x+2)\cdots(x+k)}"
        r"\sim\sum_{k=1}^\infty\frac{(-1)^{k+1}B(k)}{x^k}$, "
        r"where $B(k)$ is the $k$th Bell number.",
    ),
    rec(
        "RN-P1-C06-Entry11-Example01",
        r"As $x\to\infty$, "
        r"$\displaystyle\sum_{k=1}^\infty\frac{(-1)^{k+1}}{x+k}"
        r"\sim\frac{1}{2x}-\sum_{k=1}^\infty\frac{(4k-1)B_{2k}}{2k\,x^{2k}}$.",
    ),
    rec(
        "RN-P1-C06-Entry14i",
        r"Let $x>0$. Then, for $n\ge 1$, "
        r"$\displaystyle\sum_{k=1}^\infty\frac{1}{e^{kx}+1}"
        r"=\frac{\log 2}{x}+\frac{1}{4}"
        r"+\sum_{k=1}^n\frac{(2^{2k}-1)B_{2k}x^{2k-1}}{(2k)(2k)!}+R_n$, "
        r"where $|R_n|<\dfrac{|B_{2n}B_{2n+2}|x^{2n}}{(2n)!}\left\{\dfrac{x^2}{4n^2}+\dfrac{n^2}{6}"
        r"+\dfrac{2^{2n+1}}{n^2}\left(\dfrac{x^2}{4n^2}+\dfrac{n^2}{6}\right)\right\}$.",
    ),
    rec(
        "RN-P1-C06-Entry14ii",
        r"Let $x>0$. Then, for $n\ge 1$, "
        r"$\displaystyle\sum_{k=1}^\infty\frac{1}{e^{kx}-1}"
        r"=\frac{\gamma}{x}-\frac{\log x}{4}-\frac{1}{2x}"
        r"+\sum_{k=1}^n\frac{B_{2k}x^{2k-1}}{(2k)(2k)!}+R_n$, "
        r"where $\gamma$ denotes Euler's constant and "
        r"$|R_n|<\dfrac{|B_{2n}B_{2n+2}|x^{2n}}{(2n)!}\left(\dfrac{x^2}{4n^2}+\dfrac{n^2}{6}\right)$.",
    ),
    rec(
        "RN-P1-C06-Entry14-Example01",
        r"The constant of the divergent series $\displaystyle\sum_{k=1}^\infty k^{1/100}$ is "
        r"approximately $-0.4909$.",
    ),
    rec(
        "RN-P1-C06-Entry14-Example02",
        r"$\displaystyle\sum_{k=1}^\infty\frac{1}{2k+1}\approx\frac{\pi}{4}+\frac{\log 2}{48}$.",
    ),
    rec(
        "RN-P1-C06-Entry14-Example03",
        r"$\displaystyle\sum_{k=1}^\infty\frac{(10/9)^k}{k+1}\approx 6.331009$.",
    ),
    rec(
        "RN-P1-C06-Entry14-Example04",
        r"$\displaystyle\sum_{k=1}^\infty\frac{(10/9)^k}{k-1}\approx 27$.",
    ),
    rec(
        "RN-P1-C06-Entry15i",
        r"For $|x|>1$, "
        r"$\displaystyle\sum_{k=1}^\infty\frac{1}{x^k-1}"
        r"=\sum_{k=1}^\infty\frac{x^{k+1}}{k^2(x^k-1)}$.",
    ),
    rec(
        "RN-P1-C06-Entry15ii",
        r"For $|x|>1$, "
        r"$\displaystyle\sum_{k=1}^\infty\frac{(-1)^{k+1}}{x^k-1}"
        r"=\sum_{k=1}^\infty\frac{(-1)^{k+1}(x^{2k}+1)}{x^k(x^{2k}-1)}$.",
    ),
    rec(
        "RN-P1-C06-Entry16",
        r"For each positive integer $n$, "
        r"$\displaystyle\sum_{k=1}^n\frac{r^k}{k(1-\alpha x^k)}"
        r"-\sum_{k=1}^n\frac{(\alpha x^k)^k}{k(1-\alpha x^k)}"
        r"=\sum_{k=1}^n\frac{(\alpha x^{k-1})^k\bigl(1-(\alpha x^{k-1})^{n+1}\bigr)}{k(1-\alpha x)}$.",
    ),
    rec(
        "RN-P1-C06-Entry16-Corollary",
        r"Let $|r|<1$ and $|x|\le 1$. If $|x|=1$, assume $|\alpha r|<1$. Then "
        r"$\displaystyle\sum_{k=1}^\infty\frac{r^k}{k(1-\alpha x^k)}"
        r"-\sum_{k=1}^\infty\frac{(\alpha x^k)^k}{k(1-\alpha x^k)}"
        r"=\sum_{k=1}^\infty\frac{(\alpha x^{k-1})^k}{k(1-\alpha x)}$.",
    ),
    rec(
        "RN-P1-C06-Entry17",
        r"Let $a$ and $b$ be arbitrary, $|x|\le 1$, and $|m|<1$. If $|x|=1$, assume $|mn|<1$. Then "
        r"$\displaystyle\sum_{k=0}^\infty\frac{(a+kb)x^k}{1-mx^k}"
        r"=\sum_{k=0}^\infty\frac{(a+kb)(1-mnx^{2k})(mnx^k)^k}{(1-mx^k)(1-nx^k)}"
        r"+\frac{b}{m}\sum_{k=0}^\infty\frac{(mnx^k)^{k+1}}{(1-nx^k)^2}$.",
    ),
    rec(
        "RN-P1-C06-Entry17-Corollary02",
        r"For $|x|>1$, "
        r"$\displaystyle\sum_{n=1}^\infty\frac{d(n)}{x^n}=\sum_{k=1}^\infty\frac{1}{x^k-1}$, "
        r"where $d(n)$ denotes the number of positive divisors of $n$.",
    ),
]
