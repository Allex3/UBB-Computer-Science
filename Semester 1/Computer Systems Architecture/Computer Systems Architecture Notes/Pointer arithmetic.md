___

>[!warning] YOU CANNOT subtract a FAR address from an OFFSET


>[!warning] Dereferencing is **NOT** a pointer arithmetic operation

Any operation which allows the programmer to parse the memory (bytes) in such a way that an address was indeed reached is acceptable: (DO NOT divide/multiply addresses)
1. **Addition** of a **constant** to a **pointer**: `a[7] = *(a+7)`
	p+ 9 -> POINTER !
2. **Subtraction** of a constant from a pointer: `a[7] = *(a-7) = *(a+(-7))`
	p-9 -> POINTER
3. **Subtracting** two pointers: `$-a in NASM (currend address offset - starting location of a is the size of a array` (q-p)
	q-p -> SCALAR !
>[!important] Only those **3 operations are allowed!** Others do not make sense

In `i = i+1` , `i = ADDRESS (LHS L-value); i+1 = CONTENTS (RHS R-value)`

Every program is just a succession of attribution instructions
