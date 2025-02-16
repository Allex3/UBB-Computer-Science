
"""
Iterative and Recursive + Explain the time complexity for each

Problem 11

Two natural numbers m and n are given. Display in all possible modalities the numbers from 1 to n, such that between any two numbers on consecutive positions, the difference in absolute value is at least m. If there is no solution, display a message.
"""

def userInput() -> tuple:
    try:
        n = int(input("n: "))
        m = int(input("m: "))
        if (n<=0 or m<=0):
            print("Your values should be higher than 0. Try again")
            return userInput()
        return tuple([n, m])
    except ValueError:
        print("Your values are not numbers. Try again")
        return userInput()


# T(n) = n!
# if m = 1, it looks through all the possible permutations of (1, 2, ..., n)
# so the worst case time complexity is O(n!) when m=1, it HAS to run through all the possible permutations

#The best case happens when m is large, because we know when m>=n there are NO solutions from the start
#there are no numbers from 1 to n for which their difference is >= m
# the largest there can be is n - 1, which is < n, and it is O(1)
#if m<=n but it is very large, the time complexity is exponentially better
# because we don't call as many recursive calls, thus not checking as many times the numbers from 1 to n again

def bktIterative(n:int, m:int) -> None:
    solutionExists = bktIterativeImpl(n, m)
    # solutionExists turns True if there is atleast a solution found and printed
    if not solutionExists:
        print(
            "There is no modality to display the numbers from 1 to n such that between any two numbers on consecutive positions, the difference in absolute value is at least m")

#The worst time complexity again happens when m=1, and best when m>=n
#The rest it's the exact same algorithm, but the function stack is simulated iteratively
def bktIterativeImpl(n: int, m: int) -> bool:
    if (m>=n):
        return False

    solutionExists = False
    stack: list[tuple[list[int], set[int]]] = list()
    for i in range(1, n+1):
        stack.append(([i], {i}))
    #first has all the possible modalities with their associated usedNumbers
    #because if we use an empty list with an empty set it would be seen as False
    #and if we put [1] and {1} all the modalities have to start with 1, so put all the base cases

    while stack: #while stack of sequences is NOT empty (basically simulate the recursive function)
        currModality, usedNumbers = stack.pop() #pop the currently checked sequence from the stack and use it
        if (len(currModality) == n):
            print(currModality)
            solutionExists = True
            continue #popped from the stack, go to the next modality from the stack

        for i in range(1, n+1): #iterate through the numbers from 1 to n
            if (not currModality or abs(currModality[-1] - i) >= m) and i not in usedNumbers:

                newModality = currModality[:] #make a copy of the list and add i to it
                newModality.append(i)
                newUsedNumbers = usedNumbers | {i} #union of the set of used numbers with the number i to put i in it
                stack.append((newModality, newUsedNumbers)) # put it on the stack to check it after

    return solutionExists #returns true if there is atleast a solution

def bktRecursiveImpl(n: int, m: int, currModality: list, elemInCurrModality: list, solutionExists: list) -> None:
    if (m>=n):
        return
    if len(currModality) == n: #all numbers from 1 to n here, so print the solution
        solutionExists[0] = True
        print(currModality)
        return

    for i in range(1, n+1):
        if (not currModality or abs(currModality[-1] - i) >=m) and not elemInCurrModality[i]:
            #so either the current modality is empty or the difference between the last element added
            #and the current element we want to add, is at least m, append it to the current modality
            #and then go to the next element to add
            elemInCurrModality[i] = True # True if the current number IS in the current modality
            #because the numbers have to be unique, all from 1 to n, not duplicates
            currModality.append(i)
            bktRecursiveImpl(n, m, currModality, elemInCurrModality, solutionExists)
            currModality.pop() #come back and remove the last element added now, to add a new one
            #on the SAME position
            elemInCurrModality[i] = False


def bktRecursive(n:int, m:int) -> None:
    solutionExists = [False]
    bktRecursiveImpl(n, m, [], [False]*(n+1), solutionExists)
    #solutionExists turns True if there is atleast a solution found and printed
    if not solutionExists[0]:
        print("There is no modality to display the numbers from 1 to n such that between any two numbers on consecutive positions, the difference in absolute value is at least m")


def solve():
    n, m = userInput()
    option = int(input("Choose 1 for iterative approach or 2 for recursive approach: "))
    if (option == 1):
        bktIterative(n, m)
    elif (option==2):
        bktRecursive(n, m)
    else:
        print("Not 1 or 2. Try again")


if __name__=="__main__":
    solve()