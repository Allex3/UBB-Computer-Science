- **EFLAGS** & **ALU** - 17 October
- **Two's complement - when OF, when CF, signed and unsigned** - 24 October
- **Memory Segments** (and BIU?) how do they function - 31 October?
- **Offset specification formula** and it in respect to the memory segments - 7 November
- Types of errors and when they happen, depending on instructions and types - 14/21 November lecture
- Concepts of **overflowing**, **two's complement** - 28 November lecture

`db 300, "F"+3` -> 'F'+3 = 49
WARNING: 300 exceeds bounds, on a db only `[-128, 255]`

`a4 dw a2+1, 'bc'` -> CORRECT, `a2+1` is pointer arithmetic, and `a2` is determinable at assembly time, so it works!

`a11 db [a2]` -> SYNTAX ERROR

`a6 TIMES 4 db '13'` <=> `a61 TIMES 4 db '1', '3'` <=> `a62 TIMES 4 dw '13'`

`a7 db a2` <- **SYNTAX ERROR** - OBJ format can only handle 16/32 bits offset
`a8 dw a2` ; 08 10
`a9 dd a2` ; correct offset: 08 10 40 00
`a10 dq a2` ; 08 10 40 00 00 00 00 00 -> correct


>[!question] Example of instructions with both operands from memory!
>`push mem`, `pop mem` :O, BUT THERE IS NO ISNTRUCTION WITH BOTH EXPLICIT OPERANDS FROM MEMORY 



