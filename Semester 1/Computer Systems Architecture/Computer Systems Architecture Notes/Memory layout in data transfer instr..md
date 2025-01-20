
kms

---
noooo

---
>[!important] When initializing a memory area with string type constants (sizeof > 1) the data type used in definition (dw, dd, dq) does only the reservation of the **REQUIRED** space, ==the "filling" order of that memory area being the order in which the characters appear in the string constant==:

```nasm
a6 dd '123', '345', 'abcd' ; 3 doublewords are defined, their contents being
						   ; 31 32 33 00 | 33 34 35 00 | 61 62 63 64
							; 31 = 1, 32 =2, ... ARE ASCII CODES OF THE CHARS
a6 dd '1234' ; 31 32 33 34 ; EXACTLY ONE DWORD

a6 dd '12345' ; 31 32 33 34 | 35 00 00 00

a71 dw '23', '45' : 32 33 | 34 35 - 2 words, 1 dword
a72 dw '2345' ; - 2 words - 32 33 | 34 35
a73 dw '23456' ; 3 words - 32 33 | 34 35 | 36 00

mov eax, [a73] ;EAX = 35 34 33 32
mov ah, [a73] ; AH = 32
mov ax, [a73] ; AX = 33 32
THE SAME HAPPENS FOR a71 and a72
```
=='...'="..." in NASM==, but in **C**, '...' != "...", char vs array of chars/string
in C, ASCIIZ implies that `'x' = ASCII code for x (1 byte) - char`
but `"x" = 'x','\0' (2 bytes) - string` (like when u send "abc" as parameter it automatically puts '\0' there)

---
```nasm
a8 dw '1', '2', '3' - 3 words, because comma - 31 00 32 00 33 00
a9 dw '123' - 2 words - 31 32 | 33 00
```

#### The following definitions provide the same memory configuration
```nasm
dd 'ninechars' ;dword string constant - 9 bytes, so 3 dwords: 4, 4, 1+3, 3 which are 00
dd 'nine', 'char', 's' ; 3 doublewords
db 'ninechars', 0, 0, 0 ; filling memory area by bytes sequence, because of string constant convention the order is the same as in DWORD , and the last 00's from the dword that's required

n i n e c h a r s 00 00 00 , all bytes
```

## A character constant with more than one byte will be arranged (where?) with little-endian order in mind

if you code
`mov eax, 'abcd' ; (EAX = 0x64636261)` ==OPPOSITE OF MEMORY, USING BIG-ENDIAN==

>[!important] In memory `'abcd'` is taken in opposite of little-endian => 61 62 63 64 instead of 64 63 62 61, and in 'REGISTER', it is also the opposite of its normal order: 64 63 62 61 instead of 61 62 63 64 as should be the order of 'abcd' normally.

then **the constant generated is not 0x61626364, but 0x64636261** so that if you were then to store the value into memory, it would read abcd (little-endian, because EAX is big-endian)

==So EAX put into memory 64636261 => 61626364 in little-endian, SO IT IS EQUIVALENT TO THE ABOVE DEFITINION OF DEFINING STRINGS IN MEMORY! IN NORMAL ORDER==

>[!note] The main idea of this definition is that THE CHARACTER REPRESENTATION VALUE associated to a string constant 'abcd' is in fact 'dcba' (this being the STORAGE format in the CONSTANTS TABLE): ex: eax, etc.

`       table of constants` = HASMAP SMTH LIKE THAT
`'abcd' -----------------> 'dcba` WHEN PUT IN REGISTERS!
`a dd 'abcd' = mov ptr DS:[a], 34333231, in memory = 31323334`

==Table of constants 'converts' 'abcd' to 'dcba' to use it like this, in memory or registers==
**THAT IS WHY `mov eax, 'abcd' = 'dcba' **
AND WHY `a dd 'abcd' is in memory 'abcd' instead of 'dcba' little-endian`
	IT ACTS LIKE `a dd 34333231(dcba) which in memory is 31323334 = 'abcd'` **
	

`mov dword[a], '2345' -> mov dword ptr DS:[401000], 35343332`
BUT if a register would store them in opposite order, that is 
`mov EAX, 'abcd' = dcba => mov dword[a], EAX => [a] = 32333435 in memory, good order as if we defined it in DS from the start!`


