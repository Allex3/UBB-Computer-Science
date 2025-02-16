"""
    Greedy + Dynamic programming

    Greedy concerns taking the local optimum hoping that it will also lead us to the global optimum (but the
    demonstration might not be trivial)
    Dynamic programming is useful for more complex problems, optimizing the solutions, breaking the problem into
    smaller subproblems and storing their results in order to avoid redundant computations.
"""


#Fibonacci function with memoization
"""
f(n) = f(n - 2) + f(n - 1)
"""
#Pop Darius FLorin Luca
# store the first two values of the sequence
cache = {0: 0, 1: 1}

def fib(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
# T(n) = T(n-2) + T(n-1) + 1 = 2(T(n-1))+1 -> O(2^n)


def fibCache(n: int) -> int:
    if n in cache:
        return cache[n]
    else:
        cache[n] = fibCache(n-2) + fibCache(n-1)
        return cache[n]
# T(n) = O(n)

"""
1. Calculate the maximum subarray sum (subarray = elements having continuous indices)

    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""

# time complexity: O(n)
def maximum_sum(data: list) -> int:
    if len(data) == 0:
        return -1

    max_sum = data[0]
    current_sum = data[0]

    for i in range(1, len(data)):
        if current_sum + data[i] > data[i]:
            current_sum += data[i]
        else:
            current_sum = data[i]

        max_sum = max(max_sum, current_sum)

    return max_sum


"""
2. Fractional Knapsack problem. Given the weights and values of N items, put them in a 
   knapsack having capacity W so that you maximize the value of the stored items. Items can be broken up
"""

#Stanculescu Andrada Cristina
#Complexity: O(n)
#Assume the elements are sorted by ratio
def Knapsack(list_of_weights, list_of_values, total_weight, index=0):

    if(index >= len(list_of_values) or total_weight<=0):
        return 0

    ratio = list_of_values[index]/list_of_weights[index]

    if list_of_weights[index]<=total_weight:
        return list_of_values[index] + Knapsack(list_of_weights, list_of_values, total_weight-list_of_weights[index], index+1)
    else:
        return ratio*total_weight

"""
3. 0-1 Knapsack problem. Given the weights and values of N items, put them in a knapsack having capacity W so that you
   maximize the value of the stored items. Items cannot be broken up (0-1 property)
   
Knapsack Capacity 
W=50
Items:
Item 1: Weight = 10, Value = 60 (Value-to-Weight Ratio = 6)
Item 2: Weight = 20, Value = 100 (Value-to-Weight Ratio = 5)
Item 3: Weight = 30, Value = 120 (Value-to-Weight Ratio = 4)
Greedy: 
Select Item 1 (Weight = 10, Value = 60)
Select Item 2 (Weight = 20, Value = 100)
Total weight = 10 + 20 = 30, which leaves room for another item, but adding Item 3 would exceed the capacity.
Greedy Result: Item 1 + Item 2 with a total value of 60 + 100 = 160
Optimal: 
Select Item 2 (Weight = 20, Value = 100)
Select Item 3 (Weight = 30, Value = 120)
Optimal Result: Item 2 + Item 3 with a total value of  100+120=220.
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