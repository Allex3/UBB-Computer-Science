- **Present the corresp. memory layout for following data segment (i.e its structure & corresp memory vals, assuming offset = 0) →**
- **justify (in context) the reason for obtaining each of the stored vals**
- If there are data elems or source lines which u consider syntactically incorrect, motivate n explain ur decision & ignore further those vals or lines in providing the requestedmem. layout

---

### 01.27.2023

```nasm
segment data
x dw -128, 128h
y dw 256 >>2, 256h-256 (cred)
z db z,$-z
p dd {$-y} * (x - $}, y-x
a dw $-$$, $$-a
h dw 11b,11-b,11h, 11-h 
b dw xy-2-18, x-y+z-18 
c db 2-b, b-2
d dw 257,-255
e dd 12345h, '12345'
f dw x+1, [x+1]
g times 4 db 'dw'
h db 11b, 11h,-11,-11b 
k dw 1+2b+3h+a, a+Oah 
m dd Oah+Obh, a+b
times 2 dd 1234h, 5678h


Memory's layout is in little endian, meaning that the order of the bytes of a number is from lowest to highest, but the bits order does not change.
dw = define word = 2 bytes before ',', dd = define double word = 4 bytes before ','

-128 is represented as 0x80, 1000 0000, which is -128 in signed interpretation
Converted to a word is FF80h
x: 80 FF 28 01, so the words -128=0x80, 128h=0x128 = 01 28 = 28 01 in little endian

256 = 1 00000000, the bits shifted right two times, so 01000000 = 0040h = 64
256h-256 = 256h - 0100h = 0156h, so a word is two bytes, so 01 56
y: 40 00 56 01 in little-endian

The third line gives a syntax error, because offsets can only be represented on double words, or on words half of the offset, but on byte it gives an OBJ error

p: wtf - syntax error

$ is the current offset, the number of bytes generated inside a segment, a location counter. $$ is the base address of the current segment, so $-$$ evaluates the number of bytes generated until now in the current segment
$-$$ = 8 since only 4 words = 8 bytes were generated
$$-a is pointer airthmetic, subtractic a pointer from a pointer IS ALLOWED, so no syntax error! $$ = 0 , a = 8, since there are 8 bytes generated until a , and the segment starts at offset 0, so $$-a = -8 in a word, so FF F8 
a: 08 00 F8 FF

11-b is not an acceptable pointer arithmetic operation, you cannot subtract a pointer from a constant. Only pointer from a pointer, or constant from a pointer, or adding a constant to a pointer. So h is syntax error 

xy is not defined => syntax error

c is syntax error, 2-b is not acceptable pointer arithemtic

257 = 01 01 , -255 fits only on a word = FF 01
d: 01 01 01 FF

When you have a character string it is inversed and put into memory byte by byte, but since e is a define dword, 4 bytes each are put in this inversed order, so '12345' = 1 2 3 4 5 0 0 0, 3 more 0 bytes have to be reserved, because at '5' we HAVE to create another dword, cannot create only a byte
e: 45 23 01 00 '1' '2' '3' '4' '5' 00 00 00

f: syntaxe rror, tf is dwx

times 4 = the allocation is executed 4 times, so "db 'dw'" is executed 4 times
Bytes put in inverse order in memory, one byte allocated each, so we allocate oen for 'd' and one for 'w' and stop there, do this 4 times
g: 'd' 'w' 'd' 'w' 'd' 'w' 'd' 'w' 

11b = 3h, 11h = 11h as a byte, -11 = 11110101 = F5, -11b = -3 = FD
h: 03 11 F5 FD

2b is syntax error, not a binary digit

a+b is syntax error, pointer addition NOT allowed, on the same line, so even if the first allocation is valid, it will not happen, it will cause a syntax error and the program will NOT run

an offset label is not specified but the bytes are generated, just cannot be accessed i guess...



```

### 01.28.2022

```nasm
a1 dd '0abcdefh',0abcdefh
a2 dw '0abcdefh',3 | 6
a3 dw $-a2,a2-a1
a4 db 129>>1,-129 << 1
a5 dw a2-a4, ~(a2-a4)
a6 dd $+a2-1,!a2
a7 dd 256h^256,256256h
a8 dd ($-a7) + (a9-$) , -256
a9 dw -255, -128
a10 times 4 dw 128h,-128
a11 db a3
a12 dw a3

string is put into memory in reverse order, it is checked in the table of constants. a double word allocates 4 bytes, so even if the number of string characters is not a multiple of 4, after the last cahracter is allocated, 0 bytes will be allocated until the dword is finished
a1: '0' 'a' 'b' 'c' 'd' 'e' 'f' 'h' EF CD AB 00

a1 has 12 bytes, a2 has 10 bytes
011 | 110 = 111 = 00 07
a2: '0' 'a' 'b' 'c' 'd' 'e' 'f' 'h' 07 00

$-a2 = 22-12 , a2 begins at offset 12 = 10 = Ah
a2-a1 is subtraction of pointers, allowed, and can be put into a word and dword, but not in a byte, a1 is at offset 0, a1 has 12 bytes, so a2-a1=12-0=12=0xC
a3: 00 0A 00 0C

129>>1 = 10000001>>1 = 01000000 = 40
-129 << 1 = 1111 1111 0111 1111 << 1 = 1111 1110 1111 1110, take the byte from this
= 1111 1110 = FE
a4: 40 FE

a2 is at offset 12, a3 at offset 22, a4 is at offset a3+4=26

a2-a4 is allowed, a2 = 12, a4 = 26
12-26 = -14, a word, so = FF F2
~(a2-a4) = ~(a2-a4) = ~(-14) = ~(11111111 11110010) = 00 0D
a5: F2 FF 0D 00

a5 is at offset a4+2 = 26+2 = 28, a7 = 28+4 = 32 

$+a2 is adding two pointers, not allowed!
a6: $ is the location counter, so an offset, adding to offset a2, SYNTAX ERROR

256h^256 = 00000256h ^ 0000000100h = 00000356h 
256h^ 256 = 00000010 01010110 ^ 00000001 00000000 = 00000011 01010110 = 356h
a7: 56 03 00 00 56 62 25 00 

a8 syntax error, a9 undefined

-255 = two-s complement of 255 as a word, so 65536 - 255 = 65281 in binary
so FF 01
-128 = 80 FF in word repres.
a9: 01 FF 80 FF

a10: 28 01 80 FF 28 01 80 FF 28 01 80 FF 28 01 80 FF

a11 is syntax error, because an offset can only be 16 bits, legacy of 16 bits asm, when part of it is cut off ,or 32 bits, but CANNOT handle 8 bit relocations

a12 puts half of the offset of a3, the lower half, at offset a12
here a3 is at offset 22, so 22 = 00 16h
a12: 16 00


```