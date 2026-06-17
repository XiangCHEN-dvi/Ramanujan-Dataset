"""Part I, Chapter 1 entries — AI curated LaTeX."""

from __future__ import annotations

TOPICS_C01 = ["magic-squares"]


def rec(entry_id: str, content: str) -> dict:
    return {"id": entry_id, "content": content, "topics": TOPICS_C01}


CHAPTER_1 = [
    rec(
        "RN-P1-C01-Example01",
        r"Given that $A+P=8$, $B+P=10$, $C+P=11$, $D+P=14$, and $C+R=25$, find $A+R$, $B+R$, and $D+R$.",
    ),
    rec(
        "RN-P1-C01-Example02",
        r"Given $A+P=5$, $A+Q=7$, $A+S=17$, $B+Q=23$, and $B+R=26$, find $A+R$, $B+P$, and $B+S$.",
    ),
    rec(
        "RN-P1-C01-Entry02i",
        r"Let $m_1$ and $m_2$ denote the sums of the middle row and middle column, respectively, of a $3\times 3$ square array of numbers. Let $c_1$ and $c_2$ denote the sums of the main diagonal and secondary diagonal, respectively. Let $S$ denote the sum of all nine elements, and let $x$ denote the center element. Then $m_1+m_2+c_1+c_2=S+3x$.",
    ),
    rec(
        "RN-P1-C01-Entry02ii",
        r"Suppose that the sum of each row and each column of a $3\times 3$ square equals $r$. In the notation of Entry 2(i), the center element is $x=\dfrac{c_1+c_2-r}{2}$. If the square is magic, then $x=r/3$ and $r$ is a multiple of $3$.",
    ),
    rec(
        "RN-P1-C01-Entry02-Corollary01",
        r"In a $3\times 3$ magic square with common row, column, and diagonal sum $r$, the three elements in the middle row, the middle column, and each diagonal are in arithmetic progression (with middle term $r/3$).",
    ),
    rec(
        "RN-P1-C01-Entry02-Example01",
        r"Construct $3\times 3$ magic squares with (i) $r=15$ and all entries odd, and (ii) $r=27$ and all entries odd. "
        r"Solutions: $\begin{smallmatrix}6&1&8\\7&5&3\\2&9&4\end{smallmatrix}$ and $\begin{smallmatrix}15&1&11\\7&17&3\\13&5&9\end{smallmatrix}$.",
    ),
    rec(
        "RN-P1-C01-Entry02-Example02",
        r"Construct $3\times 3$ magic squares with (i) $r=36$ and all entries even, and (ii) $r=63$ with all entries divisible by $3$. "
        r"Solutions: $\begin{smallmatrix}14&4&18\\12&12&12\\16&20&10\end{smallmatrix}$ and $\begin{smallmatrix}24&9&30\\21&21&21\\27&33&3\end{smallmatrix}$.",
    ),
    rec(
        "RN-P1-C01-Example03i",
        r"Construct a $3\times 3$ square with all row and column sums equal to $19$ but with only one diagonal sum equal to $19$. "
        r"Solution: $\begin{smallmatrix}10&2&7\\4&6&9\\5&11&3\end{smallmatrix}$.",
    ),
    rec(
        "RN-P1-C01-Example03ii",
        r"Construct a $3\times 3$ square with all row and column sums equal to $31$ but with only one diagonal sum equal to $31$ (Ramanujan also asks that all entries be odd). "
        r"Solution: $\begin{smallmatrix}14&5&12\\7&11&13\\10&15&6\end{smallmatrix}$.",
    ),
    rec(
        "RN-P1-C01-Example04i",
        r"Construct a $3\times 3$ square with all row and column sums equal to $20$ and diagonal sums $16$ and $19$. "
        r"Solution: $\begin{smallmatrix}10&2&8\\4&5&11\\6&13&1\end{smallmatrix}$.",
    ),
    rec(
        "RN-P1-C01-Example04ii",
        r"Construct a square with diagonal sums $15$ and $19$, column sums $16$, $17$, $12$, and row sums $6$, $21$, $18$. "
        r"Solution: $\begin{smallmatrix}1&2&3\\8&9&4\\7&6&5\end{smallmatrix}$.",
    ),
    rec(
        "RN-P1-C01-Example05",
        r"Construct $3\times 4$ rectangles whose average row sum and average column sum equal (i) $8$, and (ii) $15$ with all entries odd.",
    ),
    rec(
        "RN-P1-C01-Entry06i",
        r"In a $4\times 4$ square, the sum of the middle four elements equals $\tfrac12\bigl(\text{(sum of diagonals)}+\text{(sum of middle rows)}+\text{(sum of middle columns)}-\text{(total sum)}\bigr)$.",
    ),
    rec(
        "RN-P1-C01-Entry06ii",
        r"Construct a $4\times 4$ magic square by letting $S_1=\{A,B,C,D\}$ and $S_2=\{P,Q,R,S\}$ and placing the nine sums $A+P$, $B+Q$, etc., in a $4\times 4$ array so that each letter from $S_1$ and $S_2$ appears exactly once in each row, column, and diagonal.",
    ),
    rec(
        "RN-P1-C01-Entry06-Example01",
        r"Construct $4\times 4$ magic squares with common sum $34$ (Ramanujan gives three examples with sums $34$, $34$, and $35$).",
    ),
    rec(
        "RN-P1-C01-Entry06-Example02",
        r"Construct two $4\times 4$ magic squares with common sum $66$.",
    ),
    rec(
        "RN-P1-C01-Entry06-Example03",
        r"Construct two $3\times 3$ magic squares with common sum $60$.",
    ),
    rec(
        "RN-P1-C01-Example06",
        r"Construct $5\times 5$ magic squares with common sums $65$ and $66$.",
    ),
    rec(
        "RN-P1-C01-Example07",
        r"Construct $7\times 7$ magic squares with common sums $170$ and $175$.",
    ),
]

