#Entrada: x0 ∈ Rn
#Salida: x⋆

import numpy as np
import sympy as sp

def senlnewton(F, J, x0):
    for k in range(len(F)): #numero de variables
        s_k = np.linalg.solve (J(x), -F(x))
        x_k1 = x_k + s_k
    return x_k1

def F(x):
    # Definir la función F(x)
    # Implementa la función F(x) según tus necesidades
    pass

def J(x):
    # Definir la matriz Jacobiana J(x)
    # Implementa la matriz Jacobiana J(x) según tus necesidades
    pass

def newton_method(x, N, TOL):
    k = 1
    while k <= N:
        F_x = F(x)
        J_x = J(x)
        y = np.linalg.solve(J_x, -F_x)
        x = x + y
        if np.linalg.norm(y) < TOL:
            return x
        k += 1
    return 'Número máximo de iteraciones excedido'

# Ejemplo de uso
x_initial = np.array([1, 1, 1]) # Valor inicial de x
N = 100 # Número máximo de iteraciones
TOL = 1e-6 # Tolerancia

result = newton_method(x_initial, N, TOL)
print("Resultado:", result)



#otra forma

x1, x2, x3 = sp.symbols('x1 x2 x3')

f1 = 3*x1 - sp.cos(x2*x3) - 1/2
f2 = x1**2 - 81*(x2+0.1)**2 + sp.sin(x3) +1.06
f3 = sp.exp(-x1*x2) + 20*x3 + (10*sp.pi-3)/3

F = np.array([f1, f2, f3]).T

J = np.array([[sp.diff(f1,x1), sp.diff(f1,x2), sp.diff(f1,x1)],
                [sp.diff(f2,x1), sp.diff(f2,x2), sp.diff(f2,x3)],
                [sp.diff(f3,x1), sp.diff(f3,x2), sp.diff(f3,x3)]])

x0 = np.array((0.1, 0.1, -0.1)).T