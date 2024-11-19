
---
**Direction Flag** - set the direction of parsing the array
	DF = 1 -> descending order: STD -> SeT Direction flag
	DF = 0 -> ascending order: CLD -> CLear Direction flag

### Instructions for data transfer
```nasm
LODSB - The byte from the address <DS:ESI> is loaded in AL  <br>If DF=0 then inc(ESI), else dec(ESI)
LODSW, LODSD, the exact same, but load DS:ESI in AX, respectivley EAX
and ESI+=2 or ESI+=4

STOSB - Store AL into the byte from the address <ES:EDI>  
If DF=0 then inc(EDI), else dec(EDI)
STOSW and STOSD are the same, but store AX, respectively EAX in ES:EDI

MOVSB - Store the byte from the address <DS:ESI> to the address <ES:EDI>  
If DF=0 then inc(SI), inc(DI), else dec(SI), dec(DI)
MOVSW and MOVSD are the same, but store the word, respectively dword
from DS:ESI into ES:EDI

Example: 
;We have a source string of words. Copy this string into another string. We assume we know the length of this string.
mov ECX, dim_sir ; no of elements in string
mov ESI, sir_sursa ; load offset sir_sursa in ESI
mov EDI, sir_dest ; load offset sir_dest in EDI
CLD
Again:
	LODSW
	STOSW
LOOP Again
```

>[!question] Get the high part of a memory location

```nasm
d dq 0x1122334155667700

mov ESI, d
;THIS 
LODSW ; ax = 7700, esi = esi+2 (little-endian in memory)
LODSW ;ax = 5566, esi=esi+2
;<=> with
LODSD ; eax = 55667700, esi=esi+4

;after
LODSD ; eax = 11223344, esi=esi+4
SHR eax, 16 ; eax = 00 00 11 22 -> only high part in EAX (AX)
; how to see if the lower part of AX = 22 divisible by 8 ?
; DIV byte is AX/AL, not good, because we have 1122 in AX
mov AH, 0
div byte[opt] ;var that's 8; remainder in AH, check if it's 0 it's divisible

CMP AH, 0 ; if AH=0, ZF=1
JE someLabel ; go here if that part divisible by 8 ?? why needed

```

### Instructions for data consultation and comparison
```
SCASB - CMP AL, <ES:EDI>  
If DF=0 Then inc(EDI), Else dec(EDI)
SCASW and SCASD are the same, just comparing AX, respectively EAX, with a word/dword from <ES:EDI>, inc/dec it by 2 or 4

CMPSB - CMP <DS:ESI>, <ES:EDI>  
If DF=0 Then inc(ESI), inc(EDI), Else dec(ESI), dec(EDI)
CMPSW and CMPSD are the same, just comparing words/dwords from ESI/EDI location and inc/dec ESI and EDI by 2 or 4, respectively

Example:
;A sequence of bytes is given. Find the last character "0".
;... all data about the "destination" string is loaded
MOV AL, '0'
MOV ECX, lung_sir
STD
Cont_caut: ;continue search...
	SCASB
	JE Found
LOOP Cont_caut
;...
Found:
	INC EDI;I return to the character found before EDI was decremented 

```
### Prefix instructions for the repetitive execution of a string instruction
`repetitive_prefix string_instruction` $\iff$ 
```nasm
Again:
	string_instruction 
LOOP Again


where repetitive_prefix can be REP, equivalent to REPE (Repeat While Equal), REPZ (Repeat While Zero) - which repeat the execution of instructions SCAS or CMPS until ECX becomes 0 or an unmatch occurs ( => ZF=0)
or it can be REPNE (Repeat While Not Equal) or REPNZ (Repeat While Not Zero) - which repeat the execution of instructions SCAS or CMPS until ECX becomes 0 or when a match occurs ( => ZF=1)
```

>[!important] String instructions **DO NOT CHANGE THE FLAGS** as a result of modifications to ESI, EDI, or ECX; - LODS, STOS, MOVS - do not change any flag, while **SCAS and CMPS change the flags because they compare data.**

