### ADC, SBB: CF example + EDX:EAX quad addition 
**ADC**
- The value of the carry flag (CF) is added to the sum of the two operands
- Both operands should have the same type: byte, word or doubleword.
- While both operand can be registers, at most one operand can be a memory location.
**SBB**
- The value of the carry flag (CF) is substracted from (dest - source)
- Both operands should have the same type: byte, word or doubleword.
- While both operand can be registers, at most one operand can be a memory location.
```nasm
 a dq 1122334455667788h +
b dq 0AABBCCDDEEFF0011h
r resq 1

memory : 8877665544332211 1100FF... (a b in inverse order of bytes)

mov eax, [a] ;eax = 55667788h
mov edx, [a+4]
mov ebx, [b]
mov ecx, [b+4]
add eax, ebx
adc edx, ecx (+CF), if carry flag = 1 use it
	(EDX = EDX+ECX+CF)
sbb a, b ; a=a-b-CF

mov [r], eax ;first 4 bytes of the result in eax, low part
mov [r+4], edx ;after the 4 bytes, put the other 4 bytes, high bytes
; since in memory it's oppoiste order, put first the low part
; and since it is 4 bytes, put the other 4 at a distance of 4

```

### IMUL & IDIV
MUL, DIV - positive, unsigned multiplication/division
IMUL, IDIV - negative, or signed mul/div
The operations are the same, but the signed one are performed differently

FF * FD > 0, two negative numbers if imul, or two positive if mul, sign bit set

```nasm
a = 2, al=2
b = -3
imul bl => -3 => FD*2 ?
```

a - byte
b - word
```nasm
mov al, [a]
mov ah, 0 
mul [b] ;AX * b
```
a - byte
b - word ? a * b
### Signed conversion instructions, conversions
```nasm
I  a = 0000 0011 = 03h => AX = 00 03h: AH = 00, AL = a
II a = 1000 0011 =? AX = 1111 1111 1000 0011: AH=FF, AL = a
```
For this, we have **CBW** *ONLY IN THE SIGNED INTERPRETATION* -> `AL => AX`
```nasm
cbw ; if AL=01110111b then AX ← 00000000 01110111b
    ; if AL=11110111b then AX ← 11111111 11110111b
```
Similarly, we have:
	**CWD** -> AX => DX:AX in the same manner as above in signed interpretation
```nasm
cwd ; if AX=00110011 11001100b then DX:AX ← 00000000 00000000 00110011 11001100b
    ; if AX=10110011 11001100b then DX:AX ← 11111111 11111111 10110011 11001100b
```
**CWDE** -> AX => EAX
**CDQ** -> EAX => EDX:EAX

HW: 9+ the 9+19 = 28 , 8 exercises from LAB 3

### Unsigned conversion
- There are no instructions for conversions in the unsigned representation!
- In assembly language, the unsigned conversions are done by putting 0 in the high byte, word or doubleword:
```nasm
mov AH,0 ; for converting AL → AX
mov DX,0 ; for converting AX → DX:AX
mov EDX,0 ; for converting EAX → EDX:EAX
```