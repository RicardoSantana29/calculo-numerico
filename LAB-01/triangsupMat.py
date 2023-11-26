def triangsupMat(A):
    import numpy as np
    (n,m) = A.shape
    B = []
    
    if (m!=n):
        print ('La matriz no es cuadrada')
        return
    
    B = np.copy(A)
    for j in range(0,n-1):
        k = np.argmax(np.abs(B[j:n,j])) # maximo pivote por columna
        k=k+j
        faux = np.copy(B[j,:])
        B[j,:] = np.copy(B[k,:])
        B[k,:] = np.copy(faux)
                
        for i in range(j+1,n):
             mu = B[i,j]/B[j,j]    # calculo de multiplicadores
             B[i,:] = B[i,:] - (mu*B[j,:])
                     
    return B
