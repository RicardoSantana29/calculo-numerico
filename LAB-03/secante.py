import math as mt

def trig(x):
    'funcion de prueba'
    return mt.sin(2/x)

def pol(x):
    'funcion de prueba'
    return x**3 - 2

def secante(f, p0, p1, tol, n):
    """Implementación método de la secante
    Entradas:
    f -- función
    p0 -- aproximación inicial
    p1 -- aproximación inicial
    tol -- tolerancia
    n -- número máximo de iteraciones
    Salida:
    p aproximación a cero de f
    None en caso de iteraciones agotadas"""
    i = 2
    while i <= n:
        p = p1 - (f(p1)*(p1 - p0))/(f(p1) - f(p0))
        print("Iter = {0:<2}, p = {1:.12f}".format(i, p))
        if abs(p - p1) < tol:
            return p
        p0 = p1
        p1 = p
        i += 1
    print("Iteraciones agotadas: Error!")
    return None

print("Secante función pol(x):")
secante(pol, -3, 3, 1e-8, 100)

print("Secante función trig(x):")
secante(trig, 1.1, 0.8, 1e-8, 100)