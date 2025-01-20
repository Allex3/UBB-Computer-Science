bits 32
segment code use32 public code
global base_16_char_to_base_16_number

base_16_char_to_base_16_number:
    ; a string of characters representing the hexadecimal repres. of a number if stores in hexa_string
    ; two bytes of this string 'AB' is actually one byte of numbers in memory
    ; we need to traverse it in little-endian, because hexa_string is little-endian, so right to left
    ; but put it in hexa_number left to right like normal in little-endian
    ; because in string format it is in big-endian normal order
        cld  
        
        mov ECX, [esp+12] ; for the loop, this is the number of characters in the current number of the string
        mov esi, [esp+4] ; hexa_string
        mov edi, [esp+8] ; hexa_number, put the digits from right to left from the string to left to right little-endian here
        cld
        jecxz .end_of_func
        .convert_to_number:
            mov AL, [esi+ECX-1]
            ; 0-9 = 48-57 in ASCII, so subtract 48 from it  
            cmp AL, '9' ; below '9' it means the chars are 0-9
            jbe .AL_to_lower_half_of_byte_10
            ; if it's not 0-9, jump to convert type A-F = 65-70, so subtract 55 from it
            jmp .AL_to_lower_half_of_byte_hexa
            
            .AL_to_lower_half_of_byte_10:
                sub AL, 48
            ; to not go to the next method, go after it
                jmp .skip_AL_conv
            .AL_to_lower_half_of_byte_hexa:
                sub AL, 55
            
            .skip_AL_conv:
            cmp ECX, 1 ; if ECX=1 here, it means the highest digit (first left character in string)
            ; is of the form 0X, X=0-F, because we subtract ECX by 2 each iteration, and it reached an odd count
            ; so just... end the loop, value is good as it is in AL, no need to put a higher byte nibble because it's 0, just jump to storing the value
            je .store_in_memory
            
            mov BL, [esi+ECX-2] ; now apply the same algorithm to B
            cmp BL, '9' ; below '9' it means the chars are 0-9
            jbe .BL_to_lower_half_of_byte_10
            ; if it's not 0-9, jump to convert type A-F = 65-70, so subtract 55 from it
            jmp .BL_to_lower_half_of_byte_hexa
            
            .BL_to_lower_half_of_byte_10:
                sub BL, 48
            ; to not go to the next method, go after it
                jmp .skip_BL_conv
            .BL_to_lower_half_of_byte_hexa:
                sub BL, 55
            
            .skip_BL_conv:
            ; now, BL is the higher nibble, and AL is the lower nibble, rn it has 0000xxxx 
            ; so we need to put BL which is 0000yyyy into AL like so to form the bytes of the two hexa digits:
            ; yyyyxxxx in AL, doing bit operations
            shl BL, 4 ; 0000yyyy -> yyyy0000
            or AL, BL ; 0000xxxx or yyyy0000 = yyyyxxxx, representing the byte "AB" well now!
            dec ECX ; decrement ECX here to account for the two bytes = 1 number byte thingy
            ; becuase if we go to the label below, ECX=1, so don't make it 0 because then ECX=ffffffff
            .store_in_memory:
            stosb ; [edi] = AL, edi++
        loop .convert_to_number
        
        .end_of_func:
        ret 4*3 ; remove the 2 params from the stack
        