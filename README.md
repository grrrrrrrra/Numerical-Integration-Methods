# Numerical-Integration-Methods

This project implements various numerical integration methods, including:

- **Lagrange Polynomial Integration**: A method for approximating integrals using Lagrange polynomials.
- **Rectangular Integration**: Uses lower and upper rectangles for numerical approximation.
- **Trapezoidal Rule**: Applies the trapezoidal rule for a more accurate integration.
- **Simpson's Rule**: Uses parabolas for better approximation.
- **Newton-Cotes Integration**: Uses equally spaced points for numerical integration.

## Usage

### Lagrange Integration

1. Run `lagrange_integration.py`.
2. Input the number of nodes and the points in the format "x y".
3. Specify the lower and upper limits of integration.
4. The program will output the approximate integral using the Lagrange polynomial.

### Numerical Integration

1. Run `numerical_integration.py`.
2. Input the function as a string (e.g., `1/(1+x**2)`).
3. Specify the number of segments and the limits of integration.
4. The program will output results for various numerical integration methods, including lower and upper rectangles, trapezoidal rule, Simpson's rule, and Newton-Cotes.
