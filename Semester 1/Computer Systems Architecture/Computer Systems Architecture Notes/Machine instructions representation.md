
## Instruction representation formula 

`[prefixes] + code + [Mode R/M] + [SIB] + [displacement] + [immediate]`

We care about the last 4 of this formula 
The last 3 are exactly the address specification formula: 
- `[SIB]` = Scale index based (base + index * scale)
- `[displacement]` = Pointer type addition
- `[immediate]` = numerical constant

>[!Important] `[ModeR/M]` is the most important part! It's byte representation is below:


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

#### Reg/Opcode in Mode R/M

- Represents 7 possible sets of registers

#### Mod in Mode R/M

- Mod -> the **combinations** possibilities of the operands (4 possibilities)
- 00 -> reg, **memory operand** (only **base**) | memory operand, reg 
- 01 -> mem(base+*displacement*), reg - or inverted - 32bits displacement
- 10 -> mem(base+displacement), reg --//-- - 8 bits displacement
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
- Only need to know what they means , the 3 categories, and we can say that we can check in he table to see what it means, no need to learn it
- Example: Mod has 4 categories: explain them briefly: register and memory, displacement on 8bits: 01, register with register, or displacement with 32bits



```nasm
eip db 10 WORKS OMGOMGGOGMOGMGOGMOGMGOGMGKM
```