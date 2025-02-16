#A menu that gets a random list of a length that the user chooses
# 1 - Generate a list of numbers from 0-1000
# 2 - Search a number in the list
# 3 - Permutation sort the list and say what steps to show
# 4 - Shell sort the list and tell the program what steps to show
# 5 - Close the program

import random


def generateList(listLength) -> list[int]:
    numberList = []
    for index in range(listLength): #generate a random number for each index of the list and append it
        numberList.append(random.randint(0, 1000))

    return numberList

def binarySearchRecursive(numberList, number, left, right) -> int:
    if (left > right): #the number is not in the list since we reached the "closest" element to it
        #but then the algorithm "broke" and the left got higher than the right, showing the element is not in the list
        return -1

    mid = (left+right)//2 #the middle of the iterators, check if the number is to the left or right of it
    #since the list is sorted, if list[mid] is higher than the number, then the number is to the left of mid, so subtract from the right iterator (right=mid-1)
    #otherwise it will be to the right of mid, so make the left iterator come more to the right side (left=mid+1)

    if (numberList[mid] == number):  # number found at current mid-position
        return mid  # return the index at which the number is in the list
    if numberList[mid] > number:
        return binarySearchRecursive(numberList, number, left, mid-1) #make right mid-1 in the next call
    else: #numberList[mid]<number
        return binarySearchRecursive(numberList, number, mid+1, right)

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
                if (currStep[0]%step==0): #we print every step'th step
                    printStepPermutation(currStep[0], permutation)

                if (isSorted(permutation)):
                    #print the step we found the solution at put the sorted list in sortedList
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
                if currStep%step==0:
                    printStepShell(currStep, numberList) #print current step
        #when the gap reaches one we have to, at most, swap an element with the one to its left
        #the rest are sorted
        #after we checked all the possible elements from the current gap, halve it
        gap//=2
    #the inner while loop runs at most n/currgap iterations
    #so in the upper for , the inside of it runs for n^2/currgap
    #but the currgap is taken from the upper for itself, let's iterate through it
    #so we'd have n^2+n^2/2+n^2/4+...+n^2/(n//2)) <= 2n^2 which is part of O(n^2)
    printSorted(currStep, numberList) #print sorted list and its step

        
# User interaction part

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
    print("5 - Randomize the list")
    print("6 - Close the program\n")

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
                numberIndex = binarySearchRecursive(numberList, number, 0, listLength-1)
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
                if not numberList:
                    print("The list is empty.")
                    continue
                random.shuffle(numberList) #randomize the list again, for whatever reason
            case 6:
                close = True
            case _: # the input is not a number from 1 to 6
                print("The inputted option is not in the menu. Try again.")


menu()