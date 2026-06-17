"""Part 4, Chapter 29 entries — curated LaTeX."""

from __future__ import annotations

TOPICS = ['special-functions']


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS}


CHAPTER_29 = [

    rec(
        "RN-P4-C29-Entry01",
        r"For $n>0$ and real $x$, Binet's formula gives $\log\Gamma(n+xi)+\log\Gamma(n-xi)=(n+\tfrac12)\log(n^2+x^2)-2nx\arctan(x/n)-n+x\arctan(x/n)+\log\Gamma(n+1)$.",
    )
,
    rec(
        "RN-P4-C29-Entry02",
        r"$\displaystyle\arctan\!\left(\frac{x}{n+1}\right)=\frac{\pi}{2}-\frac{x\,\Gamma(n+xi+1)\Gamma(n-xi+1)}{n\,\Gamma(n+1)^2}$.",
    )
,
    rec(
        "RN-P4-C29-Entry03",
        r"$\displaystyle\varphi(m,n)=\frac{\Gamma(m+1)\Gamma(n+1)\{\cosh(\pi(m+n)\sqrt3)-\cos(\pi(m-n))\}}{\Gamma(2m+n+1)\Gamma(2n+m+1)\,2n(m^2+mn+n^2)}$.",
    )
,
    rec(
        "RN-P4-C29-Entry04",
        r"$\displaystyle\sum_{m=1}^\infty\sum_{n=1}^\infty\frac{\varphi(m,n)}{m^2+n^2}=\frac{\pi}{2\sqrt3}\sum_{n=1}^\infty\frac{n\sinh(\pi n\sqrt3)}{(\cosh(\pi n\sqrt3)-\cos(\pi n))^2}$.",
    )
,
    rec(
        "RN-P4-C29-Entry05",
        r"As $n\to\infty$, $\displaystyle\log\prod_{m=1}^{n-1}\left(1+\frac{6m+4}{2m+1}\right)=\tfrac12\log(2\pi n)-\log(2\cosh(\pi n\sqrt3)-2\cos(\pi n))+\sum_{k=1}^\infty\frac{B_{2k}(2^{2k-1}-1)}{(2k)(2k-1)(n/2)^{2k-1}}+O(n^{-2k})$.",
    )
,
    rec(
        "RN-P4-C29-Entry06",
        r"As $n\to\infty$, $\displaystyle\log\prod_{m=1}^{n-1}\prod_{k=1}^{n-1}\left(1+\frac{6m+4k^2}{2m+2k-1}\right)=-\tfrac12\log2-\tfrac14\log2+n-\tfrac12 n\log n-2\log(2\pi n)+O(1)$ with a full Bernoulli-number correction series.",
    )
,
    rec(
        "RN-P4-C29-Entry07",
        r"As $x\to\infty$, if $\sum_{k=1}^m A_k=\sum_{k=1}^n B_k$ and $\prod A_k=\prod B_k$, then $\displaystyle\lim_{x\to\infty}\frac{\prod_{k=1}^m\Gamma(A_k x+a_k+1)}{\prod_{k=1}^n\Gamma(B_k x+b_k+1)}=(2\pi)^{(m-n)/2}x^{\sum a_k-\sum b_k}\,e^{\pi i(\sum a_k-\sum b_k)/2}$.",
    )
,
    rec(
        "RN-P4-C29-Entry08",
        r"Let $A_k>0$, $B_k>0$, and $a_k$ be complex with $\prod_{k=1}^m A_k=\prod_{k=1}^n B_k$ and $\sum_{k=1}^m a_k=\sum_{k=1}^n b_k$. Then $\displaystyle\lim_{x\to\infty}\frac{\prod_{k=1}^m\Gamma(A_k x+a_k+1)}{\prod_{k=1}^n\Gamma(B_k x+b_k+1)}=(2\pi)^{(m-n)/2}x^{\sum a_k-\sum b_k}\,e^{\pi i(\sum a_k-\sum b_k)/2}$.",
    )
,
    rec(
        "RN-P4-C29-Entry08-Corollary01",
        r"For arbitrary complex $a,b,c$, $\displaystyle\lim_{x\to\infty}\frac{\Gamma(x+a-b+1)\Gamma(8x+2b+1)\Gamma(9x+a+c)}{\Gamma(3x+a-c+1)\Gamma(3x+a-b+c+1)\Gamma(12x+3b+1)}=2^{a-b+c}$.",
    )
,
    rec(
        "RN-P4-C29-Entry08-Corollary02",
        r"For arbitrary complex $a,b,c$, $\displaystyle\lim_{x\to\infty}\frac{\Gamma(3x+a+1)\Gamma(3x+b+1)\Gamma(12x+3c+1)}{\Gamma(x+\tfrac12(a+b-c)+1)\Gamma(8x+2c+1)\Gamma(9x+\tfrac12(a+b+3c)+1)}=2^{a+b-c}$.",
    )
,
    rec(
        "RN-P4-C29-Entry09",
        r"For $z=x+iy$ with $x,y$ real, $\displaystyle\Gamma(z+1)=\Gamma(x+1)\exp\!\left\{\lim_{N\to\infty}\left(y\log N-\arctan\frac{y}{x+N}\right.-\sum_{k=1}^N\left(\log|x+iy+k|-\log k+\frac{iy}{x+k}\right)\right\}$.",
    )
,
    rec(
        "RN-P4-C29-Entry11",
        r"If $n$ is not an integer, then as $x\to\infty$, $\displaystyle\frac{I_n(2x)-I_{-n}(2x)}{\sin(n\pi)}\sim\frac{e^{2x}}{\sin(n\pi)\sqrt{4\pi x}}\sum_{k=0}^\infty\frac{\Gamma(n+k+\tfrac12)\Gamma(n-k+\tfrac12)}{k!\,(2x)^k\,(n^2-(k-\tfrac12)^2)\cdots(n^2-(k-\tfrac32)^2)}$.",
    )
,
    rec(
        "RN-P4-C29-Entry12",
        r"If $n$ is not an integer, $\displaystyle\frac{I_n(2x)-I_{-n}(2x)}{\sin(n\pi)}=-\frac{1}{\pi}\int_0^\pi e^{2x\cos\theta}\cos(n\theta)\,d\theta$.",
    )
,
    rec(
        "RN-P4-C29-Entry13",
        r"For arbitrary complex $n$, as $x\to\infty$, $\displaystyle I_n(2x)=\frac{e^{2x}}{\sqrt{4\pi x}}\sum_{k=0}^\infty\frac{\Gamma(n+k+\tfrac12)}{k!\,(2x)^k\,(n^2-(k-\tfrac12)^2)\cdots}$.",
    )
,
    rec(
        "RN-P4-C29-Entry14",
        r"Let $\varphi(x)$ be continuous on $[0,\infty)$, $p,a>0$, and $\Re(n)>0$. If $\displaystyle\int_0^\infty e^{-p\sqrt{x}}\varphi(x)\,dx=\frac{p^{n+1}}{(n+1)!}$, then $\displaystyle\varphi(x)=\frac{x^{(n-1)/2}e^{-2\sqrt{ap}}}{\Gamma(n)}I_n(2\sqrt{ax})$; as $a\to\infty$, $\varphi(x)\sim x^{(n-1)/2}(4ax)^{-n/2}e^{-2\sqrt{ax}}$.",
    )
,
    rec(
        "RN-P4-C29-Entry16",
        r"If $a$ is a positive integer, then $\displaystyle\sum_{n=0}^{a-1}\frac{(-a+1)_n(2n+1)}{(a+1)_n(z^2+(2n+1)^2)}=\frac{\pi\,\Gamma(a+1)\Gamma(a)}{4\Gamma(a+\tfrac12)^2}\,\frac{\Gamma(\tfrac12(a+iz))\Gamma(\tfrac12(a-iz))}{\Gamma(a+\tfrac12(a+iz))\Gamma(a+\tfrac12(a-iz))}$.",
    )
,
    rec(
        "RN-P4-C29-Entry16i",
        r"If $\Re(a)>0$, then $\displaystyle\sum_{n=0}^\infty\frac{(2n+1)(-a+1)_n}{(a+1)_n(z^2+(2n+1)^2)}=\frac{\pi\,\Gamma(a+1)\Gamma(a)\,\Gamma(\tfrac12(1+iz))\Gamma(\tfrac12(1-iz))}{4\,\Gamma(a+\tfrac12(1+iz))\Gamma(a+\tfrac12(1-iz))}$.",
    )
,
    rec(
        "RN-P4-C29-Entry17",
        r"Let $\Re(2x+2y+1)>0$ and $m,n\in\mathbb{C}$. Then $\displaystyle\frac{\Gamma(x+1)\Gamma(y+1)\Gamma(2x+2y+1)}{\Gamma(x+y+1)}=\sum_{k=1}^\infty\frac{(m+n)_k(m-n)_k}{(x+y+1+k)_k}\left\{\frac{\Gamma(x+1+mi)\Gamma(x+1-mi)}{\Gamma(y+1+ni)\Gamma(y+1-ni)}\right\}^{-1}$.",
    )
,
    rec(
        "RN-P4-C29-Entry18",
        r"For $0<x<1$, ${}_3F_2(1,\tfrac54,\tfrac32;1,1;4x(1-x))={}_2F_1(2,\tfrac12;1;x)$.",
    )
,
    rec(
        "RN-P4-C29-Entry19",
        r"With $L(q):=1-24\sum_{n=1}^\infty nq^n/(1-q^n)$ and $q$ the nome for modulus $x$, $\displaystyle\frac{d}{dx}L(q)=\sum_{n=0}^\infty\frac{(3n+1)(\tfrac13)_n(4x(1-x))^n}{(1-2x)(n!)^3}$.",
    )
,
    rec(
        "RN-P4-C29-Entry20i",
        r"$\displaystyle\frac{1}{\pi}=\frac{2\sqrt2}{9801}\sum_{n=0}^\infty\frac{(4n)!(1103+26390n)}{(n!)^4\,396^{4n}}$.",
    ),
    rec(
        "RN-P4-C29-Entry20ii",
        r"$\displaystyle\frac{1}{\pi}=\frac{2\sqrt2}{992}\sum_{n=0}^\infty\frac{(4n)!(42n+5)}{(n!)^4\,64^{n+1}}$.",
    ),
    rec(
        "RN-P4-C29-Entry20iii",
        r"$\displaystyle\frac{1}{\pi}=\frac{1}{426880\sqrt2}\sum_{n=0}^\infty\frac{(4n)!(42\sqrt2n+5\sqrt2+30n-(\sqrt2-1))}{(n!)^4\,64^n}$.",
    ),
    rec(
        "RN-P4-C29-Entry21i",
        r"$\displaystyle\frac{1}{\pi}=\frac{2\sqrt2}{9801}\sum_{n=0}^\infty\frac{(4n)!(1103+26390n)}{(n!)^4\,396^{4n}}$.",
    ),
    rec(
        "RN-P4-C29-Entry21ii",
        r"$\displaystyle\frac{1}{\pi}=\frac{1}{4\sqrt2}\sum_{n=0}^\infty\frac{(\tfrac14)_n(\tfrac12)_n(\tfrac34)_n}{(n!)^3}\frac{6n+1}{4^n}$.",
    ),
    rec(
        "RN-P4-C29-Entry21iii",
        r"$\displaystyle\frac{1}{\pi}=\frac{1}{15\sqrt3}\sum_{n=0}^\infty\frac{(\tfrac13)_n(\tfrac12)_n(\tfrac23)_n}{(n!)^3}\frac{33n+4}{125^n}$.",
    ),
    rec(
        "RN-P4-C29-Entry21iv",
        r"$\displaystyle\frac{1}{\pi}=\frac{1}{4\sqrt2}\sum_{n=0}^\infty\frac{(\tfrac14)_n(\tfrac12)_n(\tfrac34)_n}{(n!)^3}\frac{11n+1}{125^n}$.",
    ),
    rec(
        "RN-P4-C29-Entry21v",
        r"$\displaystyle\frac{1}{\pi}=\frac{1}{18\sqrt3}\sum_{n=0}^\infty\frac{(\tfrac13)_n(\tfrac12)_n(\tfrac23)_n}{(n!)^3}\frac{133n+8}{85^n}$.",
    ),
    rec(
        "RN-P4-C29-Entry21vi",
        r"$\displaystyle\frac{1}{\pi}=\frac{1}{4}\sum_{n=0}^\infty\frac{(\tfrac14)_n(\tfrac12)_n(\tfrac34)_n}{(n!)^3}\frac{(-1)^n(20n+3)}{3^{4n}}$.",
    ),
    rec(
        "RN-P4-C29-Entry21vii",
        r"$\displaystyle\frac{1}{\pi}=\frac{1}{4}\sum_{n=0}^\infty\frac{(\tfrac14)_n(\tfrac12)_n(\tfrac34)_n}{(n!)^3}\frac{(-1)^n(28n+3)}{3^{4n}}$.",
    ),
    rec(
        "RN-P4-C29-Entry21viii",
        r"$\displaystyle\frac{1}{\pi}=\frac{1}{4}\sum_{n=0}^\infty\frac{(\tfrac14)_n(\tfrac12)_n(\tfrac34)_n}{(n!)^3}\frac{(-1)^n(260n+23)}{18^{4n}}$.",
    ),
    rec(
        "RN-P4-C29-Entry21ix",
        r"$\displaystyle\frac{1}{\pi}=\frac{1}{4\sqrt5}\sum_{n=0}^\infty\frac{(\tfrac14)_n(\tfrac12)_n(\tfrac34)_n}{(n!)^3}\frac{(-1)^n(644n+41)}{5^{12n}}$.",
    ),
    rec(
        "RN-P4-C29-Entry21x",
        r"$\displaystyle\frac{1}{\pi}=\frac{1}{4\sqrt2}\sum_{n=0}^\infty\frac{(\tfrac14)_n(\tfrac12)_n(\tfrac34)_n}{(n!)^3}\frac{(-1)^n(21460n+1123)}{882^{4n}}$.",
    ),
    rec(
        "RN-P4-C29-Entry21xi",
        r"$\displaystyle\frac{1}{\pi}=\frac{1}{9}\sum_{n=0}^\infty\frac{(\tfrac13)_n(\tfrac12)_n(\tfrac23)_n}{(n!)^3}\frac{8n+1}{9^{3n}}$.",
    ),
    rec(
        "RN-P4-C29-Entry21xii",
        r"$\displaystyle\frac{1}{\pi}=\frac{1}{2\pi\sqrt2}\sum_{n=0}^\infty\frac{(\tfrac14)_n(\tfrac12)_n(\tfrac34)_n}{(n!)^3}\frac{10n+1}{9^{3n}}$.",
    ),
    rec(
        "RN-P4-C29-Entry21xiii",
        r"$\displaystyle\frac{1}{\pi}=\frac{1}{3\sqrt3}\sum_{n=0}^\infty\frac{(\tfrac13)_n(\tfrac12)_n(\tfrac23)_n}{(n!)^3}\frac{40n+3}{9^{3n}}$.",
    ),
    rec(
        "RN-P4-C29-Entry21xiv",
        r"$\displaystyle\frac{1}{\pi}=\frac{1}{2\pi\sqrt2}\sum_{n=0}^\infty\frac{(\tfrac14)_n(\tfrac12)_n(\tfrac34)_n}{(n!)^3}\frac{280n+19}{99^{4n}}$ and $\displaystyle\frac{1}{\pi}=\frac{1}{2\pi\sqrt2}\sum_{n=0}^\infty\frac{(\tfrac14)_n(\tfrac12)_n(\tfrac34)_n}{(n!)^3}\frac{26390n+1103}{99^{4n}}$.",
    ),
]
