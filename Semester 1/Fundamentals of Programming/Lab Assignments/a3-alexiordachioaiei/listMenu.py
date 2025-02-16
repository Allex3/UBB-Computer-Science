#A menu that gets a random list of a length that the user chooses
# 1 - Generate a list of numbers from 0-1000
# 2 - Search a number in the list
# 3 - Permutation sort the list and say what steps to show
# 4 - Shell sort the list and tell the program what steps to show
# 5 - Close the program

import random
import timeit
from xml.etree.ElementTree import tostring

from texttable import Texttable


def generateList(listLength) -> list[int]:
    numberList = []
    for index in range(listLength): #generate a random number for each index of the list and append it
        numberList.append(random.randint(0, 1000))

    return numberList

def binarySearch(numberList, number, left, right) -> int:
    if (left > right): #the number is not in the list since we reached the "closest" element to it
        #but then the algorithm "broke" and the left got higher than the right, showing the element is not in the list
        return -1

    mid = (left+right)//2 #the middle of the iterators, check if the number is to the left or right of it
    #since the list is sorted, if list[mid] is higher than the number, then the number is to the left of mid, so subtract from the right iterator (right=mid-1)
    #otherwise it will be to the right of mid, so make the left iterator come more to the right side (left=mid+1)

    if (numberList[mid] == number):  # number found at current mid-position
        return mid  # return the index at which the number is in the list
    elif numberList[mid] > number:
        return binarySearch(numberList, number, left, mid-1) #make right mid-1 in the next call
    else: #numberList[mid]<number
        return binarySearch(numberList, number, mid+1, right)

def binarySearchRecursive(numberList, number) -> int:
    listLength = len(numberList)
    index = binarySearch(numberList, number, 0, listLength-1)

    return index #index of the number or -1 if number not in list

def isSorted(numberList) -> bool:
    #if we find even a number that's > than the next one then the list is not sorted
    listLength = len(numberList)
    for index in range(listLength-1): #go from 0 to listLength-2
        if (numberList[index] > numberList[index+1]):
            return False

    return True


def getSortedPermutation(numberList: list, permutation: list, contains: list, step: int, currStep: list, sortedList: list) -> None:
    if sortedList: #of course, we stop the permutation calculations when we found the sorted list
        #that is, when the sorted list is not empty
        return
    #currStep is a list just to keep count of it between function calls better, but it has only 1 element
    foundSorted = False
    listLength = len(numberList)
    for index in range(listLength):
        if not contains[index]: #the permutation doesn't contain the number on the current index
            permutation.append(numberList[index])
            contains[index] = True
            if (len(permutation) == listLength): #we reached a permutation since it is as long as the list
                currStep[0]+=1  #keep count of the current step (current permutation number)
                if (currStep[0]%step==0 and step!= -1): #we print every step'th step
                    printStepPermutation(currStep[0], permutation)

                if (isSorted(permutation)):
                    #print the step we found the solution at put the sorted list in sortedList
                    if step!= -1:
                        printSorted(currStep[0], permutation)
                    for number in permutation: #put the sortedList in the list
                        #and make the bool variable foundSorted = True
                        sortedList.append(number)

            else:
                getSortedPermutation(numberList, permutation, contains, step, currStep, sortedList) #form a new permutation using the existing one

            permutation.pop()
            contains[index] = False


def permutationSort(numberList : list[int], step: int) -> list[int]:
    # the sorted list will be in the sortedList list and we return it
    sortedList = []

    #now we run a while loop until we find the permutation that is the list sorted
    contains = [False] * len(numberList) #use this frequency list to see if the index of the number from the list is visited
    #or not in the permutation

    permutation = [] #define the list here only to modify it in the generating algorithm
    getSortedPermutation(numberList, permutation, contains, step, [0], sortedList)

    return sortedList


