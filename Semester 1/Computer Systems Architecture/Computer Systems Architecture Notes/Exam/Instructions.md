
`global start` - assembler gives global visibility to the symbol start
`extern` - inform the assembler of foreign symbols, defined somewhere else
`import ... msvcrt.dll` - import some symbols from a library
`bits 32` - assembling for 32 bits architecture
`segment code use32 class=CODE` the program code will be part of a segment called code
`segment data use32 class=DATA` - variables declared here

---
### Data transfer instructions

**PUSH s**, **POP d** - s and d are `doublewords`. `ESP always points to the doubleword on the top of the stack (the stack grows from big addresses to small addresses)`
- ==`PUSH ESP`== and ==`POP dword [ESP]`==:
	- The **source** operand of the instruction is evaluated (`ESP` for PUSH and `DWORD [ESP]` from the top of the stack for `POP`)
	- **ESP is updated** accordingly (`ESP-=4 for PUSH`, `ESP+=4 for POP`)
	- The destination operand is assigned:
		- The new top of the Stack (new ESP which is -4 than the one we put on the stack) for PUSH. Basically putting the stack pointer on top of the stack (4 bytes above it)
		- `dword [ESP]` for POP, but this destination now is 4 upper than the address of the `[ESP]` we added on the stack. Basically putting the value from the top of the stack 4 bytes down the stack.
- **PUSH and POP only allow you to deposit and extract values represented by word and doubleword.** Thus, ==PUSH AL is not a valid instruction (syntax error)==

**XCHG** - instruction allows interchanging the contents of two operands having the same size (byte, word or doubleword) - at least one of them be a register

**XLAT** - `AL<- <DS:[EBX-AL]> or AL <- segment:[EBX+AL]`
- "translates" the byte from AL to another byte, using for that purpose a user-defined correspondence table called translation table. The syntax of the XLAT instruction is `[reg_segment] XLAT`
	- **implicitly**, uses `DS:EBX`, otherwise we specify and `segment_regsiter:EBX` is used
	- The effect of XLAT is the replacement of the byte from AL with the byte from the translation table having the index the initial value from AL, for example the hexadecimal digits, and the `n'th` AL is that digit at the address of EBX, so we use XLAT

**LEA** `general_reg contents of a memory_operand` = `general_reg <- offset(mem_op)`
- LEA has the advantage that the **source operand may be an addressing expression** (unlike the mov instruction which allows as a source operand only a variable with direct addressing in such a case): `lea eax, [ebx+v-6]` is equivalent to `mov eax, ebx+v-6`, but the latter gives a **syntax error**
- By **using the values of offsets that result from address computations directly** (in contrast to using the memory pointed by them), LEA provides more versatility and increased efficiency: We can use the contents of a variable as an offset: 
	- `mov eax, [number] ; eax <- contents of number`
	- `mov eax, [eax*2] ; eax <- number*2, easy multiplication`
	- `mov eax, [eax*4+eax] ; eax <- number*2*4 + number*2 = number*10`

#### PUSHF - transfers all the flags on top of the stack (the contents of the EFLAGS register is transferred onto the stack)
#### POPF - extracts the dword from top of the stack and transfer its contents into the EFLAGS register.


### Type conversion instructions

Conversions classification:
- **Destructive** - `cbw, cwd, cwde, cdq, movzx, movsx, mov ah,0; mov dx,0; mov edx,0` **Non-destructive** – Type operators: `byte, word, dword, qword`
- **Signed** - `cbw, cwd, cwde, cdq, movsx` **Unsigned** –` movzx, mov ah,0; mov dx,0; mov edx,0, byte, word, dword, qword`
- by **enlargement** – all the destructive ones ! + `word, dword, qword`; by **narrowing** – `byte, word, dword`
- implicit vs explicit conversions (int -> float, but NOT float -> int)

**CBW, CWD, CWDE, CDQ**

**MOVZX d, s** - loads in d (REGISTER !), which must be of size larger than s (reg/mem), the UNSIGNED contents of s (zero extension)
- The **unsigned conversion** is done by „zeroing” the higher byte or word of the destination

**MOVSX d, s** - load in d (REGISTER !), which must be of size larger than s (reg/mem), the SIGNED contents of s (sign extension)
- **signed conversion** is extending the ==sign bit== of the source into the higher part (byte/word) of the destination, 0 if the sign bit is 0 , 1 will be put if the sign bit is 1 

