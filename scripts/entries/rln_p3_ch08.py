"""RLN Part 3, Chapter 8 — AI curated LaTeX (Entry only)."""

from __future__ import annotations

TOPICS_C08 = ["forty-rogers-ramanujan-identities"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C08}


CHAPTER_8 = [
    rec(
        "RLN-P3-C08-Entry8-3-1",
        r"$G^{11}(q)H(q) - q^2 G(q)H^{11}(q) = 1 + 11q\, G^6(q)H^6(q)$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-2",
        r"$G(q)G(q^4) + q H(q)H(q^4) = \chi^2(q) = \dfrac{\varphi(q)}{f(-q^2)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-3",
        r"$G(q)G(q^4) - q H(q)H(q^4) = \dfrac{\varphi(q^5)}{f(-q^2)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-4",
        r"$G(q^{11})H(q) - q^2 G(q)H(q^{11}) = 1$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-5",
        r"$G(q^{16})H(q) - q^3 G(q)H(q^{16}) = \chi(q^2)$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-6",
        r"$G(q)G(q^9) + q^2 H(q)H(q^9) = \dfrac{f^2(-q^3)}{f(-q)f(-q^9)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-7",
        r"$G(q^2)G(q^3) + q H(q^2)H(q^3) = \dfrac{\chi(-q^3)}{\chi(-q)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-8",
        r"$G(q^6)H(q) - q G(q)H(q^6) = \dfrac{\chi(-q)}{\chi(-q^3)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-9",
        r"$G(q^7)H(q^2) - q G(q^2)H(q^7) = \dfrac{\chi(-q)}{\chi(-q^7)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-10",
        r"$G(q)G(q^{14}) + q^3 H(q)H(q^{14}) = \dfrac{\chi(-q^7)}{\chi(-q)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-11",
        r"$G(q^8)H(q^3) - q G(q^3)H(q^8) = \dfrac{\chi(-q)\chi(-q^4)}{\chi(-q^3)\chi(-q^{12})}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-12",
        r"$G(q)G(q^{24}) + q^5 H(q)H(q^{24}) = \dfrac{\chi(-q^3)\chi(-q^{12})}{\chi(-q)\chi(-q^4)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-13",
        r"$G(q^9)H(q^4) - q G(q^4)H(q^9) = \dfrac{\chi(-q)\chi(-q^6)}{\chi(-q^3)\chi(-q^{18})}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-14",
        r"$G(q^{36})H(q) - q^7 G(q)H(q^{36}) = \dfrac{\chi(-q^6)\chi(-q^9)}{\chi(-q^2)\chi(-q^3)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-15",
        r"$G(q^3)G(q^7) + q^2 H(q^3)H(q^7) = G(q^{21})H(q) - q^4 G(q)H(q^{21}) = \dfrac{1}{2\sqrt{q}}\chi(q^{1/2})\chi(-q^{3/2})\chi(q^{7/2})\chi(-q^{21/2}) - \dfrac{1}{2\sqrt{q}}\chi(-q^{1/2})\chi(q^{3/2})\chi(-q^{7/2})\chi(q^{21/2})$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-16",
        r"$G(q^2)G(q^{13}) + q^3 H(q^2)H(q^{13}) = G(q^{26})H(q) - q^5 G(q)H(q^{26}) = \dfrac{\chi(-q^{13})}{\chi(-q)} - q\,\dfrac{\chi(-q)}{\chi(-q^{13})}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-17",
        r"$G(q)G(q^{19}) + q^4 H(q)H(q^{19}) = \dfrac{1}{4\sqrt{q}}\chi^2(q^{1/2})\chi^2(q^{19/2}) - \dfrac{1}{4\sqrt{q}}\chi^2(-q^{1/2})\chi^2(-q^{19/2}) - \dfrac{q^2}{\chi^2(-q)\chi^2(-q^{19})}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-18",
        r"$G(q^{31})H(q) - q^6 G(q)H(q^{31}) = \dfrac{1}{2q}\chi(q)\chi(q^{31}) - \dfrac{1}{2q}\chi(-q)\chi(-q^{31}) + \dfrac{q^3}{\chi(-q^2)\chi(-q^{62})}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-19",
        r"$\dfrac{G(q)G(q^{39}) + q^8 H(q)H(q^{39})}{f(-q)f(-q^{39})} = \dfrac{G(q^{13})H(q^3) - q^2 G(q^3)H(q^{13})}{f(-q^3)f(-q^{13})} = \dfrac{1}{2q}\bigl(\varphi(-q^3)\varphi(-q^{13}) - \varphi(-q)\varphi(-q^{39})\bigr)$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-20",
        r"$G(q)H(-q) + G(-q)H(q) = \dfrac{2}{\chi^2(-q^2)} = \dfrac{2\psi(q^2)}{f(-q^2)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-21",
        r"$G(q)H(-q) - G(-q)H(q) = \dfrac{2q\,\psi(q^{10})}{f(-q^2)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-22",
        r"$G(-q)G(-q^4) + q H(-q)H(-q^4) = \chi(q^2)$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-23",
        r"$G(-q^2)G(-q^3) + q H(-q^2)H(-q^3) = \dfrac{\chi(q)\chi(q^6)}{\chi(q^2)\chi(q^3)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-24",
        r"$G(-q^6)H(-q) - q H(-q^6)G(-q) = \dfrac{\chi(q^2)\chi(q^3)}{\chi(q)\chi(q^6)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-25",
        r"$G(-q)G(q^9) - q^2 H(-q)H(q^9) = \dfrac{\chi(-q)\chi(q^9)}{\chi(-q^6)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-26",
        r"$G(q^{11})H(-q) + q^2 G(-q)H(q^{11}) = \dfrac{\chi(q^2)\chi(q^{22})}{\chi(-q^2)\chi(-q^{22})} - \dfrac{2q^3}{\chi(-q^2)\chi(-q^4)\chi(-q^{22})\chi(-q^{44})}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-27",
        r"Define $U := U(q) := G(q)G(q^{44}) + q^9 H(q)H(q^{44})$ and $V := V(q) := G(q^4)G(q^{11}) + q^3 H(q^4)H(q^{11})$. Then $U^2 + q V^2 = \chi^3(q)\chi^3(q^{11})$ and $UV + q = \chi^2(q)\chi^2(q^{11})$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-28",
        r"Define $U := G(q^{17})H(q^2) - q^3 G(q^2)H(q^{17})$ and $V := G(q)G(q^{34}) + q^7 H(q)H(q^{34})$. Then $\dfrac{U}{V} = \dfrac{\chi(-q)}{\chi(-q^{17})}$ and $U^4 V^4 - q U^2 V^2 = \dfrac{\chi^3(-q^{17})}{\chi^3(-q)}\left(1 + q^2\,\dfrac{\chi^3(-q)}{\chi^3(-q^{17})}\right)^2$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-29",
        r"$\bigl(G(q^2)G(q^{23}) + q^5 H(q^2)H(q^{23})\bigr)\bigl(G(q^{46})H(q) - q^9 G(q)H(q^{46})\bigr) = \chi(-q)\chi(-q^{23}) + q + \dfrac{2q^2}{\chi(-q)\chi(-q^{23})}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-30",
        r"$\bigl(G(q^{19})H(q^4) - q^3 G(q^4)H(q^{19})\bigr)\bigl(G(q^{76})H(-q) + q^{15} G(-q)H(q^{76})\bigr) = \dfrac{\chi(-q^2)}{\chi(-q^{38})}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-31",
        r"$\bigl(G(q^2)G(q^{33}) + q^7 H(q^2)H(q^{33})\bigr)\bigl(G(q^{66})H(q) - q^{13} H(q^{66})G(q)\bigr) = \dfrac{\chi(-q^3)}{\chi(-q^{11})}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-32",
        r"$\bigl(G(q^3)G(q^{22}) + q^5 H(q^3)H(q^{22})\bigr)\bigl(G(q^{11})H(q^6) - q G(q^6)H(q^{11})\bigr) = \dfrac{\chi(-q^{33})}{\chi(-q)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-33",
        r"$\bigl(G(q)G(q^{54}) + q^{11} H(q)H(q^{54})\bigr)\bigl(G(q^{27})H(q^2) - q^5 G(q^2)H(q^{27})\bigr) = \dfrac{\chi(-q^3)\chi(-q^{27})}{\chi(-q)\chi(-q^9)}$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-34",
        r"$\bigl(G(q)G(-q^{19}) - q^4 H(q)H(-q^{19})\bigr)\bigl(G(-q)G(q^{19}) - q^4 H(-q)H(q^{19})\bigr) = G(q^2)G(q^{38}) + q^8 H(q^2)H(q^{38})$.",
    ),
    rec(
        "RLN-P3-C08-Entry8-3-35",
        r"$\bigl(G(q)G(q^{94}) + q^{19} H(q)H(q^{94})\bigr)\bigl(G(q^{47})H(q^2) - q^9 G(q^2)H(q^{47})\bigr) = \chi(-q)\chi(-q^{47}) + 2q^2 + \dfrac{2q^4}{\chi(-q)\chi(-q^{47})} + q\sqrt{\dfrac{4\chi(-q)\chi(-q^{47}) + 9q^2 + 8q^4}{\chi(-q)\chi(-q^{47})}}$.",
    ),
]
