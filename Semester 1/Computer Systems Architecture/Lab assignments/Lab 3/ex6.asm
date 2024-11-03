bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dd 0x10000
    b db 0x10
    c db 0xA
    d db 0x12
    x dq 0x100
    r resd 1

;a-(7+x)/(b*b-c/d+2); a-doubleword; b,c,d-byte; x-qword, unsigned
segment code use32 class=code
    start:
        ; do b*b-c in AX
        mov AL, byte[b]
        mul byte[b] ; AX=AL*b=b*b
        mov BX, AX ; BX =b*b
        
        mov AL, byte[c]
        mov AH, 0 ; AL->AX unsigned conversion
        div byte[d] ; AL = AX/d = c/d unsigned division
        mov AH, 0 ; AL->AX
        sub BX, AX; BX=b*b-c/d
        
        add BX, 2; BX = (b*b-c/d+2)
        
        ;now compute the left part of the main division, i.e. a-(7+x)
        ;7+x will be a qword, so make a a qword, it's now a dword, put it in EAX 
        mov EAX, dword[a]
        mov EDX, 0 ; EAX -> EDX:EAX unsigned conversion
        add dword[x], 7; x=7+x now, basically add to the lowest 4 bytes, but 7 is a byte, so it works in 32bit assembly
        sub EAX, [x] ; lower 4 bytes of x
        sbb EDX, [x+4]; higher 4 bytes of x (little endian)
        ;now EDX:EAX has a-(7+x)
        
        ;now do the main division a-(7+x)/(b*b-c/d+2) = EDX:EAX/BX, but convert BX to EBX
        push dword 0
        push BX
        pop EBX ; BX->EBX (in stack: 0000 0000, then 0000 0000 BX, and the current stack positions only takes a dword
        ; so it will POP the last 8 bytes, thus 0000 BX
        
        div EBX ; EDX:EAX / EBX -> EAX, so a-(7+x)/(b*b-c/d+2) is in EAX
        
        mov [r], EAX
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
