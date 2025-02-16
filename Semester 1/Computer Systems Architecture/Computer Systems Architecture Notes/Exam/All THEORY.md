## x86 Architecture + Two's complement

-  ==EU== (Executive Unit) – run the machine instr. by means of ALU (Arithmetic and Logic Unit) component. 
- ==BIU== (Bus Interface Unit) - **prepares** the execution of every machine instruction. **Reads** an **instruction** from memory, **decodes** it and **computes** the **memory** **address** of an operand, if any. The output configuration is stored in a 15 bytes buffer, from where EU will take it
	- EU and BIU work in parallel – while EU runs the current instruction, BIU prepares the next one. These two actions are synchronized – the one that ends first waits after the other.
"Word size" refers to the number of bits processed by a computer's CPU in one go (these days, typically 32 bits or 64 bits). Data bus size, instruction size, address size are usually multiples of the word size
Microsoft Windows API defines a WORD as being 16 bits, a DWORD as 32 bits and a QWORD as 64 bits, regardless of the processor

---

#### EU general registers
- EAX - **accumulator**. Used by the most of instructions as one of their operands. 
- EBX – **base register**. 
- ECX - **counter register** – mostly used as numerical upper limit for instructions that need repetitive runs. 
- EDX – **data register** - frequently used with EAX when the result exceed a doubleword (32 bits).
- ESP and EBP are stack registers. The stack is a LIFO memory area.
- Register ESP (**Stack Pointer**) points to the last element put on the stack (the element from the top of the stack).
- Register EBP (**Base pointer**) points to the first element put on the stack (points to the stack’s basis).
- EDI and ESI are index registers usually used for accessing elements from bytes and words strings
	- EAX, EBX, ECX, EDX, ESP, EBP, EDI, ESI are doubleword registers (32 bits).
	- The lower register could be used as single so we have the 16 bits registers AX, BX, CX, DX, SP, BP, DI, SI;
		- AX, BX, CX, DX also have two parts of 8bits, a higher one AH, a lower one: AL

#### Flags

A flag is an indicator represented on 1 bit. The flags are bits of the EFLAGS register from the EU.

- **CF** - Carry flag - transport flag. It will be set to 1 if in the LPO there was a transport digit outside the representation domain of the obtained result, 0 otherwise
	- ==Marks the UNSIGNED overflow==
- **PF** - Parity flag - Set to 1 if itself added with the number of 1 digits in the least significant byte of the LPO's representation, the result will be an odd number (basically 1 if even number of 1's in the LPO)
- **AF** - Auxiliary flag - the transport value from bit 3 to bit 4 of the LPO's result
- **ZF** - Zero flag - set if LPO was 0
- **SF** - Sign flag - set if the LPO is a strictly negative number (in the ==SIGNED INTERPRETATION==) (has the most significant bit 1)
- **TF** - Trap flag - debugging flag: if set to 1, the machine stops after every instruction
- **IF** - Interrupt flag - If set to 1 interrupts are allowed, if set to 0 interrupts will not be handled
- **DF** - Direction flag - for operating string instructions: If set to 0 (CLD) the string parsing will be made in an ascending order (+), otherwise if set to 1 descending order (-)
- **OF** - Overflow flag - ==flags the SIGNED overflow==. If the result of the LPO does not fit the reserved space, then OF will be set to 1, otherwise set to 0
	- taking the most significant bytes, OF is set when: 1+1=0 , 0+0=1, 1-0=0, 0-1=1

**Flag categories**:
- flags **set as a** **direct effect** of the execution **of the Last Performed Operation**** (LPO): CF, PF, AF, ZF, SF and OF
- flags **set by the programmer** to influence the way the next instructions to come will be run: CF, TF, DF and IF - using special instructions
	- **CLC** - CF = 0; **STC** - CF = 1; **CMC** - complements the value of CF (if 0 then 1, if 1 then 0)
	- **CLD** - DF = 0; **STD** - DF = 1
	- **CLI** - IF = 0; **STI** - IF = 1
	- NO instructions to directly access TF

