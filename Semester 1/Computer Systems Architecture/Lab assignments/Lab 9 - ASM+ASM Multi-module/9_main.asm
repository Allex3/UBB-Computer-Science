bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf, base_16_char_to_base_16_number
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    hexa_string times 100 db 0
    numbers resd 25
    s_format db '%s', 0
    print_unsigned_format db "unsigned: %u and ", 0
    print_signed_format db "signed: %d ; ", 0

; 9. Read from the keyboard a string of numbers, given in the base 16 (a string of characters is read from the keyboard and a string of numbers must be stored in memory). Show the decimal value of the number both as unsigned and signed numbers.
segment code use32 class=code
    ; main
    start:
        ; we put the numbers at numbers, each representing a dword, each 4 bytes apart
        mov edi, numbers
        cld
        main_loop:
            ; we go until we find a 0 number, stop there and apply the conversion
            push dword hexa_string
            push dword s_format
            call [scanf]
            add esp, 4*2
            
            cmp byte[hexa_string], '-'
            je end_of_loop
            
            mov esi, hexa_string ; hexa_string in edx to compare
            mov edx, hexa_string
            get_current_number:
                mov AL, [EDX]
                inc EDX
                cmp AL, 0
            loopne get_current_number ; loop while number not finished
            
            
            ; reached 0, so decrement EDX
            dec EDX
            sub EDX, ESI ; number of characters in the string, also -1
            mov ECX, EDX
            
            ; now we have our number in hexa_string at position ESI
            ; that is the position we pass to the algorithm to convert it to a number in hexa_numbers
            ; and after that, we always increment EDI=hexa_numbers with 4, to put the next dword there, because each number in the string can be a dword
            ; and we also check how many characters we are gone past, that is ECX+1, that is the current number with a space, so increment ESI by that number
            PUSHAD ; save the registers 
            
            push dword ecx ; how many characters to convert?
            push dword edi ; the numbers that will be converted will be put here in memory
            push dword esi ; this is the string to be converted and put in memory
            call base_16_char_to_base_16_number
            
            POPAD
            
            ; returned here, hexa_number has the number made fromt the string in little-endian form
            push dword [edi]
            push dword print_unsigned_format
            call [printf]
            add esp, 4*2
            
            push dword [edi]
            push dword print_signed_format
            call [printf]
            add esp, 4*2
            
            add edi, 4 ; go to the next dword in memory in hexa_numbers
           
            end_of_loop:
            cmp byte[hexa_string], '-'
        loopne main_loop
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
