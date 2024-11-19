>[!question]
>5. Let f ∈ EndR(R 3 ) be defined by f(x, y, z) = (−y + 5z, x, y − 5z). Determine a basis and the dimension of Ker f and Im f.

$$
Kerf = \{ (x, y, z) \in \mathbb{R}^3 | \begin{cases}
-y+5z = 0  \\
x = 0 \\
y-5z = 0
\end{cases}\} = \{  (0, 5z, z) | z \in \mathbb{R}\} = <(0, 5, 1)> \implies dim(Kerf) = 1
$$

$$
\begin{align}
\mathrm{Im} f &= \{  (x, y, z) | (x, y, z) \in \mathbb{R}^3 \} =\\
&= \{ (-y+5z, x, y-5z) | x, y, z \in \mathbb{R} \} \\
&= \{  X(0, 1, 0) + y(-1, 0, 1) + z(5, 0, -5) | x, y, z \in \mathbb{R} \} \\
&= <(0, 1, 0), (-1, 0, 1), (5, 0, -5)>
\end{align}
$$

$$ 
\begin{vmatrix}
0 & 1 & 0 \\
-1 & 0 & 1 \\
5 & 0 & -5
\end{vmatrix}
= 0 + 5 - 5 - 0 = 0
$$
$$ 
\begin{flalign}
&\begin{vmatrix}
0 & 1 \\
-1 & 0
\end{vmatrix}
\neq 0
\xRightarrow[\text{it's a lin. comb. of (0, 1, 0) and (-1, 0, 1)}]{\text{remove (5, 0, -5) because}} (5, 0, -5) \in <(0, 1, 0), (-1, 0, 1)> 
 \\
&(0, 1, 0) \text{ and } (-1, 0, 1) \text{ lin. ind.}
\end{flalign}
$$
$$
\implies B = ((0, 1, 0), (-1, 0, 1)) \text{ basis for Im f} \implies dim(\mathrm{Im}f) = 2
$$