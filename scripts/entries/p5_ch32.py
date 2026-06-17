"""Part 5, Chapter 32 entries — continued fractions supplement (curated LaTeX)."""

from __future__ import annotations

TOPICS = ["continued-fractions-supplement"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS}


CHAPTER_32 = [

    rec(
        "RN-P5-C32-Entry53",
        r"Entry 53 (p. 342). Let $x$ and $y$ be complex numbers with $\operatorname{Re} x > 0$ and $\operatorname{Re} y > 0$. Then "
        r"$\displaystyle\cfrac{(y-1)^2+n}{x+y}=\cfrac{(y+3)^2+n}{2y}+\cfrac{(y+5)^2+n}{2y}+\cfrac{(y+7)^2+n}{2y}+\cdots "
        r"=\cfrac{(x-1)^2+n}{2x}+\cfrac{(x-3)^2+n}{2x}+\cfrac{(x-5)^2+n}{2x}+\cdots "
        r"=\cfrac{(y-1)^2-n}{2y}+\cfrac{(x-1)^2-n}{2x}+\cfrac{(y-3)^2+n}{2x}+\cfrac{(x-3)^2-n}{2x}+\cdots "
        r"=\cfrac{(x+1)^2+n}{y+x}+\cfrac{(y+1)^2+n}{2y}+\cfrac{(x+3)^2+n}{2x}+\cfrac{(y+3)^2+n}{2y}+\cdots$.",
    )
,
    rec(
        "RN-P5-C32-Entry54",
        r"Entry 54 (p. 342). For all complex numbers $x$ and $n$, "
        r"$\displaystyle 1+\frac{x}{n+1}+\frac{x}{n+2}+\frac{x}{n+3}+\cdots "
        r"=\cfrac{x}{n-1-x}+\cfrac{1\cdot x}{n+x-1}+\cfrac{2\cdot x}{n+x-2}+\cfrac{3\cdot x}{n+x-3}+\cdots$.",
    )
,
    rec(
        "RN-P5-C32-Entry55",
        r"Entry 55 (p. 343). For every complex number $x$, "
        r"$\displaystyle 1+\frac{x}{1}+\frac{x}{2}+\frac{x}{3}+\cdots "
        r"=\cfrac{x}{1}+\cfrac{1\cdot x}{1}+\cfrac{2\cdot x}{2}+\cfrac{3\cdot x}{3}+\cdots$.",
    )
,
    rec(
        "RN-P5-C32-Entry56",
        r"Entry 56 (p. 342). For all complex $x$, "
        r"$\displaystyle\frac{e^{2x}-1}{x}=\cfrac{2x}{1}+\cfrac{2x}{2}+\cfrac{2x}{3}+\cfrac{2x}{4}+\cdots$.",
    )
,
    rec(
        "RN-P5-C32-Entry57",
        r"Entry 57 (p. 343). For all complex numbers $x$ and $n$, "
        r"$\displaystyle\frac{{}_2F_1(2;n+2;x)}{{}_2F_1(1;n+1;x)} "
        r"=\cfrac{x}{n}+\cfrac{n\cdot x}{n+1}+\cfrac{(n+1)\cdot x}{n+2}+\cfrac{(n+2)\cdot x}{n+3}+\cdots$.",
    )
,
    rec(
        "RN-P5-C32-Entry58",
        r"Entry 58 (p. 343). Let $x$ be a complex number such that $\operatorname{Re} x^2 > -\tfrac14$. Then "
        r"$\displaystyle\frac{\sinh^{-1} x}{x}=\cfrac{1}{1/2}+\cfrac{x^2/2}{1/2}+\cfrac{2x^2/2}{1}+\cfrac{3x^2/2}{1/2}+\cfrac{4x^2/2}{1}+\cdots$.",
    )
,
    rec(
        "RN-P5-C32-Entry59",
        r"Entry 59 (p. 343). Let $x$ be any complex number such that $\operatorname{Re} x^2 > -\tfrac54$. Then "
        r"$\displaystyle\frac{\tan^{-1} x}{x}=\cfrac{1}{1/2}+\cfrac{x^2/2}{1/2}+\cfrac{3x^2/2}{1}+\cfrac{4x^2/2}{1/2}+\cdots$.",
    )
,
    rec(
        "RN-P5-C32-Entry60",
        r"Entry 60 (p. 339). For $1 \le k \le n$, assume that $a_k \ne 0$. Then "
        r"$\displaystyle\cfrac{1}{a_1}-\cfrac{1}{a_1+a_2}+\cfrac{1}{a_2+a_3}-\cdots+(-1)^{n-1}\cfrac{1}{a_{n-1}+a_n} "
        r"=\cfrac{a_1}{a_1+a_2}+\cfrac{a_2}{a_2+a_3}+\cdots+\cfrac{a_{n-1}}{a_{n-1}+a_n}$ "
        r"(Ramanujan's statement is for $n=\infty$).",
    )
,
    rec(
        "RN-P5-C32-Entry61",
        r"Entry 61 (p. 339). The continued fraction "
        r"$\displaystyle\cfrac{1}{1}+\cfrac{a_1}{1}+\cfrac{a_2}{1}+\cfrac{a_3}{1}+\cfrac{a_4}{1}+\cdots$ "
        r"is intelligible (convergent) or not according as $\lim_{n\to\infty} a_n < \tfrac14$ or $> \tfrac14$.",
    )
,
    rec(
        "RN-P5-C32-Entry62",
        r"Entry 62 (p. 340). The continued fraction "
        r"$\displaystyle\cfrac{p}{1}+\cfrac{a_1}{1}+\cfrac{a_2}{1}+\cfrac{a_3}{1}+\cdots$ "
        r"tends to two limits or one limit according as "
        r"$\displaystyle\sum_{n=1}^{\infty}\frac{a_{2n-1}a_{2n}}{\sqrt{a_1a_2\cdots a_{2n}}}$ is divergent or convergent.",
    )
,
    rec(
        "RN-P5-C32-Entry63",
        r"Entry 63 (p. 340). Consider "
        r"$\displaystyle\mathrm{CF}:=\cfrac{a_1}{1}+\cfrac{a_2}{1}+\cfrac{a_3}{1}+\cfrac{a_4}{1}+\cdots$. "
        r"(1) If $\mathrm{CF}$ is limit $1$-periodic, then $\mathrm{CF}$ converges if $\lim_{n\to\infty} a_n = a \in \mathbb{C}\setminus[\tfrac34,\infty)$. "
        r"(2) If $\mathrm{CF}$ is limit $2$-periodic with limits $a$ and $b$, then $\mathrm{CF}$ converges if "
        r"$\dfrac{ab}{[1-(a+b)]^2}\in\mathbb{C}\setminus[\tfrac14,\infty)$, where $a+b\ne 1$. "
        r"(3) If $\mathrm{CF}$ is limit $3$-periodic with $\lim_{n\to\infty}a_{3n+1}=a$, $\lim_{n\to\infty}a_{3n+2}=b$, and $\lim_{n\to\infty}a_{3n}=c$, "
        r"then $\mathrm{CF}$ converges if $\dfrac{abc}{[1-(a+b+c)]^2}\in\mathbb{C}\setminus[\tfrac14,\infty)$, where $a+b+c\ne 0$, "
        r"and if $|a|>|c|$ when $b=1$, $|b|>|a|$ when $c=1$, and $|c|>|b|$ when $a=1$. "
        r"(4) If $\mathrm{CF}$ is limit $4$-periodic with $a_{4n+1},a_{4n+2},a_{4n+3},a_{4n}$ tending to $a,b,c,d$, then $\mathrm{CF}$ converges if "
        r"$\dfrac{abcd}{[1-(a+b+c+d)+(ac+bd)]^2}\in\mathbb{C}\setminus[\tfrac14,\infty)$, where $a+b+c+d-(ac+bd)\ne 1$, "
        r"and if $|ab|>|cd|$ when $b+c=1$, $|bc|>|ad|$ when $c+d=1$, $|cd|>|ab|$ when $a+d=1$, and $|ad|>|bc|$ when $a+b=1$. "
        r"(5) If $\mathrm{CF}$ is limit $5$-periodic with $a_{5n+1},\ldots,a_{5n}$ tending to $a,b,c,d,e$, then $\mathrm{CF}$ converges if "
        r"$\dfrac{abcde}{[1-(a+b+c+d+e)+(a(c+d)+b(d+e)+ce)]^2}\in\mathbb{C}\setminus[\tfrac14,\infty)$, where the denominator is nonzero, "
        r"and with the five extra Thiele-oscillation conditions stated by Berndt for the cases $b+c+d-bd=1$, $c+d+e-ce=1$, "
        r"$d+e+a-da=1$, $e+a+b-eb=1$, and $a+b+c-ac=1$.",
    )
,
    rec(
        "RN-P5-C32-Entry64",
        r"Entry 64 (p. 342). If $n$ is even, then "
        r"$\displaystyle\cfrac{a_1}{b_1+b_2+\cdots+b_n} "
        r"=\cfrac{a_1a_2}{a_2+b_1b_2}+\cfrac{a_2a_3a_4}{a_4+b_2b_3+a_2(a_4+b_3b_4)} "
        r"+\cdots+\cfrac{a_{n-2}a_{n-1}a_n}{a_n+b_{n-2}b_{n-1}+b_{n-1}b_n+a_{n-1}(a_n+b_{n-1}b_n)}$ "
        r"(the finite form of the even part of an infinite continued fraction).",
    )
,
]
