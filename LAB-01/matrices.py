import numpy as np
import math as mt
import pandas as pd
import sys
ruta_carpeta = sys.path[0]

#creacion de matrices
A = np.random.randint(10, size=(20,20))
A_ch = np.array([[4,-1,1],[-1,4.25,2.75],[1,2.75,3.5]])

#guardado de matrices en txt
np.savetxt(f'{ruta_carpeta}/A20.txt', A, fmt = '%.3f', encoding='utf-8', delimiter=';')
np.savetxt(f'{ruta_carpeta}/A_ch.txt', A_ch, fmt = '%.3f', encoding='utf-8', delimiter=';')

#llamado en el documento a utilizar
#A = np.loadtxt(f'{ruta_carpeta}/Apr.txt',skiprows = 0, delimiter=',')