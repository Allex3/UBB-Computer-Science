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
    b db 3
    c db 5
    d db 11
    res resb 1

; (d+d-b)+(c-a)+d, store: d+d-b = AL, c-a = BL, result in AL 
segment code use32 class=code
    start:
        mov AL, [d]
        add AL, AL ;d+d
        sub AL, byte[b] ;d+d-b (the byte[var] is unnecessary since all the variables and the registers
        ; used in this program store only bytes, so when working with AL, it takes only a byte from the memory location
        
        mov BL, [c]
        sub BL, [a] ; BL=c-a
        
        add AL, BL ; d+d-b + c-a
        add AL, [d] ; (d+d-b)+(c-a)+d
        
        mov [res], AL ; res has the result
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
