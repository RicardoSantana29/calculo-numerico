import math as mt

def pol(x):
    """Función de prueba"""
    return x**3 + 4*(x**2) - 10 # retorna pol(x) = x3 + 4x2 − 10


def trig(x):
    """Función de prueba"""
    return x*mt.cos(x-1) - mt.sin(x) # retorna trig(x) = x cos(x − 1) − sin(x)


def bisec(f, a, b, tol, n):
    """
    Implementación método de bisección
    Entradas:
    f -- función
    a -- inicio intervalo
    b -- fin intervalo
    tol -- tolerancia
    n -- número máximo de iteraciones

    Salida:
    p aproximación a cero de f
    None en caso de iteraciones agotadas
    """
    i = 1
    while i <= n:
        p = a + (b - a)/2
        print("i = {0:<2}, p = {1:.12f}".format(i, p))
        if abs(f(p)) <= 1e-15 or (b - a)/2 < tol:
            return p
        i += 1
        if f(a)*f(p) > 0:
            a = p
        else:
            b = p
    print("Iteraciones agotadas: Error!")
    return None

def biseccion(f, a, b, tol, iter=100):
    a0 = a
    b0 = b
    c0 = (a0 +b0)/2
    k = 0
    while abs(f(c0)) > 0:
        if f(a0) * f(c0) < 0:
            b0 = c0
        else:
            a0 = c0
        c0 = (a0 + b0)/2
        k += 1
    return c0

# pol(x), a = 1, b = 2, TOL = 10e−8, N0 = 100
print("Bisección función pol(x):")
#bisec(pol, 1, 2, 1e-8, 100)
print(biseccion(pol, -2, 0, 1e-8))

# trig(x), a = 4, b = 6, TOL = 10−8, N0 = 100
print("Bisección función trig(x):")
#bisec(trig, 4, 6, 1e-8, 100)