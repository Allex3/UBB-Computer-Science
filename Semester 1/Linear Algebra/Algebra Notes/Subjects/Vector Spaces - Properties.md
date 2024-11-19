#### Theorem 2.1.4
>[!important] Let $V$ be a vector space over $K$. Then $\forall k,k'\in K$ and $\forall v, v'\in V$ we have:
>$$
>\begin{align}
>&(i)k\cdot 0=0\cdot v=0\\
>&(ii)k(-v)=(-k)v=-kv\\
>&(iii)k(v-v')=kv-kv'\\
>&(iv)(k-k')v=kv-k'v
\end{align}
>$$

*Proof:*
*(i)* $k\cdot 0+k\cdot v=k(0+v)=kv \implies k\cdot 0=0$
$0\cdot v+k\cdot v=(0+k)v=kv \implies 0\cdot v=0$
*(ii)* $kv+k(-v)=k(v-v)=k\cdot 0=0 \implies k(-v)=-kv$
$kv + (-k)v=(k-k)v=0\cdot v=0 \implies(-k)v=-kv$
*(iii)* $k(v-v') + kv' = k(v-v'+v')=kv \implies k(v-v')=kv-kv'$
*(iv)* $(k-k')v+k'v =(k-k'+k')v=kv \implies (k-k')v=kv-k'v$

#### Theorem 2.1.5
>[!important] Let $K$ be a vector space over $K$ and let $k\in K$ and $v\in V$. **Then**
>$$kv=0\iff k=0 \text{ or } v=0$$

*Proof:*
$\fbox{=>}$ Assume $kv=0$ and suppose $k\neq0$, then $k$ is invertible in the field $K$ and we have 
$kv=0\implies kv=k\cdot0\implies k^{-1}(kv)=k^{-1}(k\cdot0) \implies(k^{-1}k)v=(k^{-1}k)\cdot 0 \implies v=0$
$(p\to q)\to(\neg p\to \neg q)$ , so if $k\neq0 \implies v=0,$ then $v\neq0 \implies k=0$, so either k=0 or v=0
$\fbox{<=}$ if $k=0$ or $v=0$, then by [[#Theorem 2.1.4]] (i) it follow that $kv = k\cdot0=0$ or $kv = 0\cdot v=0$
$\square$
