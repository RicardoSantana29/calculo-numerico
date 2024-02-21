# Implementación de la regla del trapecio y algunos casos de salida.

from math import *

"""Funciones de prueba"""
pol = lambda x: x**3 + 4*x**2 - 10
trig = lambda x: x*cos(x-1) - sin(x)

def trapecio(f, a, b, n):
    """
    Implementación regla del trapecio
    Entradas:
    f -- función
    a -- inicio intervalo
    b -- fin intervalo
    n -- número de pasos
    Salida:
    abc -- aproximación área bajo la curva
    """
    h = (b - a)/n
    acum = 0
    for j in range(1, n):
        acum += 2*f(a + h*j)
        abc = (h/2)*(f(a) + acum + f(b))
    return abc

# pol(x), a = 1, b = 2, N = 10
print("\nÁrea bajo la curva pol(x):\n")
print("{0:.12f}".format(trapecio(pol, 1, 2, 10)))

# trig(x), a = 4, b = 6, N = 20
print("\nÁrea bajo la curva trig(x):\n")
print("{0:.12f}".format(trapecio(trig, 4, 6, 20)))