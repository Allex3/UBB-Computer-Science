"""
    Greedy + Dynamic programming

    Greedy algorithms make the locally optimal choice at each step with the hope of finding a global optimum.

    Dynamic programming solves complex problems by breaking them down into simpler subproblems, storing the
    results of these subproblems to avoid redundant calculations.
"""


#Fibonacci function with memoization
# store the first two values of the sequence
# Miron Alexandru Bogdan
# O(n) time complexity
cache = {0: 0, 1: 1}

def fib(n: int) -> int:
    if n in cache:
        return cache[n]
    cache[n] = fib(n - 2) + fib(n - 1)
    return cache[n]

"""
1. Calculate the maximum subarray sum (subarray = elements having 
continuous indices)

    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""

#Maxim Andrei
#O(n) time complexity
def maximum_sum(data: list) -> int:
    max_sum = data[0]
    curr_sum = data[0]

    for i in range(1, len(data)):
        curr_sum = max(curr_sum + data[i], data[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum


"""
2. Fractional Knapsack problem. Given the weights and values of N items, put them in a 
   knapsack having capacity W so that you maximize the value of the stored items. Items can be broken up
"""
#Pamfiloiu Robert-Alin
def knapsack(listWeight, listValues, capacity):
    for i in range (len(listWieght)):
        for j in range (len(listWeight)):
            if(listValues[i]/listWeight[i] > listValues[j]/listWeight[j]):
                listValues[i], listValues[j] = listValues[j], listValues[i]
                listWeight[i], listWeight[j] = listWeight[j], listWeight[i]
    TotalValue = 0
    i = 0
    while capacity > listWeight[i] and i < len(listWeight):
        capacity -= listWeight[i]
        TotalValue += listValues[i]
        i += 1
    if i < len(listWeight):
        TotalValue += listValues[i]/listWeight[i]*capacity
    return TotalValue



"""
3. 0-1 Knapsack problem. Given the weights and values of N items, put them in a knapsack having capacity W so that you
   maximize the value of the stored items. Items cannot be broken up (0-1 property)
"""




"""
4. Count in how many ways we can provide change to a given sum of money (N), 
    when provided infinite
   supply of given coin denominations.

   e.g. Let's say N = 10, and we have coins of values (1, 5, 10); we can give 
   change in 4 ways (10, 5 + 5, 5 + 1 + ... and 1 + ... + 1)
"""

"""
5. Gold mine problem (a.k.a checkerboard problem)
   https://www.geeksforgeeks.org/gold-mine-problem
"""