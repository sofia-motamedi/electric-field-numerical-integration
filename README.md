<h1>Numerical Computation of Electric Field from a Line Charge</h1>

<p>
This project computes the vertical component of the electric field <em>E<sub>y</sub></em> at a point on the <em>y</em>-axis
due to a finite, non-uniformly charged line segment along the <em>x</em>-axis.
The line extends from <code>x = -1</code> m to <code>x = +1</code> m, and the linear charge density is given by:
</p>

<p style="font-size: 110%;">
\[
\lambda(x) = \lambda_0 (1 + x^2)
\]
</p>

<p>
where \(\lambda_0\) is a constant with units of charge per meter.
We compute the electric field at the point \((0, d)\) with \(d = 2\) m.
Using Coulomb's law and symmetry, only the vertical component of the electric field survives after integration.
The resulting integral for <em>E<sub>y</sub></em> is:
</p>

<p style="font-size: 110%;">
\[
E_y = \frac{2 d}{4 \pi \varepsilon_0} \int_{-1}^{1} \frac{1 + x^2}{(x^2 + d^2)^{3/2}} \, dx
\]
</p>

<p>
For \(d = 2\) m and \(\varepsilon_0 = 8.85418782 \times 10^{-12} \, \text{F/m}\), the analytical solution is:
</p>

<p style="font-size: 110%;">
\[
E_y = \frac{\lambda_0}{\pi \varepsilon_0} \left[ 2 \ln(1 + \sqrt{5}) - \frac{2}{\sqrt{5}} \right]
\approx 1.05 \times 10^{10} \, \text{N/C}
\]
</p>

<hr />

<h2>Numerical methods implemented</h2>

<p>
The integral
\[
\int_{-1}^{1} \frac{1 + x^2}{(x^2 + d^2)^{3/2}} \, dx
\]
is approximated using several classical numerical integration techniques:
</p>

<ul>
  <li><strong>Midpoint (Rectangle) Rule</strong> – implemented in <code>rectangle.py</code></li>
  <li><strong>Trapezoidal Rule</strong> – implemented in <code>trapezoid.py</code></li>
  <li><strong>Simpson's Rule</strong> – implemented in <code>simpson.py</code></li>
  <li><strong>Gaussian Quadrature (Legendre)</strong> – implemented in <code>gauss_quadrature.py</code></li>
</ul>

<p>
Each method computes the same integral and then uses the factor
\[
\frac{2 d}{4 \pi \varepsilon_0}
\]
to obtain the vertical electric field <em>E<sub>y</sub></em>.
All methods converge to approximately
\[
E_y \approx 1.048 \times 10^{10} \, \text{N/C},
\]
which agrees very well with the analytical result.
</p>

<hr />

<h2>Project structure</h2>

<pre>
electric-field-numerical-integration/
├── rectangle.py
├── trapezoid.py
├── simpson.py
├── gauss_quadrature.py
├── fig_rectangle.png
├── fig_trapezoid.png
├── fig_simpson.png
├── fig_gauss.png
└── README.md
</pre>

<hr />

<h2>Figures</h2>

<p>
Below are the visualizations of the integrand and the numerical schemes used.
</p>

<h3>Midpoint (Rectangle) Rule</h3>
<p>
<img src="fig_rectangle.png" alt="Rectangle Method (Midpoint Rule) Diagram" width="600" />
</p>

<h3>Trapezoidal Rule</h3>
<p>
<img src="fig_trapezoid.png" alt="Trapezoidal Rule Diagram" width="600" />
</p>

<h3>Simpson's Rule</h3>
<p>
<img src="fig_simpson.png" alt="Simpson's Rule Diagram" width="600" />
</p>

<h3>Gaussian Quadrature</h3>
<p>
<img src="fig_gauss.png" alt="Gaussian Quadrature Diagram" width="600" />
</p>

<hr />

<h2>How to run the code</h2>

<ol>
  <li><strong>Clone the repository</strong>:
    <pre><code>git clone https://github.com/&lt;your-username&gt;/electric-field-numerical-integration.git
cd electric-field-numerical-integration
</code></pre>
  </li>

  <li><strong>Run each method</strong> (requires Python 3 and <code>numpy</code>, <code>matplotlib</code> for plotting):
    <pre><code>python rectangle.py
python trapezoid.py
python simpson.py
python gauss_quadrature.py
</code></pre>
  </li>

  <li><strong>Compare outputs</strong>:
    <p>
    Each script prints the numerical value of <em>E<sub>y</sub></em> at the point \((0, 2)\) m.
    The values should be very close to each other and to the analytical result
    \(E_y \approx 1.05 \times 10^{10} \, \text{N/C}\).
    </p>
  </li>
</ol>

<hr />

<h2>Discussion</h2>
<p>
For this problem, with a relatively simple integrand and a finite interval \([-1, 1]\),
Simpson's rule offers an excellent balance between accuracy and implementation simplicity.
It is easy to control the error by increasing the number of subintervals, and the code remains
compact and readable.
</p>

<p>
Gaussian quadrature can achieve high accuracy with fewer evaluation points, which is useful
when function evaluations are expensive. However, for teaching, demonstration, and clarity,
Simpson's rule is often preferred.
</p>

<p>
This project demonstrates how different numerical integration techniques can be applied to a
real physics problem (electrostatics) and how their results compare to an exact analytical solution.
</p>
