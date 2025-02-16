"""
    Greedy + Dynamic programming

    Greedy -> choose the local optimum, hoping that it will lead us to global
    optimum (proof of working might not be trivial)

    Dynamic programming -> fit for complex problems, works by diving the problem into
    smaller sub-problems and stores their results such that we avoid redundant
    computations => optimizing the solution
"""

#Fibonacci function with memoization
# f(n) = f(n - 1) + f(n - 2)

cache = {0: 0, 1: 1}
def fib(n: int) -> int:
    if n in cache:
        return cache[n]
    else:
        cache[n]= fib(n - 2)+ fib(n - 1)
        return cache[n]

print(fib(6))
#Time Complexity O(n)
#Vlad Darius Lupu
"""
1. Calculate the maximum subarray sum (subarray = elements having 
continuous indices)

    e.g.
    for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""
# Taschina Luca-Marian
def maximum_sum(data: list) -> int:
    maximum_sum = data[0]
    sum = 0

    for i in range(len(data)):
        sum += data[i]

        if sum > maximum_sum:
            maximum_sum = sum

        if sum < 0:
            sum = 0

    return maximum_sum

print(maximum_sum([-2, -5, 6, -2, -3, 1, 5, -6]))

"""
2. Fractional Knapsack problem. Given the weights and values of N items, put them in a 
   knapsack having capacity W so that you maximize the value of the stored items. Items
   can be broken up
   
   The objects are sorted in descending order by the ratio value/weight.
"""
# Timis Diana
# Time Complexity: O(n)
def fractional_knapsack(weights : list, values : list, W : int, index = 0):
    if index >= len(weights) or W <= 0:
        return 0
    ratio = values[index] / weights[index]
    if W >= weights[index]:
        return values[index] + fractional_knapsack(weights, values, W - weights[index], index + 1)
    else:
        return ratio * W

"""
3. 0-1 Knapsack problem. Given the weights and values of N items, put them in a knapsack
   having capacity W so that you
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