## Data

- Cannot declare only 1 bit (minimum 1 byte)
- byte = 8 bits (a db 5, db = declare byte)
- word = 16 bits (dw - declare word)
- double word = 32 bits (dd)
- quad word = 64 bits (qd)
- All the variables are declared in the **Data segment** like so:
	- it begins with "segment data use32 class=data":
	- a db 5 -> 05 in memory
	- a dw 0x12AB, 012ABh (0 in front so it's not ASCII (0AB, etc.)) -> AB 12 AB 12 in mem.
	- c db 5, 3, 1, 2 (in memory: 05 03 01 02)
	- ten equ 10 (doesn't occupy space in memory, it just replaces ten with 10)
### Reserving Data
- resb 2 <=> x resw 1 (it reserves 2 bytes in memory, the variable is empty tho)
- res w, res d, res q, etc.

## Memory
- intel/amd x86 uses **little-endian layout**, the smallest byte is stored first, so 12ABCD is stored as CD AB 12, while others can use big-endian, so it's stored as it's read, the highest byte first (12 AB CD)
- So the above declarations would be in memory: 05 AB 12 AB 12 05 03 01 02
## Examples of moving values
- `MOV EAX, byte[a]` -> does NOT work (the size of the operands ISN'T the same, EAX has 4 bytes)
- `MOV EAX, [a]` -> takes one DWORD from a, so 4 bytes (so from, the above memory, we'll have in EAX = 0xAB12AB05, so how it is when written/read, so in EAX values are not stored in little endian, but in the normal way, taken from the memory in the reverse order, because there they are stored in little endian)
- if we want to move `byte[a]` in EAX, we need to move it in a 1 byte register:
	- `MOV BL, byte[a]` or `MOV BL, [a]` words, since it takes only 1 byte from there anyway

## Accessing memory 
```asm
mov destination, source
mov al, byte[b] -> moves in al a byte from the address b, that is the variable b if b is one byte
mov al, byte[a] (1 byte of variable a (1 byte from the address a))
mov al, byte[a+1] (value going only one byte at address a+1)
mov al, byte[6] (value at address 6 (cred?))
```

## Registers

EAX, EBC, ECX, EDX, ESI, EDI, EBP, ESP, EIP, EFLAGS -> all have 32 bits (4 bytes), variables used by the CPU, in the CPU
- Everything has to move through one of those, **you can't work with two external variables**, you have to get it to one of those first
	- to `mov byte[c], byte[a]`:
		- `mov ah, byte[a]`
		- `mov byte[c], ah`
	- **Exception:**
		- `mov byte[a], 1` - immediate values can be moved at a memory location
- 3 **types of operands** in ASM:
	- register: EAX, EBX, etc.
	- memory operand: `a, byte[a]`, etc
	- immediate value: `mov al, 10` or `mov al, ten` where we defined `ten equ 10`
## Instructions
- ##### ADD
	- `ADD destination, source <=> dest=dest+source` 
	- `ADD byte[a], 10 -> a=a+10`
- ##### SUB
	- `SUB dest, source <=> dest=dest-source`
	- `SUB EAX, 1 <=> EAX=EAX-1`
- Example: Bigger addition
```asm
a db 5
b dw 0x100
-------------
mov al, byte[a]
add al, byte[b] ;the addition is bigger than a byte, so we should use AX for the addition:

mov al, byte[a]
mov bx, word[b]

WRONG EXAMPLE:
add bx, al doesn't work, because bx and al have different sizes

GOOD EXAMPLE:
mov ah, 0 ;make the higher half of AX 0, so only AL is present in it
; so we can add bx to ax, as if we are adding al to bx, but good sizes this time
add ax, bx (basically )

```
- Example: negative addition:
```asm
here moving 0 to ah wouldn't be ideal:

5 = 0000 0101
-5 = 1111 1011 (two's complement) =  0xFB in AL
but 0xFB can be 251 too, and will be stored as 00 FB in AX when unsigned
but when it is -5, it is stored as FF FB in AX, so we extend the sign bit to 
AH to make it -5 and make calculations iwth AX being negative too
cbw -> signed extension from AL->AX
```

