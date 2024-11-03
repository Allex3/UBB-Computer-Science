bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dw 500
    b dw 5
    c dw 3
    d dw 20
    res resw 1

;a-d+b+b+c
segment code use32 class=code
    start:
        ; all operations in AX - 2 bytes = word size
        mov AX, [a]
        sub AX, [d]
        add AX, [b]
        add AX, [b]
        add AX, [c]
        
        mov [res], AX
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
