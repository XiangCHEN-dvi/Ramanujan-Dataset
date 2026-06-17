"""Part II, Chapter 12 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C12 = ["continued-fractions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C12}


CHAPTER_12 = [
    rec(
        "RN-P2-C12-Entry01",
        'Let $a_1,a_2,\\ldots,a_r$ and $b_1,b_2,\\ldots,b_r$ be complex numbers with $a_n\\ne 0$ for each positive integer $n$. Define $N_{-1}=0$,$N_0=1$, $D_{-1}=0$, $D_0=1$, $N_k=b_kN_{k-1}+a_k N_{k-2}$ and $D_k=b_k D_{k-1}+a_k D_{k-2}$ for $k\\ge 1$. Then for $r\\ge 1$,$\\displaystyle\\cfrac{a_1}{b_1+\\cfrac{a_2}{b_2+\\cdots+\\cfrac{a_r}{b_r}}}=\\cfrac{a_1N_{r-1}}{D_r}=\\sum_{k=1}^r(-1)^{k+1}\\frac{a_1\\cdots a_k}{D_{k-1}D_k}$.',
    ),
    rec(
        "RN-P2-C12-Entry01-Corollary",
        'Let $a_1,a_2,\\ldots,a_r$ be nonzero complex numbers with $a_j+a_{j+1}\\ne 0$ for $j\\ge 1$ and $r\\ge 3$. Define $D_{-1}=0$, $D_0=1$, and $D_k=D_{k-1}+a_k D_{k-2}$ for $k\\ge 1$. Then $\\displaystyle\\cfrac{a_1}{1+\\cfrac{a_2}{1+\\cdots+\\cfrac{a_r}{1}}}=\\displaystyle\\sum_{k=1}^r(-1)^{k+1}\\frac{a_1\\cdots a_k}{D_{k-1}D_k}$.',
    ),
    rec(
        "RN-P2-C12-Entry02",
        'Let $x,a_1,a_2,\\ldots$ be nonzero complex numbers and define $f_n(x)=\\displaystyle\\sum_{k=1}^n\\frac{a_1a_2\\cdots a_k x^k}{b_1b_2\\cdotsb_k}$ for each nonnegative integer $n$. If $\\displaystyle\\lim_{n\\to\\infty}f_n(x)=\\infty$, then $a_1=\\displaystyle\\cfrac{a_1x}{x-a_2+\\cfrac{a_2 x}{x-a_3+\\cfrac{a_3 x}{x-a_4+\\cdots}}}$.',
    ),
    rec(
        "RN-P2-C12-Entry03",
        'If $x,a_1,a_2,\\ldots$ are arbitrary complex numbers, then $x=a_1+\\Bigl(x^2+a_1(a_1-2a_2)-2a_1\\bigl(x^2+a_2(a_2-2a_3)-2a_2(\\cdots)\\bigr)^{1/2}\\Bigr)^{1/2}$.',
    ),
    rec(
        "RN-P2-C12-Entry04",
        'Let $a$, $n$, and $x$ be arbitrary complex numbers and put $f(x)=x+n+a$. Then $f(x)=\\Bigl(ax+(n+a)^2+x\\bigl(a(x+n)+(n+a)^2+(x+n)f(x+2n)\\bigr)\\Bigr)^{1/2}$ (formally, by iterated substitution).',
    ),
    rec(
        "RN-P2-C12-Entry04-Example01",
        '$\\displaystyle 3=\\Bigl(1+2\\bigl(1+3(1+4(\\cdots)^{1/2})^{1/2}\\bigr)^{1/2}\\Bigr)^{1/2}$.',
    ),
    rec(
        "RN-P2-C12-Entry04-Example02",
        '$\\displaystyle 4=\\Bigl(6+2\\bigl(7+3(8+4(\\cdots)^{1/2})^{1/2}\\bigr)^{1/2}\\Bigr)^{1/2}$.',
    ),
    rec(
        "RN-P2-C12-Entry05i",
        '$\\displaystyle 2\\cos\\theta=\\Bigl(2+2\\cos 2\\theta\\Bigr)^{1/2}=\\Bigl(2+\\bigl(2+2\\cos4\\theta\\bigr)^{1/2}\\Bigr)^{1/2}=\\Bigl(2+\\bigl(2+(2+2\\cos8\\theta)^{1/2}\\bigr)^{1/2}\\Bigr)^{1/2}=\\cdots$ (valid only for $\\theta=0$ withoutsign choices).',
    ),
    rec(
        "RN-P2-C12-Entry05ii",
        'If either $|\\theta|\\le\\pi/6$ or $5\\pi/6\\le\\theta\\le 7\\pi/6$, then $\\displaystyle 2\\cos\\theta=\\Bigl(2\\cos 3\\theta+3\\bigl(2\\cos3\\theta+3(\\cdots)^{1/3}\\bigr)^{1/3}\\Bigr)^{1/3}$.',
    ),
    rec(
        "RN-P2-C12-Entry05iii",
        "Formally, $\\displaystyle 2\\cos\\theta=\\Bigl(6\\cos\\theta+\\bigl(6\\cos 3\\theta+(6\\cos 9\\theta+\\cdots)^{1/3}\\bigr)^{1/3}\\Bigr)^{1/3}$(Ramanujan's second part of Entry 5(ii)).",
    ),
    rec(
        "RN-P2-C12-Entry06",
        'Let $a>0$, $a\\ne 1$, and let $n$ be a nonnegative integer. In the field of formal power series, put $f_n(v)=\\sum_{j=0}^\\infty a_j(n)v^j$with $a_0(n)=1$, $a_1(n)=-a^{-n}$, and for $j\\ge 2$, $a_j(n)=\\frac{2}{a^j-1}\\sum_{k=1}^{j-1}k a_k(n)a_{j-k}(n)$. Then $\\displaystyle\\cfrac{a}{2}+\\cfrac{a(a-2)}{2a}+\\cfrac{a(a-2)}{2a}+\\cdots+\\cfrac{a}{2a^n}$ (with $n$ iterated radicals on the left) equals$-f_n(v)$, and $f_n(v)=1-\\frac{v}{a^n}+\\frac{(v/a^n)^2}{2(a-1)}-\\frac{(v/a^n)^3}{2(a-1)(a^2-1)}+\\frac{(v/a^n)^4(a+5)}{8(a-1)(a^2-1)(a^3-1)}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry07",
        'If $x$ is not a negative integer, then $\\displaystyle 1=\\cfrac{x}{x+1}+\\cfrac{x+1}{x+2}+\\cfrac{x+2}{x+3}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry07-Corollary",
        '$\\displaystyle 1=\\cfrac{2}{1}+\\cfrac{3}{2}+\\cfrac{4}{3}+\\cfrac{5}{4}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry08",
        'Let $n$ be a positive integer and suppose $x\\ne -ka$ for $1\\le k\\le n$. Then $\\displaystyle\\sum_{k=1}^n\\frac{(-1)^{k+1}}{(x+a)(x+2a)\\cdots(x+ka)}=\\cfrac{1}{x+a}+\\cfrac{x+a}{x+2a-1}+\\cfrac{x+2a}{x+3a-1}+\\cdots+\\cfrac{x+(n-1)a}{x+na-1}$.',
    ),
    rec(
        "RN-P2-C12-Entry08-Corollary",
        '$\\displaystyle e^{-1}=\\cfrac{2}{1}+\\cfrac{3}{2}+\\cfrac{4}{3}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry09",
        'Let $a$ and $x$ be complex numbers such that either $x\\ne -ka$ for $k\\in\\{1,2,\\ldots\\}$ and $a\\ne 0$, or $a=0$ and $|x|>1$. Then $\\displaystyle\\cfrac{x+a+1}{x+1}=\\cfrac{x+a}{x-1}+\\cfrac{x+2a}{x+a-1}+\\cfrac{x+3a}{x+2a-1}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry09-Example01",
        '$\\displaystyle\\cfrac{3}{2}=\\cfrac{3}{2}+\\cfrac{3}{3}+\\cfrac{3}{4}+\\cfrac{3}{5}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry09-Example02",
        '$\\displaystyle\\cfrac{10}{3}=\\cfrac{10}{3}+\\cfrac{10}{5}+\\cfrac{10}{7}+\\cfrac{10}{9}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry10",
        'If $n$ is a positive integer, then $\\displaystyle n=\\cfrac{n}{1-n}+\\cfrac{n+1}{2-n}+\\cfrac{n+2}{3-n}+\\cdots+\\cfrac{2n-1}{0}+\\cfrac{2n}{1}+\\cfrac{2n+1}{2}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry11",
        'Suppose $a$ is a positive integer and $n\\notin\\{0,-1,-2,\\ldots\\}$. Define $N_a={}_1F_1(1-a;n+2-a;-1)$ and $D_a={}_1F_1(1-a;n+1-a;-1)$,where if $a=1$ the denominators in thehypergeometric definitions are understood to be $1$. Then $\\displaystyle\\cfrac{N_a}{D_a}=\\cfrac{n}{n-a}+\\cfrac{n+1}{n-a+1}+\\cfrac{n+2}{n-a+2}+\\cdots$, and $\\displaystyle\\cfrac{N_{a+1}}{N_a}=\\cfrac{n+2-a}{a-2}+\\cfrac{n+3-a}{a-2}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry11-Corollary01",
        'If $n$ is not a nonpositive integer, then $\\displaystyle\\cfrac{n^2+n+1}{n}=\\cfrac{n}{n-3}+\\cfrac{n+1}{n-2}+\\cfrac{n+2}{n-1}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry11-Corollary02",
        'If $n$ is not a nonpositive integer, then $\\displaystyle\\cfrac{n^3+2n+1}{n}=\\cfrac{n}{n-4}+\\cfrac{n+1}{n-3}+\\cfrac{n+2}{n-2}+\\cdots$, wherethe numerators are $(k-1)^3+2(k-1)+1$for the term with denominator $n+k-4$.',
    ),
    rec(
        "RN-P2-C12-Entry12",
        'If $a\\ne 0$ and $x\\ne -ka$ for each positive integer $k$, then $\\displaystyle1=\\cfrac{x+a}{a}+\\cfrac{(x+a)^2-a^2}{a}+\\cfrac{(x+2a)^2-a^2}{a}+\\cfrac{(x+3a)^2-a^2}{a}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry13",
        'Let $a,b,d$ be complex numbers such that either $d\\ne 0$, $b\\ne -kd$ for nonnegative integers $k$, and $\\operatorname{Re}((a-b)/d)>0$, or$d\\ne 0$ and $a=b$, or $d=0$ and $|a|<|b|$. Then $\\displaystyle\\frac{a}{b}=\\cfrac{ab}{a+b+d}-\\cfrac{(a+d)(b+d)}{a+b+3d}-\\cfrac{(a+2d)(b+2d)}{a+b+5d}-\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry14",
        'If $a_1,a_2,\\ldots,a_{2n}$ and $x$ are arbitrary complex numbers, then $\\displaystyle\\cfrac{a_1}{x+1}+\\cfrac{a_2}{x+1}+\\cdots+\\cfrac{a_{2n}}{x+1}=\\cfrac{-a_1}{x+a_2}+\\cfrac{a_2a_3}{x+a_3+a_4}-\\cfrac{a_4a_5}{x+a_5+a_6}+\\cdots+\\cfrac{(-1)^{n-1}a_{2n-2}a_{2n-1}}{x+a_{2n-1}+a_{2n}}$.',
    ),
    rec(
        "RN-P2-C12-Entry15",
        'As a formal identity between corresponding C-fractions, $\\displaystyle\\cfrac{a_1+h}{1+x}+\\cfrac{a_2+h}{1+x}+\\cdots=\\cfrac{a_1}{1}+\\cfrac{a_2}{x+1}+\\cfrac{a_3}{x+1}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry15ii",
        'For the continued fractions in Entry 15: if the left side of (15.1) converges to $F$, then the odd part of the right side converges to $F$, and conversely; in particular, the identity holds in the usual sense if both continued fractions converge.',
    ),
    rec(
        "RN-P2-C12-Entry15iii",
        'For the continued fractions in Entry 15: if the left side converges to $F$, then the right side converges to $F$, except possibly if $h$ is a limit point of $\\{-B_{2k}/B_{2k-1}\\}$, where $A_k/B_k$ denotes the $k$th approximant of the left side, and conversely.',
    ),
    rec(
        "RN-P2-C12-Entry16",
        'If neither $m$ nor $n$ is a negative integer, then $\\displaystyle\\sum_{k=1}^\\infty\\frac{(-1)^{k+1}}{(m+k)(n+k)}=\\cfrac{1}{(m+1)(n+1)}+\\cfrac{(m+1)^2(n+1)^2}{m+n+3}+\\cfrac{(m+2)^2(n+2)^2}{m+n+5}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry17",
        'Write $\\displaystyle\\cfrac{1}{1+\\cfrac{a_1 x}{1}+\\cfrac{a_2 x}{1}+\\cfrac{a_3 x}{1}+\\cdots}=\\sum_{k=0}^\\infty A_k(-x)^k$, where $A_0=1$. Let $P_n=a_1a_2\\cdots a_{n-1}(a_1+a_2+\\cdots+a_n)$ for $n\\ge 1$. Then $P_1=A_1$, $P_2=A_2$, $P_3=A_3-a_1A_2$, $P_4=A_4-(a_1+a_2)A_3$, and in general for $n\\ge 1$, $P_n=\\displaystyle\\sum_{0\\le k<n/2}(-1)^k\\varphi_k(n)A_{n-k}$, where $\\varphi_0(n)\\equiv 1$ and $\\varphi_r(n)$, $r\\ge1$, satisfies $\\varphi_r(n+1)-\\varphi_r(n)=a_{n-1}\\varphi_{r-1}(n-1)$.',
    ),
    rec(
        "RN-P2-C12-Entry17-Corollary01",
        'Write $\\displaystyle\\cfrac{1}{1+\\cfrac{a_1 x}{b_1 x+1}+\\cfrac{a_2 x}{b_2 x+1}+\\cdots}=\\sum_{k=0}^\\infty A_k(-x)^k$, where $A_0=1$. Let $P_n=a_1a_2\\cdots a_{n-1}(a_1+b_1+a_2+b_2+\\cdots+a_n+b_n)$ for $n\\ge 1$. Then for $n\\ge 1$,$P_n=\\displaystyle\\sum_{k=0}^{n-1}(-1)^k\\varphi_k(n)A_{n-k}$, where $\\varphi_0(n)\\equiv 1$ and $\\varphi_r(n)$, $r\\ge 1$, satisfies$\\varphi_r(n+1)-\\varphi_r(n)=b_n\\varphi_r(n)+a_{n-1}\\varphi_{r-1}(n-1)$.',
    ),
    rec(
        "RN-P2-C12-Entry17-Corollary02",
        'Let $B_n(x)$ be the denominator of the $n$th convergent of the continued fraction in Entry 17. Then for $n\\ge 1$, $\\displaystyleB_n(x)=\\sum_{k=0}^{\\lfloor n/2\\rfloor}\\varphi_k(n+1)x^k$.',
    ),
    rec(
        "RN-P2-C12-Entry17-Example",
        '$\\displaystyle{}_2F_1\\!\\left(\\tfrac12,\\tfrac12;1;x\\right)=\\cfrac{3x}{1-2x}+\\cfrac{5x}{8-40x}+\\cfrac{17x}{2-3128x}+\\cfrac{23x}{40-1395x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry18",
        'Suppose $x$ and $n$ are complex numbers such that either $x\\notin[-1,1]$, or $x=\\pm 1$ and $\\operatorname{Re} n\\ne 0$, or $n$ is aninteger. Then $\\displaystyle\\cfrac{(x+1)^n-(x-1)^n}{(x+1)^n+(x-1)^n}=\\cfrac{n}{x}+\\cfrac{n^2-1^2}{3x}+\\cfrac{n^2-2^2}{5x}+\\cfrac{n^2-3^2}{7x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry18-Corollary01",
        'Let $x$ be any complex number outside the cuts $(-\\infty,-i]$ and $[i,\\infty)$. Then $\\displaystyle\\tan^{-1}x=\\cfrac{x}{1}+\\cfrac{x^2}{3}+\\cfrac{(2x)^2}{5}+\\cfrac{(3x)^2}{7}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry18-Corollary02",
        'Let $x$ be any complex number outside the cuts $(-\\infty,-1]$ and $[1,\\infty)$. Then $\\displaystyle\\log\\frac{1+x}{1-x}=\\cfrac{2x}{1}-\\cfrac{x^2}{3}-\\cfrac{(2x)^2}{5}-\\cfrac{(3x)^2}{7}-\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry18-Corollary03",
        'For any complex number $x$, $\\displaystyle\\tan x=\\cfrac{x}{1}-\\cfrac{x^2}{3}-\\cfrac{x^2}{5}-\\cfrac{x^2}{7}-\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry18-Corollary04",
        'For any complex number $x$, $\\displaystyle\\cfrac{e^x-1}{e^x+1}=\\cfrac{x}{2}+\\cfrac{x^2}{6}+\\cfrac{x^2}{10}+\\cfrac{x^2}{14}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry19",
        'If $n$ and $x$ are arbitrary complex numbers, then $\\displaystyle\\cfrac{x\\,{}_0F_1(n+1;x)}{J_n(2i\\sqrt{x})}=\\cfrac{x\\,{}_0F_1(n;x)}{iJ_{n-1}(2i\\sqrt{x})}=n+\\cfrac{x}{n+1}+\\cfrac{x}{n+2}+\\cfrac{x}{n+3}+\\cdots$, where $J_\\nu$ denotes the ordinary Bessel function of order $\\nu$.',
    ),
    rec(
        "RN-P2-C12-Entry20",
        "If $x$ is any complex number outside $(-\\infty,-1]$, or if $\\alpha$, $\\beta$, or $\\gamma-\\alpha$ or $\\gamma-\\beta\\in\\{0,-1,-2,\\ldots\\}$, then $\\displaystyle\\cfrac{\\alpha\\beta x\\,{}_2F_1(\\gamma-\\alpha,\\beta+1;\\gamma+1;-x)}{\\gamma\\,{}_2F_1(\\gamma-\\alpha,\\beta;\\gamma;-x)}=\\cfrac{\\alpha\\beta x}{\\gamma}+\\cfrac{(\\alpha-\\gamma)(\\beta-\\gamma)x}{\\gamma+1}+\\cfrac{(\\alpha+1)(\\beta+1)x}{\\gamma+2}+\\cfrac{(\\alpha-\\gamma-1)(\\beta-\\gamma-1)x}{\\gamma+3}+\\cdots$ (Gauss's continued fraction).",
    ),
    rec(
        "RN-P2-C12-Entry21",
        'Let $x$, $p$, and $\\gamma$ be complex. If either $x\\notin(-\\infty,-1]$, or $p,\\gamma$ or $\\gamma-p\\in\\{0,-1,-2,\\ldots\\}$, then $\\displaystyle\\cfrac{px\\,{}_2F_1(p+1,1;\\gamma+1;-x)}{\\gamma\\,{}_2F_1(p,1;\\gamma;-x)}=\\cfrac{px}{\\gamma}+\\cfrac{\\gamma(p+1)x}{\\gamma+1}+\\cfrac{(\\gamma-p)x}{\\gamma+2}+\\cfrac{(\\gamma+1)(p+2)x}{\\gamma+3}+\\cfrac{2(\\gamma+1-p)x}{\\gamma+4}+\\cdots$. If either $\\operatorname{Re} x>-1/2$ and not both $p+1$ and $\\gamma-p$ lie in $\\{0,-1,-2,\\ldots\\}$, or $p\\in\\{0,-1,-2,\\ldots\\}$ and $\\gamma-p\\notin\\{0,-1,-2,\\ldots\\}$, then also $\\displaystyle\\cfrac{px\\,{}_2F_1(p+1,1;\\gamma+1;-x)}{\\gamma\\,{}_2F_1(p,1;\\gamma;-x)}=\\cfrac{px}{\\gamma}+\\cfrac{(p+1)x}{1}+\\cfrac{(p+2)x}{\\gamma+1}+\\cfrac{2(1+x)}{\\gamma+2}+\\cdots$, and $\\displaystyle\\cfrac{px\\,{}_2F_1(p+1,1;\\gamma+1;-x)}{\\gamma\\,{}_2F_1(p,1;\\gamma;-x)}=\\cfrac{px}{x(p+1)-\\gamma}+\\cfrac{(p+1)x(x+1)}{\\gamma+1}+\\cfrac{(p+3)x(x+1)}{\\gamma+2}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry21-Corollary01",
        'For every complex number $x$, $\\displaystyle\\cfrac{x}{n}=\\cfrac{nx}{n+1}+\\cfrac{x}{n+2}+\\cfrac{2x}{n+3}+\\cfrac{3x}{n+4}+\\cdots$ and $\\displaystyle\\cfrac{x}{n-x}=\\cfrac{x}{n+1-x}+\\cfrac{x}{n+2-x}+\\cfrac{2x}{n+3-x}+\\cfrac{3x}{n+4-x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry21-Corollary02",
        'If $x$ is any complex number, then $\\displaystyle{}_1F_1(1;x+1;x)=1+\\cfrac{2x}{2}+\\cfrac{3x}{3}+\\cfrac{4x}{4}+\\cfrac{5x}{5}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry22",
        'Assume $\\alpha$, $\\beta$, and $\\gamma$ are complex numbers such that not both $\\beta+1$ and $\\gamma-\\beta$ belong to $\\{0,-1,-2,\\ldots\\}$and not both $-\\alpha$ and $\\alpha+\\gamma+1$ are in $\\{0,-1,-2,\\ldots\\}$. Suppose that either $|x|<1$, or $\\beta\\in\\{0,-1,-2,\\ldots\\}$, or$x=1$ and $\\operatorname{Re}(\\gamma-\\alpha-\\beta-1)>0$. Then $\\displaystyle\\cfrac{\\betax\\,{}_2F_1(-\\alpha,\\beta+1;\\gamma+1;-x)}{\\gamma\\,{}_2F_1(-\\alpha,\\beta;\\gamma;-x)}=\\cfrac{\\betax}{\\gamma}+\\cfrac{(\\beta+1)(\\alpha+\\gamma+1)x}{\\gamma+1-(\\alpha+\\beta+1)x}+\\cfrac{(\\beta+2)(\\alpha+\\gamma+2)x}{\\gamma+2-(\\alpha+\\beta+2)x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry23",
        'Write, for each nonnegative integer $n$, $\\displaystyle\\cfrac{a_{n+1}}{b_n x+b_{n+1}x+b_{n+2}x+\\cdots}=c_n\\sum_{k=0}^\\infty A_n(k)(-x)^k$,where $A_n(0)=1$. Then $c_nc_{n+1}=a_n$, $A_n(2)+A_{n+1}(2)=A_n(1)^2$, $A_n(3)+A_{n+1}(3)=A_n(1)\\{A_n(2)-A_{n+1}(2)\\}$,$A_n(4)+A_{n+1}(4)=A_n(1)\\{A_n(3)-A_{n+1}(3)\\}-A_n(2)A_{n+1}(2)$, and for $k\\ge3$,$A_n(k)+A_{n+1}(k)=A_n(1)\\{A_n(k-1)-A_{n+1}(k-1)\\}-\\displaystyle\\sum_{j=2}^{k-2}A_n(j)A_{n+1}(k-j)$.',
    ),
    rec(
        "RN-P2-C12-Entry23-Example",
        'Let $P_x=e^x\\Gamma(x+1)\\displaystyle\\int_0^\\infty e^{-t}\\left(1+\\frac{t}{x}\\right)^x dt$. Then $\\displaystyle\\lim_{x\\to\\infty}\\left\\{\\frac{P_x}{\\sqrt{\\pi/2}}-\\frac{2}{3\\pi}\\right\\}=0$, where$P_x=\\cfrac{x}{1}+\\cfrac{2x}{2}+\\cfrac{3x}{3}+\\cfrac{4x}{4}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry24",
        'Let $n$ and $x$ be any complex numbers and let $r$ be any positive integer. Define $\\displaystyle f(n,r,x)=\\sum_{k=0}^n\\binom{n}{k}\\frac{(-r+k-1)_k x^k}{(n)_k(r)_k x^k}$. Then $\\displaystyle\\cfrac{n}{x}=\\cfrac{n}{n+1}+\\cfrac{x}{n+2}+\\cfrac{x}{n+3}+\\cdots+\\cfrac{x}{n+r}+\\cfrac{f(n+1,r-1,x)}{f(n,r,x)}$.',
    ),
    rec(
        "RN-P2-C12-Entry25",
        'Suppose that either $n$ is an odd integer and $x$ is any complex number, or $n$ is any complex number and $\\operatorname{Re} x>0$. Then $\\displaystyle\\cfrac{\\Gamma(\\tfrac12(x+n+1))\\Gamma(\\tfrac12(x-n+1))}{\\Gamma(\\tfrac12(x+n+3))\\Gamma(\\tfrac12(x-n+3))}=\\cfrac{x}{2x}+\\cfrac{n^2-1^2}{2x}+\\cfrac{n^2-3^2}{2x}+\\cfrac{n^2-5^2}{2x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry25-Corollary01",
        'If $\\operatorname{Re} x>0$, then $\\displaystyle\\cfrac{\\Gamma^2(\\tfrac12(x+1))}{\\Gamma^2(\\tfrac12(x+3))}=\\cfrac{4}{x}+\\cfrac{1^2}{2x}+\\cfrac{3^2}{2x}+\\cfrac{5^2}{2x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry25-Corollary02",
        'If $\\operatorname{Re} x>0$, then $\\displaystyle\\cfrac{\\Gamma(\\tfrac14(x+3))\\Gamma(\\tfrac34(x+1))}{\\Gamma(\\tfrac14(x+7))\\Gamma(\\tfrac34(x+5))}=\\cfrac{1}{x}+\\cfrac{1\\cdot3}{2x}+\\cfrac{5\\cdot 7}{2x}+\\cfrac{9\\cdot 11}{2x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry26",
        'Suppose that $n$ is an odd integer and $x$ is any complex number, or that $n$ is an arbitrary complex number and $\\operatorname{Re} x>0$.Then $\\displaystyle\\cfrac{\\Gamma^2(\\tfrac12(x+n+1))\\Gamma^2(\\tfrac12(x-n+1))}{\\Gamma^2(\\tfrac12(x+n+3))\\Gamma^2(\\tfrac12(x-n+3))}=\\cfrac{1^2-n^2}{x^2-1}+\\cfrac{3^2-n^2}{x^2-1}+\\cfrac{5^2-n^2}{x^2-1}+\\cdots$ and $\\displaystyle\\cfrac{\\Gamma^2(\\tfrac12(x+n+1))\\Gamma^2(\\tfrac12(x-n+1))}{\\Gamma^2(\\tfrac12(x+n+3))\\Gamma^2(\\tfrac12(x-n+3))}=\\cfrac{1^2-n^2}{x^2-n^2+1}+\\cfrac{3^2-n^2}{3(x^2-n^2+5)}+\\cfrac{5^2-n^2}{5(x^2-n^2+13)}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry26-Corollary",
        'If $\\operatorname{Re} x>0$, then $\\displaystyle\\cfrac{\\Gamma^4(\\tfrac14(x+1))}{\\Gamma^4(\\tfrac14(x+3))}=\\cfrac{1^2}{x^2-1}+\\cfrac{1^2}{x^2-1}+\\cfrac{3^2}{x^2-1}+\\cfrac{3^2}{x^2-1}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry27",
        'Suppose that $x,y>0$. Then $\\displaystyle\\cfrac{(1+y)^2+n}{x+y}=\\cfrac{(3+y)^2+n}{2y}+\\cfrac{(5+y)^2+n}{2y}+\\cdots$ and $\\displaystyle\\cfrac{(1+x)^2+n}{y+x}=\\cfrac{(3+x)^2+n}{2x}+\\cfrac{(5+x)^2+n}{2x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry28",
        'Let $\\operatorname{Re} x>0$ and $|\\arg n|\\le\\pi/2-b$ for some positive number $b$. Then $\\displaystyle\\lim_{n\\to\\infty}\\left\\{\\cfrac{n^2+1^2}{x^2-1^2}+\\cfrac{n^2+3^2}{x^2-3^2}+\\cfrac{n^2+5^2}{x^2-5^2}+\\cdots\\right\\}=1$.',
    ),
    rec(
        "RN-P2-C12-Entry29",
        'Let $n$ be an odd integer and $x$ complex, or let $n$ be complex and $\\operatorname{Re} x>0$. Then $\\displaystyle\\sum_{k=1}^\\infty(-1)^{k+1}\\left\\{\\cfrac{1}{x+n+2k-1}+\\cfrac{1}{x-n+2k-1}\\right\\}=\\cfrac{1^2-n^2}{x}+\\cfrac{3^2-n^2}{x}+\\cfrac{5^2-n^2}{x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry29-Corollary",
        'If $\\operatorname{Re} x>0$, then $\\displaystyle\\sum_{k=1}^\\infty\\frac{(-1)^{k+1}}{x+2k-1}=\\cfrac{1^2}{x}+\\cfrac{3^2}{x}+\\cfrac{5^2}{x}+\\cfrac{7^2}{x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry30",
        'Suppose either that $n$ is an integer or that $\\operatorname{Re} x>0$. Then $\\displaystyle\\int_0^\\infty\\left\\{\\frac{1}{x+n+2k+1}-\\frac{1}{x-n+2k+1}\\right\\}dk=\\cfrac{n\\,1^2(1^2-n^2)}{3x}+\\cfrac{n\\,2^2(2^2-n^2)}{5x}+\\cfrac{n\\,3^2(3^2-n^2)}{7x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry30-Corollary",
        'If $\\operatorname{Re} x>0$, then $\\displaystyle\\sum_{k=0}^\\infty\\frac{2}{(x+2k+1)^2}=\\cfrac{1^2}{3x}+\\cfrac{2^2}{5x}+\\cfrac{3^2}{7x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry31",
        'Suppose that $n$ is an even integer or that $\\operatorname{Re} x>0$ and $n$ is any complex number. Then $\\displaystyle\\sum_{k=0}^\\infty(-1)^k\\left\\{\\cfrac{1}{x-n+2k+1}-\\cfrac{1}{x+n+2k+1}\\right\\}=\\cfrac{2^2-n^2}{x^2-1}+\\cfrac{4^2-n^2}{x^2-1}+\\cfrac{6^2-n^2}{x^2-1}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry31-Corollary",
        'If $\\operatorname{Re} x>0$, then $\\displaystyle\\sum_{k=0}^\\infty\\frac{(-1)^k}{(x+2k+1)^2}=\\cfrac{1^2}{x^2-1}+\\cfrac{2^2}{x^2-1}+\\cfrac{3^2}{x^2-1}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry32i",
        'If $\\operatorname{Re} x>0$, then $\\displaystyle 1+2\\sum_{k=1}^\\infty\\frac{(-1)^k}{x+2k}=\\cfrac{1\\cdot 2}{x}+\\cfrac{2\\cdot3}{x}+\\cfrac{3\\cdot 4}{x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry32ii",
        'If $\\operatorname{Re} x>0$, then $\\displaystyle 1+2x^2\\sum_{k=1}^\\infty\\frac{(-1)^k}{(x+k)^2}=\\cfrac{1^2}{x}+\\cfrac{1\\cdot2}{x}+\\cfrac{2^2}{x}+\\cfrac{2\\cdot 3}{x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry32iii",
        'If $\\operatorname{Re} x>-1/2$, then with $\\zeta(3,x+1)=\\displaystyle\\sum_{k=1}^\\infty\\frac{1}{(x+k)^3}$,$\\displaystyle\\cfrac{1^3}{2x(x+1)+1}+\\cfrac{2^3}{6x(x+1)+1}+\\cfrac{3^3}{10x(x+1)+1}+\\cdots$=\\cfrac{2x^2+2x+1}{16}-\\cfrac{3(2x^2+2x+3)}{26}-\\cfrac{5(2x^2+2x+7)}{36}-\\cfrac{7(2x^2+2x+13)}{46}-\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry33",
        'Let $x$, $m$, and $n$ be complex. If either $m$ or $n$ is an integer or if $\\operatorname{Re} x>0$,then $\\displaystyle\\cfrac{\\Gamma(\\tfrac12(x+m+n+1))\\Gamma(\\tfrac12(x-m-n+1))-\\Gamma(\\tfrac12(x+m-n+1))\\Gamma(\\tfrac12(x-m+n+1))}{\\Gamma(\\tfrac12(x+m+n+1))\\Gamma(\\tfrac12(x-m-n+1))+\\Gamma(\\tfrac12(x+m-n+1))\\Gamma(\\tfrac12(x-m+n+1))}=\\cfrac{mn}{x}+\\cfrac{(m^2-1^2)(n^2-1^2)}{3x}+\\cfrac{(m^2-2^2)(n^2-2^2)}{5x}+\\cfrac{(m^2-3^2)(n^2-3^2)}{7x}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry34",
        'Suppose that $n$ is an odd integer or $t$ is an even integer, or assume that $\\operatorname{Re} x>0$ with $t$ and $n$ arbitrary complexnumbers. Define $P=\\dfrac{\\Gamma(\\tfrac12(x+t+n+1))\\Gamma(\\tfrac12(x+t-n+1))\\Gamma(\\tfrac12(x-t+n+3))\\Gamma(\\tfrac12(x-t-n+3))}{\\Gamma(\\tfrac12(x-t+n+1))\\Gamma(\\tfrac12(x-t-n+1))\\Gamma(\\tfrac12(x+t+n+3))\\Gamma(\\tfrac12(x+t-n+3))}$. Then $\\displaystyle\\cfrac{1+P}{1-P}=\\cfrac{x}{1}+\\cfrac{1^2-n^2/t^2}{3^2}+\\cfrac{2^2-n^2/t^2}{5^2}+\\cfrac{3^2-n^2/t^2}{7^2}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry34-Corollary",
        'Suppose that $\\operatorname{Re}(x/y)\\ne 0$. Put $F(a,\\beta)=\\tan^{-1}\\!\\left\\{\\cfrac{a}{x}+\\cfrac{a^2+(2y)^2}{x}+\\cfrac{\\beta^2+(3y)^2}{x}+\\cdots\\right\\}$. Then $F(a,\\beta)+F(\\beta,a)=2F\\!\\left(\\tfrac12(a+\\beta),\\tfrac12(a+\\beta)\\right)$.',
    ),
    rec(
        "RN-P2-C12-Entry35",
        'Let $x,t,m,n$ be complex numbers with $y=x^2-(1-m)^2$ and . Define $z=(n^2-t^2)(1-2m)$.Define$P=\\dfrac{\\Gamma(\\tfrac12(x+t+m+n+1))\\Gamma(\\tfrac12(x+t-m-n+1))\\Gamma(\\tfrac12(x-t+m-n+1))\\Gamma(\\tfrac12(x-t-m+n+1))}{\\Gamma(\\tfrac12(x-t-m-n+1))\\Gamma(\\tfrac12(x-t+m+n+1))\\Gamma(\\tfrac12(x+t-m+n+1))\\Gamma(\\tfrac12(x+t+m-n+1))}$. If either $t,m,$ or $n$ is an integer or if $\\operatorname{Re} x>0$, then $\\displaystyle\\cfrac{1-P}{1+P}=\\cfrac{2tmn}{x^2-t^2-m^2-n^2+1}+\\cfrac{4(t^2-2^2)(m^2-2^2)(n^2-2^2)}{3(x^2-t^2-m^2-n^2+5)}+\\cfrac{4(t^2-3^2)(m^2-3^2)(n^2-3^2)}{5(x^2-t^2-m^2-n^2+13)}+\\cdots$ and $\\displaystyle\\cfrac{1-P}{1+P}=\\cfrac{2tmn}{y+t-2t^2m}+\\cfrac{2(1-m)(1^2-n^2)}{3y+t}+\\cfrac{2(1+m)(1^2-t^2)}{3y+t}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry36",
        'Suppose either that $n$ or $t$ is an even integer or that $\\operatorname{Re} x>0$ and $n,t$ are arbitrary complex numbers. Let $P=\\dfrac{\\Gamma(\\tfrac12(x+t+n+3))\\Gamma(\\tfrac12(x-t-n+3))\\Gamma(\\tfrac12(x+t-n+1))\\Gamma(\\tfrac12(x-t+n+1))}{\\Gamma(\\tfrac12(x+t+n+1))\\Gamma(\\tfrac12(x-t-n+1))\\Gamma(\\tfrac12(x+t-n+3))\\Gamma(\\tfrac12(x-t+n+3))}$. Then $\\displaystyle\\cfrac{1-P}{1+P}=\\cfrac{tn}{x^2-1-t^2}+\\cfrac{2^2-n^2}{x^2-1}+\\cfrac{2^2-t^2}{x^2-1}+\\cfrac{4^2-n^2}{x^2-1}+\\cfrac{4^2-t^2}{x^2-1}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry37",
        'Suppose that either $t$ or $n$ is an integer or that $\\operatorname{Re} x>0$. Then $\\displaystyle\\sum_{k=0}^\\infty\\left\\{\\cfrac{1}{x+t-n+1}+\\cfrac{1}{x-t-n+1}-\\cfrac{1}{x+t+n+1}-\\cfrac{1}{x-t+n+1}\\right\\}=\\cfrac{2tn}{x^2-1+n^2-t^2}+\\cfrac{2(1^2-n^2)}{3(x^2-1)}+\\cfrac{2(1^2-t^2)}{3(x^2-1)}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry38",
        'Assume that either $n$ is an integer or that $\\operatorname{Re} x>0$. Then $\\displaystyle\\sum_{k=0}^\\infty\\left\\{\\cfrac{1}{(x-n+2k+1)^2}-\\cfrac{1}{(x+n+2k+1)^2}\\right\\}=\\cfrac{n\\,2(1^2-n^2)}{3(x^2-1)+n^2}+\\cfrac{n\\,4(2^2-n^2)}{5(x^2-1)+n^2}+\\cdots$ and $\\displaystyle\\sum_{k=0}^\\infty\\left\\{\\cfrac{1}{(x-n+2k+1)^2}-\\cfrac{1}{(x+n+2k+1)^2}\\right\\}=\\cfrac{n\\,4(1^2-n^2)}{x^2-n^2+1}-\\cfrac{n\\,4(2^2-n^2)}{3(x^2-n^2+5)}-\\cfrac{n\\,4(3^2-n^2)}{5(x^2-n^2+13)}-\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry39",
        'Let $t$ and $n$ be arbitrary complex numbers. Suppose that $x$ is complex with $\\operatorname{Re} x>0$ or that either $n$ or $t$ is an odd integer. Define$P=\\dfrac{\\Gamma(\\tfrac12(x+t+n+1))\\Gamma(\\tfrac12(x-t+n+1))\\Gamma(\\tfrac12(x+t-n+1))\\Gamma(\\tfrac12(x-t-n+1))}{\\Gamma(\\tfrac12(x+t+n+3))\\Gamma(\\tfrac12(x-t+n+3))\\Gamma(\\tfrac12(x+t-n+3))\\Gamma(\\tfrac12(x-t-n+3))}$. Then $\\displaystyleP=\\cfrac{(x^2-t^2+n^2-1)/2}{x^2-1}+\\cfrac{1^2-n^2}{x^2-1}+\\cfrac{1^2-t^2}{x^2-1}+\\cfrac{3^2-n^2}{x^2-1}+\\cfrac{3^2-t^2}{x^2-1}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry40",
        "Let $P$ be the product of eight gamma functions $\\Gamma(\\tfrac12(\\alpha\\pm\\beta\\pm\\gamma\\pm(\\gamma\\pm\\delta+1)))$ with an even number of minus signs in each argument, and let $Q$ be the corresponding product with an odd number of minus signs. Suppose that at least one of $\\beta,\\gamma,\\delta,\\varepsilon$ is a nonzero integer. Then $\\displaystyle\\cfrac{P-Q}{P+Q}=\\cfrac{8\\alpha\\beta\\gamma\\varepsilon}{1}+\\cfrac{2\\{\\alpha^4+\\beta^4+\\gamma^4+\\delta^4+\\varepsilon^4+1\\}-(\\alpha^2+\\beta^2+\\gamma^2+\\delta^2+\\varepsilon^2-1)^2-2^2}{64(\\alpha^2-1^2)(\\beta^2-1^2)(\\gamma^2-1^2)(\\delta^2-1^2)(\\varepsilon^2-1^2)}+\\cfrac{3\\{\\alpha^4+\\beta^4+\\gamma^4+\\delta^4+\\varepsilon^4+1\\}-(\\alpha^2+\\beta^2+\\gamma^2+\\delta^2+\\varepsilon^2-5)^2-6^2}{64(\\alpha^2-2^2)(\\beta^2-2^2)(\\gamma^2-2^2)(\\delta^2-2^2)(\\varepsilon^2-2^2)}+\\cfrac{5\\{\\alpha^4+\\beta^4+\\gamma^4+\\delta^4+\\varepsilon^4+1\\}-(\\alpha^2+\\beta^2+\\gamma^2+\\delta^2+\\varepsilon^2-9)^2-14^2}{64(\\alpha^2-3^2)(\\beta^2-3^2)(\\gamma^2-3^2)(\\delta^2-3^2)(\\varepsilon^2-3^2)}+\\cdots$ (Watson's continued fraction; denominators follow the quadratic patterns $2n^2+2n+1$ and $2n^2+2n+2$).",
    ),
    rec(
        "RN-P2-C12-Entry41",
        'Let $x$ and $y$ be complex numbers such that either $|x+1|>1$ or $y$ is a nonnegative integer. Then $\\displaystyle{}_2F_1(-p,1;y+1;-x)=\\cfrac{\\Gamma(p+1)\\Gamma(y+1)(1+x)^{p+y}}{\\Gamma(p+y+1)x^y}\\left\\{\\cfrac{y}{p+y+1}+\\cfrac{(p+1)x}{1-y}+\\cfrac{(1-y)(x+1)}{p+2}+\\cfrac{(p+3)x}{3-y}+\\cfrac{(2-y)(x+1)}{p+4}+\\cdots\\right\\}$.',
    ),
    rec(
        "RN-P2-C12-Entry42",
        'If $n$ is a nonnegative integer, or if $x\\notin(-\\infty,0]$, then $\\displaystyle\\cfrac{{}_1F_1(1;n+1;x)}{e^x\\Gamma(n+1)}=\\cfrac{n}{x}+\\cfrac{1-n}{1}+\\cfrac{2-n}{x+1}+\\cfrac{3-n}{x+2}+\\cdots$ and $\\displaystyle\\cfrac{{}_1F_1(1;n+1;x)}{e^x\\Gamma(n+1)}=\\cfrac{n}{x+1-n}+\\cfrac{(1-n)x}{x+3-n}+\\cfrac{(2-n)x}{x+5-n}+\\cfrac{(3-n)x}{x+7-n}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry42-Corollary",
        'If either $x$ is exterior to $(-\\infty,0]$ or if $n$ is a positive integer,then $\\displaystyle\\sum_{k=0}^\\infty\\frac{(-x)^k}{k!(n+k)}=\\cfrac{x^n}{e^{-x}\\Gamma(n)}=\\cfrac{x^n}{x+1-n}+\\cfrac{2-n}{x+1}+\\cfrac{3-n}{x+2}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry43",
        'If $x$ is any complex number outside $(-\\infty,0]$, then $\\displaystyle\\sum_{k=0}^\\infty\\frac{x^k}{1\\cdot3\\cdots(2k+1)}=\\sqrt{\\frac{\\pi}{4x}}e^{-x/2}+\\cfrac{1/2}{x+1}+\\cfrac{1}{x+1}+\\cfrac{3/2}{x+1}+\\cdots$ and $\\displaystyle\\log\\frac{1\\cdot 2}{3\\cdot 4}\\frac{5\\cdot6}{7\\cdot8}\\cdots=\\sqrt{\\frac{\\pi}{4x}}e^{x/2}-\\cfrac{x}{1}+\\cfrac{1}{x+5}+\\cfrac{1}{x+9}+\\cfrac{1}{x+13}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry43-Corollary01",
        'For $\\operatorname{Re} x>0$, with $F(x)=\\displaystyle\\frac{2}{\\sqrt{\\pi}}\\int_0^x e^{-t^2}\\,dt$,$\\displaystyle\\int_0^xe^{-t^2}\\,dt=\\cfrac{e^{-x^2}}{\\sqrt{\\pi}}\\left\\{\\cfrac{1}{2x}+\\cfrac{1}{x+2x}+\\cfrac{2}{x+2x}+\\cfrac{3}{x+2x}+\\cdots\\right\\}$.',
    ),
    rec(
        "RN-P2-C12-Entry43-Corollary02",
        "Let $x$ be real and let $F$ be as in Corollary 1. Then as $x\\to\\infty$, $\\displaystyle\\int_0^x\\frac{F(t)}{t}\\,dt=\\gamma+\\log(2x)+O(1)$,where $\\gamma$ denotes Euler's constant.",
    ),
    rec(
        "RN-P2-C12-Entry44",
        "For $x>0$, define $\\displaystyle\\varphi(x)=\\int_0^\\infty\\frac{e^{-t}}{x+t}\\,dt$. Then $\\displaystyle\\int_0^x\\frac{1-e^{-t}}{t}\\,dt=\\sum_{k=1}^\\infty\\frac{(-1)^{k-1}x^k}{k!\\,k}=\\gamma+\\log x+e^{-x}\\varphi(x)$, where $\\gamma$denotes Euler's constant.",
    ),
    rec(
        "RN-P2-C12-Entry44i",
        'Let $x$ be real. Then as $x\\to\\infty$, $\\displaystyle\\varphi(x)\\sim\\sum_{k=0}^\\infty\\frac{(-1)^k k!}{x^{k+1}}$.',
    ),
    rec(
        "RN-P2-C12-Entry44ii",
        'For $x>0$, $\\varphi(x)$ lies between $1/x$ and $1/(x+1)$, and is very nearly equal to $\\varphi(x+1)/x$.',
    ),
    rec(
        "RN-P2-C12-Entry44iii",
        'For $x>0$, $\\displaystyle\\varphi(x)=\\cfrac{1}{x+1}+\\cfrac{1}{1}+\\cfrac{2}{x+3}+\\cfrac{2}{1}+\\cfrac{3}{x+5}+\\cfrac{3}{1}+\\cfrac{4}{x+7}+\\cdots$ and $\\displaystyle\\varphi(x)=\\cfrac{2}{x+1}-\\cfrac{3}{x+2}+\\cfrac{4}{x+3}-\\cfrac{5}{x+4}+\\cdots$ (Tschebyscheff).',
    ),
    rec(
        "RN-P2-C12-Entry44iv",
        'Let $x$ be any complex number exterior to $(-\\infty,0]$, and let $n$ be a natural number. Then $\\displaystyle\\varphi(x)=\\sum_{k=0}^{n-1}\\frac{(-1)^k k!}{x^{k+1}}+\\frac{(-1)^nn!}{x^n}\\left\\{\\cfrac{1}{x+n+1}+\\cfrac{2(n+2)}{x+n+3}+\\cfrac{3(n+3)}{x+n+5}+\\cdots\\right\\}$.',
    ),
    rec(
        "RN-P2-C12-Entry44-Corollary01",
        'For $x>0$, the difference $\\displaystyle\\sum_{k=1}^\\infty\\frac{(-1)^{k-1}x^k}{k!\\,k}-\\gamma-\\log x$ lies between $e^{-x}/x$ and $e^{-x}/(x+1)$ (equivalently, $\\varphi(x)$ lies between $1/x$ and $1/(x+1)$).',
    ),
    rec(
        "RN-P2-C12-Entry44-Corollary02",
        'For $|h|<1$ and $n>0$, define $f(h,n)$ by $\\displaystyle\\int_0^{n(1-h)}\\frac{1-e^{-t}}{t}\\,dt=\\gamma+\\log n+e^{-n}\\varphi(n)-e^{-n}f(h,n)$.Then $\\displaystyle f(h,n)=\\sum_{k=0}^\\infty\\frac{e^n\\left\\{H_n-\\sum_{j=0}^k n^j/j!\\right\\}}{k!}\\,h^{k+1}$.',
    ),
    rec(
        "RN-P2-C12-Entry45i",
        'For the continued fraction $\\displaystyle\\cfrac{1}{1}+\\cfrac{x}{1}+\\cfrac{x}{1}+\\cfrac{2x}{1}+\\cfrac{2x}{1}+\\cfrac{3x}{1}+\\cdots$, the denominator $B_{2n}$ of the $2n$th convergent equals $\\displaystyle B_{2n}(x)=\\sum_{k=0}^n\\frac{(-n)_k x^k}{k!}$.',
    ),
    rec(
        "RN-P2-C12-Entry45ii",
        'For the continued fraction in Entry 45i, the denominator $B_{2n-1}$ of the $(2n-1)$st convergent equals $\\displaystyleB_{2n-1}(x)=\\sum_{k=0}^{n-1}\\frac{(-n)_k(1-k/n)x^k}{(k-1)!}$.',
    ),
    rec(
        "RN-P2-C12-Entry46i",
        "For $|x|<1$, set $\\displaystyle\\Gamma(x+1)=\\sum_{k=0}^\\infty\\frac{A_k x^k}{k!}$ (46.1). Define $\\varphi_n(x)$ as the constant term in theLaurent expansion of$x^p\\Gamma(1-p)/p^n$, $0<|p|<1$, where $n$ is a nonnegative integer. Then if $x\\ne 0$,$\\displaystyle\\varphi_n(x)=\\frac{1}{n!}\\sum_{k=0}^n\\binom{n}{k}A_{n-k}\\log^k x$. Define$\\psi_n(x)$, $n\\ge 0$, by$\\displaystyle\\sum_{k=1}^\\infty\\frac{(-1)^{k-1}x^k}{k^n k!}=\\varphi_n(x)+(-1)^{n-1}e^{-x}\\psi_n(x)$. Then for $n\\ge1$,$\\displaystyle\\psi_n'(x)-\\frac{\\psi_n(x)}{x}=\\psi_{n-1}(x)$.",
    ),
    rec(
        "RN-P2-C12-Entry46ii",
        'For $n\\ge 1$, $\\displaystyle nA_n=\\sum_{k=1}^n(-1)^k S_k A_{n-k}$, where $A_k$ is defined by (46.1), $S_1=\\gamma$, and $S_k=\\zeta(k)$ for$k\\ge 2$.',
    ),
    rec(
        "RN-P2-C12-Entry46iii",
        'In the notation (46.6), if $\\displaystyle\\Gamma(x+1)=\\sum_{k=0}^\\infty b_k x^k$ and $\\displaystyle\\Gamma(x+1)\\approx\\sum_{k=0}^\\infty\\theta_k x^k/k!$, then $b_1=-\\gamma$,$b_2=0.9890559953$, $b_3=-0.9074790762$,$b_4=0.9817280865$, and Ramanujan gives $\\theta_0=1.00027$, $\\theta_1=51/52$, $\\theta_2=77/82$, $\\theta_6=5/68$, $\\theta_7=-1/38$.',
    ),
    rec(
        "RN-P2-C12-Entry46iv",
        'If $n$ is a nonnegative integer, then $\\displaystyle\\psi_n(x)=\\left(\\cfrac{n}{x}+\\cfrac{5n+10}{2}+\\cfrac{41n+58}{6x}+\\cdots\\right)^{n+1}$(as the C-fraction corresponding to thepower series for $\\psi_n$).',
    ),
    rec(
        "RN-P2-C12-Entry46-Example",
        'For $x>0$, let $\\displaystyle F(x)=\\int_0^x\\frac{1-e^{-t}}{t}\\,dt$. Then $\\displaystyle\\lim_{x\\to\\infty}\\left\\{\\int_0^x\\frac{F(t)}{t}\\,dt-\\tfrac12F_2(x)\\right\\}=\\frac{\\pi^2}{12}$, where$F_2(x)=\\tfrac12\\gamma^2+\\gamma\\log x+O(1)$ as $x\\to\\infty$.',
    ),
    rec(
        "RN-P2-C12-Entry47",
        'If $n$ is any complex number outside $(-\\infty,0]$, then $\\displaystyle\\int_0^\\inftye^{-x}\\left(1+\\frac{x}{n}\\right)^tdx$=1+\\cfrac{1}{1}+\\cfrac{n-1}{3}+\\cfrac{n-2}{5}+\\cfrac{n-3}{7}+\\cdots$=2+\\cfrac{n-1}{2}+\\cfrac{n-2}{4}+\\cfrac{n-3}{6}+\\cfrac{n-4}{8}+\\cdots$=\\cfrac{e^n\\Gamma(n+1)}{n^n}\\left\\{\\cfrac{2n}{2}+\\cfrac{3n}{3}+\\cfrac{4n}{4}+\\cfrac{5n}{5}+\\cdots\\right\\}$.',
    ),
    rec(
        "RN-P2-C12-Entry48",
        'As $n\\to\\infty$, $\\displaystyle\\frac{e^n\\Gamma(n+1)}{\\sqrt{2\\pi n}}\\int_0^\\inftye^{-x}\\left(1+\\frac{x}{n}\\right)^ndx$=\\frac{2}{3}+\\frac{4}{135n}-\\frac{8}{2835n^2}+\\frac{16}{8505n^3}-\\frac{384}{385245n^4}+\\cdots$.',
    ),
    rec(
        "RN-P2-C12-Entry48-Corollary",
        'Define $\\theta=\\theta_n$ by $\\displaystyle\\theta=\\frac{e^n\\Gamma(n+1)}{\\sqrt{2\\pi n}}\\int_0^\\infty e^{-x}\\left(1+\\frac{x}{n}\\right)^ndx-1$. Then $\\displaystyle\\theta\\sim\\theta^*:=\\frac{4+15n}{8+45n}$ as $n\\to\\infty$.',
    ),
    rec(
        "RN-P2-C12-Entry49",
        "For each integer $n\\ge 2$, define $\\theta=\\theta_n$ by $\\displaystyle\\gamma+\\logn+\\sum_{k=1}^\\infty\\frac{n^k}{k!\\,k}=e^\\theta\\sum_{k=0}^{n-2}\\frac{k!}{(n-1)!\\,k+1}$, where$\\gamma$ denotes Euler's constant. Then as$n\\to\\infty$, $\\displaystyle\\theta=\\frac{2}{3}+\\frac{4}{135n}+\\frac{76}{2835n^2}+\\cdots$.",
    ),
]
