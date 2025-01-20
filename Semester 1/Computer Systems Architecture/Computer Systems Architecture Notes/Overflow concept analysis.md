>[!info] At the level of the assembly language an overflow is a situation (condition) which expresses the fact that the result of the LPO either:
>- did not fit the space for it (ex: unsigned addition, 8bits+8bits=9bits, CF=1)
>- does not belong to the admissible representation interval for that size
>- the operation is a mathematical nonsense in that particular interpretation (signed or unsigned) (**ex**: in signed: pos+pos = negative and vice versa because of the rules of the signed interpretation)



### Divide overflow
When the result does NOT fit on the representation
	**3000/2** = 1500, does NOT fit on a byte, so DIVISION BY ZERO ERROR - TREATED AS INFINITY



