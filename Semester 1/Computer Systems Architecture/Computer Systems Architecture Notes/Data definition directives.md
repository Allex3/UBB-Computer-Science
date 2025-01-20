Data definition directives in NASM are **NOT** data types definition mechanisms!!

---
`a db `
`b dw`
`c dd`

The task of the ==data definition directives (SET OF RULES TO GENERATE CORRECTLY THE BYTES)== (DB, DW, DD, DQ, DT) in NASM is **NOT to specify an associated data type** to the defined variables, but **ONLY TO GENERATE THE CORRESPONDING BYTES** to those memory areas designated by the variables accordingly to the chosen data definition directive and following the little-endian representation order.
So, a is NOT a byte - but only an offset and that is all, a symbol representing the start of a memory area WITHOUT HAVING AN ASSOCIATED DATA TYPE !

`ex: a db 1, 2 is the same as a dw 0x0201`, **WE DECIDE HOW TO USE A VARIABLE, A MEMORY LOCATION, BUT IT DOES NOT HAVE AN ASSOCIATED DATA TYPE**, it only generates bytes, and `a` or `b` is the starting address at which we generate them


## TIMES Directive
`TIMES 32 add eax, edx` <- 32 lines of `add eax, edx` <=> `EAX = EAX + 32*EDX`

---
`a1 db 0, 1, 2, 'xyz' => 00 01 02 'x' 'y' 'z'` in memory
offset(a1) determined at assembly time by NASM = 0, but OllyDBG computes it as `00401000`
