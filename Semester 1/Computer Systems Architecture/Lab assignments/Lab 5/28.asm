bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s1 db '+', '4', '2', 'a', '8', '4', 'X', '5'
    lens1 equ $-s1
    s2 db 'a', '4', '5'
    lens2 equ $-s2
    d times (lens1+lens2) db 0
    

   
; Two character strings S1 and S2 are given. Obtain the string D by concatenating the elements found on the positions multiple of 3 from S1 and the elements of S2 in reverse order.
segment code use32 class=code
    start:
        mov esi, s1
        mov edi, d
        mov ecx, lens1 ; run the loop for all the elems in s1
        cld
        mov DX, 0 ;start at position 0 in lens1, see if this position DX is a multiple of 3
        
        jecxz endOfProgram
        s1MultiplesOf3:
            mov BL, 3
            mov AX, DX ;bring the index to AX for the division
            inc DX
            
            div BL ;AX/BL=AX/3 => remainder in AH, if it's not 0 jump
            cmp AH, 0
            jnz dontAdd
            
            ; if we remained here, it's a multiple of 3
            movsb ; s1[esi] in d[edi], esi++, edi++
            jmp endOfs1MultiplesOf3
            
            dontAdd:
            ; if we jumped to the end, increment esi without storing it in edi
                inc esi
        
            endOfs1MultiplesOf3:
        loop s1MultiplesOf3
        
        mov esi, s2+lens2-1 ;both constants so addition works, reverse order start from last elem
        mov ecx, lens2
        jecxz endOfProgram
        s2Inversed:
            mov al, byte[esi]
            mov [edi], al
            inc edi
            dec esi
            
        loop s2Inversed
        
        endOfProgram:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
