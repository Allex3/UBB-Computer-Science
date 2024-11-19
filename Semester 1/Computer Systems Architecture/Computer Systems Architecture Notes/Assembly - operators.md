### Operators

**Operators** - used for combining, comparing, modifying and analysing the operands. Some operators work with integer constants, others with stored integer values and others with both types of operands.

>[!important] operators vs instructions
>Operators perform computations only with constant **SCALAR** values computable **at assembly time** (scalar values = constant immediate values), with the exception of adding and/or subtracting a constant from a pointer (which will issue a pointer data type) and with the exception of the offset computation formula (which supports the '+' operator!) -> **POINTER ARITHMATIC is EXCLUDED from this scalar rule!** (b+7, a-2, etc.) and also the **OFFSET SPECIFICATION FORMULA is EXCLUDED from this scalar rule** (`[a+2]`, only **+**)
>Instructions perform computations with values that may remain unknown until run time.
>

**Example:** (+) performs addition at assembly time and the ADD instruction performs addition during run time.
`mov eax, ebx+2 SYNTAX ERROR, so have to do add ebx, 2`

Operators used by the x86 assembly language expressions in NASM!:
In order of PRIORITY DESCENDING:
- `-` - two's complement negation
- `~` - NOT (one's complement) - **inverse all bits**
- `!` - logical negation
- `*` - multiplication
- `<<` - Bitwise shift left `0xFE<<4`
- `>>` - Bitwise shift right `0xFE>>4`
- `&` - binary AND - 3
- `^` - binary XOR - 2
- `|` - binary OR - 1

`5|6+7&8=5|(6+7)&8=5|13&8=5|8=13=0Dh!!`

**Examples**
`~11110000b: 00001111b`
`!0 = 1,if  n!=0, !n=0`


### Bitwise operators and instructions

- `XOR` - **for COMPLEMENTING the values of some bits:0
	- `x XOR 0 = x`
	- `x XOR x = 0`
	- `x XOR 1 = ~x`
	- `x XOR ~x = 1`

`! and ~`:
	`mov eax, ![a] SYNTAX ERROR`
	`mov 
	i give up`

>[!question] **EXAM QUESTION:** Please provide minimum 15 DIFFERENT WAYS of initializing with 0 the contents of a register! 

```nasm
mov eax, 0 
xor eax, eax
and eax, 0

```