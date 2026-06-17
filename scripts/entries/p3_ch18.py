"""Part III, Chapter 18 entries — Jacobian elliptic functions (curated LaTeX)."""

from __future__ import annotations

TOPICS_C18 = ["jacobian-elliptic-functions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C18}


CHAPTER_18 = [
    rec(
        "RN-P3-C18-Entry01",
        r"Recall from Section 9 of Chapter 15 the definition $L(e^{-2y})=1-24\sum_{n=1}^\infty "
        r"\frac{n}{e^{ny}-1}$. In the notation of Section 6 of Chapter 17, "
        r"$\displaystyle{}_2F_1\!\left(-\tfrac12,-\tfrac12;1;x\right)"
        r"=z(1-x)+\int_0^x\frac{z}{x}\,dx"
        r"=\frac{3(1+x)}{2}+\frac{1}{3z}\,L(e^{-2y})$.",
    ),
    rec(
        "RN-P3-C18-Entry02",
        r"In the same notation as Entry 1, "
        r"$\displaystyle{}_2F_1\!\left(-\tfrac12,\tfrac12;1;x\right)"
        r"=z(1-x)+\int_0^x\frac{z}{x}\,dx"
        r"=\frac{2-x}{3}+\frac{1}{3z}\,L(e^{-2y})$.",
    ),
    rec(
        "RN-P3-C18-Entry03",
        r"Consider the ellipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ with eccentricity "
        r"$e=\frac{1}{a}\sqrt{a^2-b^2}$. If $L=L(a,b)$ denotes the perimeter, then "
        r"$L=2\pi a\,{}_2F_1\!\left(\tfrac12,-\tfrac12;1;e^2\right)"
        r"=\pi(a+b)\,{}_2F_1\!\left(-\tfrac12,-\tfrac12;1;t\right)"
        r"=\pi\{3(a+b)-\sqrt{(a+3b)(3a+b)}\}$ nearly, "
        r"$=\pi(a+b)\left\{1+\frac{3t}{10+4\sqrt{1-3t}}\right\}$ very nearly, "
        r"where $t=\left(\frac{a-b}{a+b}\right)^2$ in the last two formulas.",
    ),
    rec(
        "RN-P3-C18-Entry03-Example",
        r"(i) $\pi=3.1415926535897932384626434$; "
        r"(ii) $\log 10=2.302585092994045684018$; "
        r"(iii) $e^{-\pi}=0.04321391826377225$; "
        r"(iv) $e^{\pi/2}=4.810477380965351655473$.",
    ),
    rec(
        "RN-P3-C18-Entry03-Corollary",
        r"According to Ramanujan, $\pi=\frac{355}{113}\left(1-\frac{0.0003}{3533}\right)$ "
        r"very nearly, and $\pi\approx\left(97+\tfrac34-\tfrac14\right)^{1/4}$ nearly.",
    ),
    rec(
        "RN-P3-C18-Entry04",
        r"Let $x$ and $y$ be as in Section 6 of Chapter 17. Then "
        r"$\displaystyle\sqrt{x}\sum_{n=0}^\infty\frac{\left(\frac12\right)_n}{n!}x^n"
        r"=-2\sum_{n=0}^\infty(-1)^n(2n+1)\log\frac{1+e^{-(2n+1)y/2}}{1-e^{-(2n+1)y/2}}$.",
    ),
    rec(
        "RN-P3-C18-Entry05",
        r"Let $x$ and $y$ be as in Entry 4. Then "
        r"$\displaystyle\log\frac{16}{x}-\sum_{n=1}^\infty\frac{\left(\frac12\right)_n^2}{n!^2}x^n"
        r"=y-4\sum_{n=0}^\infty(-1)^n(2n+1)\log(1-e^{-(2n+1)y})$.",
    ),
    rec(
        "RN-P3-C18-Entry06",
        r"With $x$, $y$, and $z$ as in Section 6 of Chapter 17, "
        r"$\displaystyle\sum_{n=0}^\infty\frac{1}{(2n+1)^2\cosh\{\tfrac12(2n+1)y\}}"
        r"=\frac{z}{2}\,{}_3F_2(1,1,1;\tfrac32,\tfrac32;x)$.",
    ),
    rec(
        "RN-P3-C18-Entry07",
        r"Let Catalan's constant $C=\displaystyle\sum_{n=0}^\infty\frac{(-1)^n}{(2n+1)^2}$. Then "
        r"$\displaystyle\sum_{n=0}^\infty\frac{(-1)^n}{(2n+1)^2(e^{(2n+1)y}+1)}"
        r"=\frac{\pi^2}{16}-\frac{C}{2}+\frac{y}{4z}\,{}_3F_2\!\left(1,1,1;\tfrac32,\tfrac32;1-x\right)$.",
    ),
    rec(
        "RN-P3-C18-Entry07-Example",
        r"Let $x$ and $y$ be as above. Then "
        r"$\displaystyle\sum_{n=0}^\infty\frac{1}{(2n+1)\sinh\{\tfrac12(2n+1)y\}}"
        r"=\frac14\log\frac{1+\sqrt{x}}{1-\sqrt{x}}$.",
    ),
    rec(
        "RN-P3-C18-Entry08",
        r"Let $\varepsilon$ be real. If $|\varepsilon|<\pi$, then "
        r"$\displaystyle\sum_{n=0}^\infty\frac{(-1)^n\{\cos(2n+1)\varepsilon+2\cos\{\tfrac12(2n+1)\varepsilon\}"
        r"\cosh\{\tfrac12(2n+1)\sqrt3\,\varepsilon\}\}}{(2n+1)\cosh\{\tfrac12(2n+1)\pi\sqrt3\}}"
        r"=-\frac{\pi}{8}$; if $|\varepsilon|<\pi/2$, then "
        r"$\displaystyle\sum_{n=0}^\infty\frac{(-1)^n\cos(2n+1)\varepsilon\{\cos(2n+1)\varepsilon"
        r"+\cosh((2n+1)\sqrt3\,\varepsilon)\}}{(2n+1)\cosh\{\tfrac12(2n+1)\pi\sqrt3\}}=\frac{\pi}{12}$, "
        r"$\displaystyle\sum_{n=0}^\infty\frac{(-1)^n\sin(2n+1)\varepsilon\{\cos(2n+1)\varepsilon"
        r"-\cosh((2n+1)\sqrt3\,\varepsilon)\}}{(2n+1)^4\cosh\{\tfrac12(2n+1)\pi\sqrt3\}}"
        r"=-\frac{\pi^3\varepsilon^3}{12}$, and "
        r"$\displaystyle\sum_{n=0}^\infty\frac{(-1)^n\cos(2n+1)\varepsilon\{\cos(2n+1)\varepsilon"
        r"+\cosh((2n+1)\sqrt3\,\varepsilon)\}}{(2n+1)^7\cosh\{\tfrac12(2n+1)\pi\sqrt3\}}"
        r"=\frac{\pi^7\varepsilon^6}{11520}$.",
    ),
    rec(
        "RN-P3-C18-Entry09",
        r"If $z\neq\pm\omega^j(2n+1)$ for $0\le j\le 2$, $0\le n<\infty$, where $\omega=e^{2\pi i/3}$, then "
        r"$\displaystyle\sum_{n=0}^\infty\frac{(-1)^n(2n+1)^5}"
        r"{\cosh\{\tfrac12(2n+1)\pi\sqrt3\}\{(2n+1)^6-z^6\}}"
        r"=-\frac{1}{12\cos(\tfrac{z}{3})\{\cos(\tfrac{z}{3})+\cosh(\tfrac{\sqrt3\,z}{3})\}}$.",
    ),
    rec(
        "RN-P3-C18-Entry09-Examplei",
        r"For each complex $z$, "
        r"$\displaystyle\frac12\cos(\tfrac13 z)\{\cos(\tfrac13 z)+\cosh(\tfrac13\sqrt3\,z)\}"
        r"=1+\frac34\sum_{n=1}^\infty\frac{(-1)^n z^6}{(6n)^6-(2n+1)^6}"
        r"=\prod_{n=1}^\infty\left(1-\frac{z^6}{(2n+1)^6\pi^6}\right)$.",
    ),
    rec(
        "RN-P3-C18-Entry09-Exampleii",
        r"For each complex $z$, "
        r"$\displaystyle\frac12\sin(\tfrac13 z)\{\cos(\tfrac13 z)-\cosh(\tfrac13\sqrt3\,z)\}"
        r"=-\frac34\sum_{n=0}^\infty\frac{(-1)^n z^{6n+3}}{(6n+3)^3-(2n+1)^3}"
        r"=-\frac{z^3}{8}\prod_{n=1}^\infty\left(1-\frac{z^6}{(2\pi n)^6}\right)$.",
    ),
    rec(
        "RN-P3-C18-Entry10",
        r"If $z\neq\pm\omega^j(2n+1)$ for $0\le j\le 2$, $0\le n<\infty$, where $\omega=e^{2\pi i/3}$, then "
        r"$\displaystyle\sum_{n=0}^\infty\frac{(-1)^n(2n+1)^5}"
        r"{\cosh\{\tfrac12(2n+1)\pi\sqrt3\}\{(2n+1)^6-z^6\}}"
        r"=\frac{z^4}{12}\frac{\cosh(\tfrac{\sqrt3\,z}{3})\{\cos(\tfrac{z}{3})+\cosh(\tfrac{\sqrt3\,z}{3})\}-3}"
        r"{\cos(\tfrac{z}{3})\{\cos(\tfrac{z}{3})+\cosh(\tfrac{\sqrt3\,z}{3})\}}$.",
    ),
    rec(
        "RN-P3-C18-Entry10-Example01",
        r"Under the hypotheses of Entry 10, "
        r"$\displaystyle\sum_{n=0}^\infty\frac{(2n+1)^2}{(2n+1)^6-z^6}"
        r"=\frac{\cosh(\tfrac{\sqrt3\,z}{3})-\cos(\tfrac{z}{3})\tan(\tfrac{z}{3})}{12\cosh(\tfrac{\sqrt3\,z}{3})"
        r"+\cos(\tfrac{z}{3})}$.",
    ),
    rec(
        "RN-P3-C18-Entry10-Example02",
        r"$\displaystyle\sum_{n=0}^\infty\frac{(-1)^n}{(2n+1)^7\cosh\{\tfrac12(2n+1)\pi\sqrt3\}}"
        r"=-\frac{\pi^7}{23040}$.",
    ),
    rec(
        "RN-P3-C18-Entry11",
        r"(i) If $|\operatorname{Im}\,\theta|<\pi$, then "
        r"$\displaystyle\left\{1+2\sum_{n=1}^\infty\frac{\cos(n\theta)}{\cosh(n\pi)}\right\}^{-1}"
        r"+\left\{1+2\sum_{n=1}^\infty\frac{\cosh(n\theta)}{\cosh(n\pi)}\right\}^{-1}"
        r"=\frac{2}{\Gamma^4(\tfrac14)}$. "
        r"(ii) Let $x'$, $y'$, and $z'$ denote the parameters associated with the complementary "
        r"modulus $k'$. If $|\operatorname{Im}\,\theta|<y/2$, then "
        r"$\displaystyle\sum_{n=0}^\infty\frac{\cos(2n+1)\theta}{\cosh\{\tfrac12(2n+1)y\}}"
        r"=\sum_{n=0}^\infty\frac{\cosh(2n+1)\theta}{\cosh\{\tfrac12(2n+1)y'\}}"
        r"=\frac{zz'}{4\sqrt{xx'}}$.",
    ),
    rec(
        "RN-P3-C18-Entry12",
        r"If $\eta>0$, then "
        r"(i) $\displaystyle\frac12+\sum_{j=1}^\infty\frac{\operatorname{sech}(jy)}{1+(j\eta)^2}"
        r"=\frac{(\eta z)^2}{2}+\frac{(\eta z)^2}{2^2}+\frac{(2\eta z)^2}{3^2}+\frac{(3\eta z)^2}{4^2}+\cdots$, and "
        r"(ii) $\displaystyle\sum_{j=0}^\infty\frac{\operatorname{sech}\{\tfrac12(2j+1)y\}}{1+(2j+1)^2\eta^2}"
        r"=\frac{z\sqrt{x}}{(\eta z)^2}+\frac{z\sqrt{x}}{(2\eta z)^2}+\frac{z\sqrt{x}}{(3\eta z)^2}+\cdots$.",
    ),
    rec(
        "RN-P3-C18-Entry12-Corollary",
        r"For $\eta>0$, $\operatorname{Re}\,\alpha>0$, and $\operatorname{Re}\,\beta>0$, define "
        r"$F(\alpha,\beta)=\frac{\alpha}{\eta}+\frac{\beta^2}{(\eta\alpha)^2}+\frac{(2\alpha)^2}{(3\beta)^2}"
        r"+\frac{(3\beta)^2}{(4\alpha)^2}+\cdots$. Then "
        r"$F\!\left(\tfrac{\alpha+\beta}{2},\sqrt{\alpha\beta}\right)=\tfrac12\{F(\alpha,\beta)+F(\beta,\alpha)\}$.",
    ),
    rec(
        "RN-P3-C18-Entry13",
        r"If $\eta>0$, then "
        r"(i) $\displaystyle\sum_{j=0}^\infty\frac{(-1)^j\operatorname{csch}\{\tfrac12(2j+1)y\}}{1+(2j+1)^2\eta^2}"
        r"=\frac{z\sqrt{x}}{(1-x)(\eta z)^2}+\frac{z\sqrt{x}}{(2\eta z)^2}+\cdots$; "
        r"(ii) $\displaystyle\sum_{j=0}^\infty\frac{(-1)^j(2j+1)\operatorname{sech}\{\tfrac12(2j+1)y\}}{1+(2j+1)^2\eta^2}"
        r"=\frac{z^2\sqrt{x(1-x)}}{1+(\eta z)^2(1-2x)}+\frac{2^2(2^2-1)x(1-x)(\eta z)^4}{1+(3\eta z)^2(1-2x)}+\cdots$; "
        r"(iii) $\displaystyle\sum_{j=0}^\infty\frac{(2j+1)\operatorname{csch}\{\tfrac12(2j+1)y\}}{1+(2j+1)^2\eta^2}"
        r"=\frac{z^2\sqrt{x}}{1+(\eta z)^2(1+x)}-\frac{2^2(2^2-1)x(\eta z)^4}{1+(3\eta z)^2(1+x)}+\cdots$, "
        r"where in (i) and (ii), $0<x<1/\sqrt2$.",
    ),
    rec(
        "RN-P3-C18-Entry13-Corollary",
        r"If $\eta>0$, then "
        r"$\displaystyle\sum_{j=0}^\infty\frac{(-1)^j(2j+1)\operatorname{sech}\{\tfrac12(2j+1)\eta\}}{1+(2j+1)^2\eta^2}"
        r"=\frac{\mu}{\eta^2}+\frac{\mu^2+1\cdot 3(\eta\mu)^4}{6}+\frac{15\cdot 21(\eta\mu)^4}{10}+\cdots$, "
        r"where $\mu=\ln/\Gamma^2(\tfrac34)$ in Ramanujan's notation.",
    ),
    rec(
        "RN-P3-C18-Entry14",
        r"Define, for real $\theta$, "
        r"$S(\theta)=\sum_{j=0}^\infty\frac{\sin((2j+1)\theta)}{\sinh\{\tfrac12(2j+1)y\}}$, "
        r"$C(\theta)=\sum_{j=0}^\infty\frac{\cos((2j+1)\theta)}{\cosh\{\tfrac12(2j+1)y\}}$, and "
        r"$C_1(\theta)=\tfrac12+\sum_{j=1}^\infty\frac{\cos(2j\theta)}{\cosh(jy)}$, "
        r"so that $S=\tfrac12 z\sqrt{x}\,\mathrm{sn}(z\theta)$, $C=\tfrac12 z\sqrt{x}\,\mathrm{cn}(z\theta)$, and "
        r"$C_1=\tfrac12 z\,\mathrm{dn}(z\theta)$. Then "
        r"$C^2+S^2=\tfrac14 xz^2$, $C_1^2+S^2=\tfrac14 z^2$, "
        r"$CS=\sum_{j=1}^\infty\frac{j\sin(2j\theta)}{\cosh(jy)}$, "
        r"$\frac{dC_1}{d\theta}+2CS=0$, and $\frac{dS}{d\theta}=2CC_1$. "
        r"Define $\varphi$, $0\le\varphi<2\pi$, by $C=\tfrac12 z\sqrt{x}\cos\varphi$ and $S=\tfrac12 z\sqrt{x}\sin\varphi$. Then "
        r"$C_1=\tfrac12 z\sqrt{1-x\sin^2\varphi}$, "
        r"$\displaystyle\frac{z\cos\varphi}{\sqrt{1-x\sin^2\varphi}}=\frac{d\sin\varphi}{d\varphi}=\cos\varphi\,\frac{d\varphi}{d\theta}$, and "
        r"$\displaystyle\frac{z\sqrt{x}\cos\varphi}{\sqrt{1-x\sin^2\varphi}}=\frac{d\theta}{d\varphi}$.",
    ),
    rec(
        "RN-P3-C18-Entry15",
        r"Let $\varphi$ be defined by Entry 14. Then "
        r"(i) $\displaystyle 1+2\sum_{n=1}^\infty\frac{\cos(2n\theta)}{\cosh(ny)}=\frac{z\sqrt{x}}{\sqrt{1-x\sin^2\varphi}}$; "
        r"(ii) $\displaystyle\sum_{n=0}^\infty\frac{\cos((2n+1)\theta)}{\cosh\{\tfrac12(2n+1)y\}}"
        r"=\frac{2z}{\pi}\sqrt{x}\cos\varphi$; "
        r"(iii) $\displaystyle\sum_{n=0}^\infty\frac{\sin((2n+1)\theta)}{\sinh\{\tfrac12(2n+1)y\}}"
        r"=\frac{2z}{\pi}\sqrt{x}\sin\varphi$; "
        r"(iv) $\displaystyle\theta+\sum_{n=1}^\infty\frac{\sin(2n\theta)}{n\cosh(ny)}=\varphi$; "
        r"(v) $\displaystyle\sum_{n=0}^\infty\frac{\sin((2n+1)\theta)}{(2n+1)\cosh\{\tfrac12(2n+1)y\}}"
        r"=\frac{2}{\pi}\sin^{-1}(\sqrt{yx}\sin\varphi)$; "
        r"(vi) $\displaystyle\sum_{n=0}^\infty\frac{\cos((2n+1)\theta)}{(2n+1)\sinh\{\tfrac12(2n+1)y\}}"
        r"$=-\frac12\log\frac{\sqrt{1-x\sin^2\varphi}-\sqrt{x}\cos\varphi}{\sqrt{1-x\sin^2\varphi}+\sqrt{x}\cos\varphi}$ "
        r"(Berndt notes Ramanujan omitted the minus sign).",
    ),
    rec(
        "RN-P3-C18-Entry16i",
        r"Suppose $\theta$ and $\varphi$ are related as in Entry 14. If $\theta$ is replaced by $\pi-\theta$ "
        r"in any formula involving $\theta$, the corresponding conversions for functions of $\varphi$ are: "
        r"$\cot\varphi\to\sqrt{1-x}\tan\varphi$; $\sin\varphi\to\cos\varphi$; "
        r"$\cos\varphi\to\sqrt{1-x\sin^2\varphi}$; "
        r"$\sqrt{1-x\sin^2\varphi}\to\frac{\sin\varphi}{\sqrt{1-x\sin^2\varphi}}$.",
    ),
    rec(
        "RN-P3-C18-Entry16ii",
        r"With $\theta$ and $\varphi$ related by Entry 14, "
        r"(i) $\displaystyle\sum_{n=0}^\infty\frac{(-1)^n\cos((2n+1)\theta)}{\sinh\{\tfrac12(2n+1)y\}}"
        r"=\frac{\cos\varphi}{z\sqrt{x}\sqrt{1-x\sin^2\varphi}}$; "
        r"(ii) $\displaystyle\sum_{n=0}^\infty\frac{(-1)^n\sin((2n+1)\theta)}{\cosh\{\tfrac12(2n+1)y\}}"
        r"=\frac{\sin\varphi}{2z\sqrt{x(1-x)}\sqrt{1-x\sin^2\varphi}}$; "
        r"(iii) $\displaystyle\csc\theta+4\sum_{n=0}^\infty\frac{\sin((2n+1)\theta)}{e^{(2n+1)y}-1}"
        r"=z\csc\varphi$; "
        r"(iv) $\displaystyle\sec\theta+4\sum_{n=0}^\infty\frac{(-1)^n\cos((2n+1)\theta)}{e^{(2n+1)y}-1}"
        r"=z\sec\varphi\sqrt{1-x\sin^2\varphi}$; "
        r"(v) $\displaystyle\log\tan\!\left(\frac{\pi}{4}+\frac{\theta}{2}\right)"
        r"+4\sum_{n=0}^\infty\frac{(-1)^n\sin((2n+1)\theta)}{(2n+1)(e^{(2n+1)y}-1)}"
        r"=\log\tan\!\left(\frac{\pi}{4}+\frac{\varphi}{2}\right)$.",
    ),
    rec(
        "RN-P3-C18-Entry17",
        r"Let $\theta$ and $\varphi$ be related by Entry 14. Define $L$ as in Section 9 of Chapter 15 by "
        r"$L(e^{-2y})=1-24\sum_{n=1}^\infty\frac{2n}{e^{ny}-1}$. Then "
        r"(i) $\displaystyle\frac{\cos\theta}{\sin^3\theta}+16\sum_{n=1}^\infty\frac{n^2\sin(2n\theta)}{e^{2ny}-1}"
        r"=-\frac{2z^2\cos\varphi}{\sin^3\varphi\sqrt{1-x\sin^2\varphi}}$; "
        r"(ii) $\displaystyle\frac{z^2}{\sin^2\theta}-8\sum_{n=1}^\infty\frac{n\cos(2n\theta)}{e^{2ny}-1}"
        r"=\frac{z^2}{\sin^2\varphi}-\frac{3z^2(1+x)}{2}+3L(e^{-2y})$; "
        r"(iii) $\displaystyle\cot\theta+4\sum_{n=1}^\infty\frac{\sin(2n\theta)}{e^{2ny}-1}"
        r"$=z\cot\varphi\sqrt{1-x\sin^2\varphi}+\frac{z}{\pi}\int_0^\varphi\sqrt{1-x\sin^2\psi}\,d\psi"
        r"-\frac{2z}{\pi}\int_0^{\pi/2}\sqrt{1-x\sin^2\psi}\,d\psi$; "
        r"(iv) $\displaystyle\sum_{n=1}^\infty\frac{\sin(2n\theta)}{\sinh(ny)}"
        r"$=-\frac{z}{\pi}\int_0^\varphi\sqrt{1-x\sin^2\psi}\,d\psi"
        r"+\frac{z}{\pi}\int_0^{\pi/2}\sqrt{1-x\sin^2\psi}\,d\psi$.",
    ),
    rec(
        "RN-P3-C18-Entry18i",
        r"If $\theta$ is replaced by $\tfrac{\theta}{2}$ and $y$ by $\tfrac{y}{2}$ in (18.1), then "
        r"$\eta\!\left(\frac{4\sqrt{x}}{1+x},e^{-y/2},(1+\sqrt{x})z,\tfrac{\theta}{2},"
        r"\tfrac12\{\varphi+\sin^{-1}(\sqrt{x}\sin\varphi)\}\right)=0$.",
    ),
    rec(
        "RN-P3-C18-Entry18ii",
        r"If $\theta$ is replaced by $\pi-\theta$ and $e^{-y}$ by $-e^{-y}$, then "
        r"$\eta\!\left(\frac{x}{1-x},-e^{-y},z\sqrt{1-x},\pi-\theta,\pi-\varphi\right)=0$.",
    ),
    rec(
        "RN-P3-C18-Entry18iii",
        r"If $e^{-y}$ is replaced by $-e^{-y}$, then "
        r"$\eta\!\left(\frac{x}{1-x},-e^{-y},z\sqrt{1-x},\theta,\frac{\cot\varphi}{\sqrt{1-x}}\right)=0$ "
        r"(Ramanujan incorrectly wrote $\frac{\cot\varphi}{\sqrt{x-1}}$).",
    ),
    rec(
        "RN-P3-C18-Entry18iv",
        r"Let $z'=2F_1(\tfrac12,\tfrac12;1;1-x)$ and $y'=\pi/z'$. If $\theta$ is replaced by $i\theta z/z'$ "
        r"and $y$ by $y'$, then "
        r"$\eta(1-x,e^{-y'},z',i\theta z/z',i\log\tan(\tfrac{\pi}{4}+\tfrac{\varphi}{2}))=0$. "
        r"Furthermore, $\sin\varphi$ is converted to $i\tan\varphi$ and $\cos\varphi$ to $\sec\varphi$.",
    ),
    rec(
        "RN-P3-C18-Entry19i",
        r"Let an ellipse of eccentricity $e$ be given by $x=a\cos\varphi$, $y=b\sin\varphi$, "
        r"$0\le\varphi\le 2\pi$. Let $P=(a\cos\varphi,b\sin\varphi)$ and $A=(a,0)$. Then the arc length "
        r"$L(AP)=a\int_0^\varphi\sqrt{1-e^2\cos^2\psi}\,d\psi$.",
    ),
    rec(
        "RN-P3-C18-Entry19ii",
        r"Let a hyperbola of eccentricity $e$ be given by $x=a\sec\varphi$, $y=b\tan\varphi$, "
        r"$0\le\varphi\le 2\pi$. Let $P=(a\sec\varphi,b\tan\varphi)$ and $A=(a,0)$. Then "
        r"$L(AP)=a\tan\varphi\sqrt{e^2-\cos^2\varphi}-a\int_0^\varphi\sqrt{e^2-\cos^2\psi}\,d\psi$.",
    ),
    rec(
        "RN-P3-C18-Entry19iii",
        r"Let the perimeter $L$ of the ellipse $x=a\cos t$, $y=b\sin t$, $0\le t\le 2\pi$, be given by "
        r"$L=\pi(a+b)(1+4\sin^2\theta)$, $0\le\theta\le\pi$, where "
        r"$\sin\theta=\sqrt{x}\sin\varphi$ and $x=\left(\frac{a-b}{a+b}\right)^2$. "
        r"Then when $e=1$, $\varphi=30^\circ18'6''$, and as $e\to 0$, $\varphi$ tends monotonically to $30^\circ$.",
    ),
    rec(
        "RN-P3-C18-Entry19iv",
        r"Consider the same ellipse as in Entry 19(iii), but now set "
        r"$L=\pi(a+b)\left(1+\frac{\sin^2\theta}{2+\cos^2\theta}\right)$, $0\le\theta\le\pi$, where "
        r"$\sin\theta=\sqrt{x}\sin\varphi$ and $x=\left(\frac{a-b}{a+b}\right)^2$. "
        r"Then when $e=1$, $\varphi=60^\circ4'55''$, and when $e=0$, $\varphi=60^\circ$.",
    ),
    rec(
        "RN-P3-C18-Entry19-Corollary01",
        r"Let the perimeter $L$ of an ellipse be given by "
        r"$L=\pi(a+b)\frac{\tan\theta}{\theta}$, $0<\theta<\pi/2$, where "
        r"$\tan\theta=\sqrt{x}\cos\varphi$ and $x=\left(\frac{a-b}{a+b}\right)^2$. "
        r"As $e$ increases from $0$ to $1$, $\varphi$ decreases from $\pi/6$ to $0$. Furthermore, "
        r"$\varphi$ is approximately "
        r"$\frac{\pi}{6}-x(1-x)\left(11'22''+32'42''x\right)$.",
    ),
    rec(
        "RN-P3-C18-Entry19-Corollary02",
        r"Let $L(UV)$ denote the length of an arc $UV$ of an ellipse or circle. "
        r"Suppose $PN$ is rotated until $\frac{L(AI)}{L(AB)}=\frac{L(AK)}{AN}$. Then $\varphi$ is approximately "
        r"$30^\circ-x(1-x)(11'22''+32'42''x)$, where $x=\left(\frac{a-b}{a+b}\right)^2$ as before.",
    ),
    rec(
        "RN-P3-C18-Entry20i",
        r"Let $O$ be the center and $PR$ a diameter of a circle. Bisect $OP$ at $H$ and trisect "
        r"$OR$ at $T$ with $OT=2TR$. Let $TQ\perp OR$ with $Q$ on the circle, $RS=TQ$ with $S$ on "
        r"arc $QR$, $OM\parallel RS$ and $TN\parallel RS$ with $M,N$ on $PS$, $PK=PM$ with $K$ on "
        r"the circle opposite $Q$ and $S$, $PL\perp OP$ of length $MN$ on the same side of $PR$ as $K$, "
        r"$RC=RH$ with $C$ on $RK$, and $CD\parallel KL$ with $D$ on $RL$. Then $RD=\frac{3}{4}RL$. "
        r"Ramanujan asserts that the area of the circle is approximately $RD^2$, giving "
        r"$\pi\approx 355/113$.",
    ),
    rec(
        "RN-P3-C18-Entry20-Corollary01",
        r"Inscribe an equilateral triangle of side $t$ in the circle of Entry 20(i). Let $m$ denote the "
        r"first of two mean proportionals between $t$ and $PS$. Then $m/(t\sqrt{d/\pi})$ differs from "
        r"unity by approximately $1/30000$.",
    ),
    rec(
        "RN-P3-C18-Entry20-Corollary02",
        r"If $\pi$ is approximated by $(97\pi-\sqrt{1})^{1/4}$ in the expression $\tfrac12 d\sqrt{\pi}$, then "
        r"for a circle of one million square miles the error is approximately $1/100$th of an inch.",
    ),
    rec(
        "RN-P3-C18-Entry20ii",
        r"Parametric solutions of $A^3+B^3=C^2$ are given by "
        r"$A=3n^3+6n^2-n$, $B=-3n^3+6n^2+n$, and $C=n^2(18n^2+6)$, where $n$ is arbitrary.",
    ),
    rec(
        "RN-P3-C18-Entry20iii",
        r"Parametric solutions of $A^3+B^3+C^3=D^3$ are given by "
        r"$A=m^7-3(p+1)m^4+(3p^2+6p+2)m$, "
        r"$B=2m^6-3(2p+1)m^3+(3p^2+3p+1)$, "
        r"$C=m^6-(3p^2+3p+1)$, and "
        r"$D=m^7-3pm^4+(3p^2-1)m$, where $m$ and $p$ are arbitrary.",
    ),
    rec(
        "RN-P3-C18-Entry21",
        r"Let $x$ be any complex number except at poles of the functions below. Then "
        r"(i) $\displaystyle\frac{\pi}{\sqrt3\,x^2}\frac{\cosh(\pi\sqrt3\,x)+2\cos(\pi x)}{\cosh(\pi\sqrt3\,x)-\cos(\pi x)}"
        r"=\frac{2}{\sqrt3\,x^4}+\sum_{k=1}^\infty\frac{(-1)^k k}{x^4+k^2x^2+k^4}"
        r"+\sum_{k=1}^\infty\frac{(-1)^k k}{(x^4+k^2x^2+k^4)(e^{k\pi\sqrt3}-(-1)^k)}$; "
        r"(ii) $\displaystyle\frac{\pi}{\sqrt3\,x^2}\frac{\cosh(\pi\sqrt3\,x)+2\cos(\pi x)+6\cosh(x/\sqrt3)}{\cosh(\pi\sqrt3\,x)-\cos(\pi x)}"
        r"$=\frac{2}{\sqrt3\,x^4}-\frac{2}{\pi x^4}+\sum_{k=1}^\infty\frac{(-1)^k k}{x^4+k^2x^2+k^4}"
        r"+\sum_{k=1}^\infty\frac{(-1)^k p(k)}{(x^4+k^2x^2+k^4)(e^{k\pi\sqrt3}-(-1)^k)}$, "
        r"where $p(k)=\frac{2k}{\sinh(\tfrac12 k\pi\sqrt3)\cosh(\tfrac12 k\pi\sqrt3)}$ if $k$ is even and "
        r"$p(k)=\frac{2k}{\cosh(\tfrac12 k\pi\sqrt3)\sinh(\tfrac12 k\pi\sqrt3)}$ if $k$ is odd; "
        r"(iii) $\displaystyle\frac{2\pi}{\sqrt3\,x^2}\frac{e^{2\pi\sqrt3\,x}-2e^{\pi\sqrt3\,x}\cos(\pi x)+1}"
        r"=\frac{2}{\sqrt3\,x^4}+\frac{1}{2x^3}+\frac{1}{3\sqrt3\,x^2}"
        r"+\sum_{k=1}^\infty\frac{(-1)^k k}{(x^4+k^2x^2+k^4)(e^{k\pi\sqrt3}-(-1)^k)}"
        r"$-\frac{1}{x}\sum_{k=1}^\infty\frac{1}{x^2+kx+k^2}$; "
        r"(iv) $\displaystyle\frac{2\pi}{\sqrt3\,x^2}\frac{e^{2\pi\sqrt3\,x}-2e^{\pi\sqrt3\,x}\cos(3\pi x)+1}"
        r"=\frac{2}{3\sqrt3\,x^4}+\frac{1}{6x^3}+\frac{1}{3\sqrt3\,x^2}"
        r"+\sum_{k=1}^\infty\frac{(-1)^k k}{(9x^4-3k^2x^2+k^4)(e^{k\pi\sqrt3}-(-1)^k)}"
        r"$-\frac{1}{3x}\sum_{k=1}^\infty\frac{1}{3x^2+3kx+k^2}$ "
        r"(Berndt notes Ramanujan's notebook statement of (ii) appears incorrect).",
    ),
    rec(
        "RN-P3-C18-Entry21-Example",
        r"$\displaystyle\sum_{n=1}^\infty\frac{(-1)^{n-1}n}{81+9n^2+n^4}"
        r"=\frac{\pi}{324\sqrt3}+\frac{11}{756}+\frac{1}{27\sqrt3}"
        r"+\frac{\pi}{18\sqrt3(1+\cosh(3\sqrt3\,\pi))}$.",
    ),
    rec(
        "RN-P3-C18-Entry22",
        r"If $0<x<1$ and $\eta>0$, then "
        r"(i) $\displaystyle\int_0^\infty\exp\!\left(-\eta\int_0^\varphi\frac{d\theta}{\sqrt{1-x\sin^2\theta}}\right)d\varphi"
        r"=\frac{1}{\eta}+\frac{x}{\eta}+\frac{4}{\eta}+\frac{9x}{\eta}+\frac{16}{\eta}+\cdots$; "
        r"(ii) $\displaystyle\int_0^\infty\exp\!\left(-\eta\int_0^\varphi\frac{d\theta}{\sqrt{1-x\sin^2\theta}}\right)"
        r"\frac{\cos\varphi}{\sqrt{1-x\sin^2\varphi}}\,d\varphi"
        r"=\frac{4x}{\eta}+\frac{9}{\eta}+\frac{16x}{\eta}+\cdots$; "
        r"(iii) $\displaystyle\int_0^\infty\exp\!\left(-\eta\int_0^\varphi\frac{d\theta}{\sqrt{1-x\sin^2\theta}}\right)"
        r"\frac{\cos^2\varphi}{1-x\sin^2\varphi}\,d\varphi"
        r"=\frac{4x}{\eta}+\frac{9(1-x)}{\eta}+\frac{16x}{\eta}+\cdots$.",
    ),
    rec(
        "RN-P3-C18-Entry23",
        r"Let $x$ and $y$ be complex with $\operatorname{Re}(x\pm iy)>0$. Then "
        r"(i) $\displaystyle\frac{\sqrt{y}}{\sqrt2}\left\{-\frac12+\sum_{n=1}^\infty e^{-n^2\pi x/(x^2+y^2)}"
        r"\cos\frac{n^2\pi y}{x^2+y^2}\right\}"
        r"$+\sqrt{\frac{\sqrt{x^2+y^2}-x}{2}}\sum_{n=1}^\infty e^{-n^2\pi x}\sin(n^2\pi y)$; "
        r"(ii) $-\sqrt{\frac{\sqrt{x^2+y^2}+x}{2}}\displaystyle\sum_{n=1}^\infty e^{-n^2\pi x}\sin(n^2\pi y)$.",
    ),
    rec(
        "RN-P3-C18-Entry23-Corollary",
        r"If $\operatorname{Re}(x)>0$, then "
        r"$\displaystyle\frac12+\sum_{n=1}^\infty e^{-n^2\pi x}\cos\!\left(n\pi\sqrt{1-x}\right)"
        r"=\frac{\sqrt{x}}{\sqrt{1-x}}+\frac{\sqrt{1-x}}{\sqrt{x}}\sum_{n=1}^\infty e^{-n^2\pi x}"
        r"\sin\!\left(n\pi\sqrt{1-x}\right)$.",
    ),
    rec(
        "RN-P3-C18-Entry23-Example01",
        r"With $\varphi(q)$ as in Entry 22 of Chapter 16, "
        r"$\sqrt5\,\varphi(e^{-5\pi})=\varphi(e^{-\pi/5})$ and "
        r"$\sqrt{\frac{\sqrt5+1}{2}}\,\varphi(e^{-\pi})"
        r"=2\sqrt2\left\{\frac12+\sum_{n=1}^\infty e^{-n^2\pi/5}\cos\frac{2\pi n^2}{5}\right\}$.",
    ),
    rec(
        "RN-P3-C18-Entry23-Example02",
        r"With $\varphi(q)$ as in Entry 22 of Chapter 16, "
        r"$\varphi(e^{-\pi\sqrt5})-\varphi(e^{-\pi/\sqrt5})"
        r"=(\sqrt5-1)\left\{\varphi(e^{-\pi\sqrt5/3})-\varphi(e^{-3\pi/\sqrt5})\right\}$.",
    ),
    rec(
        "RN-P3-C18-Entry24ii",
        r"Let $m=\dfrac{{}_2F_1(\tfrac12,\tfrac12;1;\alpha)}{{}_2F_1(\tfrac12,\tfrac12;1;\beta)}$ as in Section 24(i). "
        r"Modular equations of degree $2$ are $m\sqrt{\alpha}+\sqrt{\beta}=1$ and "
        r"$m\sqrt{1-\alpha}+\sqrt{1-\beta}=1$. Furthermore, "
        r"$\dfrac{1+\beta}{1+\alpha}=\dfrac{1+\sqrt{\beta}}{1+\sqrt{1-\alpha}}$.",
    ),
    rec(
        "RN-P3-C18-Entry24iii",
        r"Modular equations of degree $4$ are $\sqrt{m}(1-\alpha)^{1/4}+\beta^{1/4}=1$ and "
        r"$m(1-\alpha)^{1/4}+\sqrt{\beta}=1$. Furthermore, the multiplier is "
        r"$m=\dfrac{1+\beta^{1/4}}{1+(1-\alpha)^{1/4}}=\dfrac{1+\sqrt{\beta}}{1+\alpha^{1/4}}$.",
    ),
    rec(
        "RN-P3-C18-Entry24v",
        r"If $\alpha$ is replaced by $1-\beta$, $\beta$ by $1-\alpha$, and $m$ by $n/m$, where $n$ is the degree "
        r"of the modular equation, one obtains a modular equation of the same degree "
        r"(the method of reciprocation, or Fricke involution).",
    ),
    rec(
        "RN-P3-C18-Entry24vi",
        r"Consider again the definitions of $m$ in Entry 24(ii). Then "
        r"$\displaystyle\frac{d\alpha}{\alpha(1-\alpha)}=\frac{n}{\,m^2\,}\frac{d\beta}{\beta(1-\beta)}$.",
    ),
]
