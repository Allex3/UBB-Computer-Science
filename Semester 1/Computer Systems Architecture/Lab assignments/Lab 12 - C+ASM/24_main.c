/*
Read a string s1 (which contains only lowercase letters). Using an alphabet (defined in the data segment),
determine and display the string s2 obtained by substitution of each letter of the string s1
 with the corresponding letter in the given alphabet.
Example:
The alphabet:  OPQRSTUVWXYZABCDEFGHIJKLMN
The string s1: anaaremere
The string s2: OBOOFSASFS
*/
#include <stdio.h>
#include <string.h>

char alphabet[] = "OPQRSTUVWXYZABCDEFGHIJKLMN";
char s1[100];
char s2[100] = "";

char* change_alphabet(char s[], int len, char alphabet[], char s2[]);

int main()
{
    scanf("%s", s1);
    change_alphabet(s1, strlen(s1), alphabet, s2);
    printf("s2: %s", s2);
}