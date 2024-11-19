
---

#### Theorem 1.6.2

>[!important] Let $(G, \cdot)\text{ be a group and let }H\subseteq G$. **Then**
>$$
>H\leq G \iff \begin{cases} 
H\neq \emptyset \text{ }(1 \in H) \\ 
\forall x, y \in H, x\cdot y \in H \\
\forall x \in H, x^{-1}\in H
\end{cases}
>$$

**Proof:**
$\fbox{=>}$ 
Suppose $H$ is a subgroup of $G$. Thus $H$ has an identity element $1'$, so $x\cdot1' = 1'\cdot x = x, \forall x \in H$.
But if $1'\cdot x =x/\cdot x^{-1} \iff1'=1\in H$. Therefore, the subgroup $H$ must contain the identity element of the group $G$, and so $H\neq \emptyset.$
$H$ is a group and $H \subseteq G$, we know that $H$ is a stable subset of $(G, \cdot)$, thus $\forall x, y\in H: x\cdot y\in H$
$H$ is a group. Let $x \in H$ and denote by $x'$ its inverse in the group $(H, \cdot)$. So $x\cdot x'=x'\cdot x=1$. Multiplying with $x^{-1}$, we have $x'=x^{-1} \in H$. So $\forall x \in H, x^{-1}\in H$
$\fbox{<=}$
Suppose that the three conditions hold. Then, from the second condition we know that $H$ is a stable subset of $(G, \cdot)$. 
Associativity holds on $H$ too if it holds on $G$.
Let $x \in H \neq \emptyset \implies \exists x^{-1}\in H$ and $1=x\cdot x^{-1}\in H$ (because $H$ is a stable subset). Hence 1 is the identity element of H  
From $\forall x\in H, x^{-1}\in H$, so we know every element in $H$ has an inverse in $H$.
Hence, $(H, \cdot)$ is a group.
$\square$


#### Theorem 1.6.3
>[!important] Let $(G, \cdot)$ be a group and let $H \subseteq G$. **Then**
>$$
>H\leq G \iff \begin{cases} 
H \neq \emptyset \text{ }(1\in H) \\
\forall x, y\in H,\text{ } x\cdot y^{-1}\in H
\end{cases}
>$$

**Proof:**
By the definition and [[#Theorem 1.6.2]]
$\fbox{=>}$ $H$ is subgroup of $G$, so $H$ is a stable subset of $(G, \cdot)$ and the inverse of every element is in $H$. Thus, $\forall x, y \in H,$  $x\cdot y^{-1}\in H$, and clearly $H\neq \emptyset$ because of [[#Theorem 1.6.2]]
$\fbox{<=}$ Suppose that the conditions hold. From the second condition we know that H is a stable subset of $(G, \cdot)$. Clearly $H$ is associative 
Take $x=y$ in the second condition: $\forall y\in H,\;y\cdot y^{-1}=1\in H$, so H has an identity element, and we see that for any number in $H$, there is an inverse, because $\forall y\in H,\;y\cdot y^{-1}=1$
Thus, $(H, \cdot)$ is a group.
$\square$


---

#### Theorem 1.6.8 
>[!important] Let $(R, +,\cdot)$ be a ring and let $A\subseteq R$. **Then**
>$$
>A \text{ is a subring of }R \iff \begin{cases}
A\neq \emptyset\; (0\in A) \\
\forall x, y\in A,\;x-y\in A \\
\forall x,y\in A,\;x\cdot y\in A
\end{cases}
>$$

**Proof:**
$\fbox{=>}$ Assume that $A$ is a subring or $R$. Thus, $(A, +, \cdot)$ is a ring, so $(A, +)$ is a group, so $0\in A \implies A\neq \emptyset$. But, because $A$ is a subring, it is a stable subset of $(R, +)$ and $(R, +)$ is a group, hence $(A, +)$ is a subgroup of $(R, +)$. By [[#Theorem 1.6.3]] we have $\forall x, y \in A,\;x-y\in A$
Since $A$ is a subring, $A$ is a stable subset of $(R, \cdot)$ too, so $\forall x\cdot y\in A,\;x\cdot y\in A$
$\fbox{<=}$  Assume the conditions. From the fact that $A\subseteq R$ and the first two conditions: $A\neq \emptyset$ and $\forall x, y\in a\;x-y\in A$ so by [[#Theorem 1.6.3]] we have that $(A, +)$ is a subgroup of $(R, +)$, and, consequently, a stable subset of $(R, +)$. The last condition tells us that $A$ is a stable subset of $(R, \cdot)$. Associativity holds in $A\subseteq R$, hence $(A, \cdot)$ is a semigroup. Since $(A, +)$ is a group and $(A, \cdot)$ is a semigroup, and $A$ is a stable subset of $(R, +)$ and of $(R, \cdot)$, we have that $(A, +, \cdot)$ is a ring, and even more, a subring of $(R, +, \cdot)$.
$\square$
---
#### Theorem 1.6.9
>[!important] Let $(K, +, \cdot)$ be a field and let $A\subseteq K$. **Then**
>$$
>A \text{ is a subfield of }K \iff \begin{cases}
|A|\geq 2\;(0, 1 \in A) \\
\forall x, y\in A,\;x-y\in A \\
\forall x,y\in A\text{ with }y\neq 0,\;x\cdot y^{-1}\in A
\end{cases}
>$$

*Proof*:
$\fbox{=>}$ Assume that A is a subfield of $(K, +, ·)$. Since $(A, +)$ is a group, we have $0 ∈ A \neq ∅.$ Since $(A, +, ·)$ is a field, $(A^{*} , ·)$ is a group, and thus $1 ∈ A,$ and consequently $|A| \geq 2$. But A is a stable subset of $(K, +)$ and $(A, +)$ is group, hence $A$ is a subgroup of $(K, +)$. By [[#Theorem 1.6.3]] we have $x − y ∈ A, ∀x, y ∈ A$. Since $(A^{*} , ·)$ is a subgroup of the group $(K^{*} , ·)$, by [[#Theorem 1.6.2]] we have $y^{-1} ∈ A,$ $∀y ∈ A^{*}$ . But A is also a stable subset of (K, ·), hence ∀x, y ∈ A with $y \neq 0$, we have $x · y^{-1} ∈ A$.
$\fbox{<=}$  Assume that the three conditions hold. By the first two of them and [[#Theorem 1.6.3]], $(A, +)$ is a subgroup of $(K, +)$ and consequently a stable subset of $(K, +)$.
Now let $x, y \in A$. If $y=0,$ then $x\cdot y=0\in A$ by the first condition. If $y\neq0$, then $x\cdot y=x\cdot(y^{-1})^{-1}\in A$ by the last condition. Thus, $A$ is a stable subset of $(K, \cdot)$. 
From the first and third conditions, $(A^{*}, \cdot)$ is a subgroup of the group $(K^{*}, \cdot)$ by [[#Theorem 1.6.3]] so we have all the conditions for $A$ to be a subfield of $K$.

