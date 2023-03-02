import numpy as np
from sympy import symbols, lambdify

def factorial(n, symbolic=False):
    if symbolic:
        ns = symbols(f"{n}")
    else:
        ns = n
    if n < 1:
        return 1
    else:
        return ns * factorial(n - 1, symbolic=symbolic)


def permute(n, k, symbolic=False):
    return factorial(n, symbolic=symbolic) / (factorial(n - k, symbolic=symbolic))


def choose(n, k, symbolic=False):
    return permute(n, k, symbolic=symbolic) / factorial(k, symbolic=symbolic)


def binomial_expansion(n, symbolic=False, xy=None):
    if xy is None:
        x, y = symbols("x y")
    else:
        x, y = xy
    expression = 0
    for k in range(0, n + 1, 1):
        expression = expression + choose(n, k, symbolic=True) * x ** (n - k) * y ** (k)
    return expression


print(factorial(5))
print("Oi oi!")