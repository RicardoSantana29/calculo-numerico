import math as mt

def expo(x):
    "Función de prueba"
    return x**2 + mt.exp(-2*x) - 2*x*mt.exp(-x) # retorna expo(x) = x^2 + e^(−2x) − 2xe^(−x)

def expoprima(x):
    "Derivada función de prueba"
    return 2*x - 2*mt.exp(-2*x) - 2*mt.exp(-x) + 2*x*mt.exp(-x) # retorna expoprima(x) = derivada_de_expo(x)

def trig(x):
    "Función de prueba"
    return mt.cos(x) - x # retorna trig(x) = cos(x) − x

def trigprima(x):
    "Derivada función de prueba"
    return -mt.sin(x) - 1 # retorna trigprima(x) = derivada_de_trig(x)

def newton(f, fprima, p0, tol, n):
    """Implementación método de Newton
    Entradas:
    f -- función
    fprima -- derivada función f
    p0 -- aproximación inicial
    tol -- tolerancia
    n -- número máximo de iteraciones
    Salida:
    p aproximación a cero de f
    None en caso de iteraciones agotadas
    B.1. BÚSQUEDA DE RAÍCES 145"""
    i = 1
    while i <= n:
        p = p0 - f(p0)/fprima(p0)
        print("Iter = {0:<2}, p = {1:.12f}".format(i, p))
        if abs(p - p0) < tol:
            return p
        p0 = p
        i += 1
    print("Iteraciones agotadas: Error!")
    return None

print("Newton función trig(x):")
newton(trig, trigprima, mt.pi/4, 1e-8, 100)

print("Newton función expo(x):")
newton(expo, expoprima, 4, 1e-8, 100)