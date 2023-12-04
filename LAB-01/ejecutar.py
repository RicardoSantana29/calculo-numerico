from resolver_SEL import SEL
import numpy as np
import sys
import pandas as pd

#A = np.array([[1,2,4],[2,9,7],[-1,8,-2]],dtype='f')
#A = np.array([[4,1,-1,0],[1,3,-1,0],[-1,-1,5,2],[0,0,2,4]],dtype='f')
#b = np.array([[4],[2],[-12]], dtype='f')

#x0=np.array([[-1],[5],[3],[2]],dtype='f')
#A=np.array([[5,-1,1,1],[1,4,0,1],[3,-1,6,0],[0,1,-1,3]],dtype='f')
#b=np.array([[5],[2],[-3],[4]],dtype='f')
itera=100
tol=0.0000001

ruta_carpeta = sys.path[0]

A = pd.read_csv(f'{ruta_carpeta}/Apr.csv', header=None, delimiter=';')
b = pd.read_csv(f'{ruta_carpeta}/bpr.csv', header=None, delimiter=';')

#A = np.loadtxt(f'{ruta_carpeta}/Apr.txt',skiprows = 0, delimiter=',')
#b = np.loadtxt(f'{ruta_carpeta}/bpr.txt',skiprows = 0, delimiter=',')
#np.reshape(b, (len(b),1))

inst = SEL(A, b)
x = inst.resolucion_jacobi(itera, tol)[0]
print(x)

#np.savetxt(f'{ruta_carpeta}/xpr.txt', x, fmt = '%.3f', encoding='utf-8')

df = pd.DataFrame(x)
df.to_csv(f'{ruta_carpeta}/xpr.csv', sep=';', decimal=',', header = False, index = False, float_format = '%.3f')