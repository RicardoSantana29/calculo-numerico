#Implementación de la regla de Simpson y algunos casos de salida.

from math import *

"""Funciones de prueba"""
exp = lambda x: -exp(x**2)+3
pol = lambda x: x**3 + 4*x**2 - 10
trig = lambda x: x*cos(x-1) - sin(x)

def simpson(f, a, b, n):
    """
    Implementación regla de Simpson
    Entradas:
    f -- función
    a -- inicio intervalo
    b -- fin intervalo
    n -- número de pasos (par)

    Salida:
    abc -- aproximación área bajo la curva
    """
    h = (b - a)/n
    oddsum = 0
    evensum = 0
    for j in range(1, n):
        x = a + h*j
        if j % 2 == 0:
            evensum += 2*f(x)
        else:
            oddsum += 4*f(x)
        abc = (h/3)*(f(a) + evensum + oddsum + f(b))
    return abc

# pol(x), a = 1, b = 2, N = 10
print("Área bajo la curva pol(x):")
print("{0:.12f}".format(simpson(pol, 1, 2, 10)))

# trig(x), a = 4, b = 6, N = 20
print("Área bajo la curva trig(x):")
print("{0:.12f}".format(simpson(trig, 4, 6, 20)))

print("Área bajo la curva exp(x):")
print("{0:.12f}".format(simpson(exp, -1, 1, 20)))