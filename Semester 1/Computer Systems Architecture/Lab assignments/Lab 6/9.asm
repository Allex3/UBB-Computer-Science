bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
     s DD 12345678h, 1A2C3C4Dh, 98FCDD76h, 12783A2Bh
     len_s equ ($-s)/4
     d resd 1 ; at the end it should be FF3A3C56h

;9. A list of doublewords is given. Starting from the low part of the doubleword, obtain the doubleword made of the high even bytes of the low words of each doubleword from the given list. If there are not enough bytes, the remaining bytes of the doubleword will be filled with the byte FFh.
segment code use32 class=code
    start:
        mov ECX, len_s ; length of the source string in ECX for the loop
        mov ESI, s ; offset of the source string in ESI  
        mov EDI, d ; offset of the destination "string" in EDI, a doubleword
        ; but fill d one byte at a time, so it's actually a string of 4 words
        CLD ;ascending order
        JECXZ endOfProgram
        evenBytes:
            ; for each dword from s, obtain the higher byte of the lower word
            LODSD ; load DS:ESI in EAX (the current dword we check from s), and ESI=ESI+4 (go to the next dword)
            SHR AX, 8 ; AX has the lower word of s[esi], get the higher byte of this word
            ;by shifting 8 bits to the right, so AL now is the higher part of EAX
            ; (or MOV AL, AH)
            test AL, 1 ;will set ZF=1 if number is even, or ZF=0 if number is odd
            ;basically if it is 1, ZF=0, if 0 ZF=1
            JNE notAdded
            ;if added, execute here
            STOSB ; store the byte AL into EDI, then EDI+=1, sucessfully putting it into d
            ; from lower to higher bytes, because of little-endian
            
            
            notAdded: ; jump here without adding to d, because the byte isn't even
            
        loop evenBytes
        
        ;if at the end of the loop, d is not filled, fill the rest with FF
        ; if d is filled (i.e d, d+1, d+2, d+3), then EDI-d will be 4 (because of incrementing after adding at d+3 the byte, now EDI=d+4, go to the end
        mov eax, EDI
        sub eax, d ; eax = EDI-d, compare it with 4
        cmp eax, 4 ; if zero, then jump to end, otherwise loop through the remaining value
        ; that is 4-(EDI-d) remaining bytes at location d to be filled with FF
        JE endOfProgram
        ; not zero, remain here
        mov ECX, 4
        sub ECX, EAX ; ECX = 4 - (EDI-d)
        JECXZ endOfProgram
        addRemaining:
            mov AL, 0xFF
            STOSB ; store AL in EDI, EDI+=1, thus filling the remaining high bytes of d with FF
        loop addRemaining
        
        endOfProgram:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
