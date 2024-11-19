bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    A db 2, 1, -3, 0
    lenA equ $-A
    B db 4, 5, 7, 6, 2, 1
    lenB equ $-B
    R times (lenA+lenB) db 0 ; allocate lenA+lenB for R which has the elements of B and A in reverse order

; 24. Two byte strings A and B are given. Obtain the string R by concatenating the elements of B in reverse order and the elements of A in reverse order
segment code use32 class=code
    start:
        ; need two loops: one to concatenate the elements of B to R in reverse order
                        ; and the other one to concatenate A in reverse order to R
        ; use ECX to run the loop, and use ECX to also get the elements of B (or A) in reverse order
        ; ECX = lenB -> the last element of B is ECX-1, and it decrements from there
        ; then, last ECX will be 1, and so the first element of B will be ECX-1=1-1=0
        ; before the loop finishes, this is the logic of the program
        ; also, use ESI to iterate through R, incrementing it with 1 after every element added in R
        mov ESI, 0
        
        mov ECX, lenB
        jecxz endBReverseLoop
        BReverseLoop:
            mov al, [B+ECX-1] ; base + index*scale + constant = B+(ECX-1)*1+0
            mov [R+esi], al ; R[esi] = B[ecx-1], elements of B in reverse order since ECX is decremented
            inc esi ; esi++
        loop BReverseLoop
        endBReverseLoop:
        
        mov ECX, lenA
        jecxz endAReverseLoop
        AReverseLoop:
            mov al, [A+ECX-1]
            mov [R+esi], al
            inc esi
        loop AReverseLoop
        endAReverseLoop:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
