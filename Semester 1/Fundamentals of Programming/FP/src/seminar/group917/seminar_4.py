"""
    Problem Solving Methods -- Divide & Conquer, Backtracking

    How does divide and conquer work?

    Divide & Conquer
    Divide: divide problem in sub-problems which are similar to the original (disjoint sub-problems)
    Conquer: solve the smallest problems
    Combine: combine the result obtained for the smaller problems (to solve the original one)


    What D&C algorithms do we already know?

    Merge sort, Binary search, Quick sort

    Divide: divide the list into halves
    Conquer: array of length 1 is sorted
    Combine: merge the sorted lists
"""
from Seminar916.seminar_4 import divide_half

"""
    1. Implement an optimized version of the merge sort algorithm
        a. Implement Merge Sort
        b. Use the insertion sorting algorithm with the binary search optimization found in the lecture examples
        c. Time the resulting version using the ex17_sort_comparison.py example - at home
        d. Discuss how merging might be improved using exponential search
"""

# Taschina Luca-Marian
def merge_sort(array, thershold = 10):
    if len(array) <= 1:
        return array

    if len(array) <= thershold:
        return insertion_sort(array)

    middle = len(array) // 2

    subarray1 = merge_sort(array[:middle])
    subarray2 = merge_sort(array[middle:])

    return merge(subarray1, subarray2)

def merge(list1, list2):
    output = []

    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            output.append(list1[i])
            i += 1
        else:
             output.append(list2[j])
             j += 1

    while i < len(list1):
        output.append(list1[i])
        i += 1

    while j < len(list2):
        output.append(list2[j])
        j += 1

    return output

def test():
    list1 = [2, 4, -5, 81, 9, -2]
    list2 = []
    sorted_list1 = merge_sort(list1)
    sorted_list2 = merge_sort(list2)

    assert sorted_list1 == [-5, -2, 2, 4, 9, 81]
    assert sorted_list2 == []

# Tira Denis-Mihai
def binary_search(input_list, value, left, right):
    while left <= right:
        mid = (left + right) // 2
        if input_list[mid] == value:
            return mid

        if input_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return left

def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        val = input_list[i]
        pos = binary_search(input_list, val, 0, i)
        input_list = input_list[:pos] + [val] + input_list[pos:i] + input_list[i + 1:]
    return input_list

"""
    2. Find the smallest number in a list using a recursive divide & conquer implementation. Return None for an empty 
    list. Implement the following variants:
        a. Chip & conquer (data of size 1 and data of size n - 1)
        b. Divide the list into halves
"""
# Ungureanu Maia
def chipAndConquer(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    val1 = arr[0]
    val2 = chipAndConquer(arr[1:])
    return min(val1, val2)

def divideAndConquer(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    val1 = divideAndConquer(arr[:mid])
    val2 = divideAndConquer(arr[mid:])
    return min(val1, val2)

"""
    3. Calculate the r-th root of a given number x with a given precision p
"""
import cmath

# Timis Diana
def r_root(x, r, p):
    minVal = 0
    maxVal = x
    mid = (minVal + maxVal) / 2
    power = mid**r
    while abs(power - x) > p:
        if power < x:
            minVal = mid
        else:
            maxVal = mid
        mid = (minVal + maxVal) / 2
        power = mid**r
    return mid

"""
    4. Calculate the maximum subarray sum (elements of a subarray have consecutive indices in the parent array)
        a. Naive implementation
        b. Divide & conquer implementation
        c. Dynamic programming implementation (next week)

        e.g.
        for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""

"""
    Backtracking template

    We have a template that we need to customize.
        1. How is the search space represented (values in array X)
        2. When is array X consistent (consistent function)
            -> True if we can reach a solution strictly by adding values
            -> False otherwise
        3. When do we have a solution
            -> depends on the problem
"""

"""
    5. All permutations of the {0, 1, 2, ..., n - 1} set (recursive implementation)
    Searching space: X = [0, 1, 2, ..., n - 1]
"""


def consistent(x):
    """
    Determines whether the current partial array can lead to a solution
    """
    return len(set(x)) == len(x)


def solution(x, n):
    """
    Determines whether we have a solution
    """
    return len(x) == n


def solution_found(x):
    """
    What to do when a solution is found
    """
    print("Solution: ", x)


def bkt_rec(x, n):
    """
    Backtracking algorithm for permutations problem, recursive implementation
    """
    x.append(0)
    for i in range(0, n):
        x[len(x) - 1] = i
        if consistent(x):
            if solution(x, n):
                solution_found(x)
            else:
                bkt_rec(x[:], n)


# bkt_rec([], 4)

"""
    6. Change the code above to work for the n-Queen problem
    
    Board: NOT OK
    
    n = 6
    R1: Q _ _ _ _ _      => X[0] = 1
    R2: _ _ Q _ _ _      => X[1] = 3
    R3: _ _ _ _ Q _      => X[2] = 5
    R4: _ Q _ _ _ _
    R5: _ _ _ Q _ _
    R6: _ _ _ _ _ Q
    
    Conditions: 2 queens should not be on the same row
                2 queens should not be on the same column
                2 queens should not be on diagonal
                
    Searching space: X = [1, ....., n]
    X[i] = the column on which the queen from row i is placed
    
    Consistent: 1. It's already dealt with from the representation of the searching space
                2. X[i] != X[j], for all i != j
                3. |X[i] - X[j]| != |i - j|, for all i != j 
                
    Solution: len(X) = n, meaning that we have placed all the queens on the board
"""

# Tapordei Maia
def consistent(x):
    """
    Determines whether the current partial array can lead to a solution
    """
    j = len(x)-1
    for i in range(len(x)-1):
        if x[i]==x[j] or abs(x[i]-x[j])==abs(i-j):
            return False
    return True



def solution(x, n):
    """
    Determines whether we have a solution
    """
    return len(x) == n


def solution_found(x):
    """
    What to do when a solution is found
    """
    print("Solution: ", x)


def bkt_rec(x, n):
    """
    Backtracking algorithm for permutations problem, recursive implementation
    """
    x.append(0)
    for i in range(0, n):
        x[len(x) - 1] = i
        if consistent(x):
            if solution(x, n):
                solution_found(x)
            else:
                bkt_rec(x[:], n)



"""
    7. A Latin square is an n × n square filled with n different symbols, each occurring exactly once in each row and 
    exactly once in each column

    Generate all the N x N Latin squares for a given number N. 
"""

"""
    8. Generate all reduced N x N Latin squares for a given number N. In a reduced Latin square, the elements of the 
    first row and first column are sorted.
"""