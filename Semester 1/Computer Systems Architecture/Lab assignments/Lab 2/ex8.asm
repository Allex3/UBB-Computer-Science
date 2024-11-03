bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 5
    b db 2
    c db 15
    d dw 291 
    res resw 1

; (10*a-5*b)+(d-5*c) = in this example 256 = 0x0100
segment code use32 class=code
    start:
        mov AL, 10
        mul byte[a] ; AX = 10*a, but it in BX
        mov BX, AX
        
        mov AL, 5
        mul byte[b] ; AX = 5*b
        sub BX, AX ; BX=10*a-5*b, leave it alone, work with CX
        
        mov AL, 5
        mul byte[c] ; AX = 5*c
        sub AX, [d] ;d is a word, so subtract it from AX: AX=5*c-d, now negate it
        neg AX ;AX = d-5*c
        
        add AX, BX ; (10*a-5*b)+(d-5*c)
        
        mov [res], AX
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
