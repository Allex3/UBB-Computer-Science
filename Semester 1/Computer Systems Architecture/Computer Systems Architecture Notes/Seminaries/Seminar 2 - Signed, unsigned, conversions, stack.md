[[Lab 3 - Flags and signed instructions|Related to lab 3]]
## Conversions
#### Unsigned addition
```nasm
a db 5
b dw 0x320

mov al, byte[a]
mov bx, word[b]
mov ah, 0 (otherwise [??][05] in AX)
add ax, bx
```
What if signed addition?
### Signed /vs/ unsigned interpretation
`a db -5`  -> 1111 1011, -5 only if signed
otherwise 251 in unsigned, **the CPU treats them the same**, we decide what we use **signed or unsigned**
if `AL = 0xFB` byte
	to make it a word, put 00 in AH: `AX = 00 FB`, this is the **unsigned interpretation**
	to make it a word in **signed interpretation**, fill the high part of what we convert it to with 1s instead of 0s: `AX = FF FB` = -5 in signed, `mov AH, 0xFF`, because the sign bit is 1

#### Signed conversions
>[!INFO] *C*onvert *B*yte/*W*ord/*D*oubleword to *W*ord/*D*oubleword/*Q*uadword in **signed** interpretation, so **fill the higher part with 1** **IF the sign bit is 1**, but if the **sign bit is 0, fill it with 0**
- CBW => AL -> AX `if AL = FB, put FF in AH: AX = FF FB`
- CWD => AX -> DX:AX `basically, put FF FF in DX, fill it with 1`, but if we were to have `AX = 0101 1011 for example, the sign bit is 0, so put 0 in DX, so DX:AX = 00 00 05 0B `
- CWDE => AX -> EAX (CWD Extended)
- CDQ => EAX -> EDX:EAX, same principles as above
>[!WARNING] Only use them when we have negative numbers or a result **could be negative**, otherwise if we know everything is unsigned, just put 0 in the higher parts as above
#### Unsigned conversions 
Their equivalent in signed conversions:
- AL -> AX: `mov AH, 0`
- AX -> DX:AX : `mov DX, 0`
- AX -> EAX : `mov EAX, 0 ; mov AX, [var]`
- EAX -> EDX:EAX: `mov EDX, 0`

## Mul/div vs imul/idiv

#### MUL/IMUL: 
```nasm
MUL op => unsigned
MUL BL => AX = AL*BL
MUL BX => DX:AX = AX*BX
MUL EBX => EDX:EAX = EBX*EAX

IMUL BL ;BL=FB=-5, interprets BL as signed
```

#### DIV/IDIV:
```nasm
DIV op => unsigned
DIV BL ;AX/BL - res AL, rem AH
DIV BX; DX:AX/bx - res AX, rem DX
DIV EBX; EDX:EAX/EBX - res EAX, rem EDX

IDIV op => interprets op as signed
```

>[!INFO] Use `IMUL reg/mem or IDIV reg/mem` if you want the assembler to **interpret reg/mem as signed**, otherwise the instructions behave the same way

 >[!QUESTION] Question: How many operands does `DIV BL` have? 4:
	 BL is explicit
	 AX/BL -> quotient AL, rem AH, so  3 implicit ones

>[!WARNING] **Division error!** 
```nasm
mov ax, 0x1000
mov bl, 1
div bl ; AX/BL - res = AL, AL too small for 0x1000, so division error
```
**Correct way to do it:**
```nasm
mov dx, 0
mov ax, 0x1000
mov bl, 1 -|
			<=> mov bx, 1 -> better way
mov bh, 0 -| 

div bx ;DX:AX/BX - AX = 0x1000, DX = 0, now it works we doubled the size of the operand by putting it in BX instead of BL, and the dividend in DX:AX so we perform DX:AX/BX instead of AX/BL, thus allocating to the result double the memory too
```

When doing signed multiplication or division, **don't forget to convert them using the instructions,** either putting 0 or 1 in the higher part of the registers we convert it to, depending on the sign bit
```nasm
mov ax, 0x8000
CWD ; use this because we will use IDIV (AX -> converted into DX:AX signed, because here AX in signed interpretation the sign bit is set, so it will be different than just setting 0 in DX
; this lets the assembler decide if to put 0 or 1 in DX, depending on the sign bit of AX, so you don't do it manually
mov bx, 1
IDIV bx ; DX:AX/BX
```

##### How to add a * b + c
###### Addition: Convert DX:AX -> EAX using **the stack**
```nasm
a dw 32
b dw 15
c dd 32456

; a*b+c
mov ax, word[a]
mov bx, word[b];
mul bx ;dx:ax = a*b

;convert dx:ax into eax:
push dx
push ax
pop eax ; DX:AX -> EAX

add eax, dword[c]
```
###### a, b = word, c = dword, use DX:AX
```
c:
32 10
__ __
32 01
__ __
DX AX

first AX = AX+c10, then DX = DX+c32+carry

add AX, [c] ;first two bytes
adc DX, [c+2] ;last two bytes of c
```

###### a, b = word, C = qword
>[!INFO] EAX -> DX:AX
```nasm
push EAX
pop AX
pop DX
```

```nasm
a dw 5
b dw 25
c dq 345231897

;a*b+c
mov ax, word[a]
mov bx, word[b]
mov bx ;dx:ax = a*b
push dx
push ax
pop eax ;eax=a*b

mov ebx, dword[c]
mov ecx, dword[c+4] ;ecx = higher part of c, higher 4 bytes
; ecx:ebx = c
add ebx, eax ; add the lower part of c with a*b which is a dword
adc ecx, 0 ; <=> mov edx, 0 then adc ecx, edx
;to add the possible carry, ONLY in the unsigned, in signed below, but use EDX
```

**signed** difference:
```nasm
everything the same, but:
...
IMUL bx ;dx:ax = a*b
...
cdq ; EAX -> EDX:EAX
add ebx, eax
adc ecx, edx ; could be the same as unsigned if it puts only 0s, but if not, we have to make sure it's fine

```
>[!INFO] **SBB  <=> ADC**, add, adc, sub, sbb work the same in signed and unsigned
```
FF FF|FF FB
00 00|03 20
00 00|03 1B , CF = 1 for first half
```

## [[Stack related]]

