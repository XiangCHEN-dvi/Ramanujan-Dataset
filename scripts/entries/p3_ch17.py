"""Part III, Chapter 17 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C17 = ["fundamental-properties-of-elliptic-functions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C17}


CHAPTER_17 = [
    rec(
        "RN-P3-C17-Entry01",
        r"""Let $n$ and $x$ be real numbers with $0\le x<1$. Then $\displaystyle\int_0^{\pi/2}\frac{\cos\{(1-2n)\sin^{-1}(\sqrt{x}\sin\varphi)\}}{\sqrt{1-x\sin^2\varphi}}\,d\varphi=\frac{\pi}{2}\,{}_2F_1(1-n,n;1;x)$.""",
    ),
    rec(
        "RN-P3-C17-Entry01-Corollary01",
        r"""For any real number $n$, $\displaystyle\int_0^{\pi/2}\frac{\cos\{(1-2n)\sin^{-1}(\sin\varphi/\sqrt{2})\}}{\sqrt{1-\tfrac{1}{2}\sin^2\varphi}}\,d\varphi=\frac{\pi^{3/2}}{2\,\Gamma(\tfrac12-n)\,\Gamma(\tfrac32+2n)}$.""",
    ),
    rec(
        "RN-P3-C17-Entry01-Corollary02",
        r"""For $0<x<1$, let $\displaystyle U_x=\int_0^{\pi/2}\frac{\cos\{(1-2n)\sin^{-1}(\sqrt{x}\sin\varphi)\}}{\sqrt{1-x\sin^2\varphi}}\,d\varphi$. If $0<x<1$ and $n$ is nonintegral, then $\displaystyle\exp\!\left(-\frac{n\,U_{1-x}}{\sin(\pi n)}\right)=x\,\exp(\psi(n)+\psi(1-n)+2\gamma)$, where $\psi(x)=\Gamma'(x)/\Gamma(x)$ and $\gamma$ is Euler's constant.""",
    ),
    rec(
        "RN-P3-C17-Entry02i",
        r"""Define $\displaystyle F(x)=\exp\!\left(-\frac{\pi\,{}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;x)}{{}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;1-x)}\right)$ for $0<x<1$, extended by $F(0)=0$ and $F(1)=1$. If $0<x<1$, then $\displaystyle F(x)=\exp\!\left(\frac{\pi}{16\,{}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;x)}\sum_{k=1}^{\infty}\frac{1}{(k!)^2}\sum_{j=1}^{k}\frac{x^k}{2j(2j-1)}\right)$.""",
    ),
    rec(
        "RN-P3-C17-Entry02ii",
        r"""For $x\ge 0$, $\displaystyle x\,F(1-e^{-x})\approx\frac{x}{\sqrt{10+\sqrt{36+x^2}}}$ very nearly.""",
    ),
    rec(
        "RN-P3-C17-Entry02iii",
        r"""For $0<x<1$, $\log F(x)\,\log F(1-x)=\pi^2$.""",
    ),
    rec(
        "RN-P3-C17-Entry02iv",
        r"""$F(1-x)+F(1-1/x)=0$.""",
    ),
    rec(
        "RN-P3-C17-Entry02v",
        r"""$\displaystyle F(x^2)=\left\{F\!\left(\frac{4x}{(1+x)^2}\right)\right\}^2$.""",
    ),
    rec(
        "RN-P3-C17-Entry02vi",
        r"""If $|x|<\tfrac{1}{2}$, then $\displaystyle F\!\left(\frac{2x}{1+x}\right)=\frac{x}{8}+\frac{5x^3}{128}+\frac{3x^5}{214}+\frac{369x^7}{2^{18}}+\frac{4097x^9}{2^{21}}+\frac{1594895x^{11}}{2^{27}}+\cdots$.""",
    ),
    rec(
        "RN-P3-C17-Entry02vii",
        r"""For $x\ge 0$, $\displaystyle F(1-e^{-8x})=\frac{x}{2}-\frac{x^3}{6}+\frac{31x^5}{240}-\frac{661x^7}{5040}+\frac{219677x^9}{1451520}+\cdots$.""",
    ),
    rec(
        "RN-P3-C17-Entry02-Example01",
        r"""$F(0)=0$, $F(\tfrac{1}{2})=e^{-\pi}$, $F(1)=1$, $F((\sqrt{2}-1)^2)=e^{-\pi\sqrt{2}}$, and $F((\sqrt{2}-1)^4)=e^{-2\pi}$.""",
    ),
    rec(
        "RN-P3-C17-Entry02-Example02",
        r"""If $0\le x<1$, then $\displaystyle F\!\left(1-\exp\!\left(\frac{-8x}{1-x^2}\right)\right)=\frac{x}{2}+\frac{x^3}{6}+\frac{31x^5}{240}+\frac{37x^7}{2520}+\frac{5981x^9}{1451520}+\cdots$.""",
    ),
    rec(
        "RN-P3-C17-Entry03",
        r"""If $|q|<1$ and $\displaystyle\varphi(q)=\sum_{k=-\infty}^{\infty}q^{k^2}$, then $\displaystyle\varphi^2(q)={}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;\frac{\varphi^4(-q)}{\varphi^4(q)}\right)$.""",
    ),
    rec(
        "RN-P3-C17-Entry04i",
        r"""If $m$ is a nonnegative integer and $n=2^m$, then $\displaystyle\frac{F\!\left(\dfrac{\varphi^4(-q)}{\varphi^4(q)}\right)}{F\!\left(\dfrac{\varphi^4(-q^n)}{\varphi^4(q^n)}\right)}=n\,\frac{{}_2F_1(\tfrac12,\tfrac12;1;\varphi^4(-q)/\varphi^4(q))}{{}_2F_1(\tfrac12,\tfrac12;1;\varphi^4(-q^n)/\varphi^4(q^n))}$.""",
    ),
    rec(
        "RN-P3-C17-Entry04ii",
        r"""If $n=2^m$, as above, then $\displaystyle\log F\!\left(\frac{\varphi^4(-q)}{\varphi^4(q)}\right)=\frac{1}{n}\log F\!\left(\frac{\varphi^4(-q^n)}{\varphi^4(q^n)}\right)$.""",
    ),
    rec(
        "RN-P3-C17-Entry05",
        r"""(Inversion formula.) For $|q|<1$, $\displaystyle F\!\left(1-\frac{\varphi^4(-q)}{\varphi^4(q)}\right)=q$, where $\displaystyle\varphi(q)=\sum_{k=-\infty}^{\infty}q^{k^2}$ and $F$ is defined by (2.1).""",
    ),
    rec(
        "RN-P3-C17-Entry06",
        r"""Let $\displaystyle F(x)=\exp\!\left(-\frac{\pi\,{}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;x)}{{}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;1-x)}\right)$ and $\displaystyle\varphi(q)=\sum_{k=-\infty}^{\infty}q^{k^2}$. Then $\varphi^2(F(x))={}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;x)$. If furthermore $q=e^{-y}$, $\displaystyle z={}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;x)$, and $\displaystyle y=\frac{\pi\,{}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;1-x)}{{}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;x)}$, then $\varphi^2(e^{-y})=z$.""",
    ),
    rec(
        "RN-P3-C17-Entry06-Corollary",
        r"""Let $\alpha,\beta>0$ with $\alpha\beta=\pi$. Then $\displaystyle\frac{\varphi(e^{-\alpha^2})}{\varphi(e^{-\beta^2})}=\sqrt{\frac{\alpha}{\beta}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry06-Example01",
        r"""$\displaystyle\varphi^2(e^{-\pi})={}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;\tfrac{1}{2}\right)=\frac{\pi}{\Gamma(\tfrac{1}{4})^2}$.""",
    ),
    rec(
        "RN-P3-C17-Entry06-Example02",
        r"""$\displaystyle\varphi(e^{-\pi\sqrt{2}})=\frac{\Gamma(\tfrac{1}{4})^2}{2^{3/4}\sqrt{\pi}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry06-Example03",
        r"""$\displaystyle\varphi^2(e^{-2\pi})=\frac{\sqrt{2}\,\Gamma(\tfrac{1}{4})^4}{8(2-\sqrt{2})\,\pi}$.""",
    ),
    rec(
        "RN-P3-C17-Entry06-Example04",
        r"""$\displaystyle\frac{1}{2\sqrt{2}}\varphi(e^{-2\pi})+2\sqrt{2}\sum_{k=1}^{\infty}(-1)^k k\,e^{-2\pi k^2}=-\frac{\pi}{2\sqrt{2}}\varphi(e^{-\pi/2})+2\sqrt{\pi}\sum_{k=1}^{\infty}(-1)^k k\,e^{-\pi k^2/2}$.""",
    ),
    rec(
        "RN-P3-C17-Entry07i",
        r"""If $\sin\alpha=\sqrt{x}\sin\beta$, then $\displaystyle\int_0^{\alpha}\frac{d\varphi}{\sqrt{x-\sin^2\varphi}}=\int_0^{\beta}\frac{d\varphi}{\sqrt{1-x\sin^2\varphi}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry07ii",
        r"""If $\displaystyle\tan\alpha=\sqrt{\frac{1-x}{1+x}}\tan\beta$, then $\displaystyle\int_0^{\alpha}\frac{d\varphi}{\sqrt{1-x\cos^2\varphi}}=\int_0^{\beta}\frac{d\varphi}{\sqrt{1-x\sin^2\varphi}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry07iii",
        r"""If $\displaystyle\tan\alpha=\sqrt{\frac{a-b}{1-b}}\tan\beta$, then $\displaystyle\int_0^{\alpha}\frac{d\varphi}{\sqrt{a-b\sin^2\varphi}}=\sqrt{\frac{1-b}{1-a}}\int_0^{\beta}\frac{d\varphi}{\sqrt{(1-a\sin^2\varphi)(1-b\sin^2\varphi)}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry07iv",
        r"""If $\displaystyle\tan\alpha=\frac{1-x}{1+x}\tan\beta$, then $\displaystyle\int_0^{\alpha}\frac{d\varphi}{\sqrt{1+x\cos 2\varphi}}=\int_0^{\beta}\frac{d\varphi}{\sqrt{1-x^2\sin^4\varphi}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry07v",
        r"""If $\displaystyle\cot\alpha\cot\beta=\frac{1-x}{2}$, then $\displaystyle\int_0^{\alpha}\frac{d\varphi}{\sqrt{1-x\sin^2\varphi}}+\int_0^{\beta}\frac{d\varphi}{\sqrt{1-x\sin^2\varphi}}=\frac{\pi}{2}\,{}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;x)$.""",
    ),
    rec(
        "RN-P3-C17-Entry07vi",
        r"""If $\displaystyle\cot\alpha\tan(\beta/2)=\sqrt{1-x\sin^2\alpha}$, then $\displaystyle 2\int_0^{\alpha}\frac{d\varphi}{\sqrt{1-x\sin^2\varphi}}=\int_0^{\beta}\frac{d\varphi}{\sqrt{1-x\sin^2\varphi}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry07vii",
        r"""If $\alpha=\log(\tan(\tfrac{\pi}{4}+\tfrac{\beta}{2}))$, then $\displaystyle\int_0^{i\alpha}\frac{d\varphi}{\sqrt{\sin^2\varphi}}=i\int_0^{\beta}\frac{d\varphi}{\sqrt{1-(1-x)\sin^2\varphi}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry07viii",
        r"""Let $\displaystyle U=\int_0^{\alpha}\frac{d\varphi}{\sqrt{1-x\sin^2\varphi}}$, $\displaystyle V=\int_0^{\beta}\frac{d\varphi}{\sqrt{1-x\sin^2\varphi}}$, and $\displaystyle W=\int_0^{\gamma}\frac{d\varphi}{\sqrt{1-x\sin^2\varphi}}$. If $U+V=W$, then: (a) $\displaystyle\tan\gamma=\frac{\sin\alpha\sqrt{1-x\sin^2\beta}+\sin\beta\sqrt{1-x\sin^2\alpha}}{\cos\alpha+\cos\beta}$; (b) $\displaystyle\gamma=\tan^{-1}(\tan\alpha\sqrt{1-x\sin^2\beta})+\tan^{-1}(\tan\beta\sqrt{1-x\sin^2\alpha})$; (c) $\displaystyle\cot\alpha\cot\beta=\cos\gamma+\sin\alpha\sin\beta\sqrt{1-x\sin^2\gamma}$; (d) $\displaystyle\frac{\sqrt{\sin s\sin(s-\alpha)\sin(s-\beta)\sin(s-\gamma)}}{\sin\alpha\sin\beta\sin\gamma}=\frac{1}{2}$, where $2s=\alpha+\beta+\gamma$.""",
    ),
    rec(
        "RN-P3-C17-Entry07ix",
        r"""If $|x|<1$, then $\displaystyle\frac{1}{2}\int_0^{\pi/2}\frac{d\varphi}{\sqrt{1+x\sin\varphi}}=\int_0^{\pi/2}\frac{\cos^{-1}(x\sin^2\varphi)\,d\varphi}{\sqrt{1-x^2\sin^4\varphi}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry07x",
        r"""If $|x|<1$, then $\displaystyle\int_0^{\pi/2}\int_0^{\pi/2}\frac{d\theta\,d\varphi}{\sqrt{(1-x\sin^2\theta)(1-x\sin^2\theta\sin^2\varphi)}}=\left(\int_0^{\pi/2}\frac{d\varphi}{\sqrt{1-x\sin^4\varphi}}\right)^{\!2}$.""",
    ),
    rec(
        "RN-P3-C17-Entry07xi",
        r"""If $|x|<1$, then $\displaystyle\int_0^{\pi/2}\int_0^{\pi/2}\frac{x\sin\varphi\,d\theta\,d\varphi}{\sqrt{(1-x^2\sin^2\varphi)(1-x^2\sin^2\theta\sin^2\varphi)}}=\frac{1}{2}\left(\int_0^{\pi/2}\frac{d\varphi}{\sqrt{1-\tfrac{1}{2}(1+x)\sin^2\varphi}}\right)^{\!2}-\frac{1}{2}\left(\int_0^{\pi/2}\frac{d\varphi}{\sqrt{1-\tfrac{1}{2}(1-x)\sin^2\varphi}}\right)^{\!2}$.""",
    ),
    rec(
        "RN-P3-C17-Entry07xii",
        r"""If $(1+x\sin^2\alpha)\sin\beta=(1+x)\sin\alpha$, then $\displaystyle\int_0^{\alpha}\frac{d\varphi}{\sqrt{1-x^2\sin^2\varphi}}=\frac{1+x}{\sqrt{1-x^2\sin^2\beta}}\int_0^{\beta}\frac{d\varphi}{\sqrt{1-\dfrac{4x}{(1+x)^2}\sin^2\varphi}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry07xiii",
        r"""If $x\sin\alpha=\sin(2\varphi-\alpha)$, then $\displaystyle(1+x)\int_0^{\alpha}\frac{d\varphi}{\sqrt{1-x^2\sin^2\varphi}}=2\int_0^{\beta}\frac{d\varphi}{\sqrt{1-\dfrac{4x}{(1+x)^2}\sin^2\varphi}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry08i",
        r"""$\displaystyle\varphi(q)\varphi(q^2)=1-2\sum_{k=1}^{\infty}\frac{(-1)^{k(k+1)/2}q^{2k-1}}{1-q^{2k-1}}$, where $\displaystyle\varphi(q)=\sum_{k=-\infty}^{\infty}q^{k^2}$.""",
    ),
    rec(
        "RN-P3-C17-Entry08ii",
        r"""$\displaystyle\varphi(q)\varphi(q^4)=1+2\sum_{k=1}^{\infty}\frac{q^k}{1+q^{4k}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry08iii",
        r"""$\displaystyle\varphi(q)\varphi(q^3)=1+2\sum_{k=1}^{\infty}\frac{q^k+q^{3k}}{1+q^{4k}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry08iv",
        r"""$\displaystyle\varphi(q)\varphi(q^3)=1+2\sum_{k=1}^{\infty}\frac{(k/3)\,q^k}{1+(-q)^k}$, where $(k/3)$ denotes the Legendre symbol.""",
    ),
    rec(
        "RN-P3-C17-Entry08v",
        r"""$\displaystyle\varphi^2(-q)=1+4\sum_{k=1}^{\infty}\frac{(-1)^k q^{k(k+1)/2}}{1+q^k}$.""",
    ),
    rec(
        "RN-P3-C17-Entry08vi",
        r"""$\displaystyle\psi^2(q)=\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)q^{k(k+1)/2}}{1-q^{2k+1}}$, where $\displaystyle\psi(q)=\sum_{k=0}^{\infty}q^{k(k+1)/2}$.""",
    ),
    rec(
        "RN-P3-C17-Entry08vii",
        r"""$\displaystyle\sum_{k=1}^{\infty}\frac{kq^k}{k^2(1-q^k)}=\sum_{k=1}^{\infty}\frac{(-1)^{k+1}q^{k(k+1)/2}}{(1-q^k)(1-q^{k+1})}$.""",
    ),
    rec(
        "RN-P3-C17-Entry08viii",
        r"""$\displaystyle\sum_{k=1}^{\infty}\frac{1+q^k}{k^2(1-q^k)}=2\sum_{k=1}^{\infty}\frac{(-1)^{k+1}q^{k(k+1)/2}}{(1-q^k)^2}$.""",
    ),
    rec(
        "RN-P3-C17-Entry08ix",
        r"""$\displaystyle\varphi^2(-q)f(-q)=\sum_{k=-\infty}^{\infty}(6k+1)q^{(3k^2+k)/2}$, where $\displaystyle f(a,b)=\sum_{k=-\infty}^{\infty}a^{k(k+1)/2}b^{k(k-1)/2}$.""",
    ),
    rec(
        "RN-P3-C17-Entry08x",
        r"""$\displaystyle\psi(q^2)f(-q)=\sum_{k=-\infty}^{\infty}(3k+1)q^{3k^2+2k}$, where $\displaystyle\psi(q)=\sum_{k=0}^{\infty}q^{k(k+1)/2}$.""",
    ),
    rec(
        "RN-P3-C17-Entry08xi",
        r"""$\displaystyle f(-q)f(-q^2)=\varphi(-q)\psi(q)$.""",
    ),
    rec(
        "RN-P3-C17-Entry08xii",
        r"""$\displaystyle\frac{f(-q)}{f(-q^4)}=\frac{\varphi(-q)\psi(q)}{\varphi^2(-q^2)\psi(q^2)}=\frac{\varphi(q)\psi(-q)}{\varphi^2(-q^2)\psi(q^2)}$.""",
    ),
    rec(
        "RN-P3-C17-Entry08-Example",
        r"""$\displaystyle\psi(q^2)f^2(-q)+2q\psi(q^8)f^2(-q^4)=\varphi^2(-q^8)f(-q^8)$.""",
    ),
    rec(
        "RN-P3-C17-Entry09i",
        r"""Recall that $x$, $y$, and $z$ are related by (2.1) and (6.2)--(6.4). Then $\displaystyle\frac{dy}{dx}=x(1-x)z^2$.""",
    ),
    rec(
        "RN-P3-C17-Entry09ii",
        r"""$\displaystyle\frac{dz}{dx}=\frac{z}{2x(1-x)}$.""",
    ),
    rec(
        "RN-P3-C17-Entry09iii",
        r"""For $n>0$, $\displaystyle\int_0^x t^{n-1}z(t)\,dt=\frac{x^n}{n}\,{}_3F_2\!\left(\tfrac12,\tfrac12,n;1,n+1;x\right)$, where $z(t)={}_2F_1(\tfrac12,\tfrac12;1;t)$.""",
    ),
    rec(
        "RN-P3-C17-Entry09iv",
        r"""Let $\displaystyle L(e^{-y})=1-24\sum_{k=1}^{\infty}\frac{k}{e^{ky}-1}$. Then $\displaystyle\frac{dz}{dy}=1-24\sum_{k=1}^{\infty}\frac{k}{e^{ky}-1}=(1-2x)z^2+6x(1-x)z\,\frac{dx}{dy}$.""",
    ),
    rec(
        "RN-P3-C17-Entry09-Example",
        r"""For $y>0$, $\displaystyle e^{-11y}=x^{11}\!\left(1+\frac{11}{1}x+\frac{55}{12}x^2+\frac{385}{40}x^3+\cdots\right)$.""",
    ),
    rec(
        "RN-P3-C17-Entry10i",
        r"""If $x$, $y$, and $z$ are related by (6.2)--(6.4), then $\varphi(e^{-y})=\sqrt{z}$.""",
    ),
    rec(
        "RN-P3-C17-Entry10ii",
        r"""$\varphi(-e^{-y})=\sqrt{z}(1-x)^{1/4}$.""",
    ),
    rec(
        "RN-P3-C17-Entry10iii",
        r"""$\varphi(-e^{-2y})=\sqrt{z}(1-x)^{1/8}$.""",
    ),
    rec(
        "RN-P3-C17-Entry10iv",
        r"""$\varphi(e^{-2y})=\sqrt[4]{\tfrac{1}{2}(1+\sqrt{1-x})}\,\sqrt{z}$.""",
    ),
    rec(
        "RN-P3-C17-Entry10v",
        r"""$\varphi(e^{-4y})=\tfrac{1}{\sqrt{2}}\sqrt{z}\bigl(1+(1-x)^{1/4}\bigr)$.""",
    ),
    rec(
        "RN-P3-C17-Entry10vi",
        r"""$\varphi(e^{-y/2})=\sqrt{z}(1+\sqrt{x})^{1/2}$.""",
    ),
    rec(
        "RN-P3-C17-Entry10vii",
        r"""$\varphi(-e^{-y/2})=\sqrt{z}(1-\sqrt{x})^{1/2}$.""",
    ),
    rec(
        "RN-P3-C17-Entry10viii",
        r"""$\varphi(e^{-y/4})=\sqrt{z}(1+x^{1/4})$.""",
    ),
    rec(
        "RN-P3-C17-Entry10ix",
        r"""$\varphi(-e^{-y/4})=\sqrt{z}(1-x^{1/4})$.""",
    ),
    rec(
        "RN-P3-C17-Entry11i",
        r"""$\displaystyle\psi(e^{-y})=\sqrt[4]{z(xe^y)}$, where $\displaystyle\psi(q)=\sum_{k=0}^{\infty}q^{k(k+1)/2}$.""",
    ),
    rec(
        "RN-P3-C17-Entry11ii",
        r"""$\displaystyle\psi(-e^{-y})=\sqrt[4]{z\,x(1-x)e^y}$.""",
    ),
    rec(
        "RN-P3-C17-Entry11iii",
        r"""$\displaystyle\psi(e^{-2y})=\tfrac{1}{2}\sqrt[4]{zxe^y}$.""",
    ),
    rec(
        "RN-P3-C17-Entry11iv",
        r"""$\displaystyle\psi(e^{-4y})=\tfrac{1}{2}\sqrt[4]{z\bigl(1-\tfrac{1}{4}x\bigr)e^y}$.""",
    ),
    rec(
        "RN-P3-C17-Entry11v",
        r"""$\displaystyle\psi(e^{-8y})=\tfrac{1}{4}\sqrt{z\bigl\{1-(1-x)^{1/4}\bigr\}e^y}$.""",
    ),
    rec(
        "RN-P3-C17-Entry11vi",
        r"""$\displaystyle\psi(e^{-y/2})=\sqrt[4]{z\bigl\{\tfrac{1}{2}(1+\sqrt{x})\bigr\}^2(xe^y)^{1/16}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry11vii",
        r"""$\displaystyle\psi(-e^{-y/2})=\sqrt[4]{z\bigl\{\tfrac{1}{2}(1-\sqrt{x})\bigr\}^2(xe^y)^{1/16}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry11viii",
        r"""$\displaystyle\psi(e^{-y/4})=\sqrt{z}(1+x^{1/4})^{1/2}\bigl\{\tfrac{1}{2}(1+\sqrt{x})\bigr\}^{1/8}(xe^y)^{1/32}$.""",
    ),
    rec(
        "RN-P3-C17-Entry11ix",
        r"""$\displaystyle\psi(-e^{-y/4})=\sqrt{z}(1-x^{1/4})^{1/2}\bigl\{\tfrac{1}{2}(1+\sqrt{x})\bigr\}^{1/8}(xe^y)^{1/32}$.""",
    ),
    rec(
        "RN-P3-C17-Entry12i",
        r"""Let $\displaystyle f(a,b)=\sum_{k=-\infty}^{\infty}a^{k(k+1)/2}b^{k(k-1)/2}$ and $\displaystyle\chi(q)=\frac{(-q;q^2)_\infty}{(q;q^2)_\infty}$. Then $\displaystyle f(e^{-y})=\sqrt[6]{z^2\bigl\{x(1-x)e^y\bigr\}^{1/24}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry12ii",
        r"""$\displaystyle f(-e^{-y})=\sqrt[6]{z^2(1-x)^{1/6}(xe^y)^{1/24}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry12iii",
        r"""$\displaystyle f(-e^{-2y})=\sqrt[3]{z\bigl\{x(1-x)e^y\bigr\}^{1/12}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry12iv",
        r"""$\displaystyle f(-e^{-4y})=\sqrt[3]{z^4(1-x)^{1/24}(xe^y)^{1/6}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry12v",
        r"""$\displaystyle\chi(e^{-y})=2^{1/6}\bigl\{x(1-x)e^y\bigr\}^{-1/24}$.""",
    ),
    rec(
        "RN-P3-C17-Entry12vi",
        r"""$\displaystyle\chi(-e^{-y})=2^{1/6}(1-x)^{1/12}(xe^y)^{1/24}$.""",
    ),
    rec(
        "RN-P3-C17-Entry12vii",
        r"""$\displaystyle\chi(-e^{-2y})=2^{1/3}(1-x)^{1/24}(xe^y)^{1/12}$.""",
    ),
    rec(
        "RN-P3-C17-Entry13i",
        r"""Let $\displaystyle L(q)=1-24\sum_{k=1}^{\infty}\frac{kq^k}{1-q^k}$, $\displaystyle M(q)=1+240\sum_{k=1}^{\infty}\frac{k^3q^k}{1-q^k}$, and $\displaystyle N(q)=1-504\sum_{k=1}^{\infty}\frac{k^5q^k}{1-q^k}$ for $|q|<1$. Then $M(e^{-2y})=z^4(1-x+x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry13ii",
        r"""$N(e^{-2y})=z^6(1+x)(1-29x+x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry13iii",
        r"""$M(e^{-y})=z^4(1+14x+x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry13iv",
        r"""$N(e^{-y})=z^6(1+x)(1-34x+x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry13v",
        r"""$M(e^{-4y})=z^4(1-4x+16x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry13vi",
        r"""$N(e^{-4y})=z^6(1-4x)(1-4x-16x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry13vii",
        r"""If $x$ is changed to $\bigl(\tfrac{1-\sqrt{x}}{1+\sqrt{x}}\bigr)^2$, then $y$ is changed to $2y$.""",
    ),
    rec(
        "RN-P3-C17-Entry13viii",
        r"""$\displaystyle 2L(e^{-2y})-L(e^{-y})=1+24\sum_{k=1}^{\infty}\frac{k}{e^{ky}-1}=z^2(1+x)$.""",
    ),
    rec(
        "RN-P3-C17-Entry13ix",
        r"""$\displaystyle 2L(e^{-4y})-L(e^{-2y})=1+24\sum_{k=1}^{\infty}\frac{2k}{e^{2ky}-1}=z^2(1-\sqrt{x})$.""",
    ),
    rec(
        "RN-P3-C17-Entry13x",
        r"""$\displaystyle 2M(e^{-2y})-M(e^{-y})=1-240\sum_{k=1}^{\infty}\frac{k^3}{e^{ky}-1}=z^4(1-16x+x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry13xi",
        r"""$\displaystyle 2N(e^{-2y})-N(e^{-y})=1+504\sum_{k=1}^{\infty}\frac{k^5}{e^{ky}-1}=z^6(1+x)(1+29x+x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry13xii",
        r"""$\displaystyle 2M(e^{-4y})-M(e^{-2y})=1-240\sum_{k=1}^{\infty}\frac{(2k)^3}{e^{2ky}-1}=z^4(1-4x+16x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry13xiii",
        r"""$\displaystyle 2N(e^{-4y})-N(e^{-2y})=1+504\sum_{k=1}^{\infty}\frac{(2k)^5}{e^{2ky}-1}=z^6(1-4x)(1-4x-16x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry14i",
        r"""$\displaystyle 1-8\sum_{k=1}^{\infty}\frac{(-1)^{k-1}k}{e^{ky}+1}=z^2(1-x)$.""",
    ),
    rec(
        "RN-P3-C17-Entry14ii",
        r"""$\displaystyle 1+8\sum_{k=1}^{\infty}\frac{(-1)^{k-1}k^3}{e^{ky}+1}=z^6(1-x)(1-x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry14iii",
        r"""$\displaystyle 17-32\sum_{k=1}^{\infty}\frac{(-1)^{k-1}k^5}{e^{ky}+1}=z^{10}(1-x)(1-x^2)(31-46x+31x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry14iv",
        r"""$\displaystyle 255+480\sum_{k=1}^{\infty}\frac{(-1)^{k-1}k^7}{e^{ky}+1}=z^8(1-x)^2(17-32x+17x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry14v",
        r"""$\displaystyle 16M(e^{-2y})-M(e^{-y})=15\!\left(1-16\sum_{k=1}^{\infty}\frac{(-1)^{k-1}k^3}{e^{ky}-1}\right)=z^4(1-x)$.""",
    ),
    rec(
        "RN-P3-C17-Entry14vi",
        r"""$\displaystyle 64N(e^{-2y})-N(e^{-y})=63\!\left(1+8\sum_{k=1}^{\infty}\frac{(-1)^{k-1}k^5}{e^{ky}-1}\right)=z^6(1-x)(1-\tfrac{1}{4}x)$.""",
    ),
    rec(
        "RN-P3-C17-Entry14vii",
        r"""$\displaystyle 256M^2(e^{-2y})-M^2(e^{-y})=255\!\left(17-32\sum_{k=1}^{\infty}\frac{(-1)^{k-1}k^7}{e^{ky}-1}\right)=z^8(1-x)(17-17x+2x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry14viii",
        r"""$\displaystyle 1024M^2(e^{-2y})N(e^{-2y})-M^2(e^{-y})N(e^{-y})=1023\!\left(31+8\sum_{k=1}^{\infty}\frac{(-1)^{k-1}k^9}{e^{ky}-1}\right)=z^{10}(1-x)(1-x^2)(31-46x+31x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry14ix",
        r"""$\displaystyle 16M(e^{-4y})-M(e^{-2y})=15\!\left(1-16\sum_{k=1}^{\infty}\frac{(-1)^{k-1}k^3}{e^{2ky}-1}\right)=z^4(1-x)^2$.""",
    ),
    rec(
        "RN-P3-C17-Entry14x",
        r"""$\displaystyle 64N(e^{-4y})-N(e^{-2y})=63\!\left(1+8\sum_{k=1}^{\infty}\frac{(-1)^{k-1}k^5}{e^{2ky}-1}\right)=z^6(1-x)^2(1-\tfrac{1}{4}x)$.""",
    ),
    rec(
        "RN-P3-C17-Entry14xi",
        r"""$\displaystyle 256M^2(e^{-4y})-M^2(e^{-2y})=255\!\left(17-32\sum_{k=1}^{\infty}\frac{(-1)^{k-1}k^7}{e^{2ky}-1}\right)=z^8(1-x)^2(17-2x+17x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry14xii",
        r"""If $x$ is changed to $-x/(1-x)$, then $e^{-y}$ is changed to $-e^{-y}$.""",
    ),
    rec(
        "RN-P3-C17-Entry15i",
        r"""$\displaystyle\sum_{k=1}^{\infty}\frac{k^3}{\sinh(ky)}=\tfrac{1}{4}z^4x$.""",
    ),
    rec(
        "RN-P3-C17-Entry15ii",
        r"""$\displaystyle\sum_{k=1}^{\infty}\frac{k^5}{\sinh(ky)}=\tfrac{1}{4}z^6x(1+x)$.""",
    ),
    rec(
        "RN-P3-C17-Entry15iii",
        r"""$\displaystyle\sum_{k=1}^{\infty}\frac{k^7}{\sinh(ky)}=\tfrac{1}{8}z^8x(1+14x+x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry15iv",
        r"""$\displaystyle\sum_{k=1}^{\infty}\frac{k^9}{\sinh(ky)}=\tfrac{1}{8}z^{10}x(1+x)(1+29x+x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry15v",
        r"""$\displaystyle\sum_{k=1}^{\infty}\frac{k^3}{\sinh(2ky)}=\tfrac{1}{128}z^4x^2$.""",
    ),
    rec(
        "RN-P3-C17-Entry15vi",
        r"""$\displaystyle\sum_{k=1}^{\infty}\frac{k^5}{\sinh(2ky)}=\tfrac{1}{128}z^6x^2(1-4x)$.""",
    ),
    rec(
        "RN-P3-C17-Entry15vii",
        r"""$\displaystyle\sum_{k=1}^{\infty}\frac{k^7}{\sinh(2ky)}=\tfrac{1}{128}z^8x^2(1-8x+68x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry15viii",
        r"""$\displaystyle\sum_{k=1}^{\infty}\frac{k^9}{\sinh(2ky)}=\tfrac{1}{128}z^{10}x^2(1-4x)(1-4x+16x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry15ix",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{2k+1}{\sinh((2k+1)y)}=\tfrac{1}{4}z^2x$.""",
    ),
    rec(
        "RN-P3-C17-Entry15x",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(2k+1)^3}{\sinh((2k+1)y)}=\tfrac{1}{8}z^4x(1-4x)$.""",
    ),
    rec(
        "RN-P3-C17-Entry15xi",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(2k+1)^5}{\sinh((2k+1)y)}=\tfrac{1}{8}z^6x(1-x+x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry15xii",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(2k+1)^7}{\sinh((2k+1)y)}=\tfrac{1}{8}z^8x(1-\tfrac{1}{2}x)(1-x+\tfrac{1}{2}x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry15xiii",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{2k+1}{\sinh((2k+1)y/2)}=\tfrac{1}{2}z^2\sqrt{x}$.""",
    ),
    rec(
        "RN-P3-C17-Entry15xiv",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(2k+1)^3}{\sinh((2k+1)y/2)}=\tfrac{1}{4}z^4(1+x)\sqrt{x}$.""",
    ),
    rec(
        "RN-P3-C17-Entry15xv",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(2k+1)^5}{\sinh((2k+1)y/2)}=\tfrac{1}{4}z^6(1+14x+x^2)\sqrt{x}$.""",
    ),
    rec(
        "RN-P3-C17-Entry15xvi",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(2k+1)^7}{\sinh((2k+1)y/2)}=\tfrac{1}{4}z^8(1+x)(1+134x+x^2)\sqrt{x}$.""",
    ),
    rec(
        "RN-P3-C17-Entry16i",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)}{\cosh(\tfrac{1}{2}(2k+1)y)}=\tfrac{1}{2}z^2\sqrt{x(1-x)}$.""",
    ),
    rec(
        "RN-P3-C17-Entry16ii",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)^3}{\cosh(\tfrac{1}{2}(2k+1)y)}=\tfrac{1}{2}z^4(1-2x)\sqrt{x(1-x)}$.""",
    ),
    rec(
        "RN-P3-C17-Entry16iii",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)^5}{\cosh(\tfrac{1}{2}(2k+1)y)}=\tfrac{1}{2}z^6\{1-16x(1-x)\}\sqrt{x(1-x)}$.""",
    ),
    rec(
        "RN-P3-C17-Entry16iv",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)^7}{\cosh(\tfrac{1}{2}(2k+1)y)}=\tfrac{1}{2}z^8(1-2x)\{1-136x(1-x)\}\sqrt{x(1-x)}$.""",
    ),
    rec(
        "RN-P3-C17-Entry16v",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)^9}{\cosh(\tfrac{1}{2}(2k+1)y)}=\tfrac{1}{2}z^{10}\{1-1232x(1-x)+7936x^2(1-x)^2\}\sqrt{x(1-x)}$.""",
    ),
    rec(
        "RN-P3-C17-Entry16vi",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)^{11}}{\cosh(\tfrac{1}{2}(2k+1)y)}=\tfrac{1}{2}z^{12}(1-2x)\{1-11072x(1-x)+176896x^2(1-x)^2\}\sqrt{x(1-x)}$.""",
    ),
    rec(
        "RN-P3-C17-Entry16vii",
        r"""$\displaystyle\sum_{k=0}^{\infty}(-1)^k\tan^{-1}(e^{-(2k+1)y/2})=\tfrac{1}{2}\sin^{-1}\sqrt{x}$.""",
    ),
    rec(
        "RN-P3-C17-Entry16viii",
        r"""$\displaystyle\sum_{k=0}^{\infty}(-1)^k\tan^{-1}(e^{-(2k+1)y/4})=\tfrac{1}{2}\tan^{-1}x^{1/4}$.""",
    ),
    rec(
        "RN-P3-C17-Entry16ix",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{1}{\cosh((2k+1)y/2)}=\tfrac{1}{2}z\sqrt{x}$.""",
    ),
    rec(
        "RN-P3-C17-Entry16x",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(2k+1)^2}{\cosh(\tfrac{1}{2}(2k+1)y)}=\tfrac{1}{2}z^3\sqrt{x}$.""",
    ),
    rec(
        "RN-P3-C17-Entry16xi",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(2k+1)^4}{\cosh(\tfrac{1}{2}(2k+1)y)}=\tfrac{1}{2}z^5(1+4x)\sqrt{x}$.""",
    ),
    rec(
        "RN-P3-C17-Entry16xii",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(2k+1)^6}{\cosh(\tfrac{1}{2}(2k+1)y)}=\tfrac{1}{2}z^7\{1+11(4x)+(4x)^2\}\sqrt{x}$.""",
    ),
    rec(
        "RN-P3-C17-Entry16xiii",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(2k+1)^8}{\cosh(\tfrac{1}{2}(2k+1)y)}=\tfrac{1}{2}z^9\{1+102(4x)+57(4x)^2+(4x)^3\}\sqrt{x}$.""",
    ),
    rec(
        "RN-P3-C17-Entry17i",
        r"""$\displaystyle 1+2\sum_{k=1}^{\infty}\frac{1}{\cosh(ky)}=z$.""",
    ),
    rec(
        "RN-P3-C17-Entry17ii",
        r"""$\displaystyle\sum_{k=1}^{\infty}\frac{k^2}{\cosh(ky)}=\tfrac{1}{4}z^3x$.""",
    ),
    rec(
        "RN-P3-C17-Entry17iii",
        r"""$\displaystyle\sum_{k=1}^{\infty}\frac{k^4}{\cosh(ky)}=\tfrac{1}{8}z^5\!\left(\frac{x}{4}+\frac{x^2}{4}\right)$.""",
    ),
    rec(
        "RN-P3-C17-Entry17iv",
        r"""$\displaystyle\sum_{k=1}^{\infty}\frac{k^6}{\cosh(ky)}=\tfrac{1}{8}z^7\!\left(\frac{x}{4}+\frac{x^2}{4}+\frac{x^3}{4}\right)$.""",
    ),
    rec(
        "RN-P3-C17-Entry17v",
        r"""$\displaystyle\sum_{k=1}^{\infty}\frac{k^8}{\cosh(ky)}=\tfrac{1}{8}z^9\!\left(\frac{x}{4}+57\!\left(\frac{x}{4}\right)^{\!2}+102\!\left(\frac{x}{4}\right)^{\!3}+\left(\frac{x}{4}\right)^{\!4}\right)$.""",
    ),
    rec(
        "RN-P3-C17-Entry17vi",
        r"""$\displaystyle 1+4\sum_{k=0}^{\infty}\frac{(-1)^k}{e^{(2k+1)y}-1}=z$.""",
    ),
    rec(
        "RN-P3-C17-Entry17vii",
        r"""$\displaystyle 1-4\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)^2}{e^{(2k+1)y}-1}=z^3(1-x)$.""",
    ),
    rec(
        "RN-P3-C17-Entry17viii",
        r"""$\displaystyle 5-4\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)^4}{e^{(2k+1)y}-1}=z^5(5-x)(1-x)$.""",
    ),
    rec(
        "RN-P3-C17-Entry17ix",
        r"""$\displaystyle 61-4\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)^6}{e^{(2k+1)y}-1}=z^7(1-x)(61-46x+x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry17-Example01",
        r"""$\displaystyle q\psi^8(q)=\sum_{k=1}^{\infty}\frac{k^3 q^k}{1-q^{2k}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry17-Example02",
        r"""$\displaystyle e^{-y}\psi^8(e^{-y})=16z^4x$.""",
    ),
    rec(
        "RN-P3-C17-Entry17-Example03",
        r"""$\displaystyle e^{-y}\psi^4(e^{-2y})=16z^2x$ and $\displaystyle\psi^2(q^2)=\sum_{k=0}^{\infty}\frac{q^k}{1+q^{2k+1}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry17-Example04",
        r"""$\displaystyle\varphi^2(q)\psi^4(q)=\sum_{k=0}^{\infty}\frac{(2k+1)^2 q^k}{1+q^{2k+1}}$.""",
    ),
    rec(
        "RN-P3-C17-Entry17-Example05",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(2k+1)q^{2k+1}}{1+q^{2k+1}}=q^{1/2}\varphi^{1/2}(q)\{\varphi^{1/2}(q)-\varphi^{1/2}(-q)\}^{1/2}=q\varphi^{1/2}(q)\psi^{1/2}(q^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry17-Example06",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(2k+1)^5 q^{2k+1}}{1+q^{2k+1}}=z^6(1+x)(1+29x+x^2)$.""",
    ),
    rec(
        "RN-P3-C17-Entry18i",
        r"""If $n$ is a positive integer, then $\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)\cosh(\tfrac{1}{2}(2k+1)n\pi/\sqrt{3})}=\frac{\sqrt{3}}{24n}$.""",
    ),
    rec(
        "RN-P3-C17-Entry18ii",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)\cosh(\tfrac{1}{2}(2k+1)n\pi/\sqrt[4]{3})}=\frac{\sqrt[4]{3}}{24n}$.""",
    ),
    rec(
        "RN-P3-C17-Entry18iii",
        r"""$\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)^{6n-1}}{\cosh(\tfrac{1}{2}(2k+1)n\pi/\sqrt{3})}=0$ and $\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)^{6n-1}}{\cosh(\tfrac{1}{2}(2k+1)n\pi/\sqrt[4]{3})}=0$.""",
    ),
    rec(
        "RN-P3-C17-Entry18-Example01",
        r"""If the left side of Entry 16(iv) vanishes, then $x=\tfrac{1}{2}$ or $x(1-x)=\tfrac{1}{16}$, and $\displaystyle\chi(e^{-y})=2^{1/6}\{x(1-x)e^y\}^{-1/24}$.""",
    ),
    rec(
        "RN-P3-C17-Entry18-Example02",
        r"""If the left side of Entry 16(v) vanishes, then $x(1-x)^{-1}=616\pm 24\sqrt{645}$, and $\displaystyle\chi(e^{-y})=2^{1/6}\{x(1-x)e^y\}^{-1/24}$.""",
    ),
    rec(
        "RN-P3-C17-Entry18-Example03",
        r"""If the left side of Entry 16(vi) vanishes, then $x=\tfrac{1}{2}$ or $x(1-x)^{-1}=16$ or $11056$, and $\displaystyle\chi(e^{-y})=2^{1/6}\{x(1-x)e^y\}^{-1/24}$.""",
    ),
]
