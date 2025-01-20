bits 32
segment code use32 public code
global get_maximum_of_list

get_maximum_of_list:
    mov esi, [esp+4] ; numbers array
    ; traverse the numbers until you reach 0
    mov eax, [esi] ; maximum number will be in eax, first we input the first number there
    .maximum_loop:
        mov EBX, [esi]
        cmp EAX, EBX
        JL .new_max ; EAX<EBX, so new maximum found , put it in EAX
        ; if we don't jump there, jump to the end of the loop
        jmp .end_of_loop
        .new_max: 
            mov EAX, EBX
            
        .end_of_loop:
        add esi, 4 ; go to next number, check if it's 0 
        cmp dword[esi], 0 ; check the dword at esi is the current number
    loopne .maximum_loop
    
    ret 4
