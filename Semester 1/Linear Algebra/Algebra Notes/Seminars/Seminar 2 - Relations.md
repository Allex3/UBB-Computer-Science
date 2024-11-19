>[!question] 
>4. Which ones of the properties of reflexivity, transitivity and symmetry hold for the following homogeneous relations: the strict inequality relations on R, the divisibility relation on N and on Z, the perpendicularity relation of lines in space, the parallelism relation of lines in space, the congruence of triangles in a plane, the similarity of triangles in a plane?




$$
\begin{align}
x<y: \text{not reflexive (not 1<1), not symmetric (1<2 but not 2<1)} \\
\text{but is transitive: x<y and y<z } \implies x<z
\end{align} 
$$
>[!question] 
>7. Let n ∈ N. Consider the relation ρn on Z, called the congruence modulo n, defined by: x ρn y ⇐⇒ n|(x − y). Prove that ρn is an equivalence relation on Z and determine the quotient set (partition) Z/ρn. Discuss the cases n = 0 and n = 1.

$$
\begin{flalign} 
&\text{reflexivity: } x\rho_{n}r  \iff n|(x-x) \iff n|0 \text{ (True)}  \\ 
&\text{symmetry: } x\rho_{n}y  \iff n|(x-y) \implies n|-(x-y) \iff n|(y-x) \iff y\rho_{n}x \\
&\text{transitivity: } x\rho_{n}y \text{ and } y\rho_{n}z \iff n|(x-y), n|(y-z) \implies n|[(x-y)+(y-z)] \iff 
n|(x-z) \iff x\rho_{n}z \\
&\text{In conclusion, }\rho_{n} \text{ is an equivalence relation on } \mathbb{Z}
\end{flalign}
$$

$$
\begin{flalign}
\rho/\mathbb{Z} = \{\rho<x> | x \in \mathbb{Z} \} = \{\{ x+nk | k \in \mathbb{Z}\}|x\in\mathbb{Z}\} = \{ \hat{x} | x\in\mathbb{Z}\}
\end{flalign}
$$
>[!question]
>8. Determine all equivalence relations and all partitions on the set M = {1, 2, 3}.

$$
\begin{align}
M &= \{1, 2, 3\} \\ \\
P_{1} &= \{\{1, 2, 3\}\} \implies R_{1} = \{ (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3,2), (3, 3)\} \\ 
P_{2} &=  \{\{1, 2\} \{3\} \} \implies R_{2} = \{(1, 1), (1, 2), (2, 1), (2, 2),(3, 3)\}    \\
etc
\end{align}
$$

>[!question ] 
>10. Consider the following homogeneous relations on N, defined by: m r n ⇐⇒ ∃a ∈ N : m = 2an , m s n ⇐⇒ (m = n or m = n 2 or n = m2 ). Are r and s equivalence relations?

$$
\begin{align}
&mrn \iff \exists a \in \mathbb{N}: m=2^an \\
&\text{reflexivity}: a=0 \implies \forall m \in \mathbb{N}: m=m = 2^0m \\
&symmetry: 4=2^2 *1, \text{but } \nexists a\in \mathbb{N} s.t 1=2^a*4  \implies \text{r is not symmetric} \\
&\text{In conclusion, r is not an equivalent relation}
\end{align}
$$
$$
\begin{align}
&\text{For s, if we have }m=n^2, \text{invert them so } n = m^2, \text{the variables I mean, so } \\
&\text{It is symmetric, and it is also reflexive since } n=m \text{ is a condition}  \\
&\text{But is it transitive? NO} \\
&16s 4 \iff 16=4^2, 4s 2 \iff 4=2^2, \text{but } 16s 2 \text{ cannot be true}
\end{align}
$$





