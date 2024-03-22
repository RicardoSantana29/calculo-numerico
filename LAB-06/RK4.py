# Implementación del método RK4 y algunos casos de salida.

from math import *

def test1(t, y): # y0 = y − t2 + 1
    """Función de prueba"""
    return y - t**2 + 1


def test2(t, y): # y0 = 2 − e−4t − 2y
    """Función de prueba"""
    return 2 - exp(-4*t) - 2*y


def RK4(a, b, y0, f, N):
    """
    Implementación método RK4
    Entradas:
    a -- inicio intervalo
    b -- fin intervalo
    y0 -- aproximación inicial
    f -- función
    N -- pasos

    Salida:
    w -- aproximación final
    """
    h = (b - a)/N
    t = a
    w = y0
    print("t0 = {0:.2f}, w0 = {1:.12f}".format(t, w))

    for i in range(1, N+1):
        k1 = h*f(t, w)
        k2 = h*f(t + h/2, w + k1/2)
        k3 = h*f(t + h/2, w + k2/2)
        k4 = h*f(t + h, w + k3)
        w = w + (k1 + 2*k2 + 2*k3 + k4)/6
        t = a + i*h
        print("t{0:<2} = {1:.2f}, w{0:<2} = {2:.12f}".format(i, t, w))
    return w


# dy
#= y − t2 + 1, a = 0, b = 2, y0 = 0.5, N = 10
print("Método RK4:")
RK4(0, 2, 0.5, test1, 10)

# dy
#dt = 2 − e−4t − 2y, a = 0, b = 1, y0 = 1, N = 20

print("Método RK4:")
RK4(0, 1, 1, test2, 20)