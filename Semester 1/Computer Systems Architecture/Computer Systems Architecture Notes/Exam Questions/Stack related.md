[[Stack|How does the stack function with 4 byte values]]
>[!question] What does the following code do (in the stack)?

```nasm
a dw 5 ; 05 00
b dw 6 ; 06 00
c dd 112233h ; 33 22 11 00

push ecx ; stack = 00 11 22 33 
push ax  ; add to stack 00 05 
stack:        00 05
		00 11 22 33
pop eax ; eax = 00 05 22 33

```