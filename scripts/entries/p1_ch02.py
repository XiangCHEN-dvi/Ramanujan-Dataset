"""Part I, Chapter 2 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C02 = ["harmonic-series-and-arctan"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C02}


CHAPTER_2 = [
    rec(
        "RN-P1-C02-Entry01",
        r"For each positive integer $n$, $\displaystyle\sum_{k=1}^{n}\frac{1}{n+k}=\frac{1}{2n+1}+\sum_{k=1}^{n}\frac{1}{(2k)^3-2k}=\varphi(2,n)$, "
        r"where $\displaystyle\varphi(a,n)=1+2\sum_{k=1}^{n}\frac{1}{(ak)^3-ak}$ and $\varphi(a)=\lim_{n\to\infty}\varphi(a,n)$.",
    ),
    rec(
        "RN-P1-C02-Entry01-Corollary",
        r"$\log 2=\varphi(2)$.",
    ),
    rec(
        "RN-P1-C02-Entry01-Example",
        r"For each positive integer $n$, $\displaystyle\sum_{k=1}^{n}\frac{n-k}{n+k}=2n\sum_{k=1}^{n}\frac{1}{(2k-1)2k(2k+1)}+\frac{n}{2n+1}$.",
    ),
    rec(
        "RN-P1-C02-Entry02",
        r"For each positive integer $n$, $\displaystyle\sum_{k=1}^{2n+1}\frac{1}{n+k}=\varphi(3,n)$.",
    ),
    rec(
        "RN-P1-C02-Entry02-Corollary",
        r"$\log 3=\varphi(3)$.",
    ),
    rec(
        "RN-P1-C02-Entry03",
        r"For each positive integer $n$, "
        r"$\displaystyle\sum_{k=1}^{n}\left[\arctan\frac{1}{3k-1}+\arctan\frac{1}{3k}+\arctan\frac{1}{3k+1}-\arctan\frac{1}{k}\right]"
        r"$=\arctan\dfrac{10n}{9n^2+12}$.",
    ),
    rec(
        "RN-P1-C02-Entry04",
        r"For each positive integer $n$, "
        r"$\displaystyle\sum_{k=1}^{n}\frac{1}{n+k}+\sum_{k=0}^{n}\frac{1}{2n+2k+1}=\varphi(4,n)"
        r"$=\displaystyle\sum_{k=1}^{4n+1}\frac{(-1)^{k+1}}{k}+\frac12\sum_{k=1}^{2n}\frac{(-1)^{k+1}}{k}$.",
    ),
    rec(
        "RN-P1-C02-Entry04-Corollary",
        r"$\tfrac12\log 2=\varphi(4)$.",
    ),
    rec(
        "RN-P1-C02-Entry05",
        r"For each positive integer $n$, $\displaystyle\varphi(6,n)=\frac{2}{3}\sum_{k=1}^{n}\frac{1}{n+k}+\sum_{k=0}^{n}\frac{1}{2n+2k+1}$.",
    ),
    rec(
        "RN-P1-C02-Entry05-Corollary",
        r"$\tfrac12\log 3+\tfrac14\log 4=\varphi(6)$.",
    ),
    rec(
        "RN-P1-C02-Entry05-Example01",
        r"$\displaystyle\log 2=\sum_{k=1}^{\infty}\frac{1}{2(2k-1)^3-2(2k-1)}$.",
    ),
    rec(
        "RN-P1-C02-Entry05-Example02",
        r"$\displaystyle\log 2=1+\sum_{k=1}^{\infty}\frac{2(-1)^k}{(2k)^3-2k}$.",
    ),
    rec(
        "RN-P1-C02-Entry05-Example03",
        r"For each positive integer $n$, $2\varphi(4,n)=\varphi(2,2n)+\tfrac12\varphi(2,n)+\dfrac{1}{(4n+1)(4n+2)}$.",
    ),
    rec(
        "RN-P1-C02-Entry05-Example04",
        r"For each positive integer $n$, $\displaystyle\varphi(4,n)=\frac12\sum_{k=n+1}^{2n}\frac{1}{k}+\sum_{k=2n+1}^{4n+1}\frac{1}{k}$.",
    ),
    rec(
        "RN-P1-C02-Entry05-Example05",
        r"$\displaystyle\tfrac14\log 3-\tfrac13\log 2=\sum_{k=1}^{\infty}\frac{1}{3(2k-1)^3-3(2k-1)}$.",
    ),
    rec(
        "RN-P1-C02-Entry05-Example06",
        r"$\displaystyle\tfrac12\log 4+\tfrac16\log 3=\sum_{k=1}^{\infty}\frac{2}{(3k-1)^3-(3k-1)}$.",
    ),
    rec(
        "RN-P1-C02-Entry05-Example07",
        r"For each positive integer $n$, $2\varphi(6,n)+\tfrac13\varphi(2,n)=\varphi(3,n)+\varphi(2,3n)+\dfrac{36n^2+30n+8}{(6n+1)(6n+2)(6n+3)}$.",
    ),
    rec(
        "RN-P1-C02-Entry05-Example08",
        r"$\displaystyle\sum_{k=2}^{5}\arctan\frac{1}{k}=\frac{\pi}{4}+2\arctan\frac{1}{3}+\arctan\frac{1}{9}+\arctan\frac{1}{27}+\arctan\frac{1}{75}$ "
        r"(obtained by applying Entry 3 with $n=1$ and $n=4$).",
    ),
    rec(
        "RN-P1-C02-Entry05-Example09",
        r"For each positive integer $n$, "
        r"$2\displaystyle\sum_{k=1}^{n}\arctan\frac{n}{k}=\arctan n+\sum_{k=1}^{n}\arctan\frac{1}{8k^4+22k^2+1}"
        r"$+2\displaystyle\sum_{k=1}^{n}\arctan\frac{1}{k(4k^2+3)}$.",
    ),
    rec(
        "RN-P1-C02-Entry05-Example10",
        r"For each positive integer $n$, "
        r"$\displaystyle\sum_{k=1}^{n}\arctan\frac{1}{n+k}+\sum_{k=0}^{n}\arctan\frac{1}{2n+2k+1}=\frac{\pi}{4}"
        r"$+\displaystyle\sum_{k=1}^{n}\arctan\frac{1}{32k^4+96k^2-1}+\sum_{k=1}^{n}\arctan\frac{1}{128k^4+576k^2+1}$.",
    ),
    rec(
        "RN-P1-C02-Entry06",
        r"Let $k$ and $n$ be nonnegative integers and define $A_k=3^k(n+\tfrac13)-\tfrac13$, with $A_{-1}=0$. "
        r"If $r$ is a positive integer, then "
        r"$\displaystyle\sum_{j=n+1}^{A_r}\frac{1}{j}=r+2\sum_{k=0}^{r-1}(r-k)\sum_{j=A_{k-1}+1}^{A_k}\frac{1}{(3j)^3-3j}$.",
    ),
    rec(
        "RN-P1-C02-Entry06-Corollary",
        r"For each positive integer $r$, with $A_k=\dfrac{3^k-1}{2}$, "
        r"$\displaystyle\sum_{k=1}^{(3^r-1)/2}\frac{1}{k}=r+2\sum_{k=1}^{r-1}(r-k)\sum_{j=A_{k-1}+1}^{A_k}\frac{1}{(3j)^3-3j}$.",
    ),
    rec(
        "RN-P1-C02-Entry06-Example01",
        r"$\displaystyle\sum_{k=1}^{13}\frac{1}{k}=3+\frac{1}{3^3-3}+\frac12\left(\frac{1}{6^3-6}+\frac{1}{9^3-9}+\frac{1}{12^3-12}\right)$.",
    ),
    rec(
        "RN-P1-C02-Entry06-Example02",
        r"Let $H=\sum_{k=1}^{1000}\dfrac{1}{k}$. Ramanujan asserts that $H$ equals $7$ very nearly.",
    ),
    rec(
        "RN-P1-C02-Entry07",
        r"Let $n>0$ and let $r$ be a natural number. Then "
        r"$\displaystyle\sum_{k=0}^{r-1}\arctan\frac{2}{(n+2k+1)^2}=\arctan\frac{2r}{n^2+2nr+1}$.",
    ),
    rec(
        "RN-P1-C02-Entry07-Corollary",
        r"For $n>0$, $\displaystyle\sum_{k=0}^{\infty}\arctan\frac{2}{(n+2k+1)^2}=\arctan\frac{1}{n}$.",
    ),
    rec(
        "RN-P1-C02-Entry07-Example01",
        r"For $n>0$, $\displaystyle\sum_{k=1}^{\infty}\arctan\frac{2}{(n+k)^2}=\arctan\frac{2n+1}{n^2+n}+\rho(n)$, "
        r"where $\rho(n)=n$ if $n<(\sqrt5-1)/2$ and $\rho(n)=0$ otherwise.",
    ),
    rec(
        "RN-P1-C02-Entry07-Example02",
        r"For $n>0$, $\displaystyle\sum_{k=1}^{\infty}(-1)^{k+1}\arctan\frac{2}{(n+k)^2}=\arctan\frac{1}{n^2+n+1}$.",
    ),
    rec(
        "RN-P1-C02-Entry07-Example03",
        r"For $n>0$, $\displaystyle\sum_{k=1}^{\infty}\arctan\frac{2}{(2n+k)^2}=\arctan\frac{1}{n+1}$.",
    ),
    rec(
        "RN-P1-C02-Entry07-Example04",
        r"$\displaystyle\sum_{k=1}^{\infty}\arctan\frac{2}{k^2}=\frac{\pi}{2}$.",
    ),
    rec(
        "RN-P1-C02-Entry07-Example05",
        r"$\displaystyle\sum_{k=1}^{\infty}\arctan\frac{1}{2k^2}=\frac{\pi}{4}=\sum_{k=1}^{\infty}(-1)^{k-1}\arctan\frac{1}{k^2}$.",
    ),
    rec(
        "RN-P1-C02-Entry07-Example06",
        r"$\displaystyle\sum_{k=1}^{\infty}\arctan\frac{1}{(1+k)^2}=\frac{\pi}{8}$.",
    ),
    rec(
        "RN-P1-C02-Entry07-Example07",
        r"$\displaystyle\sum_{k=1}^{\infty}\arctan\frac{1}{(2k-1+\sqrt2)^2}=\frac{\pi}{4}$.",
    ),
    rec(
        "RN-P1-C02-Entry07-Example08",
        r"$\displaystyle\sum_{k=0}^{\infty}(-1)^k\arctan\frac{1}{(2k+1)^2}=\frac{\pi}{4}$.",
    ),
    rec(
        "RN-P1-C02-Entry08",
        r"Let $f$ be an entire function with zeros $z_1,z_2,\ldots$ such that $\sum_{k=1}^{\infty}1/|z_k|$ converges. "
        r"Then $f(z)=e^{a+bz}z^m\prod_{k=1}^{\infty}(1-z/z_k)\,e^{z/z_k}$, a special case of the Hadamard factorization theorem.",
    ),
    rec(
        "RN-P1-C02-Entry09i",
        r"$\displaystyle\sin x=x\prod_{k=1}^{\infty}\left(1-\frac{x^2}{(k\pi)^2}\right)$.",
    ),
    rec(
        "RN-P1-C02-Entry09ii",
        r"$\displaystyle\cos x=\prod_{k=1}^{\infty}\left(1-\frac{x^2}{(k-\tfrac12)^2\pi^2}\right)$.",
    ),
    rec(
        "RN-P1-C02-Entry09-Corollary01",
        r"$\displaystyle\sinh x=x\prod_{k=1}^{\infty}\left(1+\frac{x^2}{(k\pi)^2}\right)$.",
    ),
    rec(
        "RN-P1-C02-Entry09-Corollary02",
        r"$\displaystyle\cosh x=\prod_{k=1}^{\infty}\left(1+\frac{x^2}{(k-\tfrac12)^2\pi^2}\right)$.",
    ),
    rec(
        "RN-P1-C02-Entry09-Corollary03",
        r"For each complex $x$, $\displaystyle\cos\frac{x}{4}+\sin\frac{x}{4}=\prod_{k=0}^{\infty}\left(1+\frac{(-1)^k x}{(2k+1)\pi}\right)$.",
    ),
    rec(
        "RN-P1-C02-Entry09-Corollary04",
        r"Let $x$ and $a$ be complex with $a$ not an integral multiple of $\pi$. Then "
        r"$\displaystyle\frac{\sin(x+a)}{\sin a}=e^{x\cot a}\prod_{k=1}^{\infty}\left(1-\frac{x}{k\pi-a}\right)\left(1+\frac{x}{k\pi+a}\right)$.",
    ),
    rec(
        "RN-P1-C02-Entry09-Example01",
        r"Let $x$ and $a$ be complex with $a$ not an odd multiple of $\pi/2$. Then "
        r"$\displaystyle\frac{\cos(x+a)}{\cos a}=\prod_{k=1}^{\infty}\left(1-\frac{x}{(k-\tfrac12)\pi-a}\right)\left(1+\frac{x}{(k-\tfrac12)\pi+a}\right)$.",
    ),
    rec(
        "RN-P1-C02-Entry09-Example02",
        r"Let $x$ and $a$ be complex with $a$ not an integral multiple of $\pi$. Then "
        r"$\displaystyle 1+\frac{x}{a}+\frac{\sin x}{\sin a}=e^{x\cot a}\prod_{k=1}^{\infty}\left(1-\frac{x}{2k\pi-a}\right)\left(1+\frac{x}{2k\pi+a}\right)"
        r"$\times\prod_{k=1}^{\infty}\left(1-\frac{x}{(2k-1)\pi+a}\right)\left(1+\frac{x}{(2k-1)\pi-a}\right)$.",
    ),
    rec(
        "RN-P1-C02-Entry10",
        r"The partial fraction expansions: "
        r"$\displaystyle\cot x=\frac{1}{x}+\sum_{k=1}^{\infty}\frac{2x}{x^2-(k\pi)^2}$, "
        r"$\displaystyle\tan x=\sum_{k=1}^{\infty}\left(\frac{1}{x-(k-\tfrac12)\pi}-\frac{1}{x+(k-\tfrac12)\pi}\right)$, "
        r"$\displaystyle\csc x=\frac{1}{x}+\sum_{k=1}^{\infty}\frac{(-1)^k 2x}{x^2-(k\pi)^2}$, "
        r"$\displaystyle\sec x=\sum_{k=1}^{\infty}\frac{(-1)^{k-1}(2k-1)\pi}{x^2-((k-\tfrac12)\pi)^2}$.",
    ),
    rec(
        "RN-P1-C02-Entry11",
        r"Let $x$ and $a$ be real. Then "
        r"$\displaystyle\arctan\frac{x}{a}+\sum_{k=1}^{\infty}\left(\arctan\frac{x}{k\pi-a}-\arctan\frac{x}{k\pi+a}\right)=\arctan(\tanh x\cot a)$.",
    ),
    rec(
        "RN-P1-C02-Entry11-Corollary01",
        r"Let $x$ and $a$ be real. Then $\displaystyle\sum_{k=-\infty}^{\infty}(-1)^k\arctan\frac{x}{k\pi+a}=\arctan(\sinh x\csc a)$.",
    ),
    rec(
        "RN-P1-C02-Entry11-Corollary02",
        r"For real $x$, $\displaystyle\sum_{k=-\infty}^{\infty}\arctan\frac{x}{(k+\tfrac12)\pi}=\arctan(\sinh x)$.",
    ),
    rec(
        "RN-P1-C02-Entry11-Corollary03",
        r"For real $x$, $\displaystyle\sum_{k=-\infty}^{\infty}(-1)^k\arctan\frac{x}{(k+\tfrac12)\pi}=\arctan(\tanh x)$.",
    ),
    rec(
        "RN-P1-C02-Entry11-Example01",
        r"For real $x$ and $a$, "
        r"$\displaystyle\sum_{k=1}^{\infty}\left[\arctan\frac{x}{\tfrac12(2k-1)\pi-a}-\arctan\frac{x}{\tfrac12(2k-1)\pi+a}\right]=\arctan(\tanh x\tan a)$.",
    ),
    rec(
        "RN-P1-C02-Entry11-Example02",
        r"For real $x$ and $a$, $\displaystyle\sum_{k=-\infty}^{\infty}(-1)^k\arctan\frac{x}{\tfrac12(2k-1)\pi+a}=\arctan(\sinh x\sec a)$.",
    ),
    rec(
        "RN-P1-C02-Entry11-Example03",
        r"$\displaystyle\prod_{k=1}^{\infty}\left(1+\frac{1}{k^3}\right)^{1/k}=\left(\cosh\frac{\pi\sqrt3}{2}\right)^{2/3}$.",
    ),
    rec(
        "RN-P1-C02-Entry11-Example04",
        r"$\displaystyle\prod_{k=2}^{\infty}\left(1-\frac{1}{k^3}\right)^{1/k}=\left(\cosh\frac{\pi\sqrt3}{3n}\right)^{-2/3}$.",
    ),
    rec(
        "RN-P1-C02-Entry12",
        r"Let $P_k$ be defined by $\sum_{k=1}^{\infty}A_k z^k=1/\sum_{k=0}^{\infty}P_k z^k$ with $P_0=1$. "
        r"If $\lim_{n\to\infty}P_n/P_{n+1}=L$ exists and all roots of $\sum A_k z^k=0$ other than $z_0$ of smallest modulus satisfy $|z|>|L|$, "
        r"then $z_0=L$ is the root of smallest modulus.",
    ),
    rec(
        "RN-P1-C02-Entry12-Example01",
        r"For $x+x^2=1$, Ramanujan gives convergents to the root of smallest modulus $(\sqrt5-1)/2$.",
    ),
    rec(
        "RN-P1-C02-Entry12-Example02",
        r"For $x+x^2+x^3=1$, Ramanujan gives convergents to the real root of smallest modulus.",
    ),
    rec(
        "RN-P1-C02-Entry12-Example03",
        r"For $x+x^3=1$, Ramanujan gives convergents to the real root of smallest modulus.",
    ),
    rec(
        "RN-P1-C02-Entry12-Example04",
        r"For $2x+x^2+x^3=1$, Ramanujan gives convergents to the real root of smallest modulus.",
    ),
    rec(
        "RN-P1-C02-Entry12-Example05",
        r"For $e^x=2$, Ramanujan gives convergents to $\log 2$.",
    ),
    rec(
        "RN-P1-C02-Entry12-Example06",
        r"For $e^{-x}=x$, Ramanujan gives convergents to the positive root.",
    ),
]


