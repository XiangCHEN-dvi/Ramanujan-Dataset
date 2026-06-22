"""RLN Part 3, Chapter 10 — mined manuscript fragments (highly composite numbers).

No Entry labels in Berndt; results extracted from Ramanujan's unpublished manuscript
on highly composite numbers (Sections 10.52–10.75; book eqs. 10.52.268–10.71.383).
"""

from __future__ import annotations

TOPICS_C10 = ["highly-composite-numbers"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C10}


CHAPTER_10 = [
    rec(
        "RLN-P3-C10-Definition01",
        r"A positive integer $N$ is highly composite if $d(M)<d(N)$ for every integer $M<N$, "
        r"where $d(n)$ denotes the number of divisors of $n$.",
    ),
    rec(
        "RLN-P3-C10-Definition02",
        r"A positive integer $N$ is largely composite if $d(M)\le d(N)$ for every integer $M\le N$.",
    ),
    rec(
        "RLN-P3-C10-Definition03",
        r"Let $Q_2(N)$ denote the number of representations of $N$ as $m^2+n^2$, "
        r"counting $m^2+n^2$ in two ways when $m\ne n$ and in one way when $m=n$ or one of $m,n$ is zero.",
    ),
    rec(
        "RLN-P3-C10-Formula1052268",
        r"With $\vartheta_3(q)=1+2q+2q^4+2q^9+\cdots$, Ramanujan has "
        r"$\vartheta_3(q)^2=1+4\sum_{n=1}^{\infty}Q_2(n)q^n$, where "
        r"$\vartheta_3(q)^2=1+4\!\left(\dfrac{q}{1-q}-\dfrac{q^3}{1-q^3}+\dfrac{q^5}{1-q^5}-\dfrac{q^7}{1-q^7}+\cdots\right)$.",
    ),
    rec(
        "RLN-P3-C10-Formula1052269",
        r"Ramanujan gives "
        r"$\zeta(s)\,\zeta_1(s)=\sum_{n=1}^{\infty}\dfrac{Q_2(n)}{n^s}$, "
        r"where $\zeta_1(s)=1^{-s}-3^{-s}+5^{-s}-7^{-s}+\cdots$.",
    ),
    rec(
        "RLN-P3-C10-Formula1052270",
        r"For all positive integers $N$, $Q_2(N)\le d(N)$.",
    ),
    rec(
        "RLN-P3-C10-Formula1052271",
        r"If $N=2^{a_2}3^{a_3}5^{a_5}\cdots p^{a_p}$ with $a_\lambda\ge 0$ and some "
        r"$a_3,a_7,a_{11},\ldots$ (primes $4n-1$) is odd, then $Q_2(N)=0$.",
    ),
    rec(
        "RLN-P3-C10-Formula1052272",
        r"If every $a_3,a_7,a_{11},\ldots$ (primes $4n-1$) is even or zero, then "
        r"$Q_2(N)=(1+a_5)(1+a_{13})(1+a_{17})\cdots$, "
        r"where $5,13,17,\ldots$ are the primes of the form $4n+1$.",
    ),
    rec(
        "RLN-P3-C10-Formula1053274",
        r"Without assuming the prime number theorem, the maximum order of $Q_2(N)$ is "
        r"$2^{\log N}\!\left\{\dfrac{1}{\log\log N}+O\!\left(\dfrac{1}{(\log\log N)^2}\right)\right\}$.",
    ),
    rec(
        "RLN-P3-C10-Formula1053275",
        r"Assuming the prime number theorem, the maximum order of $Q_2(N)$ is "
        r"$2^{\tfrac{1}{2}\mathrm{Li}(2\log N)+O(\log N\,e^{-a\sqrt{\log N})}}$ for some positive constant $a$.",
    ),
    rec(
        "RLN-P3-C10-Formula1058301",
        r"For $N=2^{a_2}3^{a_3}\cdots p_n^{a_n}$ and $s>0$, Ramanujan gives "
        r"$\sigma_{-s}(N)<\left\{1-(p_1p_2\cdots p_n N)^{-s/n}\right\}^n"
        r"\prod_{i=1}^{n}\dfrac{1}{1-p_i^{-s}}$.",
    ),
    rec(
        "RLN-P3-C10-Formula1058302",
        r"The indices $a_1,a_2,\ldots,a_n$ can be chosen so that "
        r"$\sigma_{-s}(N)=\left\{1-(p_1p_2\cdots p_n N)^{-s/n}\right\}^n"
        r"\prod_{i=1}^{n}\dfrac{1}{1-p_i^{-s}}\left\{1-O\!\left(N^{-s/n}(\log N)^{-2/(n-1)}\right)\right\}$.",
    ),
    rec(
        "RLN-P3-C10-Definition04",
        r"A positive integer $N$ is a generalized highly composite number if "
        r"$\sigma_{-s}(N)>\sigma_{-s}(N')$ for all $N'<N$; then $N=2^{a_2}3^{a_3}5^{a_5}\cdots p^{a_p}$ "
        r"with $a_2\ge a_3\ge a_5\ge\cdots\ge a_p=1$, except that $N=36$ when $2^s+4^s+8^s>3^s+9^s$ "
        r"and $N=4$ in all cases.",
    ),
    rec(
        "RLN-P3-C10-Definition05",
        r"A positive integer $N$ is a generalized superior highly composite number if there exists "
        r"$\varepsilon>0$ such that $\sigma_{-s}(N)/N^\varepsilon\ge\sigma_{-s}(N')/(N')^\varepsilon$ for all $N'<N$ "
        r"and $\sigma_{-s}(N)/N^\varepsilon>\sigma_{-s}(N')/(N')^\varepsilon$ for all $N'>N$.",
    ),
    rec(
        "RLN-P3-C10-Formula1071382",
        r"Ramanujan gives "
        r"$\Sigma_{-1}(N)=e^\gamma\!\left\{\log\log N-2(\sqrt{2}-1)\sqrt{\log N}+S_1(\log N)+O\!\left(\dfrac{1}{\sqrt{\log N}\,\log\log N}\right)\right\}$, "
        r"where $\Sigma_{-1}(N)=\sigma_{-1}(N)/N$ and $S_1$ is a bounded function.",
    ),
    rec(
        "RLN-P3-C10-Table01",
        r"Ramanujan's table of largely composite numbers lists $(N,d(N))$ in increasing order; "
        r"the opening entries are $(1,1)$, $(2,2)$, $(3,2)$, $(4,3)$, $(6,4)$, $(8,4)$, $(10,4)$, "
        r"$(12,6)$, $(18,6)$, $(20,6)$, $(24,8)$, $(30,8)$, $(36,9)$, $(48,10)$, $(60,12)$, $(72,12)$, "
        r"$(84,12)$, $(90,12)$, $(96,12)$, $(108,12)$, $(120,16)$, $(168,16)$, $(180,18)$, $(240,20)$, "
        r"$(360,24)$, $(420,24)$, $(480,24)$, $(504,24)$, $(630,24)$, $(720,30)$, $(840,32)$, "
        r"$(1260,36)$, $(1680,40)$, $(2520,48)$, $(5040,60)$, $(7560,64)$, $(9240,64)$, $(10080,72)$, "
        r"$(12600,72)$, $(15120,80)$, $(20160,84)$, $(25200,90)$, $(27720,96)$, $(30240,96)$, "
        r"$(32760,96)$, $(36960,96)$, $(37800,96)$, $(40320,96)$, $(45360,100)$, $(50400,108)$, "
        r"$(55440,120)$, $(83160,128)$, $(110880,144)$, and continues to $N=2091887232$ with $d(N)=960$; "
        r"entries marked with an asterisk are superior highly composite numbers.",
    ),
]
