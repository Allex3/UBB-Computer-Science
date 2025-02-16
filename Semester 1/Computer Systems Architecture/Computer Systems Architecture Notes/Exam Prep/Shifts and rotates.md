
---

>[!question] Write a sequence of instructions that multiplies `EDX:EAX` by 4!

```nasm
xor edx, edx
mov dl, 0fh
; "shl EDX:EAX, 2"    ; EDX: 0....01111, EAX: 
shl eax, 1
rcl edx, 1
shl eax, 1
rcl edx, 1
```