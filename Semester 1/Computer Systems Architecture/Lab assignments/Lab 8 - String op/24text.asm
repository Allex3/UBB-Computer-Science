bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fclose, fprintf
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    text db "abc72g67AB1CD151@#8", 0
    text_len equ $-text
    new_text times text_len db 0
    access_mode db "w", 0
    file_descriptor dd -1

; 24. A file name and a text (defined in data segment) are given. The text contains lowercase letters, uppercase letters, digits and special characters. Replace all digits from the text with character 'C'. Create a file with the given name and write the generated text to file.
segment code use32 class=code
    start:
        mov esi, text
        mov ecx, text_len
        mov edi, new_text
        jecxz endOfProgram
        cld
        
        convertLoop:
            lodsb ; al = [esi], esi++
            mov bl, al
            sub bl, 48; digits in ascii are 48-57, so do al-48 and see if it is lower than or equal to 9, then it is a digit
            cmp bl, 9
            jbe convert_to_C
            
            ; not jumping, put al in [edi]
            stosb ; [edi] = al, edi++
            
            JMP endOfLoop
            
            convert_to_C:
                mov al, 'C'
                stosb ; [edi] = al, edi++
                jmp endOfLoop
                
            endOfLoop:
        loop convertLoop
        
        push dword access_mode
        push dword new_text
        call [fopen]
        add esp, 4*2
        
        mov [file_descriptor], eax
        
        cmp eax, 0
        je endOfProgram ; if file successfuly created
        
        ; write the new_text to file
        push dword new_text
        push dword [file_descriptor]
        call [fprintf]
        add esp, 4*2
        
        ; exit the file by fclose()
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        endOfProgram:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
