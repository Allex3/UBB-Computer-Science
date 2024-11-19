>[!question] What does the following code do ?

```nasm
a db 1, 2, 3, 4, 5
b db 1, 2, 3, 4, 5
c dw 1, 2, 3, 4, 5
memory: 01 02 03 04 05 01 02 03 04 05 01 00 02 00 03 00 04 00 05 00 $ is here at the end
lenA1 equ $-a ;20
lenA2 equ $-b ; 15
lenA3 equ $-c ; 10
lenB1 equ $-c / 2 ; 5
!!! equ's ytes are constant, like literals, they just get replaced by the value, not stored in memory

d dd 1,2 , 3, 4 ; 4e*4 bytes = 16 bytes added to memory
$-d = 16 #current address (where last element was added - where d starts)
($-d) / 4 = 4
e dq 1, 2 => 2e*8bytes = 16 bytes, 16/8 = 2 elements
($-e)/8 => 2

lenB2 equ $-c-b => $-40k..-40k.. , goes outside of the segment
```

>[!question] How many times is the code executed? 

```nasm

```

>[!question] 

>[!question] 

>[!question] 

>[!question] 