#### The impact of the little-endian representation on accessing data

If the programmer uses data consistent with the size of representation established at definition time (for example accessing bytes as bytes and not as bytes sequences interpretted as words or doublewords, accesing words as words and not as bytes pairs, accessing doubewords as doublewords and not as sequences of bytes or words) then the assembly language instructions will automatically take into account the details of representation (they will manage automatically the little-endian memory layout). If so, the programmer must NOT provide himself any source code measures for assuring the correctness of data management. Example:


### Arithmetic operations

Operands are represented in complementary code (see 1.5.2.). The microprocessor performs additions and subtractions "seeing" only bits configurations, NOT signed or unsigned numbers.

 **Logical bitwise operations (AND, OR, XOR, NOT Instructions)**

- AND is recommended for isolating a certain bit or for forcing the value of some bits to 0.
- OR is suitable for forcing certain bits to 1. 
- XOR is suitable for complementing the value of some bits. 
- NOT is used for complementing the operand’s contents (reg/mem).

**Shifts and rotates**: 
- SHL, SHR
- SAL, SAR - Arithmetic shifting
- ROL, ROR - Rotating WITHOUT carry
- RCL, RCR - Rotate with carry (the carry flag is put in the rotated bit (leftmost in right shifting, rightmost in left shifting), and the bit that "exited" on the left/right side is put in the carry flag)

### Branching, jumps, loops

**Unconditional jumps** - JMP, CALL, RETURN
- ==JMP== - unconditional jump to a **label, register or memory address** - unconditional control transfer to the instruction following the label, or to the address contained in the registry/memory
- ==CALL== - Transfers control to the procedure identified by operand
- ==RET [n]== - Transfers control to the first instruction after CALL

**Conditional jumps**
-  ==CMP d, s== - Fictious subtraction d-s, modifies OF, SF, ZF, AF, PF, CF
-  ==TEST d, s== - non-destructive (fictious) d AND s: OF=CF=0, SF, ZF, PF - modified, AF - undefined
- `conditiona_jump_instruction label` 
	- **"jump if operand1 <> operand2"** (where on the two operands a previously CMP or SUB instruction is supposed to have been applied)
	- When two signed numbers are compared, "less than" and "greater than" terms are used and when two unsigned numbers are compared "below" and "above" terms are respectively used
[[Conditional Jumps.png]]
**Repetitive instructions** - ==DO NOT== modify the flags
- ==LOOP== - It first decrements ECX, then the test and eventually the jump.
	- The jump is **"short" (max. 127 bytes)**, use an auxiliary label to jump farther, or `DEC with JNZ`, but it modifies the flags!
	- Ends if **ECX=0**
	- If ECX=0 at the beginning, decrements to `ECX=-1 =  FFFFFFFF`, executing $2^{32}$ times
- ==LOOPE== - stops the same as LOOP + if ZF = 0 = LOOPZ
- ==LOOPNE== - stops the same as LOOP + if ZF =1 = LOOPNZ
- ==JECXZ== - jumps to label if ECX=0

**CALL and RET**
- ==CALL operand== - transfers the control to the address specified by the operand. In addition to JMP, before performing the jump, CALL saves to the stack the address of the instruction following CALL (the returning address) 
	- can be a procedure name, a register containing an address, a memory address
- The end of the called sequence is marked by a ==RET== instruction. This pops from the stack the returning address stored there by CALL, transferring the control to the instruction from this address. (NEAR return)
	- `RET n` <- here n represents how many bytes to POP from the stack (`ADD ESP, n`)
### String constants

When initializing a memory area with string type constants (size of > 1) the data type used in definition (`dw, dd, dq`) does only the reservation of the **REQUIRED** space, ==the "filling" order of that memory area being the order in which the characters appear in the string constant==:
- `a6 dd '123', '345','abcd'`: `31 32 33 00 | 33 34 35 00 | 61 62 63 64`


`mov eax, 'abcd'` <- `EAX = 0x64636261`, so that if you were then to store the value into memory, it would read `abcd` rather than `dcba` - ==LITTLE-ENDIAN==

