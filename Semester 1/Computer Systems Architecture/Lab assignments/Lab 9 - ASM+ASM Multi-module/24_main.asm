bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, get_maximum_of_list
import exit msvcrt.dll    
import scanf msvcrt.dll

extern fopen, fclose, fprintf
import fprintf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    numbers times 100 dd 0
    max resd 1
    max_format db "The maximum from the list is: %d", 0
    signed_format db '%d', 0
    
    file_name db "max.txt", 0
    access_mode db "w", 0
    file_descriptor db -1

; 24. Read a string of signed numbers in base 10 from keyboard. Determine the maximum value of the string and write it in the file max.txt (it will be created) in 16 base.
segment code use32 class=code
    ; main
    start:
        mov esi, numbers
        cld
        main_loop:
            ; we go until we find a ' ' character, stop there and apply the conversion
            push dword esi
            push dword signed_format
            call [scanf]
            add esp, 4*2  
            
            cmp dword[esi], 0 ; at 0 stop reading the list
            je after_reading
            
            add esi, 4 ; go read the next number
            
        jmp main_loop
        after_reading:
        
        push dword numbers ; give the number list 
        call get_maximum_of_list ; the maximum will be returned in eax!
        mov [max], eax ; put eax in [max] variable
        
        ; create the file "max.txt", eax = fopen(file_name, access_mode)
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 4*2
        
        mov [file_descriptor], eax
        
        cmp eax, 0 ; file not successfully created
        je end_of_main
        
        ;output the text in the file 
        push dword [max] ; put the max value on the stack (for %u)
        push dword max_format ; push the format of the string to be outputted
        push dword [file_descriptor]
        call [fprintf]
        add esp, 4*2
        
        ; close the file, fclose(file_descriptor)
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        end_of_main:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
