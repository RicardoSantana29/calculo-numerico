# Secuencia para la lectura de archivos

# ARCHIVOS .txt
import sys
ruta = sys.path[0]
import numpy as np

A = np.loadtxt(f'{ruta}\A0.txt',skiprows = 0)

print('Matriz A\n')
print(A)

# Otra forma

N = np.genfromtxt('A0.txt')

print('\n Matriz A asignada a la variable N\n')
print(N)

# ARCHIVOS .csv + PANDAS

import pandas as pd

df = pd.read_csv(f'{ruta}\A0.txt',delimiter=',',header=False)

print('\nLa matriz A0.csv asignada a data frame\n')
print(df)

# Ahora se procede a eliminar cabeceras de columnas y nombre de las filas

F = np.array(df)

print('\nMatriz F, sin las cabecera y nombres de filas para poder operar\n')
print(F)

# Esta forma arroja entradas enteras, si requerimos float se procede de la
# siguiente manera

G = np.genfromtxt('A0.csv', skip_header = 1, delimiter = ',')

print('\nForma directa de quitar los encabezados y nombres de registros\n')
print('La matriz G, ya en formato float\n')
print(G)

# Cálculo del determinate de la matriz G

print(' Determinante de la matriz G es igual a\n\n det(A)=', np.linalg.det(G))

K = 2*G

print('\n Matriz K resultado de 2*G\n\n', K)

# Se procede a guardar los resultado anterior en archivo .txt

np.savetxt('2*G.txt', K, fmt = '%.2f') 


# Se procede a guardar los resultado anterior en archivo .csv
# usando pandas

KK = pd.DataFrame(data = K)
KK.to_csv('2porG.csv', sep = '	', header = False, float_format = '%.2f', index = False)

