"""Part II, Chapter 10 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C10 = ["hypergeometric-series-i"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C10}


CHAPTER_10 = [
    rec(
        "RN-P2-C10-Entry01",
        r"Suppose that at least one of the quantities $x$, $y$, $z$, $u$, or $-x-y-z-u-2n-1$ is a "
        r"positive integer. Then "
        r"$\displaystyle{}_7F_6\!\left[\begin{array}{c}n,\tfrac12n+1,-x,-y,-z,-u,x+y+z+u+2n+1\\"
        r"\tfrac12n,x+n+1,y+n+1,z+n+1,u+n+1,-x-y-z-u-n\end{array};1\right]"
        r"$=\displaystyle\frac{\Gamma(x+n+1)\Gamma(y+n+1)\Gamma(z+n+1)\Gamma(u+n+1)\Gamma(x+y+z+n+1)}"
        r"{\Gamma(n+1)\Gamma(x+y+n+1)\Gamma(y+z+n+1)\Gamma(x+u+n+1)\Gamma(z+u+n+1)}$"
        r"$\displaystyle\times\frac{\Gamma(y+z+u+n+1)\Gamma(x+u+z+n+1)\Gamma(x+y+u+n+1)}"
        r"{\Gamma(x+z+n+1)\Gamma(y+u+n+1)\Gamma(x+y+z+u+n+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry02",
        r"If either $x$, $y$, or $z$ is a positive integer, then "
        r"$\displaystyle{}_3F_2\!\left[\begin{array}{c}-x,-y,-z\\n+1,-x-y-z-n\end{array};1\right]"
        r"$=\displaystyle\frac{\Gamma(n+1)\Gamma(x+y+n+1)\Gamma(y+z+n+1)\Gamma(z+x+n+1)}"
        r"{\Gamma(x+n+1)\Gamma(y+n+1)\Gamma(z+n+1)\Gamma(x+y+z+n+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry03",
        r"If $x$, $y$, $z$, or $-x-y-z-2n$ is a positive integer, then "
        r"$\displaystyle{}_6F_5\!\left[\begin{array}{c}\tfrac12n+1,1,-x,-y,-z,x+y+z+2n\\"
        r"\tfrac12n,x+n+1,y+n+1,z+n+1,-x-y-z-n+1\end{array};1\right]"
        r"$=\displaystyle\frac{(x+n)(y+n)(z+n)(x+y+z+n)}{n(x+y+n)(y+z+n)(x+z+n)}$.",
    ),
    rec(
        "RN-P2-C10-Entry04",
        r"If either $x$, $y$, $z$, or $-x-y-z-2n-1$ is a positive integer, then "
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{(n+2k)(-x)_k(-y)_k(-z)_k(x+y+z+2n+1)_k}"
        r"{k(n+k)(x+n+1)_k(y+n+1)_k(z+n+1)_k(-x-y-z-n)_k}"
        r"$=\psi(x+n+1)+\psi(y+n+1)+\psi(z+n+1)+\psi(x+y+z+n+1)"
        r"-\psi(n+1)-\psi(x+y+n+1)-\psi(y+z+n+1)-\psi(z+x+n+1)$.",
    ),
    rec(
        "RN-P2-C10-Entry04-Examplei",
        r"If $x$ is a positive integer, then "
        r"$1-\dfrac{3(x-1)^3(4x-1)}{x+1}+\dfrac{5((x-1)(x-2))^3(4x-1)(4x)}{(x+1)(x+2)(4x-3)(4x-4)}+\cdots"
        r"$=\dfrac{\Gamma^4(x+1)\Gamma^4(3x-1)}{\Gamma^6(2x)\Gamma(4x-2)}$.",
    ),
    rec(
        "RN-P2-C10-Entry04-Exampleii",
        r"If $x$ is an odd positive integer, then "
        r"$\dfrac{(x-1)^3(3x-1)}{x+1}+\dfrac{((x-1)(x-3))^3(3x-1)(3x+1)}{2(x+1)(x+3)(3x-3)(3x-5)}+\cdots"
        r"$=\dfrac12\{\psi(\tfrac{x+1}{2})+3\psi(\tfrac{x+1}{3})-3\psi(x)-\psi(1)\}$.",
    ),
    rec(
        "RN-P2-C10-Entry04-Exampleiii",
        r"If $x$ is a positive integer, then "
        r"$1+\dfrac{3(x-1)^3}{3x-1}+\dfrac{5((x-1)(x-2))^3(3x-1)(3x)}{(x+1)(x+2)(3x-3)(3x-4)}+\cdots"
        r"$=\dfrac{x^3(3x-2)}{(2x-1)^3}$.",
    ),
    rec(
        "RN-P2-C10-Entry04-Exampleiv",
        r"If $x$ is a nonnegative integer, then "
        r"$1+\dfrac{(\frac{x}{2})^2}{3x}+\dfrac{(\frac{x(x-1)}{2})^2}{3x(3x-1)}+\cdots"
        r"$=\dfrac{\Gamma^3(2x+1)}{\Gamma^3(x+1)\Gamma(3x+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry04-Examplev",
        r"If $x$ is a positive integer, then "
        r"$1+\dfrac{x}{x+1}+\dfrac{x(x-1)}{2!}\dfrac{(x-1)(x-2)}{(x+1)(x+2)}+\cdots"
        r"$=\dfrac{8\Gamma^3(3x+1)\Gamma(x+1)}{9\Gamma^3(2x+1)\Gamma(4x+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry05",
        r"If $\operatorname{Re}(x+y+z+n+1)>0$, then "
        r"$\displaystyle{}_5F_4\!\left[\begin{array}{c}\tfrac12n+1,n,-x,-y,-z\\"
        r"\tfrac12n,x+n+1,y+n+1,z+n+1\end{array};1\right]"
        r"$=\displaystyle\frac{\Gamma(x+n+1)\Gamma(y+n+1)\Gamma(z+n+1)\Gamma(x+y+z+n+1)}"
        r"{\Gamma(n+1)\Gamma(x+y+n+1)\Gamma(y+z+n+1)\Gamma(x+z+n+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry06",
        r"If $\alpha+\beta+\gamma+1=n$, then as $m\to\infty$, "
        r"$\displaystyle\frac{\Gamma(n+2)\Gamma(\alpha+1)\Gamma(\beta+1)\Gamma(\gamma+1)}"
        r"{\Gamma(n-\alpha+1)\Gamma(n-\beta+1)\Gamma(n-\gamma+1)}"
        r"$\displaystyle\times{}_5F_4\!\left[\begin{array}{c}\tfrac12(n+3),n+1,\alpha+1,\beta+1,\gamma+1\\"
        r"\tfrac12(n+1),n-\alpha+1,n-\beta+1,n-\gamma+1\end{array};m\right]"
        r"$\displaystyle\sim 2\log m-\psi(\alpha+1)-\psi(\beta+1)-\psi(\gamma+1)-\gamma_E$, "
        r"where $\gamma_E$ denotes Euler's constant.",
    ),
    rec(
        "RN-P2-C10-Entry06b",
        r"If $a$, $b$, $c$, and $a+b+c$ are not nonpositive integers, then as $m\to\infty$, "
        r"$\displaystyle\frac{\Gamma(a+b+c)\Gamma(a)\Gamma(b)\Gamma(c)}"
        r"{\Gamma(b+c)\Gamma(a+c)\Gamma(a+b)}"
        r"$\displaystyle\times{}_5F_4\!\left[\begin{array}{c}\tfrac12(a+b+c+1),a+b+c-1,a,b,c\\"
        r"\tfrac12(a+b+c-1),b+c,a+c,a+b\end{array};m\right]"
        r"$\displaystyle=2\log m-\gamma_E-\psi(a)-\psi(b)-\psi(c)+O\!\left(\frac{\log m}{m}\right)$, "
        r"where $\gamma_E$ denotes Euler's constant.",
    ),
    rec(
        "RN-P2-C10-Entry06-Corollary",
        r"Let $0<x<1$. Then as $x\to 0$, "
        r"$\displaystyle\frac{\pi^2}{4}\,{}_5F_4\!\left[\begin{array}{c}\tfrac12,\tfrac12,\tfrac12,\tfrac12,\tfrac12\\"
        r"1,1,1,1,1\end{array};1-x\right]\sim-\log x+3\log 2$.",
    ),
    rec(
        "RN-P2-C10-Entry07",
        r"If $\operatorname{Re}(x+y+\tfrac12n+1)>0$, then "
        r"$\displaystyle{}_3F_2\!\left[\begin{array}{c}n,-x,-y\\x+n+1,y+n+1,\tfrac12n+1\end{array};1\right]"
        r"$=\displaystyle\frac{\Gamma(x+n+1)\Gamma(y+n+1)\Gamma(\tfrac12n+1)\Gamma(x+y+\tfrac12n+1)}"
        r"{\Gamma(n+1)\Gamma(x+y+n+1)\Gamma(x+\tfrac12n+1)\Gamma(y+\tfrac12n+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary01",
        r"If $\operatorname{Re}(x+y+n+1)>0$, then "
        r"$\displaystyle\sum_{k=1}^{\infty}\left(\frac{1}{k}+\frac{1}{n+k}\right)\frac{(-x)_k(-y)_k}{(x+n+1)_k(y+n+1)_k}"
        r"$=\psi(x+n+1)+\psi(y+n+1)-\psi(n+1)-\psi(x+y+n+1)$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary02",
        r"If $\operatorname{Re}(x+y+1)>0$, then "
        r"$\displaystyle{}_5F_4\!\left[\begin{array}{c}\tfrac12n+1,n,n,-x,-y\\"
        r"\tfrac12n,x+n+1,y+n+1,1\end{array};1\right]"
        r"$=\displaystyle\frac{\Gamma(x+n+1)\Gamma(y+n+1)\Gamma(x+y+1)}"
        r"{\Gamma(n+1)\Gamma(x+y+n+1)\Gamma(x+1)\Gamma(y+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary03",
        r"If $\operatorname{Re}(x+y+n)>0$, then "
        r"$\displaystyle{}_4F_3\!\left[\begin{array}{c}\tfrac12n+1,-x,-y,1\\"
        r"\tfrac12n,x+n+1,y+n+1\end{array};1\right]"
        r"$=\displaystyle\frac{(x+n)(y+n)}{n(x+y+n)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary04",
        r"If $\operatorname{Re}(x+y+\tfrac12(n+1))>0$, then "
        r"$\displaystyle{}_4F_3\!\left[\begin{array}{c}-\tfrac12n+1,n,-x,-y\\"
        r"\tfrac12n,x+n+1,y+n+1\end{array};1\right]"
        r"$=\displaystyle\frac{(x+n+1)_n(y+n+1)_n(n+1)_n(x+y+\tfrac12(n+1))_n}"
        r"{(n+1)_n(x+y+n+1)_n(x+\tfrac12(n+1))_n(y+\tfrac12(n+1))_n}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary05",
        r"For $\operatorname{Re}(2x+2y+n+2)>0$, "
        r"$\displaystyle{}_4F_3\!\left[\begin{array}{c}\tfrac12n+1,n,-x,-y\\"
        r"\tfrac12n,x+n+1,y+n+1\end{array};1\right]"
        r"$=\displaystyle\frac{(x+n+1)_n(y+n+1)_n}{(n+1)_n(x+y+n+1)_n}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary06",
        r"If $\operatorname{Re}(x+n+1)>0$, then "
        r"$\displaystyle\sum_{k=1}^{\infty}\left(\frac{1}{k}+\frac{1}{n+k}\right)\frac{(-x)_{k-1}(k-1)!}{(x+n+1)_k(n+1)_k}"
        r"$=\displaystyle\sum_{k=1}^{\infty}\frac{1}{(k+x+n)^2}-\sum_{k=1}^{\infty}\frac{1}{(k+n)^2}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary07",
        r"If $\operatorname{Re}(x-n+1)>0$, then "
        r"$\displaystyle{}_5F_4\!\left[\begin{array}{c}-\tfrac12n+1,n,n,n,-x\\"
        r"\tfrac12n,x+n+1,1,1\end{array};1\right]"
        r"$=\displaystyle\frac{\sin(\pi n)(x+n+1)_n(x-n+1)_n}{\pi n\Gamma^2(x+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary08",
        r"If $\operatorname{Re}(x-\tfrac12n+1)>0$, then "
        r"$\displaystyle{}_3F_2\!\left[\begin{array}{c}n,n,-x\\x+n+1,1\end{array};1\right]"
        r"$=\displaystyle\frac{\Gamma(x+n+1)\Gamma(\tfrac12n+1)\Gamma(x-\tfrac12n+1)}"
        r"{\Gamma(n+1)\Gamma(x+1)\Gamma(1-\tfrac12n)\Gamma(x+\tfrac12n+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary09",
        r"If $\operatorname{Re}(x-\tfrac12n+\tfrac12)>0$, then "
        r"$\displaystyle{}_4F_3\!\left[\begin{array}{c}\tfrac12n+1,n,n,-x\\"
        r"\tfrac12n,x+n+1,1\end{array};1\right]"
        r"$=\displaystyle\frac{\Gamma(x+n+1)\Gamma(\tfrac12n+\tfrac12)\Gamma(x-\tfrac12n+\tfrac12)}"
        r"{\Gamma(n+1)\Gamma(x+1)\Gamma(\tfrac12-\tfrac12n)\Gamma(x+\tfrac12n+\tfrac12)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary10",
        r"If $\operatorname{Re}(2x-n+2)>0$, then "
        r"$\displaystyle{}_4F_3\!\left[\begin{array}{c}\tfrac12n+1,n,n,-x\\"
        r"\tfrac12n,x+n+1,1\end{array};-1\right]=\dfrac{\Gamma(x+n+1)}{\Gamma(n+1)\Gamma(x+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary11",
        r"If $\operatorname{Re}x>-1$, then "
        r"$\displaystyle{}_3F_2\!\left[\begin{array}{c}\tfrac12n,n,-x\\"
        r"\tfrac12n+1,x+n+1\end{array};1\right]"
        r"$=\displaystyle\frac{\Gamma(x+n+1)\Gamma^2(\tfrac12n+1)\Gamma(x+1)}"
        r"{\Gamma(n+1)\Gamma^2(x+\tfrac12n+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary12",
        r"If $\operatorname{Re}x>-1$, then "
        r"$\displaystyle{}_2F_1(n,-x;x+n+1;1)=\dfrac{\Gamma(x+n+1)\Gamma(2x+1)}"
        r"{\Gamma(2x+n+1)\Gamma(x+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary13",
        r"If $\operatorname{Re}x>-1$, then "
        r"$\displaystyle{}_2F_1(n,-x;x+n+1;-1)=\dfrac{\Gamma(x+n+1)\Gamma(\tfrac12n+1)}"
        r"{\Gamma(x+\tfrac12n+1)\Gamma(n+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary14",
        r"If $\operatorname{Re}x>-1$, then "
        r"$\displaystyle{}_3F_2\!\left[\begin{array}{c}\tfrac12n+1,n,-x\\"
        r"\tfrac12n,x+n+1\end{array};-1\right]"
        r"$=\displaystyle\frac{\Gamma(x+n+1)\Gamma(\tfrac14n+1)}{\Gamma(n+1)\Gamma(x+2n+2)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary15",
        r"If $\operatorname{Re}n<1$, then "
        r"$\displaystyle{}_5F_4\!\left[\begin{array}{c}\tfrac14n+1,n,n,n,n\\"
        r"\tfrac14n,1,1,1\end{array};1\right]"
        r"$=\displaystyle\frac{\Gamma^2(n)\sin(\pi n)\tan(\pi n)}{n^2\Gamma(2n+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary16",
        r"If $\operatorname{Re}n<\tfrac12$, then "
        r"$\displaystyle{}_4F_3\!\left[\begin{array}{c}\tfrac14n+1,n,n,n\\"
        r"\tfrac14n,1,1\end{array};1\right]"
        r"$=\displaystyle\frac{\sin(\pi n)\Gamma(\tfrac14n+1)\Gamma(1-\tfrac14n)}"
        r"{2\pi n\Gamma(2-2n)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary17",
        r"If $\operatorname{Re}n<\tfrac23$, then "
        r"$\displaystyle{}_4F_3\!\left[\begin{array}{c}\tfrac14n+1,n,n,n\\"
        r"2n,1,1\end{array};-1\right]=\dfrac{\sin(\pi n)}{\pi n}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary18",
        r"If $\operatorname{Re}n<1$, then "
        r"$\displaystyle{}_3F_2\!\left[\begin{array}{c}\tfrac14n,n,n\\"
        r"\tfrac14n+1,1\end{array};1\right]"
        r"$=\displaystyle\frac{2\tan(\tfrac14\pi n)\Gamma^4(\tfrac14n+1)}"
        r"{\pi n\Gamma^2(n+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary19",
        r"If $\operatorname{Re}n<2$, then "
        r"$\displaystyle{}_3F_2\!\left[\begin{array}{c}\tfrac14n,\tfrac14n,n\\"
        r"\tfrac14n+1,\tfrac14n+1\end{array};1\right]"
        r"$=\displaystyle\frac{\pi n\Gamma^2(\tfrac14n+1)}{2\sin(\tfrac14\pi n)\Gamma(n+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary20",
        r"If $\operatorname{Re}(2x+n+2)>0$, then "
        r"$\displaystyle\sum_{k=1}^{\infty}\left(\frac{1}{k}+\frac{1}{n+x+k}\right)\frac{(-1)^k(-x)_k}{(n+x+k)_k}"
        r"$=\psi(x+n+1)-\psi(n+1)$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary21",
        r"If $\operatorname{Re}x>-1$, then "
        r"$\displaystyle\sum_{k=1}^{\infty}\left(\frac{1}{k}+\frac{1}{n+k}\right)\frac{(-x)_k}{(x+n+1)_k}"
        r"$=\displaystyle\sum_{k=1}^{\infty}\left(\frac{1}{k+n}+\frac{1}{k+x}-\frac{1}{k+x+n}-\frac{1}{k}\right)$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary22",
        r"If $\operatorname{Re}n>0$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\left(\frac{1}{k+1}+\frac{1}{n+k}\right)\frac{(1)_k}{(n+1)_k}"
        r"$=2\sum_{k=0}^{\infty}\frac{1}{(k+n)^2}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary23",
        r"If $\operatorname{Re}n>-2$, then "
        r"$\displaystyle\sum_{k=1}^{\infty}\left(\frac{1}{k}-\frac{1}{n+k}\right)\frac{(k-1)!}{(n+1)_k}"
        r"$=\displaystyle\sum_{k=1}^{\infty}\frac{1}{(k+\tfrac12n)^2}-\sum_{k=1}^{\infty}\frac{1}{(k+n)^2}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Corollary24",
        r"If $\operatorname{Re}n<1$, then "
        r"$\displaystyle\sum_{k=1}^{\infty}\left(\frac{1}{k}+\frac{1}{n+k}\right)\frac{(n)_k}{(k!)^2}"
        r"$=\displaystyle\sum_{k=1}^{\infty}\left(\frac{1}{k+n}+\frac{1}{k-n}\right)$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example01",
        r"If $\operatorname{Re}x>\tfrac12$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}(2k+1)\frac{(1-x)_k^2}{(1+x)_k^2}"
        r"$=\dfrac{\Gamma^3(x+\tfrac12)\Gamma(3x-1)}{\Gamma^2(2x)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example02",
        r"If $\operatorname{Re}x>\tfrac12$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(2k+1)(1-x)_k^2}{(1+x)_k^2}=\frac{x^2}{x^2-1}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example03",
        r"If $\operatorname{Re}x>\tfrac12$, then "
        r"$1+(x-1)^2+\dfrac{((x-1)(x-2))^2}{(x+1)(x+2)}+\cdots"
        r"$=\dfrac{2x\Gamma^4(x+1)\Gamma(4x+1)}{(4x-1)\Gamma^4(2x+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example04",
        r"If $\operatorname{Re}x>\tfrac12$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}(-1)^k(2k+1)\frac{(1-x)_k^2}{(1+x)_k^2}"
        r"$=\dfrac{\Gamma^2(x+1)}{\Gamma(2x)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example05",
        r"If $\operatorname{Re}x>\tfrac12$, then "
        r"$1+\dfrac{3(x-1)}{x+1}+\dfrac{5(x-1)(x-2)}{(x+1)(x+2)}+\cdots=x$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example06",
        r"If $\operatorname{Re}x>0$, then "
        r"$1+\dfrac{x-1}{x+1}+\dfrac{(x-1)(x-2)}{(x+1)(x+2)}+\cdots"
        r"$=\dfrac{2^{2x-1}\Gamma^2(x+1)}{\Gamma(2x+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example07",
        r"If $\operatorname{Re}x>1$, then "
        r"$1-\dfrac{x-1}{x+1}+\dfrac{(x-1)(x-2)}{(x+1)(x+2)}-\cdots=\dfrac{x}{2x-1}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example08",
        r"If $\operatorname{Re}x>1$, then "
        r"$1-\dfrac{3(x-1)}{x+1}+\dfrac{5(x-1)(x-2)}{(x+1)(x+2)}-\cdots=0$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example09",
        r"If $\operatorname{Re}x>0$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(1-x)_k}{(k+1)(1+x)_k}"
        r"$=\dfrac{2^{2x-2}\Gamma^2(x)}{\Gamma(2x)}+\dfrac12\sum_{k=1}^{\infty}\left(\frac{1}{k}-\frac{1}{k+x-1}\right)$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example10",
        r"If $\operatorname{Re}x>0$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(1-x)_k}{(k+1)(1+x)_k}"
        r"$=\dfrac{1}{2x}+\sum_{k=1}^{\infty}\left(\frac{1}{k+x}-\frac{1}{k+2x}\right)$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example11",
        r"If $\operatorname{Re}x>0$, then "
        r"$1-\dfrac{3(x-1)}{x+1}+\dfrac{5(x-1)(x-2)}{(x+1)(x+2)}-\cdots"
        r"$=\dfrac{6\Gamma^4(x+1)}{\Gamma^2(2x+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example12",
        r"If $x$ is a positive integer, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(1-x)_k}{(k+1)^2(1+x)_k}"
        r"$=\dfrac{x}{2}\sum_{k=1}^{\infty}\frac{1}{k+x}+\dfrac{x}{2}\sum_{k=1}^{\infty}\frac{1}{k^2}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example13",
        r"If $\operatorname{Re}x>\tfrac12$, then "
        r"$1+\dfrac{3^3(x-1)}{x+1}+\dfrac{5^3(x-1)(x-2)}{(x+1)(x+2)}+\cdots=x(4x-3)$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example14",
        r"$1-\dfrac{5(\frac12)^3}{2\cdot 4}+\dfrac{9(\frac12)^3}{2\cdot 4\cdot 6}-\cdots=\pi$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example15",
        r"$1+\dfrac{(\frac14)^4}{4\cdot 8}+\dfrac{(\frac15)^4}{4\cdot 8\cdot 12}+\cdots=\dfrac{2}{\pi\sqrt{2}}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example16",
        r"$1+\dfrac{(\frac12)^2}{5}+\dfrac{(\frac12\cdot\frac32)^2}{9}+\cdots"
        r"$=\dfrac{\pi^2}{4\Gamma^4(\tfrac34)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example17",
        r"$1+\dfrac{(\frac12)}{5}+\dfrac{(\frac12\cdot\frac32)}{9}+\cdots"
        r"$=\dfrac{\pi^{3/2}}{2\sqrt{2}\,\Gamma^2(\tfrac34)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example18",
        r"$1+\dfrac{(\frac12)^3}{2}+\dfrac{(\frac12\cdot\frac32)^3}{2\cdot 4}+\cdots"
        r"$=\dfrac{\pi}{\Gamma^4(\tfrac14)}$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example19",
        r"$\displaystyle{}_2F_1(1,1;1;-1)=-1$.",
    ),
    rec(
        "RN-P2-C10-Entry07-Example20",
        r"If $\operatorname{Re}n<\tfrac12$, then "
        r"$1+\dfrac{(\frac{n}{2})^3}{1!}+\dfrac{(n(n+1))^3}{2!}+\cdots"
        r"$=\dfrac{6\sin(\tfrac12\pi n)\sin(\pi n)\Gamma^3(\tfrac14n+1)}"
        r"{n^2\pi^2(1+2\cos(\pi n))\Gamma(\tfrac34n+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry08",
        r"If $\operatorname{Re}(x+y+n+1)>0$, then "
        r"$\displaystyle{}_2F_1(-x,-y;n+1;1)=\dfrac{\Gamma(n+1)\Gamma(x+y+n+1)}"
        r"{\Gamma(x+n+1)\Gamma(y+n+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry09",
        r"If $\operatorname{Re}(\alpha-\beta)>0$, then "
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{(\beta)_k}{\alpha_k}=\psi(\alpha)-\psi(\alpha-\beta)$.",
    ),
    rec(
        "RN-P2-C10-Entry10",
        r"If $\operatorname{Re}x>-1$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(-x)_k}{(n+k)_k k!}"
        r"$=\dfrac{\Gamma(n)\Gamma(x+1)}{\Gamma(n+x+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry10-Example01",
        r"If $\operatorname{Re}n>-1$, then "
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{(k-1)!}{k(n+1)_k}=\sum_{k=1}^{\infty}\frac{1}{(k+n)^2}$.",
    ),
    rec(
        "RN-P2-C10-Entry10-Example02",
        r"If $\operatorname{Re}n<1$, then "
        r"$\dfrac{1}{n}+\dfrac{n}{(n+1)1!}+\dfrac{n(n+1)}{(n+2)2!}+\cdots=\dfrac{n}{\sin(\pi n)}$.",
    ),
    rec(
        "RN-P2-C10-Entry10-Example03",
        r"If $n$ is arbitrary, then "
        r"$\dfrac{1}{n+1}+\dfrac{1}{n+2}\dfrac{(\frac12)}{2!}+\dfrac{1}{n+3}\dfrac{(\frac12\cdot\frac32)}{2\cdot 4}+\cdots"
        r"$=\dfrac{\sqrt{\pi n}}{\Gamma(n+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry10-Example04",
        r"If $\operatorname{Re}n>-1$, then "
        r"$\dfrac{n}{3\cdot 1!}-\dfrac{n(n-1)}{5\cdot 2!}+\cdots=\dfrac{\sqrt{\pi n}}{2\Gamma(n+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry10-Example05",
        r"If $\operatorname{Re}x>-1$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(-x)_k}{(n+k)_k k!}"
        r"$=\dfrac{\Gamma(n)\Gamma(x+1)}{\Gamma(n+x+1)}\sum_{k=1}^{\infty}\left(\frac{1}{k+n-1}-\frac{1}{k+n+x}\right)$.",
    ),
    rec(
        "RN-P2-C10-Entry10-Example06",
        r"If $n$ is arbitrary, then "
        r"$\dfrac{1}{(n+1)^2}+\dfrac{1}{(n+2)^2}\dfrac{(\frac12)}{2}+\dfrac{1}{(n+3)^2}\dfrac{(\frac12\cdot\frac32)}{2\cdot 4}+\cdots"
        r"$=\dfrac{\sqrt{\pi n}}{\Gamma(n+1)}\sum_{k=1}^{\infty}\left(\frac{1}{k+n}-\frac{1}{k+n+\tfrac12}\right)$.",
    ),
    rec(
        "RN-P2-C10-Entry10-Example07",
        r"If $\operatorname{Re}n<1$, then "
        r"$\dfrac{n}{n^2}+\dfrac{n(n+1)}{(n+1)1!}+\dfrac{n(n+1)}{(n+2)2!}+\cdots"
        r"$=\dfrac{n}{\sin(\pi n)}\sum_{k=1}^{\infty}\left(\frac{1}{k+n-1}-\frac{1}{k}\right)$.",
    ),
    rec(
        "RN-P2-C10-Entry11",
        r"Let $n>0$ and suppose that $\operatorname{Re}(\alpha-\beta-1)>0$. Then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(\alpha+k)_n-(\beta+1+k)_n}{(\alpha+1)_k}\bigl((\beta+1)_k\bigr)^n=\alpha^n$.",
    ),
    rec(
        "RN-P2-C10-Entry11-Corollary01",
        r"If $\operatorname{Re}(\alpha-\beta-1)>0$, then "
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{(\beta)_k}{(\alpha)_k}=\dfrac{\beta}{\alpha-\beta-1}$.",
    ),
    rec(
        "RN-P2-C10-Entry11-Corollary02",
        r"If $\operatorname{Re}(\alpha-\beta-1)>0$, then "
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{(\alpha+\beta+2k-1)(\beta)_k^2}{(\alpha)_k}"
        r"$=\dfrac{\beta^2}{\alpha-\beta-1}$.",
    ),
    rec(
        "RN-P2-C10-Entry12a",
        r"Suppose that $f(x)=\sum_{k=1}^{\infty}A_k x^k/k$ in some neighborhood of the origin. "
        r"Define $P_k$, $0\le k<\infty$, by $e^{f(x)}=\sum_{k=0}^{\infty}P_k x^k$. Then $P_0=1$ and, for $n\ge 1$, "
        r"$nP_n=\sum_{k=1}^{n}A_k P_{n-k}$.",
    ),
    rec(
        "RN-P2-C10-Entry12b",
        r"For positive integers $n$ and $r$, define $S_r=S_r(n)=\sum_{k=1}^{n}a_k$ and "
        r"$\Omega_r=\Omega_r(n)=\sum_{1\le k_1<\cdots<k_r\le n}a_{k_1}\cdots a_{k_r}$, where $a_1,a_2,\ldots,a_n$ are "
        r"arbitrary nonzero complex numbers. Then, if $r\ge 1$ and $\Omega_0=1$, "
        r"$r\Omega_r=\sum_{k=1}^{r}(-1)^{k+1}S_k\Omega_{r-k}$.",
    ),
    rec(
        "RN-P2-C10-Entry13",
        r"If $\operatorname{Re}x>-1$ and $r$ is any positive integer, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(-x)_k}{(n+k)^{r+1}k!}"
        r"$=\dfrac{\Gamma(n)\Gamma(x+1)}{\Gamma(n+x+1)}\varphi(r)$, "
        r"where $S_r=S_r(n,x)$ and $\varphi(r)=\varphi(n,x,r)$ are defined by (13.1) and (13.2).",
    ),
    rec(
        "RN-P2-C10-Entry13-Corollary01",
        r"Let $S_r(n,x)$ and $\varphi(n,x,r)$ be defined by (13.1) and (13.2), respectively. "
        r"If $n=1$ and $x=-1$, then $S_1=2\log 2$, $S_r=(2^r-2)\zeta(r)$ for $r\ge 2$, and "
        r"$\dfrac{1}{3^{r+1}}+\dfrac{(\frac12)}{5^{r+1}}+\dfrac{(\frac12\cdot\frac32)}{7^{r+1}\,2\cdot 4}+\cdots"
        r"$=\dfrac{\pi}{2^{r+1}}\varphi(r)$ for $r\ge 1$.",
    ),
    rec(
        "RN-P2-C10-Entry13-Corollary02",
        r"Let $S_r$ and $\varphi(r)$ be defined by (13.1) and (13.2), respectively, with $n=1$ and $x=-\tfrac12$. "
        r"Then $S_1=2-2\log 2$, $S_r=(2-2^r)\zeta(r)+2^r$ for $r\ge 2$, and "
        r"$\dfrac{1}{2^{r+1}}+\dfrac{(\frac12)}{3^{r+1}}+\dfrac{(\frac12\cdot\frac32)}{5^{r+1}\,2\cdot 4}+\cdots"
        r"$=2\varphi(r)$ for $r\ge 1$.",
    ),
    rec(
        "RN-P2-C10-Entry13-Example01",
        r"$1+\dfrac{1}{3^3}+\dfrac{(\frac12\cdot\frac32)}{5^3\,2\cdot 4}+\cdots"
        r"$=-\dfrac{(\log 2)^2}{4}+\dfrac{\pi^2}{48}$.",
    ),
    rec(
        "RN-P2-C10-Entry13-Example02",
        r"$\displaystyle\int_0^{\pi/2}\theta\cot\theta\,\log(\sin\theta)\,d\theta"
        r"$=-\dfrac{(\log 2)^2}{4}-\dfrac{\pi^3}{48}$.",
    ),
    rec(
        "RN-P2-C10-Entry14",
        r"Let $n$ be an integer with $n\ge 2$. Then "
        r"$\displaystyle 2\sum_{k=1}^{\infty}\frac{1}{k(k+x)^n}\sum_{j=1}^{k-1}\frac{1}{j}"
        r"$=nS_{n+1}(x)-\sum_{r=1}^{n-2}S_{r+1}(x)S_{n-r}(x)"
        r"$-2\sum_{k=1}^{\infty}\frac{1}{(k+x)^n}\sum_{j=0}^{k-1}\frac{1}{j+x}"
        r"$+2\sum_{k=1}^{\infty}\sum_{j=0}^{k-1}\frac{1}{(j+x)^n}\left(\frac{1}{k-j}-\frac{1}{k+x}\right)$, "
        r"where $S_r(x)=S_r(n,x)$ is defined by (13.1).",
    ),
    rec(
        "RN-P2-C10-Entry15",
        r"If $\alpha$ and $\beta$ are arbitrary complex numbers, then as $n\to\infty$, "
        r"$\displaystyle\sum_{k=0}^{n-1}\frac{\Gamma(\alpha+k+1)\Gamma(\beta+k+1)}"
        r"{\Gamma(\alpha+\beta+k+2)k!}\sim\log n-\psi(\alpha+1)-\psi(\beta+1)-\gamma_E$.",
    ),
    rec(
        "RN-P2-C10-Entry15-Corollary",
        r"Let $0<x<1$. Then as $x\to 0$, "
        r"$\displaystyle\frac{\pi^2}{2}\,{}_2F_1\!\left(\tfrac12,\tfrac12;1;1-x\right)\sim\log x+4\log 2$.",
    ),
    rec(
        "RN-P2-C10-Entry16",
        r"If $A_0,A_1,\ldots,A_r$ are any complex numbers and "
        r"$P_r=\sum_{k=0}^{r}A_k(-1)^k\binom{r}{k}$ for $r\ge 0$, then "
        r"$A_r=\sum_{k=0}^{r}(-1)^{r-k}\binom{r}{k}P_k$.",
    ),
    rec(
        "RN-P2-C10-Entry17",
        r"Suppose that $f(x)=f(r,x)=\sum_{k=0}^{\infty}\frac{(r)_k A_k}{k!\,x^{r+k}}$ is analytic for $|x|>R$. "
        r"For $|x|>\max(R,|h|)$, write $f(x)=\sum_{k=0}^{\infty}\frac{(r)_k B_k}{k!\,(x+h)^{r+k}}$. Then "
        r"$B_n=\sum_{k=0}^{n}\binom{n}{k}A_{n-k}(-h)^k$ for $n\ge 0$.",
    ),
    rec(
        "RN-P2-C10-Entry18i",
        r"Suppose that (17.1) holds. Assume also that "
        r"$f(x)=\sum_{k=0}^{\infty}\frac{(-1)^k(r)_k A_k}{k!\,x^{r+k}}$ for $|x|>\max(R,1)$. "
        r"Furthermore, assume that $\sum_{k=0}^{\infty}A_k x^k/k!$ is analytic for $|x|<R^*$. "
        r"Then for $|x|<R^*$, "
        r"$\displaystyle e^x\sum_{k=0}^{\infty}\frac{A_k(-x)^k}{k!}=\sum_{k=0}^{\infty}\frac{A_k x^k}{k!}$.",
    ),
    rec(
        "RN-P2-C10-Entry18ii",
        r"Suppose that (17.1) and (18.1) hold. Then "
        r"$\displaystyle\frac{1}{\varphi'(x)}\sum_{k=0}^{\infty}\frac{(r)_k A_k}{k!}"
        r"\left\{\frac{\varphi(x)-\varphi(-x)}{\varphi(x)}\right\}^k$ "
        r"is an even function of $x$.",
    ),
    rec(
        "RN-P2-C10-Entry18iii",
        r"Suppose that (17.1) and (18.1) hold. Then, if $n$ is an even integer with $n\ge 2$, "
        r"$\displaystyle\frac{1}{n}A_{n-1}=\sum_{k=1}^{n/2}\binom{n}{2k}(2^{2k}-1)B_{2k}A_{n-2k}$, "
        r"where $B_j$ denotes the $j$th Bernoulli number.",
    ),
    rec(
        "RN-P2-C10-Entry19",
        r"Suppose that $|x|,|x-1|>1$. Then "
        r"$x^{-r}{}_2F_1(r,m;n;1/x)=(x-1)^{-r}{}_2F_1(r,n-m;n;-1/(x-1))$.",
    ),
    rec(
        "RN-P2-C10-Entry20",
        r"Let $\displaystyle\varphi(x)=\sum_{r=0}^{\infty}\frac{\varphi^{(r)}(1)}{r!}(x-1)^r$ be analytic for $|x-1|<R$, "
        r"where $R>1$. Suppose that $m$ and $n$ are complex parameters such that the order of summation in "
        r"$\sum_{k=0}^{\infty}\sum_{r=k}^{\infty}$ may be inverted. Then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(m)_k\varphi^{(k)}(0)}{(n)_k k!}"
        r"$=\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(n-m)_k\varphi^{(k)}(1)}{(n)_k k!}$.",
    ),
    rec(
        "RN-P2-C10-Entry21",
        r"For any complex numbers $m$, $n$, and $x$, "
        r"$\displaystyle e^x\sum_{k=0}^{\infty}\frac{(-1)^k(n-m)_k x^k}{(n)_k k!}"
        r"$=\displaystyle\sum_{r=0}^{\infty}\frac{(m)_r x^r}{(n)_r r!}$.",
    ),
    rec(
        "RN-P2-C10-Entry22",
        r"Suppose that $|x|,|x+1|>1$. Then "
        r"$(x+1)^r{}_2F_1(r,m;2m;1/(x+1))=x^{-r}{}_2F_1(r,m;2m;-1/x)$.",
    ),
    rec(
        "RN-P2-C10-Entry23",
        r"Let $m$ and $x$ be any complex numbers. Then "
        r"$\displaystyle e^x\sum_{k=0}^{\infty}\frac{(-1)^k(m)_k x^k}{(2m)_k k!}"
        r"$=\displaystyle\sum_{r=0}^{\infty}\frac{(m)_r x^r}{(2m)_r r!}$.",
    ),
    rec(
        "RN-P2-C10-Entry23-Corollary01",
        r"If $x$ is any complex number, then "
        r"$\displaystyle e^x\sum_{k=0}^{\infty}\frac{(-1)^k(\tfrac12)_k x^k}{(1)_k k!}"
        r"$=\displaystyle\sum_{r=0}^{\infty}\frac{(\tfrac12)_r x^r}{(1)_r r!}$.",
    ),
    rec(
        "RN-P2-C10-Entry23-Corollary02",
        r"If $|x|<1$ and $\operatorname{Re}x<\tfrac12$, then "
        r"${}_2F_1\!\left(\tfrac12,\tfrac12;1;\frac{x}{1-x}\right)"
        r"$=\dfrac{1}{\sqrt{1-x}}\,{}_2F_1\!\left(1,\tfrac12;1;x\right)$.",
    ),
    rec(
        "RN-P2-C10-Entry24",
        r"Let $|x|,|x-1|>1$ and suppose that $m$ is arbitrary and that $\operatorname{Re}n>0$. Then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(m)_k}{(n+k)_k k!}x^{n+k}"
        r"$=\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(n+1-m)_k}{(n+k)_k k!}(x-1)^{n+k}$.",
    ),
    rec(
        "RN-P2-C10-Entry25",
        r"Let $|x|,|x-1|>1$ and suppose that $n$ is arbitrary. Then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{k!}{(n)_{k+1}}x^{k+1}"
        r"$=\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k}{(n+k)(x-1)^{k+1}}$.",
    ),
    rec(
        "RN-P2-C10-Entry26",
        r"If $|x|<1$ and $\alpha$, $\beta$, and $\gamma$ are arbitrary, then "
        r"$(1-xy)^{-\beta}{}_2F_1(\alpha,\beta;\gamma;x)"
        r"$=(1-x)^{\gamma}{}_2F_1(\gamma-\alpha,\gamma-\beta;\gamma;x)$.",
    ),
    rec(
        "RN-P2-C10-Entry27",
        r"If $\operatorname{Re}(n+1)>-\operatorname{Re}(x+y)$ and $-\operatorname{Re}(p+q)$, then "
        r"$\displaystyle\frac{\Gamma(x+y+n+1)}{\Gamma(x+n+1)\Gamma(y+n+1)}"
        r"{}_3F_2\!\left[\begin{array}{c}-p,-q,x+y+n+1\\x+n+1,y+n+1\end{array};1\right]"
        r"$=\displaystyle\frac{\Gamma(p+q+n+1)}{\Gamma(p+n+1)\Gamma(q+n+1)}"
        r"{}_3F_2\!\left[\begin{array}{c}-x,-y,p+q+n+1\\p+n+1,q+n+1\end{array};1\right]$.",
    ),
    rec(
        "RN-P2-C10-Entry28",
        r"If $\operatorname{Re}(n+1)>-\operatorname{Re}(x+y)$ and $-\operatorname{Re}(p-1)$, then "
        r"$\displaystyle{}_3F_2\!\left[\begin{array}{c}-x,-y,p+n\\n,p+n+1\end{array};1\right]"
        r"$=\displaystyle\frac{(p+n)\Gamma(n)\Gamma(x+y+n+1)}{\Gamma(x+n+1)\Gamma(y+n+1)}"
        r"$\displaystyle\times{}_3F_2\!\left[\begin{array}{c}-p,1,x+y+n+1\\x+n+1,y+n+1\end{array};1\right]$.",
    ),
    rec(
        "RN-P2-C10-Entry29a",
        r"If $\operatorname{Re}n>-1$, then "
        r"$\displaystyle{}_3F_2\!\left[\begin{array}{c}\tfrac12,\tfrac12,n+1\\1,n+2\end{array};1\right]"
        r"$=\dfrac{4(n+1)}{n+2}\,{}_3F_2\!\left[\begin{array}{c}-n,1,1\\\tfrac12,\tfrac12\end{array};1\right]$.",
    ),
    rec(
        "RN-P2-C10-Entry29b",
        r"If $n$ is a nonnegative integer, then "
        r"$\displaystyle\frac{1}{n+1}\,{}_3F_2\!\left[\begin{array}{c}\tfrac12,\tfrac12,n+1\\1,n+2\end{array};1\right]"
        r"$=\dfrac{\Gamma^2(n+1)}{\Gamma(n+2)}\sum_{k=0}^{n}\frac{(k!)^4}{(\tfrac12)_k(k+1)_{n-k+1}}$.",
    ),
    rec(
        "RN-P2-C10-Entry29c",
        r"If $n$ is any complex number, then "
        r"$\displaystyle{}_3F_2\!\left[\begin{array}{c}\tfrac12,\tfrac12,n+1\\1,n+2\end{array};1\right]"
        r"$=\dfrac{1}{\pi}\,{}_3F_2\!\left[\begin{array}{c}\tfrac12,1,n+\tfrac12\\\tfrac12,n+2\end{array};1\right]$.",
    ),
    rec(
        "RN-P2-C10-Entry29d",
        r"If $\operatorname{Re}n>-\tfrac12$, then "
        r"$\displaystyle{}_3F_2\!\left[\begin{array}{c}\tfrac12,1,n+\tfrac12\\\tfrac12,n+2\end{array};1\right]"
        r"$=\dfrac{\pi\Gamma(n+2)}{\Gamma(n+\tfrac12)}\,{}_3F_2\!\left[\begin{array}{c}\tfrac12,\tfrac12,-n\\1,\tfrac12\end{array};1\right]$.",
    ),
    rec(
        "RN-P2-C10-Entry29-Corollary01",
        r"If $G$ denotes Catalan's constant, "
        r"$\displaystyle G=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)^2}$, then "
        r"$\displaystyle\frac12\,{}_3F_2\!\left[\begin{array}{c}\tfrac12,\tfrac12,\tfrac12\\1,\tfrac12\end{array};1\right]=2G$.",
    ),
    rec(
        "RN-P2-C10-Entry29-Corollary02",
        r"As $n\to\infty$, "
        r"$\displaystyle\pi\,{}_3F_2\!\left[\begin{array}{c}\tfrac12,\tfrac12,n\\1,n+1\end{array};1\right]"
        r"$\displaystyle\sim\log n+4\log 2+\gamma_E$.",
    ),
    rec(
        "RN-P2-C10-Entry30",
        r"If $\operatorname{Re}n>-\operatorname{Re}x$ and $-\operatorname{Re}y$, then "
        r"$\displaystyle{}_3F_2\!\left[\begin{array}{c}-x,1,y+n\\n,y+n+1\end{array};1\right]"
        r"$=\dfrac{y+n}{x+n}\,{}_3F_2\!\left[\begin{array}{c}-y,1,x+n\\n,x+n+1\end{array};1\right]$.",
    ),
    rec(
        "RN-P2-C10-Entry31",
        r"If $\operatorname{Re}(x+y+z+n+1)>0$ and $\operatorname{Re}(2x+2y+2z+2u+3n+4)>0$, then "
        r"$\displaystyle{}_6F_5\!\left[\begin{array}{c}\tfrac12n+1,n,-x,-y,-z,-u\\"
        r"\tfrac12n,x+n+1,y+n+1,z+n+1,u+n+1\end{array};1\right]"
        r"$=\displaystyle\frac{\Gamma(x+n+1)\Gamma(y+n+1)}{\Gamma(n+1)\Gamma(x+y+n+1)}"
        r"$\displaystyle\times{}_3F_2\!\left[\begin{array}{c}-x,-y,z+u+n+1\\z+n+1,u+n+1\end{array};1\right]$.",
    ),
    rec(
        "RN-P2-C10-Entry32",
        r"If $x+y+z=0$ and $x$ is a positive integer, then "
        r"$\displaystyle{}_3F_2\!\left[\begin{array}{c}n,-x,-y\\n+1,z\end{array};1\right]"
        r"$=\displaystyle\frac{\Gamma(n+1)\Gamma(x+1)}{\Gamma(n+x+1)}\sum_{k=0}^{x}\frac{(n)_k(y+z)_k}{(z)_k k!}$.",
    ),
    rec(
        "RN-P2-C10-Entry33",
        r"If $x+y+z=0$ and $x+y+n$ is a positive integer, then "
        r"$\displaystyle{}_3F_2\!\left[\begin{array}{c}n,-x,-y\\n+1,z\end{array};1\right]"
        r"$=\displaystyle\frac{\Gamma(n+1)\Gamma(x+y+n+1)}{\Gamma(x+n+1)\Gamma(y+n+1)}"
        r"$\displaystyle\times\sum_{k=0}^{x+y+n}\frac{(-x)_k(-y)_k}{(z)_k k!}$.",
    ),
    rec(
        "RN-P2-C10-Entry34",
        r"If $x$ and $y$ are arbitrary, then "
        r"$\displaystyle{}_2F_1\!\left(x,y;2(x+y+1);\tfrac12\right)"
        r"$=\dfrac{\sqrt{\pi}\,\Gamma(x+y+\tfrac32)}{\Gamma(x+1)\Gamma(y+1)}$.",
    ),
    rec(
        "RN-P2-C10-Entry35i",
        r"Let $\varphi(n)$ be defined by (35.1). Then as $n\to\infty$, "
        r"$\displaystyle n\varphi\!\left(\frac{n+1}{4}\right)\sim\psi\!\left(\frac{n+1}{2}\right)+3\log 2+\gamma_E"
        r"+\frac{3}{4n}-\frac{99}{32n^2}+\frac{999}{32n^4}+\cdots$.",
    ),
    rec(
        "RN-P2-C10-Entry35ii",
        r"Let $\varphi(n)$ be defined by (35.1). Then for each nonnegative integer $n$, "
        r"$\displaystyle\frac{n^2}{4}\varphi\!\left(n+\tfrac12\right)=\sum_{k=0}^{n-1}\binom{n}{k}^2+2G$, "
        r"where $G$ is Catalan's constant.",
    ),
    rec(
        "RN-P2-C10-Entry35iii",
        r"Let $\varphi(n)$ be defined by (35.1). Then for each nonnegative integer $n$, "
        r"$\displaystyle\varphi\!\left(n+\tfrac14\right)=1+\frac{16}{\pi^3}\sum_{k=0}^{n}\binom{2k+1}{k}^2\frac{1}{4^k}$.",
    ),
    rec(
        "RN-P2-C10-Entry35iv",
        r"If $\varphi(n)$ is defined by (35.1), then $\varphi(\tfrac12)=2G$ and $\varphi(\tfrac14)=\dfrac{\pi}{2}$.",
    ),
]
