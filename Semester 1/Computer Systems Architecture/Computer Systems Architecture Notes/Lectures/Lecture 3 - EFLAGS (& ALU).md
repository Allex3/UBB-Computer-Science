### [Operations performed by ALU](ALU)

###### Computer on n bits
- The software vision - "word size" = size of the registers on the architecture (on 32-bits)
	- The software vision that we embrace means the size of the general registers, it means the size of the "word size", which in our case it's 32 bits
- The engineering vision - **not size of registers**, but the size of a CPU on n bits means **the size of the buses** (the communication channel)
	- a bus can be on 64 bits, even if the registers are 32
	- Because there can be differences, there were situations in which the sizes were identical
- The Windows API defines a WORD as being 16 bits, regardless of the processor, even if the processor "word size" is 32 or 64 bits

### [EFLAGS Register](EFLAGS)

[EFLAGS:LPO] **LPO - Last Performed Operation, this is what sets a flag usually**, but not always
- Working with carry flags isn't recommended

 Zero is considered **positive** in two's complement

##### Additions are only made in base 2, not in a "representation" that is two's complement
##### A representation in base 2 has always ==**two possible interpretations in base 10**!!==
- signed and unsigned , so a negative number or a positive one
- the two interpretations can be the same and **represented in base 2** in the same way (0-127 in a byte) - same in unsigned and signed representation
##### BASE 2 - Representation (in the computer), NOT Interpretation
##### BASE 10 - Interpretations 



