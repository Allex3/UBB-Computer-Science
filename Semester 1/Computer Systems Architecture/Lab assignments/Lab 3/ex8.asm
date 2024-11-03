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
    b db -0x10
    c db 0xA
    d db 0x12
    x dq 0x100009999
    r resd 1

;a-(7+x)/(b*b-c/d+2); a-doubleword; b,c,d-byte; x-qword, signed
segment code use32 class=code
    start:
        ; do b*b-c in AX
        mov AL, byte[b]
        imul byte[b] ; AX=AL*b=b*b
        mov BX, AX ; BX =b*b
        
        mov AL, byte[c]
        cbw ; AL->AX signed conversion, now divide it by d 
        idiv byte[d] ; AL = AX/d = c/d signed division
        cbw ; AL->AX signed conversion to subtract it from b*b=BX
        sub BX, AX; BX=b*b-c/d
        
        add BX, 2; BX = (b*b-c/d+2)
        
        ;now compute the left part of the main division, i.e. a-(7+x)
        ;7+x will be a qword, so make a a qword, it's now a dword, put it in EAX and cdq
        mov EAX, dword[a]
        cdq ;EDX:EAX = a signed conversion
        add dword[x], 7; x=7+x now, basically add to the lowest 4 bytes, but 7 is a byte, so it works in 32bit assembly
        sub EAX, [x] ; lower 4 bytes of x
        sbb EDX, [x+4]; higher 4 bytes of x (little endian)
        ;now EDX:EAX has a-(7+x)
        
        ;now do the main division a-(7+x)/(b*b-c/d+2) = EDX:EAX/BX, but convert BX to EBX
        ;because signed conversions use EAX, put EDX:EAX in EDX:ECX temporarily
        mov ECX, EAX; now EDX:EAX = EDX:ECX
        mov AX, BX ;AX=BX = (b*b-c/d+2)
        cwde ; AX->EAX
        
        mov EBX, EAX; now EBX = EAX = (b*b-c/d+2)
      
        mov EAX, ECX ; put EDX:ECX back in EDX:EAX to do the division (implicit operands)
        
        idiv EBX ; EDX:EAX / EBX -> EAX, so a-(7+x)/(b*b-c/d+2) is in EAX
        
        mov [r], EAX
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
