from sustitucion import sustitucion_regresiva as sus_reg, sustitucion_progresiva as sus_pro
import numpy as np

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
    sol = sus_reg(A, b)
        
    return sol
