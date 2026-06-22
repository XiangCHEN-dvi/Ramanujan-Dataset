"""RLN Part 4, Chapter 12 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C12 = ["infinite-series-identities-manuscript"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C12}


CHAPTER_12 = [
    rec(
        "RLN-P4-C12-Entry12-2-1",
        r"Let $\chi(n)$ denote the nonprincipal primitive character of modulus $4$, i.e., "
        r"$\chi(2n)=0$ and $\chi(2n+1)=(-1)^n$ for each nonnegative integer $n$. "
        r"Let $d(n)$ denote the number of positive divisors of the positive integer $n$. "
        r"If $x\neq in$ for each integer $n$, then "
        r"$\displaystyle\sum_{n=1}^{\infty}\frac{\chi(n)d(n)n}{n^2+x^2}"
        r"=\frac{\pi}{4}\sum_{n=1}^{\infty}\frac{\chi(n)}{n}\operatorname{sech}\!\left(\frac{\pi x}{2n}\right)$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-2-2",
        r"Let $\sigma_k(n)=\sum_{d\mid n}d^k$. Then for $\operatorname{Re}s>1$ and $\operatorname{Re}(s-r)>1$, "
        r"$\zeta(s)\zeta(s-r)=\displaystyle\sum_{n=1}^{\infty}\frac{\sigma_r(n)}{n^s}$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-2-3",
        r"Let $\chi$ be defined as in Entry $12.2.1$, and let $\sigma_k(n)$ be as in Entry $12.2.2$. "
        r"Then for $\operatorname{Re}s>1$ and $\operatorname{Re}(s-r)>1$, "
        r"$\displaystyle\sum_{m=1}^{\infty}\frac{\chi(m)}{m^s}\sum_{n=1}^{\infty}\frac{\chi(n)}{n^{s-r}}"
        r"=\sum_{n=1}^{\infty}\frac{\chi(n)\sigma_r(n)}{n^s}$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-3-1",
        r"If $\alpha$ and $\beta$ are positive numbers such that $\alpha\beta=\pi^2$, then "
        r"$\dfrac{1}{2w}+\displaystyle\sum_{m=1}^{\infty}\left(\frac{m\alpha\coth(m\alpha)}{w+m^2\alpha}"
        r"+\frac{m\beta\coth(m\beta)}{w-m^2\beta}\right)"
        r"=\frac{\pi}{2}\cot(\sqrt{w\alpha})\coth(\sqrt{w\beta})$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-3-2",
        r"Under the hypotheses of Entry $12.3.1$, "
        r"$\dfrac{\pi}{2}\cot(\sqrt{w\alpha})\coth(\sqrt{w\beta})"
        r"=\dfrac{1}{2w}+\dfrac{1}{2}\log\dfrac{\beta}{\alpha}"
        r"+\displaystyle\sum_{m=1}^{\infty}\left(\frac{m\alpha\coth(m\alpha)}{w+m^2\alpha}"
        r"+\frac{m\beta\coth(m\beta)}{w-m^2\beta}\right)$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-3-3",
        r"If $\alpha$ and $\beta$ are positive numbers such that $\alpha\beta=\pi^2$, then "
        r"$\alpha\displaystyle\sum_{m=1}^{\infty}\frac{m}{e^{2m\alpha}-1}"
        r"+\beta\sum_{m=1}^{\infty}\frac{m}{e^{2m\beta}-1}"
        r"=\frac{\alpha+\beta}{24}-\frac{1}{4}$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-3-4",
        r"If $\alpha$ and $\beta$ are positive numbers such that $\alpha\beta=\pi^2$, and if "
        r"$\sigma(m)=\sum_{d\mid m}d$, then "
        r"$\alpha\displaystyle\sum_{m=1}^{\infty}\sigma(m)e^{-2m\alpha}"
        r"+\beta\sum_{m=1}^{\infty}\sigma(m)e^{-2m\beta}"
        r"=\frac{\alpha+\beta}{24}-\frac{1}{4}$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-3-5",
        r"If $\alpha$ and $\beta$ are positive numbers such that $\alpha\beta=\pi^2$, and if "
        r"$\sigma_k(m)=\sum_{d\mid m}d^k$, then "
        r"$\displaystyle\sum_{m=1}^{\infty}\frac{1}{m(e^{2m\alpha}-1)}"
        r"-\sum_{m=1}^{\infty}\frac{1}{m(e^{2m\beta}-1)}"
        r"=\sum_{m=1}^{\infty}\sigma_{-1}(m)e^{-2m\alpha}"
        r"-\sum_{m=1}^{\infty}\sigma_{-1}(m)e^{-2m\beta}"
        r"=\frac{1}{4}\log\frac{\alpha}{\beta}-\frac{\alpha+\beta}{12}$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-3-6",
        r"Let $\alpha$ and $\beta$ be positive numbers such that $\alpha\beta=\pi^2$, and let $B_m$, "
        r"$m\ge0$, denote the $m$th Bernoulli number. If $r$ is a positive integer with $r\ge2$, then "
        r"$\alpha^r\!\left(\displaystyle\sum_{m=1}^{\infty}\frac{m^{2r-1}}{e^{2m\alpha}-1}-\frac{B_{2r}}{4r}\right)"
        r"=(-\beta)^r\!\left(\sum_{m=1}^{\infty}\frac{m^{2r-1}}{e^{2m\beta}-1}-\frac{B_{2r}}{4r}\right)$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-3-7",
        r"If $\alpha$ and $\beta$ are positive numbers such that $\alpha\beta=\pi^2$, and if $r$ is a "
        r"positive integer with $r\ge2$, then "
        r"$\alpha^r\!\left(\displaystyle\sum_{m=1}^{\infty}\sigma_{2r-1}(m)e^{-2m\alpha}-\frac{B_{2r}}{4r}\right)"
        r"=(-\beta)^r\!\left(\sum_{m=1}^{\infty}\sigma_{2r-1}(m)e^{-2m\beta}-\frac{B_{2r}}{4r}\right)$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-3-8",
        r"$\displaystyle\sum_{m=1}^{\infty}\sigma_5(m)e^{-2\pi m}=\frac{1}{504}$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-3-9",
        r"If $\alpha$ and $\beta$ are positive numbers such that $\alpha\beta=\pi^2$, and if $r$ is a "
        r"positive integer, then "
        r"$(4\alpha)^{-r}\!\left(\dfrac{1}{2}\zeta(2r+1)+\displaystyle\sum_{m=1}^{\infty}\frac{1}{m^{2r+1}(e^{2m\alpha}-1)}\right)"
        r"-(-4\beta)^{-r}\!\left(\dfrac{1}{2}\zeta(2r+1)+\sum_{m=1}^{\infty}\frac{1}{m^{2r+1}(e^{2m\beta}-1)}\right)"
        r"=(4\alpha)^{-r}\!\left(\dfrac{1}{2}\zeta(2r+1)+\displaystyle\sum_{m=1}^{\infty}\sigma_{-1-2r}(m)e^{-2m\alpha}\right)"
        r"-(-4\beta)^{-r}\!\left(\dfrac{1}{2}\zeta(2r+1)+\sum_{m=1}^{\infty}\sigma_{-1-2r}(m)e^{-2m\beta}\right)"
        r"=-\displaystyle\sum_{k=0}^{r+1}\frac{(-1)^kB_{2k}B_{2r+2-2k}\alpha^{r+1-k}\beta^k}{(2k)!(2r+2-2k)!}$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-4-1",
        r"If $\alpha$ and $\beta$ are positive numbers such that $\alpha\beta=\pi^2/4$, and if "
        r"$w\neq-(2m+1)^2\alpha$, $-(2m+1)^2\beta$ for $0\le m<\infty$, then "
        r"$\dfrac{\pi}{4}\sec(\sqrt{w\alpha})\operatorname{sech}(\sqrt{w\beta})"
        r"=\displaystyle\sum_{m=0}^{\infty}(-1)^m\left(\frac{(2m+1)\alpha\operatorname{sech}((2m+1)\alpha)}{w+(2m+1)^2\alpha}"
        r"-\frac{(2m+1)\beta\operatorname{sech}((2m+1)\beta)}{w-(2m+1)^2\beta}\right)$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-4-2",
        r"If $\alpha\beta=\pi^2/4$, where $\alpha$ and $\beta$ are positive numbers, and if $r$ is any "
        r"positive integer, then "
        r"$\alpha^r\displaystyle\sum_{m=0}^{\infty}\frac{(-1)^m(2m+1)^{2r-1}}{\cosh((2m+1)\alpha)}"
        r"+(-\beta)^r\sum_{m=0}^{\infty}\frac{(-1)^m(2m+1)^{2r-1}}{\cosh((2m+1)\beta)}=0$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-4-3",
        r"If $\alpha$ and $\beta$ are positive numbers such that $\alpha\beta=\pi^2/4$, and if $r$ is any "
        r"positive integer, then "
        r"$\alpha^r\displaystyle\sum_{m=0}^{\infty}(-1)^m\sigma_{2r-1}(m)e^{-(2m+1)\alpha}"
        r"+(-\beta)^r\sum_{m=0}^{\infty}(-1)^m\sigma_{2r-1}(m)e^{-(2m+1)\beta}=0$.",
    ),
    rec(
        "RLN-P4-C12-Entry12-4-4",
        r"If $\alpha$ and $\beta$ are positive numbers such that $\alpha\beta=\pi^2/4$, if $r$ is any "
        r"positive integer, and if $\chi$ denotes the nonprincipal primitive character of modulus $4$, "
        r"as in Section $12.2$, then "
        r"$2\alpha^{1-r}\displaystyle\sum_{m=1}^{\infty}\frac{\chi(m)m^{1-2r}}{\cosh(m\alpha)}"
        r"+2(-\beta)^{1-r}\sum_{m=1}^{\infty}\frac{\chi(m)m^{1-2r}}{\cosh(m\beta)}"
        r"=4\alpha^{1-r}\displaystyle\sum_{m=1}^{\infty}\chi(m)\sigma_{1-2r}(m)e^{-m\alpha}"
        r"+2(-\beta)^{1-r}\sum_{m=1}^{\infty}\chi(m)\sigma_{1-2r}(m)e^{-m\beta}"
        r"=\dfrac{\pi}{2}\displaystyle\sum_{k=0}^{r-1}\frac{(-1)^kE_{2k}E_{2r-2-2k}}{(2k)!(2r-2-2k)!}\alpha^{r-1-k}\beta^k$, "
        r"where $E_{2k}$ are the Euler numbers.",
    ),
    rec(
        "RLN-P4-C12-Entry12-4-5",
        r"$4\displaystyle\sum_{m=0}^{\infty}(-1)^m\sigma_{-1}(m)e^{-(2m+1)\alpha}"
        r"+4\sum_{m=0}^{\infty}(-1)^m\sigma_{-1}(m)e^{-(2m+1)\beta}=\frac{\pi}{2}$.",
    ),
]
