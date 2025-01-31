 
---
## Propositional
---
### Normal forms
- To obtain **DNF**, replace $\to$ by $U\to V\equiv \neg U\lor V$ , $\leftrightarrow$ by $U\leftrightarrow V\equiv(\neg U\lor V)\land(\neg V\lor U)$, apply DeMorgan's laws, apply distributivity laws
- To obtain **CNF** from **DNF**, ==apply distributivity==: $U\land(V\lor Z)\equiv(U\land V)\lor(U\land Z)$
	- Distributivity is the same for $\lor$, literally inversed symbols


### Definition of deduction
- ==direct, syntactic==
- Uses the propositional axiomatic, system, containing **modus tollens, syllogism, resolution, conjunction in conclusions, etc.** Uses as a rule ==modus ponens==. 
- From some hypotheses we "infer" a conclusion through these rules
- ==IMPORTANT== recall permutation of premises, reunion of premises, separation of premises laws. ($\land \implies\to$ is separation, reunion is opposite, and permutation is $\to$ just inversed with U and V)
- ![[T. of deduction consequences (kms).png]]
### Semantic tableau
- ==refutation, semantic==
$\alpha, \beta$ rules
- **TSC**: $\neg U$ has a closed semantic tableau $\iff$ $U$ is a tautology (can result from TSC now that U is a theorem!)
- **Theorem**: $U_{1},\dots,U_{n}\models V\iff U_{1},\dots,U_{n},\neg V$ has a closed semantic tableau (also applied to predicate logic!)


### Resolution
- ==refutation, syntactic==

- **Davis-Putman** procedure:
	- Delete **tautologies**, delete the clauses **subsumed** by other clauses, delete every clause that contains a **pure literal**
	- Just simplifies the set of clauses, after this simplification ANY STRATEGY can be used the same basically, no matter the resolution method
- We need **completeness** to know that if we DO NOT derive the empty clause, THEN the set of clauses is NOT INCONSISTENT = **consistency**
- To prove inconsistency, only **soundness** (to derive the empty clause) is required, and **ALL ==combinations of== STRATEGIES** are sound! But not all are **complete**. That is, not all strategies assure us that "if the formula is inconsistent, we will indeed find the empty clause", so if we don't find the empty clause we can't really say what's going on with it, if it's consistent or inconsistent.
- All **strategies** are **SC**: deletion, level saturation strategy, general, linear 
- **Combinations** SC: general + deletion, level saturation + deletion, level saturation + lock
- **ALWAYS** combine lock with level saturation in order to prove consistency (all ways of deriving the empty clause)
	- if $S_{k}=\emptyset$ , then S is consistent!
- To prove inconsistency, we only need the empty clause, no need to combine any strategy

---
## Predicate
Usually the rules of propositional are part of the rules of predicate first-order logic, so they're extended to a quantifier, variable-constant type logic.
---
### Definition of deduction
- ==direct, syntactic==
- Same rules as in propositional, just added **universal generalization** as a rule, and some new axiom too, no idea, refer to its page rq cuz im done
- We ONLY work with free variables or constants, **bound variables are instantiated using a term (variable or constant) to work with other premises**. Then at the end we use the **universal generalization** again to get to the bounded (**closed formula**) conclusion.
### Semantic tableau
- ==semantic, refutation==

$\alpha, \beta, \gamma, \delta$ rules
Build an interpretation using the open branches of the tableau if it's consistent. The literals on that branch have to be TRUE. For example, if we have $\neg P(a)$ and $Q(b), P(b)$, we can build 2 interpretations, one that has P(a) False, Q(b) and P(b) true, and Q(a) is not here so it can be either true OR false.

**semi-decidability** for predicate logic: If the semantic tableau for a formula is finite, we can decide if its negation is tautology ($\neg U$ closed semantic tableau) or not. But if the tableau is infinite, then we cannot decide upon the validity of $U$. This happens with ANY procedure. If U is valid $Proc$ ends with the corresponding answer, but if $U$ is invalid, $Proc$ ends with the corresponding answer or $Proc$ might never stop.

---

### Resolution
- ==refutation, syntactic==
- ==ALL PROPOSITIONAL LOGIC RULES ARE APPLIED TOO, but to the clausal form clauses!==

- **Prenex normal form:** (Qixi)M, (Qixi)... - prefix, M - matrix, M has NO quantifiers - ADMITTED BY ANY PREDICATE FORMULA: $U^P$
	- -> replaced like in CNF/DNF, variables renamed, apply DeMorgan's infinitary laws, extract the quantifiers in front, then the Matrix is transformed into CNF using DeMorgan's and distributive laws
