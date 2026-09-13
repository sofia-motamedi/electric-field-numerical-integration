import numpy as np
import matplotlib.pyplot as plt
import math

# constants for the problem
d = 2.0
a = -1.0                    # Lower limit of integration
b = 1.0                     # Upper limit of integration
n = 4                       # Number of subintervals (must be even for Simpson's rule)
h = (b - a) / n             # Width of each subinterval

def f(x):
    return (1 + x**2) / ((x**2 + d**2)**(1.5))

# Generate Simpson's nodes
x_nodes = np.linspace(a, b, n + 1)
y_nodes = f(x_nodes)

# extending the x-range a little for a better view
x_smooth = np.linspace(a - 0.1, b + 0.1, 400)
y_smooth = f(x_smooth)

# create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, y_smooth, 'b-', label=r"$f(x)=\frac{1+x^2}{(x^2+d^2)^{1.5}}$")

for i in range(0, n, 2):
    x0, x1, x2 = x_nodes[i], x_nodes[i+1], x_nodes[i+2]
    f0, f1, f2 = y_nodes[i], y_nodes[i+1], y_nodes[i+2]

    x_parabola = np.linspace(x0, x2, 100)

    # using the Lagrange formula:
    L0 = ((x_parabola - x1) * (x_parabola - x2)) / ((x0 - x1) * (x0 - x2))
    L1 = ((x_parabola - x0) * (x_parabola - x2)) / ((x1 - x0) * (x1 - x2))
    L2 = ((x_parabola - x0) * (x_parabola - x1)) / ((x2 - x0) * (x2 - x1))

    P = f0 * L0 + f1 * L1 + f2 * L2

    # Mark the Simpson nodes on the plot
    plt.plot(x_nodes, y_nodes, 'ko', markersize=5, label="Simpson's nodes")

    # creating graphs
    plt.title("Simpson's Rule Diagram")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
