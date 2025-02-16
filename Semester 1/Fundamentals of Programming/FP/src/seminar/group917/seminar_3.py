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

#T(n) = 10 * n => O(n)
def f_1(n: int):
    for i in range(10):    # 10 steps
        for j in range(n): # n steps
            print("Hello World")  # O(1)

# T(n) = 10 * n => O(n)
# Timis Diana
def f_2(n: int):
    for i in range(n, n + 10): # 10 steps
        for j in range(n):    # n steps
            print("Hello World") # O(1)

#T(n) -> (n-1)*(n-1)=O(n^2)
#Tatar Patricia
def f_3(n: int):
    for i in range(1, n): # n-1 steps
        for j in range(i, n):  # n-1, n-2, n-3, ..., 1 => 1 + 2 + 3 + .. + n-1 = n(n-1)/2 = > O(n^2)
        #for j in range(i, n): # at most n-1 steps
            print("Hello World")
#ȚABREA
# T(n) = O(n^2)
def f_4(n: int):
    for i in range(n): #n - 1
        for j in range(2 * i + 1): # 1 +  2 * 1 + 1 +  2 * 2 + 1 + 2 * 3 + 1 + ...
            print("Hello World")  # 2 ( 1 + 2 + 3 + .. + n - 1) + n
                                 # 2 * ((n - 1) * n / 2) + n
                                # n * (n - 1) + n
                                # O(n^2)

#T(n) = 1 + 2 + 3 + ... + n^2 - 1 => n^2(n^2-1)/2
# T(n) = (n^4 - n^2) / 2 => O(n^4)
# Tira Denis-Mihai
def f_5(n: int):
    for i in range(n ** 2):  # n ^ 2 steps
        for j in range(i): # 1, 2, 3, ... n^2 - 1
            print("Hello World")

# T(n)=O(n*log(n))
#Utiu Victor
def f_6(n: int):
    for i in range(n): # n steps
        t = 1
        while t < n: # log2(n)
            print("Hello World")
            t *= 2


"""
    Time complexity depends on both "n" and "m"
"""

#O(n+m)
#Untea Jessica
def f_7(n, m: int):
    for i in range(0, n): # n steps
        print("Hello World")
    for j in range(0, m):  # m steps
        print("Hello World")

#T(n) = 2*n => O(n)
#Tranca Miriam
def f_8(n, m: int):
    for i in range(0, n): # n steps
        print("Hello World")
    for j in range(0, n): # n steps
        print("Hello World")

# T(n) = 2n * n => O(n^2)
# Ursache Matei
def f_9(n: int):
    for i in range(n):   # n steps
        for j in range(n): # n steps
            print("Hello World")
        for k in range(n): # n steps
            print("Hello World")

# T(n)= n*(n+m) => O(n*(n+m))
#Ungureanu Violeta
def f_9_2(n, m: int):
    for i in range(n): # n steps
        for j in range(n): # n steps
            print("Hello World")
        for k in range(m): # m steps
            print("Hello World")

 # T(n) = n*(n+1)\2 => O(n^2)
 # Taschina Luca
def f_10(n: int):
    for i in range(n): # n steps
        for j in range(n, i, -1): # n + n-1 + ... + 1
            print("Hello World")

# T(n)=max(n,m)=> 0(n)=max(n,m) ? 
#Vescan Ana
# We consider that the complexity of random is O(1)
def f_11(n: int, m: int) -> None:
    a = 0
    b = 0
    for i in range(n): # n steps
        a = a + random()

    for i in range(m): # m steps
        b = b + random()

# T = n/2 * log2(n) => O(nlog(n))
# Ungureanu Maia
def f_12(n: int) -> None:
    k = 0
    for i in range(n // 2, n): # n//2 steps
        for j in range(2, n, pow(2, j)): # log2(n)
            k = k + n / 2


"""
    Analyze the time and space complexity 
"""
#T(n) = n * log3(n) => O(n * log n)
#Tasadan Luca
#Space complexity: O(1)
def f_13(data: list) -> int:
    data_sum = 0
    for el in data: # n = len(data), n steps
        j = len(data)
        while j > 1: #log3(n) steps
            data_sum += el * j
            j = j // 3
    return data_sum

#T(n) =2 * T(n/2)+ 1= 2*(2* T(n/4)+1)+1= ... = 2 * 2^k - 1= 2*n +1
                                              # n = 2^k
# O(n): Time Complexity
# O(log(n)) : Space Complexity
# Vlad Darius Lupu
def f_14(data: list) -> int:
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2
    return f_14(data[:m]) + f_14(data[m:])

data = [2, 3, 4, 5, 6, 7]
data1 = data[3:]
data2 = data[:3]

print(data1)
print(data2)
print(id(data1))
print(id(data2))
print(id(data1[0]))
print(id(data[3]))

# O((n^2)*log(n)) Time Complexity
# O(1) Space Complexity
# Sandor Stefan
def f_15(n: int) -> int:
    s = 0
    for i in range(1, n ** 2): # n^2 - 1
        j = i
        while j != 0: # log10(n^2)
            s = s + j - 10 * j // 10
            j //= 10
    return s

# Tudor Ioan
# Time Complexity: O(n^2)
# Space Complexity: O(log(n))
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
# o(n^2)
# O(1) space complexity
def f_17(data: list) -> int:
    i = 0
    j = 0
    m = 0
    c = 0
    while i < len(data): # n steps
        if data[i] == data[j]:
            c += 1
        j += 1
        if j >= len(data): # n steps maximum
            if c > m:
                m = c
            c = 0
            i += 1
            j = i
    return m

# O(n)
# Space complexity: maximum O(n)
# Tira Denis-Mihai
def f_17_optimized(data: list) -> int:
    dict_counter: dict = {}
    for num in data: # n steps
        dict_counter[num] = 0
    for num in data: # n steps
        dict_counter[num] += 1

    maximum = -1
    for num in data: # n steps
        maximum = max(maximum, dict_counter[num])

    return maximum
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