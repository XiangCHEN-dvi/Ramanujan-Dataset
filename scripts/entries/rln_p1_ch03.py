"""RLN Part 1, Chapter 3 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C03 = ["fragment-rogers-ramanujan-cubic-continued-fraction"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C03}


CHAPTER_3 = [
    rec("RLN-P1-C03-Entry3-2-1", "With $G_1(q)$ and $H_1(q)$ as in (3.1.4) and $F(q)$ as in (3.1.2), $\\dfrac{G_1(q)}{H_1(q)}=F(q)$."),
    rec("RLN-P1-C03-Entry3-2-2", "If $G(q)$ and $H(q)$ are defined by (3.1.3), then $G(q)=\\dfrac{1}{(q;q^5)_\\infty(q^4;q^5)_\\infty}$ and $H(q)=\\dfrac{1}{(q^2;q^5)_\\infty(q^3;q^5)_\\infty}$."),
    rec("RLN-P1-C03-Entry3-2-3", "With $G_1(q)$ and $H_1(q)$ as in (3.1.4), $G_1(q)=\\dfrac{(q^2;q^4)_\\infty}{(q;q^5)_\\infty(q^4;q^5)_\\infty}$ and $H_1(q)=\\dfrac{(q^2;q^4)_\\infty}{(q^2;q^5)_\\infty(q^3;q^5)_\\infty}$."),
    rec("RLN-P1-C03-Entry3-2-4", "If $C(q)$ is defined by (3.1.2), then $5q\\dfrac{d}{dq}C(q)=\\left(1-\\dfrac{f^5(-q)}{f(-q^5)}\\right)C(q)$."),
    rec("RLN-P1-C03-Entry3-2-5", "If $v:=R(q^5)$, then $q\\left(v+\\dfrac{1}{v}\\right)\\dfrac{f^5(-q^5)}{f(-q)}=1+\\sum_{n=1}^{\\infty}\\left(\\dfrac{nq^n}{1-q^n}-\\dfrac{25nq^{25n}}{1-q^{25n}}\\right)$."),
    rec("RLN-P1-C03-Entry3-2-6", "If $v:=R(q)$, then $q\\left(\\dfrac{1}{v^5}+v^5\\right)\\dfrac{f^5(-q^5)}{f(-q)}=1+6\\sum_{n=1}^{\\infty}\\left(\\dfrac{nq^n}{1-q^n}-\\dfrac{5nq^{5n}}{1-q^{5n}}\\right)$."),
    rec("RLN-P1-C03-Entry3-2-7", "If $2u:=11+\\dfrac{f^6(-q)}{qf^6(-q^5)}$ and $2v:=1+\\dfrac{f(-q^{1/5})}{q^{1/5}f(-q^5)}$, then $5\\sqrt{u^2+1-u}=\\sqrt{v^2+1-v}=R(q)$."),
    rec("RLN-P1-C03-Entry3-2-8", "If $2u:=11+\\dfrac{125q f^6(-q^5)}{f^6(-q)}$ and $2v:=1+\\dfrac{5q f(-q^{25})}{f(-q)}$, then $\\dfrac{\\sqrt{5}}{\\frac{1+\\sqrt{5}}{2}-1}\\cdot\\dfrac{1}{5}\\sqrt{u^2+1-u}=\\dfrac{\\sqrt{5}}{\\frac{1+\\sqrt{5}}{2}-1}\\cdot\\dfrac{1}{5}\\sqrt{v^2+1-v}=\\dfrac{1+\\sqrt{5}}{2}+R(q^5)$."),
    rec("RLN-P1-C03-Entry3-2-9", "If $\\alpha\\beta=\\pi^2/5$, then $\\left(\\left(\\dfrac{\\sqrt{5}+1}{2}\\right)^5+R^5(e^{-2\\alpha})\\right)\\left(\\left(\\dfrac{\\sqrt{5}+1}{2}\\right)^5+R^5(e^{-2\\beta})\\right)=5\\left(\\dfrac{\\sqrt{5}+1}{2}\\right)^5$."),
    rec("RLN-P1-C03-Entry3-2-10", "Let $u:=U^{1/5}:=\\dfrac{q^{1/5}}{1+\\dfrac{q}{1+\\dfrac{q^2}{1+\\dfrac{q^3}{1+\\cdots}}}}$ and $v:=V^{1/5}:=\\dfrac{q^{2/5}}{1+\\dfrac{q^2}{1+\\dfrac{q^4}{1+\\dfrac{q^6}{1+\\cdots}}}}$. Then (a) $\\dfrac{v-u^2}{v+u^2}=uv^2$; (b) $UV^2(U^2+V)+U^2-V+10UV(UV-U+V+1)=0$; (c) $U=t\\left(\\dfrac{1-t}{1+t}\\right)^2$ and $V=\\dfrac{t^2(1+t)}{1-t}$, where $t\\le\\sqrt{5}-2$."),
    rec("RLN-P1-C03-Entry3-2-11", "Let $u:=\\dfrac{q^{1/5}}{1+\\dfrac{q}{1+\\dfrac{q^2}{1+\\dfrac{q^3}{1+\\cdots}}}}$ and $v:=\\dfrac{q^{3/5}}{1+\\dfrac{q^3}{1+\\dfrac{q^6}{1+\\dfrac{q^9}{1+\\cdots}}}}$. Then $(v-u^3)(1+uv^3)=3u^2v^2$."),
    rec("RLN-P1-C03-Entry3-2-12", "Let $u:=\\dfrac{q^{1/5}}{1+\\dfrac{q}{1+\\dfrac{q^2}{1+\\dfrac{q^3}{1+\\cdots}}}}$ and $v:=\\dfrac{q^{1/5}}{1-\\dfrac{q}{1+\\dfrac{q^2}{1-\\dfrac{q^3}{1+\\cdots}}}}$. Then $uv(u-v)^4-u^2v^2(u-v)^2+2u^3v^3+(u-v)(1+u^5v^5)=0$."),
    rec("RLN-P1-C03-Entry3-2-13", "Let $u:=\\dfrac{q^{1/5}}{1+\\dfrac{q}{1+\\dfrac{q^2}{1+\\dfrac{q^3}{1+\\cdots}}}}$ and $v:=\\dfrac{q^{4/5}}{1+\\dfrac{q^4}{1+\\dfrac{q^8}{1+\\dfrac{q^{12}}{1+\\cdots}}}}$. Then $(u^5+v^5)(uv-1)+u^5v^5+uv=5u^2v^2(uv-1)^2$."),
    rec("RLN-P1-C03-Entry3-2-14", "Let $u:=\\dfrac{q^{1/5}}{1+\\dfrac{q}{1+\\dfrac{q^2}{1+\\dfrac{q^3}{1+\\cdots}}}}$ and $v:=\\dfrac{q}{1+\\dfrac{q^5}{1+\\dfrac{q^{10}}{1+\\dfrac{q^{15}}{1+\\cdots}}}}$. Then $u^5=\\dfrac{v(1-2v+4v^2-3v^3+v^4)}{1+3v+4v^2+2v^3+v^4}$."),
    rec("RLN-P1-C03-Entry3-2-15", "If $2u:=11+\\dfrac{(q;q)_\\infty^6}{q(q^5;q^5)_\\infty^6}$ and $2v:=11+\\dfrac{(q^{1/5};q^{1/5})_\\infty}{q^{1/5}(q^5;q^5)_\\infty}$, then $5\\sqrt{u^2+1-u}=\\sqrt{v^2+1-v}=\\dfrac{q^{1/5}(q;q^5)_\\infty(q^4;q^5)_\\infty}{(q^2;q^5)_\\infty(q^3;q^5)_\\infty}$."),
    rec("RLN-P1-C03-Entry3-3-1", "Let $v=\\dfrac{q^{1/3}}{1+\\dfrac{q+q^2}{1+\\dfrac{q^2+q^4}{1+\\dfrac{q^3+q^6}{1+\\cdots}}}}$, $|q|<1$. Then (a) $v=\\dfrac{q^{1/3}(q;q^2)_\\infty}{(q^3;q^6)_\\infty^3}$; (b) $\\dfrac{1}{v}=\\dfrac{\\psi(q^{1/3})}{q^{1/3}\\psi(q^3)}-1=\\sqrt{\\dfrac{\\psi^4(q)}{q\\psi^4(q^3)}-1}$; (c) $2v=1-\\dfrac{\\varphi(-q^{1/3})}{\\varphi(-q)}=\\sqrt{1-\\dfrac{\\varphi^4(-q)}{\\varphi^4(-q^3)}}$; (d) $v+4v^2=3+\\dfrac{f^3(-q^{1/3})}{q^{1/3}f^3(-q^3)}=\\sqrt{27+\\dfrac{f^{12}(-q)}{qf^{12}(-q^3)}}$."),
    rec("RLN-P1-C03-Entry3-4-1", "$G(e^{-\\pi\\sqrt{10}})=\\sqrt{9+3\\sqrt{6}}-\\sqrt{7+3\\sqrt{6}}\\sqrt{(1+\\sqrt{5})\\sqrt{\\sqrt{6}+\\sqrt{3}}}$."),
]
