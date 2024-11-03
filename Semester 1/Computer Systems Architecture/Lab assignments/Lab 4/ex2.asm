bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    M dd 0x519F7BC2 ; = 0101 0001 1001 1111 0111 1011 1100 0010
    MNew dd 0

; Given the doubleword M, compute the doubleword MNew as follows:
; the bits 0-3 a of MNew are the same as the bits 5-8 a of M.
; the bits 4-7 a of MNew have the value 1
; the bits 27-31 a of MNew have the value 0
; the bits 8-26 of MNew are the same as the bits 8-26 a of M.

; in our case, MNew should be 0000 0001 1001 1111 0111 1011 1111 1110
segment code use32 class=code
    start:
        mov eax, [M]
        ;isolate bits 5-8 of M
        and eax, 0x000001E0 ; this isolates bits 5-8, basically and them with a dword that has bits 5-8 1    
        ; rotate the now 5-8 bits of M in eax at positions 5-8, 5 positions to the right
        ; to make them bits 0-3 of EAX, then or those bits of MNew, thus putting bits 0-3 of eax in bits 0-3 of Mnew
        mov cl, 5
        ror eax, cl
        or dword[MNew], eax
        
        or dword[MNew], 0x000000F0 ; or them with a dword that has bits 4-7 1, so they are also 1
        ; bits 27-31 of MNew have value 0 already, so don't interfere with them
        ; but if we wanted to make them 0, just use AND Mnew with a dword that has bits 27-31 0
        ; thus making them 0 in any case
        
        ; put M in eax and isolate bits 8-26 of M, and since we want to put them on bits 8-26 of MNew anyway
        ; no need to rotate them, just OR them with MNew
        mov eax, [M]
        and eax, 0x07FFFF00 ; so bits 0-3 and 4-7 are always 0 , and bits 27 and 28-31 too
        ;the rest are 1, to put the bits of EAX there, bits 8-26 of M
        or dword[MNew], eax
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
