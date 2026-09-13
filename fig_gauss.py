import numpy as np
import matplotlib.pyplot as plt
import math

# Problem constants
d = 2.0
a = -1.0                    # Lower limit of integration
b = 1.0                     # Upper limit of integration

def f(x):
    return (1 + x**2) / ((x**2 + d**2)**(1.5))

# Choose the number of points for Gaussian quadrature
n_points = 4

# Get nodes and weights
nodes, weights = np.polynomial.legendre.leggauss(n_points)

y_nodes = f(nodes)

# extending the x-range a little for a better view
x_smooth = np.linspace(a - 0.1, b + 0.1, 400)
y_smooth = f(x_smooth)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, y_smooth, 'b-', label=r"$f(x)=\frac{1+x^2}{(x^2+d^2)^{1.5}}$")

# Plot the Gaussian quadrature nodes
plt.scatter(nodes, y_nodes, color='red', s=80, label="Quadrature nodes")

# Draw vertical dashed lines from each node down to the x axis
for i in range(n_points):
    plt.vlines(nodes[i], 0, y_nodes[i], colors='green', linestyles='dashed', linewidth=1)
    plt.vlines(a, 0, f(a), colors='green', linestyles='--', linewidth=1)
    plt.vlines(b, 0, f(b), colors='green', linestyles='--', linewidth=1)

# creating graphs
plt.title("Gaussian Quadrature Diagram")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
