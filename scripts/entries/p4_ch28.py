"""Part 4, Chapter 28 entries — curated LaTeX."""

from __future__ import annotations

TOPICS = ['integrals']


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS}


CHAPTER_28 = [

    rec(
        "RN-P4-C28-Entry01",
        r"If $n>0$, then $\displaystyle\int_0^\infty e^{-2x}\sin(nx)\cot x\,dx=2n^2\sum_{k=1}^\infty\frac{1}{4k^2+n^2}$.",
    )
,
    rec(
        "RN-P4-C28-Entry02",
        r"For $a>0$, $\displaystyle\int_0^\infty e^{-ax}\sin(ax)\coth x\,dx=\frac{1}{2a}+2\sum_{k=0}^\infty\frac{a}{a^2+(a+2k)^2}$.",
    )
,
    rec(
        "RN-P4-C28-Entry03",
        r"If $a>0$, then $\displaystyle\int_0^\infty e^{-ax}\sin(ax)\{\cot x+\coth x\}\,dx=\frac{\pi}{2\sinh(\pi a)}$.",
    )
,
    rec(
        "RN-P4-C28-Entry04",
        r"For $a,\beta>0$ with $\alpha\beta=4\pi^2$, define $\displaystyle I(a)=\int_0^\infty\frac{a^{a-1}x^{a-1}}{e^{4\pi x}-1}\,dx$. Then $I(\alpha)=I(\beta)$.",
    )
,
    rec(
        "RN-P4-C28-Entry05",
        r"With $I(a)$ as in Entry 4 and $\alpha\beta=4\pi^2$, Ramanujan asserts that $I(\alpha)\approx\frac{1}{2}\sqrt{\alpha}\,\Gamma(\alpha)\,\zeta(\alpha+1)(2\pi)^{-\alpha-1/2}$ agrees \"nearly\" with the asymptotic expansion obtained from Watson's lemma.",
    )
,
    rec(
        "RN-P4-C28-Entry06",
        r"Let $\alpha,\beta>0$, $\alpha\beta=4\pi^2$, and $m>1$. Define $\displaystyle I(\alpha)=\int_0^\infty\frac{\alpha^{\alpha-1}x^{m-1}}{e^{4\pi x/\beta}-1}\,dx$. As $\alpha\to0$, $I(\alpha)\sim(2\pi)^{(\alpha+m)/2}\alpha^{(\alpha-m)/2}\sum_{n=0}^\infty\frac{B_n\Gamma(m+n)\zeta(m+n)}{(2\pi)^n n!}\alpha^n$; as $\beta\to0$, the symmetric expansion holds with $\alpha$ and $\beta$ interchanged.",
    )
,
    rec(
        "RN-P4-C28-Entry07",
        r"If $n>0$, then $\displaystyle\int_0^\infty\frac{x\sin(2nx)}{e^{2\pi\sqrt{x}}-1}\,dx=\frac{n}{2}\sum_{k=0}^\infty{}'\,e^{-2n\sqrt{k}}\cos(2n\sqrt{k}\,\pi)$, where the prime indicates that the $k=0$ term is multiplied by $\tfrac12$.",
    )
,
    rec(
        "RN-P4-C28-Entry08",
        r"Let $\chi$ denote the primitive character modulo $4$. If $n>0$, then $\displaystyle\int_0^\infty\frac{x\sin(2nx)}{e^{2\pi\sqrt{x}}+1}\,dx=\frac{n}{2\pi}\sum_{k=1}^\infty\chi(k)\,e^{-n\sqrt{k}}\sin(n\sqrt{k}\,\pi)$.",
    )
,
    rec(
        "RN-P4-C28-Entry09",
        r"For nonzero real $\theta$, Ramanujan records divergent asymptotic series relating $\displaystyle\sum_{k=0}^\infty\frac{\theta^{2k+1}}{(2k+1)!}\left(\frac{\pi}{2\theta}\right)^{2k+1}$ to integrals of $\cos(\pi x^2)/(e^{\theta x^2}-1)$ and $\sin(\pi x^2)/(e^{\theta x^2}-1)$ as $\theta\to0$ and $\theta\to\infty$.",
    )
,
    rec(
        "RN-P4-C28-Entry10",
        r"With $\displaystyle\varphi(n)=\varphi^*(n/n)$ and $\displaystyle\varphi^*(n)=\int_0^\infty\frac{\cos(\pi nx)}{e^{n x^2}-1}\,dx$, for nonzero real $n$, $\displaystyle\int_0^\infty\frac{\sin(nx)}{e^{nx^2}-1}\,dx=\frac{1}{n}\left\{\frac{\pi}{2n}-\varphi(n)\right\}$.",
    )
,
    rec(
        "RN-P4-C28-Entry11",
        r"For $a>0$, with $\displaystyle\psi(n)=\frac{4\pi e^{-2\pi n^2}}{e^{2\pi n^2}-1}$ and $\displaystyle G(a)=\frac{2}{\cosh(2\pi a)-\cos(2\pi a)}$, $\displaystyle\int_0^\infty e^{-2\pi a^2 n}\,\psi(n)\,dn=\frac{1}{G(a)}$.",
    )
,
    rec(
        "RN-P4-C28-Entry12",
        r"Let $\varphi$ be as in Entry 10. The non-transcendental part of $\varphi(\pi n)$ for rational $n=a/b$ is expressible by finite trigonometric sums $\sum_k\sin(k^2\pi a/b)$ and $\sum_k\cos(k^2\pi a/b)$.",
    )
,
    rec(
        "RN-P4-C28-Entry13",
        r"If $\displaystyle\int_0^\infty f(n)\,dn=\sum_{k=1}^\infty e^{-2\pi k p}$ for $p>0$ and $\displaystyle f(n)=\frac{e^{-2\pi np}}{\sqrt{n}}$ with $|\arg p|<\pi/4$, then $f$ is the inverse Laplace transform of $e^{-2\pi p\sqrt{s}}/\sqrt{s}$.",
    )
,
    rec(
        "RN-P4-C28-Entry14",
        r"For $n>0$, with $\psi$ as in Entry 11, $\displaystyle\psi(n\pi)=\sum_{r=1}^\infty\sum_{j=0}^\infty\frac{2}{j!}\left\{\frac{(2r+j)\cos(\pi j(2r+j)/n)+j\sin(\pi j(2r+j)/n)}{(2r+j)!}\right\}e^{-2\pi(r+j/2-1/2)^2/n}$.",
    )
,
    rec(
        "RN-P4-C28-Entry15",
        r"For real $p,n,a$ with $0<p<a$ and $n<1$, $\displaystyle I(p,n,a):=\int_0^1 x^{n-1}(1-x^p)^a\,dx=\frac{\pi}{p\sin(\pi n)}\sum_{j=0}^\infty(-1)^j\frac{\Gamma(a+j+1)}{\Gamma(a+1+j/n)}\frac{1}{(p+j/n)(a+j/n)}$.",
    )
,
    rec(
        "RN-P4-C28-Entry16",
        r"$\displaystyle\int_0^\infty e^{-x^2}\sin(nx)\,dx=\frac{\sqrt{\pi}}{2}\,\Gamma(n)\sin(n\pi/4)$ for $\Re n>-1$, and $\displaystyle\int_0^\infty e^{-x^2}\cos(nx)\,dx=\frac{\sqrt{\pi}}{2}\,\Gamma(n)\cos(n\pi/4)$ for $\Re n>0$.",
    )
,
    rec(
        "RN-P4-C28-Entry17",
        r"If $a$ is real, $|a|<n$, and $n>0$, then $\displaystyle\int_0^\infty\frac{\sinh(ax)}{\sinh(\pi x)(n^2+x^2)}\,dx=\frac{\pi}{n}\int_0^\infty\frac{x^{n-1}}{1+2x\cos a+x^2}\,dx=\frac{\pi\sin(na)}{2n\sin(n\pi)}\sum_{k=1}^\infty\frac{(-1)^{k-1}\sin(ka)}{n+k}$.",
    )
,
    rec(
        "RN-P4-C28-Entry18",
        r"If $a,b,n>0$, then $\displaystyle\int_0^\infty\frac{\cos(nx)\log\!\left(\frac{b+x^2}{a+x^2}\right)}{x}\,dx=-\frac{\pi}{2n}\left(e^{-n\sqrt{b}}-e^{-n\sqrt{a}}\right)$.",
    )
,
    rec(
        "RN-P4-C28-Entry19",
        r"If $n>0$, then $\displaystyle\int_0^1\frac{x^{n-1}(1-x^n)}{1+x}\,dx=\sum_{k=0}^\infty(-1)^k\left\{\frac{1}{n+2k}-\frac{1}{n+2k+1}\right\}$.",
    )
,
    rec(
        "RN-P4-C28-Entry20",
        r"For $n>0$, $\displaystyle\int_0^\infty\frac{\sin(2nx)\,dx}{x(\cosh(\pi x)+\cos(\pi x))}=\frac{\pi}{4}\sum_{k=0}^\infty\frac{(-1)^k(1-e^{-(2k+1)\pi})\cos\{(2k+1)n\pi\}}{(2k+1)\cosh\{(2k+1)\pi/2\}}$.",
    )
,
    rec(
        "RN-P4-C28-Entry21",
        r"For $n>1$, $\displaystyle\int_0^\infty\frac{dx}{x(e^{2\pi x}+e^{-2\pi x})}=\frac{\pi}{4}-\frac{1}{2}\sum_{k=1}^\infty\frac{(-1)^k\,\chi(k)\,k^{-1/n}}{k^{1/n}+1}$, where $\chi$ is the primitive character modulo $4$ and the series defines $L(s)$ at $s=1/n$.",
    )
,
    rec(
        "RN-P4-C28-Entry22",
        r"Formally, $\displaystyle\varphi(x)\sim\sum_{k=0}^\infty\varphi^{(k)}(0)\,\frac{x^k}{k!}$ in Ramanujan's sense of termwise identification of integrals and series.",
    )
,
    rec(
        "RN-P4-C28-Entry23",
        r"As $a\to\infty$, $\displaystyle\int_0^\infty\frac{dx}{x(e^{ax}+e^{-ax})}\sim\sum_{k=0}^\infty(-k)^k a^{-k-1}$ (a formal divergent asymptotic series).",
    )
,
    rec(
        "RN-P4-C28-Entry24",
        r"Let $0<p<1$. If $x^{p-1}F(x)$ and $x^{-p}f(x)$ are absolutely integrable on $(0,\infty)$ and $\displaystyle\int_0^\infty F(ax)f(bx)\,dx=\frac{1}{ab}$ for all $a,b>0$ with $a+b=1$, then $\displaystyle\int_0^\infty x^{p-1}F(x)\,dx\int_0^\infty y^{-p}f(y)\,dy=\frac{\pi}{\sin(\pi p)}$.",
    )
,
    rec(
        "RN-P4-C28-Entry25",
        r"Under the hypotheses of Entry 24, $\displaystyle\int_0^\infty\varphi(x)\{F(nx)+F(-nx)\}\,dx=\int_0^\infty\psi(x)\{f(nx)+f(-nx)\}\,dx$.",
    )
,
    rec(
        "RN-P4-C28-Entry26",
        r"Let $a,b,m,n,p>0$ with $a/m=(n-b)/n=p$. If $x^{-p}F(x^m)$ and $x^{p-1}f(x^n)$ are absolutely integrable on $(0,\infty)$ and $\displaystyle\int_0^\infty F(ax^m)f(bx^n)\,dx=\frac{1}{ab}$ for all $a,b\ge0$ with $a+b\ne0$, then $\displaystyle I(a,b,m,n):=\int_0^\infty x^{p-1}F(x^m)\,dx\int_0^\infty y^{-p}f(y^n)\,dy=\frac{\pi}{mn\sin(\pi p)}$.",
    )
,
    rec(
        "RN-P4-C28-Entry27",
        r"If $a>0$ and $0\le b<2$, then $\displaystyle\int_0^\infty\frac{\sinh(bx)\sin(ax)}{e^{2x}-1}\,dx=\int_0^\infty e^{-ax}\cot x\sin(bx)\,dx$.",
    )
,
    rec(
        "RN-P4-C28-Entry28",
        r"Let $\displaystyle\varphi(x)=\sum_{k=0}^\infty a(k)x^k$ and $\displaystyle\psi(x)=\sum_{k=0}^\infty b(k)x^k$ near $x=0$, with $\lim_{x\to0}\varphi(x)=\lim_{x\to0}\psi(x)=0$ and $a(0)=b(0)$. If $a,b>0$, then $\displaystyle\int_0^\infty\{\varphi(ax)-\psi(bx)\}\,\frac{dx}{x}=\int_0^\infty\{\varphi(x)-\psi(x)\}\,\frac{dx}{x}$.",
    )
,
    rec(
        "RN-P4-C28-Entry29",
        r"Let $F(z)$ be analytic on $\Re z\ge0$ (except possibly $z=0$), with $F(z)=O(z^\alpha)$ as $z\to\infty$ for some $\alpha<1$ and $F(z)=O(z^\delta)$ as $z\to0$ for some $\delta>0$. For $\Re a>0$, define $\displaystyle\varphi(a)=\frac{1}{\pi}\int_0^\infty e^{-z/a}F(z)\,dz$. Then for $w>0$, $\displaystyle F(w)=\frac{1}{\pi}\int_0^\infty\frac{F(iw/u)+F(-iw/u)}{u^2+1}\,du$.",
    )
,
    rec(
        "RN-P4-C28-Entry30",
        r"If $n>0$ and $a$ is a positive integer, then for each nonnegative integer $k$, $\displaystyle\int_0^\infty\frac{\cos(nx)\,dx}{(2k+1)^2+x^2}=\frac{\pi}{2}\,\frac{\Gamma(1)\Gamma(a+\tfrac12)}{\Gamma(\tfrac12)\Gamma(a)\Gamma(a+1)}\,\frac{1}{(\tfrac12+k,a)}$.",
    )
,
    rec(
        "RN-P4-C28-Entry31",
        r"Let $m>0$ and $0<a<b+1$. Then $\displaystyle\int_0^\infty\int_0^\infty\frac{\cos(nx)\,dx\,dy}{(b+k+1)^{m}(x^2+y^2)^a}=\frac{\pi\,\Gamma(2a)\Gamma(b+1)}{2\,\Gamma(a)\Gamma(b+a+1)\Gamma(b-a+1)}\sum_{k=0}^\infty\frac{1}{(a+b+1,k)}$.",
    )
,
    rec(
        "RN-P4-C28-Entry32",
        r"If $\varphi(x)$ is continuous on $[0,\infty)$ and $\displaystyle\lim_{x\to\infty}\varphi(x)=\varphi(\infty)$ exists, then $\displaystyle\lim_{n\to0}n\int_0^\infty x^{n-1}\varphi(x)\,dx=\varphi(0)-\varphi(\infty)$.",
    )
,
    rec(
        "RN-P4-C28-Entry33",
        r"Let $\varphi(z)$ be analytic for $\Re z\le0$ and $n>0$. If contour integrals of $(-iz)^{n-1}\varphi(z)$ and $(iz)^{n-1}\varphi(z)$ over large rectangles in the left half-plane tend to $0$, then $\displaystyle\int_0^\infty x^{n-1}\{\varphi(ix)+\varphi(-ix)\}\,dx=2\cos(\pi n/2)\int_0^\infty x^{n-1}\varphi(x)\,dx$.",
    )
,
    rec(
        "RN-P4-C28-Entry34",
        r"Under the hypotheses of Entry 33 and $n>0$, $\displaystyle\int_0^\infty x^{n-1}\{\varphi(ix)-\varphi(-ix)\}\,dx=-2i\sin(\pi n/2)\int_0^\infty x^{n-1}\varphi(x)\,dx$.",
    )
,
    rec(
        "RN-P4-C28-Entry35",
        r"If for $\Re a>0$ and $r>-1$, $\displaystyle\int_0^\infty\varphi(z)e^{-az}\,dz=a^{-r-1}$, then for $z>0$, $\displaystyle\varphi(z)=\frac{z^r}{\Gamma(r+1)}$.",
    )
,
    rec(
        "RN-P4-C28-Entry36",
        r"For $n\in\mathbb{C}\setminus[-1,0]$, $\displaystyle\Li_2\!\left(1+\frac{1}{n}\right)+\Li_2(-n)=\frac{\pi^2}{6}+\frac12\Log^2 n+\Log(1+n)\Log n$, with principal values of logarithms.",
    )
,
    rec(
        "RN-P4-C28-Entry37",
        r"If $p,q,r,s$ are real with $p+qx\ne0$ and $r+sx\ne0$, then $\displaystyle\int\log(p+qx)\log(r+sx)\,dx$ can be evaluated in terms of $\Li_2$ and elementary functions.",
    )
,
    rec(
        "RN-P4-C28-Entry38",
        r"If $p,q,r,s$ are real with $p+qx\ne0$ and $r+sx\ne0$, then $\displaystyle\int\frac{\log(p+qx)}{r+sx}\,dx$ can be evaluated in terms of $\Li_2$ and elementary functions.",
    )
,
    rec(
        "RN-P4-C28-Entry39",
        r"We have $\Li_2(\tfrac13)-5\Li_2(\tfrac15)=\tfrac{\pi^2}{6}-\tfrac12\Log^2 3$; $\Li_2(-\tfrac25)+5\Li_2(\tfrac15)=-\tfrac{\pi^2}{10}+\Log 2\,\Log 3-\tfrac12\Log^2 2-\tfrac32\Log^2 3$; $\Li_2(\tfrac13)+3\Li_2(\tfrac25)=\tfrac{\pi^2}{6}+2\Log 2\,\Log 3-2\Log^2 2-\tfrac32\Log^2 3$; $\Li_2(-\tfrac23)-3\Li_2(\tfrac25)=-\tfrac{\pi^2}{6}+\tfrac52\Log^2 3$; $\Li_2(-\tfrac23)+\Li_2(\tfrac25)=-\tfrac32\Log^2\tfrac23$.",
    )
,
    rec(
        "RN-P4-C28-Entry40",
        r"$\displaystyle\int_0^1\frac{\log x}{1+x+x^2}\,dx=-\frac{\pi^2}{15}$.",
    )
,
    rec(
        "RN-P4-C28-Entry42",
        r"For $n>0$, $\displaystyle\int_0^\infty\frac{\cos(nx)}{x^2+1}\,dx=\frac{\pi}{2}e^{-n}$ and $\displaystyle\int_0^\infty\frac{n\sin(nx)}{x(x^2+1)}\,dx=\frac{\pi}{2}(1-e^{-n})$.",
    )
,
    rec(
        "RN-P4-C28-Entry43",
        r"For $n>0$, $\displaystyle\int_0^\infty e^{-x}x^{n-1}\,dx=\Gamma(n)$; $\displaystyle\int_{-\infty}^\infty e^{-x^2}x^{n-1}\,dx=\sqrt{\pi}\,\Gamma\!\left(\tfrac{n}{2}\right)$; $\displaystyle\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}\Gamma(z)n^{-z}\,dz=e^{-n}$; $\displaystyle\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}e^{sz}s^{-n}\,ds=\frac{x^{n-1}}{\Gamma(n)}$ for $x>0$.",
    )
,
    rec(
        "RN-P4-C28-Entry44",
        r"If $\displaystyle\int_0^\infty\varphi(t)t^{s-1}\,dt=\psi(s)$ converges absolutely on $\Re s=c$ and $\varphi(t)$ is a continuous function of bounded variation near $t=x>0$, then $\displaystyle\lim_{T\to\infty}\frac{1}{2\pi i}\int_{c-iT}^{c+iT}\psi(s)x^{-s}\,ds=\varphi(x)$ (Mellin inversion).",
    )
,
    rec(
        "RN-P4-C28-Entry45",
        r"Under certain conditions, if $\displaystyle\int_{-\infty}^\infty x^{n-1}\varphi(x)\,dx=\psi(n)$, then formally $\displaystyle\frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty}e^{nz}\psi(z)\,dz=\varphi(\log n)$.",
    )
,
    rec(
        "RN-P4-C28-Entry46",
        r"If $\varphi$ is absolutely integrable on $[0,R]$ for every $R>0$, $\displaystyle\int_0^\infty e^{-sx}\varphi(x)\,dx=\psi(s)$ converges absolutely for $\Re s=c$, and $\varphi(t)$ is of bounded variation near $t=x>0$, then $\displaystyle\varphi(x)=\lim_{T\to\infty}\frac{1}{2\pi i}\int_{c-iT}^{c+iT}e^{sx}\psi(s)\,ds$ (Laplace inversion).",
    )
,
    rec(
        "RN-P4-C28-Entry47",
        r"If $\varphi$ is absolutely integrable on every finite interval, $\displaystyle\int_{-\infty}^\infty e^{-sx}\varphi(x)\,dx=\psi(s)$ converges absolutely on $\Re s=c$, and $\varphi(t)$ is of bounded variation near $t=x$, then $\displaystyle\lim_{T\to\infty}\frac{1}{2\pi i}\int_{c-iT}^{c+iT}e^{sx}\psi(s)\,ds=\varphi(x)$ (bilateral Laplace inversion).",
    )
]