- **Skolem normal form**: $U^S$ for each existential quantifier for the prefix:
	- For the existential quantifiers on the left side, introduce new constants for all of them and **replace** their **variables** **by** the **constants**
	- If on the left side it has only universal quantifiers, introduce the function $f$ that has the **arity of the number of universal quantifiers on the left of this existential one**, and replace the variable of the existential quantifier with the function of the universal quantifiers
	- These are called **skolem functions/constants**
- **Clausal normal form** ($U^C$): delete the prefix of $U^S$ 
- If the obtained final formula before obtaining PNF has n groups of quantifiers, then we can extract them in an arbitrary order => **n!** prenex normal forms!
- **Skolemization** does not preserve logical equivalence, **BUT IT PRESERVES INCONSISTENCY**
- $V \iff V^p \iff V^S \iff V^C$, after each one "is inconsistent" => 
	- ==IMPORTANT== The set $\{ U_{1}, \dots, U_{n} \}$ is inconsistent $\iff$ the set $\{ U_{1}^\mathbf{C}\dots,U_{n}^C \}$ is inconsistent!

- **Substitution** - assigns $\theta(x_{i}) =t_{i}$ to variables from a domain, and then in a given formula or anything, $x_{i}$ is replaced with $t_{i}$; $x_{i}$ is a **variable**, $t_{i}$ is a **term**
- **Composition of substitutions**:
$\theta=\theta_{1}\theta_{2} = [x_{i}\leftarrow \theta_{2}(t_{i})\text{ }|\text{ }x_{i}\in dom(\theta_{1}), x_{i}\neq \theta_{2}(t_{i})]\cup[y_{j}\leftarrow s_{j}\text{ }|\text{ }y_{j}\in dom(\theta_{2})\backslash dom(\theta_{1})]$
	- $\epsilon$ = empty substitution: $\theta=\theta\epsilon=\epsilon \theta$
	- Associativity, NOT commutativity
- **Most general unifier**
	- A substitution is called a **"unifier"** of $t_{1}$ and $t_{2}$ if $\theta(t_{1})=\theta(t_{2})$, here $\theta(t_{1})$ is called **"common instance"**
	- Unifier of set: $\theta(U_{1})=\dots=\theta(U_{n})$
	- ==most general unifier==: a unifier $\mu$ such that any other unifier $\theta$ can be obtained from $\mu$ by a further substitution $\lambda$, $\theta = \lambda \mu$
	- To compute MGU:
		- The predicate and the number of terms have to be the same! (otherwise NOT unfiiable)
		- $\theta=\epsilon$
		- Find the outermost terms of the literals ($P(t_{1},\dots)$) $t_{1},t_{2}$
		- if they are NOT a variable, or one is a SUBTERM of the other => NOT UNIFIABLE
		- if $t_{1}$ is a variable => $\lambda=[t_{1}<-t_{2}]$, otherwise $\lambda=[t_{2}<-t_{1}]$
		- $\theta=\theta \lambda$
		- END WHEN $\theta(l_{1})=\theta(l_{2}) = $ **common instance**


- **Predicate resolution**:
![[Predicate resolution.png]]
- Two clauses are **clashing** only if there is a general unifier for their resolving literals
- ![[Predicate Resolution Definitions.png]]
- ![[Predicate Resolution Algo.png]]
- ![[Predicate Resolution Theoretical Results.png]]

## Boolean
### Definitions

![[Boolean Algebra Definition.png]]
- There are $2^{2^n}$ Boolean functions of $n$ variables - The set $FB(n)$ of all Boolean functions of $n$ variables defines a Boolean algebra, the only difference being, the neutral alements are $f_{0}=0$ and $f_{2^{2^n}-1}=1$, constant functions
- **Examples**: binary boolean algebra, propositional formulas set defines a boolean algebra, partitions of real numbers with the complementary set
![[Boolean functions of 2 variables.png]]

![[Boolean operations.png]]

#### Negation:
![[Boolean notation negation.png]]


### Canonical forms
![[Boolean canonical forms.png]]
- Clearly, when f of the $\alpha$'s is 0 in DNF, then the cube will be FALSE, as 0 is part of the conjunction, so we can give it up, it doesn't add anything to the disjunction:
- In the same manner, when f of the $\alpha$'s is 1 in CNF, the clause is always TRUE, and it doesn't add ANYTHING to the conjunction:
![[Canonical boolean forms T.png]]

