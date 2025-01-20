
## First test

---
*1)* We need examples prepared for the theory. At least half of the examples should be tweaked by us at least a bit and not just copied from him
*2)*

- Here are the next lines of code, what is their output
```nasm
x dw -129, 10+1000b+1000b
-128 = 0x80 , in word is FF80, FF80-1 = FF7F = -129


EXPLAIN LITTLE ENDIAN! The bytes are reversed in memory, the first byte is the smallest

in memory :
0: 7F FF
2: 10+1000b+1000b = 1010b+1000b+1000b = 11010b a word = 1A 00 

y dw 1001h >> 1001b, 128h & 128
1001h>>1001b => 0001 0000 0000 0001 >> 9 = 0000 0000 0000 1000 = 8
4: 08 00 - little endian :3
6: 00 00: 128h & 128 = 01 28h & 128 = 01 28h & 00 80h = 00 20h & 0080h = 0

z dw z, $$-z = 0-8=-8 (z is at offset 8) = F8FF
8: lower part ofo ffset of z: 1000
10: F8FF = -8

; data: 0x401000 => 0x1000 - lower part of offset

w dd x+y-z = 0+4-8 = -4 = FF FF FF FC
12: FC FF FF FF 
; (x-$$) + (y-$$) = x+y

e dd abcdefh, 'abcdefh'
abcdefh -> ERROR, should have started with 0 to be hexa
'abcdefh' -> 'a' 'b' 'c' 'd' | 'e' 'f' 'h' 00 <- RESERVE DWORD

; (if it was like e dd 'a' it has to reserve a dword: 'a' 00 00 00)

g times 3 dw 'db' -> 'd' 'b' 'd' 'b' 'd' 'b'

```


## WHAT IS A DIRECTIVE
- fuck knows

**3)**

```nasm
mov al, -1
mov bl, -128
add al, bl

al = -1 = 0xFF -> unsigned 255, signed -1
bl = -128 = 0x80 -> unsigned 128, signed -128

FROM ADDITION: 
1111 1111+
1000 0000
0111 1111, = 0x7F => unsigned 127, signed 127, that's the issue
CF=1 carry outside
OF = 1 because the sign bits are 1 (negative numbers in signed) but the result has the sign bit 0

MUL
mov al, 1 
mov bl, 1255 => AX = 510 => OF=CF=1 ; fits , that's how MUL works
1255 = 4E7 => BL = E7 = 231
mul bl

DIV => CF, OF UNDEFINED
```

Which instruction does the same thing as another:
```nasm
XOR EAX, EAX => EAX = 0
LEA EBX, [ESI] => EBX = ESI
ES XLAT => AL <- DS:[EBX+AL] <=> AL <- DS:[ESI] <=> LODSB because AL = 0
! it is NOT es:[EBX+AL], ES in front of XLAT is USELESS

ES LODSB => ES:[ESI]
```

```nasm
LEA ESI, [ESP+4]
LEA EDI, [ESI-8]
PUSH ESP
-----
SS LODSD => EAX <- SS:[ESI]
SS STOSD => EAX -> SS:[EDI]

push dword [ESP+4]

```

**4)** First describe the algorithm in half a page


