>[!question] 
>?

$$
\begin{flalign}
&f: \mathbb{R}^2\to \mathbb{R}^2  \\
&f(4, 5) = (1, 0) \\
&f(5, 6) = (0, 1) \\
&Find f(8, 9) \\
 \\
\end{flalign}
$$
$$
B = <(4, 5), (5, 6)> \text{ basis of } \mathbb{R}^2 \text{ because } dim_{\mathbb{R}}\mathbb{R}^2 = 2\text{ and (4, 5) and (5, 6) linearly independent} 
$$

$\text{We write (8, 9) in the basis B:}$

$$
\begin{align}
(8, 9) = a(4, 5) +b(5, 6) \\
\end{align}
$$
$$
\begin{cases}
4a+5b = 8 \\
5a + 6b = 9 \\
\end{cases}
\implies 
\begin{cases}
a = \frac{8-5b}{4} \\
9 = \frac{40-25b}{4} + 6b = 10-\frac{b}{4}
\end{cases} \implies \frac{b}{4} = 1 \implies b=4 \implies a=-3
$$
$$
[(8, 9)] = \begin{pmatrix}
-3 \\
4
\end{pmatrix} \implies (8, 9) = -3(4, 5) + 4(5, 6) \implies 
$$
$$
\implies f(8, 9) = f(-3(4, 5) + 4(5, 6)) = -3f(4,5) +4f(5, 6) = -3(1, 0) +4(0, 1) = (-3, 4)
$$

