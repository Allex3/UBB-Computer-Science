[[Location Counter]]

---
#### NOT ASKED AT WRITTEN EXAM
```nasm
segment data

a db 1, 2, 3, 4 ; 01 02 03 04 
lg db $-a ; 04
lg0 db $-data ; SYNTAX ERROR - expression is not simple or relocatable
lg1 db a-data ; SYNTAX ERROR - expression is not simpel or relocatable

in TASM, MASM offset(segment_name) = 0, so a-data = a 
BUT in NASM, offset(data) = 00401000 !!, so here a-data does not work, trated as FAR address
```

`lg2 dw data-a ; the assembler allows it but we obtain a LINKING ERROR`

---

`db a-$ ; = -5 = FB`
```nasm
c equ a-$ ; 0-6=-6=FA
d equ a-$ ;same
e db a-$ ;same
```

```
x dw x ; 07 10 !!! (from 00401007)
x db x ; SYNTAX ERROR, offset is only WORD/DWORD, CAN NOT TRUNCATE A BYTE FROM IT
x1 dw x1 ; x1 = offset(x1) 09 00 at assembly time and 09 10 in the end...
```

```nasm
db lg-a ; 04
db a-le ; -4=FC
db [$-a] ; EXPRESSION SYNTAX ERROR - a memory contents is not a constant computable at assembly time
db [lg-a] ; EXPRESSION SYNTAX ERROR - a memory contnets is not a constant computable at assembly time (even if lg-a is a constant, [lg-a] IS NOT, IT HAS TO BE COMPUTED!)
```
 
```nasm
lg1 EQU lg1 ; lg1=0 (BUG NASM!!!) - it considers that an unitialized constant = 0
lg1 EQU lg1-a ; lg1=0: offset(a) = 0, but if we put smth before a in data segment, offset(a) !=0 and we will obtain a SYNTAX ERROR: RECURSIVE EQUs, macro abuse"
```

```nasm
a dd a-start ; SYNTAX ERROR - EXPRESSION NOT SIMPLE OR RELOCATABLE AT ASSEMBLY TIME
(because a is defined here, start is defined SOMEWHERE ELSE, in another segment = far address)

a dd start-a ; OK - start defined somwhere else, a defined here! - POINTER DATA TYPE
; even if start is in another segment...

dd start-start1 ; OK! because they are 2 labels defined in the same segment!! RESULT WILL BE A SCALAR DTYPE

```

>[!important] 
>altundeva (alt segment) - aici ; OK!
aici - altundeva (alt segment) ; SYNTAX ERROR, in alt segment :O


```nasm
mov ah, lg1 ; AH = 0
mov bh, c ; BH = -6 = FA

mov ch, lg ; OBJ format can handle only 16 or 32 byte relocation, CH is 8 byte
mov ch, lg-a ; CH=04
mov ch, [lg-a] ; mov byte ptr DS:[4] - VIOLATION ERROR

mov ch, lg-a ; CX = 4
mov cx, [lg-a] ; mov WORD ptr DS:[4] - VIOLATION ERROR
```

```nasm
mov cx, $-a ; INVALID OPERAND TYPE!!! ($ - defined here (CS), a - somewhere else (DS))
mov cx, $$-a ; INVALDI OPERAND TYPE ($$ from code segm and a from data segm!)

mov cx, a-$ ; OK!!! (a - defined somewhere else, $ - defined here)
mov cx, $-start ; OK!!!
```


#### ????
```nasm
mov ah, a+b ; NO syntax error!!! BUT... its NO pointer arithemtic, no pointers addition ; it is SCALAR addition - a+b = (a-$$) + (b-$$)

mov ax, b+a ; AX = (b-$$) + (a-$$) - SCALARS ADDITION (somewhere else - here)
```

```nasm
mov ax, [a+b] ; INVALUD EFFECTIVE ADDRESS !!!! - this REALLY represents pointer addition which is FORBIDDEN! (because of offset specification formula)
```

```nasm
var1 dd a+b ; SYNTAX ERROR - expression not simple or relocatable
(so NASM does not allow "a+b" to appear in a DATA DEFINITION intiialization, but ONLY as an INSTRUCTION OPERAND like above)!
```

## Expressions of type et1-et2  (where et1 and et2 are labels - either code or data) are syntactically accepted by NASM:

- If both of them are defined in the same segment
- If et1 belongs to a different segment from the one in which the expression appears and et2 is defined in this latter one. In such a case, the expression is accepted and the data type associated to the expression et1-et2 is POINTER and NOT SCALAR (numeric constant) as in the case of an expression composed of labels belonging to the same segment (So **somewhere else - here OK!**, but **HERE - SOMEWHERE ELSE NO!**)
==Subtracting offset ... plm==

