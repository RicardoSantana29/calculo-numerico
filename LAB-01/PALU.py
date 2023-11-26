import numpy as np

def fact_PALU(A):
    A = np.array(A,dtype='f')

    n, m = A.shape
    if m != n:
        raise ValueError('La Matriz A no es cuadrada')

    L = np.eye(n)
    P = np.eye(n)
    U = np.copy(A)

    for j in range(n-1):
        k = np.argmax(np.abs(U[j:n, j]))+j
        
        U[[j, k], :] = U[[k, j], :]
        P[[j, k], :] = P[[k, j], :]
        L[[j, k], :j] = L[[k, j], :j]

        for i in range(j+1, n):
            L[i, j] = U[i, j] / U[j, j]
            U[i, j+1:n] = U[i, j+1:n] - L[i, j] * U[j, j+1:n]
            U[i, j] = 0
            

    return P, L, U

#A = np.array([[1,2,4],[2,9,7],[-1,8,-2]],dtype='f')
#A = np.array([[4,1,-1,0],[1,3,-1,0],[-1,-1,5,2],[0,0,2,4]],dtype='f')
#b = np.array([[4],[2],[-12]], dtype='f')

