bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 2
    d db 16
    e dw 601
    res resw 2
    
; (2*d+e)/a = 633/2 = 316, r=1 in our example, a word
segment code use32 class=code
    start:
        mov AL, 2
        mul byte[d] ; AX = 2*d
        add AX, word[e] ; AX = 2*d+e, a word
        
        ;since dividing 2*d+e by a, a being a byte, the result could be too big to fit into  a byte
        ; becuase e is a word, as shown in my example, so we will load a into a 16bit reg, BX
        mov BL, byte[a] 
        mov BH, 0 ;do it like this, otherwise if mov bx, [a] it will take a and d
        ; put 0 in DX, so DX:AX has 2*d+e, AX already has that
        mov DX, 0
        div BX ; AX = DX:AX/BX = (2*d+e)/a, DX=remainder, and since BX is a word, the remainder can also be a word, not in our case though
        
        mov [res], AX ;first word at res in memory (bytes res and res+1 = AX), reserved two words
        mov [res+2], DX ;second word (from res+2 to res+3, two bytes)
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
