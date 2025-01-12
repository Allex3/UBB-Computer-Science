
![[Pasted image 20241104124643.png]]

>[!INFO] How many times does it execute?
>
```nasm
mov ecx, 5
start:
	dec ecx
	loop start - dec ecx
			   - cmp a
			   - jmp label

what happens: ecx = 4, 3, 2, 1, 0, -1 (=FFFFFFFF = 2^32-1), keep decreasing 
```

>[!info] sfaturi de viata de la manuela
>- who hurt her?
>- how to manipulate men
>- how to obtain illegal meds
>- harrass people

### [[Jumps, Loops|Exam questions]]




### Specific jumps

**JMP d** <- d can be a **label, memory address or register**

`JMP loop`

```nasm
mov eax, etich
jmp eax

etich:..
```

#### Segment data
```nasm
segment data
Salt dd Dest ; Salt:= offset Dest
...
segment code:
	...
	jmp [Salt] : NEAR Jump
	: memory variable operand
	
Dest:...

```
[[Jumps, Loops#2.]]


## Loops higher than 127 bytes, also without affecting the flags

```nasm
mov eax, 89
...
JMP Maideparte
	Resd 1000h ; The distance between LOOP and the label Dinnou > 127 bytes so it is not a short jump
	
```

