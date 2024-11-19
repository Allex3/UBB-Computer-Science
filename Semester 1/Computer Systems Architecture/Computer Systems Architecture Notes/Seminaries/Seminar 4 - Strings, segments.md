
`MOVSB <- MOV ES:[EDI], DS:[ESI]`
`ES[EDI] = [ES<<4+EDI]` = `[0<<4+edi]` = `[EDI]`

because, **on 32 bits**: `DS, ES, CS, SS = 0 (the offset, they have a OS selector)`
but, on 16 bits: `MOV [di], [si] => es:[di] <- ds:[si] => [es<<4+di]<-[ds<<4+si]`
you could move in `ds or es registers, the address at which the segment starts, to change its base, but in 64bits it starts at 0`


#### Exam question
>[!question] Instructions equivalent with these

```nasm
sub esp, 4
mov edi, esp ; esp-4
stosd ; [edi] = EAX, which is at the top of the stack (edi=esp)

=> PUSH EAX (which subtracts 4 (a dword) from ESP and puts EAX there)
```