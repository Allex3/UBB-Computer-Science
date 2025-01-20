bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fprintf, fopen, scanf, fclose     ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import fprintf msvcrt.dll
import fopen msvcrt.dll
import scanf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import fclose msvcrt.dll
                          
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    access_mode db "w", 0 
    file_name times 30 db 0
    text times 120 db 0
    file_descriptor dd -1
    access_mode_read db "r", 0
    
    get_name_format db "%s.txt", 0
    format db "%s", 0


; Read a file name and a text from the keyboard. Create a file with that name in the current folder and write the text that has been read to file. Observations: The file name has maximum 30 characters. The text has maximum 120 characters.
segment code use32 class=code
    start:
        push dword file_name
        push dword format
        call [scanf]
        add esp, 2*4
        
        push dword text
        push dword format
        call [scanf]
        add esp, 2*4
        
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 2*4
        
        mov dword[file_descriptor], eax
        
        cmp eax, 0
        je end_of_file

        
        push dword text
        push dword format'
        push dword [file_descriptor]
        call [fprintf]
        add esp, 3*4
        
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        
        end_of_file:
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