#### Operations performed by ALU

- **Arithmetic operators** - It refers to bit subtraction and addition, despite the fact that it does multiplication and division. Multiplication and division processes, on the other hand, are more expensive to do. Addition can be used in place of multiplication, while subtraction can be used in place of division.
- **Bit-Shifting operators** - involves shifting the location of a bit to the right or left by a particular number of places. It is responsible for a multiplication operation.
- **Logical Operations**: These consist of AND, OR, XOR, NOT


#### Two's complement

Mathematically, the two's complement REPRESENTATION of a NEGATIVE number is the value  $2^n$ -V, where V is the absolute value of the represented number
With the 2’s complement, ==“We interpret representations and represent interpretations”==

---
How can we obtain the 2’s complement of a number? 

- **Variant 1 (Official)**: **Subtracting the binary contents of the location from 100 ...00** (where the number of zero’s are exactly the same as the number of bits of the location to be complemented)
- **Variant 2 (derived from the 2’s complement definition – faster from a practical point of view):** ==reversing the values of all bits of the initial binary number== (value 0 becomes 1 and value 1 becomes 0), after which we ==add 1== to the obtained value
- **Variant 3 (MUCH faster practically for obtaining the binary configuration of the 2’s complement):** We left  bits starting from the right until to the first bit 1 ==unchanged==, including it, then we reverse the values of all the other bits (all the bits from the left of this bit).
- **Variant 4 (the MOST faster practical alternative, if we are interested ONLY in the absolute value in base 10 of the 2’s complement):** 
	- **Rule** derived from the definition of the 2’s complement: ==The sum of the absolute values of the two complementary values is the cardinal of the set of values representable on that size.==
	- its basically just the definition ...
	- Which is the signed interpretation of 147 in base 10 ? - STUPID QUESTION – we cannot have DIFFERENT interpretations in base 10 of numbers ALREADY expressed in base 10 – 147 IS ALREADY AN INTERPRETATION !!)

Mathematically, the two's complement representation of a NEGATIVE number is the value 2 n - V, where V is the absolute value of the represented number. 
==So the whole discussion about the 2's complement makes practical sense ONLY WHEN we refer to the BINARY REPRESENTATION of a NEGATIVE number from base 10!!! Or to the SIGNED INTERPRETATION of a binary number starting with 1 !! That is, ONLY when we discuss the INTERPRETATION of numbers that in base 2 start with 1 !!!!!! When we have a binary number starting with 0, its INTERPRETATION WILL BE THE SAME in both SIGNED and UNSIGNED,==

So the intersection of the admissible representation intervals on a dimension N consists ONLY of the values that in binary begin with bit 0! **As a result, binary values starting with bit 1 are NOT common to these "complementary" ranges, meaning that the signed and unsigned interpretations of any binary configuration starting with 1 WILL ALWAYS BE DIFFERENT and they will NEVER be parts of the same admissible representation interval !!**! The absolute values of the two interpretations represent two complementary values

![[TwosComplement.png]]

