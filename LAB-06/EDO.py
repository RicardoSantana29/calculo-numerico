import math as mt
import numpy as np

class EDO():

    def __init__(self, a, b, y0, N, f):
        self.a = a
        self.b = b
        self.y0 = y0
        self.N = N
        self.f = f
        """
        Implementación de métodos
        Entradas:
        a -- inicio intervalo
        b -- fin intervalo
        y0 -- aproximación inicial
        f -- función
        N -- pasos

        Salida:
        w -- aproximación final
        """

    def euler(self):
        h = (self.b - self.a)/self.N
        t = self.a
        w = self.y0
        print("t0 = {0:.2f}, w0 = {1:.12f}".format(t, w))
        for i in range(1, self.N+1):
            w = w + h*self.f(t, w)
            t = self.a + i*h
            print("t{0:<2} = {1:.2f}, w{0:<2} = {2:.12f}".format(i, t, w))
        return w

    def RK4(self):
        h = (self.b - self.a)/self.N
        t = self.a
        w = self.y0
        print("t0 = {0:.2f}, w0 = {1:.12f}".format(t, w))

        for i in range(1, self.N+1):
            k1 = h*self.f(t, w)
            k2 = h*self.f(t + h/2, w + k1/2)
            k3 = h*self.f(t + h/2, w + k2/2)
            k4 = h*self.f(t + h, w + k3)
            w = w + (k1 + 2*k2 + 2*k3 + k4)/6
            t = self.a + i*h
            print("t{0:<2} = {1:.2f}, w{0:<2} = {2:.12f}".format(i, t, w))
        return w

    def sis_euler(self):
        h = (self.b - self.a)/self.N
        t = self.a
        w = np.array(self.y0)
        v = np.concatenate([[t],w])
        print("t_0 = {0:.2f}, u1_0 = {1:.12f}, u2_0 = {2:.12f}, u3_0 = {3:.12f}".format(t, w[0], w[1], w[2]))
        
        for i in range(1, self.N+1):
            w = w + h*self.f(t, w)
            t = self.a + i*h
            print("t{0:<2} = {1:.2f}, u1_{0:<2} = {2:.12f}, u2_{0:<2} = {3:.12f}, u3_{0:<2} = {4:.12f}".format(i, t, w[0], w[1], w[2]))
        return np.concatenate([[t],w])

    def sis_RK4(self):
        h = (self.b - self.a)/self.N
        t = self.a
        w = np.array(self.y0)
        v = np.concatenate([[t],w])
        print("t_0 = {0:.2f}, u1_0 = {1:.12f}, u2_0 = {2:.12f}, u3_0 = {3:.12f}".format(t, w[0], w[1], w[2]))

        for i in range(1, self.N+1):
            k1 = h*self.f(t, w)
            k2 = h*self.f(t + h/2, w + k1/2)
            k3 = h*self.f(t + h/2, w + k2/2)
            k4 = h*self.f(t + h, w + k3)
            w = w + (k1 + 2*k2 + 2*k3 + k4)/6
            t = self.a + i*h
            print("t{0:<2} = {1:.2f}, u1_{0:<2} = {2:.12f}, u2_{0:<2} = {3:.12f}, u3_{0:<2} = {4:.12f}".format(i, t, w[0], w[1], w[2]))
        return np.concatenate([[t],w])


"""def test1(t, y): # y0 = y − t2 + 1
    return y - t**2 + 1

def test2(t, y): # y0 = 2 − e−4t − 2y
    return 2 - exp(-4*t) - 2*y"""


"""def f(t, vec):
    u1, u2, u3 = vec[0], vec[1], vec[2]
    du1 = u2
    du2 = -u1 -2*mt.exp(t) +1
    du3 = -u1 -mt.exp(t) +1
    return np.array([du1, du2, du3])

u10, u20, u30 = 1, 0, 1
vec = [u10, u20, u30]

ed1 = EDO(0, 2, vec, 40, f)

ed1.sis_euler()"""



"""def g1(u2, u1):
    return u1

def g2(ecua):#t, u1, u2):
    return -ecua[1] -2*mt.exp(ecua[0]) +1 #-u1 -2*mt.exp(t) +1

def g3(t, u1, u3):
    return -u1 -mt.exp(t) +1

u10, u20, u30 = 1, 0, 1

a = np.array([1, u10, u20])
print(a)
print(g2(a))

# Definir las ecuaciones diferenciales
def f1(u1, u2, t):
    return u2

def f2(u1, t):
    return -u1 - 2*mt.exp(t) + 1

def f3(u1, t):
    return -u1 - mt.exp(t) + 1

# Definir los valores iniciales y el tamaño del paso
u1_0 = 1
u2_0 = 0
u3_0 = 1
h = 0.05

# Definir el rango de tiempo
t_start = 0
t_end = 2

# Calcular el número total de pasos
N = int((t_end - t_start) / h)

# Inicializar las variables de aproximación
t = t_start
u1 = u1_0
u2 = u2_0
u3 = u3_0

# Realizar la aproximación numérica usando el método de Euler
for _ in range(N):
    k1u1 = f1(u1, u2, t)
    k1u2 = f2(u1, t)
    k1u3 = f3(u1, t)

    u1 += h * k1u1
    u2 += h * k1u2
    u3 += h * k1u3

    t += h

# Imprimir los resultados en cada paso
print(f"t={t:.2f}, u1={u1:.6f}, u2={u2:.6f}, u3={u3:.6f}")"""