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

; a-d+b+b+c signed
segment code use32 class=code
    start:
        ; make a a signed qword
        mov al, [a]
        cbw ;signed conversion from AL to AX (byte to word)
        cwde ;signed conversion from AX to EAX (word to dword)
        cdq ; signed conversion from EAX to EDX:EAX (dword EAX to qword EDX:EAX)
        ; put 1 in EDX when negative, or 0 when positive, in signed interpretation
        ; now EDX:EAX = a, subtract d
        sub EAX, dword[d] ;lower 4 bytes of d
        sbb EDX, dword[d+4] ;highest 4 bytes of d
        ;now EDX:EAX = a-d, put it in ECX:EBX to use EAX for conversion
        mov EBX, EAX ; EDX:EAX = ECX:EBX = a-d
        mov ECX, EDX ;
        
        ; b is a word, make it a dword twice, put it once in EAX to make it a dword, then add EAX to EAX to do b+b
        ; to have b+b in a dword, then add c to it, to have b+b+c in EAX, then make ECX 0 to have it in ECX:EAX
        mov AX, [b]
        cwde ; AX->EAX signed conversion
        add EAX, EAX ; EAX = b+b
        add EAX, dword[c] ; EAX = b+b+c (c is already a dword)
        
        ;now add EAX to ECX:EBX, by adding EAX to EBX, but then it might be a carry in the middle
        ; so add with a carry to ECX a 0
        add EBX, EAX
        adc ECX, 0
        
        mov [r], EBX ; lower 4 bytes
        mov [r+4], ECX ; higher 4 bytes
        
        
        
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
