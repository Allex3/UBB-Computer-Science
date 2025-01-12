import numpy as np
import matplotlib.pyplot as plt

# Function
def f(x, y, b):
    return 0.5 * (x**2 + b * y**2)

# Gradient of f
def gradient_f(x, y, b):
    return [x, b*y]

# Gradient descent with exact line search
def gradient_descent(b, x0, y0, iterations = 69):
    trajectory = [(x0, y0)] # Start from (x0, y0)
    x, y = x0, y0

    for i in range(iterations):
        gradient = gradient_f(x, y, b)
        step_size = (x**2+(b**2)*(y**2))/(x**2+(b**3)*y**2)
        x, y = x - gradient[0] * step_size, y - gradient[1] * step_size
        trajectory.append((x, y))
        if x == 0 and y == 0:
            break

    return np.array(trajectory)

# Plotttttttt

def plot_gradient_descent(b_values: list[float], x0, y0, iterations = 69):
    x = np.linspace(-5, 5, 500)
    y = np.linspace(-5, 5, 500)
    X, Y = np.meshgrid(x, y)


    for b in b_values:
        plt.figure()
        Z = f(X, Y, b) # Get all the values of f coordinates in our range on the meshgrid
        trajectory = gradient_descent(b, x0, y0, iterations)

        plt.contour(X, Y, Z, levels=20, cmap='viridis')
        plt.plot(trajectory[:, 0], trajectory[:, 1], 'ro-', markersize=4, label="Trajectory")
        plt.title(f"Gradient Descent (b = {b})")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    b_values = [1, 1/2, 1/5, 1/10]
    x0, y0 = 4.5, 3 # Initial point
    iterations = 69
    plot_gradient_descent(b_values, x0, y0, iterations)