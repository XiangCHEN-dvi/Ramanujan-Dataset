"""Part II, Chapter 15 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C15 = ["asymptotic-expansions-and-modular-forms"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C15}


CHAPTER_15 = [
    rec(
        "RN-P2-C15-Entry01",
        r"If $\varphi$ is such that the Euler–Maclaurin formula applies on $[0,\infty)$, then "
        r"$\displaystyle h\sum_{k=1}^\infty \varphi(kh)=\int_0^\infty \varphi(x)\,dx+F(h)$, "
        r"where $F(h)$ is the constant term obtained by expanding the left side and $F(0)=0$. "
        r"Formally, $F(h)=h\sum_{k=1}^m \varphi(kh)-\int_0^\infty \varphi(x)\,dx"
        r"$+\sum_{k=1}^m \frac{(-1)^{k+1}B_k}{k!}\,\varphi^{(k-1)}(0)\,h^k+hR_m$, "
        r"assuming $\varphi^{(k-1)}(0)=0$ for $1\le k\le m$.",
    ),
    rec(
        "RN-P2-C15-Entry01-Corollary",
        r"If $h\varphi(h)=ah^p+bh^q+\cdots$ with integers $2\le p<q<\cdots$, then "
        r"$\displaystyle h\sum_{k=1}^\infty \varphi(kh)=\int_0^\infty \varphi(x)\,dx-\frac{aB_p h^p}{p}-\frac{bB_q h^q}{q}-\cdots$, "
        r"where $B_n$ denotes the $n$th Bernoulli number. When most of $p,q,\ldots$ are odd integers "
        r"greater than $1$, the Bernoulli numbers vanish and $F(h)$ appears to terminate; the remaining "
        r"rapidly diminishing part of $F(h)$ cannot be expanded in ascending powers of $h$.",
    ),
    rec(
        "RN-P2-C15-Entry01-Example01",
        r"If $\varphi(h)=1/(1+h^2)$, then "
        r"$\displaystyle F(h)=\frac{\pi}{h}\coth\!\Bigl(\frac{\pi}{h}\Bigr)-\frac{\pi^2}{2}-\frac{h}{2}$, "
        r"and $F(h)+\tfrac{h}{2}\sim \pi/(e^{2\pi/h}-1)$ as $h\to 0+$.",
    ),
    rec(
        "RN-P2-C15-Entry01-Example02",
        r"If $\varphi(h)=e^{-h^2}$, then "
        r"$\displaystyle F(h)=-\frac{\sqrt{\pi}}{2}+\frac{\sqrt{\pi}}{2}\sum_{k=-\infty}^\infty e^{-\pi^2 k^2/h^2}$, "
        r"and $F(h)+\tfrac{h}{2}\sim e^{-\pi^2/h^2}$ as $h\to 0+$.",
    ),
    rec(
        "RN-P2-C15-Entry01-Examplei",
        r"As $x\to 0+$, "
        r"$\displaystyle\sum_{k=1}^\infty e^{-kx}\log k\sim \frac{-\gamma-\log x}{x}+\tfrac{1}{2}\log(2\pi)$, "
        r"where $\gamma$ denotes Euler's constant.",
    ),
    rec(
        "RN-P2-C15-Entry01-Exampleii",
        r"Let $d(n)$ denote the number of positive divisors of $n$. As $x\to\infty$, "
        r"$\displaystyle\sum_{n\le x} d(n)\sim x\log x+(2\gamma-1)x$, "
        r"where $\gamma$ denotes Euler's constant.",
    ),
    rec(
        "RN-P2-C15-Entry01-Exampleiii",
        r"If $p_k$ denotes the $k$th prime, then as $x\to 0+$, "
        r"$\displaystyle\sum_{k=1}^\infty e^{-p_k x}\sim -\frac{\log x}{2x}$.",
    ),
    rec(
        "RN-P2-C15-Entry01-Exampleiv",
        r"For $|x|<1$, write $\displaystyle\sum_{n=0}^\infty f(n)x^n$. Then "
        r"$f(n)$ is asymptotic to "
        r"$\displaystyle\frac{1}{4n\sqrt{n}}\Bigl\{\cosh(\pi\sqrt{n})-\frac{\cos(\pi\sqrt{n})}{\pi\sqrt{n}}\sinh(\pi\sqrt{n})\Bigr\}$.",
    ),
    rec(
        "RN-P2-C15-Entry03",
        r"Suppose that $m$ and $p$ denote positive integers. As $x\to 0+$, "
        r"$\displaystyle\sum_{k=1}^\infty e^{-xk^p}k^{m-1}\sim \frac{\Gamma(m/p)}{p\,x^{m/p}}"
        r"+\sum_{k=0}^\infty \frac{\zeta(1-m-pk)}{k!}\Bigl(-\frac{x}{p}\Bigr)^k$, "
        r"provided $m/p\notin\mathbb{Z}_{\le 0}$; if $m/p=-r\in\mathbb{Z}_{\le 0}$, the leading term involves "
        r"$\{\tfrac{1}{p}(\psi_r-\gamma)+\gamma-\tfrac{1}{p}\log x\}(-x)^r/r!$, "
        r"where $\psi_r=\sum_{j=1}^r 1/j$ and $\gamma$ is Euler's constant.",
    ),
    rec(
        "RN-P2-C15-Entry03-Corollary",
        r"Suppose that $p$ is a positive integer. As $x\to 0+$, "
        r"$\displaystyle\sum_{k=1}^\infty \frac{e^{-kpx}}{k}\sim -\frac{\log x}{p}+\gamma\Bigl(1-\frac{1}{p}\Bigr)"
        r"-\sum_{k=1}^\infty \frac{B_{pk}(-x/p)^k}{pk\,k!}$.",
    ),
    rec(
        "RN-P2-C15-Entry03-Exampleiv",
        r"As $x\to 0+$, "
        r"$\displaystyle\sum_{k=1}^\infty \frac{1-e^{-k^2 x}}{k^2}\sim \frac{x}{2}+\sqrt{\pi x}+O(\sqrt{x}\,e^{-\pi^2/x})$.",
    ),
    rec(
        "RN-P2-C15-Entry04",
        r"Let $p>0$ and let $m,d$ be complex numbers with $\operatorname{Re}(pd-m)>0$. Define "
        r"$\displaystyle h(x)=\sum_{k=1}^\infty \frac{k^{m-1}}{(1+xk^p)^d}$. "
        r"If $m/p\notin\mathbb{Z}_{\le 0}$, then as $x\to 0+$, "
        r"$\displaystyle h(x)\sim \frac{\Gamma(m/p)\,\Gamma(d-m/p)}{p\,\Gamma(d)\,x^{m/p}}"
        r"+\sum_{k=0}^\infty \frac{(d)_k\,\zeta(1-m-pk)}{k!}\Bigl(-\frac{x}{p}\Bigr)^k$, "
        r"where $(d)_k=\Gamma(d+k)/\Gamma(d)$.",
    ),
    rec(
        "RN-P2-C15-Entry07",
        r"As $x\to 0+$, "
        r"$\displaystyle\sum_{s=1}^\infty s^{m-1}\sigma_{n-m}(s)\,e^{-sx}\sim \frac{\Gamma(m)\,\zeta(1+m-n)}{x^m}"
        r"+\frac{\Gamma(n)\,\zeta(1+n-m)}{x^n}+\frac{\zeta(2-m)\,\zeta(2-n)}{1+n-m}\,x^{m+n-2}"
        r"+\sum_{k=0}^\infty \frac{\zeta(1-m-k)\,\zeta(1-n-k)\,\zeta(-k)(-x)^k}{k!}$, "
        r"provided $m\ne n$, $m\ne 1$, $n\ne 1$, and $m,n\notin\mathbb{Z}_{\le 0}$, "
        r"where $\sigma_r(s)=\sum_{d\mid s}d^r$.",
    ),
    rec(
        "RN-P2-C15-Entry08",
        r"If $x>0$, then "
        r"$\displaystyle\sum_{k=1}^\infty \frac{1}{k^2(e^{k^2/x}-1)}=\frac{\pi^2}{6}+\frac{1}{2x}+\frac{i}{4\sqrt{x}}"
        r"+\frac{1}{\pi}\sum_{k=1}^\infty \frac{1}{\sqrt{k}}\,"
        r"\frac{\cos\!\bigl(\tfrac{\pi}{4}+\tfrac{2\pi i}{\sqrt{x/k}}\bigr)-e^{-2\pi\sqrt{x/k}}\cos\!\bigl(\tfrac{\pi}{4}-\tfrac{2\pi i}{\sqrt{x/k}}\bigr)}"
        r"{\cosh\!\bigl(\tfrac{2\pi i}{\sqrt{x/k}}\bigr)-\cos\!\bigl(\tfrac{2\pi i}{\sqrt{x/k}}\bigr)}$.",
    ),
    rec(
        "RN-P2-C15-Entry10i",
        r"For each integer $n\ge 2$, "
        r"$\displaystyle\frac{B_{2n}}{4n}E_{2n}(\tau)-\frac{B_{2n}}{4n}=\sum_{k=1}^\infty \sigma_{2n-1}(k)e^{2\pi i k\tau}$ "
        r"can be expressed as a polynomial in $M$ and $N$. "
        r"For each positive integer $n$, "
        r"$\displaystyle f_n(q):=\sum_{k=1}^\infty \frac{k^{2n}q^k}{(1-q^k)^2}-b_n\frac{B_{2n}}{4n}E_{2n}(\tau)"
        r"$+\sum_{k=1}^n \frac{k^{2n-1}q^k}{1-q^k}$, where $b_1=\tfrac{1}{2}$ and $b_n=1$ if $n\ge 2$, "
        r"can be expressed as a polynomial in $M$ and $N$.",
    ),
    rec(
        "RN-P2-C15-Entry10ii",
        r"The degree of a series is the sum of the highest powers of the $n$th terms together with unity "
        r"if the series contains all powers of $x$ or if the powers of $x$ are in arithmetic progression. "
        r"If the coefficient of each $n$th term is homogeneous, the series is pure; otherwise mixed. "
        r"If $F(h)$ in Entry 1 terminates, the series is perfect; if not, imperfect. "
        r"If $F(h)=0$, the series is complete; otherwise incomplete. "
        r"A series is absolutely complete when it remains complete when transformed or split up. "
        r"A linear series can only be expressed by linear, double by double, treble by treble, pure by pure, "
        r"perfect by perfect, imperfect by imperfect, and absolutely complete by absolutely complete series, "
        r"adhering to the laws of indices; a mixed series can be split into pure series of different degrees.",
    ),
    rec(
        "RN-P2-C15-Entry10-Example01",
        r"Let $\displaystyle f_1(x)=\sum_{k=1}^\infty k^n x^k$ for $|x|<1$ and nonnegative integer $n$. "
        r"Then $f_1$ is a pure, linear, imperfect, incomplete series of degree $n+1$.",
    ),
    rec(
        "RN-P2-C15-Entry10-Example02",
        r"For real $x$, let $\displaystyle f_2(x)=\sum_{k=1}^\infty \frac{\sin(kx)}{k}$. "
        r"Then $f_2$ is a pure, linear, perfect, incomplete series of degree $0$.",
    ),
    rec(
        "RN-P2-C15-Entry10-Example03",
        r"For $\displaystyle F_{m,n}(x)=\sum_{j,k=1}^\infty j^m k^n e^{-jkx}$, $F_{m,n}$ is a pure double series "
        r"of degree $m+n+1$, and is incomplete; it is imperfect if $m+n$ is even and perfect if $m+n$ is odd.",
    ),
    rec(
        "RN-P2-C15-Entry10-Example04",
        r"For positive integers $m\ne n$, let $\displaystyle g_{m,n}(x)=\sum_{i,j,k=1}^\infty e^{-ijkx}j^m k^n$. "
        r"Then $g_{m,n}$ is a treble, pure series of degree $m+n+1$; it is incomplete, "
        r"imperfect when $m$ and $n$ are both even, and perfect when at least one of $m,n$ is odd.",
    ),
    rec(
        "RN-P2-C15-Entry10-Example05",
        r"For real $m,n$ with $n>0$ and $x>0$, let "
        r"$\displaystyle h_{m,n}(x)=\sum_{k=1}^\infty\sum_{j=0}^\infty \frac{(-1)^j(n)_j}{j!}\,k^m e^{-kx(n+2j)}$. "
        r"Then $h_{m,n}$ is a mixed double series of degree $m+n+1$ and is incomplete.",
    ),
    rec(
        "RN-P2-C15-Entry10-Example06",
        r"For $|x|<1$, consider the theta-function "
        r"$\displaystyle f(x)=\tfrac{1}{2}+\sum_{k=1}^\infty x^{k^2}=\tfrac{1}{2}+\sum_{k=-\infty}^\infty x^{k^2}$. "
        r"Then $f$ is a pure, perfect bilateral series of degree $1$.",
    ),
    rec(
        "RN-P2-C15-Entry10-Example07",
        r"For $|q|<1$, with "
        r"$\displaystyle L=1-24\sum_{k=1}^\infty \frac{kq^k}{1-q^k}$, "
        r"$\displaystyle M=1+240\sum_{k=1}^\infty \frac{k^3 q^k}{1-q^k}$, and "
        r"$\displaystyle N=1-504\sum_{k=1}^\infty \frac{k^5 q^k}{1-q^k}$, "
        r"the series $L$, $M$, and $N$ are perfect, pure double series of degrees $2$, $4$, and $6$, "
        r"respectively; all three are incomplete.",
    ),
    rec(
        "RN-P2-C15-Entry11",
        r"If $\alpha,\beta>0$ and $\alpha\beta=\pi^2$, then "
        r"$\displaystyle\frac{4}{\pi^2}\sum_{k=1}^\infty \frac{k^2}{\sinh^2(\alpha k)}"
        r"+\frac{4}{\pi^2}\sum_{k=1}^\infty \frac{k^2}{\sinh^2(\beta k)}"
        r"=2\alpha\sum_{k=1}^\infty k^2\log(1-e^{-2\alpha k})"
        r"+2\beta\sum_{k=1}^\infty k^2\log(1-e^{-2\beta k})$.",
    ),
    rec(
        "RN-P2-C15-Entry12i",
        r"For $|q|<1$, with $L$, $M$, $N$ as in Entry 10 Example 7, $E_n(\tau)$ the Eisenstein series of "
        r"weight $n$, and $\Delta(\tau)=q\prod_{n=1}^\infty(1-q^n)^{24}$, "
        r"$M^3-N^2=1728\,\Delta(\tau)$.",
    ),
    rec(
        "RN-P2-C15-Entry12ii",
        r"For $|q|<1$, $E_8(\tau)=M^2$.",
    ),
    rec(
        "RN-P2-C15-Entry12iii",
        r"For $|q|<1$, $E_{10}(\tau)=MN$.",
    ),
    rec(
        "RN-P2-C15-Entry12iv",
        r"For $|q|<1$, $E_{14}(\tau)=M^2N$.",
    ),
    rec(
        "RN-P2-C15-Entry12v",
        r"For $|q|<1$, "
        r"$\displaystyle\sum_{k=1}^\infty \frac{k^2 q^k}{(1-q^k)^2}=\frac{M-L^2}{288}$.",
    ),
    rec(
        "RN-P2-C15-Entry12vi",
        r"For $|q|<1$, "
        r"$\displaystyle\sum_{k=1}^\infty \frac{k^4 q^k}{(1-q^k)^2}=\frac{LM-N}{720}$.",
    ),
    rec(
        "RN-P2-C15-Entry12vii",
        r"For $|q|<1$, "
        r"$\displaystyle\sum_{k=1}^\infty \frac{k^6 q^k}{(1-q^k)^2}=\frac{M^2-LN}{1008}$.",
    ),
    rec(
        "RN-P2-C15-Entry12viii",
        r"For $|q|<1$, "
        r"$\displaystyle\sum_{k=1}^\infty \frac{k^8 q^k}{(1-q^k)^2}=\frac{LM^2-MN}{720}$.",
    ),
    rec(
        "RN-P2-C15-Entry12ix",
        r"For $|q|<1$, "
        r"$\displaystyle\sum_{k=0}^\infty\sum_{j=1}^\infty (-1)^k(2k+1)q^{j(j+1)/2}"
        r"=\sum_{k=0}^\infty (-1)^k(2k+1)^3 q^{k(k+1)/2}$.",
    ),
    rec(
        "RN-P2-C15-Entry12x",
        r"For $|q|<1$, "
        r"$\displaystyle M\sum_{k=1}^\infty \frac{(2k-1)q^k}{1-q^{2k}}"
        r"=\sum_{k=1}^\infty \frac{(2k-1)^5 q^k}{1-q^{2k}}$.",
    ),
    rec(
        "RN-P2-C15-Entry13i",
        r"For $|q|<1$, with $\displaystyle\Phi_n(q)=\sum_{k=1}^\infty \frac{k^n q^k}{1-q^k}$ and $L,M,N$ as above, "
        r"$691+65520\,\Phi_{11}(q)=441M^3+250N^2$.",
    ),
    rec(
        "RN-P2-C15-Entry13ii",
        r"For $|q|<1$, $3617+16320\,\Phi_{15}(q)=1617M^4+2000MN^2$.",
    ),
    rec(
        "RN-P2-C15-Entry13iii",
        r"For $|q|<1$, $43867-28728\,\Phi_{17}(q)=38367M^3N+5500N^3$.",
    ),
    rec(
        "RN-P2-C15-Entry13iv",
        r"For $|q|<1$, $174611+13200\,\Phi_{19}(q)=53361M^5+121250M^2N^2$.",
    ),
    rec(
        "RN-P2-C15-Entry13v",
        r"For $|q|<1$, $77683-552\,\Phi_{21}(q)=57183M^4N+20500MN^3$.",
    ),
    rec(
        "RN-P2-C15-Entry13vi",
        r"For $|q|<1$, $236364091+131040\,\Phi_{23}(q)=49679091M^6+176400000M^3N^2+10285000N^4$.",
    ),
    rec(
        "RN-P2-C15-Entry13vii",
        r"For $|q|<1$, $657931-24\,\Phi_{25}(q)=392931M^5N+265000M^2N^3$.",
    ),
    rec(
        "RN-P2-C15-Entry13viii",
        r"For $|q|<1$, $3392780147+6960\,\Phi_{27}(q)=489693897M^7+2507636250M^4N^2+395450000MN^4$.",
    ),
    rec(
        "RN-P2-C15-Entry13ix",
        r"For $|q|<1$, $1723168255201-171864\,\Phi_{29}(q)=815806500201M^6N+881340705000M^3N^3+26021050000N^5$.",
    ),
    rec(
        "RN-P2-C15-Entry13x",
        r"For $|q|<1$, $7709321041217+32640\,\Phi_{31}(q)=764412173217M^8+5323905468000M^5N^2+1621003400000M^2N^4$.",
    ),
    rec(
        "RN-P2-C15-Entry13-Note",
        r"For $|q|<1$, $\displaystyle\frac{dL}{dq}=\frac{L^2-M}{12}$, "
        r"$\displaystyle q\frac{dM}{dq}=\frac{LM-N}{3}$, and "
        r"$\displaystyle q\frac{dN}{dq}=\frac{LN-M^2}{2}$.",
    ),
    rec(
        "RN-P2-C15-Entry13-Examplei",
        r"For $|q|<1$, with $\displaystyle\Phi_{r,s}(q)=\sum_{i,k=1}^\infty j^r k^s q^{ik}$, "
        r"$20736\,\Phi_{4,5}(q)=15LM^2+10L^3M-20L^2N-4MN-L^5$.",
    ),
    rec(
        "RN-P2-C15-Entry13-Exampleii",
        r"For $|q|<1$, $1728\,\Phi_{2,7}(q)=2LM^2-MN-LN$.",
    ),
    rec(
        "RN-P2-C15-Entry13-Exampleiii",
        r"For $|q|<1$, $3456\,\Phi_{3,6}(q)=L^3M-3L^2N+3LM^2-MN$.",
    ),
    rec(
        "RN-P2-C15-Entry14",
        r"For an even integer $n>4$, define "
        r"$\displaystyle S_{2n}=\frac{(-1)^{n/2-1}B_{2n}}{4n}+\frac{(-1)^{n/2}}{2n}\sum_{k=1}^\infty \frac{k^{n-1}q^k}{1-q^k}$ "
        r"for $|q|<1$. Then "
        r"$\displaystyle\frac{(n+2)(n+3)}{20}S_{n+2}=\frac{2n(n-1)}{(n-2)!}S_4S_{n-2}"
        r"+\sum_{k=1}^{\lfloor(n-2)/4\rfloor}\Bigl\{\frac{(n+3-5k)(n-8-5k)}{2}-5(k-2)(k+3)\Bigr\}S_{2k+2}S_{n-2k}$, "
        r"where if $(n-2)/4$ is an integer the last summand is multiplied by $\tfrac{1}{2}$.",
    ),
    rec(
        "RN-P2-C15-Entry15ii",
        r"If the $p$th iterate of $f$ is $f^{(p)}(x)$ and the $q$th iterate of $\psi$ is $\psi^{(q)}(x)$, "
        r"and if the $r$th iterate of $F$ is $F^{(r)}(x)$, then the $r$th iterate of $f\circ F$ is "
        r"$(f\circ F)^{(r)}$, and the $r$th iterate of $F\circ f$ is $(F\circ f)^{(r)}$.",
    ),
    rec(
        "RN-P2-C15-Entry15-Corollary",
        r"One may add or subtract any constant and multiply or divide by any constant in $x$ or in each "
        r"function when forming iterates.",
    ),
    rec(
        "RN-P2-C15-Entry15-Corollary01",
        r"If $f^{(1)}(x)=x$ and $f^{(2)}(x)=x^2+4x$, then for $n=2^m$, "
        r"$\displaystyle f^{(n)}(x)=\Bigl(\frac{x+2+\sqrt{x^2+4x}}{2}\Bigr)^{\!n}"
        r"+\Bigl(\frac{x+2-\sqrt{x^2+4x}}{2}\Bigr)^{\!n}-2$.",
    ),
    rec(
        "RN-P2-C15-Entry15-Corollary02",
        r"If $f^{(1)}(x)=x$ and $f^{(2)}(x)=x^2-2$, then for $n=2^m$, "
        r"$\displaystyle f^{(n)}(x)=\Bigl(\frac{x+\sqrt{x^2-4}}{2}\Bigr)^{\!n}"
        r"+\Bigl(\frac{x-\sqrt{x^2-4}}{2}\Bigr)^{\!n}$.",
    ),
    rec(
        "RN-P2-C15-Entry15iii",
        r"If $f$ and $F$ have degrees $p$ and $q$, find $\varphi$ such that "
        r"$\sqrt[p]{\varphi(f(x))}=\sqrt[q]{\varphi(F(x))}=\chi(x)$. "
        r"Then the function for the $r$th degree is $\varphi^{-1}(\chi(x)^r)$, and for a self-repeating series "
        r"$S(x)$, $\displaystyle\frac{S(F(x))}{S(f(x))}=\Bigl(\frac{\psi(f(x))F'(x)}{\psi(F(x))f'(x)}\Bigr)^{n/pq}$ "
        r"for suitable $\psi$ and $n$.",
    ),
    rec(
        "RN-P2-C15-Entry15iii-Example",
        r"If $f^{(1)}(x)=x$ and $f^{(2)}(x)=x^2+2nx$, then for large $x$, "
        r"$\displaystyle f^{(3)}(x)\approx x^3+3nx^2+\frac{3n(n+1)}{2}x-\frac{n(n-1)(n-2)}{2x}+3(n+1)/2$.",
    ),
    rec(
        "RN-P2-C15-Entry16",
        r"If the modular equation of degree $n-1$ is "
        r"$\sqrt{\alpha\beta}+\sqrt{(1-\alpha)(1-\beta)}=1$, "
        r"then the modular equation of degree $(n-1)^2$ is "
        r"$\{\sqrt{\alpha(1-\beta)}-\sqrt{\beta(1-\alpha)}\}^n"
        r"=\{\sqrt{\alpha}-\sqrt{\beta}\}^n+\{\sqrt{1-\alpha}-\sqrt{1-\beta}\}^n$.",
    ),
]
