"""
    Determine the time complexity of the following algorithms as a function of n.
    sources:
        https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
        https://www.geeksforgeeks.org/practice-questions-time-complexity-analysis/

    Notations:
    - n = size of the input (number of elements that have to be processed - but we can also have n, m, ... if multiple inputs)
    - A = the algorithm
    - T(n) = number of steps (operations) the algorithm does

    - O(n) - upper bound - my algorithm cannot go worse than this
    - Omega(n) - low bound - my algorithm cannot go better than this
    - Theta(n) - both upper and lower bound - my algorithm always has the same complexity (BC=AC=WC)

Cases
    - BC(A): case in which we do least number of steps
    - AC(A): formula
    - WC(A): case in which we do most steps

Complexity in terms of:
    - time (number of operations taken to solve the problem)
    - space (memory, number of bytes taken to solve the problem)
"""
from random import random


# T(n) = 10 * n => O(n)
def f_1(n: int):
    for i in range(10):     # 10 steps
        for j in range(n):  # n steps
            print("Hello World") # O(1)

# 10*n=n -> O(n)
#Suciu Maria
def f_2(n: int):
    for i in range(n, n + 10): # O(10)
        for j in range(n): # O(n)
            print("Hello World") # O(1)

#T(n) = O(n^2)
#Muresan Ianis
def f_3(n: int):
    for i in range(1, n):#O(N)
        for j in range(i, n): #1+2+3..+n-1= n(n-1)/2 -> O(n^2)
            print("Hello World")#O(1)

#T(n)=O(n^2)
#Simon Laszlo
def f_4(n: int):
    for i in range(n):
        for j in range(2 * i + 1): #2*(1 + 2 + 3 + ... + n-1) + n-1 = (n-1)*n + n-1 = n^2
            print("Hello World") #O(1)

#T(n) = O(n^4)
#Pop Maya - Diana
def f_5(n: int):
    for i in range(n ** 2): #O(n^2)
        for j in range(i): #1 + 2 + ... + n^2 - 1 = n^2(n^2-1)/2 => O(n^4)
            print("Hello World") #O(1)

#T(n) = O(n*log(n))
#Radu Amalia
def f_6(n: int):
    for i in range(n): #O(n)
        t = 1
        while t < n: #O(logn)
            print("Hello World") #O(1)
            t *= 2


"""
    Time complexity depends on both "n" and "m"
"""

#T(n)=O(n+m)
#Pop Nicoleta Bianca
def f_7(n, m: int):
    for i in range(0, n):  #O(n)
        print("Hello World")#O(1)
    for j in range(0, m):  #O(m)
        print("Hello World")#O(1)

#T(n)=n+n=2n  O(n)
#Ros Antonio Ionut
def f_8(n, m: int):
    for i in range(0, n): #O(n)
        print("Hello World") #O(1)
    for j in range(0, n): #O(n)
        print("Hello World") #O(1)

#T(n) = n*2*n -> O(n^2)
# Pop Raul Bogdan
def f_9(n: int):
    for i in range(n): # O(n)
        for j in range(n): # O(n)
            print("Hello World") # O(1)
        for k in range(n): # O(n)
            print("Hello World") # O(1)

#T(n)= n*(n+m)= O(n*(n+m))
#Reut Diana Elena
def f_9_2(n, m: int):
    for i in range(n): # O(n)
        for j in range(n): # O(n)
            print("Hello World") # O(1)
        for k in range(m): # O(m)
            print("Hello World") # O(1)

# T(n)=O(n^2)
#Szabo Tiberiu
def f_10(n: int):
    for i in range(n): #O(n)
        for j in range(n, i, -1): #n-1+n-2+...+1=(n-1)*n/2 -> O(n^2)
            print("Hello World") #O(1)

# T(n) = O(n+m)
# Popescu David Ionut
def f_11(n: int, m: int) -> None:
    a = 0
    b = 0
    for i in range(n): # O(n)
        a = a + random() # O(1)

    for i in range(m): # O(m)
        b = b + random() # O(1)

#T(n) = O(nlogn)
#Pop Alexandra
def f_12(n: int) -> None:
    k = 0 #O(1)
    for i in range(n // 2, n): #O(n/2)
        for j in range(2, n, pow(2, j)): #j can take the following values: 2, 6, 70, 16... n => O(log(n))
            k = k + n / 2


"""
    Analyze the time and space complexity 
"""

#T(n) = n*log(n) => O(nlog(n))
#Pop Darius Florin Luca
#Extra space complexity  = O(1)
def f_13(data: list) -> int:
    data_sum = 0 #O(1)
    for el in data: #O(n)
        j = len(data) #O(1)
        while j > 1: #O(log3(j))
            data_sum += el * j #O(1)
            j = j // 3 # O(1)
    return data_sum

#T(n)=2^(k+1)-1=2^k*2-1=2n-1 -> O(n)
#Extra space complexity = O(n)
#Popa Samuel Paul
def f_14(data: list) -> int:
    if len(data) == 0: #O(1)
        return 0
    if len(data) == 1: #O(1)
        return data[0]
    m = len(data) // 2 #O(1)
    return f_14(data[:m]) + f_14(data[m:]) #O(n)

#data = [2, 3, 4, 5, 6, 7]
#data1 = data[3:]
#data2 = data[:3]

#print(data1)
#print(data2)
#print(id(data1))
#print(id(data2))

# O(n^2*log(n))
#Stanculescu Andrada Cristina
#Extra space complexity O(1)
def f_15(n: int) -> int:
    s = 0 #O(1)
    for i in range(1, n ** 2): #O(n^2)
        j = i #O(1)
        while j != 0: # lg(1) + lg(2) +lg(3) + ... + lg(n^2-1) -> O(lg(n))
            s = s + j - 10 * j // 10 #O(1)
            j //= 10 #O(1)
    return s


#O(n^2)
#extra space complexity O(log(n))
#Suciu Teodora
def f_16(n, i: int) -> None:
    if n > 1:
        i *= 2 #O(1)
        m = n // 2 #O(1)
        f_16(m, i - 2)
        f_16(m, i - 1)
        f_16(m, i + 2)
        f_16(m, i + 1)
    else:
        print(i)


"""
Analyze the algorithm's time complexity. Write an equivalent algorithm with 
a strictly better time complexity
"""

#T(n) = n^2 -> O(n^2) - time
#O(1)                 - space
#Ratiu Mihai Cornel
def f_17(data: list) -> int:
    i = 0
    j = 0
    m = 0
    c = 0
    while i < len(data): # O(n)
        if data[i] == data[j]:
            c += 1
        j += 1
        if j >= len(data): # O(n)
            if c > m:
                m = c
            c = 0
            i += 1
            j = i
    return m


def f_17_alternative(data: list) -> int:
    datalist = {}
    for i in range (len(data)):
        datalist[data[i]] = 0
    for i in range(len(data)):
        datalist[data[i]] += 1
    max = datalist.get(0)
    for i in range (len(datalist)):
        if datalist[i]>max:
            max = datalist.get(i)
    return max

# T(n) = O(n)
# space complexity also O(n)
#Simon Laszlo


"""
    What is the time complexity when implementing the following algorithm. How can this be 
    optimized and how will that improve the complexity?
"""


def f_18(x, n: int):
    """
    The algorithm returns x ** n
    :param x:
    :param n:
    :return:
    """
    # TODO Implement me
    pass