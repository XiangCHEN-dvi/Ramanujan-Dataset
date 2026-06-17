"""Part 4, Chapter 31 entries — curated LaTeX."""

from __future__ import annotations

TOPICS = ['elementary-and-miscellaneous-analysis']


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS}


CHAPTER_31 = [

    rec(
        "RN-P4-C31-Entry01",
        r"For $x>0$, $\displaystyle\sum_{n=1}^\infty\frac{(-1)^{n-1}(2n-x)}{3(n+x)}=\sum_{n=1}^\infty\frac{(-1)^{n-1}}{1+x/n}=\sum_{n=1}^\infty\frac{(-1)^{n-1}(2n-x)}{(2n-x)^2+3x^2}$.",
    )
,
    rec(
        "RN-P4-C31-Entry02",
        r"If $\sum u_n$ and $\sum v_n$ diverge while $\sum(u_n-v_n)$ converges, then $u_n$ and $v_n$, and also $1/u_n$ and $1/v_n$, are \"nearly equal\" for large $n$.",
    )
,
    rec(
        "RN-P4-C31-Entry03",
        r"If $\displaystyle\psi'(p)=\sum_{n=1}^\infty\mu(n)\psi(np)$, then $\displaystyle\varphi(p)=\sum_{n=1}^\infty\mu(n)\varphi(np)$, where $\mu(n)$ is the Möbius function.",
    )
,
    rec(
        "RN-P4-C31-Entry04",
        r"If $\displaystyle\sum_{n=1}^\infty(-1)^{n-1}\psi(np)=\sum_{n=1}^\infty\varphi'(np)$, then $\displaystyle\varphi(p)=\sum_{n=0}^\infty2\varphi(2^np)$.",
    )
,
    rec(
        "RN-P4-C31-Entry05",
        r"Let $f(x)$ be strictly increasing with continuous derivative on $(-\infty,\infty)$. If $\displaystyle\varphi(x)=f'(x)\varphi(f(x))$, then $\displaystyle\int_{f^{-1}(a)}^{f^{-1}(a+1)}\varphi(x)\,dx$ is constant for all real $a$.",
    )
,
    rec(
        "RN-P4-C31-Entry06",
        r"With $\varphi$ as in Entry 5 and $C$ the constant integral, for integers $m,n$, $\displaystyle\int_{f^m(x)}^{f^n(x)}\varphi(t)\,dt=(m-n)C$.",
    )
,
    rec(
        "RN-P4-C31-Entry07",
        r"Under the hypotheses of Entries 5–6, if $f(x)\to\infty$ as $x\to\infty$ and $\varphi(x_0)=0$, then the order of $\displaystyle\int_{x_0}^{f^n(x)}\varphi(t)\,dt$ is less than that of $f^n(x)$.",
    )
,
    rec(
        "RN-P4-C31-Entry08",
        r"Let $\varphi$ be continuous and strictly increasing. Define $\psi_0(x)=x$ and $\displaystyle\psi_n(x)=\varphi(x)\int_{x_0}^x\psi_{n-1}(t)\,dt$. Then $\displaystyle\psi_n^{(k)}(0)=\psi_{n-k}(x_0)$ for $0\le k\le n$.",
    )
,
    rec(
        "RN-P4-C31-Entry09",
        r"With notation as in Entry 8, if $\varphi$ is strictly increasing and continuous, then $\displaystyle P_n(v)=\psi_n(\varphi^{-1}(v))$ satisfies $P_n'(v)=\psi_{n-1}(\varphi^{-1}(v))$ and $P_n'(0)=\psi_{n-1}(x_0)$.",
    )
,
    rec(
        "RN-P4-C31-Entry10",
        r"If $\varphi(x)$ has simple zeros at $a,b,c,\ldots$, then $\displaystyle\frac{1}{\varphi(x)}-\sum\frac{1}{(x-a)\varphi'(a)}-\sum\frac{1}{(x-b)\varphi'(b)}-\cdots$ converges for all $x$ (Ramanujan's Mittag-Leffler-type expansion).",
    )
,
    rec(
        "RN-P4-C31-Entry11",
        r"If $\varphi(x)$ has simple zeros at $a,b,c,\ldots$, then the coefficient of $x^{n-1}$ in the expansion of $1/\varphi(x)$ equals $\displaystyle\sum\frac{1}{a^{n}\varphi'(a)}+\sum\frac{1}{b^{n}\varphi'(b)}+\cdots+o(1)$.",
    )
,
    rec(
        "RN-P4-C31-Entry12",
        r"If $\displaystyle\varphi(x)=\sum_{n=0}^\infty a_n x^n$ with $a_n>0$ for large $n$, $\lim a_n/a_{n+1}$ exists, and $R$ is the radius of convergence, then $\displaystyle\lim_{n\to\infty}\varphi\!\left(\frac{R}{n+1}\right)=\infty$.",
    )
,
    rec(
        "RN-P4-C31-Entry13",
        r"If $\varphi(x)=\infty$ at $a,b,c,\ldots$ and $|a|$ is the singularity nearest $0$, then (1) the Taylor series of $\varphi$ converges for $|x|<|a|$ and diverges for $|x|>|a|$; (2) $\displaystyle\lim_{n\to\infty}\frac{a^n}{n}\times\{\text{coefficient of }x^{n-1}\text{ in }1/\varphi(x)\}=\varphi'(a)/(\varphi(a))^2$.",
    )
,
    rec(
        "RN-P4-C31-Entry14",
        r"Let $f,g$ be given, $a_n,b_n$ constants, and $F$ satisfy $\displaystyle\sum_{n=1}^\infty a_n F(x+b_n)=\int f(t)g(t)\,dt$. Then $\displaystyle F(x)=\int f(t)g(t-x)\,dt$ is a formal solution.",
    )
,
    rec(
        "RN-P4-C31-Entry15",
        r"For a convergent sequence $\{a_n\}$, $\displaystyle\sum_{n=1}^\infty(a_n-a_{n+1})=a_1-\lim_{n\to\infty}a_n$ (telescoping series).",
    )
,
    rec(
        "RN-P4-C31-Entry16",
        r"$\displaystyle\sum_{n=1}^\infty(a_n-a_{n+1}+1-b_n)=\lim_{n\to\infty}\left(\sum_{k=1}^n a_k+b_1-b_n\right)$ when the limit exists.",
    )
,
    rec(
        "RN-P4-C31-Entry17",
        r"For an alternating series $\sum(-1)^{n-1}a_n$ with $a_n>0$, if positive terms are grouped as $u_1+\cdots+u_{\varphi(1)}$, $u_{\varphi(1)+1}+\cdots+u_{\varphi(1)+\varphi(2)}$, etc., then the partial sum is increased by $\displaystyle\frac12\int_{n/2}^n a_x\,dx+o(1)$ as $n\to\infty$.",
    )
,
    rec(
        "RN-P4-C31-Entry18",
        r"$\lim_{n\to\infty}u_n=c$ means $u_n-c$ cannot exceed any positive $\varepsilon$ when $n$ is sufficiently large.",
    )
,
    rec(
        "RN-P4-C31-Entry19",
        r"A function $\varphi(x)$ is a legitimate convergent series if $\displaystyle\varphi(x)=\lim_{n\to\infty}\sum_{k=1}^n h_k(x)$ for some sequence $\{h_k(x)\}$.",
    )
,
    rec(
        "RN-P4-C31-Entry20",
        r"Query: if $\displaystyle\int_0^\infty a_n e^{-n^2 x^2}\,dn$ is finite as $x\to0$, what Tauberian conclusion follows?",
    )
,
    rec(
        "RN-P4-C31-Entry21",
        r"Query: if $\displaystyle\int_0^\infty a_n e^{-n^2/x^2}\,dn$ is finite as $x\to0$, what Tauberian conclusion follows?",
    )
,
    rec(
        "RN-P4-C31-Entry22",
        r"If $\displaystyle\int_0^\infty a_n e^{-n^2 x^2}\,dn$ is finite as $x\to0^+$, then the average value of $a_n$ is $\displaystyle\lim_{z\to\infty}z\int_0^\infty e^{-n^2/z^2}\,dn=\frac{\sqrt{\pi}}{2\,\Gamma(\tfrac32)}$ (with Ramanujan's $\Gamma(r)$ corrected to $\Gamma(r+1)$).",
    )
,
    rec(
        "RN-P4-C31-Entry23",
        r"If $\{a_n\}$ converges to $a\ne0$ with $a_n\ne0$ for $n>1$, then $\displaystyle\prod_{n=1}^\infty\frac{a_n}{a_{n+1}}=a_1/a$ (telescoping product).",
    )
,
    rec(
        "RN-P4-C31-Entry24",
        r"If $x$ is real and $x/2^k$ is not an odd multiple of $\pi/2$ for $k\ge1$, then $\displaystyle\sum_{k=1}^\infty\frac{\tan(x/2^k)}{2^k}=\cot x-\frac{1}{x}$.",
    )
,
    rec(
        "RN-P4-C31-Entry25",
        r"For every real $x$, $\displaystyle\sum_{k=1}^\infty\frac{\sin(x/3^k)}{3^k(1+2\cos(x/3^k))}=\frac{x}{2}$.",
    )
,
    rec(
        "RN-P4-C31-Entry26",
        r"For every real $x$, $\displaystyle\sum_{k=0}^\infty\frac{\sin^2(3^k x)}{3^k}=\frac{x}{4}$.",
    )
,
    rec(
        "RN-P4-C31-Entry11ii",
        r"If $x$ is real and $x/2^k$ ($k>0$) is not an integral multiple of $\pi$, then $\displaystyle\sum_{k=0}^\infty\left(\csc\frac{x}{2^k}-\frac{2^k}{x}\right)=\cot x-\frac{1}{x}$.",
    )
,
    rec(
        "RN-P4-C31-Entry28",
        r"If $x$ is real and $x/2^k$ ($k>0$) is not a multiple of $\pi/2$, then $\displaystyle\prod_{k=0}^\infty\left(\frac{2^{2^k}\sin^2(x/2^k)}{\sin(x/2^{k-1})}\right)^{1/2^k}=\frac{2x}{\sin(2x)}$.",
    )
,
    rec(
        "RN-P4-C31-Entry29",
        r"For $x>0$, $\displaystyle\frac{1}{1-x}-\frac{1}{\log x}=\sum_{k=1}^\infty\frac{1}{2^k(1+x^{1/2^k})}$.",
    )
,
    rec(
        "RN-P4-C31-Entry30",
        r"For $x>0$, $\displaystyle\frac{1}{1-x}+\frac{1}{\log x}=\sum_{k=1}^\infty\frac{2+x^{1/2^k}}{3^k(1+x^{1/3^k}+x^{2/3^k})}$.",
    )
]
