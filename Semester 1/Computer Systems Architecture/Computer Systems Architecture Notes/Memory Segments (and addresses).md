**Address of a memory location** - no. of consecutive **bytes** from the beginning of the RAM memory and the beginning of that memory location

## Segments

>[!INFO] **Segment** - an uninterrupted sequence of memory locations, used for similar purposes during a program execution = **logical section of a program's memory**
>A **segment** is determined by its
>	---base address (**beginning**) - 32 bits value
>	---limit (**size**) - 32 bits value
>	---type

All architectures must obey the **address specification mechanism**
#### in family of 8086-based processors, the term segment has two meanings:
1. A block of memory of discrete size, called **a physical segment**. The number of bytes in a physical segment is 
	1. 64kb for 16-bit processors - 2^16
	2. 4 gigabytes for 32-bit processors - 2^32
2. A *variable-sized block of memory*, called a **logical segment** occupied by a program's code or data
### [[BIU (Bus Interface Unit) Registers#Segment registers|Segment registers]]

### 16bit vs 32bit programming
- **16bit** -> YOU can control the CPU
- **32bit** -> the OS controls the CPU, you can't
### Offset 
>[!INFO] **Offset** - the address of a location *relative to the beginning of a **segment*** (i.e. the number of bytes between the beginning of that segment and that particular memory location)
>An **offset** is **valid** ONLY IF its numerical value, on 32 bits, doesn't exceed the segment's limit which refers to (e.g. From 0 to 2^32 is a segment, so the offset MUST BE between 0 and 2^32 so the beginning of the segment )

### Address specification

>[!info] **Address specification** - pair of *segment selector* and an *offset*.
>*Segment selector* - a numeric value of 16 bits which selects uniquely the accessed segment and its features. ==A segment selector is defined and provided by the OS==

**To represent the *address specification***:
```nasm
segment:offset
			      32 bits
segment (16 bits) -------> segment selector(16 bits always) (provided by the OS)
				  gfsdfd
				  16 bits
				  -------> the starting address of that segment

Segment             Base address       Limit (size of)
selector          
	8                     51782         
	17                     .
	2732                    .
	17152                 . 
				  
```

What do the registers contain (CS, DS, SS, ES, FS, GP)?
- 16bits: the starting address of the segment is provided
- 32bits: the starting address is NOT provided. **Instead**, the **segment selector** is issued by the OS
on 32 bits, you cannot control the starting point of a segment, only the offset

##### How to compute the linear address corresponding to a specification (HOW THE ADDRESSING SYSTEM WORKS)
- the OS provides the SEGMENT SELECTOR, **NOT** its base address, sadly
- if the **offset is smaller than the limit**,  the OS provides the base address

>[!note] Example: 8:1000h

1.  Checks **if segment 8 was defined by the OS** and blocks the access if such a segment was not defined (memory violation error)
2. It **extracts the base address (B)** and the **segment's limit (L)**. for example, as a result we may have B = 2000h and L = 4000h
3. It verifies **if** the **offset exceeds the segment's limit:** 1000h > 4000h ? If so, then the access would be blocked
4.  It **adds the offset to B** and obtains the **linear address** 3000h (1000h+2000h). This computation is performed by the ==ADR== component from ==BIU==
This kind of addressing is called **SEGMENTATION** (segment:offset) and we are talking about the segmenting address model

**Nowadays, the OS works with the *flat memory model***:
- the memory is seen as something that starts with 0 and the users only work with offsets
- from a **practical** POV, the programmer can't work with the flat memory model, only the OS does

==**paging** - fuck knows==

Both address computing and the use of segmentation and paging are influenced by the execution mode of the processor, the x86 processors  supporting the following more important execution modes:
- *real mode*, on 16 bits (using memory word of 16 bits and having limited memory at 1MiB) -> can access the **interrupt system** - control the kernel
- **protected mode on 16 bits or 32 bits, characterized by using paging and segmentation**

### Types of segments

