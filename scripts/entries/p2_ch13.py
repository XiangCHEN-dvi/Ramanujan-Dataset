"""Part II, Chapter 13 — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C13 = ["integrals-and-asymptotic-expansions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C13}


CHAPTER_13 = [
    rec(
        "RN-P2-C13-Entry01",
        r"Let $n\ge 0$ and put $N=[n+1]$. Then, when the right side is meaningful, "
        r"Ramanujan defines "
        r"$\displaystyle\int_0^\infty x^{n-1} f(x)\,dx "
        r"=\int_0^\infty t^{n-1}\left\{f(t)-\sum_{k=0}^{N-1}\frac{f^{(k)}(0)}{k!}\,t^k\right\}dt$.",
    ),
    rec(
        "RN-P2-C13-Entry01-Example",
        r"Entry 1 is illustrated by "
        r"$\displaystyle\int_0^\infty \frac{e^{-x^2}-1+x^2}{x}\,dx=\frac{\sqrt{\pi}}{2}$.",
    ),
    rec(
        "RN-P2-C13-Entry01-Corollary",
        r"If $a,n>0$ and $b$ is real, then "
        r"$\displaystyle\int_0^\infty e^{-ax}x^{n-1}\cos(bx)\,dx"
        r"=(a^2+b^2)^{-n/2}\Gamma(n)\cos\bigl(n\tan^{-1}(b/a)\bigr)$ and "
        r"$\displaystyle\int_0^\infty e^{-ax}x^{n-1}\sin(bx)\,dx"
        r"=(a^2+b^2)^{-n/2}\Gamma(n)\sin\bigl(n\tan^{-1}(b/a)\bigr)$. "
        r"The same formulas hold for $n<0$, provided $n$ is not a negative integer.",
    ),
    rec(
        "RN-P2-C13-Entry02i",
        r"Let $\varphi$ have $m+1$ continuous derivatives. Then "
        r"$\displaystyle\int \varphi(x)e^{-nx}\,dx"
        r"=-e^{-nx}\sum_{k=0}^{m}\frac{\varphi^{(k)}(x)}{n^{k+1}}"
        r"+\frac{1}{n^{m+1}}\int \varphi^{(m+1)}(x)e^{-nx}\,dx$.",
    ),
    rec(
        "RN-P2-C13-Entry02ii",
        r"Let $\varphi$ have $m+1$ continuous derivatives. If $m$ is even, then "
        r"$\displaystyle\int \varphi(x)\cos(nx)\,dx"
        r"=\sin(nx)\sum_{k=0}^{m/2}\frac{(-1)^k\varphi^{(2k)}(x)}{n^{2k+1}}"
        r"+\cos(nx)\sum_{k=0}^{m/2-1}\frac{(-1)^k\varphi^{(2k+1)}(x)}{n^{2k+2}}"
        r"+\frac{(-1)^{m/2+1}}{n^{m+1}}\int \varphi^{(m+1)}(x)\sin(nx)\,dx$; "
        r"if $m$ is odd, the last term is "
        r"$\displaystyle\frac{(-1)^{(m+1)/2}}{n^{m+1}}\int \varphi^{(m+1)}(x)\cos(nx)\,dx$.",
    ),
    rec(
        "RN-P2-C13-Entry02iii",
        r"Let $\varphi$ have $m+1$ continuous derivatives. If $m$ is even, then "
        r"$\displaystyle\int \varphi(x)\sin(nx)\,dx"
        r"=\sin(nx)\sum_{k=0}^{m/2-1}\frac{(-1)^k\varphi^{(2k+1)}(x)}{n^{2k+2}}"
        r"-\cos(nx)\sum_{k=0}^{m/2}\frac{(-1)^k\varphi^{(2k)}(x)}{n^{2k+1}}"
        r"+\frac{(-1)^{m/2}}{n^{m+1}}\int \varphi^{(m+1)}(x)\cos(nx)\,dx$; "
        r"if $m$ is odd, the last term is "
        r"$\displaystyle\frac{(-1)^{(m+1)/2}}{n^{m+1}}\int \varphi^{(m+1)}(x)\sin(nx)\,dx$.",
    ),
    rec(
        "RN-P2-C13-Entry03",
        r"Let $n,x>0$, define $\theta=\tan^{-1}(n/x)$ and $r=(n^2+x^2)^{1/2}$, and let $m$ be a positive "
        r"integer. Then as $x\to\infty$, "
        r"$\displaystyle\int_{|x|}^\infty e^{-t^2}\cos(2nt)\,dt"
        r"=\frac{e^{-n^2}}{r}\sum_{k=0}^{m-1}\frac{(-1)^k}{r^{2k+1}}"
        r"\cos\bigl(2nx+(2k+1)\theta\bigr)+O(r^{-2m-1})$.",
    ),
    rec(
        "RN-P2-C13-Entry04",
        r"Suppose $\varphi$ is entire, $n$ is real, and the integrals and series below converge. Then "
        r"$\displaystyle\int_0^\infty e^{-x^2}\{e^{2nx}\varphi(x)+e^{-2nx}\varphi(-x)\}\,dx"
        r"=\int_0^\infty e^{n^2-x^2}\{\varphi(n+x)+\varphi(n-x)\}\,dx"
        r"=\sqrt{\pi}\sum_{k=0}^\infty\frac{\varphi^{(2k)}(n)}{2^{2k}k!}$.",
    ),
    rec(
        "RN-P2-C13-Entry04-Example",
        r"If $\varphi(x)=e^x$ in Entry 4, then "
        r"$\displaystyle\int_0^\infty e^{-x^2}\cosh\bigl((2n+1)x\bigr)\,dx"
        r"=\int_0^\infty e^{n^2+n-x^2}\cosh x\,dx=\frac{e^{n^2+n+1/4}}{2}$.",
    ),
    rec(
        "RN-P2-C13-Entry05",
        r"Let $\psi(s)$ satisfy the hypotheses of Hardy's interpolation theorem for some $\delta>\tfrac12$, "
        r"and put $\psi(s)=\sum_{k=0}^\infty A_k s^{2k+1}/\Gamma(s+1)$ and "
        r"$\Psi(x)=\sum_{k=0}^\infty A_k(-x)^k/k!$. Suppose that for $\alpha=2\delta>1$, "
        r"$x^{\alpha-1/2}\Psi(x^2)\in L(0,\infty)$. Then "
        r"$\displaystyle\int_0^\infty e^{-1/x^2}\Psi(x^2)\,dx"
        r"=\sqrt{\pi}\sum_{k=0}^\infty\frac{(-2)^k A_k}{k!}$.",
    ),
    rec(
        "RN-P2-C13-Entry06",
        r"Let $n>0$ and let $m$ be a positive integer. Then as $n\to\infty$, "
        r"$\displaystyle\int_0^\infty e^{-x}\left(1+\frac{x}{n}\right)^{n-h}dx"
        r"=\sum_{k=0}^{m-1}\frac{(-1)^k(-n+h)_k}{n^k}"
        r"+\frac{A_0}{n}+\frac{A_1}{n^2}+\cdots$, where "
        r"$A_0=-\dfrac{h}{3}+\displaystyle\int_0^\infty e^{-x}\left(1+\frac{x}{n}\right)^{n-h}dx"
        r"-\dfrac{(-1)^m\Gamma(-n+h)^m}{e^n\Gamma(n-h+1)\sqrt{2\pi n^h}}"
        r"\displaystyle\int_0^\infty e^{-x}\left(1+\frac{x}{n}\right)^{n-h-m}dx$, "
        r"$A_1=\dfrac{A_0}{2n-h}+\dfrac{2}{n^2}$, and so on.",
    ),
    rec(
        "RN-P2-C13-Entry07",
        r"Let $m>n+1$. If $m$ and $n$ tend to $\infty$ while $m-n$ remains bounded, then "
        r"$\displaystyle I(m,n):=\int_0^\infty\frac{(1+x/n)^n}{(1+x/m)^m}\,dx"
        r"=n\sum_{k=0}^\infty\frac{(m-n)_k}{(m-n)^k}+O(1)$. "
        r"Put $R=n(m-n)^{-2/m}$. If $m$, $n$, and $m-n$ tend to $\infty$, then "
        r"$\displaystyle I(m,n)=\frac{m^{m+1}\Gamma(n+1)\Gamma(m-n+1)}"
        r"{2n^n\Gamma(m+1)(m-n)^{m-n}}\left\{1+\sum_{k=1}^\infty A_k\right\}$, "
        r"where $A_k=O(mR^{1-k})$. Moreover "
        r"$A_1=\dfrac{2(m+n)}{3(m-n)}$, "
        r"$A_2=\dfrac{2(m+n)(m^2-25mn+n^2)}{135\,mn^2(m-n)^2}$, and "
        r"$A_3=\dfrac{2(m+n)(m^6-3m^5n-12m^4n^2+389m^3n^3-12m^2n^4-3mn^5+n^6)}"
        r"{25515\,m^3n^4(m-n)^4}$.",
    ),
    rec(
        "RN-P2-C13-Entry08",
        r"As $n\to\infty$, "
        r"$\displaystyle\int_0^\infty\left\{\frac{n^x\Gamma(n+1)}{\Gamma(n+x+1)}+e^{-x}\left(1+\frac{x}{n}\right)^n\right\}dx"
        r"=\frac{e^n\Gamma(n+1)}{n^n}+\frac{1}{12n+1}+O(n^{-3/2})$.",
    ),
    rec(
        "RN-P2-C13-Entry09",
        r"If $\displaystyle\varphi(m)=\int_0^\infty \frac{e^{-m^2x^2}}{1+x}\,dx$ and $|m|\ge |n|$, where $m$ and $n$ "
        r"are real, then "
        r"$\displaystyle\int_0^\infty \frac{e^{-m^2x^2}}{1+x^2}\cos(2mnx)\,dx"
        r"=\frac{e^{-n^2}}{2}\{\varphi(m+n)+\varphi(m-n)\}$.",
    ),
    rec(
        "RN-P2-C13-Entry10",
        r"Let $\alpha,\beta,\gamma,\delta$ be fixed real numbers with $\gamma>\delta\ge 0$. Assume that for some "
        r"$d>0$, $\varphi(x)$ is analytic and nonzero on $|x|\le d$, that $\varphi(x)$ and $\varphi'(x)$ are "
        r"positive for $x\ge -d$, and that $x\varphi'(x)\le M\varphi(x)$ for all $x\ge d$ and some $M>0$. "
        r"Let $h>0$. Then as $h\to 0$, "
        r"$\displaystyle S(h):=\sum_{k=0}^{[h^{-3/5}]}\sum_{j=1}^{[h^{-3/5}]}\frac{\varphi(h\alpha+hj\delta)}"
        r"{\varphi(h\beta+hj\gamma)}"
        r"\sim\frac{\sqrt{\pi}\,\varphi(0)}{\gamma-\delta}\left\{\frac{1}{h}"
        r"-\frac{\varphi(0)\varphi''(0)}{2(\gamma-\delta)}\sqrt{h}\right\}"
        r"+\frac{2h(\gamma-\delta)\varphi'(0)}{3}+\frac{\varphi'(0)^2}{\gamma-\delta}+O(\sqrt{h})$.",
    ),
    rec(
        "RN-P2-C13-Entry10-Corollary01",
        r"Let $n>0$. Then as $x\to\infty$, "
        r"$\displaystyle\sum_{k=0}^\infty\left\{\frac{x^k\Gamma(x+1)}{\Gamma(x+k+1)}\right\}^n"
        r"\sim\frac{\sqrt{\pi x^n}}{2n}\left\{1+\frac{1}{3n}+O(x^{-1/2})\right\}$.",
    ),
    rec(
        "RN-P2-C13-Entry10-Corollary02",
        r"If $n$ is a positive integer, then as $x\to\infty$, "
        r"$\displaystyle\sum_{k=0}^\infty\frac{(x^k)^n}{k!}"
        r"\sim\frac{\exp\left\{nx+\frac{n^2}{2x}-\frac{n^2-1}{24x}-\frac{(n^2-1)(n^2+23)}{1152n^2x^2}-\cdots\right\}}"
        r"{\sqrt{2\pi x}\,(n-1)/2}$.",
    ),
    rec(
        "RN-P2-C13-Entry11i",
        r"As $x\to\infty$, "
        r"$\displaystyle\sum_{k=0}^\infty\frac{(ex)_k}{k!}"
        r"\sim\exp\left\{x-\frac{1}{24x}-\frac{1}{48x^2}-\frac{7}{864x^3}-\frac{139}{51840x^4}-\cdots\right\}$.",
    ),
    rec(
        "RN-P2-C13-Entry11iii",
        r"$\displaystyle S:=\log 2\sum_{k=2}^\infty\frac{(-1)^k}{k\log k}"
        r"+\log^2 2\sum_{k=2}^\infty\frac{1}{k\log k\,\log(2k)}=1$.",
    ),
    rec(
        "RN-P2-C13-Entry11-Example",
        r"As $x\to\infty$, "
        r"$\displaystyle\sum_{k=0}^\infty\frac{\log(k+1)\,x^k}{k!}"
        r"\sim e^x\left\{\log x+\frac{1}{2x}+\frac{1}{12x^2}+\frac{1}{12x^3}+\frac{19}{120x^4}"
        r"+\frac{9}{20x^5}+\cdots\right\}$.",
    ),
    rec(
        "RN-P2-C13-Entry13",
        r"Let $\alpha,\beta,\gamma,\delta$ be any complex numbers. Then "
        r"$\displaystyle\int_0^\infty\frac{dx}{(x^2+\alpha^2)(x^2+\beta^2)(x^2+\gamma^2)(x^2+\delta^2)}"
        r"=\frac{\pi}{6\alpha\beta\gamma\delta(\alpha+\beta)(\beta+\gamma)(\gamma+\alpha)(\alpha+\delta)(\beta+\delta)(\gamma+\delta)}"
        r"\left\{(\alpha+\beta+\gamma+\delta)^3-(\alpha^3+\beta^3+\gamma^3+\delta^3)\right\}$.",
    ),
    rec(
        "RN-P2-C13-Entry13-Corollary",
        r"If $\alpha,\beta,\gamma,\delta$ are the roots of $x^4-px^3+qx^2-rx+s$, then "
        r"$\displaystyle\int_0^\infty\frac{dx}{(x^2+\alpha^2)(x^2+\beta^2)(x^2+\gamma^2)(x^2+\delta^2)}"
        r"=\frac{\pi(2s-ps+r)}{q-rip}$.",
    ),
    rec(
        "RN-P2-C13-Entry14",
        r"If $x$ is arbitrary and $a\ne 0,-1,-2,\ldots$, then "
        r"$\displaystyle\sum_{k=0}^\infty\frac{(-1)^k(2a)_k}{k!\{(a+k)^2+x^2\}}"
        r"=\frac{\Gamma^2(a)}{2^{2a-1}}\prod_{k=0}^\infty\left\{1+\left(\frac{x}{a+k}\right)^2\right\}^{-1}$.",
    ),
    rec(
        "RN-P2-C13-Entry14-Example",
        r"For $n,a>0$, "
        r"$\displaystyle\int_0^\infty \frac{\cos(nx)}{a^2+x^2}\,dx=\frac{\pi}{2a}e^{-na}$.",
    ),
    rec(
        "RN-P2-C13-Entry15",
        r"For $a>0$ and $n$ real, "
        r"$\displaystyle\int_0^\infty |\Gamma(a+ix)|^2\cos(2nx)\,dx"
        r"=\tfrac12\sqrt{\pi}\,\Gamma(a)\Gamma(a+\tfrac12)\,\operatorname{sech}^{2a}n$.",
    ),
    rec(
        "RN-P2-C13-Entry16i",
        r"For real $a$ and $n$ with $|a|<n$, "
        r"$\displaystyle\int_0^\infty \frac{\sinh(ax)}{\sinh(nx)}\cos(nx)\,dx=\frac{\sin a}{2\cosh n+\cos a}$.",
    ),
    rec(
        "RN-P2-C13-Entry16ii",
        r"For real $a$ and $n$ with $|a|<n$, "
        r"$\displaystyle\int_0^\infty \frac{\cosh(ax)}{\sinh(nx)}\sin(nx)\,dx=\frac{\sinh n}{2\cosh n+\cos a}$.",
    ),
    rec(
        "RN-P2-C13-Entry16iii",
        r"For $n>0$, "
        r"$\displaystyle\int_0^\infty \frac{\sin(nx)}{x(e^{2nx}-1)}\,dx=\frac{1}{2}\left(\frac{1}{e^n-1}-\frac{1}{n}\right)$.",
    ),
    rec(
        "RN-P2-C13-Entry16iv",
        r"For $n>0$, "
        r"$\displaystyle\int_0^\infty \frac{x^{2n-1}}{e^{2nx}-1}\,dx=\frac{(-1)^{n-1}B_{2n}}{4n}$, and "
        r"$\displaystyle\int_0^\infty \frac{x^{2n}}{\cosh(nx/2)}\,dx=(-1)^n E_{2n}$, "
        r"where $B_k$ and $E_k$ denote Bernoulli and Euler numbers.",
    ),
    rec(
        "RN-P2-C13-Entry17",
        r"Let $\varphi(z)$ be analytic for $a\le \operatorname{Re}(z)\le n$, where $a$ is a nonnegative integer. "
        r"Suppose $\lim_{y\to\infty}|\varphi(x\pm iy)|e^{-2\pi y}=0$ uniformly for $a\le x\le n$. Then "
        r"$\displaystyle\sum_{k=a}^{n}\varphi(k)=\int_a^{n}\varphi(u)\,du+\tfrac12\{\varphi(a)+\varphi(n)\}"
        r"-i\displaystyle\int_0^\infty\frac{\varphi(n+iu)-\varphi(n-iu)-\varphi(a+iu)+\varphi(a-iu)}"
        r"{e^{2\pi u}-1}\,du$.",
    ),
    rec(
        "RN-P2-C13-Entry17-Corollary",
        r"For each positive integer $n$, "
        r"$\displaystyle\log n!=n\log n-n+\tfrac12\log(2\pi n)"
        r"+\int_0^\infty \frac{\tan^{-1}(x/n)}{e^{2\pi x}-1}\,dx$.",
    ),
    rec(
        "RN-P2-C13-Entry18i",
        r"Let $t>0$, fix a positive integer $n$, set $x=tn$, and put $\varphi(z)=f(t+tz)-f(tz)$ for a "
        r"given function $f$. If $\varphi$ satisfies the hypotheses of Entry 17 with $a=0$, then "
        r"$f(x)+t\varphi(n)=\tfrac12\{f(0)+f(t)\}+\int_0^{n}\varphi(u)\,du"
        r"-i\displaystyle\int_0^\infty\frac{\varphi(n+iu)-\varphi(n-iu)-\varphi(iu)+\varphi(-iu)}"
        r"{e^{2\pi u}-1}\,du$.",
    ),
    rec(
        "RN-P2-C13-Entry18ii",
        r"Let $t>0$, fix an even positive integer $n=2m$, set $x=tn$, and define "
        r"$\varphi(z)=f(tz+t)+f(tz-t)$. If $\varphi$ satisfies the hypotheses of the lemma preceding "
        r"Entry 18(ii), then "
        r"$2f(x)=2(-1)^m f(0)+\displaystyle\int_0^\infty\frac{\varphi(n+iu)+\varphi(n-iu)}"
        r"{e^{\pi tu/2}+e^{-\pi tu/2}}\,du"
        r"-(-1)^m\displaystyle\int_0^\infty\frac{\varphi(iu)+\varphi(-iu)}"
        r"{e^{\pi tu/2}+e^{-\pi tu/2}}\,du$, "
        r"provided the integrals exist.",
    ),
    rec(
        "RN-P2-C13-Entry19i",
        r"Let $h>0$. If $\displaystyle\psi(n)=\int_0^{h}\varphi(x)\cos(nx)\,dx$, then for $m>0$, "
        r"$\displaystyle\int_0^{\infty}\psi(x)\cos(mx)\,dx"
        r"=\begin{cases}\tfrac{\pi}{2}\varphi(m),&m<h,\\[4pt]\tfrac{\pi}{4}\varphi(m),&m=h,\\[4pt]0,&m>h.\end{cases}$",
    ),
    rec(
        "RN-P2-C13-Entry19ii",
        r"Let $h>0$. If $\displaystyle\psi(n)=\int_0^{h}\varphi(x)\sin(nx)\,dx$, then for $m>0$, "
        r"$\displaystyle\int_0^{\infty}\psi(x)\sin(mx)\,dx"
        r"=\begin{cases}\tfrac{\pi}{2}\varphi(m),&m<h,\\[4pt]\tfrac{\pi}{4}\varphi(m),&m=h,\\[4pt]0,&m>h.\end{cases}$",
    ),
    rec(
        "RN-P2-C13-Entry19-Corollary",
        r"If $a>0$ and $n$ is real, then "
        r"$\displaystyle\int_0^\infty \operatorname{sech}^{2a}x\cos(2nx)\,dx"
        r"=\frac{\sqrt{\pi}\,|\Gamma(a+in)|^2}{2\,\Gamma(a)\Gamma(a+\tfrac12)}$.",
    ),
    rec(
        "RN-P2-C13-Entry20",
        r"If $n>0$ and $0\le a<n$, then "
        r"$\displaystyle\int_0^\infty \frac{\sinh(ax)}{\sinh(nx)(1+n^2x^2)}\,dx"
        r"=\sum_{k=1}^\infty\frac{(-1)^{k+1}\sin(ka)}{1+nk}$.",
    ),
    rec(
        "RN-P2-C13-Entry21",
        r"Let $p,q,n$ be real. Suppose $\varphi_j(p,x)$ and $F(nx)$ are continuous for "
        r"$\alpha_j\le x\le\beta_j$, $j=1,2$. Define "
        r"$\displaystyle\int_{\alpha_1}^{\beta_1}\varphi_1(p,x)F(nx)\,dx=\Psi_1(p,n)$ and "
        r"$\displaystyle\int_{\alpha_2}^{\beta_2}\varphi_2(p,x)F(nx)\,dx=\Psi_2(p,n)$. Then "
        r"$\displaystyle\int_{\alpha_1}^{\beta_1}\varphi_1(p,x)\Psi_2(q,nx)\,dx"
        r"=\int_{\alpha_2}^{\beta_2}\varphi_2(q,x)\Psi_1(p,nx)\,dx$.",
    ),
    rec(
        "RN-P2-C13-Entry21-Corollary",
        r"Let $p,q,\ell,n$ be real. Suppose $\varphi(p,x)\in L(0,\infty)$ and $\lim_{x\to 0^+}\varphi(p,x)$ "
        r"exists. Define $\displaystyle\Psi(p,n)=\int_0^\infty\varphi(p,x)\cos(nx)\,dx$, assume $\Psi(p,n)$ is "
        r"integrable on every finite interval in $[0,\infty)$, and suppose $\Psi(p,n)\to 0$ as $n\to\infty$. "
        r"Then $\displaystyle\pi\int_0^\infty\varphi(p,x)\varphi(q,\ell x)\,dx"
        r"=\int_0^\infty\Psi(q,x)\Psi(p,\ell x)\,dx$.",
    ),
    rec(
        "RN-P2-C13-Entry21-Example",
        r"If $\alpha\beta=\pi/4$, then "
        r"$\displaystyle\int_0^\infty\frac{e^{-x^2}}{\cosh(\alpha x)}\,dx"
        r"=\sqrt{\pi}\int_0^\infty\frac{e^{-x^2}}{\cosh(\beta x)}\,dx$.",
    ),
    rec(
        "RN-P2-C13-Entry22i",
        r"If $a,b>0$, then "
        r"$\displaystyle\int_0^\infty|\Gamma(a+ix)\Gamma(b+ix)|^2\,dx"
        r"=\frac{\sqrt{\pi}\,\Gamma(a)\Gamma(b)\Gamma(a+b)}{2\,\Gamma(a+\tfrac12)\Gamma(b+\tfrac12)}$.",
    ),
    rec(
        "RN-P2-C13-Entry22ii",
        r"If $0<a<b+\tfrac12$, then "
        r"$\displaystyle\int_0^\infty\left|\frac{\Gamma(a+ix)}{\Gamma(b+\tfrac12+ix)}\right|^2 dx"
        r"=\frac{\sqrt{\pi}\,\Gamma(a)\Gamma(a+\tfrac12)\Gamma(b-a+\tfrac12)}"
        r"{2\,\Gamma(b+\tfrac12)\Gamma(b+1)\Gamma(b-a+1)}$.",
    ),
    rec(
        "RN-P2-C13-Entry23",
        r"Let $a>0$, $m<1$, and $m+n>0$. Then "
        r"$\displaystyle\int_0^\infty\frac{x^{-m}\Gamma(x+a)}{\Gamma(x+a+n+1)}\,dx"
        r"=\pi\csc(\pi n)\sum_{k=0}^\infty\frac{(-n)_k}{k!\,(a+k)^m\,\Gamma(n+1)}$.",
    ),
    rec(
        "RN-P2-C13-Entry24i",
        r"For any sequence $\{A_k\}$, "
        r"$\displaystyle\sum_{k=0}^{n}A_k=\sum_{k=0}^{\infty}A_{n-k}-\sum_{k=1}^{\infty}A_{-k}$.",
    ),
    rec(
        "RN-P2-C13-Entry24i-Corollary",
        r"For any sequence $\{A_k\}$, "
        r"$\displaystyle\sum_{k=0}^{n}\frac{A_k}{\Gamma(k+1)}"
        r"=\sum_{k=0}^{\infty}\frac{A_{n-k}}{\Gamma(n-k+1)}-\sum_{k=1}^{\infty}\frac{A_{-k}}{\Gamma(-k+1)}$.",
    ),
    rec(
        "RN-P2-C13-Entry24ii",
        r"For suitable $\varphi$, "
        r"$\displaystyle\lim_{N\to\infty}\sum_{k=-N}^{N}\varphi(x+k)=\lim_{N\to\infty}\sum_{k=-N}^{N}\varphi(y+k)$.",
    ),
    rec(
        "RN-P2-C13-Entry24ii-Corollary",
        r"Ramanujan asserts that for arbitrary $x$ and $h$, "
        r"$\displaystyle\frac{x^h}{h!}+\sum_{k=1}^{\infty}\left\{\frac{x^{h+kn}}{\Gamma(h+kn+1)}"
        r"+\frac{x^{h-kn}}{\Gamma(h-kn+1)}\right\}"
        r"=1+\sum_{k=1}^{\infty}\left\{\frac{x^{kn}}{\Gamma(kn+1)}+\frac{x^{-kn}}{\Gamma(-kn+1)}\right\}"
        r"=\frac{e^x}{n}$.",
    ),
    rec(
        "RN-P2-C13-Entry24iii",
        r"Ramanujan asserts that "
        r"$\displaystyle\int_{-\infty}^{\infty}\frac{\varphi(x)}{\Gamma(x+1)}\,dx=\sum_{n=0}^{\infty}\frac{\varphi(n)}{\Gamma(n+1)}$.",
    ),
    rec(
        "RN-P2-C13-Entry24iii-Corollary01",
        r"Ramanujan asserts that $\displaystyle\int_{-\infty}^{\infty}\frac{a^x}{\Gamma(x+1)}\,dx=e^a$.",
    ),
    rec(
        "RN-P2-C13-Entry24iii-Corollary02",
        r"Ramanujan asserts that "
        r"$\displaystyle\int_{-\infty}^{\infty}\frac{a^x\Gamma(n+1)}{\Gamma(x+1)\Gamma(n-x+1)}\,dx=(1+a)^n$; "
        r"this holds for $a=e^{i\alpha}$ with $|\alpha|<\pi$.",
    ),
    rec(
        "RN-P2-C13-Entry25i",
        r"For real $a$, "
        r"$\displaystyle\int_0^\infty \frac{a^x}{\Gamma(x+1)}\cos(nx)\,dx=e^{a\cos n}\cos(a\sin n)$.",
    ),
    rec(
        "RN-P2-C13-Entry25ii",
        r"For real $a$ and $b$, "
        r"$\displaystyle A_n:=\int_0^\infty\left\{\frac{a^{b+x}}{\Gamma(b+x+1)}+\frac{a^{b-x}}{\Gamma(b-x+1)}\right\}\cos(nx)\,dx"
        r"=e^{a\cos n}\cos(a\sin n-nb)$ and "
        r"$\displaystyle B_n:=\int_0^\infty\left\{\frac{a^{b+x}}{\Gamma(b+x+1)}-\frac{a^{b-x}}{\Gamma(b-x+1)}\right\}\sin(nx)\,dx"
        r"=e^{a\cos n}\sin(a\sin n-nb)$.",
    ),
    rec(
        "RN-P2-C13-Entry25-Example01",
        r"The maximum value of $a^x/\Gamma(x+1)$ for large $a$ is "
        r"$\displaystyle\frac{a^{a-1/2}}{\Gamma(a+\tfrac12)}\left\{1+O(a^{-4})\right\}$.",
    ),
    rec(
        "RN-P2-C13-Entry25-Example02",
        r"Ramanujan states a version of the Euler--Maclaurin summation formula: if $a$ and $b$ "
        r"are nonnegative integers with $b>a$ and $f^{(2m)}$ is absolutely integrable on $[a,b]$, then "
        r"$\displaystyle\sum_{k=a}^{b}f(k)=\int_a^{b}f(t)\,dt+\tfrac12\{f(a)+f(b)\}"
        r"+\sum_{k=1}^{m}\frac{B_{2k}}{(2k)!}\{f^{(2k-1)}(b)-f^{(2k-1)}(a)\}+R_m$, "
        r"where $B_j$ denotes the $j$th Bernoulli number and $R_m$ is the remainder in (10.6).",
    ),
    rec(
        "RN-P2-C13-Entry26i",
        r"Let $n>0$ and let $m$ be a nonnegative integer. Then "
        r"$\displaystyle\int_0^\infty \frac{\cos(2nx)}{(1+x^2)^{m+1}}\,dx"
        r"=\frac{\pi n^m e^{-2n}}{2^m m!}\sum_{k=0}^{m}\frac{(m+k)!}{(4n)^k(m-k)!\,k!}$.",
    ),
    rec(
        "RN-P2-C13-Entry26ii",
        r"Let $p>0$ and let $m,n$ be nonnegative integers with $m\le n$. Then "
        r"$\displaystyle I(m,n):=\int_0^\infty\frac{x^{2m}\cos(px)}{(1+x^2)^{n+1}}\,dx"
        r"=\frac{(-1)^m n e^{-p}}{2^{n+1}}\sum_{r=0}^{n}A_{r,p}p^{n-r}$, where for $r\ge 0$, "
        r"$\displaystyle A_{r,p}=\frac{(n+r)!}{2^r r!(n-r)!}\sum_{k=0}^{\min(r,m)}"
        r"\frac{4^k(-r)_k(-m)_k(-n)_k}{(-n-r)_{2k}k!}$.",
    ),
    rec(
        "RN-P2-C13-Entry27",
        r"If $n$ is an even positive integer, then "
        r"$\displaystyle\left(1+\frac{x}{n}\right)^n"
        r"=\prod_{k=1}^{n/2}\frac{\cosh\bigl(2nx\sin((2k-1)\pi/n)\bigr)-\cos\bigl(2nx\cos((2k-1)\pi/n)\bigr)}"
        r"{2n^2(x/k)^2}$.",
    ),
    rec(
        "RN-P2-C13-Entry27-Corollary01",
        r"If $n$ is arbitrary, then "
        r"$\displaystyle\prod_{k=1}^{n}\left\{1+\left(\frac{k}{n}\right)^3\right\}"
        r"=\frac{\Gamma^3(n+1)\sinh(\pi n/3)}{\Gamma(3n+1)\,\pi n/3}$.",
    ),
    rec(
        "RN-P2-C13-Entry27-Corollary02",
        r"If $n$ is arbitrary, then "
        r"$\displaystyle\prod_{k=1}^{n}\left\{1+\left(\frac{2n+1}{n+k}\right)^3\right\}"
        r"=\frac{\Gamma^3(n+1)\cosh\{\pi(n+\tfrac12)/3\}}{\Gamma(3n+2)\,\pi n}$.",
    ),
    rec(
        "RN-P2-C13-Entry28",
        r"If $m$ and $n$ are positive integers and $x$ is arbitrary, then "
        r"$\displaystyle\sum_{k=0}^{mn-1}\frac{x^{nk}}{(nk)!}"
        r"=\sum_{k=0}^{mn-1}e^x\cos(2\pi k/n)\cos\bigl(x\sin(2\pi k/n)\bigr)$.",
    ),
    rec(
        "RN-P2-C13-Entry29i",
        r"Suppose $p\ge 0$, $l$ is a nonnegative integer, and $n$ is a positive integer with $n>l$. "
        r"If $n$ is even, then "
        r"$\displaystyle\int_0^\infty\cos(px)\frac{x^{2l}-(-1)^l}{1-x^{2n}}\,dx"
        r"=\frac{(-1)^l e^{-p}}{2}"
        r"+\frac{1}{n}\sum_{k=1}^{n/2-1}\exp\!\left\{-p\cos\frac{\pi k}{n}\right\}"
        r"\cos\left\{\frac{(2l+1)\pi k}{n}-p\sin\frac{\pi k}{n}\right\}$.",
    ),
    rec(
        "RN-P2-C13-Entry29ii",
        r"Suppose $p\ge 0$, $l$ is a nonnegative integer, and $n$ is a positive integer with $n>l$. "
        r"If $n$ is odd, then "
        r"$\displaystyle\int_0^\infty\cos(px)\frac{x^{2l}-(-1)^l}{1-x^{2n}}\,dx"
        r"=\sum_{k=1}^{(n-1)/2}\frac{(-1)^l}{n}"
        r"\exp\!\left\{-p\cos\frac{(2k-1)\pi}{2n}\right\}"
        r"\cos\left\{\frac{(2l+1)(2k-1)\pi}{2n}-p\sin\frac{(2k-1)\pi}{2n}\right\}$.",
    ),
    rec(
        "RN-P2-C13-Entry30i",
        r"If $n$ is a nonnegative integer, then "
        r"$\displaystyle\int_0^\infty \frac{\sin^{2n+1}x}{x}\,dx"
        r"=\int_0^\infty \frac{\sin^{2n+2}x}{x}\,dx"
        r"=\frac{\sqrt{\pi}\,\Gamma(n+\tfrac12)}{2n!}$.",
    ),
    rec(
        "RN-P2-C13-Entry30ii",
        r"If $p>2$ and $n-p+1>0$, then "
        r"$(p-1)(p-2)\varphi(n,p)=n(n-1)\varphi(n-2,p-2)-n^2\varphi(n,p-2)$, where "
        r"$\displaystyle\varphi(n,p)=\int_0^\infty \frac{\sin^n x}{x^p}\,dx$.",
    ),
    rec(
        "RN-P2-C13-Entry30-Corollary01",
        r"If $n$ is a nonnegative integer, then "
        r"$\displaystyle\varphi(2n+3,3)=\frac{\sqrt{\pi}(n+\tfrac32)\Gamma(n+\tfrac12)}{4(n+1)!}$.",
    ),
    rec(
        "RN-P2-C13-Entry30-Corollary02",
        r"If $n$ is a nonnegative integer, then "
        r"$\displaystyle\varphi(2n+4,4)=\frac{\sqrt{\pi}(n+2)\Gamma(n+\tfrac12)}{6(n+1)!}$.",
    ),
    rec(
        "RN-P2-C13-Entry30-Example01",
        r"If $0<p<n+1$ and $\varphi$ is as in Entry 30(ii), then "
        r"$\displaystyle\varphi(n,p)=\frac{1}{\Gamma(p)}\int_0^\infty\int_0^\infty\frac{\sin^n x}{x^p}\,e^{-rxt}t^{p-1}\,dt\,dx$.",
    ),
    rec(
        "RN-P2-C13-Entry30-Example02",
        r"If $a>0$ and $n$ is a nonnegative integer, then "
        r"$\displaystyle\int_0^\infty e^{-ax}\frac{\sin^{2n+1}x}{x}\,dx"
        r"=\frac{(2n+1)!}{(a^2+1^2)(a^2+3^2)\cdots(a^2+(2n+1)^2)}$.",
    ),
    rec(
        "RN-P2-C13-Entry30-Example03",
        r"If $a>0$ and $n$ is a nonnegative integer, then "
        r"$\displaystyle\int_0^\infty e^{-ax}\frac{\sin^{2n}x}{x}\,dx"
        r"=\frac{(2n)!}{a(a^2+2^2)(a^2+4^2)\cdots(a^2+(2n)^2)}$.",
    ),
    rec(
        "RN-P2-C13-Entry31i",
        r"Let $h,\alpha,\beta>0$ with $\alpha\beta=2\pi$. Let $\varphi$ be continuous and of bounded variation on "
        r"$[0,h]$, and define $\displaystyle\psi(r)=\int_0^{h}\varphi(x)\cos(rx)\,dx$. Then for real $n$, "
        r"$\displaystyle\alpha\sum_{k=0}^{\prime\,h/\alpha}\varphi(\alpha k)\cos(\alpha nk)"
        r"=\psi(n)+2\sum_{k=1}^{\infty}\{\psi(\beta k+n)+\psi(\beta k-n)\}$, "
        r"where the prime on the sum indicates the usual convention for endpoints.",
    ),
    rec(
        "RN-P2-C13-Entry31ii",
        r"Let $\varphi$ and $\psi$ be as in Entry 31(i), let $h>0$, and assume $n$ is an integer. Then "
        r"$\displaystyle\int_0^{h}\frac{\sin(nx)}{\sin x}\,\varphi(x)\,dx"
        r"=\pi\sum_{k=0}^{\prime\,h/\pi}(-1)^k\varphi(k\pi)\cos(k\pi n)"
        r"-2\sum_{k=0}^{\infty}\psi(n+2k+1)$.",
    ),
    rec(
        "RN-P2-C13-Entry31-Corollary01",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=2\pi$. Let $\varphi$ be continuous and of bounded variation on "
        r"$[0,\infty)$, integrable on $(0,\infty)$, and define $\displaystyle\psi(r)=\int_0^{\infty}\varphi(x)\cos(rx)\,dx$. "
        r"Then $\displaystyle\alpha\sum_{k=0}^{\infty}\varphi(\alpha k)=\psi(0)+2\sum_{k=1}^{\infty}\psi(\beta k)$.",
    ),
    rec(
        "RN-P2-C13-Entry31-Corollary02",
        r"Under the assumptions of Entry 31(ii), "
        r"$\displaystyle\lim_{n\to\infty}\left\{\int_0^{h}\frac{\sin(nx)}{\sin x}\,\varphi(x)\,dx"
        r"-\pi\sum_{k=0}^{\prime\,h/\pi}(-1)^k\varphi(k\pi)\cos(k\pi n)\right\}=0$.",
    ),
    rec(
        "RN-P2-C13-Entry32i",
        r"Let $h,\alpha,\beta>0$ with $\alpha\beta=2\pi$. Let $\varphi$ be continuous and of bounded variation on "
        r"$[0,h]$, and define $\displaystyle\psi(r)=\int_0^{h}\varphi(x)\sin(rx)\,dx$. Then for real $n$, "
        r"$\displaystyle\alpha\sum_{k=0}^{\prime\,h/\alpha}\varphi(\alpha k)\sin(\alpha nk)"
        r"=\psi(n)+\sum_{k=1}^{\infty}\{\psi(\beta k+n)-\psi(\beta k-n)\}$.",
    ),
    rec(
        "RN-P2-C13-Entry32ii",
        r"Let $a$ and $b$ be nonnegative integers with $b>a$, and let $m$ be a positive integer. "
        r"If $f^{(2m)}$ is absolutely integrable on $[a,b]$, then "
        r"$\displaystyle\sum_{k=a}^{b}f(k)=\int_a^{b}f(t)\,dt+\tfrac12\{f(a)+f(b)\}"
        r"+\sum_{k=1}^{m}\frac{B_{2k}}{(2k)!}\{f^{(2k-1)}(b)-f^{(2k-1)}(a)\}+R_m$, "
        r"where $B_j$ denotes the $j$th Bernoulli number and $R_m$ is the remainder in (10.6).",
    ),
    rec(
        "RN-P2-C13-Entry32-Corollary",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi/2$. Let $\varphi$ be continuous on $(0,\infty)$, integrable "
        r"over $(0,\infty)$, of bounded variation on $(0,\infty)$, and tend to $0$ as $x\to\infty$. Define "
        r"$\displaystyle\psi(r)=\int_0^{\infty}\varphi(x)\sin(rx)\,dx$. Then "
        r"$\displaystyle\alpha\sum_{k=0}^{\infty}(-1)^k\varphi((2k+1)\alpha)"
        r"=\sum_{k=0}^{\infty}(-1)^k\psi((2k+1)\beta)$.",
    ),
    rec(
        "RN-P2-C13-Entry33i",
        r"Let $n$ and $\ell$ be nonnegative integers with $n>\ell$, and let $p>0$. If $n$ is even, then "
        r"$\displaystyle\int_0^\infty\frac{\left(-\dfrac{x^2}{n}\right)^{\ell}-(-1)^{\ell}}{1-\dfrac{x^{2n}}{n}+n(x^2-1)}\cos(px)\,dx"
        r"=\dfrac{(-1)^{\ell}e^{-p}}{2n}+\dfrac{1}{n}\sum_{k=1}^{n/2-1}\exp\!\left\{-p\cos\frac{\pi k}{n}\right\}"
        r"\cos\left\{\dfrac{\pi(2\ell+1)k}{n}-p\sin\frac{\pi k}{n}\right\}$.",
    ),
    rec(
        "RN-P2-C13-Entry33ii",
        r"Let $n$ and $\ell$ be nonnegative integers with $n>\ell$, and let $p>0$. If $n$ is odd, then "
        r"$\displaystyle\int_0^\infty\frac{\left(-\dfrac{x^2}{n}\right)^{\ell}-(-1)^{\ell}}{1-\dfrac{x^{2n}}{n}+n(x^2-1)}\cos(px)\,dx"
        r"=\dfrac{1}{n}\sum_{k=1}^{(n-1)/2}\exp\!\left\{-p\cos\frac{(2k-1)\pi}{2n}\right\}"
        r"\cos\left\{\dfrac{\pi(2\ell+1)(2k-1)}{2n}-p\sin\frac{(2k-1)\pi}{2n}\right\}$.",
    ),
    rec(
        "RN-P2-C13-Entry34i",
        r"If $x$ is arbitrary, then for $|\operatorname{Re}\theta|\le\pi$, "
        r"$\displaystyle\frac{\pi\cos(\theta x)}{\sin(\pi x)}=\frac{1}{2}+\sum_{k=1}^{\infty}(-1)^{k+1}\frac{\cos(k\theta)}{k^2-x^2}$.",
    ),
    rec(
        "RN-P2-C13-Entry34ii",
        r"If $x$ is arbitrary, then for $|\operatorname{Re}\theta|\le\pi/2$, "
        r"$\displaystyle\frac{\pi\sin(\theta x)}{4x\cos(\pi x)}=\sum_{k=0}^{\infty}(-1)^k\frac{\sin((2k+1)\theta)}{(2k+1)^2-x^2}$.",
    ),
    rec(
        "RN-P2-C13-Entry34-Corollary01",
        r"If $x$ is arbitrary, then for $|\operatorname{Re}\theta|\le\pi$, "
        r"$\displaystyle\frac{\pi\cosh(\theta x)}{\sinh(\pi x)}=\frac{1}{2}+2\sum_{k=1}^{\infty}(-1)^k\frac{\cos(k\theta)}{k^2+x^2}$.",
    ),
    rec(
        "RN-P2-C13-Entry34-Corollary02",
        r"If $x$ is arbitrary, then for $|\operatorname{Re}\theta|\le\pi/2$, "
        r"$\displaystyle\frac{\pi\sinh(\theta x)}{4x\cosh(\pi x)}=\sum_{k=0}^{\infty}(-1)^k\frac{\sin((2k+1)\theta)}{(2k+1)^2+x^2}$.",
    ),
    rec(
        "RN-P2-C13-Entry35",
        r"Let $n$ be a nonnegative integer, and let $\alpha,\beta>0$ with $\alpha\beta=\pi$. Then "
        r"$\displaystyle\sqrt{\alpha}\sum_{k=0}^{\infty}\frac{1}{(1+\alpha^2k^2)^{n+1}}"
        r"=\sqrt{\beta}\,\frac{\Gamma(n+\tfrac12)}{\Gamma(n+1)}\left\{\frac{1}{2}+\sum_{k=1}^{\infty}e^{-2\beta k}\varphi(4\beta k)\right\}$, "
        r"where $\displaystyle\varphi(t)=\sum_{k=0}^{n}\frac{n!}{(2n)!}\frac{(n+k)!}{(n-k)!}\frac{t^k}{k!}$.",
    ),
    rec(
        "RN-P2-C13-Entry36",
        r"Let $N$ be any positive integer. As $m^2+n^2\to\infty$, "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{1}{(m^2+(n+k)^2)^2}"
        r"=\frac{1}{m^2+n^2}\left\{\frac{1}{m^2+n^2}-\frac{1}{m}\tan^{-1}\frac{m}{n}\right\}"
        r"+\sum_{k=1}^{N}\frac{B_{2k}}{2k}\frac{\sin(2k\tan^{-1}(m/n))}{(m^2+n^2)^k}"
        r"+O\bigl((m^2+n^2)^{-N-1}\bigr)$, where $B_k$ denotes the $k$th Bernoulli number.",
    ),
    rec(
        "RN-P2-C13-Entry36-Corollary",
        r"As $n\to\infty$, "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{1}{n^2+(n+k)^2}"
        r"\sim\frac{\pi}{4n}-\sum_{k=0}^{\infty}\frac{(-1)^k B_{4k+2}}{(2k+1)2^{2k+2}n^{4k+2}}$.",
    ),
]