- And so as we can see, if the values of the f are 1 in the DCF, it doesn't add anything to the conjunction so only the variables remain, same thing in , 0 doesn't add anything to the conjunction


### Minterms and maxterms


![[Minmaxterm def.png]]

- There are $2^n$ minterms/maxterms
	- $m_{i}$ is the i'th minterm, the exponents of the variables $(\alpha's)$ are the $i$ in binary form:
		- n=2 $m_{2}$ = $m_{10} = x^1\land y^0 = x\land \overline{y}$ 
	- Same thing with maxterms, just disjunction: n=2, $M_{2}=M_{10}=x^{\overline{1}}\lor y^{\overline{0}}=\overline{x}\lor y$
![[Minterm Maxterm properties.png]]
- To construct DCF, the 1 values of the function give the specific minterm, and the function is the disjunction of the minterms, 1 only when the function has the variables for one of the minterms, at the same exponents so it will be 1
- To construct CCF, the 0 values of the function give the maxterms, and the function is the conjunction of the maxterms, so it's 0 only when one of the maxterms is 0, when the varaibles will be the opposites of the exponents, otherwise the maxterm, which is a conjunction, will be 1.
![[How to CCF DCF.png]]


### DCF Simplification general

- **Support of f**: Vectors where the function is 1
![[Support.png]]

- **Neighboring monoms**, **factorization** of monoms
![[Neighboring monoms.png]]

![[Maximal and central monoms.png]]
- **maximal monoms** = monoms of f such that they're support is highest
- **central monoms** = maximal monoms of f for whose support is not $\subseteq$ in the support of the disjunction of the other central monoms of f. Basically, **central monoms give unique values for the function, otherwise we wouldn't need to use them, the values (support) would be included in the DCF of the other maximal monoms.**

#### Simplification algorithm
![[Simplification algo informally.png]]
![[Boolean simplification algorithm.png]]

This simplification can be done in three ways:
### Veitch-Karnaugh diagram
- ==graphical method==

![[Veitch Karnaugh diagrams.png]]

![[Veitch-Karnaugh explained.png]]
![[Veitch example.png]]
- Simplfiies **2 from 3** = 2 variables from the 3 possible are simplified by the double factorization
- i-factorization = $2^i$ monoms are factorized, simplifying i variables, remaining only $n-i$ variables from a function of n variables

![[Vertch-Karnaugh method.png]]


#### First case of the algo: M(f) = C(f)
![[Veitch ex 1.png]]

#### Second case of the algo: M(f) $\neq$ C(f)
![[Veitch ex 2.png]]
- ==reminder== The **central monoms** are the maximal monoms that contain **AT LEAST** a monom **CIRCLED ONLY ONCE** in their factorization. That's why in the above example, max3 and max4 are NOT central, they **ONLY CONTAIN MONOMS CIRCLED MORE THAN ONCE**, there is ==no monom covered only by them for it to be central and give uniquely the value of the function==
- Then, how to select $h_{i}$? We see that the remaining maximal monoms have only a monom that is not covered by the central ones, $m_{10}$, so WE ONLY CARE ABOUT IT, so either take max3 or max4, no matter which
#### Third case of the algo: C(f) = $\emptyset$
![[Veitch ex 3.1.png]]
![[Veitch ex 3.2.png]]
- We need the maximal monoms that cover all the minterms in the function, in a minimal way: So Try to find if we can do that with 1, 2 , 3 maxterms, we see we can't with 1 or 2 so we NEED 3, and we know all the simplified forms have 3 maximal monoms, because 3 is the minimum needed, more is repeating, and less is not covering all

#### Karnaugh example
![[Karnaugh example.png]]

### Quine's method
- ==reminder== the simplification process is THE SAME, only the method changes but once we get to the required maximal/central monoms we use the same process.

