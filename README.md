# Numerical Calculation of Vertical Electric Field

## Problem Statement
* A thin strip of length 2 meters is located along the x-axis from $x=-1$ to $x=1$.
* The non-uniform linear charge density is described by the function $\lambda(x)=\lambda_0(1+x^2)$, where $\lambda_0=1$ C/m.
* The objective is to calculate the vertical component of the electric field ($E_y$) at a point on the y-axis, located at a distance $d=2$ meters from the center of the strip.

## Analytical Formulation
* According to Coulomb's Law, the magnitude of the electric field from a charge element $dQ = \lambda(x)dx$ at the target point is:
  $$dE = \frac{1}{4\pi\epsilon_0}\frac{dQ}{r^2}\hat{r}$$
* The distance from the charge element to the observation point is $r = \sqrt{x^2+d^2}$.
* Due to symmetry, the horizontal components cancel out entirely, leaving only the vertical component to be integrated: 
  $$dE_y = \frac{1}{4\pi\epsilon_0}\frac{\lambda(x)dx}{(x^2+d^2)}\frac{d}{\sqrt{x^2+d^2}} = \frac{1}{4\pi\epsilon_0}\frac{\lambda(x)d~dx}{(x^2+d^2)^{3/2}}$$
* Substituting $d=2$ and $\lambda_0=1$, the total vertical electric field is evaluated as:
  $$E_y = \frac{4}{4\pi\epsilon_0}\int_{-1}^{1}\frac{1+x^2}{(x^2+4)^{3/2}}dx$$
* By splitting the numerator using $1+x^2 = (x^2+4)-3$, the integral simplifies to two parts:
  $$\frac{1}{\sqrt{x^2+4}} - \frac{3}{(x^2+4)^{3/2}}$$
* Evaluating this yields the exact analytical solution:
  $$E_y = \frac{1}{\pi\epsilon_0}\left[2\ln\left(\frac{1+\sqrt{5}}{2}\right) - \frac{3}{2\sqrt{5}}\right]$$
* This results in an approximate field value of $E_y \approx 1.05 \times 10^{10}$ N/C.

## Numerical Methods & Visualizations

* Rectangle Method (Midpoint Rule): Computes the integral by calculating the midpoint of 10,000 subintervals. The script outputs a vertical electric field of $1.0483 \times 10^{10}$ N/C.
<br>
<img src="images/fig_rectangle.png" width="600" alt="Rectangle Method (Midpoint Rule) Diagram">

* Trapezoidal Rule: Approximates the integral region using trapezoids across 10,000 subintervals. The script calculates a field of $1.0483 \times 10^{10}$ N/C.
<br>
<img src="images/fig_trapezoid.png" width="600" alt="Trapezoidal Rule Diagram">

* Simpson's Rule: Approximates the curve using parabolic arcs, requiring an even number of subintervals (10,000 used). The numerical result matches at $1.0483 \times 10^{10}$ N/C.
<br>
<img src="images/fig_simpson.png" width="600" alt="Simpson's Rule Diagram">

* Gaussian Quadrature: Utilizes Legendre polynomials with 4 sample points for high-precision integration. The integral evaluates to approximately $0.2916$, yielding an electric field of $1.0484 \times 10^{10}$ N/C.
<br>
<img src="images/fig_gauss.png" width="600" alt="Gaussian Quadrature Diagram">

## Conclusion
* For this specific interval $[-1, 1]$ and relatively simple function, Simpson's Rule is the easiest to implement and the most straightforward for controlling interval divisions and estimating errors.
* While Gaussian Quadrature is highly effective when extreme precision is required using very few data points, Simpson's Rule remains the preferred method for generating clean, understandable, and easily modifiable code in standard applications.
