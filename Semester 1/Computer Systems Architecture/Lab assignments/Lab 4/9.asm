bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, printf         ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dd 0
    b dd 0
    result dd 0 
    format db "%d", 0

;9. Read two numbers a and b (base 10) from the keyboard and calculate: (a+b)/(a-b). The quotient will be stored in a variable called "result" (defined in the data segment). The values are considered in signed representation.
segment code use32 class=code
    start:
        push dword a
        push dword format
        call [scanf]
        add esp, 4*2 ; read a
        
        push dword b
        push dword format 
        call [scanf]
        add esp, 4*2 ; read b
        
        mov eax, [a]
        add eax, [b] ; eax = a+b
        
        mov ebx, [a]
        sub ebx, [b] ; ebx = a - b
        
        cdq ; EAX -> EDX:EAX signed conversion, EDX:EAX = a+b
        idiv ebx ; EDX:EAX/EBX -> quotient in EAX = (a+b)/(a-b)
        
        mov [result], eax ; result 
        
        push dword [result]
        push dword format
        call [printf]
        add esp, 4*2
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