The main idea of this definition is that THE CHARACTER REPRESENTATION VALUE associated to a string constant `‘abcd’` is in fact `‘dcba’` (this being the STORAGE format in the **CONSTANTS TABLE).**

In the case when **DB** is used as a data definition directive it is normal that the bytes order given in the constant to be also kept in memory in similar way (little-endian representation being applied only to data types bigger than a byte!), so this case doesn’t need an extra analysis.

So, a constant string in NASM ==behaves as there is a previously allocated “memory area” (IT IS AND IT IS CALLED CONSTANT TABLE)== to these constants, where these are stored using the little-endian representation !! From a **REPRESENTATION point of view** the value associated with a string constant **IS ITS INVERSE** !!!! (see the official definition above)


### Location counter and pointer arithmetic

Expressions of type et1 – et2 (where et1 and et2 are labels – either code or data) are syntactically accepted by NASM:
- ==Both of them are defined in the same segment==
- If ==et1 belongs to a different segment from the one in which the expression appears and et2 is defined in this latter one. ==In such a case, the expression is accepted and the data type associated to the expression **et1-et2 is POINTER and NOT SCALAR** (numeric constant) as in the case of an expression composed of labels belonging to the same segment. (==So SOMEWHERE ELSE – HERE OK !, but HERE – SOMEWHERE ELSE NO !!!)==
	- **Subtracting offsets specified relative to the same segment = SCALAR**
	- **Subtracting pointers belonging to different segments = POINTER**
	- 
The name of a segment is associated with **“Segment’s address in memory at run-time”, but this value isn’t accessible to us, this being decided only at loading-time by the OS loader. That is why, if we try to use the name of a segment explicitly in our programs we will get either a syntax error (in situations like 5 $/a-data – “HERE – SOMEWHERE ELSE”) either a linking error (in situations like data-a - SOMEWHERE ELSE – HERE) because practically the name of a segment is associated with its FAR address** (which will be known only at loading time, so it will be available only at run-time; we notice though that segment_address is considered to be “SOMEWHERE ELSE”) and it is NOT associated to "The Offset of a segment is a constant determinable at assembly time" (like it is in 16 bits programming for example, where segment_name at assembly time = its offset = 0). In 32 bits programming, the offset of a segment is NOT a constant computable at assembly time and that is why we cannot use it in pointer arithmetic expressions !
- `Mov eax, data` ; Segment selector relocations are not supported in PE files **(relocation error occurred)**

==`a+b ON ITS OWN = (a-$$) + (b-$$)`==, like `mov eax, a+b`


#### Jump analysis - NEAR vs FAR
- NEAR whenever u access a label through `mov eax, here` or `mov eax, [ebx]`, and `ebx` points to an offset that holds `here`
- ==FAR== jumps: `jmp far [ebx+12] => CS:EIP <- FAR ADDRESS (48 bits = 6 bytes)` $\iff$ `jmp far [DS:ebx+12] => CS:EIP <- far address 6 bytes`
	- (9b 7a 52 61 c2 65) $\to$ EIP = 61 52 7a 9b ; CS= 65 c2 **DO NOT FORGET ABOUT LITTLE-ENDIAN, CS IS IN THE HIGHEST WORD!**. Basically transferring to another code segment fuck knows or not `idfk`
- `- jmp FAR [gs:ebx + esi * 8 - 1023]` <=> `“mov EIP, DWORD [gs:ebx + esi * 8 - 1023]” + “mov CS, WORD [gs:ebx + esi * 8 - 1023 + 4]”`

==JUMPING THROUGH LABELS IS ALWAYS **NEAR**==

Final conclusions.
- **NEAR jumps** – can be accomplished through any of the three operand types (label, register, memory addressing operand)
- **FAR jumps** (this meaning modifying also the CS value, not only that from EIP) – ==can be performed ONLY by a memory addressing operand on 48 bits (pointer FAR)==. Why only so and not also by labels or registers ? - 
	-  if we would have used labels, even if we jump into another segment (an action possible as you can see above) this is not considered a FAR jump because CS is not modified (due to the implemented memory model – Flat Memory Model). Only EIP will be changed and the jump is technically considered to be a NEAR one. 
	- if we would have used registers as operands we may not perform a far jump, because registers are on 32 bits and we may so specify maximum an offset (NEAR jump), so we are practically in the case when it is impossible to specify a FAR jump using only a 32 bits operand.