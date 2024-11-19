bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s dd 0110b, 00110110101b, 10101b, 11b, 1110b
    len_s equ ($-s)/4
    d times len_s dd 0

; 24. Being given a string of doublewors, build another string of doublewords which will include only the doublewords from the given string which have an even number of bits with the value 1.
segment code use32 class=code
    start:
        mov ESI, s
        mov EDI, d
        mov ECX, len_s
        CLD ; ascending order for s
        JECXZ endOfProgram
        buildEvenString:
            LODSD ; load dd from esi into EAX, esi+=4 to go to the next element of the string
            ;since PF is set only if the least significant byte of a dword has even number of bits set, and we need to count all the bits to see, we cannot count with PF
            ; so just iterate through each bit :') 
            mov EBX, ECX ; save current ECX
            push EAX ; put eax on the stack to pop it back after counting its bits
            mov ECX, 32 ; run the loop for all the bits that could be set of EAX
            mov EDX, 0 ; count the bits set
            countBits:
                test EAX, 1 ; if 1, least significatn bit set, 0 then it's 0, so don't count it
                JZ notAdd ; jump to end if 0, don't add it
                inc EDX ; edx++, add the bit
                notAdd:
                shr eax, 1; go 1 bit to the right to check the next bit (i.e. put it in the least significant position to test it with 1)
                cmp EAX, 0 
                JE outOfLoop ;eax = 0, get out of the loop, no more bits to check!
            loop countBits
            
            outOfLoop:
            pop EAX
            mov ECX, EBX ; put the old ECX back 
            test EDX, 1 ; if EDX has the least significant bit set, then the count of bits in EAX is odd, otherwise it's even
            JNZ endOfLoop ; jump to the end of loop if the count is odd, otherwise add it
            STOSD ; store the dword from eax into memory at d, then EDI+=4, go to the next offset in d where you should put the next value, if there will be another
            endOfLoop:
        loop buildEvenString
  
        endOfProgram:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
