import numpy as np
import sys
import pandas as pd

class SEL():
    def __init__(self,A,b):
        self.A = np.array(A, dtype='f')
        self.b = np.array(b, dtype='f')
        #self.D = np.diag(np.diagonal(A))
        #self.Al = np.tril(A)*(-1)
        #self.Au = np.triu(A)*(-1)

    #herramientas
    def sustitucion_progresiva(self,triangular_inferior,vector):
        
        n = len(vector)
        sol = np.mat(np.zeros((n,1)))
        sol[0] = vector[0] / triangular_inferior[0, 0]
        for kk in range(1, n):
            sol[kk] = (vector[kk] - np.dot(triangular_inferior[kk, :kk], sol[:kk])) / triangular_inferior[kk, kk]
        return sol

    def sustitucion_regresiva(self,triangular_superior,vector):
        
        n = len(vector)
        sol = np.mat(np.zeros((n,1)))
        sol[n-1] = vector[n-1]/triangular_superior[n-1,n-1]
        for kk in range(n-2,-1,-1):
            sol[kk] = (vector[kk] - sum(triangular_superior[kk,kk+1:n]*sol[kk+1:n]).T)/triangular_superior[kk,kk]
        
        return sol

    #metodo de eliminacion gaussiana por pivoto parcial
    def resolucion_gaussiana(self):
        #copias
        A, b = self.A, self.b
        
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

        sol = self.sustitucion_regresiva(A, b)

        return sol

    #metodo por factorifacion PALU
    def factorizacion_palu(self):
        A = self.A

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
                
        return {'P':P, 'A':self.A, 'L':L, 'U':U}

    def resolucion_palu(self):
        A, b = self.A, self.b

        palu = self.factorizacion_palu()
        w = np.matmul(palu['P'], b)
        
        #resolviendo Ly=w
        y = self.sustitucion_progresiva(palu['L'], w)

        #resolviendo Ux=y
        x = self.sustitucion_regresiva(palu['U'], y)
        return x

    #metodo por factorizacion cholesky
    def factorizacion_cholesky_palu(self):
        # Prueba para verificar si la matriz es simétrica
        if not np.allclose(A, A.T):
            return 'La matriz A no es simétrica'

        # Prueba para determinar si la matriz es definida positiva
        auto_valores = np.linalg.eigvalsh(A)
        if np.any(auto_valores <= 0):
            return 'La matriz A no es definida positiva'

        palu = self.factorizacion_palu()
        D = np.sqrt(np.diag(np.diagonal(palu['U'])))
        L_chlk = np.matmul(palu['L'],D)

        return L_chlk, L_chlk.T

    def factorifacion_cholesky(self):
        A = self.A
        
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

    def resolucion_cholesky(self):
        A, b = self.A, self.b

        L, Lt = self.factorizacion_cholesky_palu()
        #L, Lt = self.factorizacion_cholesky()
        
        #resolviendo Ly=b
        y = self.sustitucion_progresiva(L, b)

        #resolviendo (Lt)x=y
        x = self.sustitucion_regresiva(Lt, y)
        return x

    #menu de metodos directos
    def metodo_directo(self,nombre):
        if nombre == 'gauss':
            return self.resolucion_gaussiana()
        elif nombre == 'palu':
            return self.resolucion_palu()
        elif nombre == 'cholesky':
            return self.resolucion_cholesky()

#A = np.array([[1,2,4],[2,9,7],[-1,8,-2]],dtype='f')
#A = np.array([[4,1,-1,0],[1,3,-1,0],[-1,-1,5,2],[0,0,2,4]],dtype='f')
#b = np.array([[4],[2],[-12]], dtype='f')

ruta_carpeta = sys.path[0]

A = np.loadtxt(f'{ruta_carpeta}/Apr.txt',skiprows = 0, delimiter=',')
b = np.loadtxt(f'{ruta_carpeta}/bpr.txt',skiprows = 0, delimiter=',')
np.reshape(b, (len(b),1))

inst = SEL(A, b)
x = inst.metodo_directo('palu')

np.savetxt(f'{ruta_carpeta}/xpr.txt', x, fmt = '%.3f', encoding='utf-8')

df = pd.DataFrame(x)
df.to_csv(f'{ruta_carpeta}/xpr.csv', sep=';', decimal=',', header = False, index = False, float_format = '%.3f')