"""RLN Part 1, Chapter 2 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C02 = ["explicit-evaluations-rogers-ramanujan-continued-fraction"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C02}


CHAPTER_2 = [
    rec("RLN-P1-C02-Entry2-2-1", "With $S(q)=-R(-q)$, we have $S(e^{-\\pi\\sqrt{3}})=-(3+\\sqrt{5})+\\sqrt{6(5+\\sqrt{5})}$."),
    rec("RLN-P1-C02-Entry2-2-2", "$S(e^{-\\pi/\\sqrt{35}})=\\left(\\sqrt{5}-7+\\sqrt{35(5-2\\sqrt{5})}\\right)^{1/5}$."),
    rec("RLN-P1-C02-Entry2-2-3", "$S(e^{-\\pi\\sqrt{7/5}})=\\left(-5\\sqrt{5}-7+\\sqrt{35(5+2\\sqrt{5})}\\right)^{1/5}$."),
    rec("RLN-P1-C02-Entry2-2-4", "$S(e^{-\\pi/\\sqrt{15}})=\\left(5\\sqrt{5}-3+\\sqrt{30(5-\\sqrt{5})}\\right)^{1/5}$."),
    rec("RLN-P1-C02-Entry2-2-5", "$S(e^{-\\pi\\sqrt{3/5}})=\\left(-5\\sqrt{5}-3+\\sqrt{30(5+\\sqrt{5})}\\right)^{1/5}$."),
    rec("RLN-P1-C02-Entry2-4-1", "$S^5(e^{-\\pi/\\sqrt{5}})=\\sqrt{\\left(\\dfrac{5\\sqrt{5}-11}{2}\\right)^2+1}-\\dfrac{5\\sqrt{5}-11}{2}$."),
    rec("RLN-P1-C02-Entry2-4-2", "Let $a=2\\sqrt{15}$ and $b=3\\sqrt{5}-1$. If $2c=\\dfrac{a+b}{a-b^5\\sqrt{5-11}}$, then $S^5(e^{-\\pi\\sqrt{9/5}})=\\sqrt{c^2+1-c}$."),
    rec("RLN-P1-C02-Entry2-4-3", "If $A_1'^2=\\sqrt{\\sqrt{5}+7}-\\sqrt{\\sqrt{5}-1}\\sqrt{\\sqrt{5}+27}-\\sqrt{\\sqrt{5}+19}$ and $2c=A_1'^6-11$, then $S^5(e^{-\\pi\\sqrt{11/5}})=\\sqrt{c^2+1-c}$."),
    rec("RLN-P1-C02-Entry2-4-4", "If $A_1'^2=\\sqrt{\\sqrt{65}+7}-\\sqrt{\\sqrt{65}-1}\\sqrt{\\sqrt{65}+9}-\\sqrt{\\sqrt{65}+7}$ and $2c=A_1'^6-11$, then $S^5(e^{-\\pi\\sqrt{13/5}})=\\sqrt{c^2+1-c}$."),
    rec("RLN-P1-C02-Entry2-5-1", "Let $t_1(q):=q^{1/6}\\dfrac{\\chi(-q)}{\\chi(-q^5)}$ and $s_1(q):=\\dfrac{\\varphi(-q)}{\\varphi(-q^5)}$. Then (i) $\\dfrac{f(-q)}{q^{1/6}f(-q^5)}=\\dfrac{s_1}{t_1}$; (ii) $\\dfrac{f(-q^2)}{q^{1/3}f(-q^{10})}=\\dfrac{s_1}{t_1^2}$; (iii) $\\dfrac{\\psi(q)}{\\sqrt{q}\\,\\psi(q^5)}=\\dfrac{s_1}{t_1^3}$; (iv) $s_1^2=\\dfrac{1}{2}\\left((1+t_1^6)+\\sqrt{(1+t_1^6)^2-20t_1^6}\\right)$."),
    rec("RLN-P1-C02-Entry2-6-1", "Let $t_2$ be as in Theorem 2.5.1. Then (i) $R(q)=\\dfrac{1}{4t_2}\\left(\\dfrac{1+t_2}{\\sqrt{5}+1}\\sqrt{1-t_2}-\\sqrt{(1-t_2)\\left(\\dfrac{1+t_2}{\\sqrt{5}+1}\\right)^2-2t_2(\\sqrt{5}+1)}\\right)\\left(-\\dfrac{1-t_2}{\\sqrt{5}-1}\\sqrt{1-t_2}+\\sqrt{(1-t_2)\\left(\\dfrac{1-t_2}{\\sqrt{5}-1}\\right)^2+2t_2(\\sqrt{5}-1)}\\right)$; (ii) $R(q^2)=\\dfrac{1}{4t_2^2}\\left(\\dfrac{1-t_2}{\\sqrt{5}+1}\\sqrt{1-t_2}-\\sqrt{(1-t_2)\\left(\\dfrac{1+t_2}{\\sqrt{5}+1}\\right)^2-2t_2(\\sqrt{5}+1)}\\right)\\left(-\\dfrac{1+t_2}{\\sqrt{5}-1}\\sqrt{1-t_2}+\\sqrt{(1-t_2)\\left(\\dfrac{1-t_2}{\\sqrt{5}-1}\\right)^2+2t_2(\\sqrt{5}-1)}\\right)$."),
    rec("RLN-P1-C02-Entry2-6-2", "Let $t_1$ be as in Entry 2.5.1 and $k=R(q)R^2(q^2)$. Then $R(q)=k^{1/5}\\left(\\dfrac{1-k}{1+k}\\right)^{2/5}$ and $R(q^2)=k^{2/5}\\left(\\dfrac{1+k}{1-k}\\right)^{1/5}$. Furthermore, $k=4t_1^6\\left(\\sqrt{1-t_1^6}-\\sqrt[6]{1-t_1^6}\\left(\\dfrac{\\sqrt{5}+1}{2}\\right)^6\\right)\\left(\\sqrt[6]{1-t_1^6}\\left(\\dfrac{\\sqrt{5}-1}{2}\\right)^6-\\sqrt{1-t_1^6}\\right)$ and $\\dfrac{1-k}{1+k}=\\dfrac{1}{\\left(\\sqrt[6]{\\left(\\frac{\\sqrt{5}+1}{2}\\right)^6-t_1^6}-\\sqrt{1-t_1^6}\\right)\\left(\\sqrt[6]{\\left(\\frac{\\sqrt{5}-1}{2}\\right)^6-t_1^6}+\\sqrt{1-t_1^6}\\right)}$."),
]
