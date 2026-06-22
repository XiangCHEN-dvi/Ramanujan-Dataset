"""RLN Part 4, Chapter 20 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C20 = ["elementary-results-lost-notebook"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C20}


CHAPTER_20 = [
    rec(
        "RLN-P4-C20-Entry20-2-1",
        r"Suppose that $(x^6+ax)^5-(x^6+bx)^5=A(x^5+p)^5+B(x^5+q)^5+C(x^5+r)^5$. "
        r"Furthermore, write "
        r"$\dfrac{A}{1-pz}+\dfrac{B}{1-qz}+\dfrac{C}{1-rz}"
        r"=\dfrac{\alpha+\beta z+\gamma z^2}{1+\delta z+\epsilon z^2+\varphi z^3}$. Then "
        r"$\alpha=5(a-b)$, "
        r"$\beta=-\dfrac{2a-b}{a+b}(4a^2+3ab+4b^2)$, $\gamma=2(a^3-b^3)$, "
        r"$\delta=-\dfrac{2a^2+ab+b^2}{a+b}$, $\epsilon=a^2+ab+b^2$, and "
        r"$\varphi=-\dfrac{a^4+6a^3b+6a^2b^2+6ab^3+b^4}{10(a+b)}$.",
    ),
    rec(
        "RLN-P4-C20-Entry20-2-2",
        r"If $z=\dfrac{1}{N}$ and $N=\dfrac{1}{2}(a+b)+\dfrac{1}{2}(a-b)M$, and if "
        r"$\delta$, $\epsilon$, and $\varphi$ are given in Entry 20.2.1, then "
        r"$1+\delta z+\epsilon z^2+\varphi z^3=0$ is equivalent to "
        r"$5(a+b)(M^3-M)=(a-b)(5M^2-1)$.",
    ),
    rec(
        "RLN-P4-C20-Entry20-2-3",
        r"Suppose that "
        r"$\dfrac{x^5}{(x+a)^3+(x+b)^6}=A(x+p)^4+B(x+q)^4+Cx^4$. Then "
        r"$p=\dfrac{a^3+b^3}{a^2+b^2}-(a-b)\sqrt{3ab}$, "
        r"$q=\dfrac{a^3+b^3}{a^2+b^2}+(a-b)\sqrt{3ab}$, "
        r"$A=-\dfrac{(a^2+b^2-(a-b)\sqrt{3ab})^4}{8(a-b)\sqrt{3ab}(a^3+b^3)^2}$, "
        r"$B=\dfrac{(a^2+b^2+(a-b)\sqrt{3ab})^4}{8(a-b)\sqrt{3ab}(a^3+b^3)^2}$, and "
        r"$C=\dfrac{(a^3-b^3)(a-b)^3}{(a^3+b^3)^2}$.",
    ),
    rec(
        "RLN-P4-C20-Entry20-2-4",
        r"A family of solutions to $A^4+B^4+C^4=D^4+E^4+F^4$ is given by "
        r"$\dfrac{\sqrt[5]{x^5(n^2+3)^2(n^4+42n^2+9)^2+x(n^2-3)(n^2+6n+3)}}{64}"
        r"-\dfrac{\sqrt[5]{x^5(n^2+3)^2(n^4+42n^2+9)^2+x(n^2-3)(n^2-6n+3)}}{64}"
        r"=\dfrac{\sqrt[5]{x^4(n^2+3)(n^4+42n^2+9)(n^4+6n^3+18n^2-18n+9)+(n^2-3)}}{64}"
        r"-\dfrac{\sqrt[5]{x^4(n^2+3)(n^4+42n^2+9)(n^4-6n^3+18n^2+18n+9)+(n^2-3)}}{64}"
        r"$+\dfrac{\sqrt[5]{6nx^4(n^2+3)(n^4+42n^2+9)(n^2+4n-3)}}{64}"
        r"-\dfrac{\sqrt[5]{6nx^4(n^2+3)(n^4+42n^2+9)(n^2-4n-3)}}{64}$.",
    ),
    rec(
        "RLN-P4-C20-Entry20-3-1",
        r"If $g^4=5$, then "
        r"$\dfrac{\sqrt[5]{3+2g}-\sqrt[5]{4-4g}}{\sqrt[5]{3+2g}+\sqrt[5]{4-4g}}=2+g+g^2+g^3$.",
    ),
    rec(
        "RLN-P4-C20-Entry20-3-2",
        r"If $g^5=2$, then "
        r"$\dfrac{\sqrt{g+3}+\sqrt{5g-5}}{\sqrt{g+3}-\sqrt{5g-5}}=g+g^2$ and "
        r"$\dfrac{\sqrt{g^2+1+\sqrt{4g-3}}}{\sqrt{g^2+1-\sqrt{4g-3}}}"
        r"=\dfrac{1}{5}\left(1+g^2+g^3+g^9\right)^2$. "
        r"If $g^5=3$, then "
        r"$\dfrac{\sqrt{g^2+1+\sqrt{5g-5}}}{\sqrt{g^2+1-\sqrt{5g-5}}}"
        r"=\dfrac{1}{g+g+g^2+g^3}$. "
        r"If $g^5=2$, then $\sqrt{1+g^2}=\dfrac{g^4+g^3+g-1}{\sqrt{5}}$ and "
        r"$\sqrt{4g-3}=\dfrac{g^9+g^7-g^6-1}{\sqrt{5}}$. "
        r"If $g^5=3$, then $\sqrt[3]{2-g^3}=\dfrac{1+g-g^2}{\sqrt[3]{5}}$. "
        r"If $g^5=2$, then $\sqrt[5]{1+g+g^3}=\dfrac{\sqrt{1+g^2}}{\sqrt[10]{5}}$.",
    ),
    rec(
        "RLN-P4-C20-Entry20-4-1",
        r"$\sqrt[3]{\dfrac{1}{3}+\sqrt[3]{\dfrac{5}{3}}}"
        r"=\sqrt[3]{\dfrac{\sqrt[3]{5}-1}{2}-\dfrac{\sqrt[3]{5}}{\sqrt[3]{3}}}"
        r"=\sqrt[3]{\dfrac{3+\sqrt[3]{5}}{\sqrt[3]{5}-1}}"
        r"=\sqrt[3]{\dfrac{\sqrt[3]{3}+\sqrt[3]{15}}{2}-\sqrt[3]{5}}$. "
        r"If $a$, $b$, and $c$ are arbitrary numbers, then "
        r"$\dfrac{\sqrt[3]{\sqrt[3]{(a+b)(a^2+b^2)-a}}}{\sqrt[3]{\sqrt[3]{(a+b)(a^2+b^2)-b}}}"
        r"=\dfrac{\sqrt[3]{(a+b)^2-\sqrt[3]{a^2+b^2}}}{\sqrt[3]{(a+b)^2+\sqrt[3]{a^2+b^2}}}\,(a^2+ab+b^2)$, "
        r"$\dfrac{(\sqrt{a^2+ab+b^2}-a)(\sqrt{a^2+ab+b^2}-b)}{a+b-\sqrt{a^2+ab+b^2}}=a+b$, and "
        r"$\dfrac{-a+\sqrt[4]{(c+a)(a+b)}}{4}"
        r"-\dfrac{b+\sqrt[4]{(a+b)(b+c)}}{4}"
        r"-\dfrac{c+\sqrt[4]{(b+c)(c+a)}}{4}"
        r"=\dfrac{2\sqrt{ab+bc+ca}}{\sqrt{a+b}+\sqrt{b+c}+\sqrt{c+a}}$.",
    ),
    rec(
        "RLN-P4-C20-Entry20-6-1",
        r"$\dfrac{9}{5}+\sqrt{\dfrac{9}{5}}=3.14164\ldots=\pi+0.00005\ldots$.",
    ),
]
