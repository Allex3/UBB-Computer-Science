

## Subjects 1 - THEORY

- WE NEED BOTH OF/CF BECAUSE the addition/subtraction is the SAME WAY in unsigned/signed, from the POV of base 2 they are the same! Because the processor/assembler does not know what we want to do next. It prepares both situations, and we as programmers decide what we do.
---
One type of subjects can be :
- Instructions that depend on the signed or unsigned representations (factor in the sign): We have to specify before an instruction what WE want to do: IDIV/IMUL to specify we want signed representation - that's also a reason why DIV/IDIV/MUL/IMUL Has only one explicit operand

Conversions (classification of conversions): byte->word->dword->qword signed/unsigned

---
Overflow concept analysis

---

Subprograms/Functions/Procedures:
CDECL: 
- cod de apel = call code
- cod de intrare = enter code
- cod de iesire = exit code
- ??? variabil la CDECL

???? FIX la STDCALL 
- The caller has the responsibility to clear the stack

for exam: MULTI-MODULE ASM+ASM CAN BE 

---
The roles of  REGISTERS: where do we use EAX, ECX, etc. ? They are general purpose but are defined for something officially
- EAX is used as the return value of a function call

---


## Subject 2 : Memory layout usually

- You have a data segment.
- What is each line generating?
- Ignore syntax errors in generating but state them! And what is the cause of the syntax error WHY
- why do i live
- Memory layout : LITTLE-ENDIAN 
- Constant strings: in such cases put 'a' in the memory layout
- How does it organize? BASE 16 implicitly.
- Can ask for both unsigned/signed values : check last seminar; 

>[!important] Representation vs interpretation ! Related to two's complement
>- In base 2 we have representation, base 16 is the same, just base 2 compressed, so base 16 is also REPRESENTATION, hence there is NO signed/unsigned interpretation, they are just bits representation, but INTERPRETATIONS decide signs
>- Cu semn/fara semn (SIGNED/UNSIGNED) APPLIES ONLY TO BASE 10 INTERPRETATION!!!

So, there are 4 ways to represent the value in signed/unsigned interpretations ???

## Subject 3 - ASM Source code

```nasm 
v dw 24357
----------
add ebx, v
sub ebx, 6
mov eax, ebx


a) Este o secventa corecta sintactic? If yes, confirm this si explicati de ce.
a) Is it a correctly syntactic sequence? If no, explain why and what element gives this error or incorrectness - DO NOT HAVE TO ARGUMENT WHY

b) In masura in care este o secventa corecta sintactic scrieti o singura insructiune care sa aiba acelasi efect asupra registrului EAX ca secventa data. - ECHIVALNETA asupra registrului EAX, cu tot cred...

a) correct
b) ebx = ebx + v - 6, v = offset
	that is what we want to transfer in eax... but how
lea eax, [ebx+v-6] AMAZINGGG
We care more about the fact that it can be represented as a fine address specification formula
```

```nasm
v dw 24357
------
add ebx, v
sub ebx, 6
mov eax, [ebx]

a) correct
b) ebx = ebx+v-6, [ebx] = [ebx+v-6]
so mov eax, [ebx+v-6]
```

```nasm
v dw 24357
------
add ebx, [v]
sub ebx, 6
mov eax, ebx

ebx = ebx + [v] - 6, cannot do that as we already have an address specification formula there

If he asks about in this calculation IT IS IMPSOSIBLE
THE ASF IS THE ONLY WAY TO COMBINE MORE INSTRUCTIONS INTO ONE, but here we use it already... so it is impossible
```


`mov eax, 7` <- NO NEED FOR EXPLANATION BUT WE CAN EXPLAIN IT IN 69 ROWS
`mov eax, [ebx+v-6]` - explain it - uses ASF 2 AM formula to calculate the short address in data segment we go to that is given by the base EBX, the constants v which is an offset value and 6 which is an immediate value.  There is no index here and no scale. The base registers can only be .... and here it is EBX so it is allowed. The only pointer arithmetic operations allowed are subtraction of pointers or addition/subtraction by a constant, NOT addition of pointers. This instruction is syntactically correct.