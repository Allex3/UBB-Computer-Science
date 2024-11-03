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
    b db -0x9
    c dw -0x100
    e dd 0x10000
    x dq 0x100000000
    r resq 1

; (a-b+c*128)/(a+b)+e-x; a,b-byte; c-word; e-doubleword; x-qword - unsigned = FF FF FF FF 00 01 0C CC
segment code use32 class=code
    start:
        ; do c*128 first, c is a word, so 128 should be a word too
        ; word*word -> dword: AX*mem8 -> DX:AX
        mov AX, 128 ; AX = 128 which is a word
        imul word[c] ; DX:AX = 128*c
        mov BX, AX ; BX= AX = c*128, to make DX:AX -> DX:BX, AX is used for conversions
        ; basically we just make a a word to add to BX, making it a word and adding it to BX is enough 
        ; because a is a byte normally, so it fits well in a word and can add to BX with no worry for bits being lost
        ; and we don't concern with DX (from DX:BX)
        mov al, byte[a]
        cbw ; AL -> AX = a
        add bx, ax ; bx = bx+a, so dx:bx = c*128+a, now subtract b
        
        ;b is also a byte, so apply the same logic
        mov al, byte[b]
        cbw ; AL -> AX = b
        sub bx, ax ; ax = bx-b, so dx:bx = a-b+c*128
        
        mov AX, BX ; DX:BX -> DX:AX, to use it for division
        
        ;now do a+b in BX and divide dx:ax to it
        mov bl, byte[a]
        add bl, byte[b] ; bl =a+b
        ; make bl a word, bl -> bx, so put it in AL first to convert it in signed repres.
        mov CX, AX ; save AX in CX to return later
        mov AL, BL
        cbw ; AL-> AX = a+b
        mov BX, AX ; BX = a+b signed conversion
        mov AX, CX
        
        idiv bx ; dx:ax / bx -> result in AX, remainder in DX, so AX = (a-b+c*128)/(a+b)
        
        ;make ax a dword to add e to it
        cwde ; AX -> EAX
        add eax, dword[e] ; eax = (a-b+c*128)/(a+b)+e
        cdq ; eax -> edx:eax
        
        ; thus it is now a qword, subtract x from it
        sub eax, dword[x]
        sbb edx, dword[x+4]
        
        mov [r], eax
        mov [r+4], edx ; edx:eax at location r
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