def shellSort(numberList, step) -> None: #the sorted list will be in numberList list
    listLength = len(numberList)
    gap = listLength//2

    #use a sort of insertion sort put for elements at the distance of "gap" between them
    #practically running an insertion sort but instead of checking for consecutive elements
    #we check them at a "gap" distance between them

    currStep = 1
    while (gap > 0): #the gap will become len/4, len/8... until it is 1, then do the final insertion sort
        #and then it will be 0, so we exit the loop
        for index in range(gap, listLength): #go through each element of the list starting from gap
            #and check consecutively bigger elements than it, to its right, but at the GAP
            #this is an insertion sort, but instead of checking every previous element
            #we check this sequence at a gap
            #also, begin at gap and not 0, because we check an element at j-gap
            #so it would be useless if index<gap, index-gap=j-gap < 0, so index out of bounds

            j = index #the currently checked element will be in numberList[j]
            #and with each iteration, we swap the element numberList[j] with numberList[j-gap]
            # and then, as is in insertion sort, subtract gap from j (j-=gap)
            # naturally, because of this, the currently checked element will be now in numberList[j] again
            # this will happen of course until we are out of the list
            #run the while ONLY if the element to its left is bigger than itself
            #and stop when we reach an element lower than it

            #successfully inserting the currently checked element before the sequence
            #of higher numbers to its left, thus it is now smaller than those elements that are now to its right

            #then go to the next element of the list and check elements beginning from there at a gap

            #run while j-gap>=0 so it is still in the list
            while (j>=gap) and (numberList[j-gap] > numberList[j]):
                numberList[j-gap], numberList[j] = numberList[j], numberList[j-gap]
                j-=gap
                currStep+=1 #let's say the step is at each swapping of elements
                if currStep%step==0 and step != -1:
                    printStepShell(currStep, numberList) #print current step
        #when the gap reaches one we have to, at most, swap an element with the one to its left
        #the rest are sorted
        #after we checked all the possible elements from the current gap, halve it
        gap//=2
    if step!=-1:
        printSorted(currStep, numberList) #print sorted list and its step

