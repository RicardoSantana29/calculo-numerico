import sympy
import numpy

vars = sympy.symbols('x y') # Define x and y variables
f = sympy.sympify(['y*x**2', '5*x + sin(y)']) # Define function
J = sympy.zeros(len(f),len(vars)) # Initialise Jacobian matrix

# Fill Jacobian matrix with entries
for i, fi in enumerate(f):
    for j, s in enumerate(vars):
        J[i,j] = sympy.diff(fi, s)

print(J)
#[2*x*y, x**2]
#[5, cos(y)]

print(sympy.Matrix.det(J))
#2*x*y*cos(y) - 5*x**2

print(type(f))
a = 0
a = [b+1 for b in f]
print(a)