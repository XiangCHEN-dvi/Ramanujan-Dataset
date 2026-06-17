"""Part 5, Chapter 34 entries — curated LaTeX."""

from __future__ import annotations

TOPICS = ["class-invariants"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS}


CHAPTER_34 = [

    rec(
        "RN-P5-C34-Entry02-01",
        r"Entry 2.1 (p. 294, NB 2). For $n > 0$, $g_{4n} = 2^{1/4} g_n G_n$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-02",
        r"Entry 2.2 (p. 294, NB 2). For $n > 0$, $(g_n G_n)^8 (G_n^8 - g_n^8) = \frac{1}{4}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G1",
        r"Section 2 (p. 189). $G_{1} = 1$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G3",
        r"Section 2 (p. 189). $G_{3} = 2^{1/12}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G5",
        r"Section 2 (p. 189). $G_{5} = \left( \frac{1 + \sqrt{5}}{2} \right)^{1/4}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G7",
        r"Section 2 (p. 189). $G_{7} = 2^{1/4}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G9",
        r"Section 2 (p. 189). $G_{9} = \left( \frac{1 + \sqrt{3}}{\sqrt{2}} \right)^{1/3}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G11",
        r"Section 2 (p. 189). $G_{11} = 2^{-1/4}x, \text{ where } x^3 - 2x^2 + 2x - 2 = 0$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G13",
        r"Section 2 (p. 190). $G_{13} = \left( \frac{3 + \sqrt{13}}{2} \right)^{1/4}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G15",
        r"Section 2 (p. 190). $G_{15} = 2^{1/4} \left( \frac{1 + \sqrt{5}}{2} \right)^{1/3}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G17",
        r"Section 2 (p. 190). $G_{17} = \sqrt{\frac{5 + \sqrt{17}}{8}} + \sqrt{\frac{\sqrt{17} - 3}{8}}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G19",
        r"Section 2 (p. 190). $G_{19} = 2^{-1/4}x, \text{ where } x^3 - 2x - 2 = 0$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G21",
        r"Section 2 (p. 190). $G_{21} = \left( \frac{\sqrt{3} + \sqrt{7}}{2} \right)^{1/4} \left( \frac{3 + \sqrt{7}}{\sqrt{2}} \right)^{1/6}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G23",
        r"Section 2 (p. 190). $G_{23} = 2^{1/4}x, \text{ where } x^3 - x - 1 = 0$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G25",
        r"Section 2 (p. 190). $G_{25} = \frac{1 + \sqrt{5}}{2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G27",
        r"Section 2 (p. 190). $G_{27} = 2^{1/12} (\sqrt[3]{2} - 1)^{-1/3}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G29",
        r"Section 2 (p. 190). $G_{29} = x, \text{ where } G_{29}^4 = x \text{ and } x^6 - 9x^5 + 5x^4 + 2x^3 - 5x^2 - 9x - 1 = 0$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G31",
        r"Section 2 (p. 191). $G_{31} = 2^{1/4}x, \text{ where } x^3 - x^2 - 1 = 0$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G33",
        r"Section 2 (p. 191). $G_{33} = \left( \frac{3 + \sqrt{11}}{\sqrt{2}} \right)^{1/6} \left( \frac{1 + \sqrt{3}}{\sqrt{2}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G37",
        r"Section 2 (p. 191). $G_{37} = (6 + \sqrt{37})^{1/4}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G39",
        r"Section 2 (p. 191). $G_{39} = 2^{1/4} \left( \frac{\sqrt{13} + 3}{2} \right)^{1/6} \left( \sqrt{\frac{5 + \sqrt{13}}{8}} + \sqrt{\frac{\sqrt{13} - 3}{8}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G41",
        r"Section 2 (p. 191). $G_{41} = x, \text{ where } G_{41}^2 = x \text{ and } \left(x + \frac{1}{x}\right)^2 - \frac{5 + \sqrt{41}}{2} \left(x + \frac{1}{x}\right) + \frac{7 + \sqrt{41}}{2} = 0$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G43",
        r"Section 2 (p. 191). $G_{43} = 2^{-1/4}x, \text{ where } x^3 - 2x^2 - 2 = 0$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G45",
        r"Section 2 (p. 191). $G_{45} = (2 + \sqrt{5})^{1/4} \left( \frac{\sqrt{3} + \sqrt{5}}{\sqrt{2}} \right)^{1/3}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G47",
        r"Section 2 (p. 191). $G_{47} = 2^{1/4}x, \text{ where } x^5 = (1 + x)(1 + x + x^2)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G49",
        r"Section 2 (p. 191). $G_{49} = \frac{7^{1/4} + \sqrt{4 + \sqrt{7}}}{2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G55",
        r"Section 2 (p. 192). $G_{55} = 2^{1/4} (\sqrt{5} + 2)^{1/6} \left( \sqrt{\frac{7 + \sqrt{5}}{8}} + \sqrt{\frac{\sqrt{5} - 1}{8}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G57",
        r"Section 2 (p. 192). $G_{57} = \left( \frac{3\sqrt{19} + 13}{\sqrt{2}} \right)^{1/6} (2 + \sqrt{3})^{1/4}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G63",
        r"Section 2 (p. 192). $G_{63} = 2^{1/4} \left( \frac{5 + \sqrt{21}}{2} \right)^{1/6} \left( \sqrt{\frac{5 + \sqrt{21}}{8}} + \sqrt{\frac{\sqrt{21} - 3}{8}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G65",
        r"Section 2 (p. 192). $G_{65} = \left( \frac{\sqrt{13} + 3}{2} \right)^{1/4} \left( \frac{\sqrt{5} + 1}{2} \right)^{1/4} \left( \sqrt{\frac{9 + \sqrt{65}}{8}} + \sqrt{\frac{1 + \sqrt{65}}{8}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G67",
        r"Section 2 (p. 192). $G_{67} = 2^{-1/4}x, \text{ where } x^3 - 2x^2 - 2x - 2 = 0$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G69",
        r"Section 2 (p. 192). $G_{69} = \left( \frac{5 + \sqrt{23}}{\sqrt{2}} \right)^{1/12} \left( \frac{3\sqrt{3} + \sqrt{23}}{2} \right)^{1/8} \left( \sqrt{\frac{6 + 3\sqrt{3}}{4}} + \sqrt{\frac{2 + 3\sqrt{3}}{4}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G73",
        r"Section 2 (p. 192). $G_{73} = \sqrt{\frac{9 + \sqrt{73}}{8}} + \sqrt{\frac{1 + \sqrt{73}}{8}}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G75",
        r"Section 2 (p. 192). $G_{75} = \frac{3 \cdot 2^{5/12}}{\frac{\sqrt{5} + 1}{2} (10)^{1/3} + \frac{\sqrt{5} - 1}{2} \cdot 4^{1/3} \cdot 5^{1/6} - \sqrt{5} - 1}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G77",
        r"Section 2 (p. 193). $G_{77} = (8 + 3\sqrt{7})^{1/8} \left( \frac{\sqrt{11} + \sqrt{7}}{2} \right)^{1/8} \left( \sqrt{\frac{6 + \sqrt{11}}{4}} + \sqrt{\frac{2 + \sqrt{11}}{4}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G79",
        r"Section 2 (p. 193). $G_{79} = x, \text{ where } t = 2^{1/4}/G_{79} \text{ and } t^5 - t^4 + t^3 - 2t^2 + 3t - 1 = 0$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G81",
        r"Section 2 (p. 193). $G_{81} = \left( \frac{\sqrt[3]{2(\sqrt{3} + 1)} + 1}{\sqrt[3]{2(\sqrt{3} - 1)} - 1} \right)^{1/3}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G85",
        r"Section 2 (p. 193). $G_{85} = \left( \frac{1 + \sqrt{5}}{2} \right) \left( \frac{\sqrt{85} + 9}{2} \right)^{1/4}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G93",
        r"Section 2 (p. 193). $G_{93} = \left( \frac{39 + 7\sqrt{31}}{\sqrt{2}} \right)^{1/6} \left( \frac{\sqrt{31} + 3\sqrt{3}}{2} \right)^{1/4}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G97",
        r"Section 2 (p. 193). $G_{97} = \sqrt{\frac{13 + \sqrt{97}}{8}} + \sqrt{\frac{5 + \sqrt{97}}{8}}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G105",
        r"Section 2 (p. 193). $G_{105} = \left( \frac{5 + \sqrt{21}}{2} \right)^{1/4} (2 + \sqrt{3})^{1/4} (\sqrt{5} + 2)^{1/6} (6 + \sqrt{35})^{1/12}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G117",
        r"Section 2 (p. 193). $G_{117} = \left( \frac{3 + \sqrt{13}}{2} \right)^{1/4} (2\sqrt{3} + \sqrt{13})^{1/6} \left( \frac{3^{1/4} + \sqrt{4 + \sqrt{3}}}{2} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G121",
        r"Section 2 (p. 194). $G_{121} = \frac{1}{3\sqrt{2}} \left[ (11 + 3\sqrt{11})^{1/3} \left( (3\sqrt{11} + 3\sqrt{3} + 4)^{1/3} + (3\sqrt{11} - 3\sqrt{3} + 4)^{1/3} \right) + 2 \right]$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G133",
        r"Section 2 (p. 194). $G_{133} = (8 + 3\sqrt{7})^{1/4} \left( \frac{5\sqrt{7} + 3\sqrt{19}}{2} \right)^{1/4}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G141",
        r"Section 2 (p. 194). $G_{141} = (4\sqrt{3} + \sqrt{47})^{1/8} \left( \frac{7 + \sqrt{47}}{\sqrt{2}} \right)^{1/12} \left( \sqrt{\frac{18 + 9\sqrt{3}}{4}} + \sqrt{\frac{14 + 9\sqrt{3}}{4}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G145",
        r"Section 2 (p. 194). $G_{145} = (\sqrt{5} + 2)^{1/4} \left( \frac{5 + \sqrt{29}}{2} \right)^{1/4} \left( \sqrt{\frac{17 + \sqrt{145}}{8}} + \sqrt{\frac{9 + \sqrt{145}}{8}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G147",
        r"Section 2 (p. 194). $G_{147} = 2^{1/12} \left( \frac{1}{2} + \frac{1}{\sqrt{3}} \left\{ \sqrt{\frac{7}{4}} - (28)^{1/6} \right\} \right)^{-1}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G153",
        r"Section 2 (p. 194). $G_{153} = \left( \sqrt{\frac{5 + \sqrt{17}}{8}} + \sqrt{\frac{\sqrt{17} - 3}{8}} \right)^2 \left( \sqrt{\frac{37 + 9\sqrt{17}}{4}} + \sqrt{\frac{33 + 9\sqrt{17}}{4}} \right)^{1/3}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G163",
        r"Section 2 (p. 194). $G_{163} = 2^{-1/4}x, \text{ where } x^3 - 6x^2 + 4x - 2 = 0$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G165",
        r"Section 2 (p. 194). $G_{165} = (4 + \sqrt{15})^{1/4} (3\sqrt{5} + 2\sqrt{11})^{1/6} \left( \frac{\sqrt{15} + \sqrt{11}}{2} \right)^{1/4} (\sqrt{5} + 2)^{1/6}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G169",
        r"Section 2 (p. 195). $G_{169} = \frac{1}{3} \left[ (\sqrt{13} + 2) + \left( \frac{13 + 3\sqrt{13}}{2} \right)^{1/3} \left\{ \left( \frac{11 + \sqrt{13}}{2} + 3\sqrt{3} \right)^{1/3} + \left( \frac{11 + \sqrt{13}}{2} - 3\sqrt{3} \right)^{1/3} \right\} \right]$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G175",
        r"Section 2 (p. 195). $G_{175} = \frac{3 \cdot 2^{1/4}}{\frac{\sqrt{5} - 1}{2} + \left( \frac{5 - \sqrt{5}}{4} \right)^{1/3} \left( \sqrt[3]{8 - 3\sqrt{5} + 3\sqrt{21}} + \sqrt[3]{8 - 3\sqrt{5} - 3\sqrt{21}} \right)}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G177",
        r"Section 2 (p. 195). $G_{177} = \left( \frac{3\sqrt{59} + 23}{\sqrt{2}} \right)^{1/6} \left( \frac{1 + \sqrt{3}}{\sqrt{2}} \right)^{3/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G205",
        r"Section 2 (p. 195). $G_{205} = \left( \frac{1 + \sqrt{5}}{2} \right) \left( \frac{3\sqrt{5} + \sqrt{41}}{2} \right)^{1/4} \left( \sqrt{\frac{7 + \sqrt{41}}{8}} + \sqrt{\frac{\sqrt{41} - 1}{8}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G213",
        r"Section 2 (p. 195). $G_{213} = \left( \frac{5\sqrt{3} + \sqrt{71}}{2} \right)^{1/8} \left( \frac{59 + 7\sqrt{71}}{\sqrt{2}} \right)^{1/12} \left( \sqrt{\frac{21 + 12\sqrt{3}}{2}} + \sqrt{\frac{19 + 12\sqrt{3}}{2}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G217",
        r"Section 2 (p. 195). $G_{217} = \left( \sqrt{\frac{9 + 4\sqrt{7}}{2}} + \sqrt{\frac{11 + 4\sqrt{7}}{2}} \right)^{1/2} \left( \sqrt{\frac{12 + 5\sqrt{7}}{4}} + \sqrt{\frac{16 + 5\sqrt{7}}{4}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G225",
        r"Section 2 (p. 195). $G_{225} = \left( \frac{1 + \sqrt{5}}{2} \right) (2 + \sqrt{3})^{1/3} \left( \frac{\sqrt{4 + \sqrt{15}} + (15)^{1/4}}{2} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G253",
        r"Section 2 (p. 196). $G_{253} = \left( \frac{5 + \sqrt{23}}{\sqrt{2}} \right)^{1/2} \left( \frac{13\sqrt{11} + 9\sqrt{23}}{2} \right)^{1/4}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G265",
        r"Section 2 (p. 196). $G_{265} = (2 + \sqrt{5})^{1/4} \left( \frac{7 + \sqrt{53}}{2} \right)^{1/4} \left( \sqrt{\frac{89 + 5\sqrt{265}}{8}} + \sqrt{\frac{81 + 5\sqrt{265}}{8}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G273",
        r"Section 2 (p. 196). $G_{273} = \left( \frac{15\sqrt{7} + 11\sqrt{13}}{\sqrt{2}} \right)^{1/6} \left( \frac{\sqrt{13} + 3}{2} \right)^{1/2} \left( \frac{\sqrt{7} + \sqrt{3}}{2} \right)^{1/2} (2 + \sqrt{3})^{1/4}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G289",
        r"Section 2 (p. 196). $G_{289} = \left( \sqrt{\frac{17 + \sqrt{17} + (17)^{1/4}(5 + \sqrt{17})}{16}} + \sqrt{\frac{1 + \sqrt{17} + (17)^{1/4}(5 + \sqrt{17})}{16}} \right)^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G301",
        r"Section 2 (p. 196). $G_{301} = (8 + 3\sqrt{7})^{1/8} \left( \frac{23\sqrt{43} + 57\sqrt{7}}{2} \right)^{1/8} \left( \sqrt{\frac{46 + 7\sqrt{43}}{4}} + \sqrt{\frac{42 + 7\sqrt{43}}{4}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G325",
        r"Section 2 (p. 196). $G_{325} = t, \text{ where } G_{325} = \left( \frac{3 + \sqrt{13}}{2} \right)^{1/4} t \text{ and } t^3 + t^2 \left( \frac{1 - \sqrt{13}}{2} \right)^2 + t \left( \frac{1 + \sqrt{13}}{2} \right)^2 + 1 = \sqrt{5} \left\{ t^3 - t^2 \left( \frac{1 + \sqrt{13}}{2} \right) + t \left( \frac{1 - \sqrt{13}}{2} \right) - 1 \right\}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G333",
        r"Section 2 (p. 196). $G_{333} = (6 + \sqrt{37})^{1/4} (7\sqrt{3} + 2\sqrt{37})^{1/6} \left( \frac{\sqrt{7 + 2\sqrt{3}} + \sqrt{3 + 2\sqrt{3}}}{2} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G345",
        r"Section 2 (p. 197). $G_{345} = \frac{1 + \sqrt{5}}{2} \left( \frac{1 + \sqrt{3}}{\sqrt{2}} \right)^{1/2} \left( \frac{3\sqrt{3} + \sqrt{23}}{2} \right)^{1/2} \left( \frac{15\sqrt{5} + 7\sqrt{23}}{\sqrt{2}} \right)^{1/6}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G357",
        r"Section 2 (p. 197). $G_{357} = \left( \frac{\sqrt{3} + \sqrt{7}}{2} \right) (8 + 3\sqrt{7})^{1/4} \left( \frac{\sqrt{17} + \sqrt{21}}{2} \right)^{1/4} \left( \frac{11 + \sqrt{119}}{\sqrt{2}} \right)^{1/6}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G363",
        r"Section 2 (p. 197). $G_{363} = 2^{5/12} t, \text{ where } 2t^3 - t^2 \left\{ (4 + \sqrt{33}) + \sqrt{11 + 2\sqrt{33}} \right\} - t \left\{ 1 + \sqrt{11 + 2\sqrt{33}} \right\} - 1 = 0$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G385",
        r"Section 2 (p. 197). $G_{385} = \sqrt{\frac{1}{8}(3 + \sqrt{11})(\sqrt{5} + \sqrt{7})(\sqrt{7} + \sqrt{11})(3 + \sqrt{5})}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G441",
        r"Section 2 (p. 197). $G_{441} = \sqrt{\frac{\sqrt{3} + \sqrt{7}}{2}} (2 + \sqrt{3})^{1/6} \sqrt{\frac{2 + \sqrt{7} + \sqrt{7 + 4\sqrt{7}}}{2}} \sqrt[8]{\frac{\sqrt{3} + \sqrt{7} + (6\sqrt{7})^{1/4}}{\sqrt{3} + \sqrt{7} - (6\sqrt{7})^{1/4}}}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G445",
        r"Section 2 (p. 197). $G_{445} = \sqrt{2 + \sqrt{5}} \left( \frac{21 + \sqrt{445}}{2} \right)^{1/4} \left( \sqrt{\frac{13 + \sqrt{89}}{8}} + \sqrt{\frac{5 + \sqrt{89}}{8}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G465",
        r"Section 2 (p. 197). $G_{465} = (2 + \sqrt{3})^{1/4} \left( \frac{1 + \sqrt{5}}{2} \right) \left( \frac{3\sqrt{3} + 31}{2} \right)^{1/4} (5\sqrt{5} + 2\sqrt{31})^{1/12} \left( \sqrt{\frac{2 + \sqrt{31}}{4}} + \sqrt{\frac{6 + \sqrt{31}}{4}} \right)^{1/2} \left( \sqrt{\frac{11 + 2\sqrt{31}}{2}} + \sqrt{\frac{13 + 2\sqrt{31}}{2}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G505",
        r"Section 2 (p. 198). $G_{505} = \sqrt{2 + \sqrt{5}} \left( \frac{1 + \sqrt{5}}{2} \right)^{1/4} (10 + \sqrt{101})^{1/4} \left( \sqrt{\frac{113 + 5\sqrt{105}}{8}} + \sqrt{\frac{105 + 5\sqrt{105}}{8}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G553",
        r"Section 2 (p. 198). $G_{553} = \left( \sqrt{\frac{96 + 11\sqrt{79}}{4}} + \sqrt{\frac{100 + 11\sqrt{79}}{4}} \right)^{1/2} \left( \sqrt{\frac{141 + 16\sqrt{79}}{2}} + \sqrt{\frac{143 + 16\sqrt{79}}{2}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G765",
        r"Section 2 (p. 198). $G_{765} = \sqrt{\frac{3 + \sqrt{5}}{2}} (16 + \sqrt{255})^{1/12} (4 + \sqrt{15})^{1/4} \left( \frac{9 + \sqrt{85}}{2} \right)^{1/4} \left( \sqrt{\frac{6 + \sqrt{51}}{4}} + \sqrt{\frac{10 + \sqrt{51}}{4}} \right)^{1/2} \left( \sqrt{\frac{18 + 3\sqrt{51}}{4}} + \sqrt{\frac{22 + 3\sqrt{51}}{4}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G777",
        r"Section 2 (p. 198). $G_{777} = (2 + \sqrt{3})^{1/4} (6 + \sqrt{37})^{1/4} \left( \frac{\sqrt{3} + \sqrt{7}}{2} \right)^{1/4} (246\sqrt{7} + 107\sqrt{37})^{1/12} \left( \sqrt{\frac{6 + 3\sqrt{7}}{4}} + \sqrt{\frac{10 + 3\sqrt{7}}{4}} \right)^{1/2} \left( \sqrt{\frac{15 + 6\sqrt{7}}{2}} + \sqrt{\frac{17 + 6\sqrt{7}}{2}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G897",
        r"Section 2 (p. 198). $G_{897} = \sqrt{2 + \sqrt{3}} \sqrt{\frac{\sqrt{13} + 3}{2}} (4\sqrt{13} + 3\sqrt{23})^{1/12} \left( \frac{3\sqrt{3} + \sqrt{23}}{2} \right)^{1/4} \left( \sqrt{\frac{60 + 9\sqrt{39}}{4}} + \sqrt{\frac{56 + 9\sqrt{39}}{4}} \right)^{1/2} \left( \sqrt{\frac{8 + \sqrt{39}}{4}} + \sqrt{\frac{4 + \sqrt{39}}{4}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G1225",
        r"Section 2 (p. 199). $G_{1225} = \frac{1 + \sqrt{5}}{2} (6 + \sqrt{35})^{1/4} \left( \frac{7^{1/4} + \sqrt{4 + \sqrt{7}}}{2} \right)^{3/2} \left( \sqrt{\frac{43 + 15\sqrt{7} + (8 + 3\sqrt{7})\sqrt{10\sqrt{7}}}{8}} + \sqrt{\frac{35 + 15\sqrt{7} + (8 + 3\sqrt{7})\sqrt{10\sqrt{7}}}{8}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G1353",
        r"Section 2 (p. 199). $G_{1353} = \left( \frac{3 + \sqrt{11}}{\sqrt{2}} \right)^{1/4} \left( \frac{5 + 3\sqrt{3}}{\sqrt{2}} \right)^{1/4} \left( \frac{11 + \sqrt{123}}{\sqrt{2}} \right)^{1/4} \left( \frac{6817 + 321\sqrt{451}}{\sqrt{2}} \right)^{1/12} \left( \sqrt{\frac{17 + 3\sqrt{33}}{8}} + \sqrt{\frac{25 + 3\sqrt{33}}{8}} \right)^{1/2} \left( \sqrt{\frac{561 + 99\sqrt{33}}{8}} + \sqrt{\frac{569 + 99\sqrt{33}}{8}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G1645",
        r"Section 2 (p. 199). $G_{1645} = \sqrt{2 + \sqrt{5}} \left( \frac{3 + \sqrt{7}}{\sqrt{2}} \right)^{1/4} \left( \frac{7 + \sqrt{47}}{\sqrt{2}} \right)^{1/4} \left( \frac{73\sqrt{5} + 9\sqrt{329}}{2} \right)^{1/8} \left( \sqrt{\frac{119 + 7\sqrt{329}}{8}} + \sqrt{\frac{127 + 7\sqrt{329}}{8}} \right)^{1/2} \left( \sqrt{\frac{743 + 41\sqrt{329}}{8}} + \sqrt{\frac{751 + 41\sqrt{329}}{8}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-G1677",
        r"Section 2 (p. 199). $G_{1677} = (4414\sqrt{13} + 2427\sqrt{43})^{1/12} \left( \frac{\sqrt{13} + 3}{2} \right)^{3/4} \left( \frac{\sqrt{43} + \sqrt{39}}{2} \right)^{1/4} (\sqrt{13} + 2\sqrt{3})^{1/4} \left( \sqrt{\frac{355 + 54\sqrt{43}}{4}} + \sqrt{\frac{351 + 54\sqrt{43}}{4}} \right)^{1/2} \left( \sqrt{\frac{17 + 2\sqrt{43}}{4}} + \sqrt{\frac{13 + 2\sqrt{43}}{4}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g2",
        r"Section 2 (p. 200). $g_{2} = 1$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g6",
        r"Section 2 (p. 200). $g_{6} = (1 + \sqrt{2})^{1/6}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g10",
        r"Section 2 (p. 200). $g_{10} = \sqrt{\frac{1 + \sqrt{5}}{2}}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g14",
        r"Section 2 (p. 200). $g_{14} = \sqrt{\frac{1 + \sqrt{2} + \sqrt{2\sqrt{2}-1}}{2}}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g18",
        r"Section 2 (p. 200). $g_{18} = (\sqrt{2} + \sqrt{3})^{1/3}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g22",
        r"Section 2 (p. 200). $g_{22} = \sqrt{1 + \sqrt{2}}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g26",
        r"Section 2 (p. 200). $g_{26} = \frac{1}{3} \left( \sqrt{2} + \sqrt{13} + \sqrt[3]{(2 + \sqrt{13})\sqrt{2} + \sqrt{13} + 3\sqrt{3(3 + \sqrt{13})}} + \sqrt[3]{(2 + \sqrt{13})\sqrt{2} + \sqrt{13} - 3\sqrt{3(3 + \sqrt{13})}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g30",
        r"Section 2 (p. 200). $g_{30} = (2 + \sqrt{5})^{1/6}(3 + \sqrt{10})^{1/6}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g34",
        r"Section 2 (p. 200). $g_{34} = \sqrt{\frac{3 + \sqrt{17}}{4}} + \frac{\sqrt{\sqrt{17}-1}}{2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g38",
        r"Section 2 (p. 201). $g_{38} = g, \text{ where } g = g_{38} \text{ and } g^3 + g\sqrt{2} = \sqrt{1 + \sqrt{2}}(1 + g^2\sqrt{2})$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g42",
        r"Section 2 (p. 201). $g_{42} = (2\sqrt{2} + \sqrt{7})^{1/6} \left( \frac{\sqrt{3} + \sqrt{7}}{2} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g46",
        r"Section 2 (p. 201). $g_{46} = \sqrt{\frac{3 + \sqrt{2} + \sqrt{7 + 6\sqrt{2}}}{2}}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g50",
        r"Section 2 (p. 201). $g_{50} = \frac{1}{3} \left( 1 + \left( \frac{5 + \sqrt{5}}{4} \right)^{1/3} \left( \sqrt[3]{1 + 7\sqrt{5} + 6\sqrt{30}} + \sqrt[3]{1 + 7\sqrt{5} - 6\sqrt{30}} \right) \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g58",
        r"Section 2 (p. 201). $g_{58} = \sqrt{\frac{5 + \sqrt{29}}{2}}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g62",
        r"Section 2 (p. 201). $g_{62} = \left( \sqrt{\frac{4 + \sqrt{1 + \sqrt{2} + \sqrt{9 + 5\sqrt{2}}}}{8}} + \sqrt{\frac{1 + \sqrt{2} + \sqrt{9 + 5\sqrt{2}} - 4}{8}} \right)^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g66",
        r"Section 2 (p. 201). $g_{66} = (\sqrt{2} + \sqrt{3})^{1/4} (7\sqrt{2} + 3\sqrt{11})^{1/12} \left( \sqrt{\frac{7 + \sqrt{33}}{8}} + \sqrt{\frac{\sqrt{33} - 1}{8}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g70",
        r"Section 2 (p. 201). $g_{70} = \sqrt{\frac{(3 + \sqrt{5})(1 + \sqrt{2})}{2}}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g78",
        r"Section 2 (p. 202). $g_{78} = \left( \frac{3 + \sqrt{13}}{2} \right)^{1/2} (5 + \sqrt{26})^{1/6}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g82",
        r"Section 2 (p. 202). $g_{82} = \sqrt{\frac{13 + \sqrt{41}}{8}} + \sqrt{\frac{5 + \sqrt{41}}{8}}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g90",
        r"Section 2 (p. 202). $g_{90} = \{(2 + \sqrt{5})(\sqrt{5} + \sqrt{6})\}^{1/6} \left( \sqrt{\frac{3 + \sqrt{6}}{4}} + \sqrt{\frac{\sqrt{6} - 1}{4}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g94",
        r"Section 2 (p. 202). $g_{94} = \left( \sqrt{\frac{4 + \sqrt{7 + \sqrt{2} + \sqrt{7 + 5\sqrt{2}}}}{8}} + \sqrt{\frac{\sqrt{7 + \sqrt{2} + \sqrt{7 + 5\sqrt{2}}} - 4}{8}} \right)^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g98",
        r"Section 2 (p. 202). $g_{98} = \left( \sqrt{\frac{4 + \sqrt{2} + \sqrt{14 + 4\sqrt{14}}}{8}} + \sqrt{\frac{\sqrt{2} + \sqrt{14 + 4\sqrt{14}} - 4}{8}} \right)^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g102",
        r"Section 2 (p. 202). $g_{102} = (1 + \sqrt{2})^{1/2} (3\sqrt{2} + \sqrt{17})^{1/3}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g114",
        r"Section 2 (p. 202). $g_{114} = (\sqrt{2} + \sqrt{3})^{1/4} (3\sqrt{2} + \sqrt{19})^{1/12} \left( \sqrt{\frac{23 + 3\sqrt{57}}{8}} + \sqrt{\frac{15 + 3\sqrt{57}}{8}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g126",
        r"Section 2 (p. 202). $g_{126} = \sqrt{\frac{\sqrt{3} + \sqrt{7}}{2}} (\sqrt{6} + \sqrt{7})^{1/6} \left( \sqrt{\frac{3 + \sqrt{2}}{4}} + \sqrt{\frac{\sqrt{2} - 1}{4}} \right)^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g130",
        r"Section 2 (p. 203). $g_{130} = \left( \frac{1 + \sqrt{5}}{2} \right)^{3/2} \left( \frac{3 + \sqrt{13}}{2} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g138",
        r"Section 2 (p. 203). $g_{138} = \left( \frac{3\sqrt{3} + \sqrt{23}}{2} \right)^{1/4} (78\sqrt{2} + 23\sqrt{23})^{1/12} \left( \sqrt{\frac{5 + 2\sqrt{6}}{4}} + \sqrt{\frac{1 + 2\sqrt{6}}{4}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g142",
        r"Section 2 (p. 203). $g_{142} = \sqrt{\frac{9 + 5\sqrt{2} + \sqrt{127 + 90\sqrt{2}}}{2}}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g154",
        r"Section 2 (p. 203). $g_{154} = (2\sqrt{2} + \sqrt{7})^{1/4} \left( \frac{\sqrt{7} + \sqrt{11}}{2} \right)^{1/4} \left( \sqrt{\frac{13 + 2\sqrt{22}}{4}} + \sqrt{\frac{9 + 2\sqrt{22}}{4}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g158",
        r"Section 2 (p. 203). $g_{158} = \left( \sqrt{\frac{4 + \sqrt{9 + \sqrt{2} + \sqrt{17 + 13\sqrt{2}}}}{8}} + \sqrt{\frac{\sqrt{9 + \sqrt{2} + \sqrt{17 + 13\sqrt{2}}} - 4}{8}} \right)^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g190",
        r"Section 2 (p. 203). $g_{190} = \left( \frac{1 + \sqrt{5}}{2} \right)^{3/2} (3 + \sqrt{10})^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g198",
        r"Section 2 (p. 203). $g_{198} = \sqrt{1 + \sqrt{2}} (4\sqrt{2} + \sqrt{33})^{1/6} \left( \sqrt{\frac{9 + \sqrt{33}}{8}} + \sqrt{\frac{1 + \sqrt{33}}{8}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g210",
        r"Section 2 (p. 203). $g_{210} = \sqrt{\sqrt{3} + \sqrt{2}} (3\sqrt{14} + 5\sqrt{5})^{1/6} \sqrt{\frac{\sqrt{7} + \sqrt{3}}{2}} \sqrt{\frac{\sqrt{5} + 1}{2}}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g238",
        r"Section 2 (p. 204). $g_{238} = \left( \sqrt{\frac{1 + 2\sqrt{2}}{4}} + \sqrt{\frac{5 + 2\sqrt{2}}{4}} \right) \left( \sqrt{\frac{1 + 3\sqrt{2}}{4}} + \sqrt{\frac{5 + 3\sqrt{2}}{4}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g310",
        r"Section 2 (p. 204). $g_{310} = \left( \frac{1 + \sqrt{5}}{2} \right) \sqrt{1 + \sqrt{2}} \left( \sqrt{\frac{7 + 2\sqrt{10}}{4}} + \sqrt{\frac{3 + 2\sqrt{10}}{4}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g330",
        r"Section 2 (p. 204). $g_{330} = (\sqrt{6} + \sqrt{5}) \sqrt{\frac{\sqrt{15} + \sqrt{11}}{2}} \left( \frac{\sqrt{5} + 1}{2} \right) (\sqrt{11} + \sqrt{10})^{1/6}$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g522",
        r"Section 2 (p. 204). $g_{522} = \sqrt{\frac{5 + \sqrt{29}}{2}} (5\sqrt{29} + 11\sqrt{6})^{1/6} \left( \sqrt{\frac{9 + 3\sqrt{6}}{4}} + \sqrt{\frac{5 + 3\sqrt{6}}{4}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry02-g630",
        r"Section 2 (p. 204). $g_{630} = (\sqrt{14} + \sqrt{15})^{1/6} \sqrt{(1 + \sqrt{2}) \left( \frac{3 + \sqrt{5}}{2} \right) \left( \frac{\sqrt{3} + \sqrt{7}}{2} \right)} \left( \sqrt{\frac{\sqrt{15} + \sqrt{7} + 2}{4}} + \sqrt{\frac{\sqrt{15} + \sqrt{7} - 2}{4}} \right) \left( \sqrt{\frac{\sqrt{15} + \sqrt{7} + 4}{8}} + \sqrt{\frac{\sqrt{15} + \sqrt{7} - 4}{8}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry03-04",
        r"Entry 3.4 (p. 209, NB 2). $G_{117} = \frac{1}{2} \left( \frac{3 + \sqrt{13}}{2} \right)^{1/4} (2\sqrt{3} + \sqrt{13})^{1/6} \left( 3^{1/4} + \sqrt{4 + \sqrt{3}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry03-06",
        r"Entry 3.6 (p. 212, NB 2). $G_{441} = \sqrt{\frac{2 + \sqrt{7} + \sqrt{7 + 4\sqrt{7}}}{2}} \sqrt{\frac{\sqrt{3} + \sqrt{7}}{2}} (2 + \sqrt{3})^{1/6} \left\{ \frac{\sqrt{3} + \sqrt{7} + 6^{1/4} 7^{1/4}}{\sqrt{3} + \sqrt{7} - 6^{1/4} 7^{1/4}} \right\}^{1/3}$.",
    )
,
    rec(
        "RN-P5-C34-Entry03-07",
        r"Entry 3.7 (p. 214, NB 2). $g_{90} = (2 + \sqrt{5})^{1/6}(\sqrt{5} + \sqrt{6})^{1/6} \left( \sqrt{\frac{3 + \sqrt{6}}{4}} + \sqrt{\frac{\sqrt{6} - 1}{4}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry03-08",
        r"Entry 3.8 (p. 215, NB 2). $g_{198} = \sqrt{1 + \sqrt{2}} (4\sqrt{2} + \sqrt{33})^{1/6} \left( \sqrt{\frac{9 + \sqrt{33}}{8}} + \sqrt{\frac{1 + \sqrt{33}}{8}} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Example07-01",
        r"Example (Section 7, p. 264). Let $p = 5$ and $q = 13$. Then $\alpha_{5,13} = \frac{41 + 5\sqrt{65}}{2}$, $\beta_{5,13} = \frac{33 + 3\sqrt{65}}{2}$, $G_{65} = \left( \sqrt{\frac{\sqrt{65} + 9}{8}} + \sqrt{\frac{\sqrt{65} + 1}{8}} \right)^{1/2} \left( \sqrt{\frac{\sqrt{65} + 7}{8}} + \sqrt{\frac{\sqrt{65} - 1}{8}} \right)^{1/2}$, and $G_{13/5} = \left( \sqrt{\frac{\sqrt{65} + 9}{8}} + \sqrt{\frac{\sqrt{65} + 1}{8}} \right)^{1/2} \left( \sqrt{\frac{\sqrt{65} + 7}{8}} - \sqrt{\frac{\sqrt{65} - 1}{8}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Example07-02",
        r"Example (Section 7, p. 265). Let $p = 3$ and $q = 23$. Then $G_{69} = \left( \sqrt{748 + 432\sqrt{3}} + \sqrt{747 + 432\sqrt{3}} \right)^{1/12} \left( \sqrt{\frac{6 + 3\sqrt{3}}{4}} + \sqrt{\frac{2 + 3\sqrt{3}}{4}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Example07-03",
        r"Section 7 table (p. 267). $G_{213} = \left( \sqrt{\frac{21 + 12\sqrt{3}}{2}} + \sqrt{\frac{19 + 12\sqrt{3}}{2}} \right)^{1/2} \left( \sqrt{542476 + 313200\sqrt{3}} + \sqrt{542475 + 313200\sqrt{3}} \right)^{1/12}$.",
    )
,
    rec(
        "RN-P5-C34-Example07-04",
        r"Section 7 table (p. 267). $G_{217} = \left( \sqrt{\frac{22 + 8\sqrt{7}}{4}} + \sqrt{\frac{18 + 8\sqrt{7}}{4}} \right)^{1/2} \left( \sqrt{\frac{16 + 5\sqrt{7}}{4}} + \sqrt{\frac{12 + 5\sqrt{7}}{4}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Example07-05",
        r"Section 7 table (p. 267). $G_{265} = \left( \sqrt{\frac{89 + 5\sqrt{265}}{8}} + \sqrt{\frac{81 + 5\sqrt{265}}{8}} \right)^{1/2} \left( \sqrt{\frac{16 + \sqrt{265}}{4}} + \sqrt{\frac{12 + \sqrt{265}}{4}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Example07-06",
        r"Section 7 table (p. 267). $G_{301} = \left( \sqrt{\frac{46 + 7\sqrt{43}}{4}} + \sqrt{\frac{42 + 7\sqrt{43}}{4}} \right)^{1/2} \left( \sqrt{\frac{1199 + 184\sqrt{43}}{4}} + \sqrt{\frac{1195 + 184\sqrt{43}}{4}} \right)^{1/4}$.",
    )
,
    rec(
        "RN-P5-C34-Example07-07",
        r"Section 7 table (p. 268). $G_{445} = \left( \sqrt{\frac{71325 + 7560\sqrt{89}}{4}} + \sqrt{\frac{71321 + 7560\sqrt{89}}{4}} \right)^{1/4} \left( \sqrt{\frac{85 + 9\sqrt{89}}{8}} + \sqrt{\frac{77 + 9\sqrt{89}}{8}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Example07-08",
        r"Section 7 table (p. 268). $G_{505} = \left( \sqrt{\frac{292 + 13\sqrt{505}}{4}} + \sqrt{\frac{288 + 13\sqrt{505}}{4}} \right)^{1/2} \left( \sqrt{\frac{113 + 5\sqrt{505}}{8}} + \sqrt{\frac{105 + 5\sqrt{505}}{8}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Example07-09",
        r"Section 7 table (p. 268). $G_{553} = \left( \sqrt{\frac{286 + 32\sqrt{79}}{4}} + \sqrt{\frac{282 + 32\sqrt{79}}{4}} \right)^{1/2} \left( \sqrt{\frac{19163 + 2156\sqrt{79}}{4}} + \sqrt{\frac{19159 + 2156\sqrt{79}}{4}} \right)^{1/4}$.",
    )
,
    rec(
        "RN-P5-C34-Example07-10",
        r"Section 7 table (p. 268). $G_{697} = \left( \sqrt{\frac{769 + 29\sqrt{697}}{8}} + \sqrt{\frac{761 + 29\sqrt{697}}{8}} \right)^{1/2} \left( \sqrt{\frac{661 + 25\sqrt{697}}{8}} + \sqrt{\frac{653 + 25\sqrt{697}}{8}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Example07-11",
        r"Section 7 table (p. 269). $G_{793} = \left( \sqrt{\frac{704 + 25\sqrt{793}}{4}} + \sqrt{\frac{700 + 25\sqrt{793}}{4}} \right)^{1/2} \left( \sqrt{\frac{452 + 16\sqrt{793}}{4}} + \sqrt{\frac{448 + 16\sqrt{793}}{4}} \right)^{1/2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry08-01",
        r"Entry 8.1 (p. 311, NB 1). $G_{75} = \frac{3 \cdot 2^{5/12}}{\frac{\sqrt{5}+1}{2}(10)^{1/3} + \frac{\sqrt{5}-1}{2}4^{1/3} \cdot 5^{1/6} - \sqrt{5}-1}$ and $G_{3/25} = \frac{3 \cdot 2^{5/12}}{\frac{\sqrt{5}+1}{2}4^{1/3} \cdot 5^{1/6} - \frac{\sqrt{5}-1}{2}(10)^{1/3} + \sqrt{5}-1}$.",
    )
,
    rec(
        "RN-P5-C34-Entry08-02",
        r"Entry 8.2 (p. 316, NB 1). $G_{175} = \frac{3 \cdot 2^{1/4}}{\frac{\sqrt{5}-1}{2} + \left(\frac{5-\sqrt{5}}{4}\right)^{1/3} \left(\sqrt[3]{8-3\sqrt{5}+3\sqrt{21}} + \sqrt[3]{8-3\sqrt{5}-3\sqrt{21}}\right)}$ and $G_{25/7} = \frac{3 \cdot 2^{1/4}}{\frac{\sqrt{5}+1}{2} + \left(\frac{5+\sqrt{5}}{4}\right)^{1/3} \left(\sqrt[3]{8+3\sqrt{5}+3\sqrt{21}} + \sqrt[3]{8+3\sqrt{5}-3\sqrt{21}}\right)}$.",
    )
,
    rec(
        "RN-P5-C34-Entry08-03",
        r"Entry 8.3 (p. 263, NB 2). Let $t = 1/G_{29}^4$ and let $x$ denote the positive real root of $x^6 + 9x^5 + 5x^4 - 2x^3 - 5x^2 + 9x - 1 = 0$. Then $x = t^4$, where $t > 0$. Furthermore, $\frac{t^6 + t^2}{1 - t^4} = \sqrt{\frac{\sqrt{29}-5}{2}}$ and $\frac{t^3 + t\sqrt{\sqrt{29}-2}}{1 + t^2\sqrt{\sqrt{29}+2}} = \sqrt{\frac{\sqrt{29}-5}{2}}$. Lastly, if $\sqrt[4]{1-t^8} = t(1 + \mu^2)$, where $\mu > 0$, then $\mu^3 + \mu = \sqrt{2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry08-04",
        r"Entry 8.4 (pp. 263, 300, NB 2). Let $t = 2^{1/4}/G_{79}$. Then $t$ is the real root of $t^5 - t^4 + t^3 - 2t^2 + 3t - 1 = 0$. Furthermore, if $\sqrt{\frac{1}{t} - t} = \mu$, then $\mu^5 - 2\mu^4 + \mu^3 + 2\mu - 3 = 0$.",
    )
,
    rec(
        "RN-P5-C34-Entry08-05",
        r"Entry 8.5 (p. 382, NB 3). Let $z = x + 1/x$, where $x = G_{41}^2$. Then $z^2 - z \frac{5 + \sqrt{41}}{2} + \frac{7 + \sqrt{41}}{2} = 0$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-02-02",
        r"Theorem 9.2 (p. 281, NB 1). $\alpha_{2} = (\sqrt{2} - 1)^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-02-06",
        r"Theorem 9.2 (p. 281, NB 1). $\alpha_{6} = (2 - \sqrt{3})^2(\sqrt{3} - \sqrt{2})^2 = \frac{\sqrt{6} - \sqrt{2} - 1}{\sqrt{6} + \sqrt{2} + 1}$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-02-10",
        r"Theorem 9.2 (p. 281, NB 1). $\alpha_{10} = (\sqrt{10} - 3)^2(3 - 2\sqrt{2})^2 = \frac{3\sqrt{2} - \sqrt{5} - 2}{3\sqrt{2} + \sqrt{5} + 2}$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-02-18",
        r"Theorem 9.2 (p. 281, NB 1). $\alpha_{18} = (5\sqrt{2} - 7)^2(7 - 4\sqrt{3})^2 = \frac{7\sqrt{2} - 2\sqrt{6} - 5}{7\sqrt{2} + 2\sqrt{6} + 5}$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-02-22",
        r"Theorem 9.2 (p. 281, NB 1). $\alpha_{22} = (10 - 3\sqrt{11})^2(3\sqrt{11} - 7\sqrt{2})^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-02-30",
        r"Theorem 9.2 (p. 281, NB 1). $\alpha_{30} = (5 - 2\sqrt{6})^2(4 - \sqrt{15})^2(\sqrt{6} - \sqrt{5})^2(2 - \sqrt{3})^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-02-42",
        r"Theorem 9.2 (p. 281, NB 1). $\alpha_{42} = (8 - 3\sqrt{7})^2(7 - 4\sqrt{3})^2(3 - 2\sqrt{2})^2(\sqrt{7} - \sqrt{6})^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-02-58",
        r"Theorem 9.2 (p. 281, NB 1). $\alpha_{58} = (13\sqrt{58} - 99)^2(99 - 70\sqrt{2})^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-02-70",
        r"Theorem 9.2 (p. 281, NB 1). $\alpha_{70} = (15 - 4\sqrt{14})^2(8 - 3\sqrt{7})^2(3\sqrt{14} - 5\sqrt{5})^2(6 - \sqrt{35})^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-02-78",
        r"Theorem 9.2 (p. 281, NB 1). $\alpha_{78} = (2 - \sqrt{3})^6(3\sqrt{3} - \sqrt{26})^2(\sqrt{13} - 2\sqrt{3})^4(5 - 2\sqrt{6})^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-02-102",
        r"Theorem 9.2 (p. 281, NB 1). $\alpha_{102} = \left( \frac{\sqrt{51} - 7}{\sqrt{2}} \right)^4 (5 - 2\sqrt{6})^4 (\sqrt{51} - 5\sqrt{2})^2 (2 - \sqrt{3})^4$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-02-130",
        r"Theorem 9.2 (p. 281, NB 1). $\alpha_{130} = (5\sqrt{130} - 57)^2(\sqrt{10} - 3)^4(\sqrt{26} - 5)^4(3 - 2\sqrt{2})^4$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-02-190",
        r"Theorem 9.2 (p. 281, NB 1). $\alpha_{190} = \left( \frac{3\sqrt{19} - 13}{\sqrt{2}} \right)^4 (37\sqrt{19} - 51\sqrt{10})^2 (2\sqrt{5} - \sqrt{19})^4 (\sqrt{19} - 3\sqrt{2})^4$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-09-03",
        r"Theorem 9.9 (p. 290, NB 1). $\alpha_{3} = \frac{2 - \sqrt{3}}{4}$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-09-05",
        r"Theorem 9.9 (p. 290, NB 1). $\alpha_{5} = \frac{1}{2} \left( \frac{\sqrt{5} - 1}{2} \right)^3 \left( \sqrt{\frac{3 + \sqrt{5}}{4}} - \sqrt{\frac{\sqrt{5} - 1}{4}} \right)^4$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-09-07",
        r"Theorem 9.9 (p. 290, NB 1). $\alpha_{7} = \frac{8 - 3\sqrt{7}}{16}$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-09-09",
        r"Theorem 9.9 (p. 290, NB 1). $\alpha_{9} = \frac{1}{2} \left( \frac{\sqrt{3} - 1}{\sqrt{2}} \right)^4 \left( \sqrt{\frac{3 + \sqrt{3}}{4}} - \sqrt{\frac{\sqrt{3} - 1}{4}} \right)^8$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-09-13",
        r"Theorem 9.9 (p. 290, NB 1). $\alpha_{13} = \frac{1}{2} \left( \frac{\sqrt{13} - 3}{2} \right)^3 \left( \sqrt{\frac{7 + \sqrt{13}}{4}} - \sqrt{\frac{3 + \sqrt{13}}{4}} \right)^4$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-09-15",
        r"Theorem 9.9 (p. 290, NB 1). $\alpha_{15} = \frac{1}{16} \left( \frac{\sqrt{5} - 1}{2} \right)^4 (2 - \sqrt{3})^2 (4 - \sqrt{15})$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-09-17",
        r"Theorem 9.9 (p. 290, NB 1). $\alpha_{17} = \frac{1}{2} \left( \sqrt{\frac{7 + \sqrt{17}}{4}} - \sqrt{\frac{3 + \sqrt{17}}{4}} \right)^4 \left( \sqrt{\frac{3 + \sqrt{4 + \sqrt{17}}}{4}} - \sqrt{\frac{\sqrt{4 + \sqrt{17}} - 1}{4}} \right)^8$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-09-21",
        r"Theorem 9.9 (p. 290, NB 1). $\alpha_{21} = \frac{1}{2} \left( \frac{3 - \sqrt{7}}{\sqrt{2}} \right)^2 \left( \frac{\sqrt{7} - \sqrt{3}}{2} \right)^3 \left( \sqrt{\frac{5 + \sqrt{7}}{4}} - \sqrt{\frac{1 + \sqrt{7}}{4}} \right)^4 \left( \sqrt{\frac{3 + \sqrt{7}}{4}} - \sqrt{\frac{\sqrt{7} - 1}{4}} \right)^4$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-09-25",
        r"Theorem 9.9 (p. 290, NB 1). $\alpha_{25} = \frac{1}{2} (161 - 72\sqrt{5}) \left( \sqrt{\frac{5 + \sqrt{5}}{4}} - \sqrt{\frac{1 + \sqrt{5}}{4}} \right)^8$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-09-33",
        r"Theorem 9.9 (p. 290, NB 1). $\alpha_{33} = \frac{1}{2} (2 - \sqrt{3})^3 \left( \frac{\sqrt{11} - 3}{\sqrt{2}} \right)^2 \left( \sqrt{\frac{7 + 3\sqrt{3}}{4}} - \sqrt{\frac{3 + 3\sqrt{3}}{4}} \right)^4 \left( \sqrt{\frac{5 + \sqrt{3}}{4}} - \sqrt{\frac{1 + \sqrt{3}}{4}} \right)^4$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-09-45",
        r"Theorem 9.9 (p. 290, NB 1). $\alpha_{45} = \frac{1}{2} (\sqrt{5} - 2)^3 \left( \frac{\sqrt{5} - \sqrt{3}}{\sqrt{2}} \right)^4 \left( \sqrt{\frac{7 + 3\sqrt{5}}{4}} - \sqrt{\frac{3 + 3\sqrt{5}}{4}} \right)^4 \left( \sqrt{\frac{3 + \sqrt{5}}{2}} - \sqrt{\frac{1 + \sqrt{5}}{2}} \right)^4$.",
    )
,
    rec(
        "RN-P5-C34-Entry09-09-55",
        r"Theorem 9.9 (p. 290, NB 1). $\alpha_{55} = \frac{1}{16}(\sqrt{5}-2)^2(10-3\sqrt{11})(3\sqrt{5}-2\sqrt{11}) \left(\sqrt{\frac{7+\sqrt{5}}{8}} - \sqrt{\frac{\sqrt{5}-1}{8}}\right)^{12} \left(\sqrt{\frac{4+\sqrt{5}}{2}} - \sqrt{\frac{2+\sqrt{5}}{2}}\right)^4$.",
    )
,
    rec(
        "RN-P5-C34-Example09-15a",
        r"Example 9.15(a) (p. 302). Let $n = 3$. Then $(\alpha\beta)^{1/4} + \{(1-\alpha)(1-\beta)\}^{1/4} = 1$, and $\alpha_6 = (2-\sqrt{3})^2(\sqrt{3}-\sqrt{2})^2 = \frac{2\sqrt{3}+\sqrt{6}-3-2\sqrt{2}}{2\sqrt{3}+\sqrt{6}+3+2\sqrt{2}}$.",
    )
,
    rec(
        "RN-P5-C34-Example09-15b",
        r"Example 9.15(b) (p. 303). Let $n = 5$. Then $(\alpha\beta)^{1/2} + \{(1-\alpha)(1-\beta)\}^{1/2} + 2\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/6} = 1$, and $\alpha_{10} = (\sqrt{10}-3)^2(3-2\sqrt{2})^2 = \frac{3\sqrt{10}+6\sqrt{2}-9-4\sqrt{5}}{3\sqrt{10}+6\sqrt{2}+9+4\sqrt{5}}$.",
    )
,
    rec(
        "RN-P5-C34-Example09-17a",
        r"Example 9.17(a) (p. 306). Let $n = 1$. Then $\alpha_3 = \frac{2-\sqrt{3}}{4}$.",
    )
,
    rec(
        "RN-P5-C34-Example09-17b",
        r"Example 9.17(b) (p. 306). Let $n = 5$. Then $\alpha_{15} = \frac{16-7\sqrt{3}-\sqrt{15}}{32}$.",
    )
,
    rec(
        "RN-P5-C34-Entry10-01",
        r"Section 10 (p. 306). $U_{1} = 1$.",
    )
,
    rec(
        "RN-P5-C34-Entry10-03",
        r"Section 10 (p. 306). $U_{3} = 3$.",
    )
,
    rec(
        "RN-P5-C34-Entry10-05",
        r"Section 10 (p. 306). $U_{5} = 9$.",
    )
,
    rec(
        "RN-P5-C34-Entry10-07",
        r"Section 10 (p. 306). $U_{7} = (\sqrt{2} + 1)^2(1 + 2\sqrt{2})$.",
    )
,
    rec(
        "RN-P5-C34-Entry10-09",
        r"Section 10 (p. 306). $U_{9} = 49$.",
    )
,
    rec(
        "RN-P5-C34-Entry10-11",
        r"Section 10 (p. 306). $U_{11} = 99$.",
    )
,
    rec(
        "RN-P5-C34-Entry10-15",
        r"Section 10 (p. 306). $U_{15} = 3(5 + 4\sqrt{2})^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry10-23",
        r"Section 10 (p. 306). $U_{23} = 9(1 + \sqrt{2})^4(3 + 4\sqrt{2})$.",
    )
,
    rec(
        "RN-P5-C34-Entry10-29",
        r"Section 10 (p. 306). $U_{29} = 99^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry10-35",
        r"Section 10 (p. 306). $U_{35} = 63(8\sqrt{2} + 5\sqrt{3})^2$.",
    )
,
    rec(
        "RN-P5-C34-Entry10-71",
        r"Section 10 (p. 306). $U_{71} = 9(1 + \sqrt{2})^{10}(2\sqrt{2} + 1)^2(6\sqrt{2} + 1)$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-01",
        r"Entry 11.1 (p. 310). $J_3 = 0$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-02",
        r"Entry 11.2 (p. 310). $J_{27} = 5 \cdot 3^{1/3}$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-03",
        r"Entry 11.3 (p. 310). $J_{11} = 1$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-04",
        r"Entry 11.4 (p. 310). $J_{19} = 3$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-05",
        r"Entry 11.5 (p. 310). $J_{43} = 30$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-06",
        r"Entry 11.6 (p. 311). $J_{67} = 165$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-07",
        r"Entry 11.7 (p. 311). $J_{163} = 20{,}010$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-08",
        r"Entry 11.8 (p. 311). $J_{35} = \sqrt{5} \left( \frac{\sqrt{5} + 1}{2} \right)^4$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-09",
        r"Entry 11.9 (p. 311). $J_{51} = 3 (\sqrt{17} + 4)^{2/3} \left( \frac{5 + \sqrt{17}}{2} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-10",
        r"Entry 11.10 (p. 311). $J_{75} = 3 \cdot 5^{1/6} \left( \frac{69 + 31\sqrt{5}}{2} \right)$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-11",
        r"Entry 11.11 (p. 311). $J_{91} = \frac{1}{2} (227 + 63\sqrt{13})$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-12",
        r"Entry 11.12 (p. 311). $J_{99} = \frac{1}{2} (23 + 4\sqrt{33})^{2/3} (77 + 15\sqrt{33})$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-13",
        r"Entry 11.13 (p. 312). $J_{115} = \frac{1}{2}(785 + 351\sqrt{5})$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-14",
        r"Entry 11.14 (p. 312). Let $u_n$ be defined by (11.3) and define $p > 0$ by $u_{59} = \frac{(1-p^8)^3}{p^8}$. Then $p^9 - 7p^8 + 22p^7 - 34p^6 + 40p^5 - 28p^4 + 22p^3 - 10p^2 + 11p - 1 = 0$. Furthermore, $u_{59}^{1/3}$ satisfies an irreducible cubic polynomial over $\mathbb{Q}$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-15",
        r"Entry 11.15 (p. 312). Let $u_n$ be defined by (11.3). Define $s > 0$ by $u_{83} = \frac{(1-256s^{24})^3}{256s^{24}}$ and set $\beta = \frac{1-2s-2s^2-2s^3}{2s^3}$. Then $\beta^3 + 4\beta^2 + 2\beta - 5 = 0$. Furthermore, $u_{83}^{1/3}$ satisfies an irreducible cubic polynomial over $\mathbb{Q}$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-16",
        r"Entry 11.16 (p. 316). For $q = \exp(-\pi\sqrt{n})$, define $t_n := \frac{1}{3}\sqrt{1 + \frac{8}{3}J_n}$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-17",
        r"Entry 11.17 (p. 313). For $q = \exp(-\pi\sqrt{n})$, define $t := t_n := \sqrt{3}\, q^{1/18} \frac{f(q^{1/3})f(q^3)}{f^2(q)}$. Then $t_n = \left( 2\sqrt{64J_n^2 - 24J_n + 9} - (16J_n - 3) \right)^{1/6}$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-18",
        r"Entry 11.18 (p. 314). For $n \in \{11, 35, 59, 83, 107\}$, the polynomials $p_n(t)$ satisfied by $t_n$ are: $t-1$; $t^2+t-1$; $t^3+2t-1$; $t^4+2t^2+2t-1$; $t^5-2t^2+4t-1$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-19",
        r"Entry 11.19 (p. 317). For $n \in \{19, 43, 67, 91, 115, 163\}$, we have $t_{19} = 1$, $t_{43} = 3$, $t_{67} = 7$, $t_{91} = 7 + 2\sqrt{13}$, $t_{115} = 13 + 6\sqrt{5}$, and $t_{163} = 77$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-20",
        r"Entry 11.20 (p. 318). Let $t_n$ be defined by (11.16). Then, as $n$ tends to $\infty$, $t_n \sim \frac{e^{\pi\sqrt{n}/6} + 6e^{-\pi\sqrt{n}/6}}{6\sqrt{3}}$.",
    )
,
    rec(
        "RN-P5-C34-Entry11-21",
        r"Entry 11.21 (p. 318). Let $q = \exp(-\pi\sqrt{n})$ and put $R := R_n := 3^{1/4} q^{1/36} \frac{f(q)}{f(q^{1/3})}$. Then $\frac{3\sqrt{3}}{R_n^6} = \sqrt{8J_n + 3} + \sqrt{2\sqrt{64J_n^2 - 24J_n + 9} - 8J_n + 6}$.",
    )
,
]
