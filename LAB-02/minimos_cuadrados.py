import numpy as np

def MCpoli(X, Y, m):
    n = len(X)
    B = [0] * (m + 1)
    F = [[0] * (m + 1) for _ in range(n)]

    for k in range(1, m + 2):
        F[:, k - 1] = [x ** (k - 1) for x in X]

    A = np.dot(F.T, F)
    B = np.dot(F.T, Y)
    C = np.linalg.solve(A, B)
    
    return C

# esta funciona
def min_cua_poli(X, Y, m):
    n = len(X)
    B = np.zeros(m + 1)
    F = np.zeros((n, m + 1))

    for k in range(1, m + 2):
        F[:, k - 1] = X ** (k - 1)

    A = np.dot(F.T, F)
    B = np.dot(F.T, Y)
    C = np.linalg.solve(A, B)
    
    c = np.flip(C).T  #invirtiendo coeficientes (agregado)
    #polinomio
    p = np.poly1d(c)

    return C, p

x = np.array([-1, 0, 1])
y = np.array([2, 1, 4])
x = np.array([-1,0,1,2,3,4,5,6])
y = np.array([10,9,7,5,4,3,0,-1])
p = min_cua_poli(x, y, 1)
print(p[1])
