- `PUSH` - push on the stack
	- **ESP** is the address of the last element pushed onto the stack <=> ESP-=4
	- **PUSH** has **1** ==implicit== operand: PUSH (s) <- source
- `POP d` - pop on the stack
	- **POP d** has **1 ==implicit: source==** and 1 explicit: destination

#### XCHG d, s- interchanges the contents of these two operands
- `<d> <-> <s> ; s, d have to be L-Values` ?? can both be from memory?
#### XLAT
- `AL<- <DS:[EBX-AL]> or AL <- segment:[EBX+AL]`

When is `MOV EAX, EFLAGS` valid ? when EFLAGS is offset defined in DS ??

#### PUSHF
`pushf`
`pop eax`
Now you can manipulate the EFLAGS in EAX 😈😈😈😈
... after giving EFLAGS emotional trauma, we killed its spirit
`push eax`
`popf`

#### LEA `general_reg` `contents of a memory_operand`

LOAD EFFECTIVE ADDRESS - transfers the offset of the mem operand into the destination register
`general_reg <- offset(mem_operand)`

`mov ebx, [eax+4*ebp+v-7]` - 2 AM FORMULA 
`mov ebx, eax+4 ..` - SYNTAX ERROR

`LEA ebx, [eax+4*ebp+v-7]` <=> `mov ebx, eax+4*ebp+v-7`, if it would work

## MOVZX d, s
- Loads in **d (REGISTER!),** which must be of size larger than **s (reg/mem),** the **UNSIGNED contents of s (zero extension)**

## MOVSX d, s
- Loads in **d** (**REGISTER!**), which must be of size larger than **s (reg/mem)** the **SIGNED contents of s (sign extension)**

```nasm
mov ah, 0c8h
movzx edx, ah ; EDX = 000000c8h
movsx ebx, ah ; EDX = FFFFFFC8h
movsx ax, [v] ; AX is two bytes, so take from v a byte and loads in ax the signed
content of the byte at [v], so extend the byte to a word in a SIGNED manner!
				; mov ax, byte ptr DS:[00401020]

movzx eax, [v] ; SYNTAX ERROR
			should be byte, word

movsx eax, dword[v] - SYNTAX ERROR
```

## [[Shifts and rotates]]

## [[Memory layout in data transfer instr.]]
