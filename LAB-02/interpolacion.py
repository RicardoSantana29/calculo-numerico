import numpy as np

def policoefind(x, y):
    x = np.reshape(np.array(x), (len(x), 1))
    y = np.reshape(np.array(y), (len(y), 1))

    m1, n1 = x.shape
    m2, n2 = y.shape
    if (m1 != m2) or (n1 != n2):
        raise ValueError('x e y no tienen la misma dimensión')

    m = m1
    n = m - 1
    B = np.ones((m, m)) # inicializar una matriz con unos

    # completar las m-1 filas de B, con las potencias apropiadas de los valores
    # que corresponden a la variable independiente.
    for i in range(m):
        for j in range(1, m):
            B[i, j] = x[i]**(j)

    c = np.linalg.solve(B, y) # resuelve el sistema de ecuaciones, dando como resultado los coeficientes del polinomio. Cambio de y con-y

    c = np.flip(c).T  #invirtiendo coeficientes (agregado)

    p = np.poly1d(c[0]) # librería para trabajo simbólico de polinomios

    return p

x = [-1,0,1]
y = [2,1,4]

p = policoefind(x, y)
print(p)
print(p(1))