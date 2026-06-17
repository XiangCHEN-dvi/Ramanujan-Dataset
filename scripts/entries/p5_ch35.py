"""Part V, Chapter 35 entries — values of theta-functions (curated LaTeX)."""

from __future__ import annotations

TOPICS_C35 = ["values-of-theta-functions"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C35}


CHAPTER_35 = [
    rec("RN-P5-C35-Entry01i", r"Let $a=\Gamma(1/4)/(2\pi^{3/4})$. Then $\varphi(e^{-\pi})=a$."),
    rec("RN-P5-C35-Entry01ii", r"Let $a$ be as in Entry 1(i). Then $\varphi(-e^{-\pi})=a\,2^{-1/4}$."),
    rec("RN-P5-C35-Entry01iii", r"Let $a$ be as in Entry 1(i). Then $\varphi(e^{-\pi/2})=a\,2^{-1/4}(\sqrt{2}+1)^{1/4}$."),
    rec("RN-P5-C35-Entry01iv", r"Let $a$ be as in Entry 1(i). Then $\varphi(-e^{-\pi/2})=a\,2^{-1/2}$."),
    rec("RN-P5-C35-Entry01v", r"Let $a$ be as in Entry 1(i). Then $\varphi(e^{-\pi/4})=a\,2^{-1/4}(1+2^{-1/4})$."),
    rec("RN-P5-C35-Entry01vi", r"Let $a$ be as in Entry 1(i). Then $\varphi(-e^{-\pi/4})=a\,2^{-5/4}(2^{1/4}+2^{-1/4})^{1/2}$."),
    rec("RN-P5-C35-Entry01vii", r"Let $a$ be as in Entry 1(i). Then $\varphi(e^{-\pi/8})=a\,2^{-1/8}(\sqrt{2}+1)^{1/4}$."),
    rec("RN-P5-C35-Entry01viii", r"Let $a$ be as in Entry 1(i). Then $\varphi(-e^{-\pi/8})=a\,2^{-1/8}(\sqrt{2}-1)^{1/4}$."),
    rec("RN-P5-C35-Entry01ix", r"Let $a$ be as in Entry 1(i). Then $\varphi(e^{-\pi/16})=a(1+2^{-1/4})$."),
    rec("RN-P5-C35-Entry01x", r"Let $a$ be as in Entry 1(i). Then $\varphi(-e^{-\pi/16})=a\,2^{-1/16}$."),
    rec("RN-P5-C35-Entry01xi", r"Let $a$ be as in Entry 1(i). Then $\psi(e^{-\pi})=a\,2^{-1/4}(\sqrt{2}+1)^{1/4}$."),
    rec("RN-P5-C35-Entry01xii", r"Let $a$ be as in Entry 1(i). Then $\psi(-e^{-\pi})=a\,2^{-1/4}(\sqrt{2}-1)^{1/4}$."),
    rec("RN-P5-C35-Entry01xiii", r"Let $a$ be as in Entry 1(i). Then $\chi(e^{-\pi})=a\,2^{-1/8}(1-\sqrt{2})^{1/4}e^{\pi/8}$."),
    rec("RN-P5-C35-Entry01xiv", r"Let $a$ be as in Entry 1(i). Then $\chi(-e^{-\pi})=a\,2^{-1/8}(1-2^{-1/4})e^{\pi/8}$."),
    rec("RN-P5-C35-Entry01xv", r"Let $a$ be as in Entry 1(i). Then $f(e^{-\pi/4})=a\,2^{-1/16}(1+\sqrt{2})^{1/4}e^{\pi/16}$."),
    rec("RN-P5-C35-Entry01xvi", r"Let $a$ be as in Entry 1(i). Then $f(-e^{-\pi/4})=a\,2^{-1/16}\sqrt{2^{1/4}+1}\,\sqrt{\sqrt{2}+1}\,e^{\pi/16}$."),
    rec("RN-P5-C35-Entry02i", r"Let $a$ be given by (1.1). Then $f(-e^{-\pi})=a\,2^{-1/4}\sqrt{\sqrt{2}+1}$."),
    rec("RN-P5-C35-Entry02ii", r"Let $a$ be given by (1.1). Then $f(e^{-\pi/2})=a\,2^{-1/4}\sqrt{\sqrt{2}-1}$."),
    rec("RN-P5-C35-Entry02iii", r"Let $a$ be given by (1.1). Then $f(-e^{-\pi/2})=a\,2^{-1/8}e^{\pi/8}$."),
    rec("RN-P5-C35-Entry02iv", r"Let $a$ be given by (1.1). Then $f(e^{-\pi/4})=a\,2^{-1/8}(\sqrt{2}-1)^{1/4}$."),
    rec("RN-P5-C35-Entry02v", r"Let $a$ be given by (1.1). Then $\chi(-e^{-\pi/2})=2^{1/4}a$."),
    rec("RN-P5-C35-Entry02vi", r"Let $a$ be given by (1.1). Then $\chi(-e^{-\pi/4})=2^{1/8}a$."),
    rec("RN-P5-C35-Entry02vii", r"Let $a$ be given by (1.1). Then $\chi(-e^{-\pi/8})=2^{1/16}(2+\sqrt{2})^{1/4}a$."),
    rec("RN-P5-C35-Entry02viii", r"Let $a$ be given by (1.1). Then $\chi(e^{-\pi/8})=2^{1/16}(\sqrt{2+\sqrt{2}})^{1/2}a$."),
    rec("RN-P5-C35-Entry02ix", r"Let $a$ be given by (1.1). Then $\chi(e^{-\pi/16})=2^{1/32}(\sqrt{2}+1)^{1/4}e^{\pi/32}a$."),
    rec("RN-P5-C35-Entry03", r"$\displaystyle\frac{\varphi(e^{-\pi\sqrt{5}})}{\varphi(e^{-\pi})}=\frac{(1+\sqrt{5})^{1/4}}{2^{2/5}\bigl(5(\sqrt{5}-2)\bigr)^{1/4}}$."),
    rec("RN-P5-C35-Entry04", r"$\displaystyle\frac{\varphi(e^{-\pi\sqrt{3}})}{\varphi(e^{-\pi})}=\frac{3^{1/8}}{2^{1/3}(3\sqrt{3}-5)^{1/4}}$."),
    rec("RN-P5-C35-Entry05", r"$\displaystyle\frac{\varphi(e^{-3\pi})}{\varphi(e^{-\pi})}=\frac{1+2^{1/4}(2(1+\sqrt{3}))^{1/3}}{1+(2(\sqrt{3}+1))^{1/3}}$."),
    rec("RN-P5-C35-Entry06", r"$\displaystyle\frac{\varphi(e^{-\pi\sqrt{45}})}{\varphi(e^{-\pi})}=\frac{3-\sqrt{10}+\sqrt{5}\bigl(\sqrt{3}+\sqrt{2}+\sqrt{6}+\sqrt{15}+3+\sqrt{5}\bigr)}{3(\sqrt{3}+\sqrt{2})\bigl(2+\sqrt{5}\bigr)}$."),
    rec("RN-P5-C35-Entry07", r"$\displaystyle\frac{\varphi(e^{-\pi\sqrt{7}})}{\varphi(e^{-\pi})}=\frac{1}{7^{1/8}\bigl(7+5\sqrt{2}+4\sqrt{7}+2\cdot 7^{1/4}+20^{1/4}+4\cdot 7^{3/8}\bigr)^{1/2}}$."),
    rec("RN-P5-C35-Entry04-Corollary", r"$\displaystyle{}_2F_1\!\left(\tfrac12,\tfrac12;1;\tfrac12\right)=\frac{\Gamma(\tfrac14)^2}{2\sqrt{2\pi}}$."),
    rec("RN-P5-C35-Entry05-Corollary", r"$\displaystyle a(e^{-2\pi/3})=\frac{\varphi(e^{-\pi\sqrt{9}})}{\varphi(e^{-\pi})}=\frac{1+2^{1/4}(2(1+\sqrt{3}))^{1/3}}{1+(2(\sqrt{3}+1))^{1/3}}$."),
    rec("RN-P5-C35-Entry06-Corollary", r"$\displaystyle{}_2F_1\!\left(\tfrac12,\tfrac12;1;\tfrac{1}{45}\right)=\frac{\varphi(e^{-\pi\sqrt{45}})^2}{\varphi(e^{-\pi})^2}\cdot\frac{45}{2(\sqrt{45}-1)}$."),
    rec("RN-P5-C35-Entry07-Corollary", r"$\displaystyle{}_2F_1\!\left(\tfrac12,\tfrac12;1;\tfrac17\right)=\frac{\varphi(e^{-\pi\sqrt{7}})^2}{\varphi(e^{-\pi})^2}\cdot\frac{7}{2(\sqrt{7}-1)}$."),
    rec("RN-P5-C35-Entry08-Theorem01", r"If $n$ is a positive integer and $V=(G_{n/3}/G_{3n})^{1/2}$, then $\alpha_{3,n}=\bigl(V^2+3V^{-2}-2\bigr)^{-1/2}$."),
    rec("RN-P5-C35-Entry08-Corollary02", r"If $n$ is a positive integer and $U_n=G_{n/3}G_{3n}$, then $\alpha_{5,n}=\tfrac12(8G_n^4+8G_n^{-4}-20)^{-1/4}$."),
    rec("RN-P5-C35-Entry08-Theorem03", r"Let $f(-q)$ be defined by (0.3), and let $k$ be a positive rational number. Put $A_k=(G_k/G_{5k})^{1/2}$ and $V=(G_{k/5}/G_k)^{1/2}$. Then $\alpha_{5,k}=\bigl(A_k^2V^2+V^{-2}-1\bigr)^{-1/2}$."),
    rec("RN-P5-C35-Entry08-Corollary04", r"If $n$ is a positive integer and $V=(G_{n/5}/G_{5n})^{1/2}$, then $\alpha_{5,n}=\bigl(V^2+V^{-2}+3\bigr)^{-1/2}$."),
    rec("RN-P5-C35-Entry08-Theorem05", r"If $n$ is any positive integer and $V=(G_{n/7}/G_{7n})^{1/2}$, then $\alpha_{7,n}=\tfrac12\bigl((V_n^2-V_n^{-2})+8(V_n^4-V_n^{-4})\bigr)^{-1/4}$."),
    rec("RN-P5-C35-Entry08-Theorem06", r"Let $m$ and $n$ be odd positive integers such that $mn$ is squarefree and $-mn\equiv 3\pmod 4$. Then $\alpha_{m,n}$ is a unit."),
    rec("RN-P5-C35-Entry08-Theorem07", r"Let $m$ and $n$ be odd positive integers such that $mn$ is squarefree and $-mn\equiv 1\pmod 8$. Then $\alpha_{m,n}$ is a unit."),
]
