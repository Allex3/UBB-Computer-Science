 Input: non-zero natural numbers k and n with k ≤ n  Output: 1. the number of k-dimensional subspaces of the vector space Z n 2 over Z2 2. a basis of each such subspace (for 1 ≤ k ≤ n ≤ 6)

`k = 2, n = 3` 
There are $2^n$ vectors in $Z_{2}^n$ , so in $Z_{2}^3$ there are $2^3=8$ vectors!
Choose any non-zero vector first, so $2^n$-1
Choose any non-zero vector that is not a lin. comb. of the previous: $2^n-2$

So $6\cdot 7=42$ lists of (v1, v2) , but it is equal to (v2, v1)
So $\frac{42}{2} = 21$ combinations of two vectors from $Z_{2}^3$

Algorithm: 
- Store in memory BITMASKS for the vectors from $Z_{2}^n$ , because they only have 0s and 1s it can be an integer value. Ex: `(0, 1, 0, 1) = 0101 = 5`, but now, we have 0s to its left, how do we know how many to take? From `n`, so take only one zero to its left. If we have, for example, `(1, 0, 0, 0) = 1000 = 15` 
	- We take the components of the vector from the `(n-1)'th` bit of the bitmask, always!
- **Addition in $Z_{2}$** is equivalent to the **bit XOR** operation of the **bitmasks representing the vectors**.
	- `(1, 0, 1, 1) + (0, 0, 1, 0) = 1011^0010 = 1001 = (1, 0, 0, 1)`
- To 