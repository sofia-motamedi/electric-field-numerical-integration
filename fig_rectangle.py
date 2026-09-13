import numpy as np
import matplotlib.pyplot as plt
import math

# constants of the problem
d = 2.0
a = -1.0                     # lower limit of integration
b = 1.0                      # upper limit of integration
N = 10                       # Number of subintervals (rectangles)
h = (b - a) / N              # width of each rectangle

def f(x):
    return (1 + x**2) / ((x**2 + d**2)**(1.5))

# extending the x-range a little for a better view
x_smooth = np.linspace(a - 0.1, b + 0.1, 400)
y_smooth = f(x_smooth)

# the plot
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, y_smooth, 'b-', label=r"$f(x)=\frac{1+x^2}{(x^2+d^2)^{1.5}}$")

# Plot the rectangles
for i in range(N):
    # Determine the endpoints of the subinterval
    x_left = a + i * h
    x_right = x_left + h
    # Calculate the midpoint
    x_mid = (x_left + x_right) / 2.0
    # rectangle height
    rect_height = f(x_mid)

    # Define the vertices of the rectangle:
    # starting at (x_left, 0), then (x_left, f(x_mid)),
    # then (x_right, f(x_mid)), and finally (x_right, 0)
    xs = [x_left, x_left, x_right, x_right]
    ys = [0, rect_height, rect_height, 0]
    plt.fill(xs, ys, 'r', alpha=0.3, edgecolor='black')

plt.title("Rectangle Method (Midpoint Rule) Diagram")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
