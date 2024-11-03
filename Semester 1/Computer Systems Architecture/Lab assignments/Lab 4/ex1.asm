bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dw 1101011100100011b
    b db 00110101b
    c dd 0

; Given the word A and the byte B, compute the doubleword C as follows:
; the bits 0-3 of C are the same as the bits 6-9 of A
; the bits 4-5 of C have the value 1
; the bits 6-7 of C are the same as the bits 1-2 of B
; the bits 8-23 of C are the same as the bits of A
; the bits 24-31 of C are the same as the bits of B

; here C should be at the end  0011 0101 1101 0111 0010 0011 1011 1100, and it is
segment code use32 class=code
    start:
        mov ebx, 0 ; result (C) will 
           
        mov eax, 0 
        mov ax, word[a] ;ax = a so eax = a
        and ax, 0x03C0 ; isolate bits 6-9 of A, so now AX = 0 in bits 0-5 and 10-15, but on bits 6-9 are the bits of A
        ; and the rest of the bytes of eax are 0, so it's good
        ; now since EAX has the bits 6-9 of A on the same positions, rotate them 6 positions to the right
        ; to make them bits 0-3 of EAX, then or them with C to make them the bits 0-3 of C
        mov cl, 6
        ror eax, cl 
        or dword[c], eax ; now C has bits 6-9 of A
        
        or dword[c], 0x00000030 ; or the dword c with a dword that only has bits 4-5 set (second hexadecimal is 0011 (bits 4-7)
        
        mov eax, 0
        mov al, byte[b] ; al = b, so eax = b
        and al, 00000110b ; isolate bits 1-2 of B in al, and the rest of eax bits are 0
        ; rotate them 5 positions to the left to make them bits 6-7 of AL, so of EAX too in this case
        mov cl, 5
        rol eax, cl
        or dword[c], eax ;or them with c and that makes bits 6-7 of C the same as bits 6-7 of eax (bits 1-2 of B)
        ; because all the unset bits in C are 0 
        
        ;to put all the bits of A in the bits 8-23 of C, put the bits of A in eax, so we can shift them to the left
        ; even if A is a word
        mov eax, 0
        mov ax, word[a]
        ; now eax = a, in bits 0-15 is A, rotate them to the left 8 positions to make them bits 8-23 of EAX, then or them with C
        mov cl, 8
        rol eax, cl
        or dword[c], eax
        
        ;same principle for B, make eax 0, put it in AL, they're bits 0-7, shift them left 24 positions to make them bits 24-31
        ; of EAX, then or with c to put bits 24-31 of eax in bits 24-31 of C, which are the bits of A
        mov eax, 0
        mov al, byte[b]
        mov cl, 24
        rol eax, cl
        or dword[c], eax
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
