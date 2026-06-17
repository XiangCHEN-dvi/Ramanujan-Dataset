"""Part III, Chapter 21 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C21 = ["eisenstein-series"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C21}


CHAPTER_21 = [
    rec(
        "RN-P3-C21-Entry01i",
        r"Let $y>0$, $q=e^{-y}$, and write $x=k^2$ and $z=2K/\pi$ in the notation of "
        r"Chapter 17. Suppose $y^2/\pi^2$ is rational. Then "
        r"$\displaystyle L-\frac{3}{y}=1-24\sum_{n=1}^\infty\frac{n}{e^{2ny}-1}$ "
        r"is a complete series which, when divided by $z^2$, can be expressed by radicals "
        r"precisely in the same manner as "
        r"$\displaystyle\frac{1}{z^4}\Bigl(1+240\sum_{n=1}^\infty\frac{n^3}{e^{2ny}-1}\Bigr)$ "
        r"and "
        r"$\displaystyle\frac{1}{z^6}\Bigl(1-504\sum_{n=1}^\infty\frac{n^5}{e^{2ny}-1}\Bigr)$ "
        r"when divided by $z^4$ and $z^6$, respectively.",
    ),
    rec(
        "RN-P3-C21-Entry01ii",
        r"With the notation of Entry 1(i), "
        r"$\displaystyle 1-24\sum_{n=0}^\infty\frac{2n+1}{e^{(2n+1)y}+1}=z^2(1-2x)$.",
    ),
    rec(
        "RN-P3-C21-Entry01iii",
        r"With the notation of Entry 1(i), "
        r"$\displaystyle 1-240\sum_{n=1}^\infty\frac{(-1)^{n+1}n^3}{e^{ny}+(-1)^n}"
        r"=z^4\{1-16x(1-x)\}$.",
    ),
    rec(
        "RN-P3-C21-Entry01iv",
        r"With the notation of Entry 1(i), "
        r"$\displaystyle 1+504\sum_{n=1}^\infty\frac{(-1)^{n+1}n^5}{e^{ny}+(-1)^n}"
        r"=z^6(1-2x)\{1+32x(1-x)\}$.",
    ),
    rec(
        "RN-P3-C21-Entry02i",
        r"For $|q|<1$, "
        r"$\displaystyle\frac{\varphi'(q)}{12q\,\varphi(q)}"
        r"=1-24\sum_{n=1}^\infty\frac{nq^{2n}}{1-q^{2n}}"
        r"-24\sum_{n=0}^\infty\frac{(2n+1)q^{2n+1}}{1+q^{2n+1}}$.",
    ),
    rec(
        "RN-P3-C21-Entry02ii",
        r"For $|q|<1$, "
        r"$\displaystyle\frac{d}{dq}\frac{24q}{q^{1/8}\psi(q)}"
        r"=3+24\sum_{n=0}^\infty\frac{(2n+1)q^{2n+1}}{1+q^{2n+1}}"
        r"-24\sum_{n=1}^\infty\frac{4nq^{4n}}{1-q^{4n}}$.",
    ),
    rec(
        "RN-P3-C21-Entry02iii",
        r"For $|q|<1$, "
        r"$\displaystyle\frac{d}{dq}\log\{q^{1/24}f(-q)\}"
        r"=1-24\sum_{n=1}^\infty\frac{nq^n}{1-q^n}$.",
    ),
    rec(
        "RN-P3-C21-Entry02iv",
        r"For $|q|<1$, "
        r"$\displaystyle\frac{d}{dq}\log\{q^{1/24}/\chi(q)\}"
        r"=1-24\sum_{n=0}^\infty\frac{(2n+1)q^{2n+1}}{1+q^{2n+1}}$.",
    ),
    rec(
        "RN-P3-C21-Entry02v",
        r"By differentiating the equation for $m$ once or the equation for $\alpha$, $\beta$ "
        r"twice, one can calculate the value of the first series in Entry 2(i).",
    ),
    rec(
        "RN-P3-C21-Entry03i",
        r"Let $\beta$ have degree $3$ over $\alpha$, and let $m$ denote the associated "
        r"multiplier. Then "
        r"$\displaystyle 1+12\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-36\sum_{k=1}^\infty\frac{kq^{6k}}{1-q^{6k}}$ "
        r"equals each of the following five expressions: "
        r"$\displaystyle z_1z_3\left\{\frac{(3+m)^2+3(m-1)^2}{4m}\right\}^2$, "
        r"$\displaystyle z_1z_3\left\{\frac{m(\alpha^3)^{1/4}}{4}+\frac{(\beta^3)^{1/4}}{4m}-\alpha\right\}^2$, "
        r"$\displaystyle \varphi(q)\varphi(q^3)+4q\psi(q^2)\psi(q^6)$, "
        r"$\displaystyle\frac{\{\psi^3(q^2)+2\psi^3(q^6)\}^2}{\{\psi(q^6)+3q\psi(q^2)\}^2}$, "
        r"and "
        r"$\displaystyle\frac{\{f^{12}(-q)+27qf^{12}(-q^3)\}^{1/3}}{f^3(-q)f^3(-q^3)}$.",
    ),
    rec(
        "RN-P3-C21-Entry03ii",
        r"$\displaystyle 1+12\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-36\sum_{k=1}^\infty\frac{kq^{6k}}{1-q^{6k}}"
        r"=\frac{\{\varphi^4(q)+3\varphi^4(q^3)\}^2}{4\varphi(q)\varphi(q^3)}"
        r"=\varphi^2(q)\varphi^2(q^3)-4q\psi^2(-q)\psi^2(-q^3)$.",
    ),
    rec(
        "RN-P3-C21-Entry03iii",
        r"Let $\beta$ have degree $3$ with respect to $\alpha$. Then "
        r"$\displaystyle 1+12\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-36\sum_{k=1}^\infty\frac{kq^{6k}}{1-q^{6k}}"
        r"=\tfrac12\varphi^2(q)\varphi^2(q^3)\{1+\sqrt{\alpha\beta}+\sqrt{(1-\alpha)(1-\beta)}\}$.",
    ),
    rec(
        "RN-P3-C21-Entry04i",
        r"$\displaystyle 1+6\sum_{k=1}^\infty\frac{kq^k}{1-q^k}"
        r"-30\sum_{k=1}^\infty\frac{kq^{5k}}{1-q^{5k}}$ "
        r"$\displaystyle =\frac{\{f^{12}(-q)+22qf^6(-q)f^6(-q^5)+125q^2f^{12}(-q^5)\}^{1/2}}"
        r"{f(-q)f(-q^5)}$ "
        r"$\displaystyle =\frac{\psi^4(q)+2q\psi^2(q)\psi^2(q^5)+5q^2\psi^4(q^5)}"
        r"{\psi(q)\psi(q^5)}"
        r"$\displaystyle\times\{\psi^4(q)-2q\psi^2(q)\psi^2(q^5)+5q^2\psi^4(q^5)\}^{1/2}$.",
    ),
    rec(
        "RN-P3-C21-Entry04ii",
        r"Let $\beta$ have degree $5$ over $\alpha$, and let $p$ denote the associated "
        r"multiplier. Then "
        r"$\displaystyle 1+6\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-30\sum_{k=1}^\infty\frac{kq^{10k}}{1-q^{10k}}$ "
        r"$\displaystyle =\frac{p(m^2+2m+5)z_1^2}{16m^2}$ "
        r"$\displaystyle =\left(1-\frac{2qf^2(-q^{10})}{\varphi^2(q)\varphi^2(q^5)}\right)"
        r"\left(1-\frac{4q}{\chi^4(q)\chi^4(q^5)}\right)^{1/2}$.",
    ),
    rec(
        "RN-P3-C21-Entry04iii",
        r"Let $\beta$ have degree $5$ over $\alpha$. Then "
        r"$\displaystyle 1+6\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-30\sum_{k=1}^\infty\frac{kq^{10k}}{1-q^{10k}}$ "
        r"$\displaystyle =\tfrac12\varphi^2(q)\varphi^2(q^5)\{3+\sqrt{\alpha\beta}+\sqrt{(1-\alpha)(1-\beta)}\}$ "
        r"$\displaystyle\times\{\alpha(1+\sqrt{\alpha\beta}+\sqrt{(1-\alpha)(1-\beta)})\}^{1/2}$ "
        r"$\displaystyle =\varphi^2(q)\varphi^2(q^5)\left(\tfrac12\{1+\alpha\beta+(1-\alpha)(1-\beta)\}\right."
        r"\left.\tfrac12\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/3}\right)^{1/2}$.",
    ),
    rec(
        "RN-P3-C21-Entry05i",
        r"$\displaystyle 1+4\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-28\sum_{k=1}^\infty\frac{kq^{14k}}{1-q^{14k}}$ "
        r"$\displaystyle =z_1z_7(1-2t+2t^2)^4$ "
        r"$\displaystyle =\{\varphi(q)\varphi(q^7)-2q\psi(-q)\psi(-q^7)\}^2$ "
        r"$\displaystyle =(2q)^{2/3}\frac{f^2(q)}{f^2(q^7)}\varphi(q^7)"
        r"(-6t+18t^2-56t^4+24t^5+8t^6)^{1/3}$ "
        r"$\displaystyle =\frac{f^4(q)}{f^4(q^7)}\,"
        r"\frac{2+t+23t^2-64t^3+72t^4-48t^5+16t^6}{t(1-t)}$, "
        r"where $t$ is defined as in Chapter 19, Entry 19(2).",
    ),
    rec(
        "RN-P3-C21-Entry05ii",
        r"$\displaystyle 1+4\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-28\sum_{k=1}^\infty\frac{kq^{14k}}{1-q^{14k}}"
        r"=\{\varphi(q)\varphi(q^7)-2q\psi(-q)\psi(-q^7)\}^2$.",
    ),
    rec(
        "RN-P3-C21-Entry05iii",
        r"Let $\beta$ have degree $7$ over $\alpha$. Then "
        r"$\displaystyle 1+4\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-28\sum_{k=1}^\infty\frac{kq^{14k}}{1-q^{14k}}$ "
        r"$\displaystyle =\tfrac12\varphi^2(q)\varphi^2(q^7)\{1+\sqrt{\alpha\beta}+\sqrt{(1-\alpha)(1-\beta)}\}$.",
    ),
    rec(
        "RN-P3-C21-Entry06i",
        r"If $\beta$ has degree $3$, then "
        r"$\displaystyle 1+12\sum_{k=1}^\infty\frac{k(-q)^k}{1-(-q)^k}"
        r"-36\sum_{k=1}^\infty\frac{k(-q)^{3k}}{1-(-q)^{3k}}$ "
        r"$\displaystyle =\varphi^2(q)\varphi^2(q^3)\{(\alpha\beta)^{1/4}-\{(1-\alpha)(1-\beta)\}^{1/4}\}^2$.",
    ),
    rec(
        "RN-P3-C21-Entry06ii",
        r"If $\beta$ has degree $5$, then "
        r"$\displaystyle 1+6\sum_{k=1}^\infty\frac{k(-q)^k}{1-(-q)^k}"
        r"-30\sum_{k=1}^\infty\frac{k(-q)^{5k}}{1-(-q)^{5k}}$ "
        r"$\displaystyle =\varphi^2(q)\varphi^2(q^5)(\sqrt{\beta}+\sqrt{(1-\alpha)(1-\beta)})"
        r"\left(\tfrac12\{1+\sqrt{\alpha\beta}+\sqrt{(1-\alpha)(1-\beta)}\}\right)^{1/2}$.",
    ),
    rec(
        "RN-P3-C21-Entry06iii",
        r"If $\beta$ has degree $7$, then "
        r"$\displaystyle 1+4\sum_{k=1}^\infty\frac{k(-q)^k}{1-(-q)^k}"
        r"-28\sum_{k=1}^\infty\frac{k(-q)^{7k}}{1-(-q)^{7k}}$ "
        r"$\displaystyle =\varphi^2(q)\varphi^2(q^7)\{(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}\}^2$.",
    ),
    rec(
        "RN-P3-C21-Entry07i",
        r"$\displaystyle 1+3\sum_{k=1}^\infty\frac{kq^k}{1-q^k}"
        r"-27\sum_{k=1}^\infty\frac{kq^{9k}}{1-q^{9k}}$ "
        r"$\displaystyle =\frac{q^{1/3}f^6(q^3)}{f(q)f(q^9)}"
        r"\left\{\frac{(1+t+t^2)(1-2t+4t^2)}{t(1+2t)^2(1-t)}\right\}^{1/3}$ "
        r"$\displaystyle =\frac{q^{21/12}\psi(-q^3)\psi(-q)\psi(-q^9)}{z_3z_9}"
        r"\left\{\frac{t(1+t+t^2)}{1+2t}\right\}^{1/2}\left\{\frac{t(1+t+t^2)}{1+2t}-3\right\}^{1/2}$, "
        r"where $t$ is as in Chapter 20, Section 3.",
    ),
    rec(
        "RN-P3-C21-Entry07ii",
        r"$\displaystyle 1+3\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-27\sum_{k=1}^\infty\frac{kq^{18k}}{1-q^{18k}}$ "
        r"$\displaystyle =\left\{\frac{\varphi^4(q^3)+3q\varphi^2(q)\varphi^2(q^9)}{\varphi^2(q^3)}\right\}^2"
        r"=\left\{\frac{\varphi^4(q^3)+3q\varphi^2(q)\varphi^2(q^9)}{\varphi^3(q)\varphi^3(q^9)}\right\}^2$.",
    ),
    rec(
        "RN-P3-C21-Entry07iii",
        r"With $w=f(-q)/\{qf(-q^{25})\}$, "
        r"$\displaystyle 1+\sum_{k=1}^\infty\frac{kq^k}{1-q^k}"
        r"-25\sum_{k=1}^\infty\frac{kq^{25k}}{1-q^{25k}}$ "
        r"$\displaystyle =\frac{qf^5(-q^5)}{f(-q)}"
        r"\left(\tfrac12(w^4+10w^3+45w^2+100w+125)\right."
        r"\left.\tfrac12(w^4+4w^3+9w^2+10w+5)\right)^{1/2}(w^2+2w+5)^{1/2}$.",
    ),
    rec(
        "RN-P3-C21-Entry08i",
        r"$\displaystyle 5+12\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-132\sum_{k=1}^\infty\frac{kq^{22k}}{1-q^{22k}}$ "
        r"$\displaystyle =5\varphi^2(q)\varphi^2(q^{11})-20qf^2(q)f^2(q^{11})"
        r"+32q^2f^2(-q^2)f^2(-q^{22})-20q^3\psi^2(-q)\psi^2(-q^{11})$.",
    ),
    rec(
        "RN-P3-C21-Entry08ii",
        r"Let $\beta$ have degree $11$ over $\alpha$. Then "
        r"$\displaystyle 5+12\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-132\sum_{k=1}^\infty\frac{kq^{22k}}{1-q^{22k}}$ "
        r"$\displaystyle =\varphi^2(q)\varphi^2(q^{11})\{2+2(\alpha\beta)^{1/2}"
        r"+2\{(1-\alpha)(1-\beta)\}^{1/2}+(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}"
        r"-\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/4}\}$.",
    ),
    rec(
        "RN-P3-C21-Entry08iii",
        r"If $\beta$ has degree $19$, then "
        r"$\displaystyle 3+4\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-76\sum_{k=1}^\infty\frac{kq^{38k}}{1-q^{38k}}$ "
        r"$\displaystyle =\varphi^2(q)\varphi^2(q^{19})\{1+(\alpha\beta)^{1/2}+\{(1-\alpha)(1-\beta)\}^{1/2}"
        r"+(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}"
        r"-\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/4}\}$.",
    ),
    rec(
        "RN-P3-C21-Entry09i",
        r"If $\beta$ has degree $23$, then "
        r"$\displaystyle 11+12\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-276\sum_{k=1}^\infty\frac{kq^{46k}}{1-q^{46k}}$ "
        r"$\displaystyle =\varphi^2(q)\varphi^2(q^{23})\{21(1+\sqrt{\alpha\beta}+\sqrt{(1-\alpha)(1-\beta)})"
        r"-10\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/6}$ "
        r"$\displaystyle -8\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/12}"
        r"(1+(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4})\}$.",
    ),
    rec(
        "RN-P3-C21-Entry09ii",
        r"If $\beta$ has degree $15$, then "
        r"$\displaystyle 7+12\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-180\sum_{k=1}^\infty\frac{kq^{30k}}{1-q^{30k}}$ "
        r"$\displaystyle =\tfrac12\varphi^2(q)\varphi^2(q^{15})"
        r"(\{1+(\alpha\beta)^{1/8}+\{(1-\alpha)(1-\beta)\}^{1/8}\}^4"
        r"-1-\sqrt{\alpha\beta}-\sqrt{(1-\alpha)(1-\beta)})$.",
    ),
    rec(
        "RN-P3-C21-Entry09iii",
        r"If $\beta$ has degree $31$, then "
        r"$\displaystyle 5+4\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-124\sum_{k=1}^\infty\frac{kq^{62k}}{1-q^{62k}}$ "
        r"$\displaystyle =\varphi^2(q)\varphi^2(q^{31})\left(\tfrac12\{1+\sqrt{\alpha\beta}+\sqrt{(1-\alpha)(1-\beta)}\}\right."
        r"\left.\{1+(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}\}^2\right.$ "
        r"$\displaystyle\left.-2\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/8}"
        r"\{1+(\alpha\beta)^{1/8}+\{(1-\alpha)(1-\beta)\}^{1/8}\}\right)$.",
    ),
    rec(
        "RN-P3-C21-Entry10i",
        r"Let $\beta$ have degree $5$ with respect to $\alpha$. Then "
        r"$\displaystyle 1+6\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-30\sum_{k=1}^\infty\frac{kq^{10k}}{1-q^{10k}}$ "
        r"$\displaystyle =\varphi^2(q)\varphi^2(q^5)\left(\tfrac12\{1+\alpha\beta+(1-\alpha)(1-\beta)\}\right."
        r"\left.-16\{1-\sqrt{\alpha\beta}-\sqrt{(1-\alpha)(1-\beta)}\}^2\right)^{1/2}$.",
    ),
    rec(
        "RN-P3-C21-Entry10ii",
        r"If $\beta$ has degree $9$, then "
        r"$\displaystyle 1+3\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-27\sum_{k=1}^\infty\frac{kq^{18k}}{1-q^{18k}}$ "
        r"$\displaystyle =\varphi^2(q)\varphi^2(q^9)\left(\tfrac12\{1+\alpha\beta+(1-\alpha)(1-\beta)\}\right."
        r"\left.-\tfrac12\{1-\sqrt{\alpha\beta}-\sqrt{(1-\alpha)(1-\beta)}\}^2\right."
        r"\left.\tfrac{\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/2}}{21-(\alpha\beta)^{1/2}-\{(1-\alpha)(1-\beta)\}^{1/2}}\right)^{1/2}$.",
    ),
    rec(
        "RN-P3-C21-Entry10iii",
        r"If $\beta$ has degree $17$, then "
        r"$\displaystyle 2+3\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-51\sum_{k=1}^\infty\frac{kq^{34k}}{1-q^{34k}}$ "
        r"$\displaystyle =\varphi^2(q)\varphi^2(q^{17})\left(2\{1+\alpha\beta+(1-\alpha)(1-\beta)\}\right."
        r"\left.-\tfrac14\{1-\sqrt{\alpha\beta}-\sqrt{(1-\alpha)(1-\beta)}\}^2\right."
        r"\left.-\tfrac18\{1-\sqrt{\alpha\beta}-\sqrt{(1-\alpha)(1-\beta)}\}\right.$ "
        r"$\displaystyle\left.\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/16}"
        r"-3\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/3}\right)^{1/2}$.",
    ),
    rec(
        "RN-P3-C21-Entry11",
        r"If $\beta$ has degree $35$ over $\alpha$, then "
        r"$\displaystyle 17+12\sum_{k=1}^\infty\frac{kq^{2k}}{1-q^{2k}}"
        r"-420\sum_{k=1}^\infty\frac{kq^{70k}}{1-q^{70k}}$ "
        r"$\displaystyle =\varphi^2(q)\varphi^2(q^{35})\{(1-(\alpha\beta)^{1/4}-\{(1-\alpha)(1-\beta)\}^{1/4})^3"
        r"+2\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/12}$ "
        r"$\displaystyle +(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}"
        r"-\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/4}\}$.",
    ),
    rec(
        "RN-P3-C21-FinalEntry01",
        r"If the principal branch of each root is taken, then "
        r"$\displaystyle\frac{\varphi(q)-\varphi(-q)}{\varphi(q)+\varphi(-q)}"
        r"=\left(\frac{\varphi^2(q^2)-\varphi^2(-q^2)}{\varphi^2(q^2)+\varphi^2(-q^2)}\right)^{1/2}"
        r"=\left(\frac{\varphi^4(q^4)-\varphi^4(-q^4)}{\varphi^4(q^4)}\right)^{1/4}$.",
    ),
    rec(
        "RN-P3-C21-FinalEntry02",
        r"If the principal branch of each root is taken, then "
        r"$\{\varphi(q)+i\varphi(-q)\}^{1/2}=\{\varphi(q)+\varphi(q^2)\sqrt{i}\}^{1/2}"
        r"+\{\varphi(q)-\varphi(q^2)\sqrt{i}\}^{1/2}$.",
    ),
]
