<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Numerical Computation of Electric Field from a Line Charge</title>
  </head>
  <body>

    <h1>Numerical Computation of Electric Field from a Non-Uniform Line Charge</h1>

    <p><strong>Author:</strong> Sofia Motamedi<br />
       <strong>Institution:</strong> Amirkabir University of Technology (Tehran Polytechnic)</p>

    <hr />

    <h2>Problem description</h2>

    <p>
      We consider a thin charged rod of length <code>L = 2 m</code> lying along the x-axis,
      from <code>x = -1 m</code> to <code>x = +1 m</code>. The linear charge density is
      non-uniform and given by:
    </p>

    <p>
      <code>λ(x) = λ₀ (1 + x²)</code>
    </p>

    <p>
      where <code>λ₀</code> is a constant with units of charge per meter.
      We want to compute the vertical component of the electric field,
      <code>E<sub>y</sub></code>, at the point on the y-axis located at
      <code>(0, d)</code> with <code>d = 2 m</code>.
    </p>

    <p>
      Using Coulomb's law, the contribution of a small charge element
      <code>dQ = λ(x) dx</code> at position <code>x</code> to the electric field at
      <code>(0, d)</code> is:
    </p>

    <p>
      <code>dE = (1 / (4 π ε₀)) · (dQ / r²)</code>
    </p>

    <p>
      where <code>r = √(x² + d²)</code> is the distance from the element to the point.
      By symmetry, only the vertical component survives after integration, and the
      vertical component is:
    </p>

    <p>
      <code>dE<sub>y</sub> = (1 / (4 π ε₀)) · (λ(x) dx · d / (x² + d²)^(3/2))</code>
    </p>

    <p>
      Therefore, the total vertical electric field is:
    </p>

    <p>
      <code>
        E<sub>y</sub> =
        (2 d / (4 π ε₀)) ∫<sub>x = -1</sub><sup>1</sup>
        (1 + x²) / (x² + d²)^(3/2) dx
      </code>
    </p>

    <p>
      In this project, we set <code>d = 2 m</code> and
      <code>ε₀ = 8.85418782 × 10⁻¹² F/m</code>.
    </p>

    <hr />

    <h2>Analytical solution</h2>

    <p>
      The integral can be evaluated analytically. After simplification, the result
      for <code>E<sub>y</sub></code> can be written in the form:
    </p>

    <p>
      <code>
        E<sub>y</sub> =
        (λ₀ / (π ε₀)) ·
        [ 2 ln(1 + √5) − 2 / √5 ]
      </code>
    </p>

    <p>
      Numerically, this gives approximately:
    </p>

    <p>
      <code>E<sub>y</sub> ≈ 1.05 × 10¹⁰ N/C</code>
    </p>

    <hr />

    <h2>Numerical methods implemented</h2>

    <p>
      The integral
      <code>
        ∫<sub>-1</sub><sup>1</sup> (1 + x²) / (x² + d²)^(3/2) dx
      </code>
      is approximated using several classical numerical integration techniques:
    </p>

    <ul>
      <li><strong>Midpoint (Rectangle) Rule</strong> – implemented in <code>rectangle.py</code></li>
      <li><strong>Trapezoidal Rule</strong> – implemented in <code>trapezoid.py</code></li>
      <li><strong>Simpson's Rule</strong> – implemented in <code>simpson.py</code></li>
      <li><strong>Gaussian Quadrature (Legendre)</strong> – implemented in <code>gauss_quadrature.py</code></li>
    </ul>

    <p>
      Each method computes the same integral and then multiplies by the factor
      <code>(2 d) / (4 π ε₀)</code> to obtain the vertical electric field
      <code>E<sub>y</sub></code>. All methods converge to approximately:
    </p>

    <p>
      <code>E<sub>y</sub> ≈ 1.048 × 10¹⁰ N/C</code>
    </p>

    <p>
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
      Make sure the image filenames in the repository match those used here.
    </p>
    <h3>Midpoint (Rectangle) Rule</h3>
    <p>
      <img src="fig_rectangle.png"
           alt="Rectangle Method (Midpoint Rule) Diagram"
           width="600" />
    </p>

    <h3>
