
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










