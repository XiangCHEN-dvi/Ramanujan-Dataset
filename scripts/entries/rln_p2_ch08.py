"""RLN Part 2, Chapter 8 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C08 = ["theta-function-identities"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C08}


CHAPTER_8 = [
    rec("RLN-P2-C08-Entry8-2-1", r"Let $A:=f(-q^7,-q^8)$ and $B:=q f(-q^2,-q^{13})$. Then $A+B=\frac{f(-q^2,-q^3)}{f(-q,-q^4)f(-q^5)}$, $A-B=f(-q^{2/3},-q)+q^{2/3}f(-q^3,-q^{12})$, $A^3+B^3=\frac{f(-q^6,-q^9)}{f(-q^3,-q^{12})f^3(-q^5)}$, and $(A-B)^3=\frac{f(-q^2,-q^3)f^3(-q,-q^4)}{f(-q^3,-q^{12})}+q^2 f^3(-q^3,-q^{12})$."),
    rec("RLN-P2-C08-Entry8-2-2", r"Let $A:=f(-q^4,-q^{11})$ and $B:=q f(-q,-q^{14})$. For $|q|<1$, $A-B=\frac{f(-q,-q^4)}{f(-q^2,-q^3)f(-q^5)}$, $A+B=-\frac{1}{q^{1/3}}\bigl(f(-q^{1/3},-q^{4/3})-f(-q^6,-q^9)\bigr)$, $A^3-B^3=\frac{f(-q^3,-q^{12})}{f(-q^6,-q^9)f^3(-q^5)}$, and $(A+B)^3=-\frac{1}{q}\left(\frac{f(-q,-q^4)f^3(-q^2,-q^3)}{f(-q^6,-q^9)}-f^3(-q^6,-q^9)\right)$."),
    rec("RLN-P2-C08-Entry8-2-3", r"For $|ab|<1$, with $q=ab$, $f^3(ab^2,a^2b)+a f^3(b,a^3b^2)+b f^3(a,a^2b^3)=f(a,b)\left(\frac{f^9(-q)}{f^3(-q^3)}+\frac{27q f^9(-q^3)}{f^3(-q)}\right)^{1/3}=f(a,b)\left(\frac{\psi^3(q)}{\psi(q^3)}+\frac{3q\psi^3(q^3)}{\psi(q)}\right)$."),
    rec("RLN-P2-C08-Entry8-2-4", r"For $|q|<1$, let $U:=\sum_{n=0}^{\infty}\frac{q^{3n^2}}{(q^3;q^3)_n}$ and $V:=\sum_{n=0}^{\infty}\frac{q^{3n(n+1)}}{(q^3;q^3)_n}$. Then $f^3(-q^{13},-q^{17})+q^3 f^3(-q^7,-q^{23})=\frac{U f(-q^6)f^3(-q^{10})}{f(-q^{30})}$ and $f^3(-q^{11},-q^{19})+q^9 f^3(-q,-q^{29})=\frac{V f(-q^6)f^3(-q^{10})}{f(-q^{30})}$."),
    rec("RLN-P2-C08-Entry8-3-1", r"Let $\frac{\varphi(q^{1/7})}{\varphi(q^7)}=1+u+v+w$. Then $p:=uvw=\frac{8q^2}{(-q;q^2)_{\infty}(-q^7;q^{14})_{\infty}^7}$ and $\frac{\varphi^8(q)}{\varphi^8(q^7)}-(2+5p)\frac{\varphi^4(q)}{\varphi^4(q^7)}+(1-p)^3=0$. Furthermore, $u=\left(\frac{\alpha^2 p}{\beta}\right)^{1/7}$, $v=\left(\frac{\beta^2 p}{\gamma}\right)^{1/7}$, and $w=\left(\frac{\gamma^2 p}{\alpha}\right)^{1/7}$, where $\alpha$, $\beta$, and $\gamma$ are roots of $\xi^3+2\xi^2\left(1+3p-\frac{\varphi^4(q)}{\varphi^4(q^7)}\right)+\xi p^2(p+4)-p^4=0$. For example, $\varphi(e^{-7\pi\sqrt{7}})=7^{3/4}\varphi(e^{-\pi\sqrt{7}})\bigl(1+(-)^{2/7}+(-)^{2/7}+(-)^{2/7}\bigr)$, with $u:=\frac{2q^{1/7}f(q^5,q^9)}{\varphi(q^7)}$, $v:=\frac{2q^{4/7}f(q^3,q^{11})}{\varphi(q^7)}$, and $w:=\frac{2q^{9/7}f(q,q^{13})}{\varphi(q^7)}$."),
]
