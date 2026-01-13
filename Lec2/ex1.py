import sympy as sp
import math

def tayser(f, x0, N):
    """
    Returns the first N Taylor series terms of function f around x0.
    
    f  : sympy expression in x
    x0 : expansion point
    N  : number of terms
    """
    x = sp.symbols('x')
    terms = []

    for i in range(N):
        derivative = sp.diff(f, x, i)
        coeff = derivative.subs(x, x0) / math.factorial(i)
        term = coeff * (x - x0)**i
        terms.append(sp.simplify(term))

    return terms

x = sp.symbols('x')  
print("The 10th tylor expansion for sin(x) are: ", tayser(sp.sin(x), 0, 10))
