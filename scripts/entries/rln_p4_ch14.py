"""RLN Part 4, Chapter 14 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C14 = ["integral-analogues-theta-gauss-sums"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C14}


CHAPTER_14 = [
    rec(
        "RLN-P4-C14-Entry14-3-1",
        r"For $w>0$, with $\varphi_w(t):=\displaystyle\int_0^{\infty}\frac{\cos(\pi tx)}{\cosh(\pi x)}e^{-\pi wx^2}\,dx$, "
        r"$\varphi_w(t)=\dfrac{1}{\sqrt{w}}e^{-\pi t^2/(4w)}\varphi_{1/w}(it/w)$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-2",
        r"With $\psi_w(t):=\displaystyle\int_0^{\infty}\frac{\sin(\pi tx)}{\sinh(\pi x)}e^{-\pi wx^2}\,dx$, "
        r"$e^{\pi(t+w)^2/(4w)}\varphi_w(t+w)=e^{\pi t^2/(4w)}\!\left(\dfrac{1}{2}+\psi_w(t)\right)$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-3",
        r"$\dfrac{1}{2}+\psi_w(t+i)=\dfrac{i}{\sqrt{w}}e^{-\pi t^2/(4w)}"
        r"\left(\dfrac{1}{2}-\psi_{1/w}\!\left(\dfrac{it}{w}+i\right)\right)$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-4",
        r"$\varphi_w(i)=\dfrac{1}{2\sqrt{w}}$, $\psi_w(i)=\dfrac{i}{2\sqrt{w}}$, "
        r"$\varphi_w(w)=\dfrac{1}{2}e^{-\pi w/4}$, and "
        r"$\dfrac{1}{2}-\psi_w(w)=e^{-\pi w/4}\varphi_w(0)$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-5",
        r"$\varphi_w(w\pm i)=\left(\dfrac{1}{2\sqrt{w}}\mp\dfrac{i}{2}\right)e^{-\pi w/4}$, "
        r"$\psi_w(w\pm i)=\dfrac{1}{2}\pm\dfrac{i}{2\sqrt{w}}e^{-\pi w/4}$, and "
        r"$\varphi_w\!\left(\dfrac{1}{2w}\right)+\psi_w\!\left(\dfrac{1}{2w}\right)=\dfrac{1}{2}$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-6",
        r"$\varphi_w(t+i)+\varphi_w(t-i)=\dfrac{1}{\sqrt{w}}e^{-\pi t^2/(4w)}$ and "
        r"$\psi_w(t+i)-\psi_w(t-i)=\dfrac{i}{\sqrt{w}}e^{-\pi t^2/(4w)}$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-7",
        r"$e^{\pi(t+w)^2/(4w)}\varphi_w(t+w)+e^{\pi(t-w)^2/(4w)}\varphi_w(t-w)=e^{\pi t^2/(4w)}$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-8",
        r"$e^{\pi(t+w)^2/(4w)}\!\left(\dfrac{1}{2}-\psi_w(t+w)\right)"
        r"=e^{\pi(t-w)^2/(4w)}\!\left(\dfrac{1}{2}+\psi_w(t-w)\right)$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-9",
        r"If $n$ is any positive integer, then "
        r"$\varphi_w(t)+(-1)^{n+1}\varphi_w(t+2ni)"
        r"=\dfrac{1}{\sqrt{w}}\displaystyle\sum_{k=0}^{n-1}(-1)^ke^{-\pi(t+(2k+1)i)^2/(4w)}$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-10",
        r"If $n$ is any positive integer, then "
        r"$\psi_w(t)-\psi_w(t+2ni)"
        r"=-\dfrac{i}{\sqrt{w}}\displaystyle\sum_{k=0}^{n-1}e^{-\pi(t+(2k+1)i)^2/(4w)}$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-11",
        r"For any positive integer $n$, "
        r"$e^{\pi t^2/(4w)}\varphi_w(t)+(-1)^{n+1}e^{\pi(t+2nw)^2/(4w)}\varphi_w(t+2nw)"
        r"=\displaystyle\sum_{k=0}^{n-1}(-1)^ke^{\pi(t+(2k+1)w)^2/(4w)}$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-12",
        r"For any positive integer $n$, "
        r"$e^{\pi t^2/(4w)}\!\left(\dfrac{1}{2}+\psi_w(t)\right)"
        r"+(-1)^{n+1}e^{\pi(t+2nw)^2/(4w)}\!\left(\dfrac{1}{2}+\psi_w(t+2nw)\right)"
        r"=\displaystyle\sum_{k=1}^{n}(-1)^{k-1}e^{\pi(t+2kw)^2/(4w)}$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-13",
        r"Let $m$ and $n$ denote any positive integers and set $s=t+2mw\pm2ni$. Then "
        r"$\varphi_w(s)+(-1)^{(m+1)(n+1)}e^{-\pi m(s+t)/2}\varphi_w(t)"
        r"=e^{-\pi s^2/(4w)}\displaystyle\sum_{k=0}^{m-1}(-1)^ke^{\pi(s-(2k+1)w)^2/(4w)}"
        r"+(-1)^{(m+1)(n+1)}\dfrac{1}{\sqrt{w}}e^{-\pi m(s+t)/2}"
        r"\displaystyle\sum_{k=0}^{n-1}(-1)^ke^{-\pi(t\pm(2k+1)i)^2/(4w)}$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-14",
        r"Let $m$ and $n$ denote positive integers. If $s=2mw\pm2ni$, then "
        r"$\dfrac{1}{2}-\psi_w(s)+(-1)^{mn+m+1}e^{-\pi m(s+t)/2}\!\left(\dfrac{1}{2}-\psi_w(t)\right)"
        r"=e^{-\pi s^2/(4w)}\displaystyle\sum_{j=1}^{m}(-1)^{j-1}e^{\pi(s-2jw)^2/(4w)}"
        r"\pm(-1)^{mn+m+1}\dfrac{i}{\sqrt{w}}e^{-\pi m(s+t)/2}"
        r"\displaystyle\sum_{j=0}^{n-1}e^{-\pi(t\pm(2j+1)i)^2/(4w)}$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-15",
        r"Let $t=mw\pm ni$, where $m$ and $n$ are positive integers. If $m$ is odd and $n$ is odd, "
        r"or if $m$ is even and $n$ is odd, or if $m$ is odd and $n$ is even, then "
        r"$\varphi_w(t)=\dfrac{1}{2}e^{-\pi t^2/(4w)}\displaystyle\sum_{j=0}^{m-1}(-1)^je^{\pi(t-(2j+1)w)^2/(4w)}"
        r"+\dfrac{1}{2\sqrt{w}}\displaystyle\sum_{j=0}^{n-1}(-1)^je^{\pi(t\mp(2j+1)i)^2/(4w)}$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-3-16",
        r"Let $t=mw\pm ni$, where $m$ and $n$ are positive integers. If $m$ is odd and $n$ is odd, "
        r"or if $m$ is even and $n$ is odd, or if $m$ is even and $n$ is even, then "
        r"$\psi_w(t)=-\dfrac{1}{2}e^{-\pi t^2/(4w)}\displaystyle\sum_{j=1}^{m}(-1)^{j-1}e^{\pi(t-2jw)^2/(4w)}"
        r"\pm\dfrac{i}{2\sqrt{w}}\displaystyle\sum_{j=0}^{n-1}e^{\pi(t\mp(2j+1)i)^2/(4w)}$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-4-1",
        r"With $F_w(t):=\displaystyle\int_0^{\infty}\frac{\sin(\pi tx)}{\tanh(\pi x)}e^{-\pi wx^2}\,dx$, "
        r"$F_w(t)=-\dfrac{i}{\sqrt{w}}e^{-\pi t^2/(4w)}F_{1/w}(it/w)$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-4-2",
        r"If $n$ is any positive integer, then "
        r"$F_w(t)-F_w(t+2ni)=-\dfrac{i}{\sqrt{w}}\displaystyle\sum_{j=0}^{n}{}'e^{-\pi(t+2ji)^2/(4w)}$, "
        r"where the prime on the summation indicates that the terms with $j=0$ and $j=n$ are multiplied by "
        r"$\dfrac{1}{2}$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-4-3",
        r"If $n$ is a positive integer, then "
        r"$F_w(t)-e^{\pi n(t+nw)}F_w(t+2nw)=-e^{-\pi t^2/(4w)}\displaystyle\sum_{j=0}^{n}{}'e^{\pi(t+2jw)^2/(4w)}$, "
        r"where the prime on the summation has the same meaning as in Entry $14.4.2$.",
    ),
    rec(
        "RLN-P4-C14-Entry14-4-4",
        r"Let $s=t+2\eta_1mw+2\eta_2ni$, where $\eta_1^2=\eta_2^2=1$, and where $m$ and $n$ are positive "
        r"integers. Then "
        r"$F_w(s)+(-1)^{mn-1}e^{-\pi\eta_1m(s+t)/2}F_w(t)"
        r"=\eta_1e^{-\pi s^2/(4w)}\displaystyle\sum_{j=0}^{m}{}'e^{\pi(s-2j\eta_1w)^2/(4w)}"
        r"+\eta_2(-1)^{mn}\dfrac{i}{\sqrt{w}}e^{-\pi\eta_1m(s+t)/2}"
        r"\displaystyle\sum_{j=0}^{n}{}'e^{-\pi(t+2\eta_2ji)^2/(4w)}$, "
        r"where the primes on the summation signs have the same meaning as in Entries $14.4.2$ and $14.4.3$.",
    ),
]
