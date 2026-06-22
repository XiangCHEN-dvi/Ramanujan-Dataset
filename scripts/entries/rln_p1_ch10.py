"""RLN Part I, Chapter 10 — mined manuscript fragments (pp. 358–361)."""

from __future__ import annotations

TOPICS_C10 = ["empirical-study-rogers-ramanujan-identities"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C10}


CHAPTER_10 = [
    rec(
        "RLN-P1-C10-Argument01",
        r"Ramanujan appeals to authority: ``Mr. MacMahon has verified up to $q^{55}$ and found the result correct "
        r"up to that term'' for the first Rogers–Ramanujan identity "
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{q^{n^2}}{(q;q)_n}=\frac{1}{(q;q^5)_\infty(q^4;q^5)_\infty}$. "
        r"He also calculates both sides independently through $q^{36}$.",
    ),
    rec(
        "RLN-P1-C10-Formula0201",
        r"Define, for $N\ge 0$, "
        r"$\displaystyle\nu^{(N)}(q):=\sum_{j=0}^{N}\frac{q^{j^2}}{(q;q)_j}$.",
    ),
    rec(
        "RLN-P1-C10-Formula0202",
        r"For $N\ge 1$, $\nu^{(N)}(q)=(1-q^N)\nu^{(N-1)}(q)+q^{N^2}$, with $\nu^{(0)}(q)=1$.",
    ),
    rec(
        "RLN-P1-C10-Formula0203",
        r"Ramanujan computes $\nu^{(7)}(q)\equiv 1-q^2-q^3+q^8+2q^9-q^{12}-q^{13}-q^{14}-q^{15}+q^{17}+q^{18}+q^{19}"
        r"+q^{20}-q^{21}-q^{23}-q^{24}+q^{27}+q^{28}-q^{32}-q^{34}+q^{36}\pmod{q^{37}}$.",
    ),
    rec(
        "RLN-P1-C10-Formula0204",
        r"Using this congruence, Ramanujan finds "
        r"$\displaystyle\sum_{n=0}^{\infty}\frac{q^{n^2}}{(q;q)_n}\equiv\frac{1}{(q;q)_\infty}(1-q^2-q^3+q^9+q^{11}-q^{21}-q^{24})\pmod{q^{37}}$, "
        r"agreeing with the product side of the first Rogers–Ramanujan identity through $q^{36}$.",
    ),
    rec(
        "RLN-P1-C10-Formula0205",
        r"Ramanujan observes that "
        r"$\displaystyle\lim_{N\to\infty}\nu^{(N)}(q)=1+\sum_{n=1}^{\infty}(-1)^n q^{n(5n-1)/2}(1+q^n)"
        r"=f(-q^2,-q^3)=(q^2;q^5)_\infty(q^3;q^5)_\infty(q^5;q^5)_\infty$.",
    ),
    rec(
        "RLN-P1-C10-Argument02",
        r"Ramanujan claims that, as $q\to 1$, "
        r"$\log\!\left\{\sum_{n=0}^{\infty}\dfrac{q^{n^2}}{(q;q)_n}\right\}\sim\dfrac{\pi^2}{15(1-q)}$ "
        r"and $\log\!\left\{\dfrac{1}{(q;q^5)_\infty(q^4;q^5)_\infty}\right\}\sim\dfrac{\pi^2}{15(1-q)}$.",
    ),
    rec(
        "RLN-P1-C10-Argument03",
        r"Ramanujan states: ``The numerical results of the cont. fraction go to prove the truth of the result,'' "
        r"referring to the Rogers–Ramanujan continued fraction "
        r"$C(q):=1+\dfrac{q}{1+\dfrac{q^2}{1+\dfrac{q^3}{1+\cdots}}"
        r"=\dfrac{\sum_{n=0}^{\infty}q^{n^2}/(q;q)_n}{\sum_{n=0}^{\infty}q^{n^2+n}/(q;q)_n}"
        r"=\dfrac{(q^2;q^5)_\infty(q^3;q^5)_\infty}{(q;q^5)_\infty(q^4;q^5)_\infty}$ for $|q|<1$.",
    ),
    rec(
        "RLN-P1-C10-Argument04",
        r"Ramanujan asserts that if "
        r"$v=\dfrac{q}{1+\dfrac{q^5}{1+\dfrac{q^{10}}{1+\cdots}}}$ "
        r"(so $v=R(q^5)$ in the notation of Chapter 1), then "
        r"$\dfrac{1}{v}-v-1$ vanishes when $q=e^{\pi i m/n}$, where $m$ and $n$ are coprime integers and $25\nmid n$.",
    ),
]
