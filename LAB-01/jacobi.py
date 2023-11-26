import numpy as np

def jacobi(x0, A, b, maxit, tol):
    n, m = A.shape
    if m != n:
        return 'La Matriz A no es cuadrada'
    
    n1, m1 = b.shape
    if n1 != n or m1 != 1:
        return 'Medida del vector independiente no valida'
    
    n1, m1 = x0.shape
    if n1 != n or m1 != 1:
        return 'Medida del iterado inicial no valida'
    
    if np.linalg.matrix_rank(A) != n or np.linalg.matrix_rank(A) != m:
        return 'Sistema incompatible'
    
    D = np.diag(np.diagonal(A))
    Al = -np.tril(A)
    Au = -np.triu(A)
    print(D,'---',Al,'---',Au)
    M = np.matmul(np.linalg.inv(D), (Al + Au))
    radio_espectral_M = np.max(np.abs(np.linalg.eigvals(M)))
    print(np.linalg.eigvals(M))
    if radio_espectral_M >= 1:
        return 'El metodo no converge'
    
    v = np.matmul(np.linalg.inv(D), b)
    xk = x0
    rk = np.matmul(A, xk) - b
    Nrk = np.linalg.norm(rk, 1)
    k = 0
    res = np.array([k, Nrk])
    
    while True:
        if Nrk <= tol:
            return xk, res
        if k > maxit:
            return xk, res
        
        res = np.append(res, Nrk)
        xk = np.matmul(M, xk) + v
        rk = np.matmul(A, xk) - b
        Nrk = np.linalg.norm(rk, 1)
        k += 1

x0=np.array([[2],[-1],[1]],dtype='f')
A=np.array([[1,2,4],[2,9,7],[-1,8,-2]],dtype='f')
b=np.array([[4],[2],[-12]],dtype='f')
itera=20
tol=0.0001

x, resto = jacobi(x0,A,b,itera,tol)

print(x)