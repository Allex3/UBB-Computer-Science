bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fclose, fread
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fread msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    char db 0 
    char_freq db 0
    file_name db "sequence.txt", 0
    access_mode db "r", 0
    file_descriptor dd -1
    len equ 100
    text times len db 0
    frequency times 256 db 0 ; frequency of ascii characters

    
; 9. A text file is given. Read the content of the file, determine the special character with the highest frequency and display the character along with its frequency on the screen. The name of text file is defined in the data segment.
segment code use32 class=code
    start:
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 4*2 ; open file in reading mode
        
        mov [file_descriptor], eax ;file descriptor returned by eax
        ; read the text from file using fread()
        ; after the fread() call, EAX will contain the number of chars we've read 
        ; eax = fread(text, 1, len, file_descriptor)
        
        push dword [file_descriptor]
        push dword len
        push dword 1
        push dword text
        call [fread]
        add esp, 4*4
        
        mov ecx, eax ; number of chars of our text
        jecxz endOfProgram
        countFrequency:
            mov ebx, 0
            mov bl, byte[text+ecx-1] ; from character n-1 to 0
            inc byte[frequency+ebx]
            
        loop countFrequency
        
        mov ecx, 256
        mov bl, -1
        mostFrequency:
            cmp bl, byte[frequency+ecx-1]
            JL new_high_frequency; below, make ebx equal to that frequency and dl equal to that character represented by ecx-1
            JMP endOfLoop
            new_high_frequency: 
             
                mov dx, cx
                dec dx
                mov bl, [frequency+ecx-1]
               
            endOfLoop:
        loop mostFrequency
            
        mov byte[char], dl
        mov byte[char_freq], bl
        endOfProgram:
        
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
