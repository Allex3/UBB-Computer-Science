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
    b dw 8
    c dd 11
    d dq 100
    r resq 1
    
    

;(d+d-b)+(c-a)+ d = 298 = 0x012A in our example
segment code use32 class=code
    start:
        mov eax, [d]
        mov edx, [d+4]
        mov ebx, [d]
        mov ecx, [d+4]
        add eax, ebx ; add the lower halfs of d together, then add with the carry flag the higher parts
        ; (the CF at the middle, end of addition of lower half part)
        adc edx, ecx
        ; result in EDX:EAX
        ; b is a word, make it a dword so we subtract it from EAX (lower dword part of EDX:EAX)
        ; if we substract it from AX only, risk a CF remaining, and we can't access higher part of EAX
        ; this way no CF
        mov EBX, 0 
        mov BX, [b] ;EBX= 00 00 b
        
        sub EAX, EBX ;eax=eax-b; edx:eax = d+d-b
        
        mov ebx, [d]
        mov ecx, [d+4] ; ECX:EBX = d, add it to EDX:EAX
        add eax, ebx
        adc edx, ecx ; EDX:EAX = (d+d-b)+ d 
        
        ; make a a double word in ebx, make ebx 0 and put it in BL
        mov ebx, 0
        mov bl, [a] ;ebx = 00 00 00 a
        mov ecx, [c] ; ecx = c
        sub ecx, ebx ; ecx = c - a, a was a byte so no need for any carry
        
        add eax, ecx ; eax=eax+ecx, basically add c-a dword to the lower part of EDX:EAX
        ; now maybe a carry at the middle so
        adc edx, 0; only add the carry at the beginning of the higher part if it exists
        
        mov [r], eax 
        mov [r+4], edx ; r = EDX:EAX, inverse in memory
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
