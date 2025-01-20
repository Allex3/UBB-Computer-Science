bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf           ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import scanf msvcrt.dll
import printf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dd 0
    b dd 0
    k dd 0xA
    format db "%d", 0
    result resq 0

; 24. Two numbers a and b are given. Compute the expression value: (a/b)*k, where k is a constant value defined in data segment. Display the expression value (in base 2).
segment code use32 class=code
    start:
        push dword a
        push dword format
        call [scanf]
        add esp, 4*2
        
        push dword b
        push dword format
        call [scanf]
        add esp, 4*2
        
        mov eax, [a]
        cdq ; eax -> edx:eax
        idiv dword[b] ; EDX:EAX/[b] -> a/b, result in EAX
        
        imul dword[k] ; EDX:EAX = EAX*k = (a/b)*k
        mov [result], eax
        ; assume the result will fit on a dword, hopefully
        
        push dword[result]
        push dword format
        call [printf]
        add esp, 4*2
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
