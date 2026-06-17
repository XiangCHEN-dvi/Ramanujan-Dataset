"""Part 4, Chapter 30 entries — curated LaTeX."""

from __future__ import annotations

TOPICS = ['partial-fraction-expansions']


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS}


CHAPTER_30 = [

    rec(
        "RN-P4-C30-Entry01",
        r"Let $\varphi(z)$ be entire, $\alpha\beta=\pi^2$ with $\alpha,\beta>0$, and $\displaystyle f(z)=\frac{\alpha^\alpha\Gamma(z+1)\zeta(z)\varphi(z)\sin(\pi z)}{(2\pi)^z\Gamma(3z+1)}$ tend to $0$ as $|z|\to\infty$. Then $\displaystyle f(z)=\varphi(0)\left\{\frac{1}{z}-\frac{1}{1-z}\right\}+\sum_{n=1}^\infty\frac{\alpha^{2n}\varphi(2n)B_{2n}}{(z-2n)\,n!}+\sum_{n=0}^\infty\frac{(-1)^n\beta^{2n+1}\varphi(-2n-1)}{(2n+1+z)(n+1)!}$.",
    )
,
    rec(
        "RN-P4-C30-Entry02",
        r"Let $\varphi(z)$ be entire and $\displaystyle f(z)=\frac{\alpha^\alpha\Gamma(z+1)\zeta(z)\varphi(z)\sin(\pi z)}{(2\pi)^z}$ with $f(z)\to0$ as $|z|\to\infty$. Then $\displaystyle f(z)=-\varphi(0)+\sum_{n=1}^\infty\frac{(-1)^n\alpha^{2n}B_{2n}\varphi(2n)}{z-2n}+\sum_{n=1}^\infty\frac{(-1)^{n-1}(n+1)\varphi(-n)}{n!\,(z+n)}$.",
    )
,
    rec(
        "RN-P4-C30-Entry03",
        r"$\displaystyle\frac{1}{\sin^2(\pi z)(e^{2\pi z}-1)}=\frac{1}{2\pi z^2}+\frac{1}{2z^3}+\sum_{n=1}^\infty\left\{\frac{1}{(e^{2\pi n}-1)(z^2-n^2)}+\frac{2z}{(e^{2\pi n}-1)(z^2-n^2)^2}+\frac{1}{\sinh^2(\pi n)(z^2-n^2)}\right\}$.",
    )
,
    rec(
        "RN-P4-C30-Entry04",
        r"$\displaystyle\frac{n\sinh(nz\sqrt3)\sinh(\pi z)+\sin(\pi z\sqrt3)\sin(\pi z)}{z^2\sqrt3(\cosh(\pi z\sqrt3)-\cos(\pi z))(\cosh(\pi z)-\cos(\pi z\sqrt3))}=\frac{1}{2z^2}+\sum_{n=1}^\infty\left\{\frac{n\coth(\pi n)}{z^2+n^2\sqrt3}+\frac{n\coth(\pi n\sqrt3)}{z^2-n^2\sqrt3}\right\}$.",
    )
,
    rec(
        "RN-P4-C30-Entry05",
        r"For real $m$ and complex $n\ne0$, with $z=1/n$, $\displaystyle\frac{\sec(\pi m z)}{2z(e^{2\pi i m z}-1)}=\frac{1}{2z}+\sum_{k=1}^\infty\frac{\sech(\pi m k)}{4z^2+4k^2}-2\sum_{k=0}^\infty\frac{(-1)^k}{(2k+1)(e^{(2k+1)\pi i/m}-1)(m^2z^2-(2k+1)^2)}$.",
    )
,
    rec(
        "RN-P4-C30-Entry06",
        r"For complex $\alpha,\beta$, $\displaystyle\frac{\pi\alpha\beta}{(e^{2\pi\alpha}-1)(\alpha^2+(\beta+n)^2)(\alpha^2+(\beta-n)^2)}=\frac{\pi\cosh(2\pi(\alpha-\beta))-\cos(2\pi(\alpha-\beta))}{2(\cosh(2\pi\alpha)-\cos(2\pi\beta))(\cosh(2\pi\beta)-\cos(2\pi\alpha))}-\sum_{n=1}^\infty\left\{\frac{1}{(e^{2\pi n}-1)(\alpha^2+(n-\beta)^2)(\alpha^2+(n+\beta)^2)}+\frac{2\alpha\beta}{(\alpha^2+(n-\beta)^2)(\alpha^2+(n+\beta)^2)}\right\}$.",
    )
,
    rec(
        "RN-P4-C30-Entry07",
        r"For complex $\alpha,\beta$, $\displaystyle\varphi(\alpha,\beta)=\frac{1}{1+2e^{2\pi\alpha}\cos(2\pi\beta)+e^{4\pi\alpha}}=\frac{\pi\cosh(\pi(\alpha-\beta))-\cos(\pi(\alpha-\beta))}{2(\cosh(\pi\alpha)+\cos(\pi\beta))(\cosh(\pi\beta)+\cos(\pi\alpha))}-\sum_{n=0}^\infty\frac{2n+1}{(e^{(2n+1)\pi}-1)((2n+1+\beta)^2+\alpha^2)((2n+1-\beta)^2+\alpha^2)}$.",
    )
,
    rec(
        "RN-P4-C30-Entry08",
        r"$\displaystyle\psi(z)=\frac{\Gamma'(z)}{\Gamma(z)}=\frac{1}{2z}-\gamma-\sum_{k=1}^\infty\left\{\frac{2z}{k(k^2-z^2)}-\frac{\pi\cot(\pi k)}{k(k^2-z^2)}\right\}+\sum_{k=1}^\infty\frac{4k z}{(e^{2\pi k}-1)(k^2+z^2)}$.",
    )
,
    rec(
        "RN-P4-C30-Entry09",
        r"For positive integer $n$ (with $n$ replaced by $2n$ in Ramanujan's notation), $\displaystyle\sum_{k=0}^\infty\frac{1}{2k+1}=\frac{\pi}{2}\sum_{k=0}^\infty\frac{\tan(\pi n)}{2k+1}-\sum_{k=0}^\infty\frac{4n}{(2k+1)(4n^2+(2k+1)^2)}-\sum_{k=0}^\infty\frac{16n(2k+1)}{(2k+1)^2((2k+1)^2-16n^2)}$.",
    )
,
    rec(
        "RN-P4-C30-Entry10",
        r"$\displaystyle\sum_{k=0}^\infty\frac{(-1)^k}{2k+1}=\frac{\pi\sec(\pi z)}{2z(e^{2\pi i z}-1)}+\sum_{k=0}^\infty\frac{(-1)^k\,\sech(\pi k)}{(2k+1)((2k+1)^2-z^2)}$.",
    )
,
    rec(
        "RN-P4-C30-Entry11",
        r"If $\varphi(z)$ is entire and $p$ is any complex number, then formally $\displaystyle\frac{p\varphi(z)}{2\zeta(z)\cos(\pi z)}=\sum_{n=1}^\infty\frac{(-1)^n p\,\varphi(-2n)}{(2n)!\,(z+2n)}+\sum_{n=0}^\infty\frac{(-1)^n p\,\varphi(2n+1)}{(2n+1)!\,\zeta(2n+2)(z-2n-1)}$ + terms involving the nontrivial zeros of $\zeta(z)$.",
    )
,
    rec(
        "RN-P4-C30-Entry12",
        r"If $\varphi(z)$ is entire and $p$ is any complex number, then formally $\displaystyle\frac{p\varphi(z)}{2\Gamma(\tfrac12(z+1))\zeta(z)\cos(\pi z)}=\sum_{n=1}^\infty\frac{(-1)^n p\,\varphi(-2n)}{n!\,\zeta(2n+1)(z+2n)}+\sum_{n=0}^\infty\frac{(-1)^n p^{2n+1}\varphi(2n+1)}{(2n+1)!\,\zeta(2n+1)(z-2n-1)}$ + terms involving the nontrivial zeros of $\zeta(z)$.",
    )
,
    rec(
        "RN-P4-C30-Entry13",
        r"$\displaystyle\frac{n\sinh(2\pi z)+\sin(2\pi z)}{8z^2(\cosh(2\pi z)-\cos(2\pi z))}=\frac{1}{8z^2}+\sum_{n=1}^\infty\frac{1}{4z^2+n^2}$.",
    )
,
    rec(
        "RN-P4-C30-Entry14",
        r"$\displaystyle\frac{n\sinh(2\pi z)-\sin(2\pi z)}{4z(\cosh(2\pi z)-\cos(2\pi z))}=\sum_{n=1}^\infty\frac{n}{4z^2+n^2}$.",
    )
,
    rec(
        "RN-P4-C30-Entry15",
        r"$\displaystyle\frac{n\sinh(2\pi z)}{4z^2(\cosh(2\pi z)-\cos(2\pi z))}=\frac{1}{8z^2}+\sum_{n=1}^\infty\left\{\frac{1}{4z^2+n^2}+\frac{1}{2z(z^2+n^2)}\right\}$.",
    )
]
