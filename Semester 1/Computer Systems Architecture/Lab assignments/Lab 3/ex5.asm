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
    b db 0x9
    c dw 0x100
    e dd 0x10000
    x dq 0x100000000
    r resq 1

; (a-b+c*128)/(a+b)+e-x; a,b-byte; c-word; e-doubleword; x-qword - unsigned = FF FF FF FF 00 01 0C CC
segment code use32 class=code
    start:
        ; do c*128 first, c is a word, so 128 should be a word too
        ; word*word -> dword: AX*mem8 -> DX:AX
        mov AX, 128 ; AX = 128 which is a word
        mul word[c] ; DX:AX = 128*c
        ; basically we just make a a word to add to AX, making it a word and adding it to AX is enough 
        ; because a is a byte normally, so it fits well in a word and can add to AX with no worry for bits being lost
        ; and we don't concern with DX
        mov bx, 0
        mov bl, byte[a] ; bx = 00a
        add ax, bx ; ax = ax+a, so dx:ax = c*128+a, now subtract b
        ;b is also a byte, so apply the same logic
        mov bx, 0
        mov bl, byte[b]
        sub ax, bx ; ax = ax-bx, so dx:ax = a-b+c*128
        
        ;now do a+b in BX and divide dx:ax by it
        mov bh, 0
        mov bl, byte[a]
        add bl, byte[b] ; bl =a+b
        adc bh, 0 ;add with carry if the addition doesn't fit on BL, so BX=a+b
        
        div bx ; dx:ax / bx -> result in AX, remainder in DX, so AX = (a-b+c*128)/(a+b)
        
        ;make ax a dword to add e to it
        mov bx, ax ; save ax temporarily in bx
        mov eax, 0
        mov ax, bx ; now eax = 0000ax
        add eax, dword[e] ; eax = (a-b+c*128)/(a+b)+e
        mov edx, 0 
        adc edx, 0 ; carry from eax+e, maybe, so now edx+e is in EDX:EAX
        
        ; thus it is now a qword, subtract x from it
        sub eax, dword[x]
        sbb edx, dword[x+4]
        
        mov [r], eax
        mov [r+4], edx ; edx:eax at location r
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
