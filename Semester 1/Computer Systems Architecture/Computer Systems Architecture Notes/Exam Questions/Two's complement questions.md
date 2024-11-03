
>[!QUESTION] 1) Which is the signed interpretation of:

>[!answer] 
>i) 10010011 -> **b) -109**  
ii) 93h (= 10010011 -> **b) -109**)  
iii) 147 -> **NONE - THIS IS A STUPID QUESTION** - we cannot have **DIFFERENT** interpretations in base 10 of numbers **ALREADY** expressed in base 10 (**147 is already an interpretation**) => **f) None of the above** 
>a) 01101101  
b) -109  
c) 6Dh  
d) +147  
e) -147  
f) NONE of the above

### Giving a configuration, in what situations do we need to use the 2's complement? Types of questions
##### a)
>[!Question] If we have a REPRESENTATION of type 0𝑥𝑥𝑥…. having the value +𝑎𝑏𝑐 in the UNSIGNED interpretation, which will be the value of this REPRESENTATION in the SIGNED interpretation ? **==(b2 – b10)==**

>[!answer] The same ! A number that begins with 0 in base 2 has the same value in base 10 both in signed and unsigned interpretation, being a positive number (109 is +109 in both interpretations).
##### b)
>[!question] If we have a **REPRESENTATION** of type 0xxx..... having the value +abc, which will be the binary **REPRESENTATION** of -abc ? (Ex: if we consider 109, how is -109 represented in base 2?) **(==b2-b2==)**

>[!answer] **Answer**: Only in such a question 2's complement starts to play a role
>its REPRESENTATION will be "the 2's complement of the initial binary configuration". For the value 109 = 01101101, the 2's complement of 01101101 is 10010011, so -109 = 10010011
>
>As a result we can conclude that the complementary value of an integer that **begins with 0, will begin with 1** (exception making only the value 0) and will fit as a complementary value in the SIGNED interpretation on the same representation size as the initial value !! (-109 is also a byte , similar to 109). 

>[!question] c) If we have a **REPRESENTATION** of type 1xxx.... having the value +abc in the **UNSIGNED** interpretation, which will be the value in the **SIGNED** interpretation ? (==b2-b10==)

>[!answer] **Answer:** The value is **-(the 2's complement of the initial binary configuration)** 
>For our example we have: 10010011 = 147 (unsigned) = - (the 2’s complement of 10010011) = -(01101101) = -109.

>[!question] d) If we have a **REPRESENTATION** of **1xxx.....** having the value +abc, which will be the binary **REPRESENTATION** for the value -abc ? (Ex: if we consider 10010011 = +147, which is the binary representation for -147?) (==b2-b2==)
>**DOES NOT FIT on n bits, because it starts with 1 in the unsigned notation**, and the negative value has to also **start with 1**, but if it's positive representation **starts with a 1**, the value of -147 **CANNOT BE REPRESENTED ON 8 bits**
>
>==**Answer**==: Extend it (byte->word, word->dword, dword->qword), or on paper 1 bit is enough!
>If we extend it by 1 bit we have a range of `[0, 511] => [-256, +255] in signed interpretation`, so now a number of 8 bits, or in general, n bits, **if it starts with 1 and it's positive, to get it's negative value extend the size by 1 bit!**
>
>2’s complement of 1xxx’s UNSIGNED extension on 2 * sizeof (1xxx) **AND THEN** compute it's complement, adn that will be negative
>
>Example: 147 = 10010011, it's negative CANNOT be represented on 8 bits, so extend it by 1 bit and get it's complement: 
>` 0 10010011`'s complement is `1 01101101`, which is -147 here ! 
>(in nasm you need to extend a full byte and it will be `00000000 10010011 -> 11111111 01101101`)

>[!info] As a result, we conclude that if we start from a representation of the form **1𝑥𝑥𝑥…. of value +𝑎𝑏𝑐** ==WE CANNOT== obtain the value **− 𝑎𝑏𝑐 ON THE SAME REPRESENTATION SIZE !!!**!! 

>[!INFO] Basically, if a number X starts with:
>	0..., -X starts with a 1, and fits on the same size
>	1..., -X starts with a 1, and fits on double it's size in ASM (need only 1 bit more, but need to allocate atleast 8 or 16)


>[!question] Which is the minimum number of bits on which you can represent a number (-147 let's say)? **(EXPLANATION NEEDED)**

>[!answer] On n bits we can represent 2^n values:	
-147 does not fit on 8 bits, so try on 9 bits
On 9 bits... `[0, 511]` or `[-256, 255]` and because 147 belongs to `[-256, 255]`, it follows that the **MINIMUM** number of bits on which we may represent -147 is 9 and -147 representation is:
(On 9 bits we represent 512 numbers, )

```
So… obtaining -147 starting from 147 = 10010011 must be done in the following way:

i). The binary representation of 147 begins with 1, but we must notice that -147 ∉ [-128..+127], but -147 ∈ [-32768..+32767] which concludes that -147 is NOT representable as a byte BUT ONLY AS A WORD !!

ii). On a WORD size, 147 = 00000000 10010011 (so a binary number beginning with 0) and according to b), we have that -147 = "the 2's complement of the initial binary configuration" 

The 2's complement of the configuration 00000000 10010011 is 11111111 01101101, so -147 = 11111111 01101101 = FF6Dh
```
![[Images/TwosComplement.png]]

>[!question] Which is the minimum number of bits on which we can represent 3?

>[!answer] Answer: 2 bits, 3 = 11b
>On two bits we may represent 2^2 values = 4 values, `0, 1, 2, 3 in unsigned` or `-2, -1, 0, 1` in SIGNED
>