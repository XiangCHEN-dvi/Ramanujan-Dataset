"""Part III, Chapter 19 entries — Modular equations degrees 3, 5, 7 (curated LaTeX)."""

from __future__ import annotations

TOPICS_C19 = ["modular-equations-degrees-3-5-7"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C19}


CHAPTER_19 = [
    rec(
        "RN-P3-C19-Entry01i",
        r"Let $\varphi$ and $\psi$ be defined as in Entry 22 of Chapter 16. Then $\displaystyle\frac{\psi(q)}{q^{1/8}\varphi(q)}=\frac{q}{-1}+\frac{q}{1+q}+\frac{q^2}{1+q^2}+\frac{q^3}{1+q^3}+\cdots$.",
    ),
    rec(
        "RN-P3-C19-Entry01ii",
        r"Recall that $f(a,b)$ is defined by (18.1) in Chapter 16. Let $\displaystyle v=\frac{q^{1/2}f(-q,-q^7)}{f(-q^3,-q^5)}$. Then $\displaystyle v=\frac{\psi(iq^{1/2})-\psi(-iq^{1/2})}{\psi(iq^{1/2})+\psi(-iq^{1/2})}$, $f(-q,-q^7)f(-q^3,-q^5)=\psi(-q)\psi(q^4)$, and $\displaystyle v=\frac{\varphi(q)-\varphi(q^2)}{2q^{1/2}\psi(q^4)}=\frac{P(-q^3,-q^5)}{2q^{1/2}\psi(q^4)}$.",
    ),
    rec(
        "RN-P3-C19-Entry02i",
        r"Recall that $f(-q)$ is defined in Entry 22 of Chapter 16. Then $f(-q,-q^4)f^3(-q^{15})=f(-q^5)f(-q^6,-q^9)f(-q,-q^{14})f(-q^4,-q^{11})$, and $f(-q^2,-q^3)f^3(-q^{15})=f(-q^5)f(-q^3,-q^{12})f(-q^2,-q^{13})f(-q^7,-q^8)$.",
    ),
    rec(
        "RN-P3-C19-Entry02ii",
        r"With $f(-q)$ as in Entry 2, $f(-q,-q^6)f^3(-q^{21})=f(-q^7)f(-q^6,-q^{15})f(-q,-q^{20})f(-q^8,-q^{12})$, $f(-q^2,-q^5)f^3(-q^{21})=f(-q^7)f(-q^9,-q^{12})f(-q^2,-q^{19})f(-q^5,-q^{16})$, and $f(-q^3,-q^4)f^3(-q^{21})=f(-q^7)f(-q^3,-q^{18})f(-q^4,-q^{17})f(-q^{10},-q^{11})$.",
    ),
    rec(
        "RN-P3-C19-Entry03i",
        r"$\displaystyle q\psi(q^2)\psi(q^6)=\frac{q}{-1}-\frac{q^5}{-1}+\frac{q^{10}}{1}+\frac{q^{14}}{-1}+\frac{q^{11}}{-1}+\cdots$.",
    ),
    rec(
        "RN-P3-C19-Entry03ii",
        r"$\displaystyle\varphi(q)\varphi(q^3)=1+2\left(\frac{q}{1-q}+\frac{q^2}{1+q^2}+\frac{q^4}{1+q^4}-\frac{q^5}{1-q^5}+\cdots\right)$.",
    ),
    rec(
        "RN-P3-C19-Entry03iii",
        r"$\displaystyle q\psi^2(q)\psi^2(q^3)=\frac{q}{-1}+\frac{2q^2}{-1}+\frac{3q^3}{-1}+\frac{4q^4}{-1}+\frac{5q^5}{1}+\frac{6q^6}{-1}+\cdots$.",
    ),
    rec(
        "RN-P3-C19-Entry03iv",
        r"$\displaystyle\varphi^2(q)\varphi^2(q^3)=1+4\left(\frac{q}{1-q}+\frac{q^4}{1-q}+\frac{q^5}{1-q}+\frac{q^7}{1-q}+\cdots\right)$, where the summation is over all $n$ which are neither a multiple of $3$ nor an odd multiple of $2$.",
    ),
    rec(
        "RN-P3-C19-Entry04i",
        r"$\displaystyle q^{1/2}\psi^5(q)\psi(q^3)-9q^2\psi(q)\psi^5(q^3)=\frac{q}{1-q^2}-\frac{2q^2}{1-q^4}-\frac{3q^3}{1-q^6}+\frac{4q^4}{1-q^8}+\frac{5q^6}{1-q^{12}}-\cdots$.",
    ),
    rec(
        "RN-P3-C19-Entry04ii",
        r"$\displaystyle\varphi(q)\varphi(q^3)\left\{\cot(\pi/6)-4\sum_{n=1}^\infty\frac{q^n\sin(n\pi/3)}{1+q^n}\right\}\left\{\csc^2(\pi/6)+8\sum_{n=1}^\infty\frac{nq^n\cos(n\pi/3)}{1+q^n}\right\}=\cot(\pi/6)\csc^2(\pi/6)-8\sum_{n=1}^\infty\frac{n^2q^n\sin(n\pi/3)}{1-q^n}$.",
    ),
    rec(
        "RN-P3-C19-Entry04iii",
        r"$\displaystyle\frac{\psi(q^2)j^2(-q)}{f(-q,q^5)}=1-3\sum_{n=0}^\infty\left(\frac{q^{6n+1}}{1+q^{6n+1}}-\frac{q^{6n+5}}{1+q^{6n+5}}\right)$.",
    ),
    rec(
        "RN-P3-C19-Entry04iv",
        r"$\displaystyle\frac{\varphi^2(q)f(q)}{f(-q,q^2)}=1-6\sum_{n=0}^\infty\left(\frac{q^{3n+1}}{1+q^{3n+1}}-\frac{q^{3n+2}}{1+q^{3n+2}}\right)$.",
    ),
    rec(
        "RN-P3-C19-Entry05i",
        r"Let $\beta$ be of degree $3$ in $\alpha$, and let $m$ be the corresponding multiplier. Then $\displaystyle\frac{(\alpha/\beta)^{1/3}-((1-\alpha)/(1-\beta))^{1/3}}{(\alpha\beta)^{1/3}-((1-\alpha)(1-\beta))^{1/3}}=1=\frac{((1-\alpha)(1-\beta))^{1/3}-(\alpha\beta)^{1/3}}{((1-\alpha)(1-\beta))^{1/3}+(\alpha\beta)^{1/3}}$.",
    ),
    rec(
        "RN-P3-C19-Entry05ii",
        r"$(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}=1$.",
    ),
    rec(
        "RN-P3-C19-Entry05iii",
        r"$\displaystyle\frac{((1-\alpha)^3)^{1/8}}{1-\alpha}+\frac{((1-\beta)^3)^{1/8}}{1-\beta}=\frac{3}{2m}$ and $\displaystyle\frac{(\alpha^3)^{1/8}}{\beta}+\frac{((1-\alpha)^3)^{1/8}}{1-\beta}=\frac{3}{2m}$.",
    ),
    rec(
        "RN-P3-C19-Entry05iv",
        r"$\displaystyle m^2\left(\frac{\alpha}{\beta}\right)^{1/2}=\left(\frac{\alpha^3}{\beta}\right)^{1/8}$ and $\displaystyle\frac{m^2}{4}=\left(\frac{\beta^3(1-\beta)^3}{\alpha(1-\alpha)}\right)^{1/8}$.",
    ),
    rec(
        "RN-P3-C19-Entry05v",
        r"If $\beta=\alpha$, then $\displaystyle m=\frac{1-2(\alpha\beta)^{1/4}}{1+4\alpha(1-\alpha)}=\frac{1-2(\alpha\beta)^{1/4}}{1+4\beta(1-\beta)}$, $\displaystyle m=\frac{(\alpha^3(1-\alpha)^3)^{1/8}}{2\beta(1-\beta)}=\left\{(\alpha^3(1-\alpha)^3)^{1/8}\right\}^{1/2}$, $\displaystyle m=\frac{(\beta^3(1-\beta)^3)^{1/8}}{2\alpha(1-\alpha)}=\left\{(\beta^3(1-\beta)^3)^{1/8}\right\}^{1/2}$, and $\displaystyle(\beta)^{1/4}=\frac{m^2+2m-3}{4m}$.",
    ),
    rec(
        "RN-P3-C19-Entry05vi",
        r"If $m=1+2p$ with $0<p<1$, then $\displaystyle\alpha=\frac{p(2+p)^3}{(1+2p)^3}$, $\beta=\frac{p^3(2+p)}{(1+2p)^3}$, $1-\alpha=\frac{(1+p)^3(1-p)}{(1+2p)^3}$, and $1-\beta=\frac{(1+p)(1-p)^3}{(1+2p)^3}$.",
    ),
    rec(
        "RN-P3-C19-Entry05vii",
        r"$\displaystyle m^2=\left(\frac{\alpha}{\beta}\right)^{1/2}+\left(\frac{1-\beta}{1-\alpha}\right)^{1/2}-\left(\frac{\beta(1-\beta)}{\alpha(1-\alpha)}\right)^{1/2}$ and $\displaystyle\frac{m^2}{\beta}=\left(\frac{\alpha}{\beta}\right)^{1/2}+\left(\frac{1-\alpha}{1-\beta}\right)^{1/2}-\left(\frac{\alpha(1-\alpha)}{\beta(1-\beta)}\right)^{1/2}$.",
    ),
    rec(
        "RN-P3-C19-Entry05viii",
        r"$\displaystyle\frac{(\alpha^5\beta)^{1/8}+\{(1-\alpha)^5(1-\beta)\}^{1/8}}{\alpha(1-\beta)}=1-\frac{(\beta^3(1-\alpha)^3)^{1/8}}{\alpha(1-\beta)}=\left\{1+(\alpha\beta)^{1/2}+\{(1-\alpha)(1-\beta)\}^{1/2}\right\}^{1/2}$.",
    ),
    rec(
        "RN-P3-C19-Entry05ix",
        r"$\displaystyle\{\alpha(1-\beta)\}^{1/2}+\{\beta(1-\alpha)\}^{1/2}=2\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/8}$.",
    ),
    rec(
        "RN-P3-C19-Entry05x",
        r"$\displaystyle m^2\{\alpha(1-\alpha)\}^{1/2}+\{\beta(1-\beta)\}^{1/2}=\frac{9}{2}\{\beta(1-\beta)\}^{1/2}+\frac{9}{2}\{\alpha(1-\alpha)\}^{1/2}$.",
    ),
    rec(
        "RN-P3-C19-Entry05xi",
        r"$\displaystyle\frac{m\alpha^{1/2}-\beta^{1/2}}{\beta^{1/2}}=\frac{m(1-\alpha)^{1/2}-(1-\beta)^{1/2}}{(1-\beta)^{1/2}}=2(\alpha\beta)^{1/8}$, $\displaystyle\frac{m+\beta}{\alpha}=\frac{m+(1-\beta)}{1-\alpha}=4\left(\{1+(\alpha\beta)^{1/2}+\{(1-\alpha)(1-\beta)\}^{1/2}\}^{1/2}\right)^{1/2}$.",
    ),
    rec(
        "RN-P3-C19-Entry05xii",
        r"If $P=\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/8}$ and $Q=\dfrac{\beta(1-\beta)}{\alpha(1-\alpha)}$, then $Q+\dfrac{1}{Q}+2\sqrt{2}\left(P-\dfrac{1}{P}\right)=0$.",
    ),
    rec(
        "RN-P3-C19-Entry05xiii",
        r"If $P=(\alpha\beta)^{1/8}$ and $Q=(\beta/\alpha)^{1/4}$, then $Q-\dfrac{1}{Q}=2\left(P-\dfrac{1}{P}\right)$.",
    ),
    rec(
        "RN-P3-C19-Entry05xiv",
        r"If $\alpha=\sin^2(\mu+\nu)$ and $\beta=\sin^2(\mu-\nu)$ with $\mu+\nu$ and $\mu-\nu$ positive acute angles, then $\sin(2\mu)=2\sin\nu$.",
    ),
    rec(
        "RN-P3-C19-Entry05xv",
        r"Let $p$ be defined by $m=1+2p$ with $0<p<1$, and let $q=p+p^2$. If $\alpha$ is the root $\displaystyle\alpha=\frac{(2+p)^3}{p(1+2p)^3}=\frac{\{-1+(4q+1)^{1/2}\}\{3+(4q+1)^{1/2}\}^3}{2(4q+1)^{1/2}}$, then $\displaystyle\beta(1-\beta)=q^3\frac{2-q}{1+4q}$.",
    ),
    rec(
        "RN-P3-C19-Entry06i",
        r"Let $p$ be defined by (5.4), so that $m=1+2p$. Then $\displaystyle{}_2F_1\!\left(\tfrac12,\tfrac12;1;\frac{p(2+p)^3}{(1+2p)^3}\right)=(1+2p)\,{}_2F_1\!\left(\tfrac12,\tfrac12;1;\frac{p^3(2+p)}{(1+2p)^3}\right)$.",
    ),
    rec(
        "RN-P3-C19-Entry06ii",
        r"Let $q=p+p^2$ with $p$ as in Entry 5(vi). If $q<\tfrac13(\sqrt{3}-5)$, then $\displaystyle{}_2F_1\!\left(\tfrac14,\tfrac34;1;\frac{4q(2-q)}{1+4q}\right)=(1+4q)^{1/2}\,{}_2F_1\!\left(\tfrac34,\tfrac14;1;\frac{4q^3(2-q)}{1+4q}\right)$.",
    ),
    rec(
        "RN-P3-C19-Entry06iii",
        r"If $\tan\tfrac12(A+B)=(1+p)\tan A$, then $\displaystyle\int_0^A\frac{d\varphi}{\sqrt{1-\alpha\sin^2\varphi}}=\frac{1+2p}{3}\int_0^B\frac{d\varphi}{\sqrt{1-\beta\sin^2\varphi}}$, where $\alpha$ and $\beta$ are given by Entry 5(vi). It is tacitly assumed that $0\le A,B,C\le\pi/2$.",
    ),
    rec(
        "RN-P3-C19-Entry06iv",
        r"If $\tan\tfrac12(A-B)=\dfrac{1-p}{1+2p}\tan B$, then $\displaystyle\frac{1+2p}{3}\int_0^B\frac{d\varphi}{\sqrt{1-\beta\sin^2\varphi}}=\int_0^2\frac{d\varphi}{\sqrt{1-\dfrac{p^3}{1-p}\sin^2\varphi}}$.",
    ),
    rec(
        "RN-P3-C19-Entry06v",
        r"If $\displaystyle\tan 2(C+B)=-\frac{2\tan B+2(1-x)\tan^3 B}{(1-x)\tan^4 B}$, then $\displaystyle\int_0^{\pi/2}\frac{d\varphi}{\sqrt{1-x\sin^2\varphi}}=3\int_0^{\pi/4}\frac{d\varphi}{\sqrt{1-x\sin^2\varphi}}$.",
    ),
    rec(
        "RN-P3-C19-Entry07iii",
        r"Let $AP$ denote the diameter of a circle with center $O$. Let $TB$ be perpendicular to $AP$, with $B$ on the circle and $T$ on $AP$. Draw chords $PR$ and $PR'$ equal in length to $TB$ with $R$ nearer to $B$. Form $AB$, $AR$, and $AR'$. Then a pendulum oscillating through $\angle BAR'$ takes $(AR-OT)/AO$ or $3AO/(AR+OT)$ times the time required to oscillate through $\angle BAR$.",
    ),
    rec(
        "RN-P3-C19-Entry07-Corollary",
        r"Suppose that $T$ coincides with $O$. Then $\angle BAR=\pi/12$, $\angle BAR'=\pi/12$, and $\dfrac{AR-OT}{AO}=\dfrac{3AO}{AR+OT}=\sqrt{3}$. Furthermore, a pendulum oscillating through $300^\circ$ takes $\sqrt{3}$ times the time required to oscillate through $60^\circ$.",
    ),
    rec(
        "RN-P3-C19-Entry07iv-FirstPart",
        r"Let $AP$ denote a diameter and $PQ$ a chord of a circle. Let $B$ denote the midpoint of the arc $PQ$. Draw $AB$ and $PB$. Let $B'$ be the mirror image of $B$ in $AP$ and construct $AB'$ and $PB'$. Let $R$ be a point on the circle such that $PR=\tfrac12 PQ$ and $R$ is on the same side of $AP$ as $B$ and $Q$. Let $R'$ be the image of $R$ in $AP$. Form $PR$, $PR'$, $QR$, and $QR'$. Draw $AR$ and $AR'$, cutting $PB$ and $PB'$ at $C$ and $C'$, respectively. Construct a line perpendicular to $AP$ at $P$. Let the extensions of $AB$ and $AB'$ meet this line at $M$ and $M'$, respectively. Extend $BP$ and $AR'$ to their point of intersection $C_2$, and extend $B'P$ and $AR$ to their point of intersection $C_3$. Then a circle passes through $M$, $C$, $C'$, $M'$, $C_2$, and $C_3$, and this circle is orthogonal to the original circle. Furthermore, it is tangent to the lines $AB$ and $AB'$ at $M$ and $M'$, respectively. Let $O$ denote the center of this circle and form $OM$ and $OM'$. The circle also passes through the intersections of the circles with centers $A$ and $P$ and radii $AB$ and $PR$, respectively. The distances of any point on the circumference of this circle from $A$ and $P$ bear a constant ratio. Lastly, $QR\cdot QR'=3RP^2$.",
    ),
    rec(
        "RN-P3-C19-Entry07iv-SecondPart",
        r"With the notation of Entry 7(iv) (First Part), a pendulum oscillating through the angle $4\angle BAR'$ takes $QR/RP$ or $3R'P/R'Q$ times the time required to oscillate through the angle $4\angle BAR$.",
    ),
    rec(
        "RN-P3-C19-Entry07iv-ThirdPart",
        r"With the notation of Entry 7(iv) (First Part) and Entry 5(xiv), $\alpha^{1/2}=\dfrac{BP}{AP}$, $\beta^{1/2}=\dfrac{AC_2}{AP}$, $(1-\alpha)^{1/2}=\dfrac{AC}{AP}$, $(1-\beta)^{1/2}=\dfrac{PC_2}{AP}$, $\displaystyle\frac{(\alpha\beta)^{1/8}}{AC_1/AC_3}=\frac{(BM)^{1/2}}{AM}=\frac{BP}{AP}$, $\{(1-\alpha)(1-\beta)\}^{1/8}=\dfrac{AB}{AP}$, $\dfrac{QR}{RP}=\dfrac{3}{m}=\dfrac{QR'}{R'P}$, $(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}=\dfrac{BM+AB}{AM}=1$, $\displaystyle\frac{(\alpha^3)^{1/8}}{AC_2/AP}-\frac{((1-\alpha)^3)^{1/8}}{PC_2/AP}=\frac{(\alpha\beta)^{1/8}}{\{(1-\alpha)(1-\beta)\}^{1/8}}=1$, and $\displaystyle\frac{((1-\beta)^3)^{1/8}}{AC/AP}-\frac{(\beta^3)^{1/8}}{PC_2/AP}=\frac{\{(1-\alpha)(1-\beta)\}^{1/8}}{(\alpha\beta)^{1/8}}=1$.",
    ),
    rec(
        "RN-P3-C19-Entry08i",
        r"$\displaystyle\frac{q\psi(q)\psi(q^5)-5q^2\psi(q)\psi^3(q^5)}{q^{1/2}f(q)f(q^5)}=\frac{q}{1-q^2}-\frac{2q^2}{1-q^4}-\frac{3q^3}{1-q^6}+\frac{4q^4}{1-q^8}+\frac{5q^6}{1-q^{12}}-\cdots$.",
    ),
    rec(
        "RN-P3-C19-Entry08ii",
        r"$\displaystyle\frac{5\varphi(q)\varphi(q^5)-\varphi(q^3)\varphi(q^{15})}{4}=1+\frac{q}{1+q}-\frac{q^2}{1-q^2}-\frac{q^3}{1+q^3}+\frac{q^4}{1-q^4}+\frac{q^6}{1-q^6}-\cdots$.",
    ),
    rec(
        "RN-P3-C19-Entry08iii",
        r"$\displaystyle\frac{\psi^5(q)}{\psi(q^5)}-\frac{\varphi^5(q)}{\varphi(q^5)}=\frac{\varphi(q)\varphi^3(q^5)}{25}(25-m^2)$, where $m$ is the degree-$5$ multiplier connecting $\alpha$ and $\beta$.",
    ),
    rec(
        "RN-P3-C19-Entry08iv",
        r"$\displaystyle\frac{\varphi^5(q)}{\varphi(q^5)}-100q^2\frac{\psi(-q)\psi^3(-q^5)}{\psi^4(-q^5)}=1+5\left(\frac{q}{1+q}-\frac{q^2}{1+q^2}-\frac{q^3}{1+q^3}+\frac{q^4}{1+q^4}+\frac{q^6}{1+q^6}-\cdots\right)$.",
    ),
    rec(
        "RN-P3-C19-Entry09i",
        r"$\displaystyle\frac{f^5(-q)}{f(-q^5)}=1-5\left(\frac{q}{1+q}-\frac{q^3}{1+q^3}+\frac{q^4}{1+q^4}-\frac{q^7}{1+q^7}+\frac{q^9}{1+q^9}+\frac{q^{11}}{1+q^{11}}-\frac{q^{12}}{1+q^{12}}-\cdots\right)$, where the powers of $q$ are not multiples of $5$ but are otherwise all odd multiples of $2^{2k}$, $k\ge 0$, and the signs are $+,-,-,+$ according as the power of $q$ is congruent to $1,2,3,4\pmod 5$, respectively.",
    ),
    rec(
        "RN-P3-C19-Entry09ii",
        r"$\displaystyle\frac{4f^5(q^5)}{f(q)}+\frac{\varphi^5(q^5)}{\varphi(q)}=\frac{\varphi^3(q)}{\varphi(q^5)}$.",
    ),
    rec(
        "RN-P3-C19-Entry09iii",
        r"$\displaystyle\varphi^2(q)-\varphi^2(q^5)=4qf(q,q^9)f(q^3,q^7)$.",
    ),
    rec(
        "RN-P3-C19-Entry09iv",
        r"$\displaystyle\varphi^2(q^{1/5})=\{\varphi(q^5)+2q^{1/5}f(q^3,q^7)\}^2+\{\varphi(q^5)+2q^{4/5}f(q,q^9)\}^2-\varphi^2(q^5)-8qf(q^3,q^7)f(q,q^9)$.",
    ),
    rec(
        "RN-P3-C19-Entry09v",
        r"$\displaystyle q\frac{d}{dq}\log\frac{f(-q^2,-q^3)}{f(-q,-q^4)}=\frac{q}{1+q}-\frac{q^3}{1+q^3}+\frac{q^4}{1+q^4}-\frac{q^7}{1+q^7}+\frac{q^9}{1+q^9}+\cdots$, where the powers of $q$ are odd multiples of $2^{2k}$, $k\ge 0$, with a plus sign when $n\equiv 1,4\pmod 5$ and a minus sign when $n\equiv 2,3\pmod 5$.",
    ),
    rec(
        "RN-P3-C19-Entry09vi",
        r"$\displaystyle 1+\frac{25q^2\psi(q)\psi^3(q^5)}{\psi^5(q)}-\frac{\varphi^5(q)}{\varphi(q^5)}=\frac{\varphi^5(q)}{\varphi(q^5)}-100q^2\frac{\psi(-q)\psi^3(-q^5)}{\psi^4(-q^5)}$.",
    ),
    rec(
        "RN-P3-C19-Entry09vii",
        r"$f(q,q^4)f(q^2,q^3)=\dfrac{\chi(-q^5)f^2(-q^5)}{\chi(-q)}=\dfrac{\varphi(-q^5)f(-q^5)}{\chi(-q)}$, and $f(q,q^9)f(q^3,q^7)=\chi(q)(q^{20};q^{20})_\infty(q^5;q^5)_\infty$.",
    ),
    rec(
        "RN-P3-C19-Entry10i",
        r"$\displaystyle\psi(q^{1/5})-q^{3/5}\psi(q^5)=f(q^2,q^3)+q^{1/5}f(q,q^4)$.",
    ),
    rec(
        "RN-P3-C19-Entry10ii",
        r"$\displaystyle\varphi(q^{1/5})-\varphi(q^5)=2q^{1/5}f(q^3,q^7)+2q^{4/5}f(q,q^9)$.",
    ),
    rec(
        "RN-P3-C19-Entry10iii",
        r"$f(-q)\{f(-q^{1/5})+q^{1/5}f(-q^5)\}=P(-q^2,-q^3)-q^{2/5}P(-q,-q^4)$.",
    ),
    rec(
        "RN-P3-C19-Entry10iv",
        r"$\displaystyle\varphi^2(q)-\varphi^2(q^5)=4qf(q,q^9)f(q^3,q^7)$.",
    ),
    rec(
        "RN-P3-C19-Entry10v",
        r"$\displaystyle\psi^2(q)-q\psi^2(q^5)=f(q,q^4)f(q^2,q^3)$.",
    ),
    rec(
        "RN-P3-C19-Entry10vi",
        r"$\displaystyle f^5(q^2,q^3)+qf^5(q,q^4)=\left(\frac{\psi(q)}{\psi(q^5)}-q^{3/5}\right)\{\psi^4(q)-4q\psi^2(q)\psi^2(q^5)+11q^2\psi^4(q^5)\}$.",
    ),
    rec(
        "RN-P3-C19-Entry10vii",
        r"$\displaystyle 32qf^5(q^3,q^7)+32q^4f^5(q,q^9)=\left(\frac{\varphi(q)}{\varphi(q^5)}-q^{1/5}\right)\{\varphi^4(q)-4\varphi^2(q)\varphi^2(q^5)+11\varphi^4(q^5)\}$.",
    ),
    rec(
        "RN-P3-C19-Entry10viii",
        r"$\displaystyle\frac{f^5(-q)}{f(-q^5)}\prod_{\zeta^5=1}f(-\zeta q^{1/5})=f^{10}(-q^2,-q^3)-q^2f^{10}(-q,-q^4)-qf^6(-q)f^6(-q^5)-5qf^3(-q)f^3(-q^5)P(-q,-q^4)P(-q^2,-q^3)-5f(-q)f(-q^5)f^4(-q,-q^4)f^4(-q^2,-q^3)$.",
    ),
    rec(
        "RN-P3-C19-Entry11i",
        r"There exist positive functions $\mu$ and $\nu$ such that $\displaystyle\varphi(q^{1/5})=\varphi(q^5)+\mu^{1/5}+\nu^{1/5}$, where $\displaystyle\mu+\nu=\frac{\varphi^2(q)-\varphi^2(q^5)}{\varphi(q^5)}\{\varphi^4(q)-4\varphi^2(q)\varphi^2(q^5)+11\varphi^4(q^5)\}$, $\displaystyle\mu-\nu=\frac{\varphi^2(q)-\varphi^2(q^5)}{\varphi(q^5)}\{5\varphi^2(q^5)-\varphi^2(q)\}\{\varphi^4(q)-2\varphi^2(q)\varphi^2(q^5)+5\varphi^4(q^5)\}^{1/2}$, and $(\mu\nu)^{1/5}=\varphi^2(q)-\varphi^2(q^5)$.",
    ),
    rec(
        "RN-P3-C19-Entry11ii",
        r"There are positive functions $\mu$ and $\nu$ satisfying $\displaystyle q^{1/40}\psi(q^{1/5})=q^{5/8}\psi(q^5)+\mu^{1/5}+\nu^{1/5}$, with analogous formulas for $\mu+\nu$, $\mu-\nu$, and $(\mu\nu)^{1/5}$ obtained from Entry 10(vi), (v), and (vii), respectively.",
    ),
    rec(
        "RN-P3-C19-Entry11iii",
        r"If $\displaystyle\frac{q^{1/5}f(-q,-q^4)}{f(-q^2,-q^3)}=\frac{q}{-1}+\frac{q}{1+q}+\frac{q^2}{1+q^2}+\frac{q^3}{1+q^3}+\frac{q^4}{1+q^4}+\cdots$, then $(\mu^2+1)^{1/2}-\mu^{1/5}=(\nu^2+1)^{1/2}-\nu^{1/5}=\dfrac{q^{1/5}f(-q,-q^4)}{f(-q^2,-q^3)}$.",
    ),
    rec(
        "RN-P3-C19-Entry11iv",
        r"For certain positive functions $\mu$ and $\nu$, $\displaystyle\frac{f(-q^{1/5})}{q^{1/5}f(-q^5)}=\left(\frac{\mu^{1/5}}{\nu^{1/5}}+\frac{\nu^{1/5}}{\mu^{1/5}}-5\right)^{1/3}$, where $(\mu\nu)^{1/5}=\dfrac{25f^6(-q)+3qf^6(-q^5)}{qf^6(-q^5)}$ and $\displaystyle\nu-\mu=\dfrac{f^{18}(-q^5)}{11+15^2Q\dfrac{f^6(-Q)}{f^6(-Q^5)}+5\cdot15^2Q^2\dfrac{f^{12}(-Q)}{f^{12}(-Q^5)}-25^2Q^3\dfrac{f^8(-Q)}{f^8(-Q^5)}}$ with $Q=q^5$.",
    ),
    rec(
        "RN-P3-C19-Entry12i",
        r"There are positive functions $\mu$ and $\nu$ such that $\displaystyle 1+\frac{5Qf(-Q^{25})}{f(-Q)}=\frac{\mu^{1/5}}{\nu^{1/5}}$, where $\mu\nu=1$ and $\displaystyle\mu+\nu=\frac{f^{10}(-Q^2,-Q^3)}{Qf^{10}(-Q,-Q^4)}-\frac{f^{10}(-Q^2,-Q^3)}{f^{10}(-Q,-Q^4)}-11$.",
    ),
    rec(
        "RN-P3-C19-Entry12ii",
        r"For certain positive functions $\mu$ and $\nu$, $\displaystyle\frac{f(-Q^{25})}{Qf(-Q)}=\left(1+\frac{\mu^{1/5}}{\nu^{1/5}}-5\right)^{1/3}$, with $(\mu\nu)^{1/5}=\dfrac{1+15Qf^6(-Q^5)}{25qf^6(-Q)}$ and the formula for $\nu-\mu$ given in Entry 11(iv).",
    ),
    rec(
        "RN-P3-C19-Entry12iii",
        r"There exist positive functions $\mu$ and $\nu$ such that $\displaystyle\frac{5\varphi(Q^{25})}{\varphi(Q)}=1+\frac{\mu^{1/5}}{\nu^{1/5}}$, with $(\mu\nu)^{1/5}=\dfrac{5\varphi^2(Q^5)}{\varphi^2(Q)}-1$ and $\displaystyle\mu+\nu=\frac{\varphi^2(Q)-\varphi^2(Q^5)}{\varphi^2(Q^5)}\{\varphi^4(Q)-4\varphi^2(Q)\varphi^2(Q^5)+11\varphi^4(Q^5)\}$.",
    ),
    rec(
        "RN-P3-C19-Entry12iv",
        r"For certain positive functions $\mu$ and $\nu$, $\displaystyle\frac{5Q^3\psi(Q^{25})}{\psi(Q)}=1-\frac{\mu^{1/5}}{\nu^{1/5}}$, where $(\mu\nu)^{1/5}=1-\dfrac{5Q\psi^2(Q^5)}{\psi^2(Q)}$ and $\displaystyle\mu-\nu=(1-\dfrac{5\varphi^2(Q^5)}{\varphi^2(Q)})(11-20\dfrac{\varphi^2(Q^5)}{\varphi^2(Q)}+25\dfrac{\varphi^4(Q^5)}{\varphi^4(Q)})$.",
    ),
    rec(
        "RN-P3-C19-Entry12v",
        r"$\displaystyle\frac{f(-q^{1/5})}{f(-q^5)}=q^{1/5}\frac{f(-q^2,-q^3)}{f(-q,-q^4)}-q^{3/5}\frac{f(-q,-q^4)}{f(-q^2,-q^3)}$.",
    ),
    rec(
        "RN-P3-C19-Entry13i",
        r"$(\alpha\beta)^{1/2}+\{(1-\alpha)(1-\beta)\}^{1/2}+2\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/6}=1$.",
    ),
    rec(
        "RN-P3-C19-Entry13ii",
        r"$\displaystyle\frac{(\alpha^5)^{1/8}}{\beta}-\frac{((1-\alpha)^5)^{1/8}}{1-\beta}=\frac{1+2^{1/3}}{2}\left\{\frac{\alpha^5(1-\alpha)^5}{\beta(1-\beta)}\right\}^{1/24}$.",
    ),
    rec(
        "RN-P3-C19-Entry13iii",
        r"$\displaystyle\frac{((1-\beta)^5)^{1/8}}{1-\alpha}-\frac{(\beta^5)^{1/8}}{\alpha}=\frac{1+2^{1/3}}{2}\left\{\frac{\beta^5(1-\beta)^5}{\alpha(1-\alpha)}\right\}^{1/24}$.",
    ),
    rec(
        "RN-P3-C19-Entry13iv",
        r"$\displaystyle m=1+2^{4/3}\left\{\frac{\beta^5(1-\beta)^5}{\alpha(1-\alpha)}\right\}^{1/24}$ and $\displaystyle\frac{5}{m}=1+2^{1/3}\left\{\frac{\alpha^5(1-\alpha)^5}{\beta(1-\beta)}\right\}^{1/24}$.",
    ),
    rec(
        "RN-P3-C19-Entry13v",
        r"$\displaystyle m=\frac{1+\{((1-\beta)^5/(1-\alpha))^{1/8}\}}{1+\{((1-\alpha)^3(1-\beta))^{1/8}\}}=1-\frac{(\beta^5/\alpha)^{1/8}}{1-(\alpha^3\beta)^{1/8}}$ and $\displaystyle\frac{m^2}{m-1}=\frac{(\alpha/\beta)^{1/8}}{1-(\alpha^3\beta)^{1/8}}$.",
    ),
    rec(
        "RN-P3-C19-Entry13vi",
        r"$\displaystyle\frac{5}{m}=\frac{1+(\alpha^5/\beta)^{1/8}}{1+(\alpha\beta^3)^{1/8}}=1-\frac{((1-\alpha)^5/(1-\beta))^{1/8}}{1-\{((1-\alpha)(1-\beta)^3)^{1/8}\}$.",
    ),
    rec(
        "RN-P3-C19-Entry13vii",
        r"$(\alpha\beta^3)^{1/8}+\{((1-\alpha)(1-\beta)^3)\}^{1/8}=(\alpha^3\beta)^{1/8}+\{((1-\alpha)^3(1-\beta))\}^{1/8}=1-2^{1/3}\left\{\frac{\beta^5(1-\alpha)^5}{\alpha(1-\beta)}\right\}^{1/24}=\left\{\dfrac{1+(\alpha\beta)^{1/2}+\{((1-\alpha)(1-\beta))\}^{1/2}}{2}\right\}^{1/2}$.",
    ),
    rec(
        "RN-P3-C19-Entry13viii",
        r"If $\alpha$ and $\beta$ are arbitrary complex numbers, then $\displaystyle m=1-3\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/6}+\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/3}$ and $\displaystyle m(1-3\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/6}+\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/3})^{1/2}=\tfrac12(5-m^2)$.",
    ),
    rec(
        "RN-P3-C19-Entry13ix",
        r"$\displaystyle 1+\frac{4^{1/3}\{\beta^5(1-\beta)^5\}^{1/12}}{\alpha(1-\alpha)}=\frac{m}{2}\{1+(\alpha\beta)^{1/2}+\{((1-\alpha)(1-\beta))\}^{1/2}\}$ and $\displaystyle 1+\frac{4^{1/3}\{\alpha^5(1-\alpha)^5\}^{1/12}}{\beta(1-\beta)}=\frac{5}{2m}\{1+(\alpha\beta)^{1/2}+\{((1-\alpha)(1-\beta))\}^{1/2}\}$.",
    ),
    rec(
        "RN-P3-C19-Entry13x",
        r"$\displaystyle\{\alpha(1-\beta)\}^{1/4}+\{\beta(1-\alpha)\}^{1/4}=4^{1/3}\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/24}=m\{\alpha(1-\alpha)\}^{1/4}+\{\beta(1-\beta)\}^{1/4}=\{\alpha(1-\alpha)\}^{1/4}+\dfrac{5}{m}\{\beta(1-\beta)\}^{1/4}$.",
    ),
    rec(
        "RN-P3-C19-Entry13xi",
        r"$\displaystyle\frac{((1-\beta)^5)^{1/8}}{1-\alpha}+\frac{(\beta^5)^{1/8}}{\alpha}=\frac{m}{2}\left\{1+(\alpha\beta)^{1/2}+\{((1-\alpha)(1-\beta))\}^{1/2}\right\}^{1/2}$ and $\displaystyle\frac{(\alpha^5)^{1/8}}{\beta}+\frac{((1-\alpha)^5)^{1/8}}{1-\beta}=\frac{5}{2m}\left\{1+(\alpha\beta)^{1/2}+\{((1-\alpha)(1-\beta))\}^{1/2}\right\}^{1/2}$.",
    ),
    rec(
        "RN-P3-C19-Entry13xii",
        r"$\displaystyle m=\left(\frac{\beta}{\alpha}\right)^{1/4}+\left(\frac{1-\beta}{1-\alpha}\right)^{1/4}-\left(\frac{\beta(1-\beta)}{\alpha(1-\alpha)}\right)^{1/4}$ and $\displaystyle\frac{5}{m}=\left(\frac{\alpha}{\beta}\right)^{1/4}+\left(\frac{1-\alpha}{1-\beta}\right)^{1/4}-\left(\frac{\alpha(1-\alpha)}{\beta(1-\beta)}\right)^{1/4}$.",
    ),
    rec(
        "RN-P3-C19-Entry13xiii",
        r"$\displaystyle\frac{m-5}{m}=\frac{4\{(\alpha\beta)^{1/2}-\{((1-\alpha)(1-\beta))\}^{1/2}\}}{\{1+(\alpha\beta)^{1/2}+\{((1-\alpha)(1-\beta))\}^{1/2}/2\}^{1/2}}$ and $\displaystyle m+\frac{5}{m}=2\{2+(\alpha\beta)^{1/2}+\{((1-\alpha)(1-\beta))\}^{1/2}\}$.",
    ),
    rec(
        "RN-P3-C19-Entry13xiv",
        r"If $P=\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/12}$ and $Q=\left(\dfrac{\beta(1-\beta)}{\alpha(1-\alpha)}\right)^{1/8}$, then $Q+\dfrac{1}{Q}+2\left(P-\dfrac{1}{P}\right)=0$.",
    ),
    rec(
        "RN-P3-C19-Entry13xv",
        r"If $P=(\alpha\beta)^{1/4}$ and $Q=(\beta/\alpha)^{1/8}$, then $(1-PQ^3)(1+P/Q^3)=5(1+PQ)(1-P/Q)$.",
    ),
    rec(
        "RN-P3-C19-Entry14i",
        r"Let $\beta$ be of the fifth degree in $\alpha$. If $\alpha=\sin^2(\mu+\nu)$ and $\beta=\sin^2(\mu-\nu)$, then $\sin(2\mu)=\sin\nu(1+\cos^2\nu)$.",
    ),
    rec(
        "RN-P3-C19-Entry14ii",
        r"If $\beta$ is defined by $m=1+2p$ and $0<p<\tfrac12(5\sqrt{5}-11)$, then $\displaystyle 4\alpha(1-\alpha)=\frac{p^5(2-p)}{(1+2p)^5}$ and $\displaystyle 4\beta(1-\beta)=\frac{p^5(2-p)}{(1+2p)^5}\cdot\frac{2-p}{p}$.",
    ),
    rec(
        "RN-P3-C19-Entry14iii",
        r"If $p$ is defined by (14.1) and $0<p<2$, then $\displaystyle 1-2\alpha=\frac{1-11p-p^2(1+p^2)^{1/2}}{(1+2p)^2(1+2p)}$ and $\displaystyle 1-2\beta=\frac{(1+p-p^2)(1+p^2)^{1/2}}{(1+2p)^2(1+2p)}$.",
    ),
    rec(
        "RN-P3-C19-Entry14iv",
        r"If $\alpha$ and $\beta$ are given by the equalities immediately above, then $\displaystyle{}_2F_1\!\left(\tfrac14,\tfrac14;1;\alpha\right)=(1+2p)\,{}_2F_1\!\left(\tfrac14,\tfrac14;1;\beta\right)$.",
    ),
    rec(
        "RN-P3-C19-Entry14v",
        r"If $0<p<\tfrac12(5\sqrt{5}-11)$, then $\displaystyle{}_2F_1\!\left(\tfrac14,\tfrac14;1;p(2-p)\right)=(1+2p)\,{}_2F_1\!\left(\tfrac14,\tfrac14;1;p^5(2-p)\right)$.",
    ),
    rec(
        "RN-P3-C19-Entry15i",
        r"Let $\beta$ be of the fifth degree in $\alpha$ and $\gamma$ of the fifth degree in $\beta$, so that $\gamma$ is of the twenty-fifth degree in $\alpha$. Let $m$ and $m'$ denote the multipliers for $(\alpha,\beta)$ and $(\beta,\gamma)$, respectively. Then $\displaystyle\frac{(\gamma)^{1/8}}{1-\gamma}+\frac{(1-\gamma)^{1/8}}{\gamma}-\frac{(\gamma(1-\gamma))^{1/8}}{\gamma(1-\gamma)}-\frac{2(\gamma(1-\gamma))^{1/12}}{\alpha(1-\alpha)}=(mm')^{1/2}$.",
    ),
    rec(
        "RN-P3-C19-Entry15ii",
        r"With notation as in Entry 15(i), $\displaystyle\frac{(\alpha)^{1/8}}{1-\alpha}+\frac{(1-\alpha)^{1/8}}{\alpha}-\frac{(\alpha(1-\alpha))^{1/8}}{\alpha(1-\alpha)}-\frac{2(\alpha(1-\alpha))^{1/12}}{\gamma(1-\gamma)}=(mm')^{1/2}$.",
    ),
    rec(
        "RN-P3-C19-Entry15iii",
        r"With notation as in Entry 15(i), $\displaystyle\frac{(\alpha\gamma)^{1/8}}{(\beta^2)^{1/4}}+\frac{((1-\alpha)(1-\gamma))^{1/8}}{((1-\beta)^2)^{1/4}}+\frac{(\alpha\gamma(1-\alpha)(1-\gamma))^{1/8}}{\beta^2(1-\beta)^2}=\left(\frac{m'}{m}\right)^{1/2}$.",
    ),
    rec(
        "RN-P3-C19-Entry15iv",
        r"With notation as in Entry 15(i), $\displaystyle\frac{(\beta^2)^{1/4}}{\alpha\gamma}+\frac{((1-\beta)^2)^{1/4}}{(1-\alpha)(1-\gamma)}+\frac{(\beta^2(1-\beta)^2)^{1/4}}{\alpha\gamma(1-\alpha)(1-\gamma)}=5\left(\frac{m'}{m}\right)^{1/2}$.",
    ),
    rec(
        "RN-P3-C19-Entry15v",
        r"With notation as in Entry 15(i), $\displaystyle\frac{(\beta^2(1-\beta)^2)^{1/8}}{\alpha\gamma(1-\alpha)(1-\gamma)}-\frac{2}{1+\alpha\gamma+(1-\alpha)(1-\gamma)}\left\{(\beta^2)^{1/8}+\left(\frac{(1-\beta)^2}{(1-\alpha)(1-\gamma)}\right)^{1/8}\right\}=\frac{5}{m}+\frac{m'}{m}\left\{1+4^{1/3}\left(\frac{\beta^{10}(1-\beta)^{10}}{\alpha\gamma(1-\alpha)(1-\gamma)}\right)^{1/24}\right\}$.",
    ),
    rec(
        "RN-P3-C19-Entry16i",
        r"Let $\beta$ be of the fifth degree in $\alpha$. If $\displaystyle\int_0^A\frac{d\varphi}{\sqrt{1-\alpha\sin^2\varphi}}=m\int_0^B\frac{d\varphi}{\sqrt{1-\beta\sin^2\varphi}}$ for some pair $A,B$ with $0\le A,B\le\pi/2$, then $\displaystyle m=1+\frac{p\tan B}{\tanh(A-B)\{1+\tfrac12(1+p+\{((1+2p)(1+p^2))^{1/2}\})\tan^2 B\}}$, where $m=2p+1$ as in (14.1).",
    ),
    rec(
        "RN-P3-C19-Entry16ii",
        r"Let $t_1$ and $t_2$ denote the times required for a pendulum of length $\ell$ to oscillate through the angles $4\angle BAR'$ and $4\angle BAR$, respectively. Then $t_1=mt_2$, where $m$ is the multiplier of degree $5$. Furthermore, $\displaystyle 1+\frac{1}{m}=\frac{2QR_1}{RT}$ and $\displaystyle 1+\frac{m}{5}=\frac{2QR}{RT}$, where $R$, $R_1$, $Q$, and $T$ are defined in the geometric configuration of Entry 16.",
    ),
    rec(
        "RN-P3-C19-Entry16-Examplei",
        r"If $AP=1$, then $TP=2\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/6}$, $DT=2(\alpha\beta)^{1/2}$, $OD+OT=2\{((1-\alpha)(1-\beta))\}^{1/2}$, and $(\alpha\beta)^{1/2}+\{((1-\alpha)(1-\beta))\}^{1/2}+2\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/6}=1$.",
    ),
    rec(
        "RN-P3-C19-Entry16-Exampleii",
        r"Let $Q=A$. Then $D=0$, $m=\sqrt{5}$, and $T$ divides $AP$ in medial section, that is, $T$ is the golden section point of $AP$.",
    ),
    rec(
        "RN-P3-C19-Entry17i",
        r"$\displaystyle q\psi(q)\psi(q^7)=\frac{q}{-1}-\frac{q^3}{-1}-\frac{q^5}{-1}+\frac{q^9}{-1}+\frac{q^{11}}{1}+\cdots$, where the cycle of coefficients is of length $14$.",
    ),
    rec(
        "RN-P3-C19-Entry17ii",
        r"$\displaystyle\varphi(q)\varphi(q^7)=1+2\left(\frac{q}{1-q}+\frac{q^2}{1-q}+\frac{q^3}{1-q}+\frac{q^4}{1-q}-\frac{q^5}{1-q}+\frac{q^6}{1-q}+\frac{q^8}{1-q}+\cdots\right)$, where the cycle of coefficients is of length $28$.",
    ),
    rec(
        "RN-P3-C19-Entry17iii",
        r"$\displaystyle\varphi(q^{1/7})-\varphi(q^7)=2q^{1/7}f(q^5,q^9)+2q^{4/7}f(q^3,q^{11})+2q^{9/7}f(q,q^{13})$.",
    ),
    rec(
        "RN-P3-C19-Entry17iv",
        r"$\displaystyle\psi(q^{1/7})-q^{6/7}\psi(q^7)=f(q^3,q^4)+q^{1/7}f(q^2,q^5)+q^{3/7}f(q,q^6)$.",
    ),
    rec(
        "RN-P3-C19-Entry17v",
        r"$\displaystyle\frac{f(-q^{1/7})}{q^{2/7}f(-q^7)}=\frac{f(-q^2,-q^5)}{f(-q^6,-q)}-q^{1/7}\frac{f(-q^3,-q^4)}{f(-q^5,-q^2)}+q^{5/7}\frac{f(-q,-q^6)}{f(-q^4,-q^3)}$.",
    ),
    rec(
        "RN-P3-C19-Entry18i",
        r"There are positive functions $u$, $v$, and $w$ such that $\displaystyle 1+\frac{f(-q^{1/7})}{q^{2/7}f(-q^7)}=\frac{u^{1/7}}{v^{1/7}}+\frac{v^{1/7}}{w^{1/7}}+\frac{w^{1/7}}{u^{1/7}}$, where $uvw=1$.",
    ),
    rec(
        "RN-P3-C19-Entry18ii",
        r"There are positive functions $u_1$, $v_1$, and $w_1$ such that $\displaystyle 1+\frac{7q^2f(-q^{49})}{f(-q)}=\frac{u_1^{1/7}}{v_1^{1/7}}+\frac{v_1^{1/7}}{w_1^{1/7}}+\frac{w_1^{1/7}}{u_1^{1/7}}$, where $u_1v_1w_1=1$.",
    ),
    rec(
        "RN-P3-C19-Entry18iii",
        r"$\displaystyle\frac{P(-q^7)}{\chi(-q)}=\dfrac{f(q,q^6)f(q^2,q^5)f(q^3,q^4)}{\varphi(-q^7)}$.",
    ),
    rec(
        "RN-P3-C19-Entry18iv",
        r"$f(-q,-q^6)f(-q^2,-q^5)f(-q^3,-q^4)=f(-q)f^2(-q^7)$.",
    ),
    rec(
        "RN-P3-C19-Entry18v",
        r"$f(q,q^{13})f(q^3,q^{11})f(q^5,q^9)=\chi(q)/\{f(-q^7)P(-q^{14})\}$.",
    ),
    rec(
        "RN-P3-C19-Entry18vi",
        r"If $u$, $v$, and $w$ are defined by Entry 18(i), then $\displaystyle\frac{2q^{2/7}f(-q^7)}{f(-q^{1/7})}=7(v^3+5v^2+7v)+(v^2+7v+7)(4v^3+21v^2+28v)^{1/2}$.",
    ),
    rec(
        "RN-P3-C19-Entry19i",
        r"If $\beta$ is of the seventh degree in $\alpha$ and $m$ is the multiplier for degree $7$, then $\{((1-\alpha)(1-\beta))\}^{1/8}-\{((1-\alpha)(1-\beta))\}^{1/4}=\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/8}$ and $(\alpha\beta)^{1/4}+\{((1-\alpha)(1-\beta))\}^{1/4}=1-2\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/8}$.",
    ),
    rec(
        "RN-P3-C19-Entry19ii",
        r"With notation as in Entry 19(i), if $t=\{((1-\alpha)(1-\beta))\}^{1/8}$, then $\displaystyle\frac{(\beta(1-\beta))^{1/3}}{(1-2t)m}=1-4t(1-t)$ and $\displaystyle\frac{(\beta^7(1-\beta)^7)^{1/24}}{\alpha(1-\alpha)}=\frac{1-4t^8(1-t)^8}{(1-t)-t}$.",
    ),
    rec(
        "RN-P3-C19-Entry19iii",
        r"$\displaystyle\frac{1-\alpha}{\alpha}-\frac{1-\beta}{\beta}=m\{1+(\alpha\beta)^{1/2}+\{((1-\alpha)(1-\beta))\}^{1/2}\}^{1/2}$.",
    ),
    rec(
        "RN-P3-C19-Entry19iv",
        r"$\displaystyle\frac{((1-\beta)^7)^{1/8}}{1-\alpha}-\frac{(\beta^7)^{1/8}}{\beta}=\frac{((1-\beta)^7)^{1/8}(\beta^7)^{1/8}}{(1-\alpha)(1-\beta)}-1$ and $\displaystyle\frac{(\alpha^7)^{1/8}}{1-\beta}-\frac{((1-\alpha)^7)^{1/8}}{\alpha}=\frac{(\alpha^7)^{1/8}((1-\alpha)^7)^{1/8}}{(1-\alpha)(1-\beta)}-1$.",
    ),
    rec(
        "RN-P3-C19-Entry19v",
        r"$\displaystyle m^2=\left(\frac{\alpha}{\beta}\right)^{1/2}+\left(\frac{1-\beta}{1-\alpha}\right)^{1/2}-\left(\frac{\beta(1-\beta)}{\alpha(1-\alpha)}\right)^{1/2}-\frac{8(\beta(1-\beta))^{1/3}}{\alpha(1-\alpha)}$ and $\displaystyle\frac{7}{m^2}=\left(\frac{\alpha}{\beta}\right)^{1/2}+\left(\frac{1-\alpha}{1-\beta}\right)^{1/2}-\left(\frac{\alpha(1-\alpha)}{\beta(1-\beta)}\right)^{1/2}-\frac{8(\alpha(1-\alpha))^{1/3}}{\beta(1-\beta)}$.",
    ),
    rec(
        "RN-P3-C19-Entry19vi",
        r"$\displaystyle\frac{((1-\beta)^3)^{1/4}}{1-\alpha}+\frac{(\beta^3)^{1/4}}{\beta}-\frac{(\beta^3(1-\beta)^3)^{1/4}}{\alpha(1-\alpha)}=\frac{2}{m}\{1+(\alpha\beta)^{1/2}+\{((1-\alpha)(1-\beta))\}^{1/2}\}$ and $\displaystyle\frac{((1-\alpha)^3)^{1/4}}{1-\beta}+\frac{(\alpha^3)^{1/4}}{\alpha}-\frac{(\alpha^3(1-\alpha)^3)^{1/4}}{\beta(1-\beta)}=\frac{49}{m^2}\{1+(\alpha\beta)^{1/2}+\{((1-\alpha)(1-\beta))\}^{1/2}\}$.",
    ),
    rec(
        "RN-P3-C19-Entry19vii",
        r"$\displaystyle\frac{((1-\beta)^7)^{1/8}}{1-\alpha}+\frac{(\beta^7)^{1/8}}{\beta}+2\left\{\frac{\beta^7(1-\beta)^7}{\alpha(1-\alpha)}\right\}^{1/24}=\frac{3+m^2}{4}$ and $\displaystyle\frac{((1-\alpha)^7)^{1/8}}{1-\beta}+\frac{(\alpha^7)^{1/8}}{\alpha}+2\left\{\frac{\alpha^7(1-\alpha)^7}{\beta(1-\beta)}\right\}^{1/24}=\frac{3+49/m^2}{4}$.",
    ),
    rec(
        "RN-P3-C19-Entry19viii",
        r"$\displaystyle\frac{m-7/m}{2}=(\alpha\beta)^{1/8}-\{((1-\alpha)(1-\beta))\}^{1/8}\cdot\{2+(\alpha\beta)^{1/4}+\{((1-\alpha)(1-\beta))\}^{1/4}\}$.",
    ),
    rec(
        "RN-P3-C19-Entry19ix",
        r"If $P=\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/8}$ and $Q=(\beta(1-\beta))^{1/6}$, then $\displaystyle\frac{\alpha(1-\alpha)}{P}+\frac{1}{P}=Q+\frac{1}{Q}+(P^{1/8}-P^{-1/8})^8$.",
    ),
    rec(
        "RN-P3-C19-Entry19x",
        r"If $P=(\alpha\beta)^{1/4}$ and $Q=(\beta/\alpha)^{1/8}$, then $(1-PQ^3)(1+P/Q^3)=7(1+PQ)(1-P/Q)$.",
    ),
    rec(
        "RN-P3-C19-Entry19xi",
        r"If $\alpha=\sin^2(\mu+\nu)$ and $\beta=\sin^2(\mu-\nu)$, then $\cos(2\mu)=(2\cos\nu-1)(4\cos\nu-1)^{1/2}$.",
    ),

]
