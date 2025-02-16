# Solve the problem from the second set here
# problem 8 from set 2

def solve(): #sort of main function
    print("This program will calculate the smallest number from the Fibonacci sequence, but larger than a given number")

    n = userInput()

    print("The smallest number from the fibonacci sequence bigger than n is ", smallestFibonacci(n))

def userInput(): #function that takes the user's input
    try: #if you input an integer this works and it outputs the solution
        n = int(input("Input your number: "))
        if (n<=2):
            print("Input a number higher than 2.")
            return userInput()
        return n
    except ValueError: # Your input is something else than an integer, so try again
        print("Your input is not an integer. Input again")
        return userInput()

def smallestFibonacci(n): #function that calculates the desired value
    a, b = 1, 1 # the first two values of the fibonacci sequence
    # b is the last number calculated from the fibonacci sequence in an iteration
    while (b <= n):
        a, b = b, a+b
    
    #when b got bigger than n, then we can return it, that is the smallest number of the fib seq
    
    return b

solve()