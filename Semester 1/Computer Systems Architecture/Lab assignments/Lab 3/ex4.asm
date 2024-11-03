bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db -0x1
    b dw 0x100
    c dd 0x10000
    d dq 0x100000000
    r resq 1
    

; (a + b + c) - d + (b - c) signed representation = in my case
segment code use32 class=code
    start:
        mov al, [a] 
        cbw ; al -> ax = a
        add ax, [b] ;ax = a+b
        cwde ; ax -> eax, so eax = a+b, a dword now
        add eax, [c] ;eax = a+b+c
        cdq ; eax -> edx:eax signed conversion, so edx:eax = a+b+c 
        
        sub eax, dword[d] ; 4 lower bytes of d subtracted from the lower 4 bytes of edx:eax, i.e EAX
        sbb edx, dword[d+4] ;4 higher bytes of d from the higher 4 bytes of edx:eax i.e EDX
        ;EDX:EAX = (a + b + c) - d
       
        ;move EDX:EAX to ECX:EBX to work with EDX:EAX again (used in conversions)
        mov EBX, EAX
        mov ECX, EDX
        
        
        mov eax, 0
        mov edx, 0
        
        
        mov ax, word[b] 
        cwde ; ax -> eax = b
        sub eax, dword[c] ; eax = b - c
        cdq ; eax -> edx:eax = b - c, so now the value b-c is represented well in EDX:EAX
        
        add eax, ebx ; EDX:EAX = ECX:EBX + b-c = ECX:EBX + EAX, so add ebx to eax, but also add ecx to edx
        ;but with a carry possible from the addition of eax+ebx
        adc edx, ecx
        
        mov [r], eax
        mov [r+4], edx
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
