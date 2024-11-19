
---
#### Theorem 2.6.3 (Linearly dependent if one is a lin. comb. of the others)
>[!important] Let $V$ be a vector space over $K$. Then the vectors $v_{1},\dots,v_{n}\in V$ are *linearly dependent* if and only if one of the vectors is a linear combination of the others, that is, $\exists j\in \{ 1,\dots,n \}$ such that 
>$$\sum_{\substack {i=1 \\ i\neq j}}^n=\alpha_{i}v_{i}$$
>for some $\alpha_{i}\in K$, where $i\in \{ 1,\dots,n \}$ and $i\neq j$



*Proof:*
$\fbox{=>}$ Assume that $v_{1},v_{2},\dots,v_{n}\in V$ are linearly dependent. 
Then $\exists k_{1},k_{2},\dots,k_{n}\in K$ not all zero, say $k_{j}\neq_{0}$, such that $k_{1}v_{1}+\dots+k_{n}v_{n}=0 \implies$
$$-k_{j}v_{j}=\sum_{\substack{i=1\\ i\neq j}}^nk_{i}v_{i}$$

 And further,
 $$v_{j}=\sum_{\substack{i=1 \\ i\neq j}}^n(-k_{j}^{-1}k_{i})v_{i}$$
 Now choose $\alpha_{i}=-k_{j}^{-1}k_{i}$ for each $i\neq j$, and thus 
 $$v_{j}=\sum_{\substack{i=1 \\ i\neq j}}^n\alpha_{i}v_{i}$$
 So one of the vectors is indeed a linear combination of the others.
 $\fbox{<=}$  Assume that $\exists j\in \{ 1,\dots,n \}$ such that $v_{j}=\sum_{\substack{i=1 \\ i\neq j}}^nk_{i}v_{i} \implies (-1)\cdot v_{j}+\sum_{\substack{i=1 \\ i\neq j}}^nk_{i}v_{i}=0$
 Thus, we have a linear combinations of all the vectors $v_{1},\dots,v_{n}\in V$ that is zero and a coefficient is not zero, so they are linearly dependent
$\square$

#### Theorem 2.6.5 (Relation between the components of a linearly dependence)
>[!important] Let $n\in \mathbb{N},n\geq 2$
>*(i)* Two vectors in the canonical vector space $K^n$ are linearly dependent $\iff$ their components are respectively proportional
>*(ii)* $n$ vectors in the canonical vector space $K^n$ are linearly dependent $\iff$ the determinant consisting of their components is zero.

*Proof:*
*(i)*: Let $v=(x_{1},\dots,x_{n}),\;v'=(x_{1}',\dots,x_{n}')\in K^n$. By [[#Theorem 2.6.3 (Linearly dependent if one is a lin. comb. of the others)]], the two vectors are linearly independent if and only if one of them is a linear combination of the other, say $v'=kv,$ for some $k\in K$.
That is $x_{i}'=kx_{i},\forall i\in \{ 1,..,n \}$. No need to prove each implication because we got here by equivalences
*(ii)* Let $v_{1}=(x_{11},x_{21},\dots,x_{n1}),\dots,v_{n}=(x_{1n},x_{2n},\dots,x_{nn})\in K^n$..
The vectors $v_{1},\dots,v_{n}$ are linearly dependent if and only if $\exists k_{1},\dots,k_{n}\in K$ not all zero such that
$$k_{1}v_{1}+\dots+k_{n}v_{n}=0$$
But this is equivalent to:
$$k_{1}(x_{11},x_{21},\dots,x_{n1})+\dots+k_{n}(x_{1n},x_{2n},\dots,x_{nn})=(0,\dots,0)$$
and further to
$$
\begin{cases}
k_{1}x_{11}+k_{2}x_{12}+\dots+k_{n}x_{1n}=0 \\
k_{1}x_{21}+k_{2}x_{22}+\dots+k_{n}x_{2n}=0 \\
\dots \\
k_{1}x_{n1}+k_{2}x_{n2}+\dots+k_{n}x_{nn}=0
\end{cases}
$$
So we want to find a non-zero solution to this homogeneous linear system. That solution does exists if and only if the determinant of the system is NOT zero (solution like ($k_{1},\dots,k_{n}$)$\neq(0,\dots,0)$) 
 


