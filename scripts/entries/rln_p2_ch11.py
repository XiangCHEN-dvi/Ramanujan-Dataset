"""RLN Part 2, Chapter 11 — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C11 = ["eisenstein-series-coefficient-formulas"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C11}


CHAPTER_11 = [
    rec(
        "RLN-P2-C11-Entry11-3-1",
        "With Q(q) = 1+240\\sum_{k=1}^{\\infty}k^3q^k/(1-q^k) and "
        "R(q) = 1-504\\sum_{k=1}^{\\infty}k^5q^k/(1-q^k), let "
        "1/Q(q^2) = \\sum_{n=0}^{\\infty}\\beta_n q^{2n} and "
        "G := R(e^{2\\pi i\\rho}) = 1-504\\sum_{k=1}^{\\infty}"
        "(-1)^k k^5/(e^{k\\pi\\sqrt{3}}-(-1)^k), where "
        "\\rho := -\\tfrac12 + i\\sqrt{3}/2. Then "
        "\\beta_n = \\frac{(-1)^n}{3G}\\sum_{(\\lambda)}"
        "\\frac{h_{\\lambda}(n)}{\\lambda^3}e^{n\\pi\\sqrt{3}/\\lambda}, "
        "where \\lambda runs over integers of the form "
        "\\lambda = 3^a\\prod_{j=1}^r p_j^{a_j} with a \\in\\{0,1\\} and "
        "p_j \\equiv 1 \\pmod{6}, h_1(n)=1, h_3(n)=-1, and for \\lambda\\ge 7, "
        "h_{\\lambda}(n) = 2\\sum_{(c,d)}\\cos\\left(\\frac{(ad+bc-2ac-2bd+\\lambda)n\\pi}"
        "{\\lambda}-6\\arctan\\frac{c}{\\sqrt{3}(2d-c)}\\right), "
        "the sum over distinct solutions to \\lambda=c^2-cd+d^2 with ad-bc=1. "
        "If n<0 the sum equals 0.",
    ),
    rec(
        "RLN-P2-C11-Entry11-4-1",
        "Let Q(q^2)/R(q^2) = \\sum_{n=0}^{\\infty}\\delta_n q^{2n} and "
        "J = Q(e^{-2\\pi}) = 1+240\\sum_{k=1}^{\\infty}k^3/(e^{2\\pi k}-1). "
        "For n\\ge 0, "
        "\\delta_n = \\frac{2}{J}\\sum_{(\\mu)}\\frac{v_{\\mu}(n)}{\\mu^2}"
        "e^{2n\\pi/\\mu}, where \\mu runs over integers of the form "
        "\\mu = 2^a\\prod_{j=1}^r p_j^{a_j} with a\\in\\{0,1\\} and "
        "p_j\\equiv 1\\pmod{4}, v_1(n)=1, v_2(n)=(-1)^{n+1}, and for \\mu\\ge 5, "
        "v_{\\mu}(n) = 2\\sum_{(c,d)}\\cos\\left(\\frac{(ac+bd)^2 n\\pi}{\\mu}"
        "+4\\arctan\\frac{c}{d}\\right), the sum over distinct solutions to "
        "\\mu=c^2+d^2 with ad-bc=1. If n<0 the sum equals 0.",
    ),
    rec(
        "RLN-P2-C11-Entry11-5-1",
        "Let \\frac{\\pi}{3}\\frac{P(q^2)}{R(q^2)} = \\sum_{n=0}^{\\infty}\\eta_{1,n}q^{2n} "
        "and \\left(\\frac{\\pi}{3}\\frac{P(q^2)}{R(q^2)}\\right)^2 "
        "= \\sum_{n=0}^{\\infty}\\eta_{2,n}q^{2n}, with "
        "C := 1+480\\sum_{k=1}^{\\infty}k^7/(e^{2\\pi k}-1). "
        "For n\\ge 0, "
        "\\eta_{1,n} = \\frac{2}{C}\\sum_{(\\mu)}\\frac{W_{\\mu}(n)}{\\mu^3}"
        "e^{2n\\pi/\\mu} and "
        "\\eta_{2,n} = \\frac{2}{C}\\sum_{(\\mu)}\\frac{W_{\\mu}(n)}{\\mu^2}"
        "e^{2n\\pi/\\mu}, where \\mu runs over integers of the form (11.4.4), "
        "W_1(n)=1, W_2(n)=-(-1)^n, and for \\mu\\ge 5, "
        "W_{\\mu}(n) = 2\\sum_{(c,d)}\\cos\\left(\\frac{(ac+bd)^2 n\\pi}{\\mu}"
        "+8\\arctan\\frac{c}{d}\\right). If n<0 both sums equal 0.",
    ),
    rec(
        "RLN-P2-C11-Entry11-6-1",
        "Let f(q) := \\frac{\\pi P(q^2)}{2\\sqrt{3}\\,Q(q^2)} "
        "= \\sum_{n=0}^{\\infty}\\theta_n q^{2n}. For n\\ge 0, "
        "\\theta_n = \\frac{(-1)^n}{3G}\\sum_{(\\lambda)}"
        "\\frac{h_{\\lambda}(n)}{\\lambda^2}e^{n\\pi\\sqrt{3}/\\lambda}, "
        "where \\lambda runs over integers of the form (11.3.4) and G and "
        "h_{\\lambda}(n) are as in Entry 11.3.1. If n<0 the sum equals 0.",
    ),
    rec(
        "RLN-P2-C11-Entry11-7-1",
        "With Q(q), R(q), B(q) = 1+24\\sum_{k=1}^{\\infty}"
        "(2k-1)q^{2k-1}/(1-q^{2k-1}), "
        "\\varphi(q) = \\sum_{k=-\\infty}^{\\infty}q^{k^2}, and "
        "\\psi(q) = \\sum_{k=0}^{\\infty}q^{k(k+1)/2}: "
        "(i) B(\\sqrt{q})+B(-\\sqrt{q})=2B(q); "
        "(ii) B(\\sqrt{q})B(-\\sqrt{q})B(q)=R(q); "
        "(iii) Q(q)+4Q(q^2)=5B^2(q); "
        "(iv) -R(q)+8R(q^2)=7B^3(q); "
        "(v) \\frac{2}{3}\\left(\\frac{1}{B(\\sqrt{q})}+\\frac{1}{B(-\\sqrt{q})}\\right)"
        "-\\frac{1}{3B(q)}=\\frac{Q(q)}{R(q)}; "
        "(vi) \\frac{11}{24}\\left(\\frac{1}{B(\\sqrt{q})}+\\frac{1}{B(-\\sqrt{q})}\\right)"
        "+\\frac{1}{12B(q)}=\\frac{Q(q^2)}{R(q)}; "
        "(vii) -Q(q)+16Q(q^2)=15\\varphi^8(-q); "
        "(viii) Q(q)-Q(q^2)=240q\\psi^8(q).",
    ),
    rec(
        "RLN-P2-C11-Entry11-8-1",
        "Let 1/B(q) = \\sum_{n=0}^{\\infty}b_n q^n and "
        "V_{\\mu}(n) = \\frac{2}{J}\\frac{v_{\\mu}(n)}{\\mu^2}e^{2n\\pi/\\mu}. "
        "Then b_n = -3\\sum_{(\\mu_e)}V_{\\mu_e}(n), where \\mu_e runs over the "
        "even integers of the form (11.4.4).",
    ),
    rec(
        "RLN-P2-C11-Entry11-9-1",
        "Suppose Entry 11.8.1 holds. With "
        "Q(q^2)/R(q) = \\sum_{n=0}^{\\infty}\\sigma_n q^n, "
        "\\varphi^8(-q)/R(q) = \\sum_{n=0}^{\\infty}v_n q^n, and "
        "q\\psi^8(q)/R(q) = \\sum_{n=0}^{\\infty}\\chi_n q^n: "
        "(i) \\sigma_n = \\frac{11}{16}\\sum_{(\\mu_o)}V_{\\mu_o}(n)"
        "-\\frac14\\sum_{(\\mu_e)}V_{\\mu_e}(n); "
        "(ii) v_n = \\frac{2}{3}\\sum_{(\\mu_o)}V_{\\mu_o}(n)"
        "-\\frac13\\sum_{(\\mu_e)}V_{\\mu_e}(n); "
        "(iii) \\chi_n = \\frac{1}{768}\\sum_{(\\mu_o)}V_{\\mu_o}(n)"
        "+\\frac{1}{192}\\sum_{(\\mu_e)}V_{\\mu_e}(n), "
        "where \\mu_o and \\mu_e run over odd and even integers of the form (11.4.4).",
    ),
    rec(
        "RLN-P2-C11-Entry11-10-1",
        "Let 1/R(q^2) = \\sum_{n=0}^{\\infty}p_n q^{2n}. For n\\ge 0, "
        "p_n = \\sum_{(\\mu)}T_{\\mu}(n), where \\mu runs over integers of the form "
        "(11.4.4), T_1(n) = \\frac{2}{Q^2(e^{-2\\pi})}e^{2n\\pi}, "
        "T_2(n) = \\frac{2}{Q^2(e^{-2\\pi})}\\frac{(-1)^n}{2^4}e^{n\\pi}, and for \\mu>2, "
        "T_{\\mu}(n) = \\frac{2}{Q^2(e^{-2\\pi})}\\frac{e^{2n\\pi/\\mu}}{\\mu^4}"
        "\\sum_{(c,d)}2\\cos\\left(\\frac{(ac+bd)^2\\pi n}{\\mu}"
        "+8\\tan^{-1}\\frac{c}{d}\\right).",
    ),
    rec(
        "RLN-P2-C11-Entry11-10-2",
        "Let 1/B^2(q^2) = \\sum_{n=0}^{\\infty}b'_n q^{2n}. Then "
        "b'_n = 18\\sum_{(\\mu_e)}\\left(n+\\frac{3\\mu_e}{2\\pi}\\right)T_{\\mu_e}(n), "
        "where the sum is over even integers \\mu_e of the form (11.4.4) and "
        "T_{\\mu_e}(n) is as in Entry 11.10.1.",
    ),
    rec(
        "RLN-P2-C11-Entry11-10-3",
        "Let P(q^2)/R(q^2) = \\sum_{n=0}^{\\infty}\\eta_n q^{2n}. For n\\ge 0, "
        "\\eta_n = \\frac{3}{\\pi}\\sum_{(\\mu)}\\mu\\,T_{\\mu}(n), where \\mu runs over "
        "integers of the form (11.4.4) and T_{\\mu}(n) is as in Entry 11.10.1.",
    ),
    rec(
        "RLN-P2-C11-Entry11-11-1",
        "The first thirteen coefficients in the expansion of 1/R(q) = "
        "\\sum_{n=0}^{\\infty}p_n q^n are "
        "p_0=1, p_1=504, p_2=270648, p_3=144912096, "
        "p_4=77599626552, p_5=41553943041744, "
        "p_6=22251789971649504, p_7=11915647845248387520, "
        "p_8=6380729991419236488504, p_9=3416827666558895485479576, "
        "p_{10}=1829682703808504464920468048, "
        "p_{11}=979779820147442370107345764512, "
        "p_{12}=524663917940510191509934144603104.",
    ),
]
