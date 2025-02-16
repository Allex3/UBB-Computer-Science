**Address of a memory location** - no. of consecutive **bytes** from the beginning of the RAM memory and the beginning of that memory location

>[!INFO] **Segment** - an uninterrupted sequence of memory locations, used for similar purposes during a program execution = **logical section of a program's memory**
>A **segment** is determined by its
>	---base address (**beginning**) - 32 bits value
>	---limit (**size**) - 32 bits value
>	---type

in 8086 processors, **segment** has two meanings: 
- Block memory of discrete size: *phyisical segment*: `2^16, 2^32` for 16/32 bit processors.
- Variable-sized block of memory: *logical segment* - program's code or data

- **==offset==** - the number of bytes between the beginning of that segment and that particular memory location. **Valid** if it doesn't exceed the segment's limit!
- ==segment selector== - numeric value of 16 bits which uniquely selects the accessed segment and its features. **Provided by the OS! The user does NOT know it!**. (corresponds to one of the active code segments)
- ==address specification==: $s_{3}s_{2}s_{1}s_{0}:o_{7}o_{6}o_{5}o_{4}o_{3}o_{2}o_{1}o_{0}$, which we will denote `s:o`. In this case, **s** is the segment selector corresponding to a segment with the base address $b_{7}b_{6}b_{5}b_{4}b_{3}b_{2}b_{1}b_{0}$ = `b` and the limit $l_{7}l_{6}l_{5}l_{4}l_{3}l_{2}l_{1}l_{0}$ = `l`. Base and limit are obtained by the processor after performing a **segmentation process**.
	- Condition to give access: `o` < `l`, so it doesn't go outside of the segment
	- also called ==FAR Address==
	- If address is specified **only by the offset, it's called a** ==NEAR Address==
- ==address computation== - based on the above definition: $a_{7}a_{6}a_{5}a_{4}a_{3}a_{2}a_{1}a_{0} := b_{7}b_{6}b_{5}b_{4}b_{3}b_{2}b_{1}b_{0} + o_{7}o_{6}o_{5}o_{4}o_{3}o_{2}o_{1}o_{0} \iff$ `a:=b+o`. where **a** is the computed address in hexadecimal form, called the **linear/segmentation address**!
	- For an address `8:1000h`, `b` = 2000h, `l` = 4000h. If `8` is not valid, memory violation error. If it is valid, extract the base and limit, then verify if `o` > `l`, if so, the access will be blocked. If `o` <= `l`, then the offset is added to `b` and we obtain the address `a = o+l`. This computation is performed by the **ADR** component of the **BIU**
	- This kind of addressing is called ==segmentation==!

- ==Flat memory model== - If the segments start from 0 and have the maximum possible size (4GiB), any offset is valid and the address `s:o` will be `a:=0+o = o` . Segmentation isn't particularly involved.
- ==paging== - *independent of address segmentation* - divide the *virtual memory* into *pages*, which are translated to physical memory: 1 page = $2^{12}$ = $4096$ bytes

>[!info] The configuration and the control of segmentation and paging are performed by the operating system. Of these two, only segmentation interferes with address specification, paging being completely transparent relative to the user programs.

Address computing and paging are influenced by the execution mode of the processor. x86 supports:
- real mode - 16 bits
- **protected mode on 16/32 bits, characterized by paging and segmentation** - ==what we use==
- 8096 virtual mode and long mode

---

### Segments

- ==code segment== - contains instructions
- ==data segment== - contains data which instructions work on
- ==stack segment== - contains the LIFO stack
- ==extra segment== - supplementary data segment

>[!important] Every program is composed by one or more segments of one or more of the above specified types. At any given moment during run time there is only at most one active segment of any type.

- ==segment registers==: Registers **CS, DS, SS, ES** from **BIU** contain the *values of the selectors of the active segments*, corresponding to every type. So they **determine** the starting address and the dimensions of the 4 active segments. **FS and GS** don't have predetermined meaning, can store selectors pointing to auxiliary segments. 
- ==EIP== (IP) - contains the **offset of the current instruction in the active code segment** - managed by **BIU**

