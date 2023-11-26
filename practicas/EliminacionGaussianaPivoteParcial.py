def EliminacionGaussianaPivoteParcial(A,b):
    import numpy as np
    (n,m) = A.shape
    if (m!=n):
        print('La matriz no es cuadrada')
        return

    (n1,m1) = b.shape
    if (n1!=n or m1!=1):
        print('Medida del vector independiente no valida')
        return

    if (np.linalg.matrix_rank(A) != m):
        print('Sistema incompatible o con infinitas soluciones')
        return

    sol = np.mat(np.zeros((n,1)))
    for j in range(0,n-1):
        k = np.argmax(np.abs(A[j:n,j]))
        k = k+j
        faux = np.copy(A[j,:])
        A[j,:] = np.copy(A[k,:])
        A[k,:] = np.copy(faux)
        baux = np.copy(b[j])
        b[j] = np.copy(b[k])
        b[k] = np.copy(baux)
        for i in range(j+1,n):
            mu = A[i,j]/A[j,j]
            A[i,:] = A[i,:] - mu*A[j,:]
            b[i] = b[i] - mu*b[j]
            
    # sustitucion regresiva (hacia atras)
    sol[n-1] = b[n-1]/A[n-1,n-1]
    for kk in range(n-2,-1,-1):
        sol[kk] = (b[kk] - sum(A[kk,kk+1:n]*sol[kk+1:n]).T)/A[kk,kk]
        
    return sol
    

    
