>[!question] what does the assembler do?

```nasm
mov eax, [v]     ; mov eax, dword ptr DS:[00401005]
	- the ... of an offset can be done ..

mov eax, [ebx]   ; mov eax, dword ptr DS:[EBX]
mov eax, [ebp]   ; mov eax, dword ptr SS:[EBP]

mov eax, [ebp*2] ; mov eax, dword ptr SS:[ebp+ebp]

mov eax, [ebp*3] ; mov eax, dword ptr SS:[ebp+ebp*2]
mov eax, [ebp*4] ; mov eax, dword ptr DS:[ebp*4] (it cannot be [ebp+ebp*3])
```

>[!important] WHEN THE ASSEMBLER CAN, IT TRIES TO FORCEFULLY MAKE IT A **BASED** addressing

Further:
```nasm
mov eax, [ebx+esp] ; mov eax, dword ptr SS:[ebx+esp] (esp CANNOT be an index), so esp HAS TO BE THE BASE! esp as base, ebx as index
<=> mov eax, [esp+ebx] ; SS -> ESP as base, EBX as index

mov eax, [ebx+esp*2] ; syntax error [esp+ebx+esp], syntax error, esp cannot be INDEX, but if it is a base one more esp remains, syntax error

mov eax, [ebx+ebp*2] ; DS, ebp as index because of *2, ebx as base

```

**Ambiguity!!!!!**
```nasm
mov eax, [ebx + ebp] ; DS 
Because the assembler has to establish a base, there appears an ambiguity, because it's not clear from EBX+EBP which is the base, both of them can be both a base and index. **SO THE FIRST THING TO ANSWER HERE: THESE SORT OF OPERATIONS LEAD TO AMBIGUITIES**
Because of this ambiguity, the assembler has to resolve it. And the only basis it can do this on is what **YOU WRITE** as a programmer. And thus, because you wrote first EBX, EBX will be taken as a base => DS

mov eax, [ebp + ebx] ; SS
Here the same explanation, thus EBP as a base => SS
```

**NOT ambiguous**
```nasm
mov eax, [ebx*2+ebp] ; SS
EBP as base, because ebx*2, so it HAS to be an index, because it has a SCALE

mov eax, [ebx*1+ebp] ; SS
EBP as base, because EBX*1 because it has a SCALE, NOT ambiguity

```
**More ambiguity: index?**
```nasm
mov eax, [ebx*1+ebp*1] ; SS
ambiguity => ebx*1 found first, so EBX IS AN INDEX!!!
So EBP*1 which is actually EBP must be the base ! 

mov eax, [ebp*1+ebx*1] ;DS
Same principle as above
```

**Tricky:**
```nasm
mov eax, [ebp*1+ebx*2] ; SS
ONLY EBP*1 can be the base, because ebx*2 has a scale with it
So EBX taken as scale, and ebp*1=ebp as base => SS
```