def bestComplexity() -> Texttable:
    #returns a texttable with the times for each of the 5 random lists
    #for each of the 3 algorithms (beside time there will be the number of terms)
    #because the starting terms are different for each algorithm


    """
    1. Binary search (recursive) - Omega(1)
        - the best case happens when the element is directly at the first function call
        - i.e. at the middle point of the sequence (rounded lower from 0.5 if element count is even)
    2. Permutation sort - Omega(1)
        - The best case happens when the first permutation is the sorted list
        - i.e. when the list is sorted
    3. Shell sort - Omega(nlogn)
        - The best case happens when the list is already sorted
        - The innermost while does not start since there are no bigger elements to the left of any element, if the list is sorted
        - The inner for runs n-gap times, each time, for all the gaps from the upper while, so we have a complexity of Theta(n-gap), for every gap, so this transfers to Theta(n)
        - The uppermost while runs for each gap divided each time by 2, so Theta(logn)
        Thus Omega(nlogn)
    """

    #now on the sorted list run the algorithms
    #if we call the algorithms with step = -1 we don't prin anything

    table = Texttable()
    #set up the table
    table.add_row(['No. of terms for Shell & BS', 'No of terms for Perm',  'Binary search', 'Permutation sort', 'Shell sort'])

    ShellBSStartLen = 10 ** 4
    PermStartLen = 1
    for i in range(0, 5):
        testListShell = generateList(ShellBSStartLen)
        testListBS = generateList(ShellBSStartLen)
        testListPerm = generateList(PermStartLen)
        ShellBSStartLen *= 2
        PermStartLen *= 2
        if PermStartLen > 8:  # if above 8 make it 10
            PermStartLen = 10

        testListBS.sort()
        testListPerm.sort()
        testListShell.sort()

        start_bs = timeit.default_timer()
        binarySearchRecursive(testListBS, testListBS[(0 - 1 + len(testListBS)) // 2])
        end_bs = timeit.default_timer()
        start_permutation = timeit.default_timer()
        permutationSort(testListPerm, -1)
        end_permutation = timeit.default_timer()
        start_shell = timeit.default_timer()
        shellSort(testListShell, -1)
        end_shell = timeit.default_timer()
        # round the seconds with 3 digits to get 3 digits of the ms (0,abc in s)
        # I give up trying to format these into seconds
        table.add_row([len(testListShell), len(testListPerm), str(1000 * round((end_bs - start_bs), 3)) + 'ms',
                       str(1000 * round((end_permutation - start_permutation), 3)) + 'ms',
                       str(1000 * round((end_shell - start_shell), 3)) + 'ms'])

    return table
         


def worstComplexity() -> Texttable:
    """
        1. Binary Search (recursive) - T(n) = log n
            - The list is already sorted!
            - Gets the middle point between, at first, indexes 0 and listLength-1 (last index)
            - If the number is not at the middle point, the list being sorted, it must be in either the left or right side, so if it is smaller than the middle point, it's on the left side, if it's higher than the number at the middle point, it's on the right side
            - The worst case here would be if we have to keep halving the intervals we look in (i.e. going in either the left or right one) the maximum number of times, that is, when the element is at the end or beginning of the list
                * Though, if the list has an even number of elements, the last element gives the worst complexity, because by doing 0+(n-1)/2 , n being even, the result would have a .5, but we round it down, so basically the middle point would be the last element in the first n/2 elements interval, thus we search faster for the first element (going to the left), then the last one
                *But if the number of terms is odd, then the middle point is "accurately" at the middle of the list, so both the first and last element give the worst case complexity!
            - So what happens when you start at the middle of something and just halve it continuously until you reach the elements at the end of it?
                you divide n by 2 until it reaches 1, i.e. log of base 2 of n
        O(logn), so we started with a sorted list for BS, from 10k to 160k elems

        2. Permutation sort
            - Since each permutation starts with the first element with the list, and then after it ran all permutations with that one, get those starting fromt he second element, etc.,
                The worst case happens when the smallest element is on the last position, and then the second smallest on the n-2 positions, etc.
                So the worst case happens when the list is sorted but in reverse, decreasingly => it runs all permutations, so O(n!)
        O(n!)

        3. Shell sort
            - We already know from the best case complexity that it has to run atleast nlogn times, approximatively, but then, if the list is sorted but in reverse, every element will have bigger elements than itself to its left, going until the very ends of the sequence with the gaps
            - So the while
            the inner while loop runs at most n/currgap iterations
                because you compare elements at a gap
            so in the upper for , the inside of it runs for n*n/currgap, at most
            (n/2 times at most, that is the gap, but its part of O(n))
            but the currgap is taken from the upper for itself, let's iterate through it
            so we'd have n^2+n^2/2+n^2/4+...+n^2/(n//2)) <= 2n^2 which is part of O(n^2)
        O(n^2)

        for this, shell sort and BS will use the same lists length, but not the smae lists, since BS lists have to be sorted (100k to 1.6m elems)
        and perm sort, since it is n! here, will lists of 1, 2, 4, 8, 12



    """

    table = Texttable()
    # set up the table
    table.add_row(
        ['No. of terms for Shell & BS', 'No of terms for Perm', 'Binary search', 'Permutation sort', 'Shell sort'])

    ShellBSStartLen = 10 ** 4
    PermStartLen = 1
    for i in range(0, 5):
        testListShell = generateList(ShellBSStartLen)
        testListBS = generateList(ShellBSStartLen)
        testListPerm = generateList(PermStartLen)
        ShellBSStartLen *= 2
        PermStartLen *= 2
        if PermStartLen > 8:  # if above 8 make it 10
            PermStartLen = 10

        testListBS.sort()
        testListPerm.sort(reverse = True)
        testListShell.sort(reverse = True)

        start_bs = timeit.default_timer()
        binarySearchRecursive(testListBS, testListBS[len(testListBS)-1])
        end_bs = timeit.default_timer()
        start_permutation = timeit.default_timer()
        permutationSort(testListPerm, -1)
        end_permutation = timeit.default_timer()
        start_shell = timeit.default_timer()
        shellSort(testListShell, -1)
        end_shell = timeit.default_timer()
        # round the seconds with 3 digits to get 3 digits of the ms (0,abc in s)
        #I give up trying to format these into seconds
        table.add_row([len(testListShell), len(testListPerm), str(1000 * round((end_bs - start_bs), 3)) + 'ms',
                       str(1000 * round((end_permutation - start_permutation), 3)) + 'ms',
                       str(1000 * round((end_shell - start_shell), 3)) + 'ms'])

    return table

def averageComplexity() -> Texttable:

    table = Texttable()
    # set up the table
    table.add_row(
        ['No. of terms for Shell & BS', 'No of terms for Perm', 'Binary search', 'Permutation sort', 'Shell sort'])

    ShellBSStartLen = 10**4
    PermStartLen = 1
    for i in range(0, 5):
        testListShell = generateList(ShellBSStartLen)
        testListBS = generateList(ShellBSStartLen)
        testListPerm = generateList(PermStartLen)
        ShellBSStartLen*=2
        PermStartLen*=2
        if PermStartLen > 8: #if above 8 make it 10
            PermStartLen = 10

        testListBS.sort()
        x = random.randrange(0, len(testListBS))

        start_bs = timeit.default_timer()
        binarySearchRecursive(testListBS, testListBS[x])
        end_bs = timeit.default_timer()
        start_permutation = timeit.default_timer()
        permutationSort(testListPerm, -1)
        end_permutation = timeit.default_timer()
        start_shell = timeit.default_timer()
        shellSort(testListShell, -1)
        end_shell = timeit.default_timer()

        # round the seconds with 3 digits to get 3 digits of the ms (0,abc in s)
        #I give up trying to format these into seconds
        table.add_row([len(testListShell), len(testListPerm), str(1000 * round((end_bs - start_bs), 3)) + 'ms',
                       str(1000 * round((end_permutation - start_permutation), 3)) + 'ms',
                       str(1000 * round((end_shell - start_shell), 3)) + 'ms'])

    return table
        
# User interaction part

def printComplexity(caseTable: Texttable)-> None :
    print(caseTable.draw()) #draw the table for the current case (best, average or worst)

def printSorted(stepNumber: int, sortedList: list):
    print(f"The sorted list has finished computing at step {stepNumber}:  {sortedList}")

def printStepPermutation(stepNumber: int, listAtStep: list):
    print(f"The progress of sorting the list at step (permutation) {stepNumber} is {listAtStep}")

def printStepShell(stepNumber: int, listAtStep: list):
    print(f"The progress of sorting the list at step (insertion) {stepNumber} is {listAtStep}")

def menu():
    print("The list has 5 options:")
    print("1 - Generate a list of random numbers from 0-1000")
    print("2 - Search a number in the list")
    print("3 - Permutation sort the list and say what steps to show")
    print("4 - Shell sort the list and tell the program what steps to show")
    print("Options 5, 6, 7 print the time complexities for the searching and sorting algorithms present\nUsing 5 different lists, each next one being double as the previous one")
    print("5 - Print the best case complexity for the algorithms.")
    print("6 - Print the worst case complexity for the algorithms.")
    print("7 - Print the average case complexity for the algorithms.")
    print("0 - Close the program\n")

    close = False
    isSortedBool = False
    numberList = []
    listLength = 0
    while not close:
        try:
            option = int(input("Write an option from the list: "))
        except ValueError:
            print("Your input isn't even an integer. Input again")
            continue

        match option:
            case 1:
                isSortedBool = False
                listLength = int(input("What length should your list be: "))
                numberList = generateList(listLength)
                print("Your list is", numberList)
            case 2:
                if not numberList: #list is empty
                    print("The list is empty.")
                    continue # go to the beginning of the while loop
                if not isSortedBool:
                    print("The list is not sorted, sort it first.")
                    continue

                number = int(input("Input the number you are looking for: "))
                numberIndex = binarySearchRecursive(numberList, number)
                if numberIndex==-1: #the number is not in the list
                    print("The number is not in the list :'( ")
                else:
                    print("The number you are looking for is at position ", numberIndex)

            case 3:
                if not numberList:  # list is empty
                    print("The list is empty.")
                    continue  # go to the beginning of the while loop

                step = int(input("Write the step at which to show the progression of the sorting: "))
                numberList = permutationSort(numberList, step) #return to numberList a new sorted list

                isSortedBool = True
            case 4:
                if not numberList:  # list is empty
                    print("The list is empty.")
                    continue  # go to the beginning of the while loop

                step = int(input("Write the step at which to show the progression of the sorting: "))
                shellSort(numberList, step) #the sorted list will already be in numberList (mutable)


                isSortedBool = True
            case 5:
                table = bestComplexity()
                printComplexity(table)
            case 6:
                table = worstComplexity()
                printComplexity(table)
            case 7:
                table = averageComplexity()
                printComplexity(table)
            case 0:
                close = True
            case _: # the input is not a number from 1 to 6
                print("The inputted option is not in the menu. Try again.")


if __name__ == '__main__':
    menu()