![[Address specification.png]]


---

### FAR and NEAR addresses

To address a RAM memory location, we need a segment selector and its offset inside that segment. 
- **The microprocessor implicitly chooses,** in the absence of other specification, the segment’s address **from** one of the segment registers **CS, DS, SS or ES.** The implicit choice of a segment register is made after some particular rules **specific** to the used **instruction**.


- ==NEAR address== - always inside one of the 4 active segments = an address for which **only the offset is specified, the segment address being implicitly taken from a segment register**
- ==FAR address== - the programmer explicitly specifies a segment selector = **COMPLETE ADDRESS SPECIFICATION**. Ways to specify:
	- `s:offset`, s - constant
	- `segment_register:offset`, where `segment_register` = CS, DS, SS, ES, FS, GS
	- `FAR [variable]` - variable is **qword** containing the 6 bytes of the **FAR address** (at the smallest 4 bytes is the offset, then at bytes 4 and 5 is the word that stores the segment selector) - follows little-endian representation

### Computing the offset

3 ways to access an operand for an instruction:
- **register mode** - required operand is a register `mov eax, 5`
- **immediate mode** - use the operand value *directly*, no address/register: `mov eax, 17` <- 17
- **memory addressing mode** - if the operand is located somewhere in memory, uses formula:
	- `offset_address = [base] + [index*scale] + [constant]` (2 AM formula)
	- ==base== - EAX, EBX, ECX, EDX, EBP, ESI, EDI, ESP
	- ==index== - as above **without ESP**
	- ==scale== - 1, 2, 4, 8
	- ==constant== - direct value (immediate) on a byte/word/dword
	- **direct addressing** - when `constant` is present
	- **based addressing** - if a *base register* is present
	- **scale-indexed addressing** - if one of the *index registers is present* (basically if an index register is multiplied with 1, 2, 4, 8 is an index, otherwise it's a base, or we can have stuff like `[9*EBX] = [EBX + 8*EBX], which is based and scale-indexed)
	- ==indirect addressing== - no constant, only based and/or scale-indexed. So at least one register

In the case of the **jump instructions** another type of addressing is present called ==relative addressing.==
- ==relative addressing== - indicates the position of the next instruction to be run relative to the current position. **"distance" = number of bytes to jump over**
- ==relative SHORT addresses== - a byte - between -128 and 127 bytes (above/below)
- ==relative NEAR addresses== - `[-2^32, 2^32-1]`

### L-values, R-value - Pointer arithmetic

==POINTER ARITHMETIC OPERATIONS== - Pointer arithmetic represents the set of arithmetic operations allowed to be performed with pointers
**Allowed pointer operations**: (ONLY THESE)
- ==addition of a constant==: `p+7` (`-p+7` gives **syntax error!**)
- ==subtraction of a constant==: `p-5` - moving in a table for example
- ==subtraction of two pointers:== `p+q` <- abs. value = number of bytes between the addresses
- **DO NOT** add/multiply/divide two pointers, or a pointer with a constant

**LHS** (left hand side/L-value) = an address, **WE PUT CONTENTS HERE**
**RHS** (right hand side/R-value) = **CONTENTS** (immediate or register or memory), DO NOT PUT CONTENTS HERE, ONLY ACCESSED CONTENTS, NOT AN ADDRESS TO BE PUT INTO

`Address_computation_expression := expression; Symbol := expression_value`
C++:
- `int& j = i //j becomes alias for i`
- `float f(int& x) - passing by reference, so contents CAN be changed`
- `Returning L-values: int& f(x, i) {return v[i];} so f(a, 7) = 79` $\iff$ `v[7] = 79`

[[WHAT SEGMENT WILL BE ACCESSED]], [[Offset formula#ASM Example|Offset formula examples]]