Explained:
-  have $f$ in DCF
- get $S_{f}$ in ascending/descending order with respect to the number of 1's in the tuples
- Construct a tableau: the header = name of variables, then each row has the minterms expressed by their variables' exponents, so the binary of the index of the minterm $m_{3}=m_{011}$, that is the minterm corresponding to the (0, 1, 1) tuple of the support of f (==recall== that when a minterm is 1 then the function is 1, and m3 is 1 at (0, 1 1) exactly)
- Make groups of minterms delimited by a horizontal line, each minterm in a group has the same number of 1's in its representation
- A double horizontal line marks the end of the function's representation and begins the computation of maximal monoms
- only two neighboring groups can have neighboring (adjacent) monoms (logical, like group 1 has n zeroes, group 3 has n-2 zeroes, they already differ)
- Add new rows representing the factorization of neighboring monoms from two adjacent groups, "-" will represent the variable that is eliminated. Since we factorised $m$ and $m'$, mark their corresponding rows $\checkmark$ saying that they are NOT maximal monoms (already covered by a better disjunction of monoms)
- The monoms obtained by factorization of two neighbor groups will form a new group, which in turn will be used itself in the same manner
- The symbol "-" cannot be combined with anything else, but we CAN "double factorize" two neighboring monoms with "-" in the same places, basically knowing we have a disjunction of four neighboring monoms at that point, with the first disjunctions getting rid of a variable, then the next getting rid of another at this step. So basically, we **cannot** factorise neighbouring monoms from **two different factorization stages**. Like simple and double, it has to be groups in the same stage: representation, simple, double, triple, etc.
- A double horizontal line will represent the end of a simpel, double, triple, etc. factorization
- A triple horizontal line signified the end of the factorization process
- --------
- $M(f)$ is the set of all maximal monoms corresponding to all unmarked rows from the tableau (they are maximal, can't be factorized with anything anymore)
- To obtain $C(f)$ we need a new tableau with maximal monoms on columns,  and minterms of the function on rows.
- A cell in this table is marked with "$*$" if the **minterm of the row** is used **to obtain the maximal monom of the column**. A maximal monom is a **central monom if there is  a $*$ on its column, which is ==unique== on a row** (basically saying, the ONLY column (maximal monom) that covers that minterm (row) IS that specific one, because it's unique on a row, the minterm IS NOT covered by any other maximal monom). The disjunction of all the central monoms, if $M(f)=C(f)$ is the DCF Simplified form of the function (**first case**)
- The minterms which aren't covered by $C(f)$ will be covered by the **a minimum number of unused maximal monoms which cover them**, in all possible ways ! (**second + third** cases)

#### Quine example 1 (First case: $M(f)=C(f)$)
![[Quine ex 1.1.png]]![[Quine ex 1.2.png]]

#### Quine example 2 (Third case: $C(f)=\emptyset$)

![[Quine ex 2.1.png]]
![[Quine ex 2.2.png]]
![[Quine ex 2.3.png]]

#### Example 3 (Second case: $C(f)\neq M(f)\neq \emptyset$)
![[Quine ex 3.1.png]]
![[Quine ex 3.2.png]]
![[Images/Quine ex 3.3.png]]
![[Quine ex 3.3 1.png]]

### Moisil's simplification method (have mercy)

Explained:
- $f$ is transformed into DCF
- $M(f)$ is obtained using a previous method (Quine, Veitch-Karnaugh diagrams)
- Moisil's method uses **propositional logic** to obtain the simplified forms from the set of maximal monoms

![[Moisil ex 1.1.png]]![[Moisil ex 1.2.png]]
- $p_{1}\lor p_{2}\equiv T$ because $m_{0}$ **HAS TO BE** in the function, and it's covered by only those two maximal monoms, so **AT LEAST** one of them has to be part of the simplifed form of the functions, OTHERWISE $m_{0}$ will not be covered. Because we don't know which one will be best to add, we say it's "either one of them: OR"

![[Moisil ex 1.3.png]]
![[Moisil ex 1.4.png]]


### Logic circuits

#### NAND

![[NAND.png]]
#### Comparator of two binary digits
![[Comparator.png]]

#### Full adder
![[Adder 1.png]]
![[Adder 2.png]]
![[Adder drawing.png]]

##### n-bit adder
![[n-bit adder.png]]

#### Full subtractor

![[Subtractor 1.png]]![[Substractor 2.png]]

##### n-bit subtractor
![[n-bit subtractor.png]]

#### Encoder

![[Encoder 1.png]]
![[Encoder 2.png]]

#### Decoder
![[Decoder 1.png]]
#### 7 Segments circuit
![[7 Segments 1.png]]
- ==KNOW THIS COMBINATIONAL LOGIC CIRCUIT BROO==
![[7 Segments 2.png]]

#### Transforming a function into NAND form
![[S3 Nand implementation 1.png]]
![[NAND impl 2.png]]

#### Transforming a function into NOR form

![[NOR impl 1.png]]
![[NOR impl 2.png]]
