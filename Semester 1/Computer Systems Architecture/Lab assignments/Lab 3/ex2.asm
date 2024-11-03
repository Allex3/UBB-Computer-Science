bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 0x1
    b dw 0x100
    c dd 0x10000
    d dq 0x100000000
    r resq 1

; ((a + b) + (a + c) + (b + c)) - d =  F 00020202 which in two's complement in a qword is FFFFFFFF 00020202 (add 1s to the left)
; because it's signed

segment code use32 class=code
    start:
        mov eax, 0 ; to make sure there are no problems at addition
        mov AL, [a]
        add AX, [b] ; eax = a+b
        mov ebx, 0
        mov bl, [a] ;eax = a (000000a)
        add ebx, [c] ; ebx=a+c, c dword
        add eax, ebx ; eax = a+b + a+c
        
        ; now do b+c in ebx since we don't use it anymore
        ; b word and c dword, so add in a dword, make b a dword
        mov ebx, 0
        mov bx, word[b]
        add ebx, [c] ; ebx = b+c 
        add eax, ebx ;eax = (a+b + a+c + b+c)
        
        ;now do this whole sum - d, which is a qword, so transfer it from eax to edx:eax -> make edx 0
        mov edx, 0
        ; now subtract lower half of d with eax, and higher half with edx with a carry
        sub eax, dword[d] ; in memory it's stored in little endian, so the lowest 4 bytes are at d -> d+3
        sbb edx, dword[d+4] ;and higher parts in d+4 -> d+7
        
        ; result is in edx:eax, move it into areserved qword
        mov [r], eax
        mov [r+4], edx
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
