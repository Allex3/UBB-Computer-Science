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
    b db 8
    c db 8
    d dw 300
    res resd 1 ; reserve 1 double word for the result (DX:AX, pop them here)
    
    

; 3*[20*(b-a+2)-10*c]+2*(d-3)
segment code use32 class=code
    start:
        ; the byte operations: AX = AL*bytevar; word: DX:AX = AX * wordvar (d)
        ;b-a+2 in AL, 20 in BL
        mov AL, [b]
        sub AL, [a]
        add AL, 2
        mov BL, 20
        mul BL ; result in AX, AX=(b-a+2)*20
        ; move it to BX
        mov BX, AX
        ; do 10*c, 10 in AL, mul [c]
        mov AL, 10
        mul byte[c] ; AX = 10*c
        ; now BX = BX-AX = 20*(b-a+2)-10*c 
        sub BX, AX
        
        ; now we have to do 3*BX+2*(d-3)
        mov AX, 3
        mul BX ;DX:AX = AX*BX
        
        ; put DX:AX in ECX, basically ECX = 3*[20*(b-a+2)-10*c] now
        ; then do 2*(d-3), d is a word, so result in DX:AX, save it in EAX, then do add EAX, ECX, final result in EAX
        ; then move it to the double word res in memory
        push DX
        push AX
        pop ECX ; ECX = DX:AX, don't have to worry about the other registers now so use them
        
        mov AX, [d]
        sub AX, 3 ; AX=d-3
        mov BX, 2
        mul BX ; DX:AX = AX*BX = (d-3)*2
        
        push DX
        push AX
        pop EAX
        
        add EAX, ECX
        
        mov [res], EAX
        
        
        
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
