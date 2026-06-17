"""Part III, Chapter 16 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C16 = ["q-series-and-theta-functions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C16}


CHAPTER_16 = [
    rec(
        "RN-P3-C16-Entry01",
        r"Let $q$ be real with $|q|<1$, and suppose that $a$ and $x$ are any complex numbers. "
        r"Let the principal branches of $(1-a)^x$ and $(1-q)^x$ be chosen. Then "
        r"(i) $\displaystyle\lim_{q\to 1^-}\frac{(a)_\infty}{(aq^x)_\infty}=(1-a)^x$; "
        r"(ii) $\displaystyle\lim_{q\to 1^-}\frac{(q)_\infty}{(1-q)^x(q^{x+1})_\infty}=\Gamma(x+1)$; "
        r"(iii) $\displaystyle(a)_\infty=\prod_{k=0}^{\infty}(aq^k;q)_\infty$; and "
        r"(iv) $\displaystyle(a)_\infty=\frac{(-a;q)_\infty(-aq^{1/2};q^{1/2})_\infty}{(q^{1/2};q^{1/2})_\infty}$.",
    ),
    rec(
        "RN-P3-C16-Entry02",
        r"If $|q|<1$ and $|a|<1$, then "
        r"$\displaystyle\frac{(-b)_\infty}{(a)_\infty}\sum_{k=0}^{\infty}\frac{(-b/a)^k a^k}{(q)_k}"
        r"=\frac{1}{(b)_\infty}$.",
    ),
    rec(
        "RN-P3-C16-Entry03",
        r"If $a$ is arbitrary and $|q|<1$, then "
        r"$\displaystyle\frac{1}{(aq)_\infty}=\sum_{k=0}^{\infty}\frac{a^k q^{k^2}}{(q,aq;q)_k}$.",
    ),
    rec(
        "RN-P3-C16-Entry04",
        r"If $|abc|<1$, then "
        r"$\displaystyle\frac{(ab)_\infty(ac)_\infty}{(a)_\infty(abc)_\infty}"
        r"\sum_{k=0}^{\infty}\frac{(1/b)_k(1/c)_k(abc)_k}{(q)_k(a)_k}"
        r"=\sum_{k=0}^{\infty}\frac{(1/b)_k(1/c)_k(ab)_k}{(q)_k(c)_k}(abc)^k$.",
    ),
    rec(
        "RN-P3-C16-Entry05",
        r"If $|q|<1$ and $|abcd|<1$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(a/q)_k(1/b)_k(1/c)_k(1/d)_k(1-aq^{2k-1})(abcd)^k}"
        r"{(ab)_k(ac)_k(ad)_k(q)_k(1-a/q)}"
        r"$=\displaystyle\frac{(a)_\infty(abd)_\infty(acd)_\infty(ad)_\infty(abcd)_\infty}"
        r"{(ab)_\infty(ac)_\infty(ad)_\infty(abcd)_\infty}$.",
    ),
    rec(
        "RN-P3-C16-Entry06",
        r"If $|a|<1$, $|c|<1$, and $|q|<1$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(a)_k(b)_k t^k}{(c)_k(d)_k(q)_k}"
        r"$=\displaystyle\frac{(b)_\infty(at)_\infty}{(c)_\infty(t)_\infty}"
        r"\sum_{k=0}^{\infty}\frac{(c/b)_k(at)_k(b)_k t^k}{(at)_k(bt/d)_k(q)_k}\left(\frac{bt}{d}\right)^k$.",
    ),
    rec(
        "RN-P3-C16-Entry07",
        r"If $|q|<1$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(a)_k(d/b)_k(d/e)_k(d/q)_k(1-dq^{2k-1})(be/4)^k q^{k(k-1)}}"
        r"{(b)_k(e)_k(d)_k(q)_k(1-d/q)}"
        r"$=\displaystyle\frac{(a)_\infty(d)_\infty}{(b)_\infty(e)_\infty}"
        r"\sum_{k=0}^{\infty}\frac{(b/a)_k(e/a)_k a^k}{(d/a)_k(q)_k}$.",
    ),
    rec(
        "RN-P3-C16-Entry08",
        r"If $|a|<1$ and $|q|<1$, then "
        r"$\displaystyle\frac{(a)_\infty}{(b)_\infty}\sum_{k=0}^{\infty}\frac{(e/b)_k a^k}{(d)_k(q)_k}"
        r"$=\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(b/a)_k(d/e)_k(ae)^k q^{k(k-1)/2}}{(b)_k(d)_k(q)_k}$.",
    ),
    rec(
        "RN-P3-C16-Entry09",
        r"If $|q|<1$, then "
        r"$\displaystyle\frac{(aq;q)_\infty}{(q;q)_\infty}\sum_{k=0}^{\infty}\frac{q^{k^2}b^k}{(q,aq;q)_k}"
        r"$=\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(b/a)^k a^k q^{k(k+1)/2}}{(q;q)_k}$.",
    ),
    rec(
        "RN-P3-C16-Entry09-Corollary01",
        r"If $|q|<1$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k q^{k(k+1)/2}}{(q;q)_k}"
        r"=(q;q)_\infty\sum_{k=0}^{\infty}\frac{q^{k^2}}{(q;q)_k}$.",
    ),
    rec(
        "RN-P3-C16-Entry09-Corollary02",
        r"If $|q|<1$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k q^{k^2}(1+q^{2k+1})}{(q;q)_{2k+1}}"
        r"$=\displaystyle\frac{(-q;q^2)_\infty}{(q^4;q^4)_\infty(q;q^2)_\infty(q^2;q^4)_\infty}$.",
    ),
    rec(
        "RN-P3-C16-Entry10",
        r"Let $x$, $t$, $m$, and $n$ denote complex numbers. Define "
        r"$P=\dfrac{\Gamma(\tfrac12(x+t-m+n+1))\Gamma(\tfrac12(x+t-m-n+1))"
        r"\Gamma(\tfrac12(x-t+m+n+1))\Gamma(\tfrac12(x-t+m-n+1))}"
        r"{\Gamma(\tfrac12(x-t-m+n+1))\Gamma(\tfrac12(x-t-m-n+1))"
        r"\Gamma(\tfrac12(x+t+m+n+1))\Gamma(\tfrac12(x+t+m-n+1))}$. "
        r"Then, if either $t$, $m$, or $n$ is an integer or if $\operatorname{Re}x>0$, "
        r"$\displaystyle\frac{1-P}{1+P}=\cfrac{2tmx}{x^2+t^2+m^2-n^2-1+"
        r"\cfrac{3(x^2+t^2+m^2-n^2-5)}{4(x^2-1^2)(t^2-1^2)(m^2-1^2)+"
        r"\cfrac{5(x^2+t^2+m^2-n^2-13)}{4(x^2-2^2)(t^2-2^2)(m^2-2^2)+\cdots}}}$.",
    ),
    rec(
        "RN-P3-C16-Entry11",
        r"Suppose that either $q$, $a$, and $b$ are complex numbers with $|q|<1$, or "
        r"$q$, $a$, and $b$ are complex numbers with $a=bq^m$ for some integer $m$. Then "
        r"$\displaystyle\frac{(-a)_\infty(b)_\infty-(a)_\infty(-b)_\infty}"
        r"{(-a)_\infty(b)_\infty+(a)_\infty(-b)_\infty}"
        r"$=\cfrac{a-b}{1-q}+\cfrac{q(a-bq)(aq-b)}{1-q^3}+\cfrac{q(a-bq^2)(aq^2-b)}{1-q^5}+\cdots$.",
    ),
    rec(
        "RN-P3-C16-Entry12",
        r"Suppose that $a$, $b$, and $q$ are complex numbers with $|ab|<1$ and $|q|<1$, "
        r"or that $a=b^{2m+1}$ for some integer $m$. Then "
        r"$\displaystyle\frac{(a^2q^3;q^4)_\infty(b^2q^3;q^4)_\infty}"
        r"{(a^2q;q^4)_\infty(b^2q;q^4)_\infty}"
        r"$=\cfrac{1}{1-ab}+\cfrac{(1-ab)(q^2+1)}{(a-bq)(b-aq)}"
        r"+\cfrac{(1-ab)(q^4+1)}{(a-bq^3)(b-aq^3)}+\cdots$.",
    ),
    rec(
        "RN-P3-C16-Entry13",
        r"If $|q|<1$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{(-a)^k q^{k(k+1)/2}}{(q)_k}"
        r"$=\cfrac{1}{1}+\cfrac{aq}{1-q}+\cfrac{aq^3}{1-q^3}+\cfrac{aq^5}{1-q^5}+\cdots$.",
    ),
    rec(
        "RN-P3-C16-Entry14",
        r"If $\operatorname{Re}\alpha<1$ and $0<a<q^{1-\alpha}$, then "
        r"$\displaystyle\int_0^{\infty}\frac{(-at)_\infty t^{\alpha-1}}{(-t)_\infty}\,dt"
        r"$=\displaystyle\frac{\pi}{(a)_\infty(q^\alpha)_\infty\sin(\pi\alpha)(q)_\infty(aq^{\alpha-1})_\infty}$.",
    ),
    rec(
        "RN-P3-C16-Entry15",
        r"If $|q|<1$, then "
        r"$\displaystyle\frac{f(b,a)}{f(bq,a)}"
        r"$=1+\cfrac{bq}{1-aq}+\cfrac{bq^2}{1-aq^2}+\cfrac{bq^3}{1-aq^3}+\cdots$, "
        r"where $f(b,a)=\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^k(b/a)^k a^k q^{k(k+1)/2}}{(q)_k}$.",
    ),
    rec(
        "RN-P3-C16-Entry15-Corollary",
        r"If $|q|<1$, then "
        r"$\displaystyle\sum_{k=0}^{\infty}\frac{a^k q^{k^2}}{(q)_k}"
        r"$=1+\cfrac{aq}{1-aq}+\cfrac{aq^2}{1-aq^2}+\cfrac{aq^3}{1-aq^3}+\cdots$.",
    ),
    rec(
        "RN-P3-C16-Entry16",
        r"For each positive integer $n$, let "
        r"$J_n=J_n(a,q)=\displaystyle\sum_{k=0}^{\lfloor(n+1)/2\rfloor}"
        r"\frac{a^k q^{k^2}(q)_n}{(q)_k(q)_{n-2k+1}}$ and $v_n=J_n(aq,q)$. Then "
        r"$\displaystyle\frac{J_n}{v_n}=1+\cfrac{aq}{1}+\cfrac{aq^2}{1}+\cdots+\cfrac{aq^n}{1}$.",
    ),
    rec(
        "RN-P3-C16-Entry17",
        r"If $|\beta q|<|z|<|1/(\alpha q)|$, then "
        r"$\displaystyle\sum_{k=-\infty}^{\infty}\frac{(\alpha)_k z^k}{(\beta)_k}"
        r"$=\displaystyle\frac{(z;q)_\infty(\alpha q/z;q)_\infty(q;q)_\infty(\beta/\alpha;q)_\infty}"
        r"{(\beta z;q)_\infty(\beta q/\alpha z;q)_\infty(\alpha q;q)_\infty(\beta/\alpha z;q)_\infty}$.",
    ),
    rec(
        "RN-P3-C16-Entry17-Corollary",
        r"If $|nq|<|z|<|1/(nq)|$, then "
        r"$1+2\displaystyle\sum_{k=1}^{\infty}\frac{(1/n;q^2)_k(-nq)_k}{(nq^2;q^2)_k}(z^k+z^{-k})"
        r"$=\displaystyle\frac{(-qz;q^2)_\infty(-q/z;q^2)_\infty(q^2;q^2)_\infty(n^2q^2;q^2)_\infty}"
        r"{(-nqz;q^2)_\infty(-nq/z;q^2)_\infty(nq^2;q^2)_\infty}$.",
    ),
    rec(
        "RN-P3-C16-Entry18",
        r"For $|ab|<1$, define "
        r"$f(a,b)=\displaystyle\sum_{k=-\infty}^{\infty}a^{k(k+1)/2}b^{k(k-1)/2}$. Then "
        r"(i) $f(a,b)=f(b,a)$; (ii) $f(1,a)=2f(a,a^3)$; (iii) $f(-1,a)=0$; and, if $n$ is an integer, "
        r"(iv) $f(a,b)=a^{n(n+1)/2}b^{n(n-1)/2}f(a(ab^n)^{n+1},b(ab^{-n})^{n-1})$.",
    ),
    rec(
        "RN-P3-C16-Entry19",
        r"If $|ab|<1$, then "
        r"$f(a,b)=(-a;b)_\infty(-b;a)_\infty(ab;ab)_\infty$.",
    ),
    rec(
        "RN-P3-C16-Entry20",
        r"If $\alpha\beta=\pi$, $\operatorname{Re}(\alpha^2)>0$, and $n$ is any complex number, then "
        r"$\displaystyle\sqrt{\alpha}\,f(e^{-\alpha^2+n\alpha},e^{-\alpha^2-n\alpha})"
        r"=e^{n^2/4}\sqrt{\beta}\,f(e^{-\beta^2+n\beta},e^{-\beta^2-n\beta})$.",
    ),
    rec(
        "RN-P3-C16-Entry21",
        r"If $|q|<1$, $|a|<1$, and $|b|<1$, then "
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{(-1)^{k-1}a^k}{k(1-q^k)}"
        r"=\log\frac{(-aq;q)_\infty}{(-a;q)_\infty}$ "
        r"and "
        r"$\displaystyle\sum_{k=1}^{\infty}\frac{(-1)^{k-1}a^k b^k}{k(1-q^k)}"
        r"=\log\frac{f(-a,-b)}{f(-aq,-bq)}$.",
    ),
    rec(
        "RN-P3-C16-Entry22i",
        r"If $|q|<1$, then "
        r"$\displaystyle\varphi(q):=f(q,q)=1+2\sum_{k=1}^{\infty}q^{k^2}"
        r"$=\displaystyle\frac{(-q;q^2)_\infty(q^2;q^2)_\infty}{(q;q^2)_\infty(-q^2;q^2)_\infty}$.",
    ),
    rec(
        "RN-P3-C16-Entry22ii",
        r"If $|q|<1$, then "
        r"$\displaystyle\psi(q):=f(q,q^3)=\sum_{k=0}^{\infty}q^{k(k+1)/2}"
        r"$=\displaystyle\frac{(q^2;q^2)_\infty}{(q;q^2)_\infty}$.",
    ),
    rec(
        "RN-P3-C16-Entry22iii",
        r"If $|q|<1$, then "
        r"$\displaystyle f(-q):=f(-q,-q^2)=\sum_{k=0}^{\infty}(-1)^k q^{k(3k-1)/2}"
        r"+\sum_{k=1}^{\infty}(-1)^k q^{k(3k+1)/2}=(q;q)_\infty$.",
    ),
    rec(
        "RN-P3-C16-Entry22iv",
        r"If $|q|<1$, define "
        r"$\displaystyle\chi(q):=\frac{f(-q,q)}{f(-q,-q^2)}=\frac{(-q;q^2)_\infty}{(q;q^2)_\infty}$.",
    ),
    rec(
        "RN-P3-C16-Entry23",
        r"For $|q|<1$, "
        r"(i) $\displaystyle\log\varphi(q)=2\sum_{k=1}^{\infty}\frac{q^{2k-1}}{(2k-1)(1+q^{2k-1})}$; "
        r"(ii) $\displaystyle\log\psi(q)=\sum_{k=1}^{\infty}\frac{(-1)^{k-1}q^{k(k+1)/2}}{k(1-q^k)}$; "
        r"(iii) $\displaystyle\log f(-q)=\sum_{k=1}^{\infty}\frac{q^{k(3k-1)/2}}{k}"
        r"+\sum_{k=1}^{\infty}\frac{(-1)^{k-1}q^{k(3k+1)/2}}{k}$; "
        r"(iv) $\displaystyle\log\chi(q)=\sum_{k=1}^{\infty}\frac{(-1)^{k-1}q^k}{k(1+q^k)}$; and "
        r"(v) $\displaystyle\frac{\psi(q)}{\varphi(q)}=\frac{(-q^2;q^2)_\infty}{(-q;q^2)_\infty}$.",
    ),
    rec(
        "RN-P3-C16-Entry23-Example",
        r"With $q=\tfrac{1}{10}$, "
        r"$\displaystyle\frac{1}{1}+\frac{1}{10}+\frac{1}{110}+\frac{1}{1110}+\cdots"
        r"$=1.101001000100001\ldots$.",
    ),
    rec(
        "RN-P3-C16-Entry24",
        r"We have "
        r"(i) $\displaystyle\frac{f(q)}{\varphi(q)}=\frac{\psi(q)}{\chi(q)}"
        r"$=\displaystyle\frac{\varphi(-q)}{f(-q)}=\frac{\psi(-q)}{\chi(-q)}$; "
        r"(ii) $f^3(-q)=\varphi^2(-q)\psi(q)=\displaystyle\sum_{k=0}^{\infty}(-1)^k(2k+1)q^{k(k+1)/2}$; "
        r"(iii) $\displaystyle\frac{\chi(q)}{f(q)}=\frac{3\varphi(q)}{\psi(-q)}"
        r"$=\displaystyle\frac{\varphi(q)}{f(-q^2)}=\frac{f(q)}{\psi(-q)}$; "
        r"(iv) $f^3(-q^2)=\varphi(-q)\psi^2(q)$; and "
        r"$\chi(q)\chi(-q)=\chi(-q^2)$.",
    ),
    rec(
        "RN-P3-C16-Entry25",
        r"We have "
        r"(i) $\varphi(q)+\varphi(-q)=2\varphi(q^4)$; "
        r"(ii) $\varphi(q)-\varphi(-q)=4q\psi(q^8)$; "
        r"(iii) $\varphi(q)\varphi(-q)=\varphi^2(-q^2)$ and $\psi(q)\psi(-q)=\psi(q^2)\varphi(-q^2)$; "
        r"(iv) $\varphi(q)\psi(q^2)=f^2(q)$; "
        r"(v) $\varphi^2(q)-\varphi^2(-q)=8q\psi^2(q^4)$; "
        r"(vi) $\varphi^2(q)+\varphi^2(-q)=2\varphi^2(q^2)$; and "
        r"(vii) $\varphi^4(q)-\varphi^4(-q)=16q\psi^4(q^2)$.",
    ),
    rec(
        "RN-P3-C16-Entry25-Corollary",
        r"If $\displaystyle\frac{\varphi^2(-q)}{\varphi^2(q)}=\frac{1-t}{1+t}$, then "
        r"$\displaystyle\frac{\varphi^4(-q^2)}{\varphi^4(q^2)}=1-t$.",
    ),
    rec(
        "RN-P3-C16-Entry26",
        r"For $m,n>0$, let $G(q)=q^{(m-n)^2/(8(m+n))}f(q^m,q^n)$. "
        r"Then $G(q)$ is a perfect, complete, pure, double series of $\tfrac12$ degree.",
    ),
    rec(
        "RN-P3-C16-Entry26-Corollary01",
        r"$\varphi(q)$, $\sqrt[4]{q}\,\psi(q)$, and $2\sqrt{q}\,f(q)$ are complete series of $\tfrac12$ degree.",
    ),
    rec(
        "RN-P3-C16-Entry26-Corollary02",
        r"$\chi(q)/\sqrt{q}$ is a complete series of $0$ degree.",
    ),
    rec(
        "RN-P3-C16-Entry27",
        r"Assume that $\alpha$ and $\beta$ are such that the modulus of each exponential argument below is less than $1$. "
        r"If $\alpha\beta=\pi$, then "
        r"(i) $\displaystyle\frac{\alpha^{1/4}}{\beta^{1/4}}e^{-\pi\alpha^2/(4\beta)}\varphi(e^{-\pi\alpha^2/\beta})"
        r"$=e^{\pi\beta/4}\varphi(e^{-\pi\beta})$; "
        r"(ii) $\displaystyle\frac{\alpha^{1/4}}{\beta^{1/4}}"
        r"\exp\!\left(-\frac{\pi\alpha^2}{12\beta}\right)"
        r"\bigl\{\varphi(e^{-\pi\alpha^2/(3\beta)})-\varphi(-e^{-\pi\alpha^2/\beta})\bigr\}"
        r"$=\exp\!\left(\frac{\pi\beta}{12}\right)"
        r"\bigl\{\varphi(e^{-\pi\beta/3})-\varphi(-e^{-\pi\beta})\bigr\}$; "
        r"If $\alpha\beta=\pi^2$, then "
        r"(iii) $\displaystyle e^{-\pi i\alpha/12}\sqrt[4]{\beta}\,f(\sqrt{\beta}\,e^{-2\pi i\alpha})"
        r"$=e^{-\pi\beta/12}\sqrt[4]{\alpha}\,f(-e^{-2\pi\beta})$; "
        r"(iv) $\displaystyle e^{-\pi i\alpha/24}\sqrt[4]{\beta}\,f(e^{-\pi i\alpha})"
        r"$=e^{-\pi\beta/24}\sqrt[4]{\alpha}\,f(e^{-\pi\beta})$; and "
        r"(v) $\displaystyle\frac{e^{-\pi i\alpha/24}\chi(e^{-\pi i\alpha})}{f(e^{-\pi i\alpha})}"
        r"$=\displaystyle\frac{e^{-\pi\beta/24}\chi(e^{-\pi\beta})}{f(e^{-\pi\beta})}$.",
    ),
    rec(
        "RN-P3-C16-Entry28",
        r"If $\rho=ab$ and $n$ is any natural number, then "
        r"$\displaystyle\prod_{k=1}^{n}(-ap^{k-1};p^n)_\infty(-bp^{n-k};p^n)_\infty(p^n;p^n)_\infty"
        r"$=\displaystyle\prod_{k=1}^{n}f(ap^{k-1},bp^{n-k})$.",
    ),
    rec(
        "RN-P3-C16-Entry28-Corollary",
        r"We have "
        r"$f(-q^2,-q^3)f(-q,-q^4)=f(-q)f(-q^5)$ and "
        r"$\displaystyle\prod_{k=1}^{n}f(-q^k,-q^{2n+1-k})=f(-q)^{n-1}f(-q^{2n+1})$ for each positive integer $n$.",
    ),
    rec(
        "RN-P3-C16-Entry29",
        r"If $ab=cd$, then "
        r"(i) $f(a,b)f(c,d)+f(-a,-b)f(-c,-d)=2f(ac,bd)f(ad,bc)$ and "
        r"(ii) $f(a,b)f(c,d)-f(-a,-b)f(-c,-d)"
        r"$=2af\!\left(\frac{c}{a},\frac{1}{abcd}\right)f\!\left(\frac{d}{b},\frac{1}{abcd}\right)$.",
    ),
    rec(
        "RN-P3-C16-Entry30",
        r"We have "
        r"(i) $f(a,ab^2)f(b,a^2b)=f(a,b)\psi(ab)$; "
        r"(ii) $f(a,b)+f(-a,-b)=2f(a^3b,ab^3)$; "
        r"(iii) $f(a,b)-f(-a,-b)=2af\!\left(\frac{b}{a},\frac{1}{a^4b^4}\right)$; "
        r"(iv) $f(a,b)f(-a,-b)=f(-a^2,-b^2)\varphi(-ab)$; "
        r"(v) $f^2(a,b)+f^2(-a,-b)=2f(a^2,b^2)\varphi(ab)$; and "
        r"(vi) $f^2(a,b)-f^2(-a,-b)=4af\!\left(\frac{b}{a},\frac{1}{a^2b^2}\right)\psi(a^2b^2)$.",
    ),
    rec(
        "RN-P3-C16-Entry30-Corollary",
        r"If $ab=cd$, then "
        r"$f(a,b)f(c,d)f(a^{1/n},b^{1/n})f(c^{1/n},d^{1/n})"
        r"-f(-a,-b)f(-c,-d)f(-a^{1/n},-b^{1/n})f(-c^{1/n},-d^{1/n})$"
        r"$=2af\!\left(\frac{c}{a},ad\right)f\!\left(\frac{d}{a^n},a^{1-n}d\right)f\!\left(n,\frac{ab}{n}\right)\psi(ab)$.",
    ),
    rec(
        "RN-P3-C16-Entry31",
        r"Let $U_n=a^{n(n+1)/2}b^{n(n-1)/2}$ and $V_n=a^{n(n-1)/2}b^{n(n+1)/2}$ for each integer $n$. Then "
        r"$\displaystyle f\!\left(\frac{U_1}{U_n},\frac{V_1}{V_n}\right)"
        r"$=\displaystyle\sum_{r=0}^{n-1}\frac{U_r}{U_n}f\!\left(\frac{U_{n+r}}{U_r},\frac{V_{n-r}}{V_r}\right)$.",
    ),
    rec(
        "RN-P3-C16-Entry31-Corollary",
        r"We have "
        r"(i) $\varphi(q)=\varphi(q^9)+2qf(q^3,q^{15})=\varphi(q^{25})+2qf(q^{15},q^{35})+2q^4f(q^5,q^{45})$; and "
        r"(ii) $\psi(q)=f(q^3,q^6)+q\psi(q^9)=f(q^6,q^{10})+qf(q^2,q^{14})"
        r"$=f(q^{10},q^{15})+qf(q^5,q^{20})+q^3\psi(q^{25})=f(q^{15},q^{21})+q\psi(q^9)+q^3f(q^3,q^{33})$.",
    ),
    rec(
        "RN-P3-C16-Entry31-Example01",
        r"We have "
        r"$\displaystyle\frac{\varphi^2(q)}{\varphi^2(-q)}+\frac{\varphi^2(r)}{\varphi^2(-r)}+\frac{\varphi^2(s)}{\varphi^2(-s)}"
        r"+\frac{\varphi^2(q)\varphi^2(r)\varphi^2(s)}{\varphi^2(-q)\varphi^2(-r)\varphi^2(-s)}"
        r"$=\displaystyle\frac{\varphi^2(q^2)\varphi^2(r^2)\varphi^2(s^2)\psi^2(q^4)\psi^2(r^4)\psi^2(s^4)}"
        r"{256qrs\,\varphi^2(-q)\varphi^2(-r)\varphi^2(-s)}$.",
    ),
    rec(
        "RN-P3-C16-Entry31-Example02",
        r"We have "
        r"$\displaystyle\frac{1}{\varphi(q^4)}=\frac{1}{\varphi(q)}\pm\frac{1}{\varphi(q^2)}+\frac{1}{\varphi(-q)}\pm\frac{1}{\varphi(q^2)}$ "
        r"and "
        r"$\displaystyle\frac{1}{\varphi(-q^2)}=\frac{1}{\varphi(-q^2)\pm\varphi(q)}+\frac{1}{\varphi(-q^2)\pm\varphi(-q)}$.",
    ),
    rec(
        "RN-P3-C16-Entry31-Example03",
        r"For each natural number $n$, the coefficient of $q^n$ in the expansion of "
        r"$\displaystyle\frac{q}{1-q}\,\psi(q^2)$ is the integer nearest to $\sqrt{n}$.",
    ),
    rec(
        "RN-P3-C16-Entry31-Example04",
        r"We have "
        r"$\displaystyle\frac{f(q,q^7)}{f(q^3,q^5)}=\frac{\varphi(-q)-\varphi(q)}{-2q\,\psi(q)}$.",
    ),
    rec(
        "RN-P3-C16-Entry31-Example05",
        r"We have $f(q,q^5)=\psi(-q^3)\chi(q)$.",
    ),
    rec(
        "RN-P3-C16-Entry32",
        r"We have "
        r"(i) $\displaystyle\frac{\varphi'(q)}{\varphi(q)}-\frac{\psi'(q)}{\psi(q)}=\frac{1-\varphi^4(-q)}{8q}$; "
        r"(ii) $\displaystyle\frac{\psi'(q)}{\psi(q)}-\frac{\psi'(q^2)}{2q\,\psi(q^2)}=\frac{1-\varphi^4(-q)}{8q}$; "
        r"(iii) $\displaystyle\frac{\varphi'(q)}{\varphi(q)}+\frac{\varphi'(-q)}{\varphi(-q)}"
        r"$=\displaystyle\frac{\varphi^4(q)-\varphi^4(-q)}{4q}$; and "
        r"(iv) $\displaystyle\frac{\psi'(q)}{\psi(q)}+\frac{\psi'(-q)}{\psi(-q)}"
        r"$=\displaystyle\frac{2\psi'(-q^2)}{\psi(-q^2)}$.",
    ),
    rec(
        "RN-P3-C16-Entry33i",
        r"If $|q|<1$ and $\theta$ is real, then "
        r"$\displaystyle\log\left[1+2\sum_{k=1}^{\infty}q^{k^2}\cos(k\theta)\right]"
        r"$=2\sum_{k=1}^{\infty}\frac{(-1)^{k-1}q^k}{k(1-q^{2k})}\cos(k\theta)$.",
    ),
    rec(
        "RN-P3-C16-Entry33ii",
        r"If $|q|<1$ and $\eta$ is real, then "
        r"$\displaystyle\log\left[\frac{\sum_{k=1}^{\infty}(-1)^{k-1}q^{k(k-1)/2}\sin((2k-1)\eta)}{\sin\eta}\right]"
        r"$=4\sum_{k=1}^{\infty}\frac{(-1)^{k-1}(2k-1)q^{k(k-1)/2}}{k(1-q^k)}$.",
    ),
    rec(
        "RN-P3-C16-Entry33iii",
        r"If $|q|<1$ and $\eta$ is real, then "
        r"$\displaystyle\frac{1+2\sum_{k=1}^{\infty}q^{k^2}\cos(2k\eta)}"
        r"{1+4\sum_{k=1}^{\infty}\frac{q^k\cos(2k\eta)}{1+q^{2k}}}"
        r"$=\displaystyle\frac{1+2\sum_{k=1}^{\infty}(-1)^k q^{k^2}\cos(2k\eta)}"
        r"{1+4\sum_{k=1}^{\infty}\frac{q^k\cos(2k\eta)}{1+q^{2k}}}$.",
    ),
    rec(
        "RN-P3-C16-Entry33-Corollary",
        r"If $|a|<1$ and $|b|<1$, then "
        r"$\displaystyle\frac{f(a,b)}{f(-a,-b)}"
        r"$=1+2\sum_{k=1}^{\infty}\frac{a^k+b^k}{1+a^kb^k}$.",
    ),
    rec(
        "RN-P3-C16-Entry34i",
        r"If $|q|<1$ and $\eta$ is real, then "
        r"$\displaystyle\log\left[\frac{(-e^{2i\eta}q;q^2)_\infty(-e^{-2i\eta}q;q^2)_\infty}"
        r"{(-e^{2i\eta}q^2;q^2)_\infty(-e^{-2i\eta}q^2;q^2)_\infty}"
        r"\cdot\frac{1+4\sum_{k=1}^{\infty}\frac{q^{2k-1}\cos((2k-1)\eta)}{1-q^{2k-1}}}{1+4\cos\eta}\right]"
        r"$=4\sum_{k=1}^{\infty}\frac{(-1)^{k-1}q^k\sin^2(k\eta)}{k(1+q^k)}$.",
    ),
    rec(
        "RN-P3-C16-Entry34ii",
        r"If $|q|<1$ and $\eta$ is real, then "
        r"$\displaystyle\log\left[\frac{\varphi^2(q)}{1+4\sum_{k=1}^{\infty}\frac{q^k\cos(2k\eta)}{1+q^{2k}}}\right]"
        r"$=\displaystyle\sum_{k=1}^{\infty}\frac{q^{2k-1}\sin^2((2k-1)\eta)}{(2k-1)(1-q^{4k-2})}$.",
    ),
    rec(
        "RN-P3-C16-Entry34-Corollary01",
        r"If $|q|<1$ and $z=e^{2i\eta}$ with $\eta$ real, then "
        r"$\displaystyle\log\left[\frac{\sum_{k=-\infty}^{\infty}q^{3k^2-2k}\sin\{2(3k-1)\eta\}}{\sin(2\eta)\sum_{k=-\infty}^{\infty}(3k-1)q^{3k^2-2k}}\right]"
        r"$=\displaystyle\sum_{k=1}^{\infty}\frac{q^k\sin^2(k\eta)}{k(1-q^{2k})}"
        r"+\displaystyle\sum_{k=1}^{\infty}\frac{q^{4k}\sin^2(2k\eta)}{k(1-q^{4k})}$.",
    ),
    rec(
        "RN-P3-C16-Entry34-Corollary02",
        r"If $|q|<1$ and $z=e^{2i\eta}$ with $\eta$ real, then "
        r"$\displaystyle\log\left[\frac{\sum_{k=1}^{\infty}(-q)^{(k-1)/2}\cos((2k-1)\eta)}{\cos\eta}\right]"
        r"$=\displaystyle\sum_{k=1}^{\infty}\frac{q^k\sin^2(k\eta)}{k(1+q^k)}"
        r"+\displaystyle\sum_{k=1}^{\infty}\frac{q^{4k}\sin^2(2k\eta)}{k(1-q^{4k})}$.",
    ),
    rec(
        "RN-P3-C16-Entry34-Corollary03",
        r"If $|q|<1$ and $z=e^{2i\eta}$ with $\eta$ real, then "
        r"$\displaystyle\log\left[\frac{\sum_{k=-\infty}^{\infty}q^{(3k^2+k)/2}\sin((6k+1)\eta)}{\sin\eta\sum_{k=-\infty}^{\infty}(6k+1)q^{(3k^2+k)/2}}\right]"
        r"$=\displaystyle\sum_{k=1}^{\infty}\frac{q^k\sin^2(k\eta)}{k(1-q^k)}"
        r"+\displaystyle\sum_{k=1}^{\infty}\frac{q^k\sin^2(2k\eta)}{2k(1-q^{2k})}$.",
    ),
    rec(
        "RN-P3-C16-Entry34-Corollary04",
        r"If $|q|<1$ and $z=e^{2i\eta}$ with $\eta$ real, then "
        r"$\displaystyle\log\left[\frac{4\cos\eta}{\varphi^2(-q)\sum_{k=-\infty}^{\infty}\frac{(-1)^k q^k\cos((2k+1)\eta)}{1+2q^{2k}\cos(2\eta)+q^{4k}}}\right]"
        r"$=\displaystyle\sum_{k=1}^{\infty}\frac{q^k\sin^2(k\eta)}{k(1-q^k)}"
        r"+\displaystyle\sum_{k=1}^{\infty}\frac{q^k\sin^2(2k\eta)}{k(1+q^k)}$.",
    ),
    rec(
        "RN-P3-C16-Entry35i",
        r"For each positive integer $n$, let "
        r"$P_n=-\dfrac{B_n}{2n}+\displaystyle\sum_{k=1}^{\infty}\frac{(-1)^{k+1}k^{n-1}q^k}{k(1-q^k)}$, "
        r"where $B_n$ denotes the $n$th Bernoulli number. For each nonnegative integer $n$, let "
        r"$Q_n=\dfrac{1}{n+1}\displaystyle\sum_{k=1}^{\infty}\frac{(-1)^{k+1}(2k-1)^{2n+1}q^{k(k-1)/2}}{k}$. "
        r"Then for each positive integer $n$, "
        r"$\displaystyle\sum_{j=1}^{n}\binom{2n-1}{2j-1}2^{2j+1}P_{2j}Q_{2n-2j}=2Q_{2n}$.",
    ),
    rec(
        "RN-P3-C16-Entry35ii",
        r"For each positive integer $n$, let "
        r"$P_n=\dfrac{(1-2n)B_n}{2n}+\displaystyle\sum_{k=1}^{\infty}\frac{(-1)^{k+1}k^{n-1}q^k}{k(1+q^k)}$, "
        r"where $B_n$ denotes the $n$th Bernoulli number. For each nonnegative integer $n$, define "
        r"$Q_{2n}$ by $\displaystyle\sec x=\sum_{n=0}^{\infty}\frac{(-1)^n E_{2n}}{(2n)!}x^{2n}$, "
        r"where $E_{2n}$ denotes the $2n$th Euler number. If $n$ is any positive integer, then "
        r"$\displaystyle\sum_{k=1}^{n}\binom{2n-1}{2k-1}2^{2k}P_{2k}Q_{2n-2k}=2Q_{2n}$.",
    ),
    rec(
        "RN-P3-C16-Entry35-Example01",
        r"Let $Q_n$, $n\ge 2$, be defined as in Entry 35(i). Let "
        r"$L=1-24\displaystyle\sum_{k=1}^{\infty}\frac{kq^k}{1-q^k}$, "
        r"$M=1+240\displaystyle\sum_{k=1}^{\infty}\frac{k^3q^k}{1-q^k}$, and "
        r"$N=1-504\displaystyle\sum_{k=1}^{\infty}\frac{k^5q^k}{1-q^k}$. Then $3Q_2=L$.",
    ),
    rec(
        "RN-P3-C16-Entry35-Example02",
        r"With $Q_n$, $L$, $M$, and $N$ as in Entry 35-Example01, "
        r"$5Q_4=\dfrac{5L^2-2M}{3}$.",
    ),
    rec(
        "RN-P3-C16-Entry35-Example03",
        r"With $Q_n$, $L$, $M$, and $N$ as in Entry 35-Example01, "
        r"$7Q_6=\dfrac{35L^3-42ML+16N}{9}$.",
    ),
    rec(
        "RN-P3-C16-Entry36",
        r"If $p=ab/(cd)$, then "
        r"(i) $\displaystyle S:=\tfrac12\{f(a,b)f(c,d)+f(-a,-b)f(-c,-d)\}"
        r"$=\displaystyle\sum_{k=-\infty}^{\infty}(ad)^{k(k+1)/2}(bc)^{k(k-1)/2}"
        r"f\!\left(acp^k,\frac{b}{d}p^k\right)$; and "
        r"(ii) $\displaystyle D:=\tfrac12\{f(a,b)f(c,d)-f(-a,-b)f(-c,-d)\}"
        r"$=\displaystyle\sum_{k=-\infty}^{\infty}a^{2k+1}(ad)^{k(k-1)/2}(bc)^{k(k+1)/2}"
        r"f\!\left(\frac{a}{c}p^k,\frac{ap^k}{cd}\right)$.",
    ),
    rec(
        "RN-P3-C16-Entry37",
        r"We have "
        r"(i) $\displaystyle\tfrac12\{\varphi(a)\varphi(b)+\varphi(-a)\varphi(-b)\}"
        r"$=\varphi(ab)+2\displaystyle\sum_{k=1}^{\infty}(ab)^{k^2}"
        r"f\!\left(\frac{ab}{a^{2k}},\frac{ab}{b^{2k}}\right)$; "
        r"(ii) $\displaystyle\tfrac12\{\varphi(a)\varphi(b)-\varphi(-a)\varphi(-b)\}"
        r"$=2\displaystyle\sum_{k=1}^{\infty}a^{k^2}b^{(k-1)^2}"
        r"f\!\left(\frac{a^{2k-1}b^{2k-1}}{a^{2k}},\frac{a^{2k-1}b^{2k-1}}{b^{2k}}\right)$; and "
        r"(iii) $\displaystyle\psi(a)\psi(b)=\psi(ab)+\sum_{k=1}^{\infty}a^{k(k+1)/2}b^{k(k-1)/2}"
        r"f\!\left(\frac{ab}{a^{2k}},\frac{ab}{b^{2k}}\right)$.",
    ),
    rec(
        "RN-P3-C16-Entry37-Corollary",
        r"We have "
        r"(i) $\psi(q^3)\psi(q^{13})-\psi(-q^3)\psi(-q^{13})"
        r"$=q^3\{\psi(q)\psi(q^{39})+\psi(-q)\psi(-q^{39})\}$; "
        r"(ii) $\psi(q^5)\psi(q^{11})-\psi(-q^5)\psi(-q^{11})"
        r"$=q^5\{\psi(q)\psi(q^{55})+\psi(-q)\psi(-q^{55})\}$; and "
        r"(iii) $\psi(q^7)\psi(q^9)-\psi(-q^7)\psi(-q^9)"
        r"$=q^7\{\psi(q)\psi(q^{63})+\psi(-q)\psi(-q^{63})\}$.",
    ),
    rec(
        "RN-P3-C16-Entry37-Example",
        r"We have "
        r"$\displaystyle\frac{\psi(q)\psi(q^5)-\psi(-q)\psi(-q^5)}"
        r"{2q^{15}\psi(q^6)\psi(q^{120})}"
        r"$=\dfrac{\varphi(-q^6)\varphi(-q^{120})}{\varphi(-q)\varphi(-q^{40})}"
        r"$-\dfrac{\varphi(-q)\varphi(-q^{40})}{\varphi(-q^6)\varphi(-q^{120})}$.",
    ),
    rec(
        "RN-P3-C16-Entry38i",
        r"For $|q|<1$, "
        r"$\displaystyle\frac{f(-q^5)}{f(-q^2,-q^3)}=\sum_{k=0}^{\infty}\frac{q^{k^2}}{(q)_k}$.",
    ),
    rec(
        "RN-P3-C16-Entry38ii",
        r"For $|q|<1$, "
        r"$\displaystyle\frac{f(-q^5)}{f(-q,-q^4)}=\sum_{k=0}^{\infty}\frac{q^{k(k+1)}}{(q)_k}$.",
    ),
    rec(
        "RN-P3-C16-Entry38iii",
        r"For $|q|<1$, "
        r"$\displaystyle\frac{f(-q,-q^4)}{f(-q^2,-q^3)}"
        r"$=\cfrac{1}{1}+\cfrac{q}{1}+\cfrac{q^2}{1}+\cfrac{q^3}{1}+\cdots$.",
    ),
    rec(
        "RN-P3-C16-Entry38iv",
        r"For $|q|<1$, "
        r"$\displaystyle\frac{f^2(-q^2,-q^3)}{q^{2/5}f^2(-q,-q^4)}"
        r"$=f(-q)\{f(-q^{1/5})+q^{1/5}f(-q^5)\}$.",
    ),
    rec(
        "RN-P3-C16-Entry39",
        r"If $\alpha,\beta>0$ and $\alpha\beta=\pi^2$, then "
        r"(i) $\displaystyle\left\{\sqrt{5}+\cfrac{1+\dfrac{e^{-2\alpha/5}}{1+\dfrac{e^{-4\alpha/5}}{1+\cdots}}}"
        r"{\sqrt{5}+\cfrac{e^{-2\beta/5}}{1+\dfrac{e^{-4\beta/5}}{1+\cdots}}}\right\}^2"
        r"$=\dfrac{5+\sqrt{5}}{2}$; and "
        r"(ii) $\displaystyle\left\{\sqrt{5}-\cfrac{1+\dfrac{e^{-\alpha/5}}{1-\dfrac{e^{-2\alpha/5}}{1-\cdots}}}"
        r"{\sqrt{5}-\cfrac{e^{-\beta/5}}{1-\dfrac{e^{-2\beta/5}}{1-\cdots}}}\right\}^2"
        r"$=\dfrac{5-\sqrt{5}}{2}$.",
    ),
    rec(
        "RN-P3-C16-Entry39-Corollary01",
        r"We have "
        r"$\displaystyle\cfrac{e^{-2\pi/5}}{1+\dfrac{e^{-4\pi/5}}{1+\dfrac{e^{-6\pi/5}}{1+\cdots}}}"
        r"$=\sqrt{\dfrac{5+\sqrt{5}}{2}}-\sqrt{\dfrac{5-\sqrt{5}}{2}}$.",
    ),
    rec(
        "RN-P3-C16-Entry39-Corollary02",
        r"We have "
        r"$\displaystyle\cfrac{e^{-\pi/5}}{1-\dfrac{e^{-2\pi/5}}{1-\dfrac{e^{-3\pi/5}}{1-\cdots}}}"
        r"$=\sqrt{\dfrac{5-\sqrt{5}}{2}}$.",
    ),
]
