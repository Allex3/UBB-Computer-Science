##### Despite the fact there are 32 bits, only 9 flags (bits) of it are used
-  flag - indicator on 1 bit

### CF - Transport (Carry) flag
- if CF = 1 -> **OVERFLOW**, not correct from a mathematical point of view
- To use it: move the value of the operation in a bigger data type and move the CF in the higher part of that word, if we go from a byte for example

	ADC op1, op2 -> op1 = op1+op2+CF - use the CF from LPO in the next addition, so we don't lose it
	ADD op1, op2 -> op1 = op1 + op2
		For example, if we have a **CF from a byte**, we should use ADC op1, op2 where op1 and op2 are **WORDS**, so the CF is efficiently used
#### Example:
  10010011+
  01110011
  --------
**1**|00000110 -> doing it on paper, its 100000110
But in the processor, it's 00000110, it is an overflow, and the **1** is in the **CF = Transport flag** = 1
###### Only addition of two values is allowed, because otherwise the transport digit could be > 1, which cannot be represented in base 2
##### **LPO** - Last Performed Operation 
###### 1. Flags that are an affect of LPO: 
- ==CF==, PF, AF, ZF, SF, OF
###### 2. Flags that have a future effect, set by the programmer:
- TF, IF, DF, ==CF== 

>[!INFO] CF is part of both categories! Can also be set by the programmer by instructions

##### PF - Parity flag - NOT important for course
- For the example above, the PF = 1 - is added to obtain an odd number of 1's
##### AF - Auxiliary flag - NOT important for course
 - shows the transport digit from bit 3 to bit 4 from LPO's result
 - boundary between the two halves (nibbles) of a byte - because 4 bits = 1 hexadecimal digit:
```
the above addition is:
  93h+
  73h
-----
1|06 - AF shows the transport bit in base 16
```

### ZF - Zero flag - If the result of LPO was zero
- Zero is considered **positive** in two's complement
- ZF  = 1 - true, the last performed operation gave 0
- ZF = 0 - LPO != 0, in our example above it's 6, not 0, so ZF = 0

### SF - Sign Flag - If the result of LPO negative
- Basically, it just **takes the sign bit of the LPO's result**
- From our example, **SF = 0**, the 8th bit here is 0, so the result is unsigned, but not mathematically accurate
##### TF - Trap flag - If set to 1 = stop after every instruction - debugging manner - NOT important for course
- Very dangerous, used for writing debuggers
- only flag **NOT** set by LPO - but by the programmer

### IF - Interrupt flag - NOT important for course
- used in the interrupt system - **working directly with the CPU**, but **can't use it in bits32,** here you have to communicate with **the OS**
- **Time critical section** if **IF = 0** -> DO NOT/CANNOT interrupt the currently running program
- Eventually set to **IF = 1**, this section between setting IF=0 until it becomes 1 again, is called the **TIME CRITICAL SECTION**

### DF - Direction flag - Set direction of arrays
- Any array can be parsed in two ways:
	- From the beginning, or from the end
- The value of the **DF Decides the direction of parsing the array (consecutive memory section from ASM point of view)
- ##### DF = 1 -> traversed in descending order, DF = 0 -> traversed in ascending (normal) order

## OF - Overflow Flag - If LPO not fit in reserved memory space, OF = 1 ; else OF = 0 -> everything worked perfectly - MOST IMPORTANT FLAG != CF

- Representation of value inside the computer - base 2
- To get to base 10, **ALWAYS go through base 16: 2 -> 16 -> 10**
	- From the previous example, 147+115=262, but in the computer we get 06h = 6, not the correct result, which is 106h in base 16, the **1** is in the **CF** 

==OF== Shows us that the space cannot fit the LPO

A **representation** in base 2 has always ==**two possible interpretations in base 10**!!==

In the previous example, if we consider the numbers signed we'd have:
```
-109+
 115
 ---
   6
```
Here, the result is CORRECT in unsigned representation, so **OF = 0**, but **CF = 1**

>[!WARNING] How does the computer know to consider LPO signed or unsigned? **IT CONSIDERS BOTH AT THE SAME TIME**, ==OF== is for the signed, but ==CF== is for the unsigned representation
##### Example: DIV/IDIV or MUL/IMUL, you choose what to use:
- MUL - unsigned - use CF
- IMUL - signed - use OF

>[!WARNING] **CF** is always set if there's a digit outside the LPO's allocated memory

>[!INFO] If result is part of the values that are admissible in the signed interpretation, thus being a CORRECT result in the signed representation, **OF is set accordingly to 0**
>Only two situations in which OF = 1:
>	1. Positive + positive -> the highest 0+0 = 1
>		0....+.0..... = 1.......
>		a. **unsigned** -> it's alright, CF = 0, no bit outside, and OF = 0
>		b. if **signed** -> OF = 1, because the highest 1 is the sign bit, so in this case the addition of two positive numbers is a negative number, but CF = 0
>	2. 1....+1.... = 0..... 
>		a. **unsigned** -> CF depends, OF  = 0, unsigned
>		b. **signed** -> OF = 1

>[!WARNING] CF AFFECTS ONLY AN UNSIGNED OPERATION, WHILE OF ONLY A SIGNED OPERATION

# Instructions to modify the flags

```nasm
IF -> CLI - IF = 0
	  STI - IF = 1
DF -> CLD - DF = 0
	  STD - DF = 1
CF -> CLC - CF = 0
	  STC - CF = 1
	  CMC - CF = !CF
```




>[!QUESTION] aa



