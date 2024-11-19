
---
**DISCLAIMER: No definitions will be written here if they are too *obvious*, only if they relate to a theorem I have to prove.**
#### Theorem 1.3.7

>[!important] Theorem 1.3.7: The bijection between equivalence relations and the partitions of the set
>$$
>\begin{flalign}
>(i) &\text{ Let } r \in E(A).\text{ }Then \text{ } A / r \in P(A) \\ 
>(ii) &\text{ Let } \pi = (A_{i})_{i \in I} \in P(A). \text{ } Then \text{ } r_{\pi} \in E(A)\\ 
>(iii) &\text{ } Let F:E(a)\to P(A) \text{ be defined by }\\ 
\end{flalign}
>$$ 
>$$
>\begin{align}
>F(r) = A / r, \text{ } \forall r \in E(A)\\ 
\end{align}
>$$
>$$
>\begin{flalign}
\text{Then } F \text{ is a bijection, whose inverse is } G: P(A)\to E(A), \text{ defined by}
\end{flalign}
>$$
>$$
>G(\pi) = r_{\pi}, \text{ } \forall \pi \in P(A)
>$$

**Proof:**
**(i)**
$\text{Since r is reflexive, we have } x \in r<x>, \forall x \in A, \text{ hence } A \subseteq \bigcup_{x \in A}\text{ } r<x>$
$\text{Obviously, we also have }\bigcup_{x \in A}\text{ }r<x> \subseteq A.\text{ Therefore, }A= \bigcup_{x \in A}\text{ } r<x>$
Now let $x, y \in A$ and $a\in r<x> \cap\text{ } r<y>$. Then $xra$ and $yra,$ hence $xry$ and $yrx$ by the symmetry and the transitivity of $r$. Then $y \in\text{ }r<x>$ and $x \in\text{ }r<y>$, whence we get $r<x> =r<y>$. Hence, the equivalence classes in $A / r$ are pairwise disjoint (we took an element from an intersection of classes, and saw that they are actually THE SAME class, thus for two classes to be actually different, their intersection must be 0 $p\to q \to \neg q\to \neg p$). 
**Therefore**, $A / r \in P(A)$ (the sets given in $A/r$ are pairwise disjoint)

**(ii)**
The relation $r$ is reflexive and symmetric (`x is from the same partition as x, and xry and yrx clearly ,because they are in the same partition`). Let $x, y, z \in A$ s.t $xr_{\pi}y$ and $yr_{\pi}z$ $\implies$ $\exists i, j \in I$ s.t $x, y \in A_{i}$ and $y, z \in A_{j}$. Thus, we see that $j \in A_{i}\cap A_{j}$. But two different sets from a partition are disjoint, and ${j}\neq \emptyset$, so $A_{i}=A_{j}\implies z\in A_{i}$, and since $x \in A_{i} \implies xr_{\pi}z$. Thus, $r_{\pi}$ is transitive too. **Therefore** $r_{\pi} \in E(A)$

**(iii)** To show that F and G are bijective and each other's inverse, it is enough to show the inverse part, since any invertible function is bijective.
So we show that $G\circ F =1_{E(A)}$ and $F\circ G = 1_{P(A)}$, the identities of the respective domains
For $\forall r \in E(A)$, we have
$$
\begin{align}
(G\circ F)(r) = G(A/ r) = r
\end{align}
$$
because for $\forall x, y \in A,$
$$
xG(A / r)y \iff \exists a\in A: x, y\in r<a> \iff xry
$$
For $\forall \pi =(A_{i})_{i\in I}\in P(A),$ we have
$$
(F\circ G)(\pi) = F(G(\pi))=A / G(\pi) = A / r_{\pi} =\{ r_{\pi}<x> | x \in A \} = \pi
$$
because for $\forall x \in A,$ the class of the partition $A / G(\pi)$ containing x is the same as the class of the partition $\pi$ containing $x$. Indeed, let $x \in A_{i}$. Then
$$
r_{\pi}<x> = \{ y \in A|xr_{\pi}y \} = \{ y\in A | y\in A_{i} \} = A_{i}
$$
Thus, $G\circ F = 1_{E(A)}$ and $F\circ G = 1_{P(A)}$, that is , F and G are **bijections**
$\square$
