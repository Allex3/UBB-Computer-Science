bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dw 1101011100100011b
    b db 00110101b
    c dd 0

; Given the word A and the byte B, compute the doubleword C as follows:
; the bits 0-3 of C are the same as the bits 6-9 of A
; the bits 4-5 of C have the value 1
; the bits 6-7 of C are the same as the bits 1-2 of B
; the bits 8-23 of C are the same as the bits of A
; the bits 24-31 of C are the same as the bits of B

; here C should be at the end  0011 0101 1101 0111 0010 0011 1011 1100, and it is
segment code use32 class=code
    start:
        mov ecx, 0x00112233
        push ecx
        mov ax, 0x0005
        pop eax
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
