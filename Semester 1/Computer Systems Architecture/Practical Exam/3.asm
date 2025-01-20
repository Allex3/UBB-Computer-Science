bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
extern printf, scanf, fread, fopen, fclose
import printf msvcrt.dll
import scanf msvcrt.dll
import fread msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    n dd 0
    count dd 0
    file_name times 50 db 0
    character dd 0
    
    format db "%s", 0
    format_n db "%u", 0
    format_end db "count of characters with the %u'th bit 1: %u", 0
    access_mode db "r", 0
    file_descriptor dd -1
    

; our code starts here
segment code use32 class=code
    start:
        push dword file_name
        push dword format
        call [scanf]
        add esp, 4*2
        
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 4*2
        
        mov [file_descriptor], eax
        cmp eax, 0
        je end_of_file
        
        push dword n
        push dword format_n
        call [scanf]
        add esp, 4*2

        ; if not 0<=n<=7 then we go to end_of_file
        cmp dword[n], 7
        jg end_of_file
        
        cmp dword[n], 0
        jl end_of_file
        
       
        
        ;infinite loop, stops when no more characters in file
        mov ecx, 0
        count_1_bits:
            ; call fread(character, 1, 1, file_descriptor) <- reads one byte from the file, returns 0 if file is empty so nothing is read
            
            push dword [file_descriptor]
            push dword 1
            push dword 1
            push dword character
            call [fread]
            add esp, 4*4
            
            cmp eax, 0 ; number of bytes read is saved in eax, if it is 0 file is empty, we read all the bytes so jump after loop
            je after_loop
            
            
            mov eax, [n] ; 0<=n<8, but is in a dword because it was read from a console, but it fits in AL
            mov CL, AL
            mov BL, 1
            shl BL, CL ; BL<<CL, for example if n =5, then BL=1<<CL=5, and it will be 00100000
            ; now the N'th bit of the character can be AND'ed with the N'th isolated bit from the above byte
            ; and if we get 0 then the N'th bit of the character byte is 0, if we get 1 from the AND then it will be above 0
            mov eax, [character] ;character is dd so it could be read, but it's size 1 so it fits in AL
            and AL, BL 
            
            cmp AL, 0
            JE end_of_loop; 0, jump at the end of the loop
            
            ; did not jump, count the 1 bits
            add dword[count], 1
            
            end_of_loop:
            
            mov ecx, 0 ; 0-1 = -1 = FFFFFFFF, ensuring an infinite loop (or jmp instruction could have worked)
            
        loop count_1_bits
        
        after_loop:
        
        push dword [file_descriptor]
        call [fclose]
        add esp, 4
        
        push dword [count] ; output the count
        push dword [n]
        push dword format_end
        call [printf]
        add esp, 4*2
       
        
        end_of_file:
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
