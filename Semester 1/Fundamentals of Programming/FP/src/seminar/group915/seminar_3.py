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
    for i in range(10):           # 10 steps
        for j in range(n):         # n steps
            print("Hello World")   # O(1)

# T(n) = 10 * n => O(n)
# David Malutan
def f_2(n: int):
    for i in range(n, n + 10):  # 10 steps
        for j in range(n):      # n steps
            print("Hello World") #0(1)

# T(n) = O(n^2)
#Oprinescu Carmen
def f_3(n: int):
    for i in range(1, n): #n-1 steps
        for j in range(i, n): # 1+2+3+...+n = n(n+1)/2
            print("Hello World") #0(1)

# O(n^2)
#Mintar Dinu Dragos
def f_4(n: int):
    for i in range(n):   # n
        for j in range(2 * i + 1): # 2 * (1+2+3+...+n-1) + n-1    O(n^2)

            print("Hello World")  # O(1)

#T(n)= O(n^4)
#Mateica Patricia
def f_5(n: int):
    for i in range(n ** 2): #n^2 steps O(n^2)
        for j in range(i): #0+1+2+3+...+n^2-1 O(n^4)
            print("Hello World") #O(1)

# T(n) = n * log(n) -> O(nlog(n))
#Maxim Andrei
def f_6(n: int):
    for i in range(n): #O(n)
        t = 1
        while t < n: #log2(n)
            print("Hello World")
            t *= 2


"""
    Time complexity depends on both "n" and "m"
"""

#O(n+m)
#Pamfiloiu Robert-Alin
def f_7(n, m: int):
    for i in range(0, n):  # n loops
        print("Hello World") #0(1)
    for j in range(0, m):  # m loops
        print("Hello World") #o(1)

#O(n+n)=O(n)
#Mihet Marius
def f_8(n, m: int):
    for i in range(0, n): # n times
        print("Hello World") # O(1)
    for j in range(0, n): # n times
        print("Hello World") # O(1)

#T(n) = n*(2n) = 2n^2 -> O(n^2)
#Pascut Rares-Alexandru
def f_9(n: int):
    for i in range(n): #n steps
        for j in range(n): #n times
            print("Hello World")
        for k in range(n): #n times
            print("Hello World")

#T(n) = n*(n+m)
# Opris Matia
def f_9_2(n, m: int):
    for i in range(n): # n times
        for j in range(n): # n times
            print("Hello World")
        for k in range(m): # m times
            print("Hello World")

#Oara Dragos
def f_10(n: int):
    for i in range(n):
        for j in range(n, i, -1):
            print("Hello World")
"""
n-1\n-2\....1   t(n)=n^2
n, n-1, n-2, ....., 1 - n
n, n-1, n-2, ...., 2 - n-1
....
n -1
n(n-1)/2


"""

# O(n+m)
# Pastiu Adrian Mihai
def f_11(n: int, m: int) -> None:
    a = 0
    b = 0
    for i in range(n): # n steps
        a = a + random()

    for i in range(m): # m steps
        b = b + random()

# O(n*log(n))
# Nojea Razvan
def f_12(n: int) -> None:
    k = 0
    for i in range(n // 2, n): # n / 2 times
        for j in range(2, n, pow(2, j)): # log(n) times
            k = k + n / 2


"""
    Analyze the time and space complexity 
"""

#O(nlog3(n)) Time
#O(1) Space
#Mocanu Cosmin
def f_13(data: list) -> int:
    data_sum = 0 #O(1)
    for el in data: #n
        j = len(data) #O(1)
        while j > 1: #log3(n)
            data_sum += el * j
            j = j // 3
    return data_sum



# t(n) = t(n/2) + t(n/2) + 1
# space complexity O(N)
#Luca Emil Olteanu
def f_14(data: list) -> int:
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2 #
    return f_14(data[:m]) + f_14(data[m:]) #O(n)


# T(n) = log(1) + log(2) + ... + log(n^2-1) => O(n^2*log(n))
# S(n) = O(1)
# Mocrei Bogdan
def f_15(n: int) -> int:
    s = 0
    for i in range(1, n ** 2): # n^2-1 times
        j = i
        while j != 0: # log10(i)
            s = s + j - 10 * j // 10
            j //= 10
    return s


# T(n) = O(n^2)
# O(log(n))
# Mateian Andrei
def f_16(n, i: int) -> None:
    if n > 1:
        i *= 2
        m = n // 2
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


def f_17(data: list) -> int:
    i = 0
    j = 0
    m = 0
    c = 0
    while i < len(data):
        if data[i] == data[j]:
            c += 1
        j += 1
        if j >= len(data):
            if c > m:
                m = c
            c = 0
            i += 1
            j = i
    return m


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