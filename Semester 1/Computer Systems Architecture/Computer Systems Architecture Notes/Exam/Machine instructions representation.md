A **x86 machine instruction represents a sequence of 1 to 15 bytes**, these values specifying an operation to be run, the operands to which it will be applied and also possible supplementary modifiers.

---
### Instruction representation formula 

`[prefixes] + code + [Mode R/M] + [SIB] + [displacement] + [immediate]`

- The **prefixes** control how an instruction is executed - *optional* (0 to 4, 1 byte each)
	- For example, they may request repetitive execution of the current instruction or may block the address bus during execution to not allow concurrent access to operands and results
- The operation to be run is identified by **1 to 2 bytes** of ==code== (**opcode**), which are the only mandatory bytes, no matter of the instruction.
- The ==byte Mode R/M ==(register/memory mode) specifies for some instructions the nature and the exact storage of operands (register or memory). This allows the specification of a register or of a memory location described by an offset

![[Internal format of machine instruction.png]]

>[!note] Most of the instructions use for their implementation either only the opcode or the opcode followed by ModeR/M.

The displacement is present in some particular addressing forms and it comes immediately after ModR/M or SIB, if SIB is present.

On the **80x86 processors**, this ==displacement is an offset from the beginning of memory (that is, address zero).== = FMM ?

We care about the last 4 of this formula 
The last 3 are exactly the address specification formula: 
- `[SIB]` = Scale index based (base + index * scale)
- `[displacement]` = Pointer type addition
- `[immediate]` = numerical constant


>[!important] The first one, `[Mode R/M]` is the most important part! It's byte representation is below:

```
 7 6   5   4   3 2 1 0 <- bits
|   |           |     |
 Mod  Reg/Opcode  R/M
 
 bits 0 1 2 3 -> R/M
 3 4 5 -> Reg/Opcode
 6 7 -> Mod

```

---
**SIB representation:**
```
7 6   5 4 3  2 1 0
Scale Index   Base    
Base = Base register, can have 7 base retergisters
Index = Index register, can have 7 index registers without ESP
Scale = 1 / 2 / 4 / 8 (00 / 10/ 01 /11) for the two bits
```

---

Back to `[Mode R/M ]`:

#### Reg/Opcode in Mode R/M - Represents 7 possible sets of registers

#### Mod in Mode R/M

- Mod -> the **combinations** possibilities of the operands (4 possibilities)
- 00 -> reg, **memory operand** (only **base**) | memory operand, reg 
- 01 -> mem(base+*displacement*), reg - or inverted - 8bits displacement
- 10 -> mem `(base+displacement)`, reg --//-- - 32 bits displacement
- 11 -> instr. **register, register**

>[!note] When you have something like `add [ebx+17], 2`, 17 will be represented on a byte, even if the formula does not normally allow to have values that are not 16/32 bits in its formula.

---
### Examples

>[!important] Example: `mov [EDX], EBP ; 892A`; 89 = code for MOV, 2A = Mod R/M

```
2A = 00    101      010
     Mod Reg/Opcode R/M

Mod = 00 -> instr memory, reg ; which is correct
Reg/Opcode = 101 = 5 which represesnts CH/BP/EBP -> Here it's EBP
R/M = 101 -> disp32 (displacement of 32 bits) -> [EDX]
```

---
- More examples: `mov ecx, [esp+ebx+4] ; 890C9C`
```
8B = code for MOV
0C = Mod R/M
9C = SIB

0C = Mod R/M = 00 001 100 (use table of MOD R/M)
Mod = 00 -> instr reg, mem
Reg/Opcode = 001 -> column 2 (CL/CX/ECX...) so ECX here
R/M = 100 = [...][...] = YOU NEED A SIB BYTE!!!

9Ch = SIB = 10 011 100 (use the TABLE OF SIB)
100 = Base = Column 3 = ESP 
011 = Index = [EBX] 
10 = Scale = Third row (*4)
combined with the scale, we will have [EBX*4]
All combined will be [ESP+EBX*4]
```


### For written exam:
- KNOW what Mod R/M Byte means, that it has 3 fields and what they mean.
- Only need to know what they mean , the 3 categories, and we can say that we can check in he table to see what it means, no need to learn it
- Example: Mod has 4 categories: explain them briefly: register and memory, displacement on 8bits: 01, register with register, or displacement with 32bits

```nasm
eip db 10 WORKS OMGOMGGOGMOGMGOGMOGMGOGMGKM
```



---

As a consequence of the impossibility of appearing more than one Mode R/M, SIB and displacement fields in one instruction, **the x86 architecture doesn’t allow encoding of two memory addresses in the same instruction.** = ==CANNOT HAVE TWO EXPLICIT MEMORY OPERANDS IN THE SAME INSTRUCTION==

With the immediate value we can define an operand as a numeric constant on 1, 2 or 4 bytes. When it is present, this field appears always at the end of instruction

### Prefixes

- an instruction can have up to **4** prefixes
**Instruction prefixes** are assembly language constructs that appear *optionally* in the composition of a source line (**explicit** prefixes) or in the ==internal format of an instruction (prefixes generated implicitly by the assembler in two cases) ==and that modify the standard behaviour of those instructions (in the case of explicit prefixes) or which **signals the processor to change the default representation size of operands and/or addresses, sizes established by assembly directives (BITS 16 and BITS 32).**

**Explicit:**
- String manipulation instruction prefixes: REP - repeats instruction the number of times as ECX, REPE, REPNE - same as LOOPE/LOOPNE concept
- Segment override prefix causes memory access to use specified segment instead of default segment designated for instruction operand: ES, etc.

**Implicit**:
- Operand override, 66h. Changes size of data expected by default mode of the instruction
- Address override, 67h. Changes size of address expected by the default mode of the instruction
	- These two last prefix types appear as a result of some particular ways of using the instructions (examples below), which will cause the generation of these prefixes by the assembler in the internal format of the instruction.