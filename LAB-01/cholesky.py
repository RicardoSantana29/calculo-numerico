import numpy as np

def fact_cholesky(A):
    n, m = A.shape
    U = np.zeros((n, m))

    # Prueba para determinar si la matriz es cuadrada
    if m != n:
        return 'La matriz A no es cuadrada'

    # Prueba para verificar si la matriz es simétrica
    if not np.allclose(A, A.T):
        return 'La matriz A no es simétrica'

    # Prueba para determinar si la matriz es definida positiva
    auto_valores = np.linalg.eigvalsh(A)
    if np.any(auto_valores <= 0):
        return 'La matriz A no es definida positiva'
    else:
        U = np.triu(A)
    
    for k in range(m):
        for j in range(k+1, m):
            U[j, j:m] = U[j, j:m] - U[k, j:m] * (U[k, j] / U[k, k])
        U[k, k:m] = U[k, k:m] / np.sqrt(U[k, k])

    L = U.T
    return L, U
