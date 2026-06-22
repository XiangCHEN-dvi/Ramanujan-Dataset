"""RLN Part 3, Chapter 3 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C03 = ["ranks-cranks-part-ii"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C03}


CHAPTER_3 = [
    rec(
        "RLN-P3-C03-Entry3-1-1",
        r"If $A_n:=a^n+a^{-n}$, then $\dfrac{(q;q)_\infty}{(aq;q)_\infty(q/a;q)_\infty}=1-\dfrac{\displaystyle\sum_{m=1,n=0}^{\infty}(-1)^m q^{m(m+1)/2+mn}(A_{n+1}-A_n)}{(q;q)_\infty}$.",
    ),
    rec(
        "RLN-P3-C03-Entry3-2-1",
        r"Let $\rho_k=(-1)^k q^{k(k+1)/2}$. Then $\dfrac{(q;q)_\infty^2}{(qa;q)_\infty(q/a;q)_\infty}=\displaystyle\sum_{k=-\infty}^{\infty}\dfrac{\rho_k(1-a)}{1-aq^k}$.",
    ),
    rec(
        "RLN-P3-C03-Entry3-3-1",
        r"With $F_a(q):=\dfrac{(q;q)_\infty}{(aq;q)_\infty(q/a;q)_\infty}$ and $f(a,b):=\displaystyle\sum_{n=-\infty}^{\infty}a^{n(n+1)/2}b^{n(n-1)/2}$, $F_a(q)\equiv\dfrac{f(-q^6,-q^{10})}{(-q^4;q^4)_\infty}+\Bigl(a-\dfrac{1}{a}\Bigr)\dfrac{q f(-q^2,-q^{14})}{(-q^4;q^4)_\infty}\pmod{A_2}$, where $A_n:=a^n+a^{-n}$.",
    ),
    rec(
        "RLN-P3-C03-Entry3-4-1",
        r"If $A_n:=a^n+a^{-n}$, then $F_a(q)\equiv\dfrac{f(-q^6,-q^{21})f(-q^{12},-q^{15})}{(q^{27};q^{27})_\infty}+(A_1-1)\dfrac{q f(-q^3,-q^{24})f(-q^{12},-q^{15})}{(q^{27};q^{27})_\infty}+A_2\dfrac{q^2 f(-q^3,-q^{24})f(-q^6,-q^{21})}{(q^{27};q^{27})_\infty}\pmod{A_3+1}$, where $F_a(q):=\dfrac{(q;q)_\infty}{(aq;q)_\infty(q/a;q)_\infty}$.",
    ),
    rec(
        "RLN-P3-C03-Entry3-5-1",
        r"With $f(-q):=f(-q,-q^2)=(q;q)_\infty$, $S_2:=\displaystyle\sum_{k=-2}^{2}a^k$, and $A_n:=a^n+a^{-n}$, $F_a(q)\equiv\dfrac{f(-q^{10},-q^{15})}{f^2(-q^5,-q^{20})f^2(-q^{25})}+(A_1-1)\dfrac{q f^2(-q^{25})}{f(-q^5,-q^{20})}+A_2\dfrac{q^2 f^2(-q^{25})}{f(-q^{10},-q^{15})}-A_1\dfrac{q^3 f(-q^5,-q^{20})}{f^2(-q^{10},-q^{15})f^2(-q^{25})}\pmod{S_2}$, where $F_a(q):=\dfrac{(q;q)_\infty}{(aq;q)_\infty(q/a;q)_\infty}$.",
    ),
    rec(
        "RLN-P3-C03-Entry3-6-1",
        r"With $f(a,b):=\displaystyle\sum_{n=-\infty}^{\infty}a^{n(n+1)/2}b^{n(n-1)/2}$, $f(-q):=(q;q)_\infty$, $A_n:=a^n+a^{-n}$, and $S_3:=\displaystyle\sum_{k=-3}^{3}a^k$, $\dfrac{(q;q)_\infty}{(qa;q)_\infty(q/a;q)_\infty}\equiv\dfrac{1}{f(-q^7)}\Bigl(A_2+(A_1-1)q AB+A_2 q^2 B^2+(A_3+1)q^3 AC-A_1 q^4 BC-(A_2+1)q^6 C^2\Bigr)\pmod{S_3}$, where $A=f(-q^{21},-q^{28})$, $B=f(-q^{35},-q^{14})$, and $C=f(-q^{42},-q^7)$.",
    ),
    rec(
        "RLN-P3-C03-Entry3-7-1",
        r"With $A_m:=a^m+a^{-m}$ and $S_5:=\displaystyle\sum_{k=-5}^{5}a^k$, $F_a(q)\equiv\dfrac{1}{(q^{11};q^{11})_\infty(q^{121};q^{121})_\infty^2}\Bigl(ABCD+(A_1-1)q A^2 BE+A_2 q^2 AC^2 D+(A_3+1)q^3 ABD^2+(A_2+A_4+1)q^4 ABCE-(A_2+A_4)q^5 B^2 CE+(A_1+A_4)q^7 ABDE-(A_2+A_5+1)q^8 CDE^2-(A_4+1)q^9 ACDE-A_3 q^{10} BCDE\Bigr)\pmod{S_5}$, where $F_a(q):=\dfrac{(q;q)_\infty}{(aq;q)_\infty(q/a;q)_\infty}$, $A=f(-q^{55},-q^{66})$, $B=f(-q^{77},-q^{44})$, $C=f(-q^{88},-q^{33})$, $D=f(-q^{99},-q^{22})$, and $E=f(-q^{110},-q^{11})$.",
    ),
]
