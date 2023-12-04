import numpy as np
import math as mt
import pandas as pd
import sys
ruta_carpeta = sys.path[0]

#creacion de matrices
"""A = np.random.randint(10, size=(20,20))
df = pd.DataFrame(A)
df.to_csv(f'{ruta_carpeta}/A20.csv', sep=';', decimal=',', header = False, index = False, float_format = '%.3f')"""

A = np.round(10*np.random.rand(3,2))
B = np.round(10*np.random.rand(2,3))
one = np.ones(())

C = np.matmul(A,B)
D = np.matmul(B,A)

