def sustitucion_progresiva(A, b):
    import numpy as np
    n = len(b)
    sol = np.mat(np.zeros((n,1)))
    sol[0] = b[0] / A[0, 0]
    for kk in range(1, n):
        sol[kk] = (b[kk] - np.dot(A[kk, :kk], sol[:kk])) / A[kk, kk]
    return sol

def sustitucion_regresiva(A, b):
    import numpy as np
    n = len(b)
    sol = np.mat(np.zeros((n,1)))
    sol[n-1] = b[n-1]/A[n-1,n-1]
    for kk in range(n-2,-1,-1):
        sol[kk] = (b[kk] - sum(A[kk,kk+1:n]*sol[kk+1:n]).T)/A[kk,kk]
    return sol