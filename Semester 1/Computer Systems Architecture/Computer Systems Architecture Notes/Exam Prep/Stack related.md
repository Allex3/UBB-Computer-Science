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

pula
```

What happens at `push v?`
```
v d?
a d?
b d?

...
push v ; v -> 32 bits offset (constant offset determinable at assembly time)
		; offset of address of a variable

push [v] ; [v] -> source opearands, contents of offset v
			; put 4 bytes (maximum) in the stack at ESP, ESP+=4

push dword[v] ; 4 bytes from address v on the stack
push word[v] ; 2 bytes from address v on the stack
push byte[v] ; SYNTAX ERROR, CANNOT PUT 8 BITS, FUCK KNOWS WHY
```



---
>[!question] ESP = 0019FF74
>
`PUSH ESP` , puts 4 bytes on the stack
a) ESP = 0019FF74 
b) ESP = ESP-4 = 0019FF70 - go down the stack first
c) `[ESP]` = 0019FF74 YES, so 0019FF74 at position 0019FF70 - put the value there second
so we first move 4 positions to the left, and put the `ESP` element that was on the stack there

`POP dword [ESP]` ; `[ESP] = 7741FA29`
	a) `ESP = 0019FF74, [0019FF74] = 7741FA29`
	b) ESP = ESP+4 = 0019FF78 - move the stack up a dword
	c) `[ESP] = 7741FA29`



