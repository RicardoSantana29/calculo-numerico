import math as mt
import sympy as sp

x = sp.symbols('x')

def trig(x):
    'funcion de prueba'
    return sp.cos(x)-x

def newton(f, p0, tol, n):
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
        p = p0 - (f.subs(x, p0)/sp.diff(f,x).subs(x, p0)).evalf()
        print("Iter = {0:<2}, p = {1:.12f}".format(i, p))
        if abs(p - p0) < tol:
            return p
        p0 = p
        i += 1
    print("Iteraciones agotadas: Error!")
    return None

fx = sp.cos(x)-x
print("Newton función trig(x):")
newton(fx, mt.pi/4, 1e-8, 100)

fx2 = 2*x - 2*sp.exp(-2*x) - 2*sp.exp(-x) + 2*x*sp.exp(-x)
print("Newton función expo(x):")
newton(fx2, 4, 1e-8, 100)

"""f = sp.sqrt(x)/x
print(sp.latex(f))"""