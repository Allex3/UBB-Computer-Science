bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s db 0x51, 0x72, 0x03, 0x70, 0x71, 0x06, 0x03, 0x70, 0x16
    s_len equ ($-s)
    subs db 0x03, 0x70 
    subs_len equ ($-subs)
    d times s_len db 0 ; destination string
    currentIndex dd 0
    
    
; 28. Being given a string of bytes and a substring of this string, eliminate all occurrences of this substring from the initial string.
segment code use32 class=code
    start:
        mov esi, s
        mov ecx, s_len
        mov edi, d
        cld
        jecxz endOfProgram
        removeSubString:
            ; at each position, check if the current string of length of subs os subs
            mov [currentIndex], esi ; save currentindex in memory
            
            mov edx, esi ; save the current source index in edx to iterate through it and current ecx in EBX
            mov ebx, ecx
            mov esi, subs ;position of subs, iterate it's length
            mov ecx, subs_len
            ;and iterate through edx in the s string and compare it with esi in the subs string
            
            checkSubstring:
                lodsb ; load from esi the current byte of the substring, esi++ in subs
                cmp al, byte[edx] ; compare subs[0] with s[i], and go forward like this                           
                jne notEqualSubs;if they're NOT equal, jump outside of loop and add the current element as normal to d, because the substring is not equal       
                inc edx ; edx++ to go to the next element of s to compare it with subs[1], and so on
                
            loop checkSubstring
            ; if we exited the loop, that means ALL OF THEM are equal, so run the next set of instructions
            
            mov esi, edx ; edx is the index of s, but skipped after all the elements of subs, put it in main esi
            ; skipped over subs_len elements, so the main iterator gets decremented by subs_len
            mov ecx, ebx
            sub ecx, subs_len
            inc ecx ; because after subtracting the substring we now ignore from ecx, it's at the good index we should be at in the NEXT iteration, the one after the substring, so increment it by 1 
            ; becuase oherwise it will miss one element from the end of the string, and so on with every deleting of the substring
            jecxz endOfProgram ; if ecx becomes 0 before exiting the loop (case when the substring is the last substring of the string)
            jmp endOfLoop
            
            notEqualSubs:
                mov esi, [currentIndex]; restore current index of s and add it to d as normal
                movsb ; [edi] = [esi], edi++, esi++, basically put the current element in the dest. string
                mov ecx, ebx ; put only one element, so get back the iterator of the main loop   
                jmp endOfLoop         
                            
                
             endOfLoop:
        loop removeSubString
        endOfProgram:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
