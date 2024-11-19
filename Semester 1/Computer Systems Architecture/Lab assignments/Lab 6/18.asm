bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
   sir DD 12AB5678h, 1256ABCDh, 12344344h 
   s_len equ ($-sir)/4
   d times s_len dd 0

; 18. A string of doublewords is given. Order in increasing order the string of the high words (most significant) from these doublewords. The low words (least significant) remain unchanged.
; what I will do is only sort the high words, put them in d
; but sorting the higher words is actually sorting the whole numbers, because then the lower word doesn't matter
; then, go in normal order through sir, and put them at the lower words in d
segment code use32 class=code
    start:
        mov esi, sir
        mov edi, d
        mov ecx, s_len
        CLD ; go through sir in ascending order, DF = 0
        moveToD: ; put sir in d first, then sort it there
            movsd ; move from ESI to EDI, then esi+=4, edi+=4, basically putting the string at ESI in EDI        
        loop orderIncreasing
        
        ; ecx will be 0 ONLY IF the string d is sorted, thus exiting the main loop!
        notSorted:
            mov esi, d
            mov edi, d 
            ; so the destination and source are the same, thus swapping elements successfully at the same loc.
            ; example: 4 3 2, we are at offset 0, so swap 4 and 3 in the same source as destination
            ; becomes 3 4 2, then when we go offset+4 -> 4 2, because the source string gets changed!
            ; so the swap was made in the destination that is actually the source
            mov edx, 1 ; remains 1 if no swapping, so it's sorted
            mov ecx, s_len-1 ;compare current with next element, so iterate only to the second to last element
            orderIncreasing:
                lodsd ; load from esi into eax, esi+=4
                mov ebx, eax ; eax = ebx
                lodsd ; again, the next element after it, in eax
                ;thing is, now esi is after two elements, but we need it at esi+4 so we compare esi+4 with esi+8 next
                ; but now it's at esi+8, so subtract 4 from it
                sub esi, 4
                
                ; if ebx > eax, swap them 
                cmp ebx, eax ; since we compare "high words", basically the whole numbers as they are in hexa
                ; we can assume they are UNSIGNED
                
                JBE notSwap ; if EBX<=EAX (below or equal), don't swap them, so go in the loop after the swapping
                
                ; we are swapping, so put 2 in EDX to put after the end in ECX to contineu running the main loop
                mov EDX, 2
                
                ; how do we swap them? so we had compared [esi] and [esi+4], now esi is esi+8
                ; so if we swap them put them in the destination edi=esi, and at edi+4, but in reverse order
                
                stosd ; put eax ([esi+4]) in edi
                mov EAX, EBX
                stosd; put eax ( first [esi] in EBX) in edi+4
                ;now, edi is after two elements, but we want to compare the next one with the one after two elems
                ;so subtract 4 from it to go back one element in the string
                sub edi, 4
                jmp endOfLoop ; go to the end of loop so the not swapping doesn't occur
                
                notSwap: ; if we don't swap them, do nothing, just increment EDI with 4 to go to the next element
                add edi, 4               
                
                endOfLoop:
                
            loop orderIncreasing
            mov ECX, EDX ; 2 if did swapping, 1 if not swapping, so sorted => exit the loop (do 1-1=0 so exit it)
        loop notSorted
        
        ;now that sir is sorted in the string d, store the lower words of sir in the lower words of d
        ; in the same order as in the initial sir, BUT the higher words in d will ofc remain sorted as they are ascendingly
        mov esi, sir ; take lower words from sir
        mov edi, d ; we do the swapping of lower words in d
        mov ecx, s_len
        
        swapLowerWords:
            lodsd ; put current element of sir in EAX, take the lower word from it
            and EAX, 0x0000FFFF ;basically make the higher word 0, and the lower word remains the same
            ; bits 1 and 1 remain the same, 0 and 1 from eax and the dword 0000FFFF remain 0 as in EAX
            mov EBX, dword[edi] ; take the dword from d too, because we have to work with it, put it in EBX
            and EBX, 0xFFFF0000 ; the same way as above, isolate the higher word from EBX
            or EAX, EBX ; now merge them, and EAX will have the higher part of [edi] and the lower part of [esi
            stosd ;store EAX at [edi], edi+=4 to go to the next element to do this for
            
        loop swapLowerWords
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
