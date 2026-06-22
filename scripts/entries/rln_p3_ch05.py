"""RLN Part 3, Chapter 5 — mined manuscript fragments (partition/tau manuscript).

No Entry labels in Berndt; results extracted from Ramanujan's unpublished manuscript
on partition and tau functions (book eqs. 5.1.1–5.22.8 and related sections).
"""

from __future__ import annotations

TOPICS_C05 = ["partition-tau-functions-manuscript"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C05}


CHAPTER_5 = [
    rec(
        "RLN-P3-C05-Formula050104",
        r"With $P=1-24\sum_{n=1}^{\infty}\dfrac{nq^n}{1-q^n}$, "
        r"$Q=1+240\sum_{n=1}^{\infty}\dfrac{n^3q^n}{1-q^n}$, "
        r"$R=1-504\sum_{n=1}^{\infty}\dfrac{n^5q^n}{1-q^n}$, and "
        r"$\Delta(\tau)=q(q;q)_\infty^{24}$, Ramanujan has $Q^3-R^2=1728q\,\Delta(\tau)$.",
    ),
    rec(
        "RLN-P3-C05-Formula050111",
        r"The partition function satisfies $p(5n-1)\equiv 0\pmod{5}$ for all $n\ge 1$.",
    ),
    rec(
        "RLN-P3-C05-Formula050112",
        r"For the partition function, "
        r"$p(n-1)-p(n-26)-p(n-51)+p(n-126)+p(n-176)-p(n-301)-\cdots-n\sigma_1(n)\equiv 0\pmod{5}$, "
        r"where $1,26,51,126,\ldots$ are numbers of the form "
        r"$\tfrac{1}{2}(5\nu+1)(15\nu+2)$ and $\tfrac{1}{2}(5\nu-1)(15\nu-2)$.",
    ),
    rec(
        "RLN-P3-C05-Congruence0501",
        r"If $\tau(n)$ is the coefficient of $q^n$ in $(q;q)_\infty^{24}$, then "
        r"$\tau(n)-n\sigma_1(n)\equiv 0\pmod{5}$ and $\lambda(n)-n\sigma_1(n)\equiv 0\pmod{5}$, "
        r"where $\sum_{n=1}^{\infty}\lambda(n)q^n=q\,(q^{25};q^{25})_\infty/(q;q)_\infty$.",
    ),
    rec(
        "RLN-P3-C05-Formula050307",
        r"The partition function satisfies $p(25n-1)\equiv 0\pmod{25}$ for all $n\ge 1$.",
    ),
    rec(
        "RLN-P3-C05-Formula050403",
        r"Ramanujan conjectures: if $k$ is any positive integer and $n$ is not a multiple of $5$, "
        r"then there exist integers $a$ and $b$ such that "
        r"$\tau(n)-n^a\sigma_b(n)\equiv 0\pmod{5^k}$; for example "
        r"$\tau(n)-n^{41}\sigma_{29}(n)\equiv 0\pmod{125}$ when $5\nmid n$.",
    ),
    rec(
        "RLN-P3-C05-Formula050404",
        r"If $n$ is a multiple of $5$, then "
        r"$\tau(n)-4830\,\tau\!\left(\dfrac{n}{5}\right)+511\,\tau\!\left(\dfrac{n}{25}\right)=0$, "
        r"with $\tau(x)=0$ when $x$ is not an integer.",
    ),
    rec(
        "RLN-P3-C05-Formula050405",
        r"Ramanujan gives "
        r"$\dfrac{q\,(q^5;q^5)_\infty^5}{(q;q)_\infty}=\sum_{n=1}^{\infty}\left(\dfrac{n}{5}\right)\dfrac{q^n}{(1-q^n)^2}$ "
        r"and "
        r"$\dfrac{(q;q)_\infty^5}{(q^5;q^5)_\infty}=1-5\sum_{n=1}^{\infty}\left(\dfrac{n}{5}\right)\dfrac{nq^n}{1-q^n}$.",
    ),
    rec(
        "RLN-P3-C05-Formula050407",
        r"For the ordinary partition function, "
        r"$\sum_{n=0}^{\infty}p(5n+4)q^n=5\dfrac{(q^5;q^5)_\infty^5}{(q;q)_\infty^6}$.",
    ),
    rec(
        "RLN-P3-C05-Formula050508",
        r"The partition function satisfies $p(7n-2)\equiv 0\pmod{7}$ for all $n\ge 1$.",
    ),
    rec(
        "RLN-P3-C05-Formula050509",
        r"For the partition function, "
        r"$p(n-2)-p(n-51)-p(n-100)+p(n-247)+p(n-345)-\cdots+n\sigma_3(n)-n^2\sigma_1(n)\equiv 0\pmod{7}$, "
        r"where $2,51,100,247,\ldots$ are numbers of the form "
        r"$\tfrac{1}{2}(7\nu+1)(21\nu+4)$ and $\tfrac{1}{2}(7\nu-1)(21\nu-4)$.",
    ),
    rec(
        "RLN-P3-C05-Congruence0502",
        r"If $\tau(n)$ is the coefficient of $q^n$ in $(q;q)_\infty^{24}$, then "
        r"$\tau(n)-n\sigma_3(n)\equiv 0\pmod{7}$.",
    ),
    rec(
        "RLN-P3-C05-Formula050706",
        r"Ramanujan states "
        r"$\sum_{n=1}^{\infty}\dfrac{\tau(n)}{n^s}=\prod_{p}\dfrac{1}{1-\tau(p)p^{-s}+p^{11-2s}}$ "
        r"for all primes $p$.",
    ),
    rec(
        "RLN-P3-C05-Formula050507",
        r"For the ordinary partition function, "
        r"$\sum_{n=0}^{\infty}p(7n+5)q^{n+1}=7\sum_{n=1}^{\infty}n\sigma_3(n)q^n+49J$, "
        r"whence $p(7n+5)\equiv 0\pmod{7}$.",
    ),
    rec(
        "RLN-P3-C05-Formula050708",
        r"The partition function satisfies "
        r"$p(49n-2),\,p(49n-9),\,p(49n-16),\,p(49n-30)\equiv 0\pmod{49}$.",
    ),
    rec(
        "RLN-P3-C05-Formula050906",
        r"The partition function satisfies $p(11n-5)\equiv 0\pmod{11}$ for all $n\ge 1$.",
    ),
    rec(
        "RLN-P3-C05-Formula050907",
        r"For the partition function, "
        r"$p(n-5)-p(n-126)-p(n-247)+p(n-610)+p(n-852)-\cdots+n^4\sigma_1(n)-3n^3\sigma_3(n)"
        r"-3n^2\sigma_5(n)+5n\sigma_7(n)\equiv 0\pmod{11}$, "
        r"where $5,126,247,610,\ldots$ are numbers of the form "
        r"$\tfrac{1}{2}(11\nu+2)(33\nu+5)$ and $\tfrac{1}{2}(11\nu-2)(33\nu-5)$.",
    ),
    rec(
        "RLN-P3-C05-Congruence0510",
        r"If $\lambda(n)$ is the coefficient of $q^n$ in $q\,(q^{121};q^{121})_\infty/(q;q)_\infty$, then "
        r"$\tau(n)-\lambda(n)\equiv 0\pmod{11}$.",
    ),
    rec(
        "RLN-P3-C05-Congruence051007",
        r"If $n$ is odd, then $\tau(2^{4\lambda-1}n)\equiv 0\pmod{11}$; "
        r"if $3\nmid n$, then $\tau(3^{11\lambda-1}n)\equiv 0\pmod{11}$; "
        r"if $5\nmid n$, then $\tau(5^{5\lambda-1}n)\equiv 0\pmod{11}$; "
        r"if $7\nmid n$, then $\tau(7^{10\lambda-1}n)\equiv 0\pmod{11}$.",
    ),
    rec(
        "RLN-P3-C05-Congruence051011",
        r"For all integers $n$ and $\lambda$, $\tau(11^\lambda n)-\tau(n)\equiv 0\pmod{11}$.",
    ),
    rec(
        "RLN-P3-C05-Formula051207",
        r"If $\sigma_{11}(n)=\sum_{d\mid n}d^{11}$, then $\tau(n)-\sigma_{11}(n)\equiv 0\pmod{691}$.",
    ),
    rec(
        "RLN-P3-C05-Formula051212",
        r"For every integer $n$, "
        r"$\tau(2n)+24\,\tau(n)+2^{11}\,\tau\!\left(\dfrac{n}{2}\right)=0$, "
        r"with $\tau(x)=0$ when $x$ is not an integer.",
    ),
    rec(
        "RLN-P3-C05-Formula051510",
        r"For each prime $\varpi>3$, Ramanujan deduces congruences of the form "
        r"$\sum_{n=1}^{\infty}p\!\left(n\varpi+\varpi\left\lfloor\dfrac{\varpi}{24}\right\rfloor"
        r"-\dfrac{\varpi^2-1}{24}\right)q^{n+\lfloor\varpi/24\rfloor}(q^\varpi;q^\varpi)_\infty"
        r"=(Q^3-R^2)^{1+\lfloor\varpi/24\rfloor}\sum K_{\ell,m}Q^\ell R^m+\varpi J$, "
        r"where the sum is over nonnegative $\ell,m$ with $4\ell+6m=\varpi-13-12\lfloor\varpi/24\rfloor$.",
    ),
    rec(
        "RLN-P3-C05-Formula051601",
        r"Ramanujan gives "
        r"$\sum_{n=1}^{\infty}p(17n-12)q^n\,(q^{17};q^{17})_\infty=7\sum_{n=1}^{\infty}\tau_2(n)q^n+17J$, "
        r"where $\sum_{n=1}^{\infty}\tau_2(n)q^n=Qq\,(q;q)_\infty^{24}$.",
    ),
    rec(
        "RLN-P3-C05-Formula051603",
        r"Ramanujan gives "
        r"$\sum_{n=1}^{\infty}p(19n-15)q^n\,(q^{19};q^{19})_\infty=5\sum_{n=1}^{\infty}\tau_3(n)q^n+19J$, "
        r"where $\sum_{n=1}^{\infty}\tau_3(n)q^n=Rq\,(q;q)_\infty^{24}$.",
    ),
    rec(
        "RLN-P3-C05-Formula051604",
        r"Ramanujan gives "
        r"$\sum_{n=1}^{\infty}p(23n-22)q^n\,(q^{23};q^{23})_\infty=\sum_{n=1}^{\infty}\tau_5(n)q^n+23J$, "
        r"where $\sum_{n=1}^{\infty}\tau_5(n)q^n=QRq\,(q;q)_\infty^{24}$.",
    ),
    rec(
        "RLN-P3-C05-Formula052207",
        r"If $\lambda$ is an odd integer greater than $1$, then "
        r"$p\!\left(\dfrac{5^\lambda n-5^{\lambda-1}-1}{24}\right),"
        r"\,p\!\left(\dfrac{5^\lambda n-5^{\lambda+1}-1}{24}\right),"
        r"\,p\!\left(\dfrac{5^\lambda n-49\cdot 5^{\lambda-1}-1}{24}\right)\equiv 0\pmod{5^\lambda}$; "
        r"if $\lambda$ is a positive even integer, then "
        r"$p\!\left(\dfrac{5^\lambda n-5^\lambda-1}{24}\right)\equiv 0\pmod{5^\lambda}$.",
    ),
]
