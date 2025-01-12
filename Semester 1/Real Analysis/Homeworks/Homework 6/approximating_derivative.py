import numpy as np

def get_f(x: float) -> float:
    return x**3+x**2

def get_f_derivative(x: float) -> float:
    return 3*(x**2)+2*x

def get_forward_difference(x: float, h: float) -> float:
    return (get_f(x+h)-get_f(x))/h

def get_centered_difference(x: float, h: float) -> float:
    return (get_f(x+h)-get_f(x-h))/(2*h)

def solve():
    print("Our function is f(x) = x^3+x^2")
    # Let's take the point x to be 1, and see the difference between the real derivative and the approximations
    # That difference is the error
    x = float(input("Take the derivative at x = ")) # 1 for example

    f_der_x = get_f_derivative(x)
    print(f"\nWe are trying to approximate f'(x) at x = {x}, so f'({x}) = {f_der_x}")
    print()
    #take 5 small values h: 0.1, 0.05, 0.02, 0.01 and 0.005
    # The errors should be a multiple of h for the forward difference, and a multiple of h^2 for the centered difference
    h = [0.1, 0.05, 0.02, 0.01, 0.005]
    for i in range(5): #take 5 small values h: 0.1, 0.05, 0.025, 0.0125,
        forward_difference = get_forward_difference(x, h[i])
        centered_difference = get_centered_difference(x, h[i])
        print(f"We will use h = {h[i]}, so h^2 = {h[i]**2}")
        print(f"The forward difference is {forward_difference}, and it approximates f'({x}) with an error of {abs(forward_difference-f_der_x)}")
        print(f"The centered difference is {centered_difference}, and it approximates f'({x}) with an error of {abs(centered_difference - f_der_x)}")
        print()

    print("When h becomes very small, the errors start to increase")
    print("This happens because in floating point arithmetic, the difference between two nearly equal numbers, in this case f(x+h)-f(x) or f(x+h)-f(x-h)")
    print("Which are nearly equal at a very small h, a numerical cancellation can happen, which means the difference of the two nearly equal floating points, which are calculated by other small floating points, so they're not that exact, and thus the difference will not be that exact.")


if __name__=="__main__":
    solve()