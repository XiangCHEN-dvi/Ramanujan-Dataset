"""Part II, Chapter 14 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C14 = ["infinite-series"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C14}


CHAPTER_14 = [
    rec(
        "RN-P2-C14-Entry01",
        r"For $z^2\neq -n(n+1)/2$, where $n$ is a nonnegative integer, $\displaystyle z^{-2}\prod_{n=1}^{\infty}\left(1+\frac{2z^2}{n(n+1)}\right)^{-1}=\sum_{n=0}^{\infty}\frac{(-1)^n(2n+1)}{z^2+n(n+1)/2}$.",
    ),
    rec(
        "RN-P2-C14-Entry01-Corollary",
        r"For $\Re z>0$, "
        r"$\displaystyle\frac{z}{\pi}+\sum_{n=1}^{\infty}\frac{(-1)^{n+1}(2n+1)}{\ln(n+1)\bigl(e^{2\pi z\sqrt{n(n+1)}}-1\bigr)}"
        r"=\frac{z}{2\pi}+\frac{1}{6}+C$, where "
        r"$\displaystyle C=\frac{1}{2}+\sum_{n=1}^{\infty}{}^{*}\frac{(-1)^{n+1}(2n+1)}{2\ln(n+1)}$, "
        r"and the asterisk indicates that the terms must be added in successive pairs for convergence.",
    ),
    rec(
        "RN-P2-C14-Entry02",
        r"Let $m$, $n$, $x$, and $y$ be complex numbers. Suppose that $\Gamma(1+xz)$ and $\Gamma(1+yz)$ have no coincident poles and that $z=1$ is not a pole of either. "
        r"If $\Re(m+n)>0$, then "
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{(-1)^{k+1}\Gamma(1-ky/x)}{\Gamma(m-k+1)\Gamma(n+1-ky/x)(k+x)}"
        r"+\sum_{k=1}^{\infty}\frac{(-1)^{k+1}\Gamma(1-kx/y)}{\Gamma(n-k+1)\Gamma(m+1-kx/y)(k+y)}"
        r"=\frac{\Gamma(x+1)\Gamma(y+1)}{\Gamma(x+m+1)\Gamma(y+n+1)}$.",
    ),
    rec(
        "RN-P2-C14-Entry02-Corollary01",
        r"Let $m$, $n$, and $x$ be complex numbers such that $x$ is not an integer and $\Re(m+n)>-1$. Then $\displaystyle\sum_{k=-\infty}^{\infty}\frac{(-1)^k}{(x+k)\Gamma(m+1-k)\Gamma(n+1+k)}=\frac{\pi}{\sin(\pi x)\Gamma(m+x+1)\Gamma(n-x+1)}$.",
    ),
    rec(
        "RN-P2-C14-Entry02-Corollary02",
        r"Let $\alpha$ and $\beta$ be complex numbers with $\Re(\alpha+\beta)>0$. Then $\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)\Gamma(\alpha-k)\Gamma(\beta+k+1)}+\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)\Gamma(\beta-k)\Gamma(\alpha+k+1)}=\frac{\pi}{2\Gamma(\alpha+\tfrac{1}{2})\Gamma(\beta+\tfrac{1}{2})}$.",
    ),
    rec(
        "RN-P2-C14-Entry03",
        r"Let $\alpha$, $\beta$, $\gamma$, and $\delta$ be complex numbers with $\Re(\alpha+\beta+\gamma+\delta)>-1$. Then $\displaystyle\sum_{k=0}^{\infty}\frac{1}{\Gamma(\alpha-k+1)\Gamma(\beta-k+1)\Gamma(\gamma+k+1)\Gamma(\delta+k+1)}+\sum_{k=1}^{\infty}\frac{1}{\Gamma(\alpha+k+1)\Gamma(\beta+k+1)\Gamma(\gamma-k+1)\Gamma(\delta-k+1)}=\frac{\Gamma(\alpha+\beta+\gamma+\delta+1)}{\Gamma(\alpha+\gamma+1)\Gamma(\beta+\gamma+1)\Gamma(\alpha+\delta+1)\Gamma(\beta+\delta+1)}$.",
    ),
    rec(
        "RN-P2-C14-Entry04",
        r"If $z\neq me^{\pm\pi i/3}$, where $m$ is a nonzero integer, then $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2+z^2+z^4/n^2}=\frac{\pi}{2z\sqrt{3}}\frac{\sinh(\pi z\sqrt{3})-\sqrt{3}\sin(\pi z)}{\cosh(\pi z\sqrt{3})-\cos(\pi z)}$.",
    ),
    rec(
        "RN-P2-C14-Entry04-Corollary",
        r"For each nonzero integer $n$, $\displaystyle\sum_{k=1}^{\infty}\frac{1}{k^2+(2n)^2+(2n)^4/k^2}=\frac{1}{12n^2}+\frac{1}{2}\sum_{k=1}^{\infty}\frac{1}{k^2+3n^2}$.",
    ),
    rec(
        "RN-P2-C14-Entry05i",
        r"Let $0<x<\pi/(n+\tfrac{1}{2})$, where $n$ is a positive integer. Then $\displaystyle\sum_{k=1}^{\infty}\frac{\sin^{2n+1}(kx)}{k}=\frac{\sqrt{\pi}}{2}\frac{\Gamma(n+\tfrac{1}{2})}{\Gamma(n+1)}$.",
    ),
    rec(
        "RN-P2-C14-Entry05ii",
        r"Let $0\leq x\leq\pi/(n+1)$, where $n$ is a positive integer. Then "
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{\sin^{2n+2}(kx)}{k^2}"
        r"=\frac{\pi}{2^{2n+2}}\frac{\Gamma(n+\tfrac{1}{2})}{\Gamma(n+1)}\,x$.",
    ),
    rec(
        "RN-P2-C14-Entry06",
        r"For $n>0$, let $\displaystyle\varphi(\beta)=\pi\prod_{k=0}^{\infty}\left(1+\frac{\beta}{n+k}\right)^{-1}$. "
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi$. Then "
        r"$\displaystyle\frac{\Gamma(n)}{\Gamma(n+\tfrac{1}{2})\sqrt{\pi}}\left\{\frac{1}{2}+\sum_{k=1}^{\infty}\operatorname{sech}^{2n}(\alpha k)\right\}"
        r"$=\frac{1}{2}+\sum_{k=1}^{\infty}\varphi(\beta k)$.",
    ),
    rec(
        "RN-P2-C14-Entry07",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi$ and let $z$ be an arbitrary complex number. Then "
        r"$\displaystyle e^{z^2/(4\pi)}\prod_{k=1}^{\infty}\left\{\tfrac{1}{2}+e^{-\alpha^2 k^2}\cos(\alpha z k)\right\}"
        r"$=\prod_{k=1}^{\infty}\left\{-\tfrac{1}{2}+e^{-\beta^2 k^2}\cosh(\beta z k)\right\}$.",
    ),
    rec(
        "RN-P2-C14-Entry07-Corollary",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi$. Then "
        r"$\displaystyle\prod_{k=1}^{\infty}\left\{\tfrac{1}{2}+e^{-\alpha^2 k^2}\right\}"
        r"$=\prod_{k=1}^{\infty}\left\{-\tfrac{1}{2}+e^{-\beta^2 k^2}\right\}$.",
    ),
    rec(
        "RN-P2-C14-Entry08i",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi$ and $0<\beta\pi<\pi$. Then "
        r"$\displaystyle\alpha\sum_{k=1}^{\infty}\frac{\sinh(2\alpha\pi k)}{k(e^{2\alpha^2\pi k}-1)}"
        r"=\frac{\pi}{4}\alpha\coth(\alpha\pi)-\frac{\pi}{4}\beta\cot(\beta\pi)-\ln 2$.",
    ),
    rec(
        "RN-P2-C14-Entry08ii",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi$ and $0<\alpha\pi<\pi$. Then "
        r"$\displaystyle 2\sum_{k=1}^{\infty}\frac{\cos(2\alpha\pi k)}{k(e^{2\alpha^2\pi k}-1)}"
        r"-2\sum_{k=1}^{\infty}\frac{\cosh(2\beta\pi k)}{k(e^{2\beta^2\pi k}-1)}"
        r"=\frac{\pi^2}{6\alpha^2}+\ln\left\{\frac{\sin(\alpha\pi)}{\sinh(\beta\pi)}\right\}$.",
    ),
    rec(
        "RN-P2-C14-Entry08iii",
        r"Let $\alpha,\beta,r,t>0$ with $\alpha\beta=\pi$, $r=\pi\beta$, and $t=\pi/\beta^2$. "
        r"Let $C$ be the positively oriented parallelogram with vertices $\pm i$ and $\pm t$. "
        r"Let $\varphi(z)$ be entire. For each positive integer $m$, put $M=m+t$ and define "
        r"$f_m(z)=\dfrac{\varphi(rMz)}{z(e^{2\pi Mz}-1)(e^{2\pi i Mz/t}-t)}$, "
        r"and assume that $mf_m(z)$ tends to $0$ boundedly on $C\setminus\{\pm i,\pm t\}$ as $m\to\infty$. Then "
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{\varphi(\alpha\pi k)+\varphi(-\alpha\pi k)}{k(e^{2\alpha^2\pi k}-1)}"
        r"+\sum_{k=1}^{\infty}\frac{\varphi(\alpha\pi k)}{k}"
        r"-\sum_{k=1}^{\infty}\frac{\varphi(i\beta\pi k)+\varphi(-i\beta\pi k)}{k(e^{2\beta^2\pi k}-1)}"
        r"-\sum_{k=1}^{\infty}\frac{\varphi(i\beta\pi k)}{k}$"
        r"$=\dfrac{\pi i\varphi(0)}{2}-\dfrac{\alpha^2\varphi(0)}{6}+\dfrac{\beta^2\varphi(0)}{6}"
        r"$-\dfrac{\alpha\pi\varphi'(0)}{2}+\dfrac{\beta\pi i\varphi'(0)}{2}-\dfrac{\pi^2\varphi''(0)}{4}$, "
        r"provided that all series above converge.",
    ),
    rec(
        "RN-P2-C14-Entry08-Corollary01",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi^2$. Then $\displaystyle\alpha\sum_{k=1}^{\infty}\frac{k}{e^{2\alpha\pi k}-1}+\beta\sum_{k=1}^{\infty}\frac{k}{e^{2\beta\pi k}-1}=\frac{\alpha+\beta}{24}-\frac{\pi^2}{4}$.",
    ),
    rec(
        "RN-P2-C14-Entry08-Corollary02",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi^2$. Then $\displaystyle e^{(\beta-\alpha)/(12\alpha)}=\left(\frac{\alpha}{\beta}\right)^{1/4}\prod_{k=1}^{\infty}\frac{1-e^{-2\beta\pi k}}{1-e^{-2\alpha\pi k}}$.",
    ),
    rec(
        "RN-P2-C14-Entry08-Example",
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{k}{e^{2\pi k}-1}=\frac{1}{24}-\frac{\pi}{8}$.",
    ),
    rec(
        "RN-P2-C14-Entry09i",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi/2$. Let $h>0$ be chosen so that $h/\alpha>1$ and $h/\alpha$ is not an odd integer. "
        r"Let $m$ be the greatest odd integer less than $h/\alpha$. Let $n$ be an arbitrary real number. "
        r"Let $\varphi(x)$ be continuous and of bounded variation on $[0,h]$ and define "
        r"$\displaystyle\psi(t)=\int_0^h\varphi(x)\cos(tx)\,dx$, where $\chi$ is the primitive character modulo $4$. Then "
        r"$\displaystyle\alpha\sum_{k=1}^{m}\chi(k)\sin(\alpha\pi k)\varphi(\alpha k)"
        r"=\frac{\pi}{2}\sum_{k=1}^{\infty}\chi(k)\{\psi(\beta k-n)-\psi(\beta k+n)\}$.",
    ),
    rec(
        "RN-P2-C14-Entry09ii",
        r"Let $\alpha,\beta,h,m,n$, and $\varphi$ satisfy the same hypotheses as in Entry 9(i). Define "
        r"$\displaystyle\psi(t)=\int_0^h\varphi(x)\sin(tx)\,dx$. Then "
        r"$\displaystyle\alpha\sum_{k=1}^{m}\chi(k)\cos(\alpha\pi k)\varphi(\alpha k)"
        r"=\frac{\pi}{2}\sum_{k=1}^{\infty}\chi(k)\{\psi(\beta k+n)+\psi(\beta k-n)\}$.",
    ),
    rec(
        "RN-P2-C14-Entry10",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi/4$ and let $z$ be an arbitrary complex number. Then $\displaystyle e^{z^2/4\pi}\sum_{k=1}^{\infty}\chi(k)e^{-\alpha^2 k^2}\sin(\alpha z k)=\sqrt{\pi}\sum_{k=1}^{\infty}\chi(k)e^{-\beta^2 k^2}\sinh(\beta z k)$.",
    ),
    rec(
        "RN-P2-C14-Entry11",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi$ and let $n$ be real with $|n|<\beta/2$. Then "
        r"$\displaystyle\frac{\alpha}{4}\sec(\alpha n)+\sum_{k=1}^{\infty}\chi(k)\frac{\cos(\alpha\pi k)}{e^{2\alpha^2\pi k}-1}"
        r"=\frac{\beta}{\pi}-\frac{1}{4}+\frac{1}{2}\sum_{k=1}^{\infty}\chi(k)\frac{\cosh(2\beta\pi k)}{\cosh(2\beta^2\pi k)}$.",
    ),
    rec(
        "RN-P2-C14-Entry12",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi/2$ and let $0<n<\pi/(2\alpha)$. Then "
        r"$\displaystyle\alpha\sum_{k=1}^{\infty}\chi(k)\frac{\sin(\alpha n/k)}{\cosh(\alpha k)}"
        r"=\beta\sum_{k=1}^{\infty}\chi(k)\frac{\sinh(\beta n/k)}{\cosh(\beta k)}$.",
    ),
    rec(
        "RN-P2-C14-Entry12-Corollary",
        r"Let $\alpha,\beta,t>0$ with $\alpha\beta=\pi/2$ and $t=\alpha/\beta$. Let $C$ be the positively oriented parallelogram with vertices $\pm i$ and $\pm t$. Let $\varphi(z)$ be entire. For each positive integer $N$, define $f_N(z)=\dfrac{\varphi(4\beta N z)}{\cosh(2\pi N z)\cosh(2\pi i N z/t)}$, and assume that $Nf_N(z)$ tends to $0$ boundedly on $C$ as $N\to\infty$. Then $\displaystyle\alpha\sum_{k=1}^{\infty}\chi(k)\frac{\varphi(\alpha k)-\varphi(-\alpha k)}{\cosh(\alpha k)}+i\beta\sum_{k=1}^{\infty}\chi(k)\frac{\varphi(i\beta k)-\varphi(-i\beta k)}{\cosh(\beta k)}=0$.",
    ),
    rec(
        "RN-P2-C14-Entry13",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi^2$ and let $n$ be an integer greater than $1$. Then $\displaystyle\alpha^n\sum_{k=1}^{\infty}\frac{k^{2n-1}}{e^{2\alpha\pi k}-1}+(-\beta)^n\sum_{k=1}^{\infty}\frac{k^{2n-1}}{e^{2\beta\pi k}-1}=\frac{B_{2n}}{(2n)!}\{\alpha^n-(-\beta)^n\}$.",
    ),
    rec(
        "RN-P2-C14-Entry13-Corollary01",
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{k^5}{e^{2\pi k}-1}=\frac{\pi^2}{504}$.",
    ),
    rec(
        "RN-P2-C14-Entry13-Corollary02",
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{k^9}{e^{2\pi k}-1}=\frac{\pi^6}{264}$.",
    ),
    rec(
        "RN-P2-C14-Entry13-Corollary03",
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{k^{13}}{e^{2\pi k}-1}=\frac{\pi^{10}}{24}$.",
    ),
    rec(
        "RN-P2-C14-Entry13-Corollary04",
        r"If $n$ is a positive integer, then $\displaystyle\sum_{k=1}^{\infty}\frac{k^{4n+1}}{e^{2\pi k}-1}=\frac{B_{4n+2}}{8n+4}$.",
    ),
    rec(
        "RN-P2-C14-Entry14",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi^2$ and let $n$ be a positive integer. Then $\displaystyle\alpha^n\sum_{k=1}^{\infty}\chi(k)\frac{k^{2n-1}}{\cosh(\alpha\pi k/2)}+(-\beta)^n\sum_{k=1}^{\infty}\chi(k)\frac{k^{2n-1}}{\cosh(\beta\pi k/2)}=0$.",
    ),
    rec(
        "RN-P2-C14-Entry14-Corollary",
        r"If $n$ is a positive integer, then $\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)^{4n-1}}{\cosh\{(2k+1)\pi/2\}}=0$.",
    ),
    rec(
        "RN-P2-C14-Entry15",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi^2/4$. Then $\displaystyle 2\sum_{n=1}^{\infty}\chi(n)\tan^{-1}(e^{-\alpha n})+2\sum_{n=1}^{\infty}\chi(n)\tan^{-1}(e^{-\beta n})=\sum_{n=1}^{\infty}\chi(n)\frac{\operatorname{sech}(\alpha n)}{n}+\sum_{n=1}^{\infty}\chi(n)\frac{\operatorname{sech}(\beta n)}{n}=\frac{\pi}{4}$.",
    ),
    rec(
        "RN-P2-C14-Entry15-Corollary",
        r"$\displaystyle\sum_{n=1}^{\infty}\chi(n)\tan^{-1}(e^{-\pi n/2})=\frac{\pi}{16}$.",
    ),
    rec(
        "RN-P2-C14-Entry16i",
        r"Let $m$ and $n$ be nonnegative integers. Then "
        r"$\displaystyle\int_0^{\infty}\frac{\sin^{2n+1}x}{x}\cos^{2m}x\,dx"
        r"=\frac{2\pi}{2^{m+n+1}}\frac{\Gamma(m+\tfrac{1}{2})\Gamma(n+\tfrac{1}{2})}{\Gamma(m+n+1)}"
        r"=\int_0^{\infty}\frac{\sin^{2n+2}x}{x}\cos^{2m}x\,dx$.",
    ),
    rec(
        "RN-P2-C14-Entry16ii",
        r"Let $n$ and $p$ be nonnegative integers. Then "
        r"$\displaystyle\int_0^{\infty}\frac{\sin^{2n+1}x}{x}\cos(2px)\,dx"
        r"=\frac{(-1)^p\pi}{2}\frac{\Gamma(n+1)\Gamma(n+\tfrac{1}{2})}{\Gamma(n-p+1)\Gamma(n+p+1)}"
        r"=\int_0^{\infty}\frac{\sin^{2n+2}x}{x}\cos(2px)\,dx$.",
    ),
    rec(
        "RN-P2-C14-Entry17i",
        r"Let $\alpha,\beta,n>0$ with $\alpha\beta=2\pi$. Suppose that $\pi/(2\alpha)$ is not an integer and let $m=[\pi/(2\alpha)]$. Let $p$ be real. Then "
        r"$\displaystyle\alpha\left\{\frac{1}{2}+\sum_{k=1}^{m}\cos^n(\alpha\pi k)\cos(\alpha\pi p k)\right\}$"
        r"$=\dfrac{\pi^n}{2^{n+1}n!}\left\{\Gamma(\tfrac{1}{2}n+\tfrac{1}{2}p+1)\Gamma(\tfrac{1}{2}n-\tfrac{1}{2}p+1)\right.$"
        r"$\displaystyle\left.+\sum_{k=1}^{\infty}\frac{1}{\Gamma(\tfrac{1}{2}n-\tfrac{1}{2}p+\beta k+1)\Gamma(\tfrac{1}{2}n+\tfrac{1}{2}p-\beta k+1)}\right.$"
        r"$\displaystyle\left.+\frac{1}{\Gamma(\tfrac{1}{2}n+\tfrac{1}{2}p+\beta k+1)\Gamma(\tfrac{1}{2}n-\tfrac{1}{2}p-\beta k+1)}\right\}$.",
    ),
    rec(
        "RN-P2-C14-Entry17ii",
        r"Let $\alpha,\beta,n>0$ with $\alpha\beta=\pi/2$. Suppose that $\pi/(2\alpha)$ is not an odd integer and let $m=[\pi/(2\alpha)]$. Let $p$ be real. Then "
        r"$\displaystyle\alpha\sum_{k=1}^{m}\chi(k)\cos^n(\alpha\pi k)\sin(\alpha\pi p k)$"
        r"$=\dfrac{\pi^n}{2^{2n+2}}\sum_{k=1}^{\infty}\chi(k)\left\{\frac{1}{\Gamma(\tfrac{1}{2}n-\tfrac{1}{2}p+\beta k+1)\Gamma(\tfrac{1}{2}n+\tfrac{1}{2}p-\beta k+1)}\right.$"
        r"$\displaystyle\left.-\frac{1}{\Gamma(\tfrac{1}{2}n+\tfrac{1}{2}p+\beta k+1)\Gamma(\tfrac{1}{2}n-\tfrac{1}{2}p-\beta k+1)}\right\}$.",
    ),
    rec(
        "RN-P2-C14-Entry17-Corollary01",
        r"Let $\alpha=\pi/(n+j)$, where $n$ and $j$ are positive integers of opposite parity. Let $m=[\pi/(2\alpha)]$. Then "
        r"$\displaystyle\frac{1}{2}+\sum_{k=1}^{m}\cos^{2n}(\alpha\pi k)=\frac{\pi^{2n+1}}{2^{2n+1}(2n)!}$.",
    ),
    rec(
        "RN-P2-C14-Entry17-Corollary02",
        r"Let $\alpha=\pi/(n-j)$, where $n$ and $j$ are integers of opposite parity with $n>0$ and $0\leq j\leq(n-1)/2$. Let $m=[\pi/(2\alpha)]$. Then $\displaystyle\alpha\left\{\frac{1}{2}+\sum_{k=1}^{m}\cos^{2n}(\alpha\pi k)\right\}$=\dfrac{\pi^{2n+1}}{2^{2n+1}(2n)!}\left\{1+\frac{2(n!)^2}{\Gamma(n+1+\pi/\alpha)\Gamma(n+1-\pi/\alpha)}\right\}$.",
    ),
    rec(
        "RN-P2-C14-Entry18",
        r"Let $a_n,b_n,p_n,q_n,P_n,Q_n$ be complex numbers with $a_nb_n\neq 0$. Let $x$ and $y$ be complex with $xy\neq 0$. Let "
        r"$\displaystyle\varphi(x)=\frac{1}{x}+\sum_{n=1}^{\infty}\frac{P_n}{p_n x+a_n}$ and "
        r"$\displaystyle\psi(y)=\frac{1}{y}+\sum_{n=1}^{\infty}\frac{Q_n}{q_n y+b_n}$. Then "
        r"$\displaystyle\varphi(x)\psi(y)=\frac{1}{xy}+\sum_{n=1}^{\infty}\sum_{k=1}^{\infty}\frac{P_n Q_k}{(p_n x+a_n)(q_k y+b_k)}$, "
        r"where it is assumed that at least one of the two double series on the right converges absolutely.",
    ),
    rec(
        "RN-P2-C14-Entry18-Corollary01",
        r"Let $\theta$ and $\varphi$ be real with $|\theta|,|\varphi|<\pi$. For complex $n,x,y$ with $x/y$ not purely imaginary, $\displaystyle\frac{\pi^2n^2xy\cos(\theta\pi x)\cosh(\varphi\pi y)}{\sin(\pi n x)\sinh(\pi n y)}=1+\pi^2n^2xy\sum_{k=1}^{\infty}\frac{(-1)^k k\cos(k\varphi)\cosh(k\theta x/y)}{(k^2+\pi^2n^2y^2)\sinh(\pi n k x/y)}-2\pi^2n^2xy\sum_{k=1}^{\infty}\frac{(-1)^k k\cos(k\theta)\cosh(k\varphi y/x)}{(k^2-\pi^2n^2x^2)\sinh(\pi n k y/x)}$.",
    ),
    rec(
        "RN-P2-C14-Entry18-Corollary02",
        r"Let $\theta$ and $\varphi$ be real with $|\theta|,|\varphi|\leq\pi/2$. For complex $n,x,y$ with $y/x$ not purely imaginary, $\displaystyle\frac{\pi n\sin(\theta\pi x)\sinh(\varphi\pi y)}{4\pi^2\cos(\pi n x/2)\cosh(\pi n y/2)}=\frac{y}{\pi}\sum_{k=1}^{\infty}\chi(k)\frac{\sin(k\varphi)\sinh(k\theta x/y)}{k(k^2+\pi^2n^2y^2)\cosh(\pi n k x/(2y))}+\frac{x}{\pi}\sum_{k=1}^{\infty}\chi(k)\frac{\sin(k\theta)\sinh(k\varphi y/x)}{k(k^2-\pi^2n^2x^2)\cosh(\pi n k y/(2x))}$.",
    ),
    rec(
        "RN-P2-C14-Entry18-Corollary03",
        r"Let $\theta$ and $\varphi$ be real with $|\theta|,|\varphi|\leq\pi/2$. For complex $n,x,y$ with $y/x$ not purely imaginary, $\displaystyle\frac{\pi n\cos(\theta\pi x)\sinh(\varphi\pi y)}{4\sin(\pi n x/2)\cosh(\pi n y/2)}=\frac{\pi y}{2x}+\pi^2n^2y^2\sum_{k=0}^{\infty}\frac{(-1)^k\sin\{(2k+1)\varphi\}\cosh\{(2k+1)\theta x/y\}}{(2k+1)\{(2k+1)^2+\pi^2n^2y^2\}\sinh\{(2k+1)\pi n x/(2y)\}}+\frac{\pi n}{x}\sum_{k=1}^{\infty}\frac{(-1)^{k+1}\cos(2k\theta)\sinh(2k\varphi y/x)}{2k\{(2k)^2-\pi^2n^2x^2\}\cosh(\pi n k y/x)}$.",
    ),
    rec(
        "RN-P2-C14-Entry19i",
        r"$\displaystyle\pi^2xy\cot(\pi x)\coth(\pi y)=1+\pi^2xy^2\sum_{n=1}^{\infty}\frac{n\coth(\pi n x/y)}{(n+y)^2}-\pi^2xy\sum_{n=1}^{\infty}\frac{n\coth(\pi n y/x)}{(n-x)^2}$.",
    ),
    rec(
        "RN-P2-C14-Entry19ii",
        r"Let $x$ and $y$ be complex with $x/y$ not purely imaginary. Then $\displaystyle\pi^2xy\csc(\pi x)\operatorname{csch}(\pi y)=1+\pi^2xy\sum_{n=1}^{\infty}\frac{(-1)^n n\operatorname{csch}(\pi n x/y)}{(n+y)^2}-2\pi^2xy\sum_{n=1}^{\infty}\frac{(-1)^n n\operatorname{csch}(\pi n y/x)}{(n-x)^2}$.",
    ),
    rec(
        "RN-P2-C14-Entry19iii",
        r"Let $x$ and $y$ be complex with $y/x$ not purely imaginary. Then "
        r"$\displaystyle\frac{\pi}{4}\tan(\pi x/2)\tanh(\pi y/2)"
        r"=\frac{y}{2}\sum_{n=0}^{\infty}\frac{\tanh\{(2n+1)\pi x/(2y)\}}{(2n+1)\{(2n+1)^2+y^2\}}"
        r"+x^2\sum_{n=0}^{\infty}\frac{\tanh\{(2n+1)\pi y/(2x)\}}{(2n+1)\{(2n+1)^2-x^2\}}$.",
    ),
    rec(
        "RN-P2-C14-Entry19iv",
        r"Let $x$ and $y$ be complex with $y/x$ not purely imaginary. Then $\displaystyle\frac{\pi}{4}\sec(\pi x/2)\operatorname{sech}(\pi y/2)=\sum_{n=1}^{\infty}\chi(n)\frac{n\operatorname{sech}\{\pi n x/(2y)\}}{n^2+y^2}+\sum_{n=1}^{\infty}\chi(n)\frac{n\operatorname{sech}\{\pi n y/(2x)\}}{n^2-x^2}$.",
    ),
    rec(
        "RN-P2-C14-Entry19v",
        r"Let $x$ and $y$ be complex with $y/x$ not purely imaginary. Then $\displaystyle\frac{\pi}{4}\cot(\pi x/2)\operatorname{sech}(\pi y/2)=\frac{y}{2}\sum_{n=1}^{\infty}\chi(n)\frac{\coth\{\pi n x/(2y)\}}{n^2+y^2}-\frac{x}{2}\sum_{n=1}^{\infty}\chi(n)\frac{\operatorname{sech}(\pi n y/x)}{(2n)^2-x^2}$.",
    ),
    rec(
        "RN-P2-C14-Entry20i",
        r"$\displaystyle\pi^2 z^2\cot(\pi z)\coth(\pi z)=1-4\pi^2 z^4\sum_{n=1}^{\infty}\frac{n\coth(\pi n)}{n^4-z^4}$.",
    ),
    rec(
        "RN-P2-C14-Entry20i-Corollary",
        r"$\displaystyle\frac{\pi^2 z^2\{\cosh(\pi z/\sqrt{2})+\cos(\pi z/\sqrt{2})\}-1}{\cosh(\pi z/\sqrt{2})-\cos(\pi z/\sqrt{2})}=4\pi z\sum_{n=1}^{\infty}\frac{n\coth(\pi n)}{n^4+z^4}$.",
    ),
    rec(
        "RN-P2-C14-Entry20ii",
        r"$\displaystyle\pi^2 z^2\csc(\pi z)\operatorname{csch}(\pi z)=1-4\pi^2 z^4\sum_{n=1}^{\infty}\frac{(-1)^n n\operatorname{csch}(\pi n)}{n^4-z^4}$.",
    ),
    rec(
        "RN-P2-C14-Entry20ii-Corollary",
        r"$\displaystyle 1+\frac{2\pi^2 z^2}{\cosh(\pi z e^{\pi i/4}/\sqrt{2})-\cos(\pi z e^{\pi i/4}/\sqrt{2})}=4\pi^2 z^4\sum_{n=1}^{\infty}\frac{(-1)^n n\operatorname{csch}(\pi n)}{n^4+e^{\pi i}z^4}$.",
    ),
    rec(
        "RN-P2-C14-Entry20iii",
        r"$\displaystyle\frac{\pi}{2}\tan(\pi z/2)\tanh(\pi z/2)=\frac{\pi}{8z}\sum_{n=0}^{\infty}\frac{(2n+1)\tanh\{(2n+1)\pi/2\}}{(2n+1)^4-z^4}$.",
    ),
    rec(
        "RN-P2-C14-Entry20iii-Corollary",
        r"$\displaystyle\frac{\pi\cosh(\pi z/\sqrt{2})-\cos(\pi z/\sqrt{2})}{\pi z^2\cosh(\pi z/\sqrt{2})+\cos(\pi z/\sqrt{2})}=\frac{8}{\pi z}\sum_{n=0}^{\infty}\frac{(2n+1)\tanh\{(2n+1)\pi/2\}}{(2n+1)^4+z^4}$.",
    ),
    rec(
        "RN-P2-C14-Entry20iv",
        r"$\displaystyle\pi^3\sec(\pi z/2)\operatorname{sech}(\pi z/2)=\sum_{n=1}^{\infty}\chi(n)\frac{n^3\operatorname{sech}(\pi n/2)}{n^4-z^4}$.",
    ),
    rec(
        "RN-P2-C14-Entry20iv-Corollary",
        r"$\displaystyle\frac{\pi/4}{\cosh(\pi z e^{\pi i/4}/\sqrt{2})+\cos(\pi z e^{\pi i/4}/\sqrt{2})}=\sum_{n=1}^{\infty}\chi(n)\frac{n^3\operatorname{sech}(\pi n/2)}{n^4+e^{\pi i}z^4}$.",
    ),
    rec(
        "RN-P2-C14-Entry21i",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi^2$ and let $n$ be any nonzero integer. Then "
        r"$\displaystyle\alpha^{-n}\left\{\zeta(2n+1)+\sum_{k=1}^{\infty}\frac{k^{-2n-1}}{e^{2\alpha\pi k}-1}\right\}"
        r"$=(-\beta)^{-n}\left\{\zeta(2n+1)+\sum_{k=1}^{\infty}\frac{k^{-2n-1}}{e^{2\beta\pi k}-1}\right\}"
        r"$-\dfrac{2^{2n}}{n!}\sum_{k=0}^{n}\frac{(-1)^k B_{2k}B_{2n+2-2k}}{(2k)!(2n+2-2k)!}\,\alpha^{n+1-k}\beta^k$, "
        r"where $B_j$ denotes the $j$th Bernoulli number.",
    ),
    rec(
        "RN-P2-C14-Entry21ii",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi^2/4$ and let $n$ be any integer. Then "
        r"$\displaystyle-\alpha\sum_{k=1}^{\infty}\chi(k)\frac{\operatorname{sech}(\alpha\pi k)}{k^{2n+1}}+(-\beta)^n\sum_{k=1}^{\infty}\chi(k)\frac{\operatorname{sech}(\beta\pi k)}{k^{2n+1}}$"
        r"$=\dfrac{\pi}{4}\sum_{k=0}^{n}\frac{(-1)^k E_{2k}E_{2n-2k}}{(2k)!(2n-2k)!}\,\alpha^{n-k}\beta^k$, "
        r"where $E_j$ denotes the $j$th Euler number.",
    ),
    rec(
        "RN-P2-C14-Entry21iii",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi^2$ and let $n$ be any integer. Then "
        r"$\displaystyle\alpha^{-n+1/2}\left\{1-L(2n)+\sum_{k=1}^{\infty}\frac{\chi(k)}{k^{2n}(e^{\alpha\pi k}-1)}\right\}$"
        r"$=\dfrac{(-1)^n\beta^{-n+1/2}}{2^{2n+1}}\sum_{k=1}^{\infty}\frac{1}{k^{2n}\cosh(\beta\pi k)}"
        r"$+\dfrac{1}{4}\sum_{k=0}^{n}\frac{(-1)^k E_{2k}B_{2n-2k}}{2^{2k}(2k)!(2n-2k)!}\,\beta^{n-k}\alpha^{k+1/2}$, "
        r"where $L(s)=\sum_{k=1}^{\infty}\chi(k)k^{-s}$ is the Dirichlet $L$-function for $\chi$.",
    ),
    rec(
        "RN-P2-C14-Entry22i",
        r"Let $x$ and $y$ be complex with $y/x$ not purely imaginary. Then "
        r"$\displaystyle\frac{\cosh\{\pi(x+y)/2\}+\cos\{\pi(x-y)/2\}-\cosh\{\pi(x-y)/2\}-\cos\{\pi(x+y)/2\}}{\pi xy}"
        r"\times\{\cosh(\pi x/2)-\cos(\pi x/2)\}\{\cosh(\pi y/2)-\cos(\pi y/2)\}$"
        r"$=\frac{3}{2}+\dfrac{3}{4\pi xy}\sum_{n=1}^{\infty}\frac{n\coth(\pi^2 n x/y)}{n^4+x^4}"
        r"$+\dfrac{3}{4\pi xy}\sum_{n=1}^{\infty}\frac{n\coth(\pi^2 n y/x)}{n^4+y^4}$.",
    ),
    rec(
        "RN-P2-C14-Entry22ii",
        r"Let $n\geq 0$. Then "
        r"$\displaystyle\int_0^{\infty}\frac{\cos(2\pi n x)}{\cosh(\pi x/\sqrt{2})+\cos(\pi x/\sqrt{2})}\,dx"
        r"=\sum_{k=1}^{\infty}\chi(k)\frac{k^3 e^{-\pi n k^2}}{\cosh(\pi k/2)}$.",
    ),
    rec(
        "RN-P2-C14-Entry22-Corollary",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=\pi^3/4$. Then "
        r"$\displaystyle\sum_{n=1}^{\infty}\frac{\chi(n)}{n\{\cosh(\alpha\pi n)+\cos(\alpha\pi n)\}}"
        r"+\sum_{n=1}^{\infty}\frac{\chi(n)}{n\cosh(\pi n/2)\cosh(\beta\pi n)}=\frac{\pi^2}{8}$.",
    ),
    rec(
        "RN-P2-C14-Entry22iii",
        r"Let $\alpha,\beta>0$ with $\alpha\beta=4\pi^3$ and let $\gamma$ denote Euler's constant. Then "
        r"$\displaystyle\frac{\pi}{720}+\sum_{n=1}^{\infty}\frac{\cos(\alpha\pi n)}{n\{\cosh(\alpha\pi n)-\cos(\alpha\pi n)\}}$"
        r"$=-\gamma+\ln(2\pi/\beta)+\sum_{n=1}^{\infty}\frac{1}{n(e^{2\pi n}-1)}+\sum_{n=1}^{\infty}\frac{\coth(\pi n)}{n(e^{\beta\pi n/2}-1)}$. "
        r"Furthermore, $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(e^{2\pi n}-1)}=\frac{1}{4}\ln(4/\pi)-\frac{\pi}{12}+\ln\Gamma(\tfrac{1}{4})$.",
    ),
    rec(
        "RN-P2-C14-Entry23i",
        r"$\displaystyle\sum_{n=0}^{\infty}\sum_{k=1}^{\infty}\frac{n}{k}\coth(\pi k)(-1)^t(kx)^{4n}\psi(4n)"
        r"=\frac{2}{x^2}\left\{\psi(-2)+h\right\}$, where the error $h$ is nearly equal to "
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{(2n)^{2n+1}\cos\{3(2n+1)\pi/4\}}{x^n n!}\,\psi(-2n-3)$ when $x$ is small, "
        r"and $\psi$ denotes the digamma function.",
    ),
    rec(
        "RN-P2-C14-Entry23ii",
        r"$\displaystyle\sum_{k=1}^{\infty}\sum_{n=0}^{\infty}k^{-1}\chi(k)\operatorname{sech}(\pi k/2)(-1)^n(kx)^{4n}\varphi(4n)"
        r"=-\frac{\varphi(0)}{8}-\frac{h}{2}$, where $h$ is nearly equal to "
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n(n/\sqrt{2})^n}{x^n n!}\,\varphi(-n)$ when $x$ is small.",
    ),
    rec(
        "RN-P2-C14-Entry24",
        r"For complex $z$, $\displaystyle\frac{\pi e^{-2\pi i z}}{2z\{\cosh(2\pi z)-\cos(2\pi z)\}}=8\pi z^3-4z^2+4z-\sum_{n=1}^{\infty}\frac{z^2}{(z+n)^2}-\sum_{n=1}^{\infty}\frac{n+4z}{(e^{2\pi n}-1)(4z^4+n^4)}$.",
    ),
    rec(
        "RN-P2-C14-Entry24i",
        r"For complex $z$, $\displaystyle\sum_{n=1}^{\infty}\frac{n}{z^2+n^2}=\frac{\pi}{2z}+\frac{z}{e^{2\pi z}-1}$.",
    ),
    rec(
        "RN-P2-C14-Entry24ii",
        r"Let $z$ be complex. Then $\displaystyle\frac{z}{e^{\pi z}+1}=2z-\sum_{n=0}^{\infty}\frac{z^2}{(2n+1)^2+z^2}$.",
    ),
    rec(
        "RN-P2-C14-Entry25",
        r"Let $z$ be complex. Then $\displaystyle\frac{\pi e^{-\pi z}}{4z\{\cosh(\pi z)+\cos(\pi z)\}}=8\pi z-\sum_{n=0}^{\infty}\frac{z^2}{(z+2n+1)^2}-\sum_{n=0}^{\infty}\frac{2n+1}{(e^{(2n+1)\pi}+1)(4z^4+(2n+1)^4)}$.",
    ),
    rec(
        "RN-P2-C14-Entry25i",
        r"$\displaystyle\sum_{k=1}^{\infty}\coth(\pi k)=\frac{\pi^2}{180}$.",
    ),
    rec(
        "RN-P2-C14-Entry25ii",
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{\coth(\pi k)}{k^7}=\frac{19\pi^7}{56700}$.",
    ),
    rec(
        "RN-P2-C14-Entry25iii",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{\tanh\{(2k+1)\pi/2\}}{(2k+1)^3}=\frac{\pi^3}{32}$.",
    ),
    rec(
        "RN-P2-C14-Entry25iv",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{\tanh\{(2k+1)\pi/2\}}{(2k+1)^7}=\frac{61\pi^7}{23040}$.",
    ),
    rec(
        "RN-P2-C14-Entry25v",
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{(-1)^{k+1}\operatorname{csch}(\pi k)}{k^3}=\frac{\pi^3}{360}$.",
    ),
    rec(
        "RN-P2-C14-Entry25vi",
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{(-1)^{k+1}\operatorname{csch}(\pi k)}{k^7}=\frac{13\pi^7}{453600}$.",
    ),
    rec(
        "RN-P2-C14-Entry25vii",
        r"$\displaystyle\sum_{k=1}^{\infty}\chi(k)\frac{\operatorname{sech}(\pi k/2)}{k}=\frac{\pi}{8}$.",
    ),
    rec(
        "RN-P2-C14-Entry25viii",
        r"$\displaystyle\sum_{k=1}^{\infty}\chi(k)\frac{\operatorname{sech}(\pi k/2)}{k^5}=\frac{\pi^5}{768}$.",
    ),
    rec(
        "RN-P2-C14-Entry25ix",
        r"$\displaystyle\sum_{k=1}^{\infty}\chi(k)\frac{\operatorname{sech}(\pi k/2)}{k^9}=\frac{23\pi^9}{1720320}$.",
    ),
    rec(
        "RN-P2-C14-Entry25x",
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{\chi(k)}{\pi(e^{\pi k}-1)}+\frac{1}{8}\sum_{k=1}^{\infty}\frac{1}{k^2\cosh(\pi k)}"
        r"=\frac{5\pi^2}{12}-\frac{1}{2}\int_0^1\frac{\tan^{-1}x}{x}\,dx$.",
    ),
    rec(
        "RN-P2-C14-Entry25xi",
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{1}{\{k^2+(k+1)^2\}\{\cosh\{(2k+1)\pi\}-\cosh\pi\}}=\frac{1}{2\sinh\pi}\left\{\frac{1}{\sinh\pi}+\coth\pi-\frac{\pi}{2}\tanh^2(\pi/2)\right\}$.",
    ),
    rec(
        "RN-P2-C14-Entry25xii",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{2k+1}{\{25+(2k+1)^4/100\}(e^{(2k+1)\pi}+1)}"
        r"=\frac{4689}{11890}-\frac{8}{\pi}\coth^2\!\left(\frac{5\pi}{2}\right)$.",
    ),
]
