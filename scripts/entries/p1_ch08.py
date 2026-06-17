"""Part I, Chapter 8 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C08 = ["gamma-function-analogues"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C08}


CHAPTER_8 = [
    rec(
        "RN-P1-C08-Entry02",
        r"As $x\to\infty$, "
        r"$\displaystyle\sum_{k=1}^x\frac{1}{k}\sim\log x+\gamma"
        r"-\sum_{k=1}^\infty\frac{B_{2k}}{2k\,x^{2k}}$, "
        r"where $\gamma$ denotes Euler's constant and $B_{2k}$ are Bernoulli numbers.",
    ),
    rec(
        "RN-P1-C08-Entry03",
        r"If $x$ is real, then "
        r"$\displaystyle\psi(x+1)+\gamma=\sum_{k=1}^\infty\left(\frac{1}{k}-\frac{1}{k+x}\right)$ "
        r"(3.1), "
        r"where $\psi(x)=\Gamma'(x)/\Gamma(x)$ and $\gamma$ denotes Euler's constant.",
    ),
    rec(
        "RN-P1-C08-Entry04",
        r"For $|x|<1$, "
        r"$\displaystyle\psi(x+1)+\gamma=\sum_{k=1}^\infty(-1)^{k+1}\binom{k+x}{k+1}x^{k+1}$ "
        r"(4.1), "
        r"where the left side is interpreted as in (3.1).",
    ),
    rec(
        "RN-P1-C08-Entry05",
        r"For any complex number $x$, "
        r"$\displaystyle\sum_{k=1}^\infty\left\{\frac{1}{k-1+x}-\frac{1}{k+x}\right\}=\pi\cot(\pi x)$ "
        r"(5.1). "
        r"(Ramanujan incorrectly multiplies the right side of (5.1) by $-1$.)",
    ),
    rec(
        "RN-P1-C08-Entry06",
        r"Let $n$ be a positive integer and let $x$ be any complex number. Then "
        r"$\displaystyle n\psi(x+1)-\sum_{k=1}^n\psi\!\left(\frac{x+k}{n}+1\right)=n\log n$.",
    ),
    rec(
        "RN-P1-C08-Entry06-Corollary01",
        r"Let $|\arg x|<\pi$. Then as $|x|\to\infty$, "
        r"$\displaystyle\psi(x+1)\sim\log x+\sum_{k=1}^\infty\frac{B_{2k}(1-2^{1-2k})}{2k\,x^{2k}}$.",
    ),
    rec(
        "RN-P1-C08-Entry06-Corollary02",
        r"If $n$ is a positive integer, then "
        r"$\displaystyle\sum_{k=1}^{n-1}\psi\!\left(\frac{k}{n}\right)=-(n-1)\gamma-n\log n$ "
        r"(6.1).",
    ),
    rec(
        "RN-P1-C08-Entry06-Corollary03",
        r"We have "
        r"(i) $\displaystyle\psi(1)=-\gamma-2\log 2$; "
        r"(ii) $\displaystyle\psi\!\left(\tfrac{1}{3}\right)=-\gamma-\tfrac{3}{2}\log 3-\tfrac{\pi}{2\sqrt{3}}$; "
        r"(iii) $\displaystyle\psi\!\left(\tfrac{1}{4}\right)=-\gamma-3\log 2-\tfrac{\pi}{2}$; "
        r"(iv) $\displaystyle\psi\!\left(\tfrac{1}{6}\right)=-\gamma-2\log 2-\tfrac{3}{2}\log 3-\tfrac{\pi\sqrt{3}}{2}$; and "
        r"(v) $\displaystyle 3\psi(1)-2\psi\!\left(\tfrac{1}{2}\right)=-\gamma+\pi$.",
    ),
    rec(
        "RN-P1-C08-Entry06-Corollary04",
        r"If $n$ is a positive integer, then "
        r"$\displaystyle\sum_{k=1}^n\psi\!\left(\frac{2k-1}{2n}\right)=-n\gamma-n\log(4n)$.",
    ),
    rec(
        "RN-P1-C08-Entry07",
        r"If $x$ is a positive integer and $a$ and $b$ are arbitrary complex numbers, then "
        r"$\displaystyle\psi\!\left(\frac{a}{b}+x+1\right)-\psi\!\left(\frac{a}{b}+1\right)"
        r"=\sum_{k=1}^x\frac{b}{a+bk}$.",
    ),
    rec(
        "RN-P1-C08-Entry08",
        r"If $a$ and $b$ are arbitrary complex numbers, then "
        r"$\displaystyle\psi\!\left(\frac{a+2b}{2b}\right)-\psi\!\left(\frac{a+b}{2b}\right)"
        r"=\sum_{k=1}^\infty\frac{2b(-1)^{k+1}}{a+bk}$.",
    ),
    rec(
        "RN-P1-C08-Entry09",
        r"If $\Re x>0$, then "
        r"$\displaystyle\psi\!\left(\frac{1}{2x}+1\right)=\psi\!\left(\frac{1}{x}+1\right)-\log 2"
        r"+x\int_0^1\frac{u^x}{1+u}\,du$ "
        r"(9.1).",
    ),
    rec(
        "RN-P1-C08-Entry10",
        r"If $\Re x<0$, then "
        r"$\displaystyle\psi\!\left(1-\frac{1}{x}\right)+\gamma"
        r"=-x\int_0^1\frac{e^{1-u}}{u(u^x-1)}\,du$.",
    ),
    rec(
        "RN-P1-C08-Entry11",
        r"Let "
        r"$\displaystyle\varphi(x)=1+\sum_{k=1}^\infty\frac{1}{k^3-kx}$ "
        r"(11.1). "
        r"If $x$ is any complex number, then "
        r"$\displaystyle\psi\!\left(\frac{1}{x}\right)+\psi\!\left(1-\frac{1}{x}\right)=-2\gamma-x\varphi(x)$.",
    ),
    rec(
        "RN-P1-C08-Entry12",
        r"If $\Re x>1$, then "
        r"$\displaystyle\int_0^1\frac{u^{x-2}(1-u)^2}{1-u}\,du=\varphi(x)-1$, "
        r"where $\varphi$ is defined by (11.1).",
    ),
    rec(
        "RN-P1-C08-Entry13",
        r"If $\Re x>0$, then "
        r"$\displaystyle\varphi(2x)-\tfrac{1}{2}\varphi(x)-\tfrac{1}{2}\log 2"
        r"=\int_0^1\frac{1}{1+ux}\,du-\frac{\pi}{2x}\csc\!\left(\frac{\pi}{2x}\right)$, "
        r"where $\varphi$ is defined by (11.1).",
    ),
    rec(
        "RN-P1-C08-Entry13-Examplei",
        r"If $|x|<1$ and $\Re n>0$, then "
        r"$\displaystyle\int_0^x\frac{du}{1+u^n}=\sum_{k=0}^\infty\frac{(-1)^k x^{nk+1}}{nk+1}$.",
    ),
    rec(
        "RN-P1-C08-Entry13-Exampleii",
        r"If $|x|<1$ and $\Re n>0$, then "
        r"$\displaystyle\int_0^x\frac{du}{1-u^n}=\sum_{k=0}^\infty\frac{x^{nk+1}}{nk+1}$.",
    ),
    rec(
        "RN-P1-C08-Entry13-Exampleiii",
        r"If $|x|<1$ and $n$ is odd, then "
        r"$\displaystyle\int_0^x\frac{du}{1-u^n}=\int_0^x\frac{du}{1+(-u)^n}$.",
    ),
    rec(
        "RN-P1-C08-Entry13-Exampleiv",
        r"If $|x|<1$ and $n$ is even, then "
        r"$\displaystyle\int_0^x\frac{du}{1-u^n}"
        r"=\tfrac{1}{2}\int_0^x\frac{du}{1+u^{n/2}}+\tfrac{1}{2}\int_0^x\frac{du}{1-u^{n/2}}$.",
    ),
    rec(
        "RN-P1-C08-Entry13-Examplev",
        r"Let $\ell$ and $n$ be positive integers with $\ell<n+1$. "
        r"If $n$ is even, then "
        r"$\displaystyle\int\frac{x^{\ell-1}}{x^n-1}\,dx"
        r"=-\log(x-1)+\frac{(-1)^\ell}{n}\log(x+1)"
        r"+\frac{2}{n}\sum_{r=1}^{\lfloor(\ell n-1)/n\rfloor}\cos\!\left(\frac{2\pi r\ell}{n}\right)"
        r"\log\!\left(x^2-2x\cos\frac{2\pi r}{n}+1\right)"
        r"-\frac{2}{n}\sum_{r=1}^{\lfloor(\ell n-1)/n\rfloor}\frac{\sin(2\pi r\ell/n)}{\sin(2\pi r/n)}"
        r"\tan^{-1}\!\left(\frac{x-\cos(2\pi r/n)}{\sin(2\pi r/n)}\right)$. "
        r"If $n$ is odd, then "
        r"$\displaystyle\int\frac{x^{\ell-1}}{x^n+1}\,dx"
        r"=\frac{(-1)^{\ell-1}}{n}\log(x+1)"
        r"-\frac{2}{n}\sum_{r=1}^{\lfloor(\ell n-1)/n\rfloor}\cos\!\left(\frac{(2r-1)\pi\ell}{n}\right)"
        r"\log\!\left(x^2-2x\cos\frac{(2r-1)\pi}{n}+1\right)"
        r"+\frac{2}{n}\sum_{r=1}^{\lfloor(\ell n-1)/n\rfloor}\frac{\sin((2r-1)\pi\ell/n)}{\sin((2r-1)\pi/n)}"
        r"\tan^{-1}\!\left(\frac{x-\cos((2r-1)\pi/n)}{\sin((2r-1)\pi/n)}\right)$.",
    ),
    rec(
        "RN-P1-C08-Entry13-Examplevi",
        r"Let $\ell$ and $n$ be positive integers with $\ell<n+1$. "
        r"If $n$ is odd, then "
        r"$\displaystyle\int\frac{x^{\ell-1}}{x^n-1}\,dx"
        r"=-\log(x-1)+\frac{2}{n}\sum_{r=1}^{\lfloor(n-1)/2\rfloor}\cos\!\left(\frac{2\pi r\ell}{n}\right)"
        r"\log\!\left(x^2-2x\cos\frac{2\pi r}{n}+1\right)"
        r"-\frac{2}{n}\sum_{r=1}^{\lfloor(n-1)/2\rfloor}\frac{\sin(2\pi r\ell/n)}{\sin(2\pi r/n)}"
        r"\tan^{-1}\!\left(\frac{x-\cos(2\pi r/n)}{\sin(2\pi r/n)}\right)$. "
        r"If $n$ is even, then "
        r"$\displaystyle\int\frac{x^{\ell-1}}{x^n+1}\,dx"
        r"=-\frac{2}{n}\sum_{r=1}^{n/2}\cos\!\left(\frac{(2r-1)\pi\ell}{n}\right)"
        r"\log\!\left(x^2-2x\cos\frac{(2r-1)\pi}{n}+1\right)"
        r"+\frac{2}{n}\sum_{r=1}^{n/2}\frac{\sin((2r-1)\pi\ell/n)}{\sin((2r-1)\pi/n)}"
        r"\tan^{-1}\!\left(\frac{x-\cos((2r-1)\pi/n)}{\sin((2r-1)\pi/n)}\right)$.",
    ),
    rec(
        "RN-P1-C08-Entry14i",
        r"Let $A_n=\displaystyle\int_0^x\frac{du}{1+u^n}$. Then $A_1=\log(1+x)$.",
    ),
    rec(
        "RN-P1-C08-Entry14ii",
        r"With $A_n$ as in Entry 14(i), $A_2=\tan^{-1}x$.",
    ),
    rec(
        "RN-P1-C08-Entry14iii",
        r"With $A_n$ as in Entry 14(i), "
        r"$A_3=-\tfrac{1}{6}\log\!\left(\dfrac{1+x}{1+x^3}\right)+\dfrac{1}{\sqrt{3}}\tan^{-1}\!\left(\dfrac{x}{\sqrt{3}}\right)$.",
    ),
    rec(
        "RN-P1-C08-Entry14iv",
        r"With $A_n$ as in Entry 14(i), "
        r"$A_4=-\dfrac{1}{4\sqrt{2}}\log\!\left(\dfrac{1+x\sqrt{2}+x^2}{1-x\sqrt{2}+x^2}\right)"
        r"+\dfrac{1}{2\sqrt{2}}\tan^{-1}\!\left(\dfrac{x}{\sqrt{2}-x}\right)"
        r"+\dfrac{1}{2\sqrt{2}}\tan^{-1}\!\left(\dfrac{x}{\sqrt{2}+x}\right)$.",
    ),
    rec(
        "RN-P1-C08-Entry14v",
        r"With $A_n$ as in Entry 14(i), "
        r"$A_5=-\dfrac{1}{20}\log\!\left(\dfrac{1+x}{1+x^5}\right)"
        r"+\dfrac{1}{4\sqrt{5}}\log\!\left(\dfrac{1+\tfrac{1}{2}x(\sqrt{5}-1)+x^2}{1-\tfrac{1}{2}x(\sqrt{5}+1)+x^2}\right)"
        r"+\dfrac{1}{\sqrt{10+2\sqrt{5}}}\tan^{-1}\!\left(\dfrac{x\sqrt{10+2\sqrt{5}}}{4+x(\sqrt{5}-1)}\right)"
        r"+\dfrac{1}{\sqrt{10-2\sqrt{5}}}\tan^{-1}\!\left(\dfrac{x\sqrt{10-2\sqrt{5}}}{4-x(\sqrt{5}+1)}\right)$.",
    ),
    rec(
        "RN-P1-C08-Entry14vi",
        r"With $A_n$ as in Entry 14(i), "
        r"$A_6=\tfrac{1}{2}\tan^{-1}x+\tfrac{1}{6}\tan^{-1}\!\left(\dfrac{x}{3}\right)"
        r"+\dfrac{1}{4\sqrt{3}}\log\!\left(\dfrac{1+x\sqrt{3}+x^2}{1-x\sqrt{3}+x^2}\right)$.",
    ),
    rec(
        "RN-P1-C08-Entry14vii",
        r"With $A_n$ as in Entry 14(i), "
        r"$A_8=\dfrac{1}{16}\log\!\left(\dfrac{(\sqrt{2}+\sqrt{2})(1+x\sqrt{2+\sqrt{2}}+x^2)}"
        r"{(1-x\sqrt{2+\sqrt{2}}+x^2)}\right)"
        r"+2\tan^{-1}\!\left(\dfrac{x}{\sqrt{2+\sqrt{2}}}\right)"
        r"+\dfrac{1}{16}\log\!\left(\dfrac{(\sqrt{2}-\sqrt{2})(1+x\sqrt{2-\sqrt{2}}+x^2)}"
        r"{(1-x\sqrt{2-\sqrt{2}}+x^2)}\right)$.",
    ),
    rec(
        "RN-P1-C08-Entry14viii",
        r"With $A_n$ as in Entry 14(i), "
        r"$A_{10}=\dfrac{1}{5}\tan^{-1}x"
        r"+\dfrac{1}{2(1-x^2)}\tan^{-1}\!\left(x\sqrt{6+2\sqrt{5}}\right)"
        r"+\dfrac{1}{2(1-x^2)}\tan^{-1}\!\left(x\sqrt{6-2\sqrt{5}}\right)"
        r"+\dfrac{\sqrt{10+2\sqrt{5}}}{40}\log\!\left(\dfrac{1+\tfrac{1}{2}x\sqrt{10+2\sqrt{5}}+x^2}"
        r"{1-\tfrac{1}{2}x\sqrt{10+2\sqrt{5}}+x^2}\right)"
        r"+\dfrac{\sqrt{10-2\sqrt{5}}}{40}\log\!\left(\dfrac{1+\tfrac{1}{2}x\sqrt{10-2\sqrt{5}}+x^2}"
        r"{1-\tfrac{1}{2}x\sqrt{10-2\sqrt{5}}+x^2}\right)$.",
    ),
    rec(
        "RN-P1-C08-Entry14-Example01",
        r"We have "
        r"(i) $\displaystyle\sum_{k=0}^\infty\frac{(-1)^k}{(3k+1)\,3^{2k+1}}=\dfrac{\pi}{6\sqrt{3}}+\dfrac{1}{6}\gamma$; "
        r"(ii) $\displaystyle\sum_{k=0}^\infty\frac{(-1)^k(\sqrt{3}-1)\,3^{2k+1}}{(1+\sqrt{3})(3k+1)}"
        r"=-\dfrac{\pi}{4\sqrt{3}}+\dfrac{1}{4\sqrt{3}}\gamma$; and "
        r"(iii) $\displaystyle\sum_{k=0}^\infty\frac{(-1)^k(2-\sqrt{3})^{2k+1}}{4k+1}"
        r"=-\dfrac{\sqrt{3}-1}{16}\log\!\left(\dfrac{\sqrt{3}-1}{\sqrt{2}}\right)$ "
        r"(Ramanujan inadvertently omitted a factor $\sqrt{2}$ in the denominator on the right side).",
    ),
    rec(
        "RN-P1-C08-Entry14-Example02",
        r"With $\varphi(x)$ defined by (11.1), we have "
        r"(i) $\varphi(2)=2\log 2$; "
        r"(ii) $\varphi(3)=\log 3$; "
        r"(iii) $\varphi(4)=\tfrac{3}{2}\log 2$; "
        r"(iv) $\varphi(6)=\tfrac{1}{2}\log 3+\tfrac{1}{4}\log 4$; "
        r"(v) $\varphi(5)=\tfrac{1}{4}\log 5+\dfrac{\sqrt{5}}{2}\log\!\left(\dfrac{\sqrt{5}+1}{2}\right)$; "
        r"(vi) $\varphi(8)=\log 2+\tfrac{1}{4}\log(\sqrt{2}+1)$; "
        r"(vii) $\varphi(10)=\tfrac{1}{2}\log 2+\tfrac{1}{4}\log 5+\dfrac{3}{2\sqrt{5}}\log\!\left(\dfrac{\sqrt{5}+1}{2}\right)$; "
        r"(viii) $\varphi(12)=\dfrac{3+\sqrt{3}}{6}\log 2+\tfrac{1}{4}\log 3-\dfrac{\sqrt{3}}{6}\log(\sqrt{3}-1)$; "
        r"(ix) $\varphi(16)=\tfrac{1}{4}\log 2+\dfrac{1}{4\sqrt{2}}\log(\sqrt{2}+1)$; and "
        r"(x) $\displaystyle\varphi(20)=\tfrac{1}{10}\log 2+\tfrac{1}{4}\log 5"
        r"+\dfrac{\sqrt{5}}{4}\log\!\left(\dfrac{\sqrt{5}+1}{2}\right)"
        r"+\dfrac{\sqrt{10+2\sqrt{5}}}{40}\log\!\left(\dfrac{4+\sqrt{10+2\sqrt{5}}}{4-\sqrt{10+2\sqrt{5}}}\right)"
        r"+\dfrac{\sqrt{10-2\sqrt{5}}}{40}\log\!\left(\dfrac{4+\sqrt{10-2\sqrt{5}}}{4-\sqrt{10-2\sqrt{5}}}\right)$.",
    ),
    rec(
        "RN-P1-C08-Entry15",
        r"Let $x$ be real and positive with $\log a=\psi(x+1)$ (15.1), and let $n$ be any complex number. "
        r"Then as $a\to\infty$, "
        r"$\displaystyle\left(\frac{a}{z}\right)^{4n}\sim 1-\frac{n}{6a^2}"
        r"+\frac{n(7n-31)}{2880a^4}-\frac{533n}{10080a^6}+\cdots$ "
        r"(15.2), "
        r"where $z$ is defined implicitly by $\log a=\psi(z+1)$.",
    ),
    rec(
        "RN-P1-C08-Entry15-Corollary",
        r"$\Gamma(x+1)$ is minimum when $x=6/13$ very nearly.",
    ),
    rec(
        "RN-P1-C08-Entry16",
        r"Let $A_k=\lfloor 3^k/2\rfloor-1$ for $k\ge 0$. Then "
        r"$\displaystyle\gamma=\log 2-2\sum_{k=1}^\infty\frac{A_k}{k}"
        r"\sum_{j=A_k-1+1}^{\lfloor 3^j/2\rfloor-1}\frac{1}{(3^j-3)}$ "
        r"(16.1), "
        r"where $\gamma$ denotes Euler's constant.",
    ),
    rec(
        "RN-P1-C08-Entry17i",
        r"Let "
        r"$\displaystyle\varphi(x)=\sum_{k=1}^x\frac{\log k}{k}$ "
        r"(17.1), "
        r"$c_1=\displaystyle\lim_{n\to\infty}\left\{\varphi(n)-\tfrac{1}{2}\log^2 n\right\}$ "
        r"(17.2), and "
        r"$H_n=\displaystyle\sum_{k=1}^n\frac{1}{k}$ "
        r"(17.3). "
        r"Then as $x\to\infty$, "
        r"$\displaystyle\varphi(x)-\psi(x+1)\log x-\tfrac{1}{2}\log^2 x+c_1"
        r"+\sum_{k=1}^\infty\frac{B_{2k}}{2^{2k-1}\,2k\,x^{2k}}$, "
        r"where $B_n$ denotes the $n$th Bernoulli number.",
    ),
    rec(
        "RN-P1-C08-Entry17-Corollary01",
        r"Let $\varphi(x)$ and $c_1$ be defined by (17.1) and (17.2), respectively. Then "
        r"$\displaystyle\lim_{x\to\infty}\left\{\varphi(x)-\tfrac{1}{2}\psi^2(x+1)\right\}=c_1$.",
    ),
    rec(
        "RN-P1-C08-Entry17ii",
        r"If $x$ is real, then "
        r"$\displaystyle\varphi(x)=\sum_{k=1}^\infty\left\{\frac{\log k}{k}-\frac{\log(k+x)}{k+x}\right\}$ "
        r"(17.7).",
    ),
    rec(
        "RN-P1-C08-Entry17-Corollary02",
        r"If $\varphi(x)$ is defined by (17.7), then "
        r"$\displaystyle\sum_{k=0}^\infty\frac{(-1)^k}{2k+1}"
        r"=\tfrac{1}{4}\left\{\varphi\!\left(-\tfrac{1}{4}\right)-\varphi\!\left(-\tfrac{3}{4}\right)\right\}+\tfrac{1}{4}\pi\log 2$.",
    ),
    rec(
        "RN-P1-C08-Entry17iii",
        r"If $\varphi(x)$ is defined by (17.7) and $n$ is a positive integer, then "
        r"$\displaystyle n\varphi(x)-\sum_{k=0}^{n-1}\varphi\!\left(\frac{x-k}{n}\right)"
        r"=n\log n\,\psi(x+1)-\tfrac{1}{2}n\log^2 n$.",
    ),
    rec(
        "RN-P1-C08-Entry17-Corollary03",
        r"If $\varphi(x)$ is defined by (17.7), then "
        r"$\displaystyle\sum_{k=1}^{n-1}\varphi\!\left(\frac{k}{n}\right)"
        r"=\gamma n\log n+\tfrac{1}{2}n\log^2 n$ "
        r"(17.8).",
    ),
    rec(
        "RN-P1-C08-Entry17-Example01",
        r"$\displaystyle\prod_{k=1}^\infty\frac{(2k-1)^{1/(2k-1)}}{(2k)^{1/(2k)}}"
        r"=\sqrt{2}\,e^{-\tfrac{1}{2}\gamma\log 2-\pi}$.",
    ),
    rec(
        "RN-P1-C08-Entry17-Example02",
        r"$\displaystyle\varphi\!\left(-\tfrac{1}{4}\right)=2\gamma\log 2+\log^2 2$.",
    ),
    rec(
        "RN-P1-C08-Entry17-Example03",
        r"$\displaystyle\varphi\!\left(-\tfrac{1}{4}\right)+\varphi\!\left(-\tfrac{1}{3}\right)"
        r"=3\gamma\log 3+\tfrac{1}{2}\log^2 3$.",
    ),
    rec(
        "RN-P1-C08-Entry17-Example04",
        r"$\displaystyle\varphi\!\left(-\tfrac{1}{4}\right)+\varphi\!\left(-\tfrac{1}{2}\right)"
        r"=6\gamma\log 2+7\log^2 2$.",
    ),
    rec(
        "RN-P1-C08-Entry17-Example05",
        r"$\displaystyle\varphi\!\left(-\tfrac{1}{3}\right)+\varphi\!\left(-\tfrac{1}{2}\right)"
        r"=3\gamma\log 3+4\gamma\log 2+\tfrac{1}{2}\log^2(12)-\log^2 4$.",
    ),
    rec(
        "RN-P1-C08-Entry17iv",
        r"If $0<x<1$, then "
        r"$\displaystyle\frac{\pi}{2}\left\{\log\frac{\Gamma(x)}{\Gamma(1-x)}"
        r"+(\gamma+\log(2\pi))(2x-1)\right\}"
        r"=\sum_{k=1}^\infty\frac{\log k}{k}\sin(2\pi kx)$.",
    ),
    rec(
        "RN-P1-C08-Entry17v",
        r"Let $\varphi(x)$ be defined by (17.7). If $0<x<1$, then "
        r"$\displaystyle\varphi(x-1)-\varphi(-x)=(\gamma+\log(2\pi))\pi\cot(\pi x)"
        r"+2\pi\sum_{k=1}^\infty\sin(2\pi kx)\log k$ "
        r"(17.11). "
        r"(Berndt: right-side series diverges for $0<x<1$.)",
    ),
    rec(
        "RN-P1-C08-Entry17-Example06",
        r"$\displaystyle\sum_{k=0}^\infty\frac{(-1)^k\log(2k+1)}{2k+1}"
        r"=\tfrac{1}{4}\pi\log\pi-\tfrac{1}{4}\log\Gamma\!\left(\tfrac{1}{4}\right)-\tfrac{1}{4}\pi\gamma$.",
    ),
    rec(
        "RN-P1-C08-Entry17-Example07",
        r"$\displaystyle\left\{\prod_{k=1}^\infty\frac{(2k-1)^{1/(2k-1)}}{(2k)^{1/(2k)}}\right\}^{1/\log 2}"
        r"=\dfrac{\sqrt{2}}{4}\,\Gamma\!\left(\tfrac{1}{4}\right)^{3/\pi}$ "
        r"and "
        r"$\displaystyle\left\{\prod_{k=1}^\infty\frac{(4k-3)^{1/(4k-3)}}{(4k-1)^{1/(4k-1)}}\right\}^{4/\pi}"
        r"=\dfrac{3\sqrt{2}}{4}\,\Gamma\!\left(\tfrac{1}{4}\right)$.",
    ),
    rec(
        "RN-P1-C08-Entry18i",
        r"Let $c_1$ and $H_n$ be defined by (17.2) and (17.3), respectively. Define "
        r"$\displaystyle\varphi(x)=\sum_{k=1}^x\log^2 k$ "
        r"(18.1) and "
        r"$\displaystyle C=\lim_{n\to\infty}\left\{\sum_{k=1}^n\log^2 k-n\log^2 n\right\}$ "
        r"(18.2). "
        r"Then as $x\to\infty$, "
        r"$\displaystyle\varphi(x)-2\log x\,\log\!\left(\frac{\Gamma(x)}{\sqrt{\pi}}\right)"
        r"\sim-\left(x+\tfrac{1}{2}\right)\log^2 x+2x+C"
        r"-2\sum_{k=1}^\infty\frac{B_{2k}H_{2k-2}}{(2k-1)(2k)\,x^{2k-1}}$.",
    ),
    rec(
        "RN-P1-C08-Entry18ii",
        r"Let $\varphi(x)$ be defined by (18.13) and let $C$ be given by (18.2). "
        r"If $n$ is any natural number, then "
        r"$\displaystyle\varphi(x)-\sum_{j=0}^{n-1}\varphi\!\left(\frac{x-j}{n}\right)"
        r"=2\log n\,\log\frac{\Gamma(x+1)}{\sqrt{2\pi}}"
        r"-\left(x+\tfrac{1}{2}\right)\log^2 n-C(n-1)$ "
        r"(18.16), "
        r"where $\displaystyle\varphi(x)=-\zeta'(0,x+1)+\zeta'(0)$ (18.13).",
    ),
    rec(
        "RN-P1-C08-Entry18iii",
        r"Let $\varphi(x)$, $c_1$, and $C$ be defined by (18.13), (17.2), and (18.2), respectively. "
        r"If $0<x<1$, then "
        r"$\displaystyle\tfrac{1}{2}\{\varphi(x-1)+\varphi(-x)\}"
        r"=c_1-\tfrac{1}{4}\pi^2\sum_{k=1}^\infty\frac{\log k}{k}\cos(2\pi kx)"
        r"+\tfrac{1}{2}(\gamma+\log(2\pi))\left\{\gamma-\log\!\left(\tfrac{1}{2}\pi\csc^2(\pi x)\right)\right\}$ "
        r"(18.19).",
    ),
    rec(
        "RN-P1-C08-Entry18-Corollary",
        r"Under the assumptions of Entry 18(ii), "
        r"$\displaystyle\sum_{k=1}^{n-1}\varphi\!\left(\frac{k}{n}\right)"
        r"=\log(2\pi)\log n+\tfrac{1}{2}\log^2 n+C(n-1)$.",
    ),
    rec(
        "RN-P1-C08-Entry18-Example01",
        r"$\displaystyle\lim_{x\to\infty}\frac{x\log x-2x}{e^{2x}}\prod_{k=1}^x\frac{k^{1/k}}{\log k}"
        r"=(2\pi)^{1/2}\log(2\pi)\,e^{-\pi^2/2+1/(24\pi^2)}$.",
    ),
    rec(
        "RN-P1-C08-Entry18-Example02",
        r"Let $\varphi(x)$ be defined by (18.13) and let $C$ be given by (18.2). Then "
        r"$\displaystyle\varphi\!\left(-\tfrac{1}{4}\right)=\log(2\pi)\log 2+\tfrac{1}{2}\log^2 2+C$; "
        r"$\displaystyle\varphi\!\left(-\tfrac{1}{3}\right)+\varphi\!\left(-\tfrac{1}{4}\right)"
        r"=\log(2\pi)\log 3+\tfrac{1}{2}\log^2 3+2C$; "
        r"$\displaystyle\varphi\!\left(-\tfrac{1}{4}\right)+\varphi\!\left(-\tfrac{3}{4}\right)"
        r"=\log(2\pi)\log 2+\tfrac{1}{2}\log^2 2+2C$; and "
        r"$\displaystyle\varphi\!\left(-\tfrac{1}{3}\right)+\varphi\!\left(-\tfrac{1}{2}\right)"
        r"=\log 2\log 3+2C$.",
    ),
    rec(
        "RN-P1-C08-Entry19i",
        r"Let $n$ be a positive integer. Then, in the notation of (19.2), "
        r"$\displaystyle\mathfrak{L}\psi_n(x)=\mathfrak{L}\sum_{j=0}^n(-1)^{j+1}\binom{n}{j}\log^j x\,\psi_{n-j}(x)$ "
        r"(19.3), "
        r"where $\mathfrak{L}f(x)$ denotes the logarithmic part of $f(x)$ as $x\to\infty$.",
    ),
    rec(
        "RN-P1-C08-Entry19ii",
        r"Let $\psi_n(x)$, $n\ge 0$, be defined by (19.2). Then as $x\to\infty$, "
        r"$\displaystyle\sum_{k=0}^n(-1)^{n+k}\binom{n}{k}\log^k x\,\psi_{n-k}(x)"
        r"\sim n!\left\{\frac{B_{n+1}}{(n+1)x^n}+\frac{nB_{n+2}}{2(n+2)x^{n+1}}"
        r"+\frac{n(n+1)B_{n+3}}{2^2\cdot 2!(n+3)x^{n+2}}\right.$ "
        r"$\displaystyle\left.+\frac{n(n+2)(n+3)B_{n+4}}{2^3\cdot 3!(n+4)x^{n+3}}\right.$ "
        r"$\displaystyle\left.+\frac{n\{(n+2)(n+4)^2+\tfrac{1}{2}(n+2)+\tfrac{1}{3}\}B_{n+5}}{2^4\cdot 4!(n+5)x^{n+4}}\right.$ "
        r"$\displaystyle\left.+\frac{n(n+4)(n+5)\{(n+3)(n+4)+\tfrac{1}{2}n+\tfrac{1}{6}\}B_{n+6}}{2^5\cdot 5!(n+6)x^{n+5}}+\cdots\right\}$ "
        r"(19.7).",
    ),
    rec(
        "RN-P1-C08-Entry19iii",
        r"Let $\psi_n(x)$ be defined by (19.17), where $n\ge 1$. "
        r"If $r$ is any positive integer, then "
        r"$\displaystyle\psi_n(x)-\sum_{j=0}^{r-1}\psi_n\!\left(\frac{x-j}{r}\right)"
        r"=\sum_{j=1}^n\binom{n}{j}(-1)^{j+1}\log^j r\,\psi_{n-j}(x)$ "
        r"(19.19).",
    ),
    rec(
        "RN-P1-C08-Entry19-Corollary01",
        r"For each pair of positive integers $n$ and $r$, "
        r"$\displaystyle\sum_{j=1}^{r-1}\psi_n\!\left(\frac{j}{r}\right)"
        r"=\sum_{j=1}^n\binom{n}{j}(-1)^{j+1}c_j\log^j r$, "
        r"where $c_j$ is the constant in (19.1).",
    ),
    rec(
        "RN-P1-C08-Entry19-Corollary02",
        r"Let $\mathfrak{L}f(x)$ denote the logarithmic part of $f(x)$ as defined prior to Entry 19(i). "
        r"If $x$ and $n$ are positive integers, then "
        r"$\displaystyle\mathfrak{L}\sum_{j=0}^{x-1}\psi_n\!\left(\frac{x-j}{x}\right)=0$.",
    ),
    rec(
        "RN-P1-C08-Entry20i",
        r"Let $r$ and $x$ be positive integers and suppose $k>0$. Define "
        r"$F_k(x)=P\varphi(x)=\displaystyle\sum_{n=1}^x n^{k-1}$ "
        r"(20.1). "
        r"If $k\neq 1$, then "
        r"$\displaystyle\varphi(x)=\sum_{j=0}^r\binom{r}{j}\psi_{j(-k)}\frac{x^{r-j}}{(k-1)^{j+1}}"
        r"+\frac{C_r(k)}{(k-1)^{r+1}}x^r+\frac{P}{(k-1)^{r+1}}+2\varphi(k)+kx+1$ "
        r"(20.2), "
        r"where "
        r"$\displaystyle\psi_{j(-k)}=\frac{k(-1)^{j+1}\log^{j+1}k}{j!(k-1)^{j+1}}$ "
        r"for $0\le j\le r$, "
        r"$\displaystyle C_r(k)=\frac{(-1)^{r+1}r!}{k\log^{r+1}k}$, "
        r"and $R$ is given by (20.5).",
    ),
    rec(
        "RN-P1-C08-Entry20ii",
        r"For each positive integer $r$, "
        r"$\displaystyle\psi_r(-k)=\frac{(-1)^{r+1}}{(1-k)^{r+1}}$ "
        r"and "
        r"$\displaystyle k^j\psi_j(-k)=\frac{k}{j!}\,\psi_{j(-k)}$ for $0\le j\le r$, "
        r"where $\psi_{j(-k)}$ is defined in Entry 20(i).",
    ),
    rec(
        "RN-P1-C08-Entry20iii",
        r"For $0<k<1$ and real $r$, let "
        r"$\displaystyle C_r(k)=\sum_{m=1}^\infty m^r k^{m-1}$. "
        r"If $x$ is real and $n$ is any positive integer, then "
        r"$\displaystyle\sum_{j=0}^n F_k\!\left(\frac{x-j}{n}\right)"
        r"=nC_r(k)+n^{-rk(1-n)/n}\left\{F_{k/n}(x)-C_r(k/n)\right\}$ "
        r"(20.9), "
        r"where $F_k$ is defined by (20.8).",
    ),
    rec(
        "RN-P1-C08-Entry20-Corollary",
        r"Under the same hypotheses as Entry 20(iii), "
        r"$\displaystyle\sum_{j=1}^n F_k\!\left(-\frac{j}{n}\right)"
        r"=nC_r(k)-n^{-rk(1-n)/n}C_r(k/n)$.",
    ),
    rec(
        "RN-P1-C08-Entry21i",
        r"Define "
        r"$\displaystyle\varphi_r(x)=\sum_{k=1}^x\frac{\log^r k}{k^r}$ "
        r"(21.1) and "
        r"$\displaystyle H_n(r)=\sum_{k=0}^n\frac{1}{k+r}$ "
        r"(21.2). "
        r"Let $\zeta(s,x)$ denote the extended Hurwitz zeta-function. "
        r"Then as $x\to\infty$, "
        r"$\displaystyle\varphi_r(x)+\log x\,\zeta(r,x+1)-\zeta'(r)"
        r"\sim\frac{1}{(r-1)^2 x^{r-1}}"
        r"+\sum_{k=1}^\infty\frac{B_{2k}(r)_{2k-1}H_{2k-1}(r)}{(2k)!\,x^{r+2k-1}}$ "
        r"(21.3).",
    ),
    rec(
        "RN-P1-C08-Entry21ii",
        r"Let $\varphi_r(x)$ be defined by (21.10). Then for $r>0$ and $|x|<1$, "
        r"$\displaystyle\varphi_r(x)=\sum_{j=1}^\infty\binom{-r}{j}"
        r"\left\{\zeta(r+j)H_{j-1}(r)-\zeta'(r+j)\right\}x^j$, "
        r"where $H_n(r)$ is defined by (21.2).",
    ),
    rec(
        "RN-P1-C08-Entry21iii",
        r"If $r>1$ and $n$ is any natural number, then "
        r"$\displaystyle n^r\varphi_r(x)-\sum_{j=0}^{n-1}\varphi_r\!\left(\frac{x-j}{n}\right)"
        r"=(n-n^r)\zeta'(r)-nr\log n\,\zeta(r,x+1)$.",
    ),
    rec(
        "RN-P1-C08-Entry21-Corollary",
        r"For $r>1$ and each positive integer $n$, "
        r"$\displaystyle\sum_{j=1}^{n-1}\varphi_r\!\left(\frac{j}{n}\right)"
        r"=nr\log n\,\zeta(r)+(nr-n)\zeta'(r)$.",
    ),
    rec(
        "RN-P1-C08-Entry22i",
        r"If $c_r$ is the constant appearing in the asymptotic expansion of $\varphi_r(x)$ as $x\to\infty$, then "
        r"$\displaystyle c_r=\lim_{x\to\infty}\left\{\varphi_r(x)-\frac{\log^{r+1}x}{r+1}\right\}$.",
    ),
    rec(
        "RN-P1-C08-Entry22ii",
        r"Let $r$ be any nonnegative integer and $n$ any positive integer. "
        r"With $\varphi_r(x)$ defined by (22.2), "
        r"$\displaystyle n\varphi_r(x)-\sum_{j=0}^{n-1}\varphi_r\!\left(\frac{x-j}{n}\right)"
        r"=\binom{n}{r}\log^{r+1}n+n\sum_{j=1}^r\binom{r}{j}(-1)^{j+1}\log^j n"
        r"\left\{\varphi_{r-j}(x)-c_{r-j}\right\}+\frac{(-1)^r n}{r+1}\log^{r+1}n$.",
    ),
    rec(
        "RN-P1-C08-Entry23",
        r"Let $c_r$ be defined as in Entry 22(i). If $r\ge 0$ and $\Re s>0$, then "
        r"$\displaystyle\sum_{k=1}^\infty\frac{\log^r k}{k^{s+1}}"
        r"=\frac{r(r+1)}{s^{r+1}}+\sum_{k=0}^\infty\frac{(-1)^k c_{r+k}s^k}{k!}$ "
        r"(23.1).",
    ),
    rec(
        "RN-P1-C08-Entry23-Example01",
        r"$-\zeta'''\!\left(\tfrac{1}{2}\right)\approx 96.001$.",
    ),
    rec(
        "RN-P1-C08-Entry23-Example02",
        r"$-\zeta'(2)\approx 0.9382$.",
    ),
    rec(
        "RN-P1-C08-Entry23-Example03",
        r"$\zeta^{(4)}(2)\approx 24$.",
    ),
    rec(
        "RN-P1-C08-Entry23-Example04",
        r"$-\zeta^{(5)}\!\left(\tfrac{1}{2}\right)\approx 7680$.",
    ),
    rec(
        "RN-P1-C08-Entry23-Example05",
        r"$\displaystyle\sum_{k=1}^\infty\frac{\log^{11/2}k}{k^2}\approx 288$.",
    ),
    rec(
        "RN-P1-C08-Entry24i",
        r"Let "
        r"$\displaystyle\varphi(x)=\sum_{k=1}^x\frac{\log k}{\sqrt{k}}$ "
        r"(24.1). Then "
        r"$\displaystyle\varphi(x)=\sum_{k=1}^\infty\left\{\frac{\log k}{\sqrt{k}}-\frac{\log(k+x)}{(k+x)^{1/2}}\right\}$ "
        r"(24.2) for all $x>-1$.",
    ),
    rec(
        "RN-P1-C08-Entry24ii",
        r"Let $\varphi(x)$ be defined by (24.1). Then as $x\to\infty$, "
        r"$\displaystyle\varphi(x)-\left\{\sum_{k=1}^x\frac{1}{\sqrt{k}}-\zeta\!\left(\tfrac{1}{2}\right)\right\}\log x"
        r"\sim-4\sqrt{x}-\zeta\!\left(\tfrac{1}{2}\right)\sqrt{x}+\tfrac{1}{2}\pi+\tfrac{1}{2}\log(8\pi)"
        r"+\sum_{k=1}^\infty\frac{B_{2k}(\tfrac{1}{2})_{2k-1}H_{2k-2}(\tfrac{1}{2})}{(2k)!\,x^{2k-1/2}}$, "
        r"where $H_n(r)$ is defined by (21.2).",
    ),
    rec(
        "RN-P1-C08-Entry24iii",
        r"Let $\varphi(x)$ and $\psi(x)$ be defined by (24.2) and (24.7), respectively, for $x>-1$. "
        r"If $n$ is any positive integer, then "
        r"$\displaystyle\frac{1}{\sqrt{n}}\varphi(x)-\sum_{j=0}^{n-1}\varphi\!\left(\frac{x-j}{n}\right)"
        r"=\psi(x)\log n-\left(\tfrac{1}{2}n-1\right)c-\tfrac{1}{2}n\zeta\!\left(\tfrac{1}{2}\right)\log n$, "
        r"where $c$ is given by (24.4).",
    ),
    rec(
        "RN-P1-C08-Entry24iv",
        r"Let $\varphi(x)$ and $\psi(x)$ be defined by (24.2) and (24.7), respectively. "
        r"If $0<x<1$, then "
        r"$\displaystyle\varphi(x-1)+\varphi(-x)-2c+(\gamma+\tfrac{1}{2}\pi+\log(8\pi))"
        r"\left\{\psi(x-1)+\psi(-x)-2\zeta\!\left(\tfrac{1}{2}\right)\right\}"
        r"=2\sum_{k=1}^\infty\frac{\log k}{\sqrt{k}}\cos(2\pi kx)$, "
        r"where $c$ is given by (24.4).",
    ),
    rec(
        "RN-P1-C08-Entry24v",
        r"Under the same hypotheses as Entry 24(iv), "
        r"$\displaystyle\varphi(x-1)-\varphi(-x)+(\gamma-\tfrac{1}{2}\pi+\log(8\pi))"
        r"\left\{\psi(x-1)-\psi(-x)\right\}"
        r"=2\sum_{k=1}^\infty\frac{\log k}{\sqrt{k}}\sin(2\pi kx)$.",
    ),
    rec(
        "RN-P1-C08-Entry24-Example02i",
        r"If $c$ is defined by (24.4), then $c\approx 3.92265$.",
    ),
    rec(
        "RN-P1-C08-Entry24-Example02ii",
        r"If $c$ is defined by (24.4), then "
        r"$\displaystyle c\approx 4-\sum_{k=1}^\infty\frac{B_{2k}(\tfrac{1}{2})_{2k-1}H_{2k-2}(\tfrac{1}{2})}{(2k)!}$ "
        r"(24.13), "
        r"where the sign $\approx$ indicates semiconvergent interpretation.",
    ),
]
