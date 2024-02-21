import numpy as np
import sympy as sp
import math as mt
from interpolante import *

def PoliTrigCoefi(X, Y, G):
    n = len(X) - 1
    maxg = int((n - 1) / 2)
    if G > maxg:
        G = maxg

    A = np.zeros(G + 1)
    B = np.zeros(G + 1)
    Yes = (Y[0] + Y[n]) / 2
    Y[0] = Yes
    Y[n] = Yes
    A[0] = np.sum(Y)

    for i in range(1, G + 1):
        A[i] = np.dot(np.cos(i * X), Y.T)
        B[i] = np.dot(np.sin(i * X), Y.T)

    A = 2 * A / n
    B = 2 * B / n
    A[0] = A[0] / 2

    return A, B

def PoliTrig(A, B, G):
    f = A[0]
    var = sp.symbols('x') #(2*sp.pi/19.5)* (2*sp.pi/21)*
    for k in range(1, G + 1):
        f += A[k] * sp.cos(k *  var) + B[k] * sp.sin(k * var)

    return f

def EvaPoliTrig(A, B, x, G):
    f = A[0]
    for k  in (1,G):
        f = f + A[k]*np.cos(k*x) + B[k]*np.sin(k*x)
    return f


#test 1
"""x = [-np.pi, -3*np.pi/5, -np.pi/5, np.pi/5, 3*np.pi/5, np.pi]
y = [-2*np.pi, -6*np.pi/5, -2*np.pi/5, 2*np.pi/5, 6*np.pi/5, 2*np.pi]

x = np.array(x)
y = np.array(y)

A, B = PoliTrigCoefi(x, y, 2)
print(A, B)

var = sp.symbols('x')
pol = PoliTrig(A, B, 2)
print(pol)


pnp = np.pi/4
psp = sp.pi/4

print(pol.subs(var, psp).evalf())
print(EvaPoliTrig(A, B, pnp, 2))
dat = data(x, y)
print(EvaPoliTrig(A, B, -np.pi/5, 2))
dat.graficar_pol_sp(pol, 'probando')"""


#test 2
x1 = np.array([0.7, 1.0, 1.3, 1.6, 1.9, 2.2])
y1 = np.array([0.5428, 0.7652, 0.6893, 0.1946, 0.2818, 0.1104])

x1 = np.array([0.0, 1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0, 13.5, 15.0, 16.5, 18.0, 19.5])
y1 = np.array([-1.000, -3.625, 5.000, 45.125, 137.000, 300.875, 557.000, 925.625, 1427.000, 2081.375, 2909.000, 3930.125, 5165.000, 6633.875])

# xtr = np.linspace(0,2*np.pi,2*np.pi/len(x1))
x1tr = np.linspace(0,2*np.pi,len(x1))
print(x1tr)

dat = data(x1tr, y1)
A, B = PoliTrigCoefi(x1tr, y1, 6)
var = sp.symbols('x')
px = PoliTrig(A, B, 6)

print(px.subs(18.0, var).evalf()) #-629.927610085526
print(EvaPoliTrig(A, B, 18, 6)) #-629.927610085526
dat.graficar_pol_sp(px, 'probando')
