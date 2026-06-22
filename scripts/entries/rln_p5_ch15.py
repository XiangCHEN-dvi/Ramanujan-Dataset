"""RLN Part 5, Chapter 15 — AI curated LaTeX (Entry only).

Euler products in Ramanujan's Lost Notebook; Ramanujan statements only.
"""

from __future__ import annotations

TOPICS_C15 = ["euler-products-lost-notebook-p5"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C15}


CHAPTER_15 = [
    rec(
        "RLN-P5-C15-Entry15-2-1",
        r"If $f(-q)=(q;q)_\infty$ as in (15.1.2) and $\sum_{n=1}^{\infty}a_n q^n"
        r"=qf^3(-q)f^3(-q^7)$, then "
        r"$\sum_{n=1}^{\infty}a_n n^{-s}=\dfrac{1}{1+7^{1-s}}\prod_{p\equiv 3,5,6\,(7)}"
        r"\dfrac{1}{1-p^{2(1-s)}}\prod_{q\equiv 1,2,4\,(7)}\dfrac{1}{1+2c_q q^{-s}+q^{2(1-s)}}$, "
        r"where $c_q=2$ if $q=2$ and $c_q=7v^2-u^2$ if $q=u^2+7v^2$.",
    ),
    rec(
        "RLN-P5-C15-Entry15-2-2",
        r"With $a_n$ defined by $\sum_{n=1}^{\infty}a_n q^n=qf^3(-q)f^3(-q^7)$, "
        r"Ramanujan gives $\sum_{n=1}^{\infty}a_n n^{-s}=\dfrac{1}{1+7^{1-s}}"
        r"\prod_{p\equiv 3,5,6\,(7)}\dfrac{1}{1-p^{2(1-s)}}\prod_{p\equiv 1,2,4\,(7)}"
        r"\dfrac{1}{1+C_p p^{-s}+p^{2(1-s)}}$, where $C_p=2p-a^2$ with $4p=a^2+7b^2$.",
    ),
    rec(
        "RLN-P5-C15-Entry15-2-3",
        r"If $\sum_{n=1}^{\infty}q(n)q^n=qf^4(-q)f^4(-q^5)$, then "
        r"$\sum_{n=1}^{\infty}q(n)n^{-s}=\dfrac{1}{1+5^{1-s}}\prod_{p\neq 5}"
        r"\dfrac{1}{1-q(p)p^{-s}+p^{3-2s}}$. Ramanujan records $q(2)=-4$, $q(3)=2$, "
        r"$q(5)=-5$, $q(7)=6$, and $q(p)^2<4p^3$ in general.",
    ),
    rec(
        "RLN-P5-C15-Entry15-2-4",
        r"If $\sum_{n=1}^{\infty}\varphi(n)q^n=qf^{12}(-q^2)$, then "
        r"$\sum_{n=1}^{\infty}\varphi(n)n^{-s}=\prod_{p\ \mathrm{odd}}"
        r"\dfrac{1}{1-\varphi(p)p^{-s}+p^{5-2s}}$.",
    ),
    rec(
        "RLN-P5-C15-Entry15-2-5",
        r"If $\sum_{n=1}^{\infty}\varphi(n)q^n=qf(-q^2)f(-q^{22})$, then "
        r"$\sum_{n=1}^{\infty}\varphi(n)n^{-s}=1-11^{-s}\prod_{p\equiv 1,3,4,5,9\,(11)}"
        r"(1+p^{-s}+p^{-2s})\prod_{q\ \mathrm{odd},\,q\equiv 2,6,7,8,10\,(11)}(1-q^{-2s})"
        r"\prod_{r=11A^2+B^2}(1-r^{-s})^2$.",
    ),
    rec(
        "RLN-P5-C15-Entry15-2-6",
        r"If $\sum_{n=1}^{\infty}\varphi(n)q^n=qf(-q^3)f(-q^{21})$, then "
        r"$\sum_{n=1}^{\infty}\varphi(n)n^{-s}=1+7^{-s}\prod_{p\ \mathrm{odd},\,p\equiv 2,8,11\,(21)}"
        r"(1+p^{-2s})\prod_{q\equiv 5,17,20\,(21)}(1-q^{-2s})\prod_{r=9A^2+7B^2}(1+r^{-s})^2"
        r"\prod_{t=A^2+63B^2}(1-t^{-s})^2$.",
    ),
    rec(
        "RLN-P5-C15-Entry15-2-7",
        r"If $\sum_{n=1}^{\infty}\varphi(n)q^n=qf^4(-q^6)R(q^6)$ with $R(q)$ as in (15.1.5), "
        r"then $\sum_{n=1}^{\infty}\varphi(n)n^{-s}=\prod_{p>3}\dfrac{1}{1-\varphi(p)p^{-s}+p^{7-2s}}$, "
        r"where $\varphi(p)=0$ if $p\equiv -1\,(6)$ and $\varphi(p)=(A+iB\sqrt{3})^7+(A-iB\sqrt{3})^7$ "
        r"if $p\equiv 1\,(6)$ with $p=A^2+3B^2$.",
    ),
    rec(
        "RLN-P5-C15-Entry15-2-8",
        r"If $\sum_{n=1}^{\infty}a_n q^n=q^3f^{18}(-q^4)$, then Ramanujan claims "
        r"$\sum_{n=1}^{\infty}a_n n^{-s}=\dfrac{1}{1-78\cdot 3^{-s}+3^{8-2s}}"
        r"\dfrac{1}{1+510\cdot 5^{-s}+5^{8-2s}}\dfrac{1}{1+1404\cdot 7^{-s}+7^{8-2s}}\cdots"
        r"-\dfrac{1}{1+78\cdot 3^{-s}+3^{8-2s}}\dfrac{1}{1-510\cdot 5^{-s}+5^{8-2s}}"
        r"\dfrac{1}{1-1404\cdot 7^{-s}+7^{8-2s}}\cdots$.",
    ),
    rec(
        "RLN-P5-C15-Entry15-2-9",
        r"Ramanujan conjectures analogous Euler products for "
        r"$\sum_{n=1}^{\infty}a_n n^{-s}$ whenever $\sum_{n=1}^{\infty}a_n q^n$ is any of "
        r"$q^5f^{10}(-q^{12})$, $q^7f^{14}(-q^{12})$, $q^5f^{20}(-q^6)$, or $q^{11}f^{22}(-q^{12})$.",
    ),
    rec(
        "RLN-P5-C15-Entry15-2-10",
        r"With $F(q):=qf^{16}(-q^3)=\sum_{n=1}^{\infty}A_n q^n$ and "
        r"$F_1(q):=qf^8(-q^3)Q(q^3)=\sum_{n=1}^{\infty}a_n q^n$, Ramanujan gives "
        r"$\sum_{n=1}^{\infty}(a_n+6A_n\sqrt{n})n^{-s}=\dfrac{1-6\sqrt{10}\cdot 2^{-s}+2^{7-2s}}"
        r"\dfrac{1+96\sqrt{10}\cdot 5^{-s}+5^{7-2s}}\dfrac{1-260\cdot 7^{-s}+7^{7-2s}}"
        r"\dfrac{1+1920\sqrt{10}\cdot 11^{-s}+11^{7-2s}}\cdots$ and "
        r"$\sum_{n=1}^{\infty}(a_n-6A_n\sqrt{n})n^{-s}=\dfrac{1+6\sqrt{10}\cdot 2^{-s}+2^{7-2s}}"
        r"\dfrac{1-96\sqrt{10}\cdot 5^{-s}+5^{7-2s}}\dfrac{1-260\cdot 7^{-s}+7^{7-2s}}"
        r"\dfrac{1-1920\sqrt{10}\cdot 11^{-s}+11^{7-2s}}\cdots$.",
    ),
    rec(
        "RLN-P5-C15-Entry15-4-1",
        r"For primes $p=6k+1$ with $p=A^2+3B^2$ and $A\equiv 1\,(3)$, Ramanujan defines "
        r"$\sum_{n=1}^{\infty}\Omega_0(n)q^{n/6}=q^{1/6}(q;q)_\infty^4$, "
        r"$\sum_{n=1}^{\infty}\Omega_1(n)q^{n/6}=q^{1/6}(q;q)_\infty^4 P(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_2(n)q^{n/6}=q^{1/6}(q;q)_\infty^4 Q(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_3(n)q^{n/6}=q^{1/6}(q;q)_\infty^4 R(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_4'(n)q^{n/6}=q^{1/6}(q;q)_\infty^4 Q^2(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_4''(n)q^{n/6}=q^{5/6}(q;q)_{20}^\infty$, "
        r"$\Omega_4(n)=\Omega_4'(n)+288\omega\sqrt{70}\,\Omega_4''(n)$ with $\omega^2=1$, "
        r"$\sum_{n=1}^{\infty}\Omega_5(n)q^{n/6}=q^{1/6}(q;q)_\infty^4 Q(q)R(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_7'(n)q^{n/6}=q^{1/6}(q;q)_\infty^4 Q^2(q)R(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_7''(n)q^{n/6}=q^{5/6}(q;q)_{20}^\infty R(q)$, and "
        r"$\Omega_7(n)=\Omega_7'(n)+10080\omega\sqrt{286}\,\Omega_7''(n)$ with $\omega^2=1$. "
        r"In each case $\sum_{n=1}^{\infty}\Omega_\lambda(n)n^{-s}=\prod_{p>3}"
        r"\dfrac{1}{1-\Omega_\lambda(p)p^{-s}+p^{2\lambda+1-2s}}$, with "
        r"$\Omega_\lambda(p)=0$ for $p\equiv -1\,(6)$ and "
        r"$\Omega_\lambda(p)=(A+iB\sqrt{3})^{2\lambda+1}+(A-iB\sqrt{3})^{2\lambda+1}$ for "
        r"$p\equiv 1\,(6)$ when $\lambda=0,2,3,5$; also $\Omega_1(n)=n\Omega_0(n)$.",
    ),
    rec(
        "RLN-P5-C15-Entry15-4-2",
        r"Ramanujan (List II) defines $\sum_{n=1}^{\infty}\Omega_0(n)q^{n/3}=q^{1/3}(q;q)_\infty^8$, "
        r"$\sum_{n=1}^{\infty}\Omega_1(n)q^{n/3}=q^{1/3}(q;q)_\infty^8 P(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_2'(n)q^{n/3}=q^{1/3}(q;q)_\infty^8 Q(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_2''(n)q^{n/3}=q^{1/3}(q;q)_{16}^\infty$, "
        r"$\Omega_2(n)=\Omega_2'(n)+6\omega\sqrt{10}\,\Omega_2''(n)$ with $\omega^2=1$, "
        r"$\sum_{n=1}^{\infty}\Omega_3(n)q^{n/3}=q^{1/3}(q;q)_\infty^8 R(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_4'(n)q^{n/3}=q^{1/3}(q;q)_\infty^8 Q^2(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_4''(n)q^{n/3}=q^{2/3}(q;q)_{16}^\infty Q(q)$, "
        r"$\Omega_4(n)=\Omega_4'(n)+6\omega\sqrt{70}\,\Omega_4''(n)$, "
        r"$\sum_{n=1}^{\infty}\Omega_5'(n)q^{n/3}=q^{1/3}(q;q)_\infty^8 Q(q)R(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_5''(n)q^{n/3}=q^{2/3}(q;q)_{16}^\infty R(q)$, "
        r"$\Omega_5(n)=\Omega_5'(n)+12\omega\sqrt{55}\,\Omega_5''(n)$, "
        r"$\sum_{n=1}^{\infty}\Omega_7'(n)q^{n/3}=q^{1/3}(q;q)_\infty^8 Q^2(q)R(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_7''(n)q^{n/3}=q^{2/3}(q;q)_{16}^\infty Q(q)R(q)$, and "
        r"$\Omega_7(n)=\Omega_7'(n)+12\omega\sqrt{910}\,\Omega_7''(n)$. "
        r"Each satisfies $\sum_{n=1}^{\infty}\Omega_\lambda(n)n^{-s}=\prod_{p\neq 3}"
        r"\dfrac{1}{1-\Omega_\lambda(p)p^{-s}+p^{2\lambda+3-2s}}$ with "
        r"$\Omega_\lambda(p)=0$ for $p\equiv -1\,(3)$ and "
        r"$\Omega_\lambda(p)=(A+iB\sqrt{3})^{2\lambda+3}+(A-iB\sqrt{3})^{2\lambda+3}$ for "
        r"$p\equiv 1\,(3)$ when $\lambda=0$ or $3$; also $\Omega_1(n)=n\Omega_0(n)$.",
    ),
    rec(
        "RLN-P5-C15-Entry15-4-3",
        r"For $p=4k+1$ with $p=A^2+4B^2$, Ramanujan (List III) defines "
        r"$\sum_{n=1}^{\infty}\Omega_0(n)q^{n/4}=q^{1/4}(q;q)_\infty^6$, "
        r"$\sum_{n=1}^{\infty}\Omega_1(n)q^{n/4}=q^{1/4}(q;q)_\infty^6 P(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_2(n)q^{n/4}=q^{1/4}(q;q)_\infty^6 Q(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_3'(n)q^{n/4}=q^{1/4}(q;q)_\infty^6 R(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_3''(n)q^{n/4}=q^{3/4}(q;q)_{18}^\infty$, "
        r"$\Omega_3(n)=\Omega_3'(n)+24\omega\sqrt{35}\,\Omega_3''(n)$ with $\omega^2=-1$, "
        r"$\sum_{n=1}^{\infty}\Omega_4(n)q^{n/4}=q^{1/4}(q;q)_\infty^6 Q^2(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_5'(n)q^{n/4}=q^{1/4}(q;q)_\infty^6 Q(q)R(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_5''(n)q^{n/4}=q^{3/4}(q;q)_{18}^\infty Q(q)$, "
        r"$\Omega_5(n)=\Omega_5'(n)+24\omega\sqrt{1155}\,\Omega_5''(n)$, "
        r"$\sum_{n=1}^{\infty}\Omega_7'(n)q^{n/4}=q^{1/4}(q;q)_\infty^6 Q^2(q)R(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_7''(n)q^{n/4}=q^{3/4}(q;q)_{18}^\infty Q^2(q)$, and "
        r"$\Omega_7(n)=\Omega_7'(n)+120\omega\sqrt{3003}\,\Omega_7''(n)$ with $\omega^2=-1$. "
        r"Each satisfies $\sum_{n=1}^{\infty}\Omega_\lambda(n)n^{-s}=\prod_{p\equiv 3\,(4)}"
        r"\dfrac{1}{1-\Omega_\lambda(p)p^{-s}-p^{2\lambda+2-2s}}\prod_{p\equiv 1\,(4)}"
        r"\dfrac{1}{1-\Omega_\lambda(p)p^{-s}+p^{2\lambda+2-2s}}$ with "
        r"$\Omega_\lambda(p)=0$ for $p\equiv -1\,(4)$ and "
        r"$\Omega_\lambda(p)=(A+2iB)^{2\lambda+2}+(A-2iB)^{2\lambda+2}$ for $p\equiv 1\,(4)$ "
        r"when $\lambda=0,2,4$; also $\Omega_1(n)=n\Omega_0(n)$.",
    ),
    rec(
        "RLN-P5-C15-Entry15-4-4",
        r"Ramanujan (List IV) defines $\sum_{n=1}^{\infty}\Omega_0(n)q^{n/12}=q^{1/12}(q;q)_\infty^2$, "
        r"$\sum_{n=1}^{\infty}\Omega_1(n)q^{n/12}=q^{1/12}(q;q)_\infty^2 P(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_2'(n)q^{n/12}=q^{1/12}(q;q)_\infty^2 Q(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_2''(n)q^{n/12}=q^{5/12}(q;q)_{10}^\infty$, "
        r"$\Omega_2(n)=\Omega_2'(n)+48\omega\,\Omega_2''(n)$ with $\omega^2=1$, "
        r"$\sum_{n=1}^{\infty}\Omega_3'(n)q^{n/12}=q^{1/12}(q;q)_\infty^2 R(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_3''(n)q^{n/12}=q^{7/12}(q;q)_{14}^\infty$, "
        r"$\Omega_3(n)=\Omega_3'(n)+360\omega\sqrt{3}\,\Omega_3''(n)$ with $\omega^2=-1$, "
        r"$\sum_{n=1}^{\infty}\Omega_4'(n)q^{n/12}=q^{1/12}(q;q)_\infty^2 Q^2(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_4''(n)q^{n/12}=q^{5/12}(q;q)_{10}^\infty Q(q)$, "
        r"$\Omega_4(n)=\Omega_4'(n)+672\omega\,\Omega_4''(n)$, "
        r"$\sum_{n=1}^{\infty}\Omega_5'(n)q^{n/12}=q^{1/12}(q;q)_\infty^2 Q(q)R(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_5''(n)q^{n/12}=q^{5/12}(q;q)_{10}^\infty R(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_5'''(n)q^{n/12}=q^{7/12}(q;q)_{14}^\infty Q(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_5''''(n)q^{n/12}=q^{11/12}(q;q)_{22}^\infty$, "
        r"$\Omega_5(n)=\Omega_5'(n)+96\omega_1\sqrt{1045}\,\Omega_5''(n)"
        r"+216\omega_2\sqrt{7315}\,\Omega_5'''(n)+103680\omega_1\omega_2\sqrt{7}\,\Omega_5''''(n)$ "
        r"with $\omega_1^2=1$, $\omega_2^2=-1$, "
        r"$\sum_{n=1}^{\infty}\Omega_7'(n)q^{n/12}=q^{1/12}(q;q)_\infty^2 Q^2(q)R(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_7''(n)q^{n/12}=q^{5/12}(q;q)_{10}^\infty Q(q)R(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_7'''(n)q^{n/12}=q^{7/12}(q;q)_{14}^\infty Q^2(q)$, "
        r"$\sum_{n=1}^{\infty}\Omega_7''''(n)q^{n/12}=q^{11/12}(q;q)_{22}^\infty Q(q)$, and "
        r"$\Omega_7(n)=\Omega_7'(n)+48\omega_1\sqrt{910\cdot 2911}\,\Omega_7''(n)"
        r"+216\omega_2\sqrt{5005\cdot 2911}\,\Omega_7'''(n)"
        r"-471744\omega_1\omega_2\sqrt{22}\,\Omega_7''''(n)$ with $\omega_1^2=1$, $\omega_2^2=-1$.",
    ),
]
