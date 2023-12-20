import numpy as np
import sympy as sp
import math as mt

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

def EvaPoliTrig(A, B, G):
    f = A[0]
    var = sp.symbols('x')
    for k in range(1, G + 1):
        f += A[k] * sp.cos(k *  var) + B[k] * sp.sin(k * var)

    return f

