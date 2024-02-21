import numpy as np
import sympy as sp

"""x0 = np.array([1, 0.5]) #para n variables n elementos
itera = 5
tol = 1e-6

letras = ''
for i in range(len(x0)):
    letras += f'x{i+1} '
var = sp.symbols(letras)

f1 = 10*var[0]**2 + sp.cos(var[1]) -12
f2 = var[0]**4 + 6*var[1]-2 #seguir agregando funciones de ser necesario

F = sp.matrices.Matrix([f1, f2]) #colocar todas las funciones de la parte anterior

F0 = sp.lambdify([i for i in var], F, 'numpy')

J = sp.zeros(len(F),len(var))
for i, fi in enumerate(F):
    for j, s in enumerate(var):
        J[i,j] = sp.diff(fi, s)

J0 = sp.lambdify([i for i in var], J, 'numpy')

k = 1
while k <= itera:

    F_x = F0(x0[0], x0[1])
    J_x = J0(x0[0], x0[1])

    y = np.linalg.solve(J_x, -F_x).reshape(1,len(x0))[0]
    x0 = x0 + y
    print(x0)
    if np.linalg.norm(y) < tol:
        break
    k += 1
print('Número máximo de iteraciones excedido')

print(x0)"""

def SENL(x0, F, itera, tol):
    x0 = np.array(x0)

    if len(x0) != len(F):
        return 'numero de ecuaciones y variables diferentes, el sistema no se puede resolver'
    
    letras = ''
    for i in range(len(x0)):
        letras += f'x{i+1} '
    var = sp.symbols(letras)

    F = sp.matrices.Matrix(F)

    F0 = sp.lambdify([i for i in var], F, 'numpy')

    J = sp.zeros(len(F),len(var))
    for i, fi in enumerate(F):
        for j, s in enumerate(var):
            J[i,j] = sp.diff(fi, s)

    J0 = sp.lambdify([i for i in var], J, 'numpy')

    k = 1
    while k <= itera:

        F_x = F0(x0[0], x0[1]) #agregar x[n] donde n es el numero de elementos de x0
        J_x = J0(x0[0], x0[1])

        y = np.linalg.solve(J_x, -F_x).reshape(1,len(x0))[0]
        x0 = x0 + y
        print(x0)
        if np.linalg.norm(y) < tol:
            break
        k += 1
    print('Número máximo de iteraciones excedido')

    return x0

var = sp.symbols('x1 x2')
f1 = 10*var[0]**2 + sp.cos(var[1]) -12
f2 = var[0]**4 + 6*var[1]-2 #seguir agregando funciones de ser necesario
F = [f1, f2]
x0 = [1, 0.5]
itera = 10
tol = 1e-6

print(SENL(x0, F, itera, tol))