bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 10
    b db 5
    c db 3
    d db 20
    res resb 1

; (a-b-b-c)+(a-c-c-d)
segment code use32 class=code
    start:
        ; AL = a-b-b-c, BL=a-c-c-d
        mov AL, [a] ; again, no need to use byte[a] since everyone is 1 byte
        sub AL, [b]
        sub AL, [b] 
        sub AL, [c] 
        
        mov BL, [a]
        sub BL, [c]
        sub BL, [c]
        sub BL, [d]
        
        add AL, BL
        mov [res], AL
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
