import numpy as np
import matplotlib.pyplot as plt

#Try with the convex function x^2, (x^2)' = 2x, (2x)' = 2 >= 0 => if it's second derivative is >=0, the function is convex

def get_convex_function(x):
    return x**2

def get_convex_function_derivative(x):
    return 2*x

def get_non_convex_function(x):
    return x**4-3*(x**2)+x #f'(x) = 4x^3-6x+1
    #f''(x) = 12x^2-6, <0 for x^2<1/2, x from (-1/sqrt2, 1/sqrt2) is concave
    #so f is not convex on R, and near 0 there are 2 minimum points on the graph
    # one is the global minimum, the other a local minimum, let's plot it

def get_non_convex_function_derivative(x):
    return 4*(x**3)-6*x+1

def gradient_descent(x1, eta, max_iterations, f_der):
    x_terms = list() #list of the terms of the sequence x
    x_terms.append(x1) #add the first term to the sequence, then run the recurrence
    precision = 0.0001 #take a precision of 10^-4
    #if the difference between two sequence terms is smaller than this
    # then we sort of "reached" the convergence, it's clear what it converges to
    for i in range(2, max_iterations):
        x_next = x_terms[-1] - eta*f_der(x_terms[-1])
        x_terms.append(x_next)
        if (x_terms[-1] > x_terms[-2]): #x_n < x_(n+1) case
            if (x_terms[-1] - x_terms[-2] < precision):
                break
        else: #x_n > x_(n+1) #descending case, do the difference in opposite order
            if (x_terms[-2] - x_terms[-1] < precision):
                break

    return np.array(x_terms) #return the sequence as an array of numpy

def plot_gradient_descent(x_terms, f, title):
    x_range = np.linspace(-2, 2, 1000)
    y_range = f(x_range)

    plt.figure(figsize=(10, 6))
    if f==get_convex_function:
        plt.plot(x_range, y_range, label='x^2')
    else:
        plt.plot(x_range, y_range, label='x^4-3x^2+x')
    plt.plot(x_terms, f(x_terms), 'o-', color='red', label='Gradient descent path')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def print_menu():
    print("(a) Take a particular convex function f and show that for a small value of η the method converges to the minimum of f")
    print("(b) Show that by using a larger η the method can converge faster (in fewer steps).")
    print("(c) Show that taking η too large might lead to the divergence of the method.")
    print("(d) Take a particular nonconvex function f and show that, depending on the starting value, the method can end up in a local minimum, not in the global minimum.")
    print("(Exit) Write 0 to exit the application")

def solve():
    max_iterations = 100 #let's say we will approximate the gradient descent for the first 100 terms of the sequence x_n

    print_menu()
    while (True):
        option = input("Input what part of the question you want to solve (a, b, c, d): ")
        #we will see on the graph that will show for each option
        # how the sequence converges to the value that is also the minimum
        # on the function's graph
        if option=="a":
            x1 = 1000  # let's take 100 as a starting value of the gradient descent sequence
            eta = 0.1  # take a small eta first
            # f'(x) > 0, so x_(n+1) < x_n, for x>0, which we will take
            x_terms = gradient_descent(x1, eta, max_iterations, get_convex_function_derivative)
            plot_gradient_descent(x_terms, get_convex_function, f"Convergence to minimum with small eta={eta}") # run and plot the gradient descent for the starting value x1 with the step size eta, for iterations terms
            print(f"The gradient descent converges to the minimum of the convex function in {len(x_terms)} terms of the x sequence, for eta = {eta} starting at x1 = {x1}")

        elif option=="b":
            x1 = 1000
            eta = 0.3 #larger eta, 5 times as large, same starting point
            x_terms = gradient_descent(x1, eta, max_iterations, get_convex_function_derivative)
            plot_gradient_descent(x_terms, get_convex_function,f"Convergence to minimum faster with larger eta={eta}")
            print(f"The gradient descent converges to the minimum of the convex function in {len(x_terms)} terms of the x sequence, for eta = {eta} starting at x1 = {x1}")

        elif option=="c":
            x1 = 1000
            eta = 4  # eta too large, x_n will diverge
            x_terms = gradient_descent(x1, eta, max_iterations, get_convex_function_derivative)
            plot_gradient_descent(x_terms, get_convex_function,f"Divergence to infinity of the sequence for eta too large = {eta}")
            print(
                f"The gradient descent diverges, since it didn't stop until the maximum iterations, there are {len(x_terms)} = {max_iterations}-1 terms of the x sequence, for eta = {eta} starting at x1 = {x1}.")
            print(f"It diverges to {x_terms[-1]}")
        elif option=="d":
            #The critical points that give the local and global minimum
            #Are, the global around -1 - -1.3, and the local arounc 1 - 1.3
            #So I will start with the value 0.5, to see if it converges to the local minimum
            #Since it is closer to it than to the global minimum
            x1 = 0.5
            eta = 0.01
            x_terms = gradient_descent(x1, eta, max_iterations, get_non_convex_function_derivative)
            plot_gradient_descent(x_terms, get_non_convex_function, f"Convergence to a local minimum instead of a global one depending on the starting value of x, x1={x1}, eta={eta}")
            print(f"The gradient descent converges to a local minimum of the function instead of the global minimum for x1={x1} starting point and eta={eta}, in {len(x_terms)} terms of the x sequence")
        elif option=="0":
            return






if __name__ == "__main__":
    solve()