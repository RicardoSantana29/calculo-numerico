import numpy as np
import sympy as sp

def DiferenciasDivididas(x, y):
    if len(x) != len(y):
        raise ValueError('Error en el tamaño de la data')
    else:
        n = len(x)
    D = np.reshape(np.zeros_like(x), (len(x),1)) #[[0] * n for _ in range(n)]
    D[:, 0] = y
    for j in range(1, n):
        D[0:n-j+1, j] = (D[1:n-j+2, j-1] - D[0:n-j+1, j-1]) / (x[j:n] - x[0:n-j+1])
    return D

def polinomio_newton(x, y):
    if len(x) != len(y):
        raise ValueError('Error en el tamaño de la data')    
    
    n = len(x)
    F = [[0] * n for _ in range(n)]

    for i in range(n):
        F[i][0] = y[i]

    for i in range(1, n):
        for j in range(1, i + 1):
            F[i][j] = (F[i][j - 1] - F[i - 1][j - 1]) / (x[i] - x[i - j])

    coeficientes = [F[i][i] for i in range(n)]

    #creando polinomio
    ecuacion = 0
    termino = 1
    var = sp.symbols('x')
    for k in range(n):
        ecuacion += coeficientes[k]*termino
        termino *= (var - x[k])
        
    ecuacion = sp.simplify(ecuacion)

    return ecuacion

def simplificar(coeficientes):
    ecuacion = 0


# Ejemplo de uso
x = [1.0, 1.3, 1.6, 1.9, 2.2]
y = [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]

x = [0,1,2]
y = [1,2,5]
X = np.array(x)
Y = np.array(y)

p = DiferenciasDivididas(X, Y)
print(p)