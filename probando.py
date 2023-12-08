import matplotlib.pyplot as plt
import numpy as np

# Definir los datos de x, y las incertidumbres:
x = np.array([10, 20, 28, 36, 40, 44, 44, 44, 48, 48, 48, 48, 52, 52, 52, 52, 52, 56, 56, 56, 56, 56, 60, 60, 60, 60, 60, 60, 64, 64, 64, 64, 64, 64,]) # Datos de x

y = np.array([0.009,0.017,0.027,0.036,0.044,0.056,0.064,0.076,0.085,0.095,0.105,0.115,0.135,0.155,0.175,0.195,0.215,0.254,0.274,0.294,0.354,0.394,0.514,0.594,0.714,0.794,0.894,0.994,1.090,1.190,1.290,1.490,1.790,1.990]) # Datos de y

incertidumbres_x = np.array([1, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,]) # Incertidumbres de x

incertidumbres_y = np.array([0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,0.150,])

# Graficar los datos utilizando el método errorbar de matplotlib:
plt.errorbar(x, y, xerr=incertidumbres_x, yerr=incertidumbres_y, fmt='o', markersize=0, capsize=4, elinewidth=1)
plt.plot(x, y, 'r-', label='Curva Característica 1N4148', linewidth=2)
plt.xlabel('Vb [mV]') # Etiqueta del eje x
plt.ylabel('I [mA]') # Etiqueta del eje y

#plt.xticks(np.arange(min(x), max(x)+1, 2))
#plt.yticks(np.arange(min(y), max(y)+0.2, 0.2))

# Agregar la recta con la ecuación y = -0.1x + 1
x_recta = np.arange(max(x))
print(x_recta)
y_recta = -0.0001 * x_recta + 1
plt.plot(x_recta, y_recta, color='green')
print(y_recta[60])
"""x1 = np.linspace(0, 64, 100)
x1 = range(0, 64)
plt.plot(x1, -0.1*x1+1)"""

#plt.xlim(0, 1000)
#plt.ylim(-0.3, 2.309)

plt.title('Curva experimental diodo 1N4148') # Título del gráfico
plt.grid(True) # Mostrar cuadrícula en el gráfico
#plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.legend() # Mostrar leyenda
plt.show() # Mostrar el gráfico




"""import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# Definir los datos de x, y las incertidumbres:
x = np.array([10, 20, 28, 36, 40, 44, 44, 44, 48, 48, 48, 48, 52, 52, 52, 52, 52, 56, 56, 56, 56, 56, 60, 60, 60, 60, 60, 60, 64, 64, 64, 64, 64, 64]) # Datos de x
y = np.array([0.009,0.017,0.027,0.036,0.044,0.056,0.064,0.076,0.085,0.095,0.105,0.115,0.135,0.155,0.175,0.195,0.215,0.254,0.274,0.294,0.354,0.394,0.514,0.594,0.714,0.794,0.894,0.994,1.090,1.190,1.290,1.490,1.790,1.990]) # Datos de y

# Realizar interpolación lineal
f = interp1d(x, y, kind='linear')

# Generar puntos para la curva aproximada
x_interp = np.linspace(min(x), max(x), 100)
y_interp = f(x_interp)

# Graficar los datos y la curva aproximada
plt.errorbar(x, y, fmt='o', markersize=4, capsize=3, label='Datos')
plt.plot(x_interp, y_interp, 'r-', label='Curva aproximada', linewidth=2)
plt.xlabel('Vb [V]') # Etiqueta del eje x
plt.ylabel('I [mA]') # Etiqueta del eje y
plt.title('Curva característica diodo 1N4148') # Título del gráfico
plt.grid(True) # Mostrar cuadrícula en el gráfico
plt.legend() # Mostrar leyenda
plt.show() # Mostrar el gráfico"""