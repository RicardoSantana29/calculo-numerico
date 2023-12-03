import numpy as np

def GaussSeidel(x0, A, b, maxit, tol):
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

    D = np.diag(np.diag(A))
    Al = -np.tril(A, -1)
    Au = -np.triu(A, 1)
    inv_D_Al = np.linalg.inv(D - Al)
    M = np.matmul(inv_D_Al, Au)
    rho = np.max(np.abs(np.linalg.eigvals(M)))
    if rho >= 1:
        return 'El metodo no converge'

    v = np.matmul(inv_D_Al, b)
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

        res = np.append(res, [Nrk], axis=0)
        xk = np.matmul(M, xk) + v
        rk = np.matmul(A, xk) - b
        Nrk = np.linalg.norm(rk, 1)
        k += 1

x0=np.array([[-1],[5],[3],[2]],dtype='f')
A=np.array([[5,-1,1,1],[1,4,0,1],[3,-1,6,0],[0,1,-1,3]],dtype='f')
b=np.array([[5],[2],[-3],[4]],dtype='f')
itera=50
tol=0.0000001

x, res = GaussSeidel(x0,A,b,itera,tol)

print(x)