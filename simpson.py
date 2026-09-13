import math
import numpy as np

# Constants for the problem
epsilon0 = 8.85418782e-12
d = 2.0
a = -1.0                    # lower limit of integration
b = 1.0                     # Upper limit of integration
n = 10000                   # Number of subintervals (n must be even for Simpson's rule)

h = (b - a) / n             # Width of each subinterval

def f(x):
    return (1 + x**2) / ((x**2 + d**2)**(1.5))

# Simpson's rule integration:
x = np.linspace(a, b, n + 1)
y = f(x)

# Apply Simpson's rule formula:
simpson_integral = (h / 3) * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]))

# Compute the vertical electric field E_y using the formula
E_y = (2 * d / (4 * math.pi * epsilon0)) * simpson_integral

print("Value of vertical electric field E_y at point (0, 2) m:")
print(f"{E_y:.4e} N/C")
