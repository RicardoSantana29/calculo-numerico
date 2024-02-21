# Implementación extrapolación de Richardson y algunos casos de salida.
from math import *

'Funciones de prueba'
pol = lambda x: x**3 + 4*x**2 - 10
trig = lambda x: x*cos(x-1) - sin(x) # x en radianes

def dercentrada(f, x, h):
    'Retorna diferencias centradas'
    return (f(x + h) - f(x - h))/(2*h)

def progresiva(f, x, h):
    return (f(x + h) - f(x))/h

def regresiva(f, x, h):
    return (f(x) - f(x - h))/h

def dif_fin(f, x, h):
    """
    Implementación extrapolación de Richardson
    Entradas:
    f -- función
    x -- punto
    h -- paso

    Salida:
    d -- aproximación a la derivada
    """
    d = (4/3)*dercentrada(f, x, h/2)-(1/3)*dercentrada(f, x, h)
    return d

# pol(x), x = 1.5, h = 0.1
print("Derivada función pol(x):")
print("{0:.12f}".format(dif_fin(pol, 1.5, 0.1)))

# trig(x), x = 4, h = 0.2
print("Derivada función trig(x):")
print("{0:.12f}".format(dif_fin(trig, 4, 0.2)))