import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy.abc import x,y,z
import math as math
from interpolante import data

x0 = np.array([0.0, 1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0, 13.5, 15.0, 16.5, 18.0, 19.5])
y0 = np.array([-1.000, -3.625, 5.000, 45.125, 137.000, 300.875, 557.000, 925.625, 1427.000, 2081.375, 2909.000, 3930.125, 5165.000, 6633.875])

tab = data(x0, y0)
p = tab.polinomio_trigonometrico(6)
px = sp.lambdify(x, p)
error = tab.error(tab.y , [px(i) for i in tab.x])
print('polinomio interpolante\n', p)
print('error\n', error)
tab.graficar_pol_sp(p, 'probando')

# Graficar los datos utilizando el método errorbar de matplotlib:
#plt.errorbar(x, y, xerr=incertidumbres_x, yerr=incertidumbres_y, fmt='o', markersize=0, capsize=4, elinewidth=1)