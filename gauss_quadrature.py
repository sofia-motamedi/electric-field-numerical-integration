import numpy as np
import math

# Constants for the problem
epsilon0 = 8.85418782e-12
d = 2.0
a = -1.0                    # Lower limit of integration
b = 1.0                     # Upper limit of integration

def f(x):
    return (1 + x**2) / ((x**2 + d**2)**(1.5))

# Choose the number of points for Gaussian quadrature
n_points = 4

# Get nodes and weights
nodes, weights = np.polynomial.legendre.leggauss(n_points)

integral = np.sum(weights * f(nodes))

# Compute the vertical electric field E_y using the given formula
E_y = (2 * d / (4 * math.pi * epsilon0)) * integral

print("Gaussian Quadrature Integral:", integral)
print("Value of vertical electric field E_y at point (0, 2) m:")
print(f"{E_y:.4e} N/C")
