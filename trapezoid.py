import math
import numpy as np
import matplotlib.pyplot as plt

# Constants of the problem
epsilon0 = 8.85418782e-12
d = 2.0
a = -1.0                    # Lower limit of integration
b = 1.0                     # Upper limit of integration
n = 10000                   # Number of subintervals for the integration

def f(x):
    return (1 + x**2) / ((x**2 + d**2)**(1.5))

# width of each subinterval
h = (b - a) / n

# Compute the integral using the trapezoidal rule
integral = 0.5 * (f(a) + f(b))
for i in range(1, n):
    x_val = a + i * h
    integral += f(x_val)
integral *= h

# factor for the vertical electric field E_y
constant_factor = (2 * d) / (4 * math.pi * epsilon0)
E_y = constant_factor * integral

print("Value of the vertical electric field E_y at point (0, 2) m:")
print(f"{E_y:.4e} N/C")
