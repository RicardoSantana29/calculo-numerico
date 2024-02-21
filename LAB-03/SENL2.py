import sympy as sp
import numpy as np

"""Entrada:
F: matriz que define el sistema no lineal
x0: aproximación inicial
itera: máximo número de iteraciones
tol: tolerancia
n: número de variables"""

def var(x0):
    letras = ''
    for i in range(len(x0)):
        letras += f'x{i+1} '
    var = sp.symbols(letras)
    return var

def J(F, x0):
    xyz = var(x0)
    J = sp.zeros(len(F),len(xyz))

    for i, fi in enumerate(f):
        for j, s in enumerate(vars):
            J[i,j] = sympy.diff(fi, s)

    return J

def newton_metodo(F, x0, itera, tol):
        k = 1
        F0 = sp.lambdify([i for i in self.var], self.F, 'numpy')
        J0 = sp.lambdify([i for i in self.var], self.J, 'numpy')
        while k <= itera:
            F_x = F0(x)
            J_x = J0(x)
            y = np.linalg.solve(J_x, -F_x)
            x = x + y
            if np.linalg.norm(y) < tol:
                return x
            k += 1
        return 'Número máximo de iteraciones excedido'

x0 = np.array([0.1, 0.1, -0.1])#.reshape((3,1))
itera = 5
tol = 1e-6

letras = ''
for i in range(len(x0)):
    letras += f'x{i+1} '
var = sp.symbols(letras)

f1 = 3*var[0] - sp.cos(var[1]*var[2]*(sp.pi/180)**2) - 1/2
f2 = var[0]**2 - 81*(var[1]+0.1)**2 + sp.sin(var[2]) +1.06
f3 = sp.exp(-var[0]*var[1]) + 20*var[2] + (10*sp.pi-3)/3

F = sp.matrices.Matrix([f1, f2, f3])

F0 = sp.lambdify([i for i in var], F, 'numpy')

J = sp.zeros(len(F),len(var))

for i, fi in enumerate(F):
    for j, s in enumerate(var):
        J[i,j] = sp.diff(fi, s)

J0 = sp.lambdify([i for i in var], J, 'numpy')
#print(F)
#print(J)
k = 1
while k <= itera:
    """print(x0)
    print(x0, type(x0))
    print(x0[1], type(x0[1]))"""
    F_x = F0(x0[0], x0[1], x0[2])
    J_x = J0(x0[0], x0[1], x0[2])
    #print(F_x, type(F_x))
    #print(J_x, type(J_x))

    y = np.linalg.solve(J_x, -F_x).reshape(1, 3)

    x0 = x0[0] + y[0]
    print(x0)
    if np.linalg.norm(y) < tol:
        break
    k += 1
print('Número máximo de iteraciones excedido')

print(x0)

"""vars = sympy.symbols('x y') # Define x and y variables
f = sympy.sympify(['y*x**2', '5*x + sin(y)']) # Define function
J = sympy.zeros(len(f),len(vars)) # Initialise Jacobian matrix

# Fill Jacobian matrix with entries
for i, fi in enumerate(f):
    for j, s in enumerate(vars):
        J[i,j] = sympy.diff(fi, s)"""