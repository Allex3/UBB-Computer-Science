bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    sir DW 12345, 20778, 4596 
    s_len equ ($-sir)/2
    result times 100 db 0
    intermediary_inverse times 8 db 0
    last_result_loc dd 0
    counter dd 0

; our code starts here
segment code use32 class=code
    start:
        mov esi, sir
        mov dword[last_result_loc], result
        mov ecx, s_len
        cld
        
        digits_loop:
            lodsw ; AX = a word from the string
            mov bx, 10  
            mov [counter], ecx ; save ecx in counter
            mov ecx, 0 ; infinite loop that exits when the word reaches 0 (take each digit of it)
            mov edi, intermediary_inverse ; use this because from a number like 12345 digits will be 5 4 3 2 1
            ; and we want to reverse them in the result
            get_digits:
                mov DX, 0 ; Use DX:AX to divide by 10 so the quotient still fits in AX , and the remainder in DX
                ; so basically AX the current number is successfully divided by 10 and remains still in AX
                ; and DX will be the digit, then DX will be 0 again but we only use a dword here so the result is still in AX and fits, a word
                div bx ; DX:AX/BX -> AX, remainder in DX, which is the last digit of AX
                mov byte[edi], DL ; digit in DL as it is only a byte
                add edi, 1
                
                cmp AX, 0
                JE after_get_digits
            
            loop get_digits
            
            after_get_digits:
            mov edx, edi ; we know that edi is 1 after the last digit in the intermedairy inverse (i.e. 1)
            sub edx, 1 ; now edi is at 5, and if we go in inverse order it will be 1 2 3 4 5, put it this way in result
            mov edi, [last_result_loc] ; where we remained in the result
            
            mov ecx, edx
            sub ecx, intermediary_inverse ; so now it has the number of elements - 1 (edx-starting address)
            ; this happens because it is indexed from 0, so 5 elements would look like 0 1 2 3 4, but its 4-0+1
            inc ecx ; so add 1
            jecxz end_of_file
            put_result:
                mov AL, [edx]
                dec edx ; edx--, so we go to 2 now
                stosb ; [edi] = AL, edi++
                
            loop put_result
            
            
            mov dword[last_result_loc], edi ; here we got after input in the result file
            mov ecx, [counter] ; get back the value of ecx
            mov dword[intermediary_inverse], 0
            mov dword[intermediary_inverse+4], 0 ; basically resetting all the 8 bytes in the string
            
            
        
        loop digits_loop
        
        end_of_file:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
