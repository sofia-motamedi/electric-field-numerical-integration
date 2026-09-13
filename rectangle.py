import math

# Constants of the problem
epsilon0 = 8.85418782e-12
d = 2.0
a = -1.0                    # Lower limit of integration
b = 1.0                     # Upper limit of integration
n = 10000                   # Number of subintervals

# Calculate the width of each subinterval
h = (b - a) / n

def f(x):
    return (1 + x**2) / ((x**2 + d**2)**(1.5))

# Compute the integral using the midpoint (rectangle) method
integral = 0.0
for i in range(n):
    # Calculate the midpoint of each subinterval
    x_mid = a + (i + 0.5) * h
    integral += f(x_mid)
integral *= h

# Compute the vertical electric field using the formula:
E_y = (2 * d / (4 * math.pi * epsilon0)) * integral

print("Value of vertical electric field E_y at point (0, 2) m:")
print(f"{E_y:.4e} N/C")
