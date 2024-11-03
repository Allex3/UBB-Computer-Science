bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 10
    b db 200 ;this way [(a-d)+b]*2 will be a word, but byte*2 = byte*byte = word in AX anywayy
    c db 3 ;c is a byte, but make it a word for division
    d db 8
    res resw 2
    

;[(a-d)+b]*2/c = 404/3 = 134, r=2
segment code use32 class=code
    start:
        mov AL, [a]
        sub AL, [d] ;a-d
        add AL, [b] ;a-d+b
        mov BL, 2
        mul BL ; AX=AL*BL = [(a-d)+b]*2
        
        mov DX, 0 ;DX:AX = [(a-d)+b]*2 now
        mov BL, [c]
        mov BH, 0 ; now BX=BH:BL = c, at the lower byte because c is only a byte, to do the division dword/word instead of word/byte
        div BX ;AX = DX:AX/BX, remainder in DX
        
        mov [res], AX ;2 bytes for the quotient
        mov [res+2], DX ;these two bytes (a word) for the remainder
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
