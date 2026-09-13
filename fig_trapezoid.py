import numpy as np
import matplotlib.pyplot as plt
import math

# Constants for the problem
d = 2.0
a = -1.0                    # Lower limit of integration
b = 1.0                     # Upper limit of integration
N = 8                       # Number of subintervals
h = (b - a) / N             # width of each subinterval

def f(x):
    return (1 + x**2) / ((x**2 + d**2)**(1.5))

# creating our variables for plotting
plt.figure(figsize=(10, 6))
x = np.linspace(a, b, N+1)
y = f(x)

# approximating definite integral with the trapezoidal rule
trap_area = (h/2) * (y[0] + (2*sum(y[1:N])) + y[N])

# creating graphs
plt.vlines(x, ymin=0, ymax=y)
plt.axhline(y=0, xmin=0, xmax=1, color="black")
plt.plot(x, y, marker=".", color="black", markersize=10)
plt.title("Trapezoidal Rule Diagram")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
