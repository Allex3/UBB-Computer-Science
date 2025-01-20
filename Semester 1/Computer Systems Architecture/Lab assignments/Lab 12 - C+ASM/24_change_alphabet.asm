bits 32

global _change_alphabet

segment data use32 public data

segment code use32 public code

_change_alphabet:
    push ebp
    mov ebp, esp

    mov esi, [ebp+8] ; string of small letters :3, at ebp+4 is the return address!!
    mov ecx, [ebp+12] ; length of string
    mov edx, [ebp+16] ; pointer to the new alphabet as a string (alphabet = 'a', alphabet+1 = 'b', etc.)
    ; but it's not actually a, b, c, ..., it's new letters, and those we will change in our string 
    mov edi, [ebp+20] ; the address from C global variable into the register EDI
    
    jecxz .end_of_func
    cld
    .change_letter: 
        lodsb ; AL = load each letter from the string, therelare ECX letters
        ; 'a' = 97, 'b' = 98 ... 'z' = 122, so any letter - 97 will be its position in the new alphabet
        ; because 0 is the position of the first letter of the new alphabet so it corresponds to a, and so on
        sub AL, 97
        mov EBX, 0
        mov BL, AL
        mov AL, byte[EDX+EBX]
        stosb ; [edi] = AL, edi++, put each new letter there, that is the address of the result string
        
    
    loop .change_letter
    
    mov byte[edi], 0
    
    .end_of_func:
    mov esp, ebp
    pop ebp
  
    
    ret ; return handled by C compiler..
