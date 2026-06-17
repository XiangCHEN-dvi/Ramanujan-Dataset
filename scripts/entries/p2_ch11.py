"""Part II, Chapter 11 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C11 = ["hypergeometric-series-ii"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C11}


CHAPTER_11 = [
    rec(
        "RN-P2-C11-Entry01",
        r"Let $\varphi$ be any function. Then, provided the series converges, "
        r"$\varphi(x)^{-r/2}\,{}_2F_1\!\left(r,m;2m;1-\dfrac{\varphi(-x)}{\varphi(x)}\right)$ is an even function of $x$.",
    ),
    rec(
        "RN-P2-C11-Entry02",
        r"For arbitrary parameters $r$ and $m$, "
        r"${}_2F_1\!\left(r,m;2m;\dfrac{2x}{1+x}\right)=(1+x)^r\,{}_2F_1\!\left(\tfrac{r}{2},\tfrac{r+1}{2};m+\tfrac{1}{2};x^2\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry03",
        r"For arbitrary parameters $r$ and $m$, "
        r"${}_2F_1\!\left(r,m;2m;\left(\dfrac{1-\sqrt{x}}{1+\sqrt{x}}\right)^{\!2}\right)"
        r"=(1+\sqrt{x})^{2r}\,{}_2F_1(r,r-m+1;m+1;x^2)$.",
    ),
    rec(
        "RN-P2-C11-Entry04",
        r"For arbitrary parameters $r$ and $m$, "
        r"${}_2F_1\!\left(\tfrac{r}{2},\tfrac{r+1}{2};m+\tfrac{1}{2};\left(\dfrac{1-\sqrt{x}}{1+\sqrt{x}}\right)^{\!2}\right)"
        r"=(1+\sqrt{x})^r\,{}_2F_1(r,r-m+1;m+1;x)$.",
    ),
    rec(
        "RN-P2-C11-Entry05",
        r"Putting $m=1$ in Entry 3, "
        r"${}_2F_1\!\left(r,1;2;\left(\dfrac{1-\sqrt{x}}{1+\sqrt{x}}\right)^{\!2}\right)"
        r"=(1+\sqrt{x})^{2r}\,{}_2F_1(r,r;2;x^2)$.",
    ),
    rec(
        "RN-P2-C11-Entry06",
        r"Putting $m=1$ in Entry 4, "
        r"${}_2F_1\!\left(\tfrac{r}{2},\tfrac{r+1}{2};\tfrac{3}{2};\left(\dfrac{1-\sqrt{x}}{1+\sqrt{x}}\right)^{\!2}\right)"
        r"=(1+\sqrt{x})^r\,{}_2F_1(r,r;2;x)$.",
    ),
    rec(
        "RN-P2-C11-Entry07",
        r"For arbitrary $m$, "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(m)_k(2x)^k}{(2m)_k k!}=e^{-x}\,{}_0F_1(m;x^2)$ (7.1).",
    ),
    rec(
        "RN-P2-C11-Entry08",
        r"Let $\varphi(x)$ be analytic for $|x-1|<R$, where $R>1$. Suppose that $m$ and $\varphi$ are such that the order of summation in "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{2^k(m)_k}{(2m)_k k!}\sum_{n=k}^{\infty}\frac{\varphi^{(n)}(1)(-1)^n(-n)_k}{n!}$ may be inverted. Then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{\varphi^{(k)}(0)\,2^k(m)_k}{(2m)_k k!}=\sum_{k=0}^{\infty}\frac{2^{2k}(m+\tfrac{1}{2})_k}{k!}\,\varphi^{(2k)}(1)$.",
    ),
    rec(
        "RN-P2-C11-Entry09",
        r"If $n$ is an integer, then "
        r"${}_0F_1\!\left(n+\tfrac{1}{2};-\tfrac{1}{4}(z-x)^2\right)"
        r"=\dfrac{2n-1}{2\sqrt{\pi}(-x)^{n/2}}\left\{e^x\,{}_2F_0(n,1-n;2x)+\cos(\pi n)e^{-x}\,{}_2F_0(n,1-n;-2x)\right\}$.",
    ),
    rec(
        "RN-P2-C11-Entry10",
        r"If $n$ is an integer, then "
        r"${}_0F_1\!\left(n+\tfrac{1}{2};-\tfrac{1}{4}(1-x)^2\right)"
        r"=\dfrac{2\sqrt{\pi}\,\Gamma(n+\tfrac{1}{2})}{\sqrt{\pi}\,x^n}\left\{\cos(\pi n)\sum_{k=0}^{\infty}\frac{(-1)^k(n)_{2k}(1-n)_{2k}}{(2k)!(2x)^{2k}}"
        r"-\sin(\pi n)\sum_{k=0}^{\infty}\frac{(-1)^k(n)_{2k+1}(1-n)_{2k+1}}{(2k+1)!(2x)^{2k+1}}\right\}$.",
    ),
    rec(
        "RN-P2-C11-Entry10-Corollary",
        r"Suppose that $n$ is an integer. Let $x_0$ be a root of ${}_0F_1(n+\tfrac{1}{2};-\tfrac{1}{4}x^2)=0$. "
        r"Let $\mu$ be an odd integer chosen so that $|x_0-\tfrac{1}{2}\pi(\mu+n)|$ is minimal. Then if $x_0$ is large, "
        r"$x_0\sim\dfrac{\pi(\mu+n)}{2}+\dfrac{n(1-n)}{\pi(\mu+n)}+\dfrac{n(1-n)\{7n(1-n)-6\}}{3\pi^3(\mu+n)^3}+\cdots$ (10.1).",
    ),
    rec(
        "RN-P2-C11-Entry11",
        r"If $\displaystyle\int_0^x\frac{\sin u}{u}\,du=\tfrac{\pi}{2}-r\cos(x-\theta)$ (11.1) and "
        r"$\displaystyle\int_0^x\frac{1-\cos u}{u}\,du=\gamma+\log x-r\sin(x-\theta)$ (11.2), where $\gamma$ denotes Euler's constant, then "
        r"$r\cos\theta\sim\sum_{k=0}^{\infty}\frac{(-1)^k(2k)!}{x^{2k+1}}$, "
        r"$r\sin\theta\sim\sum_{k=1}^{\infty}\frac{(-1)^{k+1}(2k-1)!}{x^{2k}}$, and "
        r"$r\sim\sum_{k=1}^{\infty}\frac{(-1)^{k+1}(2k-1)!}{k\,x^{2k}}$ (11.3)–(11.5) as $x\to\infty$.",
    ),
    rec(
        "RN-P2-C11-Entry11-Example01",
        r"$\displaystyle\int_0^{\pi/2}\cos(n\sin^2\theta)\,d\theta=0$.",
    ),
    rec(
        "RN-P2-C11-Entry11-Example02",
        r"$\displaystyle\int_0^{\pi/2}\cos(2n\sin^2\theta)\,d\theta=-\int_0^{\pi/2}\cos(n\sin\theta)\,d\theta$ (11.12).",
    ),
    rec(
        "RN-P2-C11-Entry11-Example03",
        r"$\displaystyle\int_0^{\pi/2}\cos\!\left(3\sin^2\theta\right)\,d\theta=\tfrac{1}{2}\int_0^{\pi/2}\cos(3\sin\theta)\,d\theta$.",
    ),
    rec(
        "RN-P2-C11-Entry12",
        r"If $x+y+z=\tfrac{1}{2}$, then "
        r"${}_2F_1(-x,-y;z;p)={}_2F_1(-2x,-2y;z;\tfrac{1}{2}(1-\sqrt{p}))$.",
    ),
    rec(
        "RN-P2-C11-Entry12-Corollary",
        r"$1+\dfrac{12+n}{4^2\cdot 8^2}x^2+\dfrac{(12+n)(52+n)}{4^2\cdot 8^2\cdot 12^2}x^4+\cdots$.",
    ),
    rec(
        "RN-P2-C11-Entry12-Example01",
        r"$1+\dfrac{1}{2^2}+\sum_{k=2}^{\infty}\frac{(1)_k(1-\tfrac{1}{2^3})(1-\tfrac{1}{4^3})\cdots(1-\tfrac{1}{(2k-2)^3})}{(2k)^2}x^k"
        r"$=1+\sum_{k=1}^{\infty}\frac{1}{k+1}\left(1+\tfrac{1}{1^3}\right)\left(1+\tfrac{1}{2^3}\right)\cdots\left(1+\tfrac{1}{k^3}\right)\left(1-\tfrac{1}{2}\right)^k$.",
    ),
    rec(
        "RN-P2-C11-Entry12-Example02",
        r"If $\alpha+\beta=1$, then "
        r"$\left(1+\dfrac{x}{2}\right)^{\!\gamma}{}_2F_1\!\left(\tfrac{\alpha+\gamma}{2},\tfrac{\beta+\gamma}{2};\gamma+1;x\right)"
        r"={}_2F_1\!\left(\alpha,\beta;\gamma+1;\tfrac{1}{2}(1-\sqrt{x})\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry13",
        r"If $\alpha+\beta+\gamma=0$, then "
        r"${}_2F_1(-\alpha,-\beta;\gamma+\tfrac{1}{2};x)={}_3F_2(-2\alpha,-2\beta,\gamma;\gamma+\tfrac{1}{2},2\gamma;x)$.",
    ),
    rec(
        "RN-P2-C11-Entry13-Corollary01",
        r"Putting $\alpha=(-1+i\sqrt{n})/4$, $\beta=(-1-i\sqrt{n})/4$, and $\gamma=\tfrac{1}{2}$ in Entry 13, "
        r"${}_2F_1\!\left(\tfrac{1-i\sqrt{n}}{4},\tfrac{1+i\sqrt{n}}{4};1;x\right)"
        r"={}_3F_2\!\left(\tfrac{-1+i\sqrt{n}}{2},\tfrac{-1-i\sqrt{n}}{2},\tfrac{1}{2};1,1;x\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry13-Corollary02",
        r"If $J_0$ denotes the ordinary Bessel function of order $0$, then for all $x$, "
        r"$J_0^2(i\sqrt{x})={}_1F_2(\tfrac{1}{2};1,1;x)$.",
    ),
    rec(
        "RN-P2-C11-Entry14",
        r"If $\alpha+\beta+1=\gamma+\delta$, then "
        r"$\dfrac{{}_2F_1(\alpha,\beta;\gamma;\tfrac{1}{2}(1-\sqrt{x}))}{{}_2F_1(\alpha,\beta;\delta;\tfrac{1}{2}(1-\sqrt{x}))}"
        r"={}_4F_3\!\left(\alpha,\beta,\tfrac{\alpha+\beta}{2},\tfrac{\gamma+\delta}{2};\gamma,\delta,\alpha+\beta;x\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry15",
        r"For any $x$, "
        r"$I_{\gamma-1}(2\sqrt{\delta x})\,I_{\delta-1}(2\sqrt{\gamma x})={}_0F_1(\gamma;x)\,{}_0F_1(\delta;x)"
        r"={}_2F_3\!\left(\tfrac{\gamma+\delta}{2},\tfrac{\gamma+\delta-1}{2};\gamma,\delta,\gamma+\delta-1;4x\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry16",
        r"If $x$ is arbitrary, then "
        r"${}_0F_2(m+1,n+1;x)\,{}_0F_2(m+1,n+1;-x)=\sum_{k=0}^{\infty}\frac{(-1)^k(m+n+2k+1)_k x^{2k}}{(m+1)_k(n+1)_k(m+n+2)_k(n+1)_k(2k)!k!}$ (16.1).",
    ),
    rec(
        "RN-P2-C11-Entry17",
        r"${}_0F_2(m+n+1,n+1;x)\,{}_0F_2(m+1,1-n;-x)"
        r"$=1+\sum_{k=1}^{\infty}\alpha_k\dfrac{(\tfrac{2m+n+k+2}{2})_k(2x)^k}{(m+n+1)_k(m+1)_k k!}$ (17.1), "
        r"where, for $k\ge 1$, "
        r"$\alpha_k=\dfrac{(-1)^{(k-1)/2}(k-1)!\,2^{k-1}}{((k+1)/2)!^2}$ if $k$ is odd and "
        r"$\alpha_k=\dfrac{(-1)^{k/2}(k-1)!\,2^{k-2}}{((k/2)!)^2}$ if $k$ is even (17.2).",
    ),
    rec(
        "RN-P2-C11-Entry18",
        r"${}_1F_1(-p;\gamma;-x)\,{}_1F_1(-p;\gamma;x)={}_2F_3(-p,p+\gamma;\gamma,\tfrac{\gamma}{2},\tfrac{\gamma+1}{2};x^2/4)$.",
    ),
    rec(
        "RN-P2-C11-Entry19",
        r"If $\alpha$ or $\beta$ is a nonnegative integer, "
        r"${}_2F_0(-\alpha,-\beta;x)\,{}_2F_0(-\alpha,-\beta;-x)=\sum_{k=0}^{\infty}\frac{(-\alpha)_k(-\beta)_k(-\alpha-\beta+k)_k x^{2k}}{k!}$.",
    ),
    rec(
        "RN-P2-C11-Entry20",
        r"If $x$ is arbitrary and $\alpha_k$, $k\ge 1$, is defined by (17.2), then "
        r"${}_1F_1(-m;n+1;-x)\,{}_1F_1(-m-n;1-n;x)"
        r"$=1+\sum_{k=1}^{\infty}\alpha_k\dfrac{(\tfrac{-2m-n-k}{2})_k(-2x)^k}{(n+1)_k k!}$ (20.1).",
    ),
    rec(
        "RN-P2-C11-Entry20-Example01",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{x^{3k}}{(3k)!}+\sum_{k=0}^{\infty}\frac{(-x/3)^{3k}}{(3k)!}"
        r"$=1+2\sum_{k=0}^{\infty}\frac{(-3x^2)^{3k}}{(6k)!}$.",
    ),
    rec(
        "RN-P2-C11-Entry20-Example02",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{x^k}{(k!)^2}\sum_{k=0}^{\infty}\frac{(-x)^k}{(k!)^2}"
        r"$=\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)_k x^{2k}}{(k!)^3((2k)!)^2}$.",
    ),
    rec(
        "RN-P2-C11-Entry20-Example03",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{x^{3k+1}}{(3k+1)!}+\sum_{k=0}^{\infty}\frac{(-1)^k x^{3k+1}}{(3k+1)!}"
        r"$=2\sum_{k=0}^{\infty}\frac{(-1)^k(3x^2)^{3k+1}}{(6k+2)!}$.",
    ),
    rec(
        "RN-P2-C11-Entry20-Example04",
        r"$\displaystyle\cos x\cosh x=\sum_{k=0}^{\infty}\frac{(-1)^k(2x^2)^{2k}}{(4k)!}$.",
    ),
    rec(
        "RN-P2-C11-Entry20-Example05",
        r"$\displaystyle\sin x\sinh x=\sum_{k=0}^{\infty}\frac{(-1)^k(2x^2)^{2k+1}}{(4k+2)!}$.",
    ),
    rec(
        "RN-P2-C11-Entry20-Example06",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{x^k}{(k!)^2}+\sum_{k=0}^{\infty}\frac{(-x)^k}{(k!)^2}=\sum_{k=0}^{\infty}\frac{(-x^2)^k}{(k!)^2(2k)!}$.",
    ),
    rec(
        "RN-P2-C11-Entry20-Example07",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{x^{2k}}{(2k)!}\sum_{k=0}^{\infty}\frac{(-x)^{2k}}{(2k)!}"
        r"$=\sum_{k=0}^{\infty}\frac{(-1)^k(2k+1)_k x^{4k}}{(k!)^3((2k)!)^2}$.",
    ),
    rec(
        "RN-P2-C11-Entry20-Example08",
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{x^k}{(2k+1)!}=\sum_{k=0}^{\infty}\frac{2^{6k}(2k)!}{(\tfrac{1}{2})_k}\dfrac{(x/16)^k}{(4k+1)!}$.",
    ),
    rec(
        "RN-P2-C11-Entry20-Example09",
        r"$\displaystyle{}_1F_1(1;n+1;x)\,{}_1F_1(1;n+1;-x)=\sum_{k=0}^{\infty}\frac{nx^{2k}}{(n+k)(n+2k)}$.",
    ),
    rec(
        "RN-P2-C11-Entry20-Example10",
        r"If $n$ is a nonnegative integer, then "
        r"${}_2F_0(-n,1;x)\,{}_2F_0(-n,1;-x)=\sum_{k=0}^{\infty}(-n)_k(-n+1+k)_k x^{2k}$.",
    ),
    rec(
        "RN-P2-C11-Entry21",
        r"For arbitrary $m$, $n$, and $x$, "
        r"${}_2F_1\!\left(m,n;\tfrac{m+n+1}{2};\tfrac{1+x}{2}\right)"
        r"$=\dfrac{\Gamma(m+\tfrac{1}{2})\Gamma(n+\tfrac{1}{2})}{\sqrt{\pi}\,\Gamma(\tfrac{m+n+1}{2})}\,{}_2F_1\!\left(\tfrac{m}{2},\tfrac{n}{2};\tfrac{1}{2};x^2\right)"
        r"$+\dfrac{\Gamma(m+\tfrac{1}{2})\Gamma(n+\tfrac{1}{2})}{\sqrt{\pi}\,\Gamma(\tfrac{m+n+1}{2})}\,\dfrac{x}{2}\,{}_2F_1\!\left(\tfrac{m+1}{2},\tfrac{n+1}{2};\tfrac{3}{2};x^2\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry22",
        r"Let $m$ be a nonpositive integer and put $p=\tfrac{1}{2}m(m-1)$ (22.1). "
        r"For each nonnegative integer $k$, let "
        r"$A_k=k(k-1)p^{k-1}+\dfrac{k(k-1)(k-2)(3k-1)}{5!}p^{k-2}+\cdots+\dfrac{2(k-1)!(2^{2k}-1)B_{2k}}{(2k)!}p"
        r"+\cdots+\dfrac{1\cdot 3\cdot 5\cdots(2k-1)}{2^{2k}}p$, "
        r"where $B_j$, $0\le j<\infty$, denotes the $j$th Bernoulli number. Then, if $|x|<\pi$, "
        r"$e^{-mx}\sum_{k=0}^{\infty}\frac{(-m)_k(\tfrac{1}{2})_k(1-e^{-2ix})^k}{(k!)^2}"
        r"$=1+\sum_{k=1}^{\infty}\frac{(-1)^k A_k x^{2k}}{2^k(k!)^2}$ (22.3).",
    ),
    rec(
        "RN-P2-C11-Entry22-Corollary",
        r"If $p=1$, then $A_k=A_k(1)=\dfrac{2^k(k!)^2}{(2k)!}$ for $k\ge 1$ (22.20). "
        r"If $p=3$, then $A_k=A_k(3)=\dfrac{3\cdot 2^k(k!)^2}{(2k)!}$ for $k\ge 1$ (22.21).",
    ),
    rec(
        "RN-P2-C11-Entry23",
        r"Ramanujan claims that if $\varphi(x)=C_1+J_1=C_2+J_2=\cdots=C_n+J_n$ and "
        r"if $C_1,C_2,C_3,\ldots,C_n$ appear to be similar, then they are all identically equal to $c$, "
        r"whence $\varphi(x)=c+J_1+J_2+\cdots+J_n$.",
    ),
    rec(
        "RN-P2-C11-Entry24",
        r"Let $\varphi$ be any function and define "
        r"$Q_r=\displaystyle\sum_{k=0}^{r}\frac{(r+1)_k}{k!}\,\varphi(r+k)$. Then "
        r"$\displaystyle\sum_{k=0}^{\infty}\varphi(k)(1-x)^k=\sum_{k=0}^{\infty}Q_k(-x)^k$.",
    ),
    rec(
        "RN-P2-C11-Entry24-Corollary01",
        r"Let $\varphi(r)$ be defined as in Entry 24 and let "
        r"$Q_r^*=\dfrac{\Gamma(m+1)}{\Gamma(m+1-r)\Gamma(r+1)}\sum_{k=0}^{r}\frac{(m+1)_k}{(m+1-r)_k}\,\varphi(m+k)$. Then "
        r"$\displaystyle\sum_{k=0}^{\infty}\varphi(m+k)(1-x)^{m+k}=\sum_{k=0}^{\infty}Q_k^*(-x)^k"
        r"$+\dfrac{(-1)^{m+1}}{(\log\frac{1}{1-x})^{m+1}}\sum_{k=0}^{\infty}P_k(\log(1-x))^k$.",
    ),
    rec(
        "RN-P2-C11-Entry24-Corollary02",
        r"Let $\alpha+\beta+\gamma+1=\omega+\delta$ with $\gamma>-1$. Then as $x\to 0+$, "
        r"$\dfrac{\Gamma(\alpha+1)\Gamma(\beta+1)\Gamma(\gamma+1)}{\Gamma(\omega+1)\Gamma(\delta+1)}"
        r"{}_3F_2(\alpha+1,\beta+1,\gamma+1;\omega+1,\delta+1;1-x)"
        r"$=-\log x-\psi(\alpha+1)-\psi(\beta+1)-2C+\sum_{k=1}^{\infty}\dfrac{(\omega-\gamma)_k(\delta-\gamma)_k}{(\alpha+k)(\beta+k)k!}x^k$, "
        r"where $\psi(z)=\Gamma'(z)/\Gamma(z)$ and $C$ denotes Euler's constant.",
    ),
    rec(
        "RN-P2-C11-Entry25",
        r"Suppose that $n$ is not an integer. Then "
        r"${}_2F_1(a,b;a+b+n+2;1-x)=\dfrac{\Gamma(a+b+n+2)\Gamma(-n)}{\Gamma(a+1)\Gamma(b+1)}"
        r"{}_2F_1(a+n+1,b+n+1;n+1;x)"
        r"$+\dfrac{\Gamma(a+b+n+2)\Gamma(n)x^{-n}}{\Gamma(a+n+1)\Gamma(b+n+1)}"
        r"{}_2F_1(a+1,b+1;-n+1;x)$.",
    ),
    rec(
        "RN-P2-C11-Entry25-Corollary01",
        r"If $n$ is a nonnegative integer, then "
        r"${}_2F_1(a,b;a+b+n+2;1-x)=\dfrac{\Gamma(a+b+n+2)\Gamma(n)x^{-n}}{\Gamma(a+n+1)\Gamma(b+n+1)}"
        r"$\displaystyle\sum_{k=0}^{n}\frac{(a+1)_k(b+1)_k x^k}{(-n+1)_k k!}"
        r"$+\dfrac{(-1)^n\Gamma(a+b+n+2)}{\Gamma(a+1)\Gamma(b+1)\Gamma(n+1)}"
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(a+n+1)_k(b+n+1)_k x^k}{(n+1)_k k!}"
        r"$\{ \psi(a+n+k+1)+\psi(b+n+k+1)-\psi(n+k+1)-\psi(k+1)+\log x\}x^k$, "
        r"where $\psi(z)=\Gamma'(z)/\Gamma(z)$. If $n=0$, the first sum on the right is understood to be $0$.",
    ),
    rec(
        "RN-P2-C11-Entry25-Corollary02",
        r"If $n$ is a nonpositive integer, then "
        r"${}_2F_1(a,b;a+b+n+2;1-x)=\dfrac{\Gamma(a+b+n+2)\Gamma(-n)}{\Gamma(a+1)\Gamma(b+1)}"
        r"$\displaystyle\sum_{k=0}^{-n-1}\frac{(a+n+1)_k(b+n+1)_k x^k}{(n+1)_k k!}"
        r"$+\dfrac{\Gamma(a+b+n+2)(-x)^{-n}}{\Gamma(a+n+1)\Gamma(b+n+1)\Gamma(1-n)}"
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(a+1)_k(b+1)_k x^k}{(1-n)_k k!}"
        r"$\{ \psi(a+k+1)+\psi(b+k+1)-\psi(k-n+1)-\psi(k+1)+\log x\}x^k$. "
        r"If $n=0$, the same convention as in Corollary 1 applies.",
    ),
    rec(
        "RN-P2-C11-Entry26",
        r"$\dfrac{\Gamma(a+1)\Gamma(b+1)}{\Gamma(a+b+2)}\,{}_2F_1(a+1,b+1;a+b+2;1-x)+\log x\,{}_2F_1(a+1,b+1;1;x)"
        r"$+\displaystyle\sum_{k=0}^{\infty}\frac{(a+1)_k(b+1)_k}{(k!)^2}\{\psi(a+k+1)+\psi(b+k+1)-2\psi(k+1)\}x^k=0$.",
    ),
    rec(
        "RN-P2-C11-Entry26-Corollary",
        r"$\pi\,{}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;1-x)=\log\!\left(\dfrac{1}{x}\right){}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;x)"
        r"$-4\sum_{k=1}^{\infty}\dfrac{(\tfrac{1}{2})_k^2}{(k!)^2}\sum_{j=1}^{k}\dfrac{1}{(2j-1)(2j)}x^k$.",
    ),
    rec(
        "RN-P2-C11-Entry26-Example",
        r"If $0<x<1$, then "
        r"$\displaystyle\int_0^{\pi/2}\int_0^{\pi/2}\frac{\tan(\varphi/2)\,d\theta\,d\varphi}{\sqrt{1-x\cos^2\theta\cos^2\varphi}}"
        r"$=\dfrac{\pi}{4}\int_0^{\pi/2}\frac{d\varphi}{\sqrt{1-(1-x)\sin^2\varphi}}+\tfrac{1}{2}\log x\int_0^{\pi/2}\frac{d\varphi}{\sqrt{1-x\sin^2\varphi}}$ (26.1)–(26.3).",
    ),
    rec(
        "RN-P2-C11-Entry27",
        r"For $|x|<1$, "
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{(\tfrac{1}{2})_k^2}{(k!)^2}\sum_{j=1}^{k}\frac{1}{2j-1}x^k"
        r"$=\log\!\left(\dfrac{1}{1-x}\right){}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;x)-\tfrac{1}{4}{}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;-x)$ (27.1).",
    ),
    rec(
        "RN-P2-C11-Entry27-Example01",
        r"$\exp\!\left(-\pi\dfrac{{}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;1-x)}{{}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;x)}\right)"
        r"$=\dfrac{x}{1-x}\left(1+\dfrac{x}{16}+\dfrac{x^2}{64}+\cdots\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry27-Example02",
        r"$\exp\!\left(-\dfrac{2\pi}{\sqrt{3}}\dfrac{{}_2F_1(\tfrac{1}{3},\tfrac{2}{3};1;1-x)}{{}_2F_1(\tfrac{1}{3},\tfrac{2}{3};1;x)}\right)"
        r"$=\dfrac{1}{27}\left(1+\dfrac{5x}{9}+\cdots\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry27-Example03",
        r"$\exp\!\left(-\dfrac{\pi}{\sqrt{8}}\dfrac{{}_2F_1(\tfrac{1}{4},1;1;1-x)}{{}_2F_1(\tfrac{1}{4},1;1;x)}\right)"
        r"$=\dfrac{1}{64}\left(1+\dfrac{5x}{8}+\cdots\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry27-Example04",
        r"$\exp\!\left(-2\pi\dfrac{{}_2F_1(\tfrac{1}{6},\tfrac{5}{6};1;1-x)}{{}_2F_1(\tfrac{1}{6},\tfrac{5}{6};1;x)}\right)"
        r"$=\dfrac{1}{432}\left(1+\dfrac{13x}{18}+\cdots\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry28",
        r"Let $\varphi$ denote a polynomial of degree $m$. Suppose that $n$ is not an integer and that "
        r"$\Re(a+b+m+n+1)<0$. Then "
        r"$\dfrac{\Gamma(a+1)\Gamma(b+1)\Gamma(n)}{\Gamma(a+b+n+2)}\sum_{k=0}^{m}\frac{(a+1)_k(b+1)_k\varphi(k)}{(1-n)_k k!}"
        r"$+\dfrac{\Gamma(a+n+1)\Gamma(b+n+1)\Gamma(-n)}{\Gamma(a+b+n+2)}\sum_{k=0}^{m}\frac{(a+n+1)_k(b+n+1)_k\varphi(n+k)}{(n+1)_k k!}"
        r"$=\dfrac{\Gamma(a+n+1)\Gamma(b+n+1)\Gamma(a+1)\Gamma(b+1)}{\Gamma(a+b+n+2)}\sum_{k=0}^{m}\frac{(a+1)_k(b+1)_k A_k\varphi(0)}{(a+b+n+2)_k k!}$.",
    ),
    rec(
        "RN-P2-C11-Entry28-Corollary",
        r"Assume the hypotheses of Entry 28. Then "
        r"$\dfrac{\Gamma(a+1)\Gamma(b+1)}{\Gamma(a+b+2)}\sum_{k=0}^{m}\frac{(a+1)_k(b+1)_k A_k\varphi(0)}{(a+b+2)_k k!}"
        r"$+\sum_{k=0}^{m}\frac{(a+1)_k(b+1)_k\varphi'(k)}{(k!)^2}+\sum_{k=0}^{m}\frac{(a+1)_k(b+1)_k\varphi(k)}{(k!)^2}"
        r"$\{\psi(a+1+k)+\psi(b+1+k)-2\psi(k+1)\}=0$.",
    ),
    rec(
        "RN-P2-C11-Entry29i",
        r"If $\Re(\alpha+\beta+\gamma-\omega-\delta)<0$ and $\Re(\omega-\gamma-1)<0$, then "
        r"${}_3F_2(\alpha,\beta,\gamma;\omega,\delta;1)"
        r"$=\dfrac{\Gamma(\omega)\Gamma(\omega-\alpha-\beta)}{\Gamma(\omega-\alpha)\Gamma(\omega-\beta)}"
        r"{}_3F_2(\alpha,\beta,\delta-\gamma;\alpha+\beta-\omega+1,\delta;1)"
        r"$+\dfrac{\Gamma(\omega)\Gamma(\delta)\Gamma(\alpha+\beta-\gamma)\Gamma(\omega+\delta-\alpha-\beta-\gamma)}{\Gamma(\alpha)\Gamma(\beta)\Gamma(\delta-\gamma)\Gamma(\omega+\delta-\alpha-\beta)}"
        r"{}_3F_2(\omega-\alpha,\omega-\beta,\omega+\delta-\alpha-\beta-\gamma;\omega-\alpha-\beta+1,\omega+\delta-\alpha-\beta;1)$.",
    ),
    rec(
        "RN-P2-C11-Entry29ii",
        r"If $\alpha$, $\beta$, or $\gamma$ is a nonnegative integer, "
        r"${}_3F_2(-2\alpha,-2\beta,-\gamma;-\alpha-\beta+\tfrac{1}{2},\omega;1)"
        r"={}_4F_3(-\alpha,-\beta,-\gamma,\gamma+\omega;-\alpha-\beta+\tfrac{1}{2},\tfrac{1}{2}\omega,\tfrac{1}{2}(\omega+1);1)$ (29.1).",
    ),
    rec(
        "RN-P2-C11-Entry30",
        r"Let $\alpha+\beta+1=\gamma+\delta$, $c=\Gamma(\gamma)\Gamma(\beta)/(\Gamma(\delta)\Gamma(\alpha))$, and "
        r"$y=c\,{}_2F_1(\alpha,\beta;\delta;1-x)/{}_2F_1(\alpha,\beta;\gamma;x)$. Then "
        r"$y'=\dfrac{1}{(\gamma-1)\,{}_2F_1(\alpha,\beta;\gamma;x)^2}\,"
        r"W\!\left({}_2F_1(\alpha,\beta;\gamma;x),\,x^{1-\gamma}{}_2F_1(\delta-\alpha,\delta-\beta;2-\gamma;x)\right)$, "
        r"where $W(f,g)=fg'-f'g$ denotes the Wronskian (30.1).",
    ),
    rec(
        "RN-P2-C11-Entry30-Corollary",
        r"Let $y=\dfrac{\sin(\pi n)\,{}_2F_1(n,1-n;1;1-x)}{{}_2F_1(n,1-n;1;x)}$. Then "
        r"$y'=\dfrac{1}{x(1-x)\,{}_2F_1(n,1-n;1;x)}$ (30.3).",
    ),
    rec(
        "RN-P2-C11-Entry31i",
        r"Let $y={}_2F_1(\alpha,\beta;\gamma;x)$. Then "
        r"$(\alpha-1)(\beta-1)\displaystyle\int_0^x y\,dx-x(1-x)y'=(\gamma-1)(\gamma-1)-(\alpha+\beta-1)xy$.",
    ),
    rec(
        "RN-P2-C11-Entry31ii",
        r"Let $\alpha+\beta+1=\gamma+\delta$. Assume that $n>1$ and that $n>\Re\gamma$. If $y=y(x)={}_2F_1(\alpha,\beta;\gamma;x)$, then "
        r"$\dfrac{y(x)\displaystyle\int_0^x s\,y(s)(1-s)^\delta y^2(s)\left[\int_0^s t^{n-2}y(t)\,dt\right]ds}"
        r"{x^{n-\gamma}(1-x)^{1-\delta}}"
        r"$=\dfrac{1}{(n-\gamma)(n-1)}"
        r"{}_3F_2\!\left(\dfrac{n-\alpha}{n},\dfrac{n-\beta}{n},\dfrac{1}{n};n,\dfrac{n-\gamma+1}{n};x\right)$ (31.1).",
    ),
    rec(
        "RN-P2-C11-Entry31-Corollary",
        r"If $n$ is arbitrary and $y={}_2F_1(n,1-n;1;x)$, then $x(x-1)y'=n(n-1)\displaystyle\int_0^x y\,dx$.",
    ),
    rec(
        "RN-P2-C11-Entry32i",
        r"If $\varphi$ is any function, then, provided the series converges, "
        r"$\varphi(x)^{-1/4}\,{}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;1-\dfrac{\varphi(-x)}{\varphi(x)}\right)$ "
        r"is always an even function of $x$ (obtained from Entry 1 with $r=m=\tfrac{1}{2}$).",
    ),
    rec(
        "RN-P2-C11-Entry32ii",
        r"If $\tfrac{1}{2}<x<2$, then "
        r"${}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;1-1/x)=\sqrt{x}\,{}_2F_1(\tfrac{1}{4},\tfrac{1}{2};1;1-x)$.",
    ),
    rec(
        "RN-P2-C11-Entry32iii",
        r"${}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;1-\left(\dfrac{1-\sqrt{x}}{1+\sqrt{x}}\right)^{\!2}\right)"
        r"=(1+x)\,{}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;x^2)$.",
    ),
    rec(
        "RN-P2-C11-Entry32iv",
        r"${}_2F_1\!\left(\tfrac{1}{4},\tfrac{1}{4};1;1-\left(\dfrac{1-\sqrt{x}}{1+\sqrt{x}}\right)^{\!2}\right)"
        r"=(1+x)^2\,{}_2F_1(\tfrac{1}{4},\tfrac{1}{4};1;x^4)$.",
    ),
    rec(
        "RN-P2-C11-Entry32v",
        r"$(1+n^2)^{1/4}\,{}_2F_1\!\left(\tfrac{1}{4},\tfrac{1}{4};1;\tfrac{1}{2}(1+in)\right)"
        r"$=\tfrac{1}{2}(1+i)\,{}_2F_1\!\left(\tfrac{1}{4},\tfrac{1}{4};1;\tfrac{1}{2}\left(1+\dfrac{i}{n}\right)\right)"
        r"$+\tfrac{1}{2}(1-i)\,{}_2F_1\!\left(\tfrac{1}{4},\tfrac{1}{4};1;\tfrac{1}{2}\left(1-\dfrac{i}{n}\right)\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry33i",
        r"Putting $r=m=\tfrac{1}{2}$ in Entry 2, "
        r"${}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;\dfrac{2x}{1+x}\right)=\sqrt{1+x}\,{}_2F_1\!\left(\tfrac{1}{4},\tfrac{3}{4};\tfrac{3}{2};x^2\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry33ii",
        r"Putting $x=y=\tfrac{1}{2}$, $z=1$ in Entry 12 and replacing $p$ by $x$, "
        r"${}_2F_1\!\left(-\tfrac{1}{2},-\tfrac{1}{2};1;x\right)={}_2F_1(-1,-1;1;\tfrac{1}{2}(1-\sqrt{x}))$.",
    ),
    rec(
        "RN-P2-C11-Entry33iii",
        r"Putting $\alpha=\beta=-\tfrac{1}{2}$, $\gamma=\tfrac{1}{2}$ in Entry 13, "
        r"${}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;x\right)={}_3F_2(-1,-1,\tfrac{1}{2};1,1;x)$.",
    ),
    rec(
        "RN-P2-C11-Entry33iv",
        r"Putting $r=m=\tfrac{1}{2}$ in Entry 4, "
        r"${}_2F_1\!\left(\tfrac{1}{4},\tfrac{3}{4};\tfrac{3}{2};\left(\dfrac{1-\sqrt{x}}{1+\sqrt{x}}\right)^{\!2}\right)"
        r"=\sqrt{1+x}\,{}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};2;x\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry33v",
        r"For $|z|<1$, "
        r"${}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;z\right)=(1-z)^{-1/2}\,{}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;\dfrac{z}{z-1}\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry33-Example01",
        r"Replacing $x$ by $-x$ in Entry 33(iv) and using Entry 32(ii), "
        r"$\sqrt{1+x}\,{}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;-x\right)=(1+x)^{-1}\,{}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;\dfrac{-4x}{(1-x)^2}\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry33-Example02",
        r"$\sqrt{\dfrac{1-x}{x}}\,{}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;x\right)"
        r"$-\dfrac{1+x}{2x}\sqrt{1+x}\,{}_2F_1\!\left(\tfrac{3}{4},\tfrac{3}{4};1;\dfrac{4x}{1+x}\right)"
        r"$=\dfrac{1}{1+x}\,{}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;x^{-1}\right)"
        r"$-\,{}_2F_1\!\left(\tfrac{3}{4},\tfrac{3}{4};1;\dfrac{-4x}{(1-x)^2}\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry33-Example03",
        r"Applying Entry 33(v) with $x$ replaced by $-4x/(1-x)^2$ and then using Example 02 yields a transformation "
        r"between ${}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;x)$ and ${}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;-4x/(1-x)^2)$.",
    ),
    rec(
        "RN-P2-C11-Entry34",
        r"Numerical values: "
        r"(a) $\pi^{1/4}/\Gamma(\tfrac{3}{4})=1.08643481121330801457531612$; "
        r"(b) $\Gamma^2(\tfrac{1}{4})/\pi^{3/2}=1.311028777146060$; "
        r"(c) $4\sqrt{2\pi}/\Gamma^2(\tfrac{1}{4})=1.1803405990160926$; "
        r"(d) $\pi^{3/2}/(\Gamma(\tfrac{1}{4})\Gamma(\tfrac{3}{4}))=0.2696763005941910$; "
        r"(e) $\pi^{3/2}/\Gamma^2(\tfrac{3}{4})=3.7081493546027344$.",
    ),
    rec(
        "RN-P2-C11-Entry34i",
        r"If $|x|<1$, then "
        r"${}_2F_1(\tfrac{1}{2},\tfrac{1}{2};1;\tfrac{1}{2}(1+x))=\pi\,{}_2F_1(\tfrac{1}{4},\tfrac{1}{4};\tfrac{1}{2};x^2)+\pi x\,{}_2F_1(\tfrac{1}{4},\tfrac{1}{4};\tfrac{3}{2};x^2)$.",
    ),
    rec(
        "RN-P2-C11-Entry34ii",
        r"${}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;\tfrac{1+x^2}{1-x^2}\right)"
        r"$=\pi\,{}_2F_1(\tfrac{1}{2},\tfrac{1}{4};\tfrac{1}{2};x^4)+\pi x(1+x^2)^{3/2}\,{}_2F_1(\tfrac{1}{4},\tfrac{1}{2};\tfrac{3}{2};x^4)$ (34.3).",
    ),
    rec(
        "RN-P2-C11-Entry34iii",
        r"$\dfrac{\pi}{4}\,{}_2F_1\!\left(\tfrac{1}{2},\tfrac{3}{4};1;\tfrac{1+x}{2}\right)-\dfrac{\pi}{4}\,{}_2F_1\!\left(\tfrac{1}{2},\tfrac{3}{4};1;\tfrac{1-x}{2}\right)"
        r"$=x\sum_{n=0}^{\infty}\frac{n!\,x^{2n}}{(\tfrac{3}{2})_n(\tfrac{1}{2})_n}\,{}_3F_2\!\left(\tfrac{1}{2},\tfrac{1}{2},-n;\tfrac{1}{2},\tfrac{1}{2};x^2\right)"
        r"$=x+\dfrac{x^3}{2}+\dfrac{41x^5}{120}+\dfrac{21x^7}{80}+\cdots$.",
    ),
    rec(
        "RN-P2-C11-Entry34-Example01",
        r"${}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;\tfrac{1}{2}(1+x)\right)"
        r"$=\pi(1-x^2)^{-1/4}\,{}_2F_1\!\left(\tfrac{1}{4},\tfrac{1}{4};1;\dfrac{x^2}{1-x^2}\right)"
        r"$+\pi x(1-x^2)^{-3/4}\,{}_2F_1\!\left(\tfrac{1}{4},\tfrac{1}{4};\tfrac{3}{2};\dfrac{x^2}{1-x^2}\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry34-Example02",
        r"${}_2F_1\!\left(\tfrac{1}{2},\tfrac{1}{2};1;\tfrac{1+x^2}{1-x^2}\right)"
        r"$=\pi\,{}_2F_1\!\left(\tfrac{1}{4},\tfrac{1}{4};1;\dfrac{x^4}{1-x^4}\right)"
        r"$+\pi x(1+x^2)\,{}_2F_1\!\left(\tfrac{1}{4},\tfrac{1}{4};\tfrac{3}{2};\dfrac{x^4}{1-x^4}\right)$.",
    ),
    rec(
        "RN-P2-C11-Entry35i",
        r"If $n$ is arbitrary, then $\cos(2n\sin^{-1}x)={}_2F_1(n,-n;\tfrac{1}{2};x^2)$.",
    ),
    rec(
        "RN-P2-C11-Entry35ii",
        r"If $n$ is arbitrary, then $\sin(2n\sin^{-1}x)=2nx\,{}_2F_1(\tfrac{1}{2}+n,\tfrac{1}{2}-n;\tfrac{1}{2};x^2)$.",
    ),
    rec(
        "RN-P2-C11-Entry35iii",
        r"If $n$ is arbitrary, then "
        r"$(1-x^2)^{-1/2}\cos(2n\sin^{-1}x)={}_2F_1(\tfrac{1}{2}+n,\tfrac{1}{2}-n;\tfrac{1}{2};x^2)$.",
    ),
    rec(
        "RN-P2-C11-Entry36i",
        r"For $n$ real and $k\ge 2$, let "
        r"$b_k(n)=\begin{cases}n^2(n^2-2^2)(n^2-4^2)\cdots(n^2-(k-2)^2), & k\text{ even},\\"
        r"n(n^2-1^2)(n^2-3^2)\cdots(n^2-(k-2)^2), & k\text{ odd}.\end{cases}$ "
        r"If $2-2\sqrt{2}\le x\le 2+2\sqrt{2}$, then "
        r"$(x+1)^{n/2}-(x+1)^{-n/2}=\dfrac{nx}{2\sqrt{2}}+\sum_{k=1}^{\infty}\dfrac{b_{2k+1}(n)}{ (2k+1)!}\left(\dfrac{x}{2\sqrt{2}}\right)^{2k+1}$ (36.1).",
    ),
    rec(
        "RN-P2-C11-Entry36ii",
        r"With $b_k(n)$ as in Entry 36(i) and $2-2\sqrt{2}\le x\le 2+2\sqrt{2}$, "
        r"$(x+1)^{n/2}+(x+1)^{-n/2}=2+\sum_{k=1}^{\infty}\dfrac{b_{2k}(n)}{(2k)!}\left(\dfrac{x}{2\sqrt{2}}\right)^{2k}$ (36.2).",
    ),
    rec(
        "RN-P2-C11-Entry36iii",
        r"Let $n$ be real and suppose that $\left|\dfrac{x}{(1+x)^{3/2}}\right|\le 3/2$. Then "
        r"$(1+\sqrt{1+4x})^n-(1-\sqrt{1+4x})^n"
        r"$=2\left\{nx(1+x)^{(n-3)/2}+\dfrac{n(n-5)(n-7)}{4\cdot 3!}x^3(1+x)^{(n-9)/2}+\cdots\right\}$ (36.5).",
    ),
    rec(
        "RN-P2-C11-Entry36iv",
        r"Under the same hypothesis as Entry 36(iii), "
        r"$\dfrac{1}{2}\left[(1+\sqrt{1+4x})^n+(1-\sqrt{1+4x})^n\right]"
        r"$=(1+x)^{n/2}+\dfrac{n(n-4)}{2^2\cdot 2!}x^2(1+x)^{(n-6)/2}+\dfrac{n(n-6)(n-8)(n-10)}{2^2\cdot 4!}x^4(1+x)^{(n-12)/2}+\cdots$ (36.7).",
    ),
]
