bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fread, printf, fclose, fopen             ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import fread msvcrt.dll
import printf msvcrt.dll
import fclose msvcrt.dll
import fopen msvcrt.dll

; A text file is given. Read the content of the file, count the number of letters 'y' and 'z' and display the values on the screen. The file name is defined in the data segment.
segment data use32 class=data
    file_name db "8_16.txt", 0
    y_count dd 0
    z_count dd 0
    access_mode db "r", 0
    file_descriptor dd -1
    format db "y count: %u, z count: %u", 0
    
    character dd 0

; our code starts here
segment code use32 class=code
    start:
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 2*4
        
        mov [file_descriptor], eax
        
        cmp eax, 0
        je end_of_file
        
        mov ecx, 0 ;infinite loop :3
        count_y_and_z: ; we read character by character using fread(character, 1, 1, file_descriptor)
            push dword[file_descriptor]
            push dword 1
            push dword 1
            push character
            call [fread]
            add esp, 4*4
            
            ; eax = numbers of characters we read, if it is 0 we reached EOF and exit the loop!
            cmp eax, 0
            je end_of_file
            
            cmp byte[character], 'y'
            je count_y
            
            cmp byte[character], 'z'
            je count_z
            
            ; it's neither y, nor z, so go to end of loop
            jmp end_of_loop
            
            count_y:
                add dword[y_count], 1
                jmp end_of_loop
            
            count_z:
                add dword[z_count], 1
                jmp end_of_loop
            
            end_of_loop:
            
        loop count_y_and_z    
        

        
        end_of_file:
        
        push dword [z_count]
        push dword [y_count]
        push dword format
        call [printf]
        add esp, 4*3
        
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
