![[x86.png]]
### [[Memory Segments (and addresses)]] -Theory
### Segment registers

What do the registers contain (CS, DS, SS, ES, FS, GP)?
- 16bits: the starting address of the segment is provided
- 32bits: the starting address is NOT provided. **Instead**, the **segment selector** is issued by the OS
on 32 bits, you cannot control the starting point of a segment, only the offset
#### CS - Code segment
#### DS - Data Segment
#### SS - Stack Segment
#### ES - Extra Segment (extra DATA segment)
#### FS -
#### GS - 

### Address register - EIP
