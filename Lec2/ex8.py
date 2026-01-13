import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import sympy as sp

f = lambda x: x**2 + 10 * np.sin(x)

# Integration limits
a, b = -10, 10

# Numerical integration using scipy
num_integral, num_error = quad(f, a, b)
print(f"Numerical integral: {num_integral:.4f} ± {num_error:.4e}")

# Plot the function and shade the area under the curve
x_vals = np.linspace(a, b, 400)
y_vals = f(x_vals)

plt.figure(figsize=(8,5))
plt.plot(x_vals, y_vals, label=r"$f(x) = x^2 + 10\sin(x)$", color="blue")
plt.fill_between(x_vals, y_vals, 0, color="orange", alpha=0.3, label="Area under curve")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Numerical Integration - Area under Curve")
plt.legend()
plt.grid(True)
plt.show()

# Symbolic integration using sympy
x = sp.symbols('x')
f_sym = x**2 + 10*sp.sin(x)

# Definite integral
sym_integral = sp.integrate(f_sym, (x, a, b))
print(f"Symbolic integral: {sym_integral.evalf():.4f}")

# Optional: get the indefinite integral and plot borders
F = sp.integrate(f_sym, x)  # indefinite integral
F_borders = F.subs(x, b) - F.subs(x, a)
print(f"Indefinite integral evaluated at borders: {F_borders.evalf():.4f}")

