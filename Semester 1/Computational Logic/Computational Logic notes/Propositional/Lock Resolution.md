- **Restriction:** the literals resolved upon must have the lowest indices in their clauses.
- IF we want **CONSISTENCY** **MUST** combine it with the **Level Saturation Strategy** in order to check all the possible ways of deriving. If $S^k = \emptyset$ (the last level of lock resolvents is empty) then the set $S$ is inconsistent
- IF want **INCONSISTENCY**, a strategy is not necessary, but can be helpful.
- **Lock resolution** + **deletion strategy** is NOT complete = even if $S$ is inconsistent, the empty clause **CANNOT** be derived, because there are **TOO MANY RESTRICTIONS**
---

![[Propositional Lock Resolution.png]]

![[Propositional Lock Resolution Example.png]]