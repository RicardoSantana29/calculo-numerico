import math as mt
import random as rd
import sympy as sp
from sympy.abc import x,y,z

class integrar():

    def __init__(self, f, a, b, n = 100):
        self.f = f
        self.a = a
        self.b = b
        self.n = n
        self.h = (self.b-self.a)/self.n
        self.xi = rd.uniform(self.a, self.b)

    def trapecio(self):
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
        h = (self.b-self.a)/self.n
        acum = 0
        for j in range(1, self.n):
            acum += 2*self.f(self.a + h*j)
            abc = (h/2)*(self.f(self.a) + acum + self.f(self.b))
        return abc

    def simpson(self):
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
        h = (self.b-self.a)/self.n
        oddsum = 0
        evensum = 0
        for j in range(1, self.n):
            x = self.a + h*j
            if j % 2 == 0:
                evensum += 2*self.f(x)
            else:
                oddsum += 4*self.f(x)
            abc = (h/3)*(self.f(self.a) + evensum + oddsum + self.f(self.b))
        return abc

    def err_trapecio(self, f_sp):
        h = (self.b-self.a)/self.n
        return (h**3 / 12)*sp.diff(f_sp, x, 2).subs(x, self.xi)

    def err_simpson(self, f_sp):
        h = (self.b-self.a)/self.n
        return (h**5 / 90)*sp.diff(f_sp, x, 4).subs(x, self.xi)


"""pol = lambda x: x**3 + 4*x**2 - 10
f_sp = sp.sympify('x**3 + 4*x**2 - 10')

trig = lambda x: x*mt.cos(x-1) - mt.sin(x)
t_sp = sp.sympify('x*cos(x-1) - sin(x)')

s = integrar(trig, 1, 2, 20)
# pol(x), a = 1, b = 2, N = 10
print("\nÁrea bajo la curva trig(x):\n")
print(s.simpson())
print("\nError:\n")
print(s.err_simpson(t_sp))"""