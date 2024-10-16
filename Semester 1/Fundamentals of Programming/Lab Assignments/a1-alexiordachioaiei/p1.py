# Solve the problem from the first set here
#problem 4 from set 1

def solve(): #function that takes the number and prints the solution
    print("This is a program that calculates the largest number written with the digits of the number you will provide it")

    n = userInput()

    print("The biggest number made out of n's digits is ", greatestNumber(n))

def userInput(): #function that takes the user's input
    try: #try to get the user's integer input
        n = int(input("Input your number: "))
        if (n<0):
            print("Your input is not a natural number, it's negative. Input again")
            return userInput()
        return n
    except ValueError: # Your input is something else than an integer, so try again
        print("Your input is not an integer. Input again")
        return userInput()
    


def getDigits(n) -> list[int]:  #function that gets the number's digits count
    # split the number into a list of its digits
    # by dividing it by 10 to get to the next digit and so on until the number is 0
    digitsCount = [0] * 10 #set up a list of 10 values of 0
    #this list will contain the count of each digit from the number
    #so for each digit of the number we will add 1 to it's corresponding index
    while (n):
        digitsCount[n%10]+=1
        n//=10
    
    return digitsCount #return the list of the frequency of the number's digits

def greatestNumber(n : int) -> int: #function that calculates the greatest number formed from n's digits
    result : int = 0 # this variable will contain the result
    digitsCount : list[int] = getDigits(n) #get a list of the frequency of the digits of the number
    for digit in range(9, -1, -1): #traverse the count of each digit in the list 
        #in descending order (from 9 to 0, because we want to build the biggest number)
        while (digitsCount[digit]): #iterate the digit the number of times it appears in the number 
            result = result*10+digit #add the digit to the result
            digitsCount[digit]-=1 

    return result

solve()