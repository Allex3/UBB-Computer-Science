"""
    Input files:
    input1.txt : has 3, the example in the document too, to showcase it works
    input2.txt : has 6, a bigger example this time
    input3.txt : has 8, the maximum value for which to show the partitions
    input4.txt : has 30, a pretty big result
    input5.txt : has 100, to test a very large bell number
    You select what input file (1 to 5) to get the input from when you run the program
    And the results are in their respective output files (output follow by the same number as the input file, .txt)
"""

def getNumberOfPartitions(n: int) -> int:
    """
    Function to get the number of partitions of a set A
    """
    """
    The Bell number Bn counts the different ways to partition a set that has exactly n elements, or equivalently, it counts the number of equivalence relations on it.
    Let's denote by S(n, k) the number of ways to partition a set with n elements
        into k non-empty subsets (each partition has exactly k sets)
    Of course, by this definition, the Bell number Bn is the sum of all S(n, k) with k going from 0 to n (we get all the partitions with 1 set, 2 sets, ..., n sets, so basically all the possible partitions)
    
    This is helpful because those numbers S(n, k) can be calculated using a recurrent formula:
        S(n, k) = k*S(n-1, k) + S(n-1, k-1)
    Explanation:
        To obtain the number of partitions of a set with n elements that have exactly k sets from the previous iteration, i.e., the partitions of a set with n-1 elements into exactly k subsets
        First of all, we could have a set with n-1 elements and the same number of sets in the partitions, in which case, we add the new element in ANY set of the partition, and there are K sets, hence k*S(n-1, k)
        Secondly, we add the element to the set that has n-1 elements, but also partitions of k-1 sets, so in this way, the new element MUST go in a new set in the partition, so it's only 1*S(n-1, k-1)
    
    we can start by saying that S(1, 1) = 1, to start from there
    S(n, k) where k>n is always 0, you can't partition n elements into n+1 or n+2 or... elements, so always just iterate from 1 to the current cardinality 
        that we're checking, that is the k, no reason to go beyond that, it will always be 0
    
    But, we don't need a matrix of all the possible pairs that takes nxn memory
    It's enough to have a 2xn matrix, so the memory being occupied is way less
    because at every "row" denoted by n in S(n, k)
    we only use the row above it, i.e. S(n-1, k=1, 2, ..., n), where n is the current cardinality being checked
    So we only need two rows, and the final results will be at the end on the
        second row, which denotes S(n, k), where n=n and k=1, 2, ..., n
        The sum of that final row is the Bell number n, i.e., for our set A
    
    https://en.wikipedia.org/wiki/Bell_number
    https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind
    """
    #n is the length of set A, it's cardinality
    #I will use a dictionary with a pair of elements, instead of a matrix
    S = dict()
    #And at the end of each iteration for the current cardinality
    #   We will make the first row be equal to the current second row
    #   And the second row have only elements of value 0
    #This represents that we go "down" one row in the "matrix"
    #So let's define the two rows of the dictionary to have two rows of length n with all elements 0, representing rn S(1, k) and S(2, k), k=1, 2, .., n
    #   With S(2, k) all being 0, not calculated yet, and S(1, k) being all 0 beside S(1, 1)
    for i in range(0, n+1): #also start from 0 to be 0, because when k=1 it is accessed
        S[(1, i)] = 0
        S[(2, i)] = 0
    S[(1, 1)] = 1

    for i in range(2, n+1): #from 2 to n, (1, k) is 0 for any k>=2 and 1 for k=1 already
        for k in range(1, i+1): #1 to i; don't go beyond i, because everything is 0 there already
            #and we know that S(i, k) = 0 for any k>i
            S[(2, k)] = k*S[(1, k)] + S[(1, k-1)]
            # the above assignment <=> S(i, k) = k*S(i-1, k) + S(i-1, k-1)

        for k in range(1, i+1): #make the first row = the second row and reset the second row
            # Go only from 1 to i, the others were never used because i was only smaller
            # The elements bigger than i are 0, they were never worked with
            S[(1, k)] = S[(2, k)]
            S[(2, k)] = 0

    #Since after the last iteration, the second row that was calculated was moved in the first row
    #The S(n, k), k=1, 2, ..., n results are in S[(1, k)], k=1, 2, ..., n
    #As said before, add them up to obtain the bell number we return
    Bn = 0
    for k in range(1, n+1):
        Bn += S[(1, k)]

    return Bn

def getPartToRelStr(partition: list, eqRelGraph: list) -> str:
    outputStr = "{"
    for subset in partition:
        outputStr += "{"

        for elem in subset:
            outputStr += str(elem) + ", "
        # after it finished, the last elemennt will still have a ", " after it
        outputStr = outputStr[:-2]
        outputStr += "}, "

    #after it finished, the last subset will still have a ", " after it
    #so delete the last two characters from it, by getting only the characters before the last two like this
    outputStr = outputStr[:-2]
    if (len(partition) == 1): #it has only one subset, with all elements in it of course
        #so we just output } ⇝ AxA
        outputStr += "} ⇝ A × A\n"
        return outputStr


    outputStr += "} ⇝ ∆A" #finished a partition, write the prerequsiites for the graph, any eq. rel. graph contains the delta, atleast
    if eqRelGraph: #if the graph is not empty, append it
        outputStr += " ∪ {"
        for pair in eqRelGraph:
            outputStr += str(pair) + ", "

        # same situation here, delete the last colon with space before adding a "}\n" to end the row
        outputStr = outputStr[:-2]
        outputStr += "}\n"

    return outputStr



def writePartToRel(partition, eqRelGraph, fileNumber):
    outputFile = open(f"outputs/output{fileNumber}.txt", "a", encoding = "utf-8")
    #in append mode not to delete part

    #get the string to output first
    outputStr = getPartToRelStr(partition, eqRelGraph)

    outputFile.write(outputStr)

    outputFile.close()

