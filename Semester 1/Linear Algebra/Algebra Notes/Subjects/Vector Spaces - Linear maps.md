#### Theorem 2.4.3 (Characterization of linear maps)
>[!important] Let $V$ and $V'$ be vector space over $K$ and $f:V\to V'$. *Then*
>$$\begin{align}
&f \text{ is a }K-linear\;map \\
&\iff \\
 &f(k_{1}v_{1}+k_{2}v_{2})=k_{1}f(v_{1})+k_{2}f(v_{2}),\forall k_{1},k_{2}\in K,\;\forall v_{1},v_{2}\in V
\end{align}$$

*Proof:*
$\fbox{=>}$ Assume first that $f$ is a $K-linear$ map. Let $v_{1},v_{2}\in V,k_{1},k_{2}\in K$. Then $f(k_{1}v_{1}+k_{2}v_{2})=f(k_{1}v_{1})+f(k_{2}v_{2})=k_{1}f(v_{1})+k_{2}f(v_{2})$
$\fbox{<=}$ Take $k_{1}=k_{2}=1\;and\;let\;v_{1},v_{2}\in V\implies f(v_{1}+v_{2})=f(v_{1})+f(v_{2})$
Take $k_{2}=0$ and let $k\in K\;and\;v\in V$. Then $f(kv+0)=kf(v)+0=kf(v)$
$\square$

#### Theorem 2.4.5
>[!important] Linear map function compositions and inverse
>(i) Let $f:V\to V'$ be an isomorphism of vector spaces over $K$. Then $f^{-1}:V'\to V$ is again an isomorphism of vector spaces over $K$.
>(ii) Let $f:V\to V'$ and $g:V'\to V''$ be $K$ linear-maps. Then $g\circ f:V\to V''$ is a $K$-linear map.

*Proof:*
`(i)` Since $f$ is an isomorphism, $f$ is bijective, hence so is $f^{-1}$.
Now, let $k_{1},k_{2}\in K$ and $v_{1}',v_{2}'\in V'$. We have to prove that 
$$f^{-1}(k_{1}v_{1}'+k_{2}v_{2}')=k_{1}f^{-1}(v_{1}')+k_{2}f^{-1}(v_{2}')$$
Let's denote $v_{1}=f^{-1}(v_{1}')$ and $v_{2}=f^{-1}(v_{2}')$. Then $f(v_{1})=v_{1}'$ and $f(v_{2})=v_{2}'$. 
So $k_{1}v_{1}'+k_{2}v_{2}'=k_{1}f(v_{1})+k_{2}f(v_{2})=f(k_{1}v_{1}+k_{2}v_{2})\implies$
$\implies f^{-1}(k_{1}v_{1}'+k_{2}v_{2}')=k_{1}v_{1}+k_{2}v_{2}=k_{1}f^{-1}(v_{1}')+k_{2}f^{-1}(v_{2}')$$

Hence, $f^{-1}$ is a $K$ linear-map, and it is bijective, therefore $f^{-1}$ is an isomorphism of vector spaces over $K$
`(ii)`  Let $k_{1},k_{2}\in K$ and $v_{1},v_{2}\in V$. We have:
$$
\begin{align}
(g\circ f)(k_{1}v_{1}+k_{2}v_{2}) &= g(f(k_{1}v_{1}+k_{2}v_{2})) \\
&=g(k_{1}f(v_{1})+k_{2}f(v_{2})) \\
&=k_{1}g(f(v_{1}))+k_{2}g(f(v_{2})) \\
&=k_{1}(g\circ f)(v_{1})+k_{2}(g\circ f)(v_{2})
\end{align}
$$
Hence $g\circ f$ satisfies the requirement for a $K$ linear-map, so it is one.
$\square$

#### Theorem 2.4.7 (Kernel and Image  of a K-linear map are subspaces)
>[!important] Let $f:V\to V'$ be a $K-linear\;map$. *Then*:
>$$Kerf\leq V\;and \;\;\mathrm{Im}f\leq V$$

*Proof:*
$Kerf=\{ v\in V|f(v)=0' \}$
$f(0)=0'\implies 0\in Kerf$. Hence $Kerf\neq \emptyset$
Let $v_{1},v_{2}\in Kerf$ and $k_{1},k_{2}\in K$. Now we have:
$f(k_{1}v_{1}+k_{2}v_{2})=k_{1}f(v_{1})+k_{2}f(v_{2})=k_{1}\cdot0'+k_{2}\cdot 0'=0'$, because $v_{1},v_{2}\in Kerf$. 
Thus, $k_{1}v_{1}+k_{2}v_{2}\in Kerf$, so $Kerf\leq V$ 

$\mathrm{Im}f=\{ f(v)\;|v\in V \}$
$f(0)=0'\implies f(0)=0'\in \mathrm{Im}f$. Hence $\mathrm{Im}f\neq \emptyset$
Let $v_{1}',v_{2}'\in V$ and $k_{1},k_{2}\in K$. Indeed, $\exists v_{1},v_{2}\in V$ such that $v_{1}'=f(v_{1}),\;v_{2}'=f(v_{2})$
$k_{1}v_{1}'+k_{2}v_{2}'= k1f(v_{1})+k_{2}f(v_{2})=f(k_{1}v_{1}+k_{2}v_{2})\in \mathrm{Im}f$
Hence, $\mathrm{Im}f\leq V$

