
**PUSHING**
```
v d?
a d?
b d?

...
push v ; v -> 32 bits offset (constant offset determinable at assembly time)
		; offset of address of a variable

push [v] ; SYNTAX ERROR -> OPERATION SIZE NOT SPECIFIED

push dword[v] ; 4 bytes from address v on the stack
push word[v] ; 2 bytes from address v on the stack
push byte[v] ; SYNTAX ERROR, CANNOT PUT 8 BITS, because the ESP can ONLY be decremented by 2, 4 or 8 bytes
```

`mov eax, v` <- put the constant offset v in eax
`mov eax, [v]` <- the size of eax decides how many bytes will be taken from `[v]`, here 4 bytes
	in OLLYDBG: `mov eax, dword ptr [DS:401008]`, so `v` is replaced by the constant it represents

`push [eax]` <- **SYNTAX ERROR**, OPERATION SIZE NOT SPECIFIED!!
`push eax` <- put the contents of EAX into the stack, 4 bytes,` ESP-=4`

`push 15` <- `push 0x0000000F`, 4 bytes, the default of the stack

>[!important] So, if we push a constant to the stack, the ==assembler== decides to allocate it 32 bits ON THE STACK, as if it is a DWORD !

**POPPING**
`pop [v]` <- **SYNTAX ERROR - op size not specified, has to be** `word[v], dword[v]`
`pop v`  <- `2=3`, makes no sense => **SYNTAX ERROR**, v - CONSTANT OF POINTER TYPE

>[!important] v, a **constant** is ALWAYS an **RHS**, and never a **LHS**, we CANNOT assign to it

`pop dword b` <- **SYNTAX ERROR**, b is a **R-value**
`pop [eax]` <- **SYNTAX ERROR, OP. SIZE NOT SPECIFIED**, in push and pop both
`pop word[eax] or dword[eax]` works!

`pop 15` <- **SYNTAX ERROR**, 15 is **R-value**, 15 - CONSTANT OF IMMEDIATE TYPE
`pop [15]` <- **SYNTAX ERROR**, op. size not specified
`pop dword[15]` <- no syntax error, but **memory violation error

>[!info] Even if `push/pop dword/word[eax]` works from a syntactic POV, it will give a **RUNTIME ERROR, MEMORY VIOLATION ERROR**

---

`mov [v], 0` <- **SYNTAX ERORR**, op. size not specified
`mov byte[v], 0` <- CORRECT, put a byte from 0 at address v, only it's "smallest" part if the source would be bigger
`mov [v], byte 0` <- CORRECT, put a byte from 0 starting at address v

**DIVISION/MULT**
`div [b]` <= **SYNTAX ERROR**, have to specify `byte/word/dword[b]`
`imul [v+2]` <- **SYNTAX ERROR**, have to specify size `byte/word/dword[v+2]`
- BUT, `[v+2]` is computed correctly according to the 2 am formula

`mov a, b` <- **SYNTAX ERROR**, a is **R-Value**, but here it is **L-value**
`mov [a], b` <- **SYNTAX ERROR**, op. size not specified
`mov word/dword[a], b`  <- works, but b is on 32 bits, so should use DWORD, so it doesn't truncate
`mov a, [b]` ; **SYNTAX ERROR** - a is R-value
`mov [a], [b]` <- **SYNTAX ERROR** - **CANNOT** have both operators from memory, ever
>[!important] We can **NEVER** have **two explicit operands from memory**, ==but== if one or both of them are **IMPLICIT, IT WORKS**
>e.g. `push word[v]`, `pop word[v]` - source/dest: `[v]` from memory, then dest/source: `[SS:ESP]`, so still from memory, but IMPLICIT
>`movsb` 

>[!info] Reminder: a value at an offset and the offset itself can be 32 bits, but it can also be 16 bits, from backwards compatibility, the same way as the stack also supports PUSHES on 16 and 32 bits too


---
```nasm
mov ah, b - **syntax error**: an offset CANNOT be a byte, but it can be 16 or 32 bits on 32 bits architecture
mov ax, b - OK: 2 bytes from b
mov eax, b - OK: 4 bytes from b
Works because they specify the size AX a word, at EAX a dword, like word AX, dword EAX
```

---
**MORE MUL/DIV**
`mul v` <- **SYNTAX ERROR** INVALID COMBINATION OF OPCODE AND OPERANDS
because `mul reg/mem`, implicit = `AL/AX/DX:AX` -> `AX/DX:AX/EDX:EAX`
`mul word v` <- **SYNTAX ERROR**, not a valid comb. for `MUL` instruction
`mul [v]` <- **SYNTAX ERROR**, op. size not specified
`mul dword[v]` <- WORKS, RESULT IN `EDX:EAX`
`mul eax` <- WORKS, result in `EDX:EAX`, `EAX*EAX`

`mul [eax]` <- **SYNTAX ERROR**
`mul byte[eax]` <- WORKS
`mul 15` <- **SYNTAX ERROR**, invalid syntax of  `MUL, 15 const`

---

### NASM VS TASM

## Revision !

`pop byte[v]` <- DOES NOT WORK, **CANNOT POP A BYTE, STACK ORGANISED ON 16 OR 32 BITS**
`pop qword[v]` <- **SYNTAX ERROR**: instr. not supported in 32 bits mode