def buildEquivalentRelation(partition: list) -> list:
    """
    Build an equivalent relation from a partition of a set
    """

    #an equivalent relation respects transitivity, reflexivity and symmetry
    #so we relate in the graph of the equivalent relation, every element with every other element:
    # So delta U {(1, 2), (2, 3), (1, 3), (3, 1), (2, 1), (3, 2)}
    # here reflexivity is respected, transitivity too, and simmetry too
    # (a, a) exists, (a, b) and (b, a) exists, and transitivity holds true for all elements
    #here the partition of the set contained the set itself
    #the delta is present already since it does not matter in which subset of the partition
    #   is a, it will ALWAYS, even if only by itself, (a, a) be present in the graph
    # so what we should do is relate any element orderly to any other element
    # in the subset we are in of the current partition, and add that to the graph we return

    eqRelGraph = []
    for subset in partition:
        for elem1 in subset:
            for elem2 in subset:
                if elem1!=elem2: #already in delta_A
                    eqRelGraph.append((elem1, elem2))

    return eqRelGraph


def computePartitions(A: list, partition: list, index: int, fileNumber: int):
    """
        Return all the partitions of the set {1, 2, ..., n}
    """
    """
        To generate all possible partitions of a given set, for each element in the set we will either add
        it to existing subsets or create a singleton subset and we will repeat this process for all
        elements in the sets until we have considered all the elements and will print each partition.
        
        I will add each set element in the main set A to either a current subset from the partition
        and I will do that iterating through the set partition, which contains subsets
        and add the current element at A[index], to the current subset we are at, then 
        run the function recursively, going to the next element
        
        outside the for that runs through all the current subsets of the partition 
        make the current element begin a NEW subset with itself
    """
    #everything is a list for the sake of easier implementation
    if (len(A)==index): #finished a partition, add it to the partitions list
        #work out the equivalence relation for the current partition and print it
        eqRelGraph = buildEquivalentRelation(partition)
        writePartToRel(partition, eqRelGraph, fileNumber) #write to the output file
        # writePartToEqRel(partition, equivalentRelation)
        return

    #for each subset in the partition, add the current element to it and callback
    for i in range(len(partition)): #run through the sets of the current partition
        partition[i].append(A[index])
        computePartitions(A, partition, index+1, fileNumber)
        partition[i].pop()

    # add the current element as a subset and callback
    partition.append([A[index]])
    computePartitions(A, partition, index+1, fileNumber)
    partition.pop()



def getDelta(n):
    delta = set()
    for i in range(1, n + 1):
        delta.add((i, i))
    return sorted(delta)  # sort it so that is shows the elems from (1, 1) to (n, n)



#user interaction

def output():
    """
    The function that outputs the results for problems 1 and 2
    """
    fileNumber = getUserInput() #the number of the input and its respective ouput
    inputFile = open(f"inputs/input{fileNumber}.txt", "r") #read from the file that contains the fileNumber'th input
    outputFile = open(f"outputs/output{fileNumber}.txt", "w") #write to the file that contains the output
    #"w" and not "a", since "w" deletes the content that was in the file
    n = int(inputFile.read())  # read the file input (cardinality of set A)
    inputFile.close()
    # 1. the number of partitions on a set A = {a1, a2, ..., an}
    #get the number of partitions on a set from the

    #For the sake of simplicy of not being able to write a_1, I will
    # use A={1, 2, ..., n}
    # and for the graph delta_A, I will use ∆ = {(1, 1), (2, 2), ..., (n, n)}

    A = set() #define a set with elements {1, 2, ..., n}
    for i in range(1, n+1):
        A.add(i)
    outputFile.write(f"1. The number of partitions on a set A = {A} is {str(getNumberOfPartitions(n))}\n") #where n = cardinality of set A, so
    #in our case, the set A={1, 2, ..., n}


    '''
    2. the partitions on a set A = {a1, . . . , an} and their corresponding equivalence relations (for n ≤ 8)
    So for n<=8, we run 1., and then we run 2., otherwise, stop the program here.
    '''

    if (n>8):
        outputFile.close()
        return
    """ ⇝
        We define ∆ = delta_A, but i can't write it in python, so 
        ∆ = {(1, 1), (2, 2), ..., (n, n)}, again, using k instead of a_k element to showcase it
    """
    delta = getDelta(n) #delta_A set
    partitions = [] #partitions will contain all the partitions of the set

    outputFile.close() #close it and open it in append mode
    outputFile = open(f"outputs/output{fileNumber}.txt", "a", encoding="utf-8")
    #before computing the permtutations, write the prerequisites
    #encoding to use delta char
    outputFile.write(f"2. using the notation ∆A = {delta}, the partitions on a set A = {A} and their corresponding equivalence relations are:\n")
    outputFile.close()

    computePartitions(list(A), [], 0, fileNumber) #compute all the partitions of the set {1, 2, ..., n}
    #and in the same function compute the equivalent relation for it, and write it to file
    #i do that because I don't want to return all the partitions here, too much space needed
    #that's why i give it the fileNumber

    outputFile.close()

def getUserInput():
    try:
        n = int(input("What input file do you want to run on (1-5): "))
        if (n<=0): #n not natural, ask again
            print("Your input is not a non-zero natural number. Try again")
            return getUserInput()
        elif (n>5): #input file above 5 does not exist
            print("Your input is not between 0-5. Try again")
            return getUserInput()
        return n
    except ValueError:
        print("Your input is not an integer. Try again")
        return getUserInput() #run recursively until you get an integer and return it (if try works)

if __name__ == '__main__':
    output()
