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
    hexa_numbers resd 25
    s_format db '%s', 0
    print_unsigned_format db "unsigned: %u and ", 0
    print_signed_format db "signed: %d ; ", 0

; 9. Read from the keyboard a string of numbers, given in the base 16 (a string of characters is read from the keyboard and a string of numbers must be stored in memory). Show the decimal value of the number both as unsigned and signed numbers.
segment code use32 class=code
    ; main
    start:
        push dword hexa_string
        push dword s_format
        call [scanf]
        add esp, 4*2
        
        ; we put the numbers at hexa_numbers, each representing a dword, each 4 bytes apart
        mov esi, hexa_string
        mov edi, hexa_numbers
        main_loop:
            ; we go until we find a ' ' character, stop there and apply the conversion
            
            mov edx, esi ; hexa_string in edx to compare
            get_current_number:
                mov AL, [EDX]
                inc EDX
                cmp AL, 0 ; if it is 0 the string is DONE, so get out too!
                je reached_0
                cmp AL, ' '
            loopne get_current_number ; loop while not space yet
           
            reached_0:
            ; reached space, space character is counted to, so decrement ECX
            sub EDX, ESI ; number of characters in the string 
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
            inc ecx ; to account for the 'space' because we add it to esi to go to the nextn umber
            add esi, ecx ; now we are at the next number in string 
            
            ; now at position [esi] starts the next number, BUT what do we do if it's 0?
            ; then 0 will beat [esi-1], as the last char of the string
            cmp byte[esi-1], 0
        jne main_loop
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
