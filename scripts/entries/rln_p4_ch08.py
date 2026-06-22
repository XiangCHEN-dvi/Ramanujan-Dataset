"""RLN Part 4, Chapter 8 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C08 = ["number-theory-lost-notebook"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C08}


CHAPTER_8 = [
    rec(
        "RLN-P4-C08-Entry8-1-1",
        r"$\varphi(x)$ is the number of numbers not exceeding $x$ whose number of prime divisors "
        r"does not exceed $k$. Then "
        r"$\varphi(x)\sim\dfrac{x}{\log x}\left\{1+\dfrac{\log\log x}{1!}"
        r"+\dfrac{(\log\log x)^2}{2!}+\cdots+\dfrac{(\log\log x)^{[k]}}{[k]!}\right\}$.",
    ),
    rec(
        "RLN-P4-C08-Entry8-2-1",
        r"Let $\varphi(x)$ denote the number of numbers of the form "
        r"$2^{a_2}3^{a_3}5^{a_5}\cdots p^{a_p}$, $p\le x^\epsilon$, not exceeding $x$. "
        r"For $\tfrac{1}{2}\le\epsilon\le1$, "
        r"$\varphi(x)\sim x\left\{1-\displaystyle\int_{1}^{1/\epsilon}\dfrac{du_0}{u_0}\right\}$; "
        r"for $\tfrac{1}{3}\le\epsilon\le\tfrac{1}{2}$, "
        r"$\varphi(x)\sim x\left\{1-\displaystyle\int_{1}^{1/\epsilon}\dfrac{du_0}{u_0}"
        r"+\displaystyle\int_{1/2}^{1/\epsilon}\dfrac{du_1}{u_1}"
        r"\displaystyle\int_{1-u_1}^{u_1}\dfrac{du_0}{u_0}\right\}$; "
        r"for $\tfrac{1}{4}\le\epsilon\le\tfrac{1}{3}$, "
        r"$\varphi(x)\sim x\left\{1-\displaystyle\int_{1}^{1/\epsilon}\dfrac{du_0}{u_0}"
        r"+\displaystyle\int_{1/2}^{1/\epsilon}\dfrac{du_1}{u_1}"
        r"\displaystyle\int_{1-u_1}^{u_1}\dfrac{du_0}{u_0}"
        r"-\displaystyle\int_{1/3}^{1/\epsilon}\dfrac{du_2}{u_2}"
        r"\displaystyle\int_{\frac{1}{2}(1-u_2)}^{u_2}\dfrac{du_1}{u_1}"
        r"\displaystyle\int_{1-u_1}^{u_1}\dfrac{du_0}{u_0}\right\}$; "
        r"and for $\tfrac{1}{5}\le\epsilon\le\tfrac{1}{4}$, "
        r"$\varphi(x)\sim x\left\{1-\displaystyle\int_{1}^{1/\epsilon}\dfrac{du_0}{u_0}"
        r"+\displaystyle\int_{1/2}^{1/\epsilon}\dfrac{du_1}{u_1}"
        r"\displaystyle\int_{1-u_1}^{u_1}\dfrac{du_0}{u_0}"
        r"-\displaystyle\int_{1/3}^{1/\epsilon}\dfrac{du_2}{u_2}"
        r"\displaystyle\int_{\frac{1}{2}(1-u_2)}^{u_2}\dfrac{du_1}{u_1}"
        r"\displaystyle\int_{1-u_1}^{u_1}\dfrac{du_0}{u_0}"
        r"+\displaystyle\int_{1/4}^{1/\epsilon}\dfrac{du_3}{u_3}"
        r"\displaystyle\int_{\frac{1}{3}(1-u_3)}^{u_3}\dfrac{du_2}{u_2}"
        r"\displaystyle\int_{\frac{1}{2}(1-u_2)}^{u_2}\dfrac{du_1}{u_1}"
        r"\displaystyle\int_{1-u_1}^{u_1}\dfrac{du_0}{u_0}\right\}$, and so on.",
    ),
    rec(
        "RLN-P4-C08-Entry8-3-1",
        r"Let $\alpha$ and $\beta$ be positive numbers such that $\alpha\beta=4\pi^3$. Then "
        r"$\displaystyle\sum_{n=1}^{\infty}\dfrac{1}{e^{n^2\alpha}-1}"
        r"=\dfrac{\pi^2}{6\alpha}+\dfrac{1}{4}+\dfrac{\sqrt{\beta}}{4\pi}\left\{\zeta\!\left(\tfrac{1}{2}\right)"
        r"+\displaystyle\sum_{n=1}^{\infty}"
        r"\dfrac{\cos(\sqrt{n\beta})-\sin(\sqrt{n\beta})-e^{-\sqrt{n\beta}}}"
        r"{\sqrt{n}\bigl(\cosh(\sqrt{n\beta})-\cos(\sqrt{n\beta})\bigr)}\right\}$.",
    ),
    rec(
        "RLN-P4-C08-Entry8-3-2",
        r"Let $\alpha$ and $\beta$ be positive numbers such that $\alpha\beta=4\pi^3$. If "
        r"$\varphi(n)$ and $\psi(n)$, $n\ge1$, are defined by "
        r"$\displaystyle\sum_{j=1}^{\infty}\dfrac{x^{j^2}}{1-x^{j^2}}"
        r"=\displaystyle\sum_{n=1}^{\infty}\varphi(n)x^n$ and "
        r"$\displaystyle\sum_{j=1}^{\infty}\dfrac{jx^{j^2}}{1-x^{j^2}}"
        r"=\displaystyle\sum_{n=1}^{\infty}\psi(n)x^n$, then "
        r"$\displaystyle\sum_{n=1}^{\infty}\varphi(n)e^{-n\alpha}"
        r"=\dfrac{\pi^2}{6\alpha}+\dfrac{1}{4}+\dfrac{\sqrt{\beta}}{2\pi}\left\{\tfrac{1}{2}\zeta\!\left(\tfrac{1}{2}\right)"
        r"+\displaystyle\sum_{n=1}^{\infty}\dfrac{\psi(n)}{\sqrt{n}}e^{-\sqrt{n\beta}}"
        r"\bigl[\cos(\sqrt{n\beta})-\sin(\sqrt{n\beta})\bigr]\right\}$.",
    ),
    rec(
        "RLN-P4-C08-Entry8-4-1",
        r"$x+(x-1)+(x-2)+\cdots=\tfrac{1}{2}x^2+\tfrac{1}{2}x+\begin{cases}+1/8\\ +0\end{cases}$; "
        r"$x^2+(x-1)^2+(x-2)^2+\cdots=\tfrac{1}{3}x^3+\tfrac{1}{2}x^2+\tfrac{1}{6}x"
        r"+\begin{cases}+1/(36\sqrt{3})\\ -1/(36\sqrt{3})\end{cases}$; "
        r"$x^3+(x-1)^3+(x-2)^3+\cdots=\tfrac{1}{4}x^4+\tfrac{1}{2}x^3+\tfrac{1}{4}x^2"
        r"+\begin{cases}+0\\ -1/64\end{cases}$; "
        r"$x^4+(x-1)^4+(x-2)^4+\cdots=\tfrac{1}{5}x^5+\tfrac{1}{2}x^4+\tfrac{1}{3}x^3-\tfrac{1}{30}x"
        r"+\begin{cases}+1/(900)\sqrt{15+4\sqrt{6/5}}\\ -1/(900)\sqrt{15+4\sqrt{6/5}}\end{cases}$; "
        r"$x^5+(x-1)^5+(x-2)^5+\cdots=\tfrac{1}{6}x^6+\tfrac{1}{2}x^5+\tfrac{5}{12}x^4-\tfrac{1}{12}x^2"
        r"+\begin{cases}+1/128\\ +0\end{cases}$; "
        r"$x^6+(x-1)^6+(x-2)^6+\cdots=\tfrac{1}{7}x^7+\tfrac{1}{2}x^6+\tfrac{1}{2}x^5-\tfrac{1}{6}x^3+\tfrac{1}{42}x"
        r"+\begin{cases}\pm 1/(2352)\sqrt{1813-(47+39\sqrt{2})/\!\bigl(21-7\sqrt{2}\bigr)-(47-39\sqrt{2})/\!\bigl(21+7\sqrt{2}\bigr)}\\ \mp\text{same}\end{cases}$; "
        r"$x^7+(x-1)^7+(x-2)^7+\cdots=\tfrac{1}{8}x^8+\tfrac{1}{2}x^7+\tfrac{7}{12}x^6-\tfrac{7}{24}x^4+\tfrac{1}{12}x^2"
        r"+\begin{cases}+0\\ -17/2048\end{cases}$.",
    ),
    rec(
        "RLN-P4-C08-Entry8-5-1",
        r"If "
        r"$\dfrac{1+53x+9x^2}{1-82x-82x^2+x^3}=\displaystyle\sum_{n=0}^{\infty}a_n x^n$, "
        r"$\dfrac{2-26x-12x^2}{1-82x-82x^2+x^3}=\displaystyle\sum_{n=0}^{\infty}b_n x^n$, "
        r"and $\dfrac{2+8x-10x^2}{1-82x-82x^2+x^3}=\displaystyle\sum_{n=0}^{\infty}c_n x^n$, "
        r"then $a_n^3+b_n^3=c_n^3+(-1)^n$.",
    ),
    rec(
        "RLN-P4-C08-Entry8-5-2",
        r"If "
        r"$\dfrac{1+53x+9x^2}{1-82x-82x^2+x^3}=\displaystyle\sum_{n=1}^{\infty}\alpha_{n-1}x^{-n}$, "
        r"$\dfrac{2-26x-12x^2}{1-82x-82x^2+x^3}=\displaystyle\sum_{n=1}^{\infty}\beta_{n-1}x^{-n}$, "
        r"and $\dfrac{2+8x-10x^2}{1-82x-82x^2+x^3}=\displaystyle\sum_{n=1}^{\infty}\gamma_{n-1}x^{-n}$, "
        r"then $\alpha_n^3+\beta_n^3=\gamma_n^3-(-1)^n$.",
    ),
    rec(
        "RLN-P4-C08-Entry8-5-3",
        r"$9^3+10^3=12^3+1$, $6^3+8^3=9^3-1$, $135^3+138^3=172^3-1$, "
        r"$11{,}161^3+11{,}468^3=14{,}258^3+1$, $791^3+812^3=1{,}010^3-1$, "
        r"and $65{,}601^3+67{,}402^3=83{,}802^3+1$.",
    ),
    rec(
        "RLN-P4-C08-Entry8-6-1",
        r"If $d(N!)$ is the number of divisors of $N!$, then "
        r"$\dfrac{C\sqrt{N}}{\log N}(1-\epsilon)<d(N!)<\dfrac{C\sqrt{N}}{\log N}(1+\epsilon)$, "
        r"where $C=\left(1+\dfrac{1}{1}\right)^{\!1+\frac{1}{2}\!\left(1+\frac{1}{3}\!\left(1+\frac{1}{4}\!\left(1+\frac{1}{5}\cdots\right)\right)\right)\!}$.",
    ),
    rec(
        "RLN-P4-C08-Entry8-7-1",
        r"If $S(N)$ is the number of ways in which $N$ can be expressed as the sum of two squares, "
        r"then the maximum order of $S(N)$ equals "
        r"$\sqrt{\text{max.\ order of }d(N^2+aN+b)}\cdot e^{O(\log N)^{1/2+\epsilon}}$.",
    ),
    rec(
        "RLN-P4-C08-Entry8-8-1",
        r"For each integer $k\ge2$, let "
        r"$R_{k,2}(x):=\displaystyle\sum_{\substack{m^k+n^k\le x\\ m,n\ge0}}1$, "
        r"where $m^k+n^k$ and $n^k+m^k$ are not counted as distinct. Then, as $x\to\infty$, "
        r"for each fixed $\epsilon>0$, "
        r"$R_{k,2}(x)=\dfrac{x^{2/k}}{4k}\,\dfrac{\{\Gamma(1/k)\}^2}{\Gamma(2/k)}+O\!\left(x^{1/k+\epsilon}\right)$.",
    ),
]
