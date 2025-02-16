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

"""
    1. Implement an optimized version of the merge sort algorithm
        a. Implement Merge Sort
        b. Use the insertion sorting algorithm with the binary search optimization found in the lecture examples
        c. Time the resulting version using the ex17_sort_comparison.py example - at home
        d. Discuss how merging might be improved using exponential search
"""

#Mihet Marius
def binary_search(arr : list , k : int,st : int, dr : int):
    if st<dr:
        middle = (st+dr)//2
        if arr[middle] < k:
            return binary_search(arr,k,middle+1,dr)
        elif arr[middle] > k:
            return binary_search(arr,k,st,middle-1)
        else:
            return middle
    return st

def insertion_sort(arr : list):
    for i in range(len(arr)):
        k = arr[i]
        pos = binary_search(arr, k,0,i)
        arr = arr[:pos] + [k] + arr[pos:i] + arr[i + 1:]
    return arr


# Miron Bogdan
# Time Complexity: O(n*log(n))
def merge_sort(arr : list, threshold=10):
    if len(arr) < 2:
        return arr

    if len(arr) < threshold:
        return insertion_sort(arr)

    middle = len(arr) // 2
    lower = merge_sort(arr[:middle])
    upper = merge_sort(arr[middle:])
    return merge(lower, upper, arr)

def merge(list1, list2, resultList):
    if list1 == None or list2 == None:
        return resultList

    len1 = len(list1)
    len2 = len(list2)
    resultList = []
    i = 0
    j = 0
    while i < len1 and j < len2:
        if list1[i] < list2[j]:
            resultList.append(list1[i])
            i += 1
        else:
            resultList.append(list2[j])
            j += 1
    while i < len1:
        resultList.append(list1[i])
        i += 1
    while j < len2:
        resultList.append(list2[j])
        j += 1
    return resultList

"""
    2. Find the smallest number in a list using a recursive divide & conquer implementation. Return None for an empty 
    list. Implement the following variants:
        a. Chip & conquer (data of size 1 and data of size n - 1)
        b. Divide the list into halves
"""

#Mocrei Bogdan

def find_chip(arr):
    if arr == None or len(arr) == 0:
        return None

    if len(arr) == 1:
        return arr[0]

    return min(find_chip(arr[1:]), arr[0])

def find_halves(arr):
    if arr == None or len(arr) == 0:
        return None

    if len(arr) == 1:
        return arr[0]

    middle = len(arr) // 2
    return min(find_halves(arr[:middle]), find_halves(arr[middle:]))

def main():
    #x = [7, -2, 10, 15, 81, -10]
    # sorted = merge_sort(x)
    #sorted = insertion_sort(x)
    #print(sorted)

    x = [4, 6, -1, 5, 7]
    print(find_chip(x), ' ', find_halves(x))

if __name__ == "__main__":
    main()

"""
    3. Calculate the r-th root of a given number x with a given precision p
"""

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
    5. All permutations of the {0, 2, ..., n - 1} set (recursive implementation)
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
    
    Board: 
    n = 7
    R1: _ _ _ _ _ _ Q
    R2: Q _ _ _ _ _ _
    R3: _ _ Q _ _ _ _
    R4: _ _ _ _ Q _ _
    R5: _ Q _ _ _ _ _
    R6: _ _ _ Q _ _ _
    R7: _ _ _ _ _ Q _
    
    
    Conditions: 
        not to have 2 queens on the same row
        not to have 2 queens on the same column
        not to have 2 queens on diagonal
        
    Search Space: X = [1, ....., n]
    X[i] = on what column is the queen from row i
    
    Consistent:    X - should have unique values
                   X[i] != X[j], for all i != j
                   |X[i] - X[j]| != |i - j|, for all i, j in our searching space
                   
    Solution: When len(X) = n, meaning that all queens are placed
"""

#Mateian Andrei
def consistent(x):
    """
    Determines whether the current partial array can lead to a solution
    """

    for i in range(len(x)-1):
        if x[i]==x[len(x)-1]:
            return False
        if abs(x[i]-x[len(x)-1]) == abs(i-len(x)-1):
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