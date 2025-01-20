#include <stdio.h>
#include <string.h>

int numbers[100];
int base_16_char_to_base_16_number(char str[]);

/*
Read from the keyboard a string of numbers, given in the base 16
(a string of characters is read from the keyboard and a string of numbers must be stored in memory).
Show the decimal value of the number both as unsigned and signed numbers.
*/

int main()
{
    char number_str[10];
    while (1)
    {
        scanf("%s", number_str);
        if (number_str[0] == '0' && number_str[1] == '\0')
            break;
        int number = base_16_char_to_base_16_number(number_str, strlen(number_str));
        unsigned int u_number = base_16_char_to_base_16_number(number_str, strlen(number_str));
        printf("Unsigned: %u, Signed: %d \n", u_number, number);
    }
}