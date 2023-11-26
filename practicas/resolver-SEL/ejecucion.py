from EliminacionGaussianaPivoteParcial import EliminacionGaussianaPivoteParcial as EGPP
import numpy as np
import pandas as pd
import csv

#se debe modificar la ruta
import sys
ruta_carpeta = sys.path[0]

#SEL Ax=b
A = np.array(np.loadtxt(f'{ruta_carpeta}/A.txt',skiprows = 0))
b = np.array(np.loadtxt(f'{ruta_carpeta}/b.txt',skiprows = 0))
x = np.array(EGPP(A,b))

#guardando en .txt
np.savetxt(f'{ruta_carpeta}/x.txt', x, fmt = '%.3f', encoding='utf-8')

#guardando en .csv
df = pd.DataFrame(x)
df.to_csv(f'{ruta_carpeta}/x.csv', sep=';', decimal=',', header = False, index = False, float_format = '%.3f')