[[Two's complement questions]] - All the questions regarding AND what is the MINIMUM number of bits to represent a number...

#### Overflow concept analysis

>[!info] At the level of the assembly language an overflow is a situation (condition) which expresses the fact that the result of the LPO either:
>- did not fit the space for it (ex: unsigned addition, 8bits+8bits=9bits, CF=1)
>- does not belong to the admissible representation interval for that size
>- the operation is a mathematical nonsense in that particular interpretation (signed or unsigned) (**ex**: in signed: pos+pos = negative and vice versa because of the rules of the signed interpretation)

- OF set when, if we look ONLY at the most significant bit (sign bit in two's complement!)
	- 1+1 = 0,  0+0=1, 1-0 = 0, 0-1 = 1 ONLY those four situations


==CF and OF can be set at the same time, independent of each other, as each of them shows something different!== We do not know if we use signed or unsigned interpretation, we only care about the operations, so BOTH are used at the same time, but we only look at what we care about: CF if we care about Unsigned interpretations, OF if we care about signed interpretations. CF marks unsigned overflow, basically incorrect result, while OF marks signed overflow, an incorrect result in a signed interpretation.  ==We take into account the INTERPRETATION of the result of LPO==

Why do we need CF and OF in EFLAGS SIMULTANEOUSLY?? Isn't a single flag enough to show us IN TURN if we have an overflow or not, either in the signed interpretation or in the unsigned one ? **NO, because when performing an addition or subtraction operation in base 2, in fact 2 operations are actually performed SIMULTANEOUSLY in base 10: one in the signed interpretation and the other in the unsigned interpretation.**

As a result, two different flags are needed SIMULTANEOUSLY to deal each of them SEPARATELY with one of the 2 possible interpretations in base 10: CF – for the unsigned interpretation ; OF – for the signed one. This happens because the operation of addition or subtraction expressed IN BASE 2 is performed IDENTICALLY, therefore, REGARDLESS OF THE signed or unsigned INTERPRETATION of the operand

So, why do we need then **IMUL** and **IDIV** ?? Because unlike addition and subtraction, which work the same in base2, regardless of the interpretation (signed or unsigned), SIGNED and UNSIGNED multiplication and division work DIFFERENTLY in the signed case compared to the unsigned case !!

- **Division overflow** - ==run-time error== if the quotient does not fit in the reserved space, we get an error called "divide overflow"/division by zero/zero divide
	- In the case of **correct division, CF and OF are undefined!**
- **Multiplication** - ==does not produce overflow ever!==, but by convention, if the multiplication result is the same as the size of the operands (`b*b=b, w*w=w, d*d=d`) => **CF=OF=0**. Otherwise, `b*b=w, w*w=d, d*d=q` => **CF=OF=1**
## Address computation

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




## Assembly language basics
Assembly language is a **symbolic language. Symbols = mnemonics + labels**

- **Labels** - used-defined names for pointing to data or memory areas
	- is an offset specification!
	- pointing to a certain memory area inside the **code segment** - code labels
- **Instructions** - mnemonics which suggest the underlying action. The assembler generates the bytes that codifies the corresponding instruction
- **Directive** -  given to the assembler for correctly generating the corresponding bytes.
	- Ex: relationships between object modules, segment definitions, conditional assembling, data definition directives
- **Location counter** - an integer number managed by the assembler for very separate memory segment. At any given moment, the value of the location counter is the number of the generated bytes correspondingly with the instructions and the directives already met in that segment (the current offset inside that segment). The programmer can use this value (read-only access!) by specifying in the source code the '$' symbol. **Every segment has its own location counter!!**
	- `$` - evaluates to the assembly position at the beginning of the line containing the expression = **the current offset inside that segment** = ==location counter== - ==POINTER TYPE, offset==
	- `$$` - evaluates to the start of current segment - ==POINTER TYPE, offset==
	- `$-$$ = how far you are in a segment` = scalar, current size of section/segment
[[Location Counter]]

---

### Source line format

>[!important] $$[label[:]][prefixes][mnemonic][operands][;comment]$$

- **All** identifiers are ==case SENSITIVE==, but implicit names (keywords, mnemonics, registers) are case **insensitive**

**Label categories:**
- ==code labels== - present at the level of instructions sequences for defining the destinations of the control transfer during a program execution; can appear also in data segments
- ==data labels== - provide symbolic identification for some memory locations (contains offset); can also appear in code segments
	- ==The value associated with a **label** in assembly language is a **number representing the address of the instruction or directive following that label.**==
- **straight brackets** - denotes the value of the variable at address `p`: `[p]`
- other contexts - the name represents the **address of the variable**
As a generalization, using straight brackets always indicates accessing an operand from memory.

**Types of mnemonics:**
- ==instructions names== - actions that *guide* the processor
- ==directives names== - *guide* the assembler. They specify the particular way in which the assembler will generate the object code

==operands== - parameters which **define the values to be processed by the instructions or directives.** They can be *registers, constants, labels, expressions, keywords or other symbols*. Their semantics **depends on the mnemonic** of the associated instruction or directive.


### Expressions

- ==operators== - indicate how to combine the operands for building an expression

>[!important] ==expression== - operands + operators - **COMPUTED AT ASSEMBLY TIME** (their values are computable at assembly time, except for the operands representing registers contents, that can be evaluated only at run time – the offset specification formula)

**Operand types**: ==immediate== operands, ==register== operands, ==memory== operands. Their values are computed at:
- ==immediate== (`17, v`) and the ==direct addressed== (the offset part only: `[v]`)  operands are computed at **assembly time**:
	- ??:offset (assembly time)
- ==memory operands in direct addressing mode== (as a complete FAR address), because the segment selector is determinable only here - **loading time** - involves a process called ==ADDRESS RELOCATION PROCESS== (adjusting an address by fixing its segment part)
	- 0708:offset (loading time)
- **run time**  - ==register== operands and ==indirectly accessed memory operands== (`[ebx+2], [2*ebx+v])

#### Immediate operands - constant numeric data computable at assembly time

- specified through binary (`b, y`), octal (`q, o`), decimal (`d, t`) or hexadecimal (`h, x`) values. Can use `_` to separate groups of digits (has no effect)
	- `0ABCH - hexadeicmal`, `ABCH - symbol` - h as a suffix, or others same
	- Can also use `0x, 0h, 0b, 0d, etc.` as prefixes: `0xAb`, digits are case insensitive

>[!important] The offsets of data labels and code labels are values computable at assembly time and they remain constant during the whole program’s run-time
>`mov eax, 8 `, `mov eax, [var]` <- computable at assembly time
>determinable at assembly time based upon the order in which variables are declared in the source code and due to the dimension of representation inferred from the associated type information.

#### Register operands 

- ==Direct usage== - `mov eax, ebx`
- ==Indirect usage and addressing== - used for pointing to memory locations - `mov eax, [ebx]` 
#### Memory addressing operands

##### DIRECT addressing operands

- ==Direct addressing operands== - constant or a symbol representing the address (segment and offset) of an instruction or some data. May be **labels** (`jmp et`), **procedure names** (`call proc`), **the value of the location counter** (`b db $-a`)
	- The **offset** of a direct addressing operand is computed at **assembly time.** 
	- The ==address of every operand relative to the executable program’s structure== (**establishing the segments** to which the computed offsets are relative to) is computed at **linking time.** 
	- The== actual physical address== is computed at **loading time.**

The effective address always refers to a segment register - can be implicit by an instruction or explicit by the programmed. Rules for using an explicit specified offset operand:
- **CS** for code labels target of the control transfer instructions `(jmp, call, ret, jz etc)`;
- **SS** in **SIB** addressing when using **EBP or ESP as base** (no matter of index or scale);
- **DS** for the rest of data accesses;
- Done using `:` prefix operator: `ES:[var], DS:[ebx+eax*2-a]`, ES can ONLY be explicitly specified or used in string instructions (`MOVSB`, `ES:[EDI]` I think it was..)
	- Or `JMP FAR CS:..., JMP FAR DS:... JMP FAR [label]`

##### INDIRECT addressing operands

- ==indirect addressing operands== - use registers for pointing to memory addresses - suited for dynamic data operations (register values known only at run time)
	- indirectly accessing a memory operand formula: `[base_register + index_register*scale + constant]`, constant - computable at assembly time, can be immediate or offset: `[ebx+edi+table+6], table and 6 are constants`
	- base/index usually used to refer to an array, iterating through it
			- `mov dh, [edx+ecx*4+3]` - array at address `edx` of `dwords`, so we iterate `4` bytes at a time, and `+3` says "go to the last byte of an element" (highest byte because little-endian)

From a syntactic point of view, when the **operand is not specified by the complete formula, some of the components missing** (for example when "* scale" is not present), the assembler will solve the possible **ambiguity** by an analysis process of all possible equivalent encoding forms, choosing 
the shortest finally.

Also, in addition to solving such ambiguities, the assembler also **allows non-standard expressions,** ==with the condition to be in the end transformable into the above standard form.==
[[WHAT SEGMENT WILL BE ACCESSED|Ambiguity examples]]

#### Using operators

**Operators** – used for combining, comparing, modifying and analysing the operands.

**Operators perform computations only with constant SCALAR values computable at assembly time** , ==does not work on pointers! Cannot do ~a, !a, a+b, a and b, NOT SCALARS==(scalar values = constant immediate values), with the exception of adding and/or subtracting a constant from a pointer (which will issue a pointer data type) and with the exception of the offset computation formula (which supports the ‘+’ operator). While **Instructions** perform computations with values that may remain unknown (and this is generally the case) until run time.
- ==Expression evaluation is done on 64 bits, ==the final results being afterwards adjusted accordingly to the size of available in the available usage context of that expression.
- For example the addition operator (+) performs addition at assembly time and the ADD instruction performs addition during run time.
![[Operators.png]]

##### Bit shifting operators
- `expression >> how_many, expression << how_many`, shift all the bits `how_many` positions
##### Bitwise operators
Bitwise operators perform bit-level logical operations for the operand(s) of an expression. The resulting expressions have constant values.
##### The segment specification operator
 - The segment specifier operator (:) performs the FAR address computation of a variable or label relative to a certain segment. Its syntax is: `segment:expression` (`[ss:ebx+4]` relative to SS, `10h:var`, 10h selector)

##### Type operators
- They specify the types of some expressions or operands stored in memory. Syntax:
	- `type expression`
		- `type`: `BYTE, WORD, DWORD, QWORD, TWORD`, causes `expression` to temporarily (on that instruction) have size `type`
			- for ==memory-stored operators: ==`byte, dword, qword, tword` having size of `1, 2, 4, 8, 10 bytes`
				- `mov [v],0 ; syntax error – operation size not specified`
			- for ==code labels== `type` is either **NEAR** (4 bytes address) or **FAR** (6 bytes address)
		- When we **need** a type specifier:
			- `mov [mem], ...`, `(i)div [mem], (i)mul [mem]`, `push [mem], pop [mem]`
			- Exceptions: `push 15, ambiguity will be solved as push dword 15`
`mov ax, [ebx]` – the source operand doesn't have an associated data type (it represents only a start of a memory area) and because of that, in the case of our MOV instruction the destination operand is the one that decides the data type of the transfer (a word in this case), and the transfer will be made accordingly to the little endian representation.

### Directives

>[!important] Directives direct the way in which code and data are generated during assembling

---

#### The SEGMENT directive

**SEGMENT** directive allows targeting the bytes of code or of data emitted by an assembler to a given segment, having a name and some specific characteristics.
- `SEGMENT name [type] [ALIGN=alignment] [combination] [usage] [CLASS=class]`
- ==name== - segment address (32 bits) corresponding to the memory segment's position during run-time (`$$`)
- Except the name, all the other fields are **optional** and the order in which they are specified does not matter
- The ==optional arguments== **alignment, combination, usage and 'class'** give the necessary information regarding the way in which segments must be loaded and combined in memory to the **link-editor** and the **assembler**
	- ==type== - select the **usage** mode of the segment:
		- **code** (text) - code segment, which can be executed, not written
		- **data** (bss) - data segment allowing reading and writing but NOT execution (**implicit value**) 
		- **rdata** - can only be read, contains definitions of constant data
	- ==alignment== - the multiple of the bytes number from which that segment may start (powers of 2 between 2 and 4096). **implicitly ALIGN=1, can start from any address**
	- ==combination== - controls the way in which similar named segments from other modules will be combined with the current segment at linking time. 
		- **public** - indicates to the link editor to concatenate this segment with other segments with the same name, obtaining a single segment having the length the sum of concatenated segments’ lengths
		- **common** - specifies that the beginning of this segment must overlap with the beginning of all segments with the same name, obtaining a segment having the length equal to the length of the larger segment with the same name.
		- **PRIVATE** - indicates to the link editor that this segment cannot be combined with others with the same name.
		- **STACK** - the segments with the same name will be concatenated. During run time the resulted segment will be the stack segment.
		- **IMPLICITLY** it is always **PUBLIC**
	- ==usage== - allows choosing another word size than the default 16 bits one
	- =='class'== - has the task to allow choosing the order in which the link editor puts the segments in memory. All the segments that have the same class will be placed in a contiguous block of memory whatever their order in the source code.
		- **No implicit value exists,** it being undefined when its specification is missing, leading though to NOT concatenating all the program’s segments defined so in a continuous memory block.
	- `segment code use32 class=CODE, segment data use32 class=DATA`
 

#### Data definition directives

**Data definition** (unique) = ==declaration== (NOT unique) (attributes specification) + ==allocation== (UNIQUE) (reserving required mem. space) 
**data type** = size of representation – byte, word, doubleword or quadword

General form of a ==data definition source line:==
- `[name] data_type expression_list`
- `[name] allocation_type factor`
- `[name] TIMES factor data_type expression_list`, where name is a label for data referral
- The ==data type== is the size of representation and its value will be the address of its first byte.
- ==`factor`== is a number which shows how many times the ==`expression_list`== is repeated
- ==`Data_type`== is a data definition directive, one of the following: DB, DW, DD, DQ, DT
- After a data definition directive may appear more than one value, thereby allowing declaration and initialization of arrays. For example, the declaration: `Table dw 1, 2, 3, 4, 5`
- ==allocation_type== is a uninitialized data reservation directive: `RESB, RESW, RESD, RESQ, REST`
- ==`TIMES`== directive allows repeated assembly of an instruction or data definition: `Table TIMES 80 DB 'ab'` creates an 'array' of `80*2` bytes, each two being `'a' and 'b'`


**EQU Directive** - allows assigning a numeric value or a string during assembly time to a label without allocating any memory space or bytes generation
	- `name EQU expression` -  `BUFFER_SIZE EQU 1000H`, `EXCLAMATION_MARK EQU '!'`, `INDEX_START EQU BUFFER_SIZE/2`

### Error types in CS:
#### **ASSEMBLY ERROR** = Syntax Error - diagnosed by assembler / compiler ! - eroare de asamblare
- because an assembler generates bytes 

#### Run-time error (execution error) - program crashes - it stops executing
- e.g.: **Stack overflow**

#### Logical error = program runs until its end or remains blocked in an infinite loop ... if it functions until its end, it functions LOGICALLY WRONG obtaining a totally different result/output than the envisioned ones

#### Fatal: Linking Error  !!! 
- For example, in the case of a variable defined multiple times in a multimodule program ... if we have 17 modules, a variable must be defined ONLY in a SINGLE module ! If it is defined in 2 or more modules, a "Fatal: Linking error - Duplicate definition for symbol..." will be obtained!
##### The steps followed by a program from source code to run-time:
- Syntactic checking (done by **assembler/compiler/interpreter**)
- **OBJ** files are generated by the **assembler/compiler**
- **Linking phase** (performed by a **LINKER** = a tool provided by the **OS**, which checks the possible **DEPENDENCIES** between the **OBJ files/modules**). The result is, in windows, **.EXE** file
- You (the user) are activating your exe file by clicking or entering
- The **LOADER** of the **OS** is looking for the required RAM memory space for your EXE file. When finding it, it loads the EXE file AND performs ADDRESS RELOCATION - ==loading phase==, where are the data segments of the program, their `file descriptor`
- In the end the loader gives control to the processor by specifying THE PROGRAM's ENTRY POINT (ex: start label) !!! The run-time phase begins now!


## Instructions


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

## Machine instructions representation
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