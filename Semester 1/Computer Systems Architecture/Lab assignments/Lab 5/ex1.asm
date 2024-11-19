bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    S db 1, 2, 4, 6, 10, 20, 25 ;string of bytes S
    l equ $-S ; length of S
    D times (l-1) db 0 ; initialize l bytes that are 0, that is the string D

; 9. A byte string S of length l is given. Obtain the string D of length l-1 so that the elements of D represent the difference between every two consecutive elements of S.
segment code use32 class=code
    start:
        mov ecx, l-1 ; put the length of the string-1 in ecx to loop through  - the last element
        ; because we need S[i+1]-S[i], so stop at second to last element
        mov esi, 0 ; index to increment to loop through S and D at the same time
        jecxz endOfProgram ; if ecx is 0, don't start looping, go to the endOfProgram
        ; so situations like 0-1 = FFFFFFFF is avoided to run 2^32-1 times
        differenceLoop:
            ; do the differences as such : S[i+1]-S[i] and put it in D[i]
            ;run the loop until the second to last element of S, so l-1 in ecx
            mov al, [S+esi+1] ; al = S[i+1]
            sub al, [S+esi] ; AL = S[i+1] - S[i]
            mov byte[D+esi], al ; D[i] = S[i+1]-S[i]
            inc esi ;i++
        loop differenceLoop
          
        endOfProgram: ; end of program
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
