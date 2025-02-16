
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