### [[Two's complement questions|Go to the exam questions regarding 2's Complement]]
### Definition 

The two's complement **REPRESENTATION** of a ==NEGATIVE== number is the value 2^n - V, where V is the absolute value of the represented number

**One** possible **representation**, for which there are **two** possible **interpretations** (signed and unsigned, if we use two's complement or not)
So **the representation 10010011** has **two base 10 interpretations, unsigned**
For a binary representations that begins with 1, there will always be **two interpretations for it, signed and unsigned**: -109 and 147 for 10010011, and the two's complement of that number is 109, and 109+147 = 256 = 2^8 so all the numbers that can be represented on 8 bits

Value in **signed interpretation** (base 10), it's value is -(2's complement of the initial binary configuration) = -(2^n - V)

### How to obtain the 2's complement of a number (represented in memory, so base 2)
##### Variant 1 (Official) - Subtract the binary contents of the location from 1000......00, number of zeroes = number of bits of the location
```
1001 0011 = 147 in unsigned interpretation, but -109 in signed representation

1 0000 0000 -
  1001 0011
  0110 1101 = 6Dh = 96+13 = 109 (2's complmenet of 147 is 109, on 8 bits)
 But this 147 in the signed, so if it's complement is 109, it itself in SIGNED interpretation is -109, and in the UNSIGNED interpretation is 147
So 1001 0011 in the SIGNED interpretation is -109
```
##### Variant 3 (faster, more practical)
- Inverse the bits of the memory location
- Add one to that inverse
The two's complement of a two's complement of a number is the number itself
`10010011 -> 01101101 is its two complement, but `
`01101101 -> 10010011 is its two's complement too, so they can be inversed and it always works`

##### Variant 4 (fasterrrrrr)

>[!INFO] 2^n represents the number of values possible to be represented on that size (of n bits)

Suma valorilor absolute ale celor valori complementare in baza 10 este cardinalul multimii numerelor reprezentate pe acea dimensiune (2^n) 
**Definition**: The sum of the absolute values of the two complementary values is the cardinal of the set of values representable on that size
For a binary representations that begins with 1, there will always be **two interpretations for it, signed and unsigned**: -109 and 147 for 10010011, and the two's complement of that number is 109, and 109+147 = 256 = 2^8 so all the numbers that can be represented on 8 bits
it is 
>[!INFO] It follows that, because the sum of the number and it's complement being 2^n, the **SIGNED** interpretation for it is 2^n - (unsigned interpretation (basic base 2 to base 10 conversion))
>e.g. 256 - 147 = 109, so the complement of 147 is 109, thus 147 in binary is in two's complement representation -109 (because -109's two's complement is 109, so this **MUST** be true)

##### How do we decide what complement gives the negative number?
- **147's complement is 109, but how do we know** if 109 is -147, or 147 is -109, because one number's complement HAS TO BE interpreted in signed notation as it's negative, so it's **two choices**: 109 = -147 or 147 = -109
>[!info] Choose the number that's **WITHIN THE BOUNDS OF THE REPRESENTATION, it can't be represented**, so we choose -109, because -147 does not belong to `[-128, 127]`, so we can't fit it, and ALWAYS one of the numbers will belong and the other won't, that's how we decide **what interpretation is and should be the signed one**, but also the **sign bit**

###### Starting from this configuration, what are the 4 interpretations?
0....... -> only one interpretation - same in signed and unsigned
1...... -> unsigned and signed interpretation

