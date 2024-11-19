
---
#### Definition of Subspaces
>[!info] Let $V$ be a vector space over $K$ and let $S\subseteq V$. Then $S$ is a subspace of $V$ if:
>$$
>\begin{align}
&(i)S\neq \emptyset \\
&(ii)\forall v_{1},v_{2}\in S,\;v_{1}+v_{2}\in S \\
&(iii)\forall k\in K,\;\forall v\in V,\;kv\in S
\end{align}
>$$

#### Theorem 2.2.3
>[!important] Let $V$ be a vector space over $K$ and let $S\subseteq V$. Then
>$$
>S\leq V \iff \begin{cases}
S\neq \emptyset\;(0\in S) \\
\forall k_{1},k_{2}\in K,\;\forall v_{1},v_{2}\in S,\;k_{1}v_{1}+k_{2}v_{2}\in S
\end{cases}
>$$

*Proof:*
$\fbox{=>}$ Take k=0 in the definition $\implies 0\cdot v=0\in S\neq \emptyset$
Now, let $k_{1},k_{2}\in K$ and $v_{1},v_{2}\in V$. Then $v_{1}k_{1},v_{2}k_{2}\in S \implies k_{1}v_{1}+k_{2}v_{2}\in S$
$\fbox{<=}$ Choose $k_{1}=k_{2}=1 \implies \forall v_{1},v_{2}\in S:v_{1}+v_{2}\in S$
Choose $k_{2}=0\implies \forall k\in K,\;kv_{1}+0v_{2}=kv_{1}\in S$
Use the [[#Definition of Subspaces]] (also $S\neq \emptyset$ clearly) to get that $S\leq V$