- **Code segment,** which contains instructions
- **Data segment**, containing data which instructions work on
- **Stack segment**
- **extra segment** - supplementary data segment
Every program is composed of at least one or more of all the above segments
At any given moment during run time, there is at most **one active** segment of any type.

The registers **CS, DS, SS, ES from BIU** contain *the values of the **selector** corresponding to the currently active segment*, corresponding to every type. So registers CS, DS, SS and ES ==determine the starting addresses and the dimension of the 4 active segments: code, data, stack and extra==
**FS and GS** can store selectors pointing to other auxiliary segments without having predetermined meaning.

Because of their use, registers **CS, DS, SS, ES, FS, GS** are called *segment* (or selector) registers

Register **EIP** (which offers also the possibility of accessing its less significant word by referring to the **IP** subregister) contains *the offset of the current instruction* inside the current code segment, this register being managed exclusively by **BIU** (CS:EIP (basically, EIP is the offset of the code segment, which starts at CS -> address (offset of CS) in front of the currently executed instruction in OllyDBG

##### Simplified

poza

#### Types of addresses

**NEAR** - *always inside one of the 4 active segments*: for which only the offset is specified, the segment address being **implicitly taken from a segment register**
**FAR** -  for which programmer EXPLICITLY specifies a segment selector
so a **FAR** address is a ==COMPLETE ADDRESS SPECIFICATION== and it may be specified in one of the 3 following ways:
- s3s2s1s0 : offset_specification where s3s2s1s0 is a constant
- **segment register**: offset_specification, where segment registers are CS, DS, SS, ES, FS or GS
- **FAR `[variable]`** where variable is of type QWORD and contains the 6 bytes representing the FAR address: internal format = at the smallest address is the offset, and at the higher _by 4 bytes_ address (the word followign the current doubleword) **is the word which stores the segment selector**
	- The address representation follows the little-endian representation


### The ways of specifying an operand - 3 ways of expressing an operand in ASM
##### 1. Register mode: if the required operand is a register
`mov eax, 17 <- first operand specified in the register mode`
##### 2. Immediate mode 
`mov eax, 17 <- second operand`
##### 3. Memory addressing mode
###### offset of an operand formula 2 AM FORMULA 
```
offset_address = [base] + [index*scale] + [constant]
```
>[!info] **offset_address** is obtained from the following (maximum) four elements:
> - **base** - one of EAX, EBX, ECX, EDX, EBP, ESI, EDI, ESP
> - **index** - one of EAX, EBX, ECX, EDX, EBP, ESI, EDI (NOT ESP)
> - **scale** to multiply the value of the index register with 1, 2, 4 or 8 (depends on the size of the memory addresses contents we want to pass)
> - the value of a numeric constant, on a byte, word or doubleword
> (square brackets = optionality of elements)

**In NASM, [] -> dereferencing operator**

>[!info] From here results the following modes to access the memory: 
>- ==direct== addressing, when **only the *constant*** is present
>- *based* addressing, if in the computing **one of the base registers is present**
>- *scale-indexed addressing*, if in the computing **one of the index registers is present**

>[!warning] These three mode of addressing could be combined. All of them or only one of them can be present at the same time, but **ONLY ONE OF THEM IS NEEDED** to access the memory
>based + scale-indexed = **indirect addressing**
>direct (constant) = **DIRECT** addressing

>[!note] Examples of the offset_address FORMULA

```nasm
mov eax, [a+7] -> a+7 = 

mov eax, [ebx] -> correct! offset_address = [base] -> based address mode, indirrect addressing, go to ebx memory location and fetch the value from there (4 bytes starting from ebx address (a dword) and put them in eax)
example: ebx = 17152, mov eax, [ebx], go to mem loc. 17152 
memory: F0 56 B2 C3 ... so eax = C3 B2 56 F0


```
==**MOSTTTTT important**==
What is a **variable?** And how does it obey the **2 am formula?**
>[!info] A **variable** is a language element which value is variable - a variable is characterized by its address (which is constant) and it's content (which is variable)
``` BUT THE ADDRESS OF THE VARIABLE IS CONSTANT

v dw 4FC2h -> obeys the formula -> [constant]
the process of allocating


```



