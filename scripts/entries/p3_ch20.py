"""Part III, Chapter 20 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C20 = ["modular-equations-higher-composite-degrees"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C20}


CHAPTER_20 = [
    rec(
        "RN-P3-C20-Entry01",
        r"Define $v:=q^{1/3}\chi(-q)/\chi^3(-q^3)$. Then "
        r"(i) $v=\dfrac{q^{1/3}\psi(q^3)}{f(q,q^2)}=1+\dfrac{q}{1}+\dfrac{q^2}{1+q}+\dfrac{q^4}{1+q^2}+\dfrac{q^6}{1+q^3}+\cdots$ "
        r"and $1+\dfrac{1}{v}=\dfrac{\psi^4(q)}{q\psi^4(q^3)}$; "
        r"(ii) $1-2v=\dfrac{\varphi^4(-q)}{\varphi^4(-q^3)}=\dfrac{\psi(q)}{\varphi(-q^3)}-\dfrac{3q\psi(q^9)}{\varphi(-q^3)}$ "
        r"and $1-8v=\left(\dfrac{\varphi(-q^{1/3})\varphi(-\omega q^{1/3})\varphi(-\omega^2 q^{1/3})}{\varphi^4(-q)}\right)^{1/3}$; "
        r"(iii) $1-8v=\dfrac{\psi(q)}{\varphi(-q^3)}-\dfrac{3q\psi(q^9)}{\varphi(-q^3)}$ "
        r"and $1-8v=\left(\dfrac{\varphi^4(-q)}{\varphi^4(-q^3)}\right)^{1/3}$; "
        r"(iv) $\dfrac{f^3(-q^{1/3})}{q^{1/3}f^3(-q^3)}=\dfrac{\varphi^2(-q^{1/3})\psi(q^{1/3})}{q^{1/3}\varphi^2(-q^3)\psi(q^3)}"
        r"=\dfrac{1}{(1-2v)^2(1+v)}=4v^2+v-3$ and "
        r"$\dfrac{q^2f^6(-q)}{f^6(-q^3)}=(4v^2+v-3)^3-27$; "
        r"(v) $f^3(-q^{1/3})+3q^{1/3}f^3(-q^3)-f(-q)=6f(-q)\sum_{n=0}^{\infty}\left(\dfrac{q^{3n+1}}{1-q^{3n+1}}-\dfrac{q^{3n+2}}{1-q^{3n+2}}\right)$.",
    ),
    rec(
        "RN-P3-C20-Entry02",
        r"We have "
        r"(i) $\varphi(q)\varphi(q^9)-\varphi^2(q^3)=2q\varphi(-q^2)\psi(q^9)\chi(q^3)$; "
        r"(ii) $\dfrac{\psi(q)}{\varphi(-q^3)}-\dfrac{3q\psi(q^9)}{\varphi(-q^3)}=\dfrac{q^{1/3}\psi(q^{1/3})}{v\varphi(-q^3)}$; "
        r"(iii) $\varphi(q)\varphi(q^9)+\varphi^2(q^3)=2\psi(q)\varphi(-q^{18})\chi(q^3)$; "
        r"(iv) $\psi(q^{1/9})-q^{1/9}\psi(q)=f(q^4,q^5)+q^{1/3}f(q^2,q^7)+q^{2/3}f(q,q^8)$; "
        r"(v) $f(-q^{1/3})=f(-q^4,-q^5)-q^{1/3}f(-q^2,-q^7)-q^{2/3}f(-q,-q^8)$; "
        r"(vi) $f(-q,-q^8)f(-q^2,-q^7)f(-q^4,-q^5)=f(-q^3,-q^6)^3$; "
        r"(vii) $\dfrac{f(-q^4,-q^5)+f(-q,-q^8)-f(-q^2,-q^7)}{f(-q^2,-q^7)}"
        r"=\dfrac{qf(-q^4,-q^5)-f(-q,-q^8)}{f(-q^2,-q^7)}$; "
        r"(viii) $\dfrac{f(-q^4,-q^5)+f(-q^2,-q^7)}{f(-q,-q^8)}"
        r"=\dfrac{f^4(-q^3)}{q}+\dfrac{f(-q,-q^8)f(-q^4,-q^5)f(-q^2,-q^7)}{f(-q)f^3(-q^9)}$; "
        r"(ix) $\varphi(q)=\varphi(q^{81})+2qf(q^{63},q^{99})+2q^4f(q^{45},q^{117})+2q^9f(q^{27},q^{135})+2q^{16}f(q^9,q^{153})$.",
    ),
    rec(
        "RN-P3-C20-Entry03",
        r"Let $\beta$ and $\gamma$ be of the third and ninth degrees, respectively, with respect to $\alpha$. "
        r"Let $m=\chi_1/\chi_3$ and $m'=\chi_3/\chi_9$. Then "
        r"(i) $\dfrac{((1-\beta)^3)^{1/4}+(\beta^3)^{1/4}-1}{((1-\alpha)(1-\beta))^{1/4}}=m=\dfrac{1-(\alpha\beta)^{1/4}}{(\alpha\beta)^{1/4}}$; "
        r"(ii) $1+\dfrac{(\beta^3(1-\beta)^3)^{1/8}}{\beta(1-\beta)}"
        r"=\dfrac{m}{2}\{1+(\alpha\beta)^{1/2}+\{(1-\alpha)(1-\beta)\}^{1/2}\}^{1/2}$; "
        r"(iii) $1-2^{4/3}\dfrac{(\alpha^3\gamma^3(1-\alpha)^3(1-\gamma)^3)^{1/24}}{\beta^2(1-\beta)^2}"
        r"=\dfrac{1-2t}{1+2t}=\dfrac{m'}{m}$; "
        r"(iv) $\varphi(q)\varphi(q^9)-\varphi^2(q^3)=2q\varphi(-q^2)\psi(q^9)\chi(q^3)$ and "
        r"$\varphi(q)\varphi(q^9)+\varphi^2(q^3)=2\psi(q)\varphi(-q^{18})\chi(q^3)$; "
        r"(v) $(\alpha\gamma)^{1/2}+\{(1-\alpha)(1-\gamma)\}^{1/2}"
        r"=1-2\{4\beta(1-\beta)\}^{1/3}+8\{\beta(1-\beta)\}^{1/4}\{\alpha\gamma(1-\alpha)(1-\gamma)\}^{1/8}$; "
        r"(vi) $\dfrac{(\alpha(1-\gamma))^{1/8}}{4m'}+\dfrac{(\gamma(1-\alpha))^{1/8}}{4m'}"
        r"=\dfrac{(\gamma(1-\gamma))^{1/8}}{\alpha(1-\alpha)}+\dfrac{1}{\alpha(1-\alpha)}$; "
        r"(vii) $\dfrac{((1-\beta)^3)^{1/4}-1}{1-\alpha}=\dfrac{8m'(m'+3m)}{(m^2-1)(9-m'^2)}$ and "
        r"$\dfrac{(\beta^3)^{1/4}}{1-\beta}=\dfrac{8m'(m'+3m)}{(m^2-1)(9-m'^2)}$; "
        r"(viii) $1+\dfrac{(\beta^3(1-\beta)^3)^{1/8}}{\alpha(1-\alpha)}=\dfrac{m}{2}\{1+(\alpha\beta)^{1/2}+\{(1-\alpha)(1-\beta)\}^{1/2}\}^{1/2}$; "
        r"(ix) $1+\dfrac{(\alpha^3(1-\alpha)^3)^{1/8}}{\beta(1-\beta)}"
        r"=\dfrac{m'}{2}\{1+(\alpha\gamma)^{1/2}+\{(1-\alpha)(1-\gamma)\}^{1/2}\}^{1/2}$; "
        r"(x) $\dfrac{(\alpha)^{1/8}}{1-\alpha}+\dfrac{(\gamma)^{1/8}}{1-\gamma}=\dfrac{(\gamma(1-\gamma))^{1/8}}{\alpha(1-\alpha)}+\dfrac{1}{\alpha(1-\alpha)}$; "
        r"(xi) $\dfrac{(\gamma)^{1/8}}{1-\gamma}+\dfrac{(\alpha)^{1/8}}{1-\alpha}=\dfrac{(\alpha(1-\alpha))^{1/8}}{\gamma(1-\gamma)}+\dfrac{1}{\gamma(1-\gamma)}$; "
        r"(xii) $\dfrac{(\beta^2)^{1/4}+((1-\beta)^2)^{1/4}}{\alpha\gamma+(1-\alpha)(1-\gamma)}"
        r"=\dfrac{(\beta^3)^{1/4}}{(\beta\gamma)^{1/4}}+\dfrac{((1-\beta)^3)^{1/4}}{\{(1-\beta)(1-\gamma)\}^{1/4}}=\dfrac{3}{m''}$; "
        r"(xiii) $\dfrac{(\alpha\gamma)^{1/4}+\{(1-\alpha)(1-\gamma)\}^{1/4}-(\alpha\gamma(1-\alpha)(1-\gamma))^{1/4}}{\beta^2+(1-\beta)^2+\beta^2(1-\beta)^2}"
        r"=\dfrac{m'}{m}$; "
        r"(xiv) $2^{1/3}\dfrac{\{\beta(1-\beta)\}^{1/24}}{m}=\dfrac{\{\alpha(1-\gamma)\}^{1/8}-\{\gamma(1-\alpha)\}^{1/8}}{\sqrt{m'}}$; "
        r"(xv) $(\alpha^{1/4}-\gamma^{1/4})^4+\{(1-\gamma)^{1/4}-(1-\alpha)^{1/4}\}^4"
        r"=\left(\{\alpha(1-\gamma)\}^{1/4}-\{\gamma(1-\alpha)\}^{1/4}\right)^4$; "
        r"(xvi) $\dfrac{m'}{m}=(\alpha\gamma)^{1/2}+\{(1-\alpha)(1-\gamma)\}^{1/2}+2\{4\beta(1-\beta)\}^{1/3}$.",
    ),
    rec(
        "RN-P3-C20-Entry04",
        r"We have "
        r"(i) $\dfrac{(\alpha(1-\gamma))^{1/8}}{4m'}+\dfrac{(\gamma(1-\alpha))^{1/8}}{4m'}"
        r"=\dfrac{(\gamma(1-\gamma))^{1/8}}{\alpha(1-\alpha)}+\dfrac{1}{\alpha(1-\alpha)}$; "
        r"(ii) $\dfrac{(\gamma)^{1/8}}{1-\gamma}+\dfrac{(\alpha)^{1/8}}{1-\alpha}=\dfrac{(\alpha(1-\alpha))^{1/8}}{\gamma(1-\gamma)}+\dfrac{1}{\gamma(1-\gamma)}$; "
        r"(iii) $\dfrac{\varphi(-q^2)\varphi(-q^{54})}{\varphi(-q^6)\varphi(-q^{18})}"
        r"=\dfrac{\psi(q)\psi(q^{27})-\psi(-q)\psi(-q^{27})}{\psi(q^3)\psi(q^9)}+q^2$ "
        r"and $\dfrac{\varphi(-q^9)\psi(q^{27})+\varphi(q^9)\psi(-q^{27})}{\varphi(-q^{18})\varphi(-q^{54})}=0$; "
        r"(iv) $\varphi(q)\varphi(q^{27})-\varphi(-q)\varphi(-q^{27})=4qf(-q^6)f(-q^{18})+4q^7\psi(q^2)\psi(q^{54})$.",
    ),
    rec(
        "RN-P3-C20-Entry05",
        r"Let $\alpha$, $\beta$, $\gamma$, and $\delta$ be of the first, third, ninth, and twenty-seventh degrees, respectively. "
        r"Let $m$ be the multiplier connecting $\alpha$ and $\beta$, and let $m''$ denote the multiplier associated with $\gamma$ and $\delta$. Then "
        r"(i) $(\alpha\delta)^{1/8}+\{(1-\alpha)(1-\delta)\}^{1/8}+\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/8}=\sqrt{m}$; "
        r"(ii) $\dfrac{(\beta\gamma)^{1/4}+\{(1-\beta)(1-\gamma)\}^{1/4}+\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/4}}{\alpha\delta+(1-\alpha)(1-\delta)+\alpha\delta(1-\alpha)(1-\delta)}"
        r"=\dfrac{(\alpha\delta)^{1/8}+\{(1-\alpha)(1-\delta)\}^{1/8}}{\beta\gamma+(1-\beta)(1-\gamma)}$; "
        r"(iii) $\dfrac{\varphi(q)\varphi(q^{27})-\varphi(-q)\varphi(-q^{27})}{\varphi(-q^2)\varphi(-q^{54})}"
        r"=\dfrac{2\psi(q^2)\varphi(-q^6)}{\varphi(-q)\psi(q^3)}-\dfrac{\varphi(-q^9)\psi(q^{27})+\varphi(q^9)\psi(-q^{27})}{\varphi(-q^{18})\varphi(-q^{54})}$; "
        r"(iv) $1-(\alpha\delta)^{1/4}-\{(1-\alpha)(1-\delta)\}^{1/4}=\dfrac{2\{16\beta\gamma(1-\beta)(1-\gamma)\}^{1/12}}{\sqrt{m'}}$ and "
        r"$\dfrac{\{16\beta\gamma(1-\beta)(1-\gamma)\}^{1/24}+\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/8}}{\sqrt{m'}}"
        r"=\dfrac{\{16\beta\gamma(1-\beta)(1-\gamma)\}^{1/8}}{\sqrt{m'}}$.",
    ),
    rec(
        "RN-P3-C20-Entry06",
        r"We have "
        r"(i) $\psi(q^{1/11})-q^{15/11}\psi(q^{11})=f(q^5,q^6)+q^{1/11}f(q,q^7)+q^{3/11}f(q^3,q^8)+q^{6/11}f(q^2,q^9)+q^{10/11}f(q,q^{10})$; "
        r"(ii) $\varphi(q^{1/11})-\varphi(q^{11})=2q^{1/11}f(q^9,q^{13})+2q^{4/11}f(q^7,q^{15})+2q^{9/11}f(q^5,q^{17})+2q^{16/11}f(q^3,q^{19})+2q^{25/11}f(q,q^{21})$; "
        r"(iii) $f(-q^{1/11})=q^{5/11}\dfrac{f(-q^{11})}{q}-q^{1/11}f(-q^2,-q^9)+f(-q^4,-q^7)-q^{2/11}f(-q^6,-q^5)"
        r"+q^{7/11}f(-q^8,-q^3)-q^{15/11}f(-q^{10},-q)$.",
    ),
    rec(
        "RN-P3-C20-Entry07",
        r"The following are modular equations of degree $11$, where $m$ is the multiplier connecting $\alpha$ and $\beta$: "
        r"(i) $(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}+2\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/12}=1$; "
        r"(ii) $\dfrac{m}{m'}-\dfrac{m'}{m}=2\{(\alpha\beta)^{1/4}-\{(1-\alpha)(1-\beta)\}^{1/4}\}$; "
        r"(iii) $\dfrac{m}{m'}+\dfrac{m'}{m}=2\sqrt{2}\{2+(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}\}\{1+(\alpha\beta)^{1/2}+\{(1-\alpha)(1-\beta)\}^{1/2}\}^{1/2}$; "
        r"(iv) $\dfrac{((1-\beta)^3)^{1/8}}{1-\alpha}-\dfrac{(\beta^3)^{1/8}}{\beta}-\dfrac{(\beta^3(1-\beta)^3)^{1/8}}{\beta(1-\beta)}"
        r"=\dfrac{1}{\sqrt{2}}\{1+(\alpha\beta)^{1/2}+\{(1-\alpha)(1-\beta)\}^{1/2}\}^{1/2}$; "
        r"(v) $\dfrac{(\alpha^3)^{1/8}}{1-\beta}-\dfrac{((1-\alpha)^3)^{1/8}}{\alpha}-\dfrac{(\alpha^3(1-\alpha)^3)^{1/8}}{\alpha(1-\alpha)}"
        r"=\dfrac{11}{m\sqrt{2}}\{1+(\alpha\beta)^{1/2}+\{(1-\alpha)(1-\beta)\}^{1/2}\}^{1/2}$; "
        r"(vi) $\dfrac{1}{m}\{1+2^{10/3}(\beta^{11}(1-\beta)^{11})^{1/24}\}-\dfrac{1}{m'}\{1+2^{10/3}(\alpha^{11}(1-\alpha)^{11})^{1/24}\}"
        r"=\dfrac{\alpha(1-\alpha)}{\beta(1-\beta)}=2\{(\alpha\beta)^{1/2}-\{(1-\alpha)(1-\beta)\}^{1/2}\}$; "
        r"(vii) $\dfrac{1}{m}\{1+2^{10/3}(\beta^{11}(1-\beta)^{11})^{1/24}\}+\dfrac{1}{m'}\{1+2^{10/3}(\alpha^{11}(1-\alpha)^{11})^{1/24}\}"
        r"=\dfrac{\alpha(1-\alpha)}{\beta(1-\beta)}=2\sqrt{2}\{(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}\}\{1+(\alpha\beta)^{1/2}+\{(1-\alpha)(1-\beta)\}^{1/2}\}^{1/2}$.",
    ),
    rec(
        "RN-P3-C20-Entry08i",
        r"Define "
        r"$\Pi_{11}=\dfrac{f(-q^4,-q^9)}{q^{7/13}f(-q^2,-q^{11})}$, "
        r"$\Pi_{13}=\dfrac{f(-q^2,-q^{11})}{q^{5/13}f(-q,-q^{12})}$, "
        r"$\Pi_{15}=\dfrac{q^{5/13}f(-q^3,-q^{10})}{f(-q^5,-q^8)}$, "
        r"$\Pi_{12}=\dfrac{f(-q^6,-q^7)}{q^{6/13}f(-q^3,-q^{10})}$, "
        r"$\Pi_{14}=\dfrac{f(-q^5,-q^8)}{q^{2/13}f(-q^4,-q^9)}$, and "
        r"$\Pi_{16}=\dfrac{q^{15/13}f(-q,-q^{12})}{f(-q^6,-q^7)}$. Then "
        r"$\dfrac{f(-q^{1/13})}{q^{7/13}f(-q^{13})}=\Pi_{11}-\Pi_{12}-\Pi_{13}+\Pi_{14}+\Pi_{15}-\Pi_{16}$, "
        r"$\dfrac{j^2(-q)}{1+qj^2(-q^{13})}=\Pi_{11}\Pi_{12}-\Pi_{13}\Pi_{15}-\Pi_{14}\Pi_{16}$, "
        r"$\dfrac{-4-qj^2(-q)}{qf^2(-q^{13})}=\dfrac{1}{\Pi_{11}\Pi_{12}\Pi_{13}\Pi_{15}\Pi_{14}\Pi_{16}}$, "
        r"$\dfrac{j^2(-q)}{3+qj^2(-q^{13})}=\Pi_{12}\Pi_{13}\Pi_{14}-\Pi_{11}\Pi_{15}\Pi_{16}$, and "
        r"$\Pi_{11}/\Pi_{15}+\Pi_{12}/\Pi_{16}-\Pi_{13}/\Pi_{14}-\Pi_{15}/\Pi_{16}=-1$.",
    ),
    rec(
        "RN-P3-C20-Entry08ii",
        r"$f(-q,-q^{12})f(-q^2,-q^{11})f(-q^3,-q^{10})f(-q^4,-q^9)f(-q^5,-q^8)f(-q^6,-q^7)=f(-q)f^5(-q^{13})$.",
    ),
    rec(
        "RN-P3-C20-Entry08iii",
        r"If $\beta$ is of the thirteenth degree with respect to $\alpha$ and $m$ is the associated multiplier, then "
        r"$m=\dfrac{(\alpha)^{1/4}}{1-\alpha}+\dfrac{(1-\alpha)^{1/4}}{\alpha}-(\beta(1-\beta))^{1/4}"
        r"-\dfrac{4\{\beta(1-\beta)\}^{1/6}}{\alpha(1-\alpha)}$.",
    ),
    rec(
        "RN-P3-C20-Entry08iv",
        r"If $\beta$ is of the thirteenth degree with respect to $\alpha$ and $m$ is the associated multiplier, then "
        r"$\dfrac{13}{m}=\dfrac{(\beta)^{1/4}}{1-\beta}+\dfrac{(1-\beta)^{1/4}}{\beta}-(\alpha(1-\alpha))^{1/4}"
        r"-\dfrac{\{\alpha(1-\alpha)\}^{1/6}}{4\beta(1-\beta)}$.",
    ),
    rec(
        "RN-P3-C20-Entry09",
        r"We have "
        r"(i) $\psi(q^3)\psi(q^5)-\psi(-q^3)\psi(-q^5)=2q^3\psi(q^2)\psi(q^{30})$; "
        r"(ii) $\varphi(-q^6)\varphi(-q^{10})+2q\psi(q^3)\psi(q^5)=\varphi(q)\varphi(q^{15})$; "
        r"(iii) $\varphi(-q^2)\varphi(-q^{30})+2q^2\psi(q)\psi(q^{15})=\varphi(q^3)\varphi(q^5)$; "
        r"(iv) $\psi(q)\psi(q^{15})+\psi(-q)\psi(-q^{15})=2\psi(q^6)\psi(q^{10})$; "
        r"(v) $\varphi(q)\varphi(q^{15})-\varphi(q^3)\varphi(q^5)=2qf(-q^2)f(-q^{30})\chi(q^3)\chi(q^5)$; "
        r"(vi) $\varphi(q)\varphi(q^{15})+\varphi(q^3)\varphi(q^5)=2f(-q^6)f(-q^{10})\chi(q)\chi(q^{15})$; "
        r"(vii) $\{\psi(q^3)\psi(q^5)-q\psi(q)\psi(q^{15})\}\varphi(-q^3)\varphi(-q^5)"
        r"=\{\psi(q^3)\psi(q^5)+q\psi(q)\psi(q^{15})\}\varphi(-q)\varphi(-q^{15})=f(-q)f(-q^3)f(-q^5)f(-q^{15})$.",
    ),
    rec(
        "RN-P3-C20-Entry10",
        r"We have "
        r"(i) $f(-q^7,-q^8)+qf(-q^2,-q^{13})=\dfrac{f(-q^4,-q^5)}{f(-q^2,-q^3)}$; "
        r"(ii) $\dfrac{f(-q^{14},-q)}{f(-q^5,-q^4)}=\dfrac{f(-q,-q^4)f(-q^5,-q^9)}{f(-q^2,-q^3)}$; "
        r"(iii) $f(-q^{2/3})=f(-q^6,-q^9)-q^{2/3}f(-q^3,-q^{12})+q^{4/3}f(-q,-q^{15})$; "
        r"(iv) $f(-q^{1/3})=f(-q^8,-q^{10})-q^{1/3}f(-q^4,-q^{14})+q^{4/3}f(-q^2,-q^{16})$; "
        r"(v) $\dfrac{\varphi(-q)\varphi(-q^{15})}{qf(-q)f(-q^3)f(-q^5)f(-q^{15})}"
        r"=\sum_{n=1}^{\infty}\dfrac{q^n-q^{7n}-q^{11n}-q^{13n}+q^{17n}+q^{19n}+q^{23n}-q^{29n}}{1-q^{30n}}$; "
        r"(vi) $\varphi(q^3)\varphi(q^5)+\varphi(q)\varphi(q^{15})=2\left(1+\dfrac{q}{1-q}+\dfrac{q^2}{1+q^2}+\dfrac{q^4}{1-q^4}-\dfrac{q^7}{1-q^7}+\cdots\right)$, "
        r"where the cycle of coefficients has length $60$.",
    ),
    rec(
        "RN-P3-C20-Entry11",
        r"Let $\alpha$, $\beta$, $\gamma$, and $\delta$ be of the first, third, fifth, and fifteenth degrees, respectively. "
        r"Let $m$ denote the multiplier connecting $\alpha$ and $\beta$, and let $m'$ be the multiplier relating $\gamma$ and $\delta$. Then "
        r"(i) $(\alpha\delta)^{1/8}+\{(1-\alpha)(1-\delta)\}^{1/8}=\sqrt{m}$; "
        r"(ii) $(\beta\gamma)^{1/8}+\{(1-\beta)(1-\gamma)\}^{1/8}=\dfrac{1}{\sqrt{m'}}$ and "
        r"$(\beta\gamma)^{1/8}-\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/8}=(\alpha\delta)^{1/4}-\{(1-\beta)(1-\gamma)\}^{1/8}-\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/8}-\{(1-\alpha)(1-\delta)\}^{1/4}$; "
        r"(iii) $(\alpha\delta)^{1/8}-\{(1-\alpha)(1-\delta)\}^{1/8}=(\beta\gamma)^{1/8}-\{(1-\beta)(1-\gamma)\}^{1/8}$; "
        r"(iv) $1+(\beta\gamma)^{1/8}+\{(1-\beta)(1-\gamma)\}^{1/8}=4^{1/3}(\beta^2\gamma^2(1-\beta)^2(1-\gamma)^2)^{1/24}$; "
        r"(v) $1-(\alpha\delta)^{1/8}-\{(1-\alpha)(1-\delta)\}^{1/8}=4^{1/3}(\alpha^2\delta^2(1-\alpha)^2(1-\delta)^2)^{1/24}$; "
        r"(vi) $(\alpha\delta)^{1/16}(\{(1+\sqrt{\alpha})(1+\sqrt{\delta})\}^{1/4}+\{(1-\sqrt{\alpha})(1-\sqrt{\delta})\}^{1/4})^2"
        r"+\{(1-\alpha)(1-\delta)\}^{1/16}(\{(1+\sqrt{1-\alpha})(1+\sqrt{1-\delta})\}^{1/4}+\{(1-\sqrt{1-\alpha})(1-\sqrt{1-\delta})\}^{1/4})^2=\sqrt{2}$; "
        r"(vii) $(\beta\gamma)^{1/16}(\{(1+\sqrt{\beta})(1+\sqrt{\gamma})\}^{1/4}-\{(1-\sqrt{\beta})(1-\sqrt{\gamma})\}^{1/4})^2"
        r"+\{(1-\beta)(1-\gamma)\}^{1/16}(\{(1+\sqrt{1-\beta})(1+\sqrt{1-\gamma})\}^{1/4}-\{(1-\sqrt{1-\beta})(1-\sqrt{1-\gamma})\}^{1/4})^2=\sqrt{2}$; "
        r"(viii) $\dfrac{(\alpha\delta)^{1/8}+\{(1-\alpha)(1-\delta)\}^{1/8}-\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/8}}{\beta\gamma+(1-\beta)(1-\gamma)+\beta\gamma(1-\beta)(1-\gamma)}=\dfrac{\sqrt{m'}}{\sqrt{m}}$; "
        r"(ix) $\dfrac{(\beta\gamma)^{1/8}+\{(1-\beta)(1-\gamma)\}^{1/8}-\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/8}}{\alpha\delta+(1-\alpha)(1-\delta)+\alpha\delta(1-\alpha)(1-\delta)}=-\dfrac{\sqrt{m}}{\sqrt{m''}}$; "
        r"(x) $\dfrac{(\beta\delta)^{1/4}+\{(1-\beta)(1-\delta)\}^{1/4}-(\beta\delta(1-\beta)(1-\delta))^{1/4}}{\alpha\gamma+(1-\alpha)(1-\gamma)+\alpha\gamma(1-\alpha)(1-\gamma)}"
        r"-\dfrac{4\{\beta\delta(1-\beta)(1-\delta)\}^{1/6}}{\alpha\gamma(1-\alpha)(1-\gamma)}=mm'$; "
        r"(xi) $\dfrac{(\alpha\gamma)^{1/4}+\{(1-\alpha)(1-\gamma)\}^{1/4}-(\alpha\gamma(1-\alpha)(1-\gamma))^{1/4}}{\beta\delta+(1-\beta)(1-\delta)+\beta\delta(1-\beta)(1-\delta)}"
        r"-\dfrac{4\{\alpha\gamma(1-\alpha)(1-\gamma)\}^{1/6}}{\beta\delta(1-\beta)(1-\delta)}=-\dfrac{9}{mm''}$; "
        r"(xii) $\dfrac{\alpha\beta+(1-\alpha)(1-\beta)+\alpha\beta(1-\alpha)(1-\beta)}{\gamma\delta+(1-\gamma)(1-\delta)+\gamma\delta(1-\gamma)(1-\delta)}"
        r"-\dfrac{2\{\gamma\delta(1-\gamma)(1-\delta)\}^{1/8}\{1+(\gamma\delta)^{1/8}+\{(1-\gamma)(1-\delta)\}^{1/8}\}}{\alpha\beta(1-\alpha)(1-\beta)}"
        r"=\dfrac{2\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/8}\{1+(\alpha\beta)^{1/8}+\{(1-\alpha)(1-\beta)\}^{1/8}\}}{\gamma\delta(1-\gamma)(1-\delta)}$; "
        r"(xiii) $\dfrac{(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}+(\alpha\beta(1-\alpha)(1-\beta))^{1/4}}{\gamma\delta+(1-\gamma)(1-\delta)+\gamma\delta(1-\gamma)(1-\delta)}"
        r"-\dfrac{2\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/8}\{1+(\alpha\beta)^{1/8}+\{(1-\alpha)(1-\beta)\}^{1/8}\}}{\gamma\delta(1-\gamma)(1-\delta)}"
        r"=\dfrac{2\{\gamma\delta(1-\gamma)(1-\delta)\}^{1/8}\{1+(\gamma\delta)^{1/8}+\{(1-\gamma)(1-\delta)\}^{1/8}\}}{\alpha\beta(1-\alpha)(1-\beta)}$; "
        r"(xiv) $(\alpha\beta\gamma\delta)^{1/8}+\{(1-\alpha)(1-\beta)(1-\gamma)(1-\delta)\}^{1/8}+2^{1/3}\{\alpha\beta\gamma\delta(1-\alpha)(1-\beta)(1-\gamma)(1-\delta)\}^{1/24}=1$; "
        r"(xv) If $P=\{256\alpha\beta\gamma\delta(1-\alpha)(1-\beta)(1-\gamma)(1-\delta)\}^{1/48}$ and "
        r"$Q=\dfrac{(\alpha\delta(1-\alpha)(1-\delta))^{1/16}}{\beta\gamma(1-\beta)(1-\gamma)}$, then $P(Q+1/Q)=\dfrac{2}{m'}(P^2+1)$.",
    ),
    rec(
        "RN-P3-C20-Entry12",
        r"(i) With "
        r"$\Pi_{11}=\dfrac{f(-q^5,-q^{12})}{q^{9/17}f(-q^3,-q^{14})}$, "
        r"$\Pi_{12}=\dfrac{f(-q^6,-q^{11})}{q^{11/17}f(-q^4,-q^{13})}$, "
        r"$\Pi_{13}=\dfrac{f(-q^7,-q^{10})}{q^{10/17}f(-q^4,-q^{13})}$, "
        r"$\Pi_{14}=\dfrac{f(-q^8,-q^9)}{q^{2/17}f(-q^5,-q^{12})}$, "
        r"$\Pi_{15}=\dfrac{f(-q^5,-q^{12})}{q^{5/17}f(-q^2,-q^{15})}$, "
        r"$\Pi_{16}=\dfrac{q^{14/17}f(-q^3,-q^{14})}{f(-q^7,-q^{10})}$, "
        r"$\Pi_{17}=\dfrac{q^{28/17}f(-q,-q^{16})}{f(-q^8,-q^9)}$, and "
        r"$\Pi_{18}=\dfrac{q^{15/17}f(-q^2,-q^{15})}{f(-q^6,-q^{11})}$, "
        r"$\dfrac{f(-q^{1/17})}{q^{8/17}f(-q^{17})}=\Pi_{11}-\Pi_{12}-\Pi_{13}+\Pi_{14}+\Pi_{15}-\Pi_{16}$, "
        r"$\Pi_{11}/\Pi_{15}+\Pi_{12}/\Pi_{16}-\Pi_{13}/\Pi_{14}-\Pi_{15}/\Pi_{16}=-1$; "
        r"(ii) $f(-q)f(-q^{17})=f(-q,-q^{16})f(-q^2,-q^{15})f(-q^3,-q^{14})f(-q^4,-q^{13})f(-q^5,-q^{12})f(-q^6,-q^{11})f(-q^7,-q^{10})f(-q^8,-q^9)$; "
        r"(iii) If $\beta$ is of the seventeenth degree with respect to $\alpha$ and $m$ is the multiplier, then "
        r"$m=\dfrac{(\alpha)^{1/4}}{1-\alpha}+\dfrac{(1-\alpha)^{1/4}}{\alpha}+\dfrac{(\alpha(1-\alpha))^{1/4}}{\alpha(1-\alpha)}"
        r"-\dfrac{2\{\alpha(1-\alpha)\}^{1/8}\{1+(\alpha)^{1/8}+(1-\alpha)^{1/8}\}}{\alpha(1-\alpha)}$; "
        r"(iv) $17=\dfrac{(\beta)^{1/4}}{1-\beta}+\dfrac{(1-\beta)^{1/4}}{\beta}+\dfrac{(\beta(1-\beta))^{1/4}}{\beta(1-\beta)}"
        r"-\dfrac{2\{\beta(1-\beta)\}^{1/8}\{(\alpha)^{1/8}+(\beta)^{1/8}+(1-\beta)^{1/8}\}}{2\beta(1-\beta)}$.",
    ),
    rec(
        "RN-P3-C20-Entry13",
        r"If $\beta$, $\gamma$, and $\delta$ are of degrees $3$, $7$, and $21$, respectively, with $m=\chi_1/\chi_3$ and $m'=\chi_7/\chi_{21}$, then "
        r"(i) $\dfrac{(\beta\gamma)^{1/4}+\{(1-\beta)(1-\gamma)\}^{1/4}-(\beta\gamma(1-\beta)(1-\gamma))^{1/4}}{\alpha\delta+(1-\alpha)(1-\delta)+\alpha\delta(1-\alpha)(1-\delta)}"
        r"+\dfrac{4\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/6}}{\alpha\delta(1-\alpha)(1-\delta)}=\dfrac{m}{m''}$; "
        r"(ii) $\dfrac{(\alpha\delta)^{1/4}+\{(1-\alpha)(1-\delta)\}^{1/4}-(\alpha\delta(1-\alpha)(1-\delta))^{1/4}}{\beta\gamma+(1-\beta)(1-\gamma)+\beta\gamma(1-\beta)(1-\gamma)}"
        r"+\dfrac{4\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/6}}{\beta\gamma(1-\beta)(1-\gamma)}=\dfrac{m''}{m'}$; "
        r"(iii) $\dfrac{(\gamma\delta)^{1/8}+\{(1-\gamma)(1-\delta)\}^{1/8}-(\gamma\delta(1-\gamma)(1-\delta))^{1/8}}{\alpha\beta+(1-\alpha)(1-\beta)+\alpha\beta(1-\alpha)(1-\beta)}"
        r"-\dfrac{2\{\gamma\delta(1-\gamma)(1-\delta)\}^{1/12}}{\alpha\beta(1-\alpha)(1-\beta)}=\left(\dfrac{\chi_1\chi_3}{\chi_7\chi_{21}}\right)^{1/2}$; "
        r"(iv) $\dfrac{(\alpha\beta)^{1/8}+\{(1-\alpha)(1-\beta)\}^{1/8}-(\alpha\beta(1-\alpha)(1-\beta))^{1/8}}{\gamma\delta+(1-\gamma)(1-\delta)+\gamma\delta(1-\gamma)(1-\delta)}"
        r"-\dfrac{2\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/12}}{\gamma\delta(1-\gamma)(1-\delta)}=\left(\dfrac{7\chi_7\chi_{21}}{\chi_1\chi_3}\right)^{1/2}$; "
        r"(v) $\dfrac{(\beta\delta)^{1/4}+\{(1-\beta)(1-\delta)\}^{1/4}+(\beta\delta(1-\beta)(1-\delta))^{1/4}}{\alpha\gamma+(1-\alpha)(1-\gamma)+\alpha\gamma(1-\alpha)(1-\gamma)}"
        r"-\dfrac{2\{\beta\delta(1-\beta)(1-\delta)\}^{1/8}\{1+(\beta\delta)^{1/8}+\{(1-\beta)(1-\delta)\}^{1/8}\}}{\alpha\gamma(1-\alpha)(1-\gamma)}=mm'$; "
        r"(vi) $\dfrac{(\alpha\gamma)^{1/4}+\{(1-\alpha)(1-\gamma)\}^{1/4}-(\alpha\gamma(1-\alpha)(1-\gamma))^{1/4}}{\beta\delta+(1-\beta)(1-\delta)+\beta\delta(1-\beta)(1-\delta)}"
        r"-\dfrac{2\{\alpha\gamma(1-\alpha)(1-\gamma)\}^{1/8}\{1+(\alpha\gamma)^{1/8}+\{(1-\alpha)(1-\gamma)\}^{1/8}\}}{\beta\delta(1-\beta)(1-\delta)}=\dfrac{1}{mm''}$.",
    ),
    rec(
        "RN-P3-C20-Entry14",
        r"Let $\beta$, $\gamma$, and $\delta$ be of the third, eleventh, and thirty-third degrees, respectively, with multipliers $m$ and $m'$ for the pairs $(\alpha,\beta)$ and $(\gamma,\delta)$. Then "
        r"(i) $\dfrac{(\beta\delta)^{1/8}+\{(1-\beta)(1-\delta)\}^{1/8}-(\beta\delta(1-\beta)(1-\delta))^{1/8}}{\alpha\gamma+(1-\alpha)(1-\gamma)+\alpha\gamma(1-\alpha)(1-\gamma)}"
        r"-\dfrac{2\{\beta\delta(1-\beta)(1-\delta)\}^{1/12}}{\alpha\gamma(1-\alpha)(1-\gamma)}=\dfrac{1}{\sqrt{m}}$; "
        r"(ii) $\dfrac{(\alpha\gamma)^{1/8}+\{(1-\alpha)(1-\gamma)\}^{1/8}-(\alpha\gamma(1-\alpha)(1-\gamma))^{1/8}}{\beta\delta+(1-\beta)(1-\delta)+\beta\delta(1-\beta)(1-\delta)}"
        r"-\dfrac{2\{\alpha\gamma(1-\alpha)(1-\gamma)\}^{1/12}}{\beta\delta(1-\beta)(1-\delta)}=\dfrac{3}{\sqrt{m'}}$.",
    ),
    rec(
        "RN-P3-C20-Entry15",
        r"If $\beta$ is of the twenty-third degree with respect to $\alpha$, then "
        r"(i) $(\alpha\beta)^{1/8}+\{(1-\alpha)(1-\beta)\}^{1/8}+2^{2/3}\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/24}=1$; "
        r"(ii) $1+(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}+2^{4/3}\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/12}"
        r"=\{2(1+(\alpha\beta)^{1/2}+\{(1-\alpha)(1-\beta)\}^{1/2})\}^{1/2}$; "
        r"(iii) $\dfrac{23}{m}-\dfrac{m}{23}=2\{(\alpha\beta)^{1/8}-\{(1-\alpha)(1-\beta)\}^{1/8}\}"
        r"(-11\cdot 4^{1/3}\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/24}+18\cdot 2^{1/3}\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/12}"
        r"-14\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/8}+25^{2/3}\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/6})$.",
    ),
    rec(
        "RN-P3-C20-Entry16",
        r"If $\beta$ is of degree $19$ with respect to $\alpha$ and $m$ is the multiplier, then "
        r"(i) $\dfrac{((1-\beta)^3)^{1/8}}{1-\alpha}-\dfrac{(\beta^3)^{1/8}}{\beta}+\dfrac{(\beta^3(1-\beta)^3)^{1/8}}{\beta(1-\beta)}"
        r"-\dfrac{2\{\beta^3(1-\beta)^3\}^{1/16}\{(\beta^3)^{1/8}-1-((1-\beta)^3)^{1/8}\}^{1/2}}{\alpha(1-\alpha)}"
        r"=\dfrac{m}{2}\{1+(\alpha\beta)^{1/2}+\{(1-\alpha)(1-\beta)\}^{1/2}\}$; "
        r"(ii) $\dfrac{(\alpha^3)^{1/8}}{1-\beta}-\dfrac{((1-\alpha)^3)^{1/8}}{\alpha}+\dfrac{(\alpha^3(1-\alpha)^3)^{1/8}}{\alpha(1-\alpha)}"
        r"-\dfrac{2\{\alpha^3(1-\alpha)^3\}^{1/16}\{(\alpha^3)^{1/8}-1-((1-\alpha)^3)^{1/8}\}^{1/2}}{\beta(1-\beta)}"
        r"=\dfrac{19}{2m}\{1+(\alpha\beta)^{1/2}+\{(1-\alpha)(1-\beta)\}^{1/2}\}$.",
    ),
    rec(
        "RN-P3-C20-Entry17",
        r"We have "
        r"(i) $\varphi(q)\varphi(q^{35})=\varphi(-q)\varphi(-q^{35})+4qf(-q^{10})f(-q^{14})+4q^9\psi(q^2)\psi(q^{70})$; "
        r"(ii) $\varphi(q^5)\varphi(q^7)=\varphi(-q^5)\varphi(-q^7)+4q^3\psi(q^{10})\psi(q^{14})-4q^3f(-q^2)f(-q^{70})$; "
        r"(iii) $\varphi(q)\varphi(q^{135})=\varphi(-q^{10})\varphi(-q^{54})+2qf(q^9,q^{15})+2q^4\psi(q^5)\psi(q^{27})$; "
        r"(iv) $\varphi(q^{27})\{\varphi(q^5)+2q^{1/5}f(q,q^9)+2q^{4/5}f(q^3,q^7)\}"
        r"=\varphi(-q^2)\{\varphi(-q^{270})-2q^{54/5}f(-q^{162},-q^{378})+2q^{216/5}f(-q^{54},-q^{486})\}"
        r"+2q^{1/5}\{q^{9/5}f(q^9,q^{45})+f^2(-q^{18},q^{27})-q^{18/5}f(q^9,-q^{36})\}\psi(q)+2q^{4/5}\psi(q)\{q^{81/5}\psi(q^{135})+f(q^{54},q^{81})+q^{27/5}f(q^{27},q^{104})\}$.",
    ),
    rec(
        "RN-P3-C20-Entry18",
        r"Let $\beta$, $\gamma$, and $\delta$ have degrees $5$, $7$, and $35$, respectively, with multipliers $m$ and $m'$ for $(\alpha,\beta)$ and $(\gamma,\delta)$. Then "
        r"(i) $(\alpha\delta)^{1/4}+\{(1-\alpha)(1-\delta)\}^{1/4}+2^{4/3}\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/12}"
        r"+(\beta\gamma)^{1/4}+\{(1-\beta)(1-\gamma)\}^{1/4}+2^{4/3}\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/12}"
        r"=1+\{1+2^{4/3}\{\alpha\beta\gamma\delta(1-\alpha)(1-\beta)(1-\gamma)(1-\delta)\}^{1/24}\}^2$; "
        r"(ii) $\{(\alpha\delta)^{1/4}+\{(1-\alpha)(1-\delta)\}^{1/4}+2^{4/3}\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/12}\}"
        r"$\times\{(\beta\gamma)^{1/4}+\{(1-\beta)(1-\gamma)\}^{1/4}+2^{4/3}\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/12}\}$ "
        r"$=1-2^{7/3}\{\alpha\beta\gamma\delta(1-\alpha)(1-\beta)(1-\gamma)(1-\delta)\}^{1/24}"
        r"((\alpha\beta\gamma\delta)^{1/8}+\{(1-\alpha)(1-\beta)(1-\gamma)(1-\delta)\}^{1/8})$; "
        r"(iii) $(\alpha\delta)^{1/4}+\{(1-\alpha)(1-\delta)\}^{1/4}+2^{4/3}\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/12}=\left(\dfrac{m}{m'}\right)^{1/2}$; "
        r"(iv) $(\beta\gamma)^{1/4}+\{(1-\beta)(1-\gamma)\}^{1/4}-2^{4/3}\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/12}=\left(\dfrac{m'}{m}\right)^{1/2}$; "
        r"(v) $\dfrac{\{16\beta\gamma(1-\beta)(1-\gamma)\}^{1/24}+\{16\beta\gamma(1-\beta)(1-\gamma)\}^{1/8}}{m}=\{16\alpha\delta(1-\alpha)(1-\delta)\}^{1/8}-\{16\alpha\delta(1-\alpha)(1-\delta)\}^{1/24}=(m')^{1/2}$; "
        r"(vi) $\dfrac{\{16\alpha\delta(1-\alpha)(1-\delta)\}^{1/8}+\{16\alpha\delta(1-\alpha)(1-\delta)\}^{1/24}}{m'}"
        r"=\dfrac{\{16\beta\gamma(1-\beta)(1-\gamma)\}^{1/8}-\{16\alpha\delta(1-\alpha)(1-\delta)\}^{1/24}}{m}$; "
        r"(vii) $\dfrac{(\alpha\delta)^{1/8}+\{(1-\alpha)(1-\delta)\}^{1/8}-\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/8}}{\beta\gamma+(1-\beta)(1-\gamma)+\beta\gamma(1-\beta)(1-\gamma)}"
        r"+\dfrac{2\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/12}}{\beta\gamma(1-\beta)(1-\gamma)}=\dfrac{(m')^{1/2}}{m'}$ and "
        r"$\dfrac{(\beta\gamma)^{1/8}+\{(1-\beta)(1-\gamma)\}^{1/8}-\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/8}}{\alpha\delta+(1-\alpha)(1-\delta)+\alpha\delta(1-\alpha)(1-\delta)}"
        r"+\dfrac{2\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/12}}{\alpha\delta(1-\alpha)(1-\delta)}=-\left(\dfrac{m}{m'}\right)^{1/2}$.",
    ),
    rec(
        "RN-P3-C20-Entry19",
        r"(i) $\varphi(q)\varphi(q^{63})-\varphi(q^7)\varphi(q^9)=2qf(q^3,q^{21})$; "
        r"(ii) $\psi(q^7)\psi(q^9)-q^6\psi(q)\psi(q^{63})=f(-q^6)f(-q^{42})$; "
        r"(iii) Let $\beta$, $\gamma$, and $\delta$ have degrees $3,13,39$; or $5,11,55$; or $7,9,63$, respectively. "
        r"With multipliers $m$ for $(\alpha,\beta)$ and $m'$ for $(\gamma,\delta)$, "
        r"$\dfrac{1+\{(1-\alpha)(1-\delta)\}^{1/4}+(\alpha\delta)^{1/4}}{1+\{(1-\beta)(1-\gamma)\}^{1/4}+(\beta\gamma)^{1/4}}"
        r"=\dfrac{\{(1-\alpha)(1-\delta)\}^{1/8}-(\alpha\delta)^{1/8}\pm\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/8}}"
        r"{\{(1-\beta)(1-\gamma)\}^{1/8}-(\beta\gamma)^{1/8}-\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/8}}=\sqrt{m}$, "
        r"where the plus sign is taken in the first two cases and the minus sign in the third; "
        r"(iv) If $\beta$, $\gamma$, and $\delta$ have degrees $3,13,39$ or $5,7,35$, respectively, then "
        r"$\dfrac{(\alpha\delta)^{1/8}+\{(1-\alpha)(1-\delta)\}^{1/8}-(\alpha\delta(1-\alpha)(1-\delta))^{1/8}}{\beta\gamma+(1-\beta)(1-\gamma)+\beta\gamma(1-\beta)(1-\gamma)}"
        r"+\dfrac{2\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/12}}{\beta\gamma(1-\beta)(1-\gamma)}=\pm\dfrac{1}{\sqrt{m}}$ and "
        r"$\dfrac{(\beta\gamma)^{1/8}+\{(1-\beta)(1-\gamma)\}^{1/8}-(\beta\gamma(1-\beta)(1-\gamma))^{1/8}}{\alpha\delta+(1-\alpha)(1-\delta)+\alpha\delta(1-\alpha)(1-\delta)}"
        r"+\dfrac{2\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/12}}{\alpha\delta(1-\alpha)(1-\delta)}=\pm\dfrac{1}{\sqrt{m'}}$ "
        r"(plus in the first case, minus in the second).",
    ),
    rec(
        "RN-P3-C20-Entry20",
        r"(i) Let $\beta$, $\gamma$, and $\delta$ have one of the degree sequences $(3,21,63)$, $(5,19,95)$, $(11,13,143)$, $(7,17,119)$, or $(9,15,135)$. "
        r"With multipliers $m$ for $(\alpha,\beta)$ and $m'$ for $(\gamma,\delta)$, "
        r"$\alpha\{1+(\alpha\delta)^{1/2}+\{(1-\alpha)(1-\delta)\}^{1/2}\}^{1/2}"
        r"=(\alpha\delta)^{1/8}+\{(1-\alpha)(1-\delta)\}^{1/8}\pm\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/8}+2^{4/3}\dfrac{\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/2}}{\sqrt{m}}$, "
        r"where the plus sign is taken in the first three cases and the minus sign in the last two; "
        r"(ii) Let $\beta$, $\gamma$, and $\delta$ have degree sequences $(5,19,95)$, $(7,17,119)$, or $(11,13,143)$. Then "
        r"$\alpha\{1+(\beta\gamma)^{1/2}+\{(1-\beta)(1-\gamma)\}^{1/2}\}^{1/2}"
        r"=(\beta\gamma)^{1/8}+\{(1-\beta)(1-\gamma)\}^{1/8}-\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/8}\pm 2^{4/3}\dfrac{\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/12}}{\sqrt{m'}}$ "
        r"(minus in the first two cases, plus in the last).",
    ),
    rec(
        "RN-P3-C20-Entry21",
        r"(i) Let $\alpha$ and $\beta$ have degrees $(1,7)$, $(3,5)$, or $(1,15)$, respectively. Then "
        r"$(\alpha\beta)^{1/8}+\{(1-\alpha)(1-\beta)\}^{1/8}\pm\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/8}"
        r"=\alpha\{1+\sqrt{\alpha\beta}+\sqrt{(1-\alpha)(1-\beta)}\}^{1/2}$, "
        r"where the minus sign is chosen in the first two cases and the plus sign in the last; "
        r"(ii) Let $\beta$, $\gamma$, and $\delta$ have degree sequences $(3,13,39)$, $(5,11,55)$, or $(7,9,63)$, with multipliers $m$ and $m'$. Then "
        r"$\dfrac{1}{\sqrt{m'}}\dfrac{\{(1-\alpha)(1-\delta)\}^{1/8}+(\beta\gamma)^{1/8}+\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/8}}{\sqrt{m}}"
        r"=\alpha\{1+\sqrt{\alpha\delta}+\sqrt{(1-\alpha)(1-\delta)}\}^{1/2}$ and "
        r"$\dfrac{\{(1-\beta)(1-\gamma)\}^{1/8}+(\alpha\delta)^{1/8}\pm\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/8}}{\sqrt{m}}"
        r"=\alpha\{1+\sqrt{\beta\gamma}+\sqrt{(1-\beta)(1-\gamma)}\}^{1/2}$ "
        r"(minus in the first two cases, plus in the last).",
    ),
    rec(
        "RN-P3-C20-Entry22",
        r"Each of the following modular equations is of degree $31$. Define "
        r"$\Theta(\alpha,\beta)=(\alpha\beta)^{1/32}(\{(1+\sqrt{\alpha})(1+\sqrt{\beta})\}^{1/8}\{1+(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/2}\}^{1/2}"
        r"+\{(1-\alpha)(1-\beta)\}^{1/8}\{1+(\alpha\beta)^{1/4}+\{(1+\sqrt{\alpha})(1+\sqrt{\beta})\}^{1/2}\}^{1/2})$. Then "
        r"(i) $\Theta(\alpha,\beta)+\Theta(1-\beta,1-\alpha)=8^{1/4}$; "
        r"(ii) $1+(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}-2\{(\alpha\beta)^{1/8}+\{(1-\alpha)(1-\beta)\}^{1/8}+\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/8}\}$ "
        r"$=2\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/16}\{1+(\alpha\beta)^{1/8}+\{(1-\alpha)(1-\beta)\}^{1/8}\}^{1/2}$; "
        r"(iii) $1+(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}-\{1+\sqrt{\alpha}+\sqrt{(1-\alpha)(1-\beta)}\}^{1/2}$ "
        r"$=(\alpha\beta)^{1/8}+\{(1-\alpha)(1-\beta)\}^{1/8}+\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/8}$.",
    ),
    rec(
        "RN-P3-C20-Entry23",
        r"(i) If $\beta$ is of degree $47$ with respect to $\alpha$, then "
        r"$2\{1+\sqrt{\alpha\beta}+\sqrt{(1-\alpha)(1-\beta)}\}^{1/2}=1+(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}"
        r"+4^{1/3}\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/24}(1+(\alpha\beta)^{1/8}+\{(1-\alpha)(1-\beta)\}^{1/8})$; "
        r"(ii) If $\beta$ is of degree $71$ with respect to $\alpha$, then "
        r"$1+(\alpha\beta)^{1/4}+\{(1-\alpha)(1-\beta)\}^{1/4}-\{1+\sqrt{\alpha\beta}+\sqrt{(1-\alpha)(1-\beta)}\}^{1/2}$ "
        r"$=(\alpha\beta)^{1/8}+\{(1-\alpha)(1-\beta)\}^{1/8}-\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/8}"
        r"+4^{1/3}\{\alpha\beta(1-\alpha)(1-\beta)\}^{1/24}(1-(\alpha\beta)^{1/8}-\{(1-\alpha)(1-\beta)\}^{1/8})$.",
    ),
    rec(
        "RN-P3-C20-Entry24",
        r"Let $\beta$, $\gamma$, and $\delta$ have one of the degree sequences $(3,29,87)$, $(5,27,135)$, $(11,21,231)$, $(13,19,247)$, $(7,25,175)$, $(9,23,207)$, or $(15,17,255)$. "
        r"Let $m$ and $m'$ denote the multipliers for $(\alpha,\beta)$ and $(\gamma,\delta)$. Then "
        r"(i) $\{1+\sqrt{\beta\gamma}+\sqrt{(1-\beta)(1-\gamma)}\}^{1/2}+(\beta\gamma)^{1/8}+\{(1-\beta)(1-\gamma)\}^{1/8}+\{\beta\gamma(1-\beta)(1-\gamma)\}^{1/8}"
        r"=\{1+(\alpha\delta)^{1/4}+\{(1-\alpha)(1-\delta)\}^{1/4}\}\sqrt{m}$; "
        r"(ii) $\{1+\sqrt{\alpha\delta}+\sqrt{(1-\alpha)(1-\delta)}\}^{1/2}+(\alpha\delta)^{1/8}+\{(1-\alpha)(1-\delta)\}^{1/8}\pm\{\alpha\delta(1-\alpha)(1-\delta)\}^{1/8}"
        r"=\{1+(\beta\gamma)^{1/4}+\{(1-\beta)(1-\gamma)\}^{1/4}\}\sqrt{m'}$, "
        r"where the minus sign is chosen in the first four cases and the plus sign in the last three.",
    ),
]
