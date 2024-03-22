import math as mt

class ecu_dif():

    def __init__(self, a, b, y0, f, n):
        self.a = a
        self.b = b
        self.y0 = y0
        self.f = f
        self.n = n

    def gen(self,t,y):
        return self.f(t,y)

    def euler(self):
        h = (self.b - self.a)/self.n
        t = self.a
        w = self.y0
        print("t0 = {0:.2f}, w0 = {1:.6f}".format(t, w))
        for i in range(1, self.n+1):
            w = w + h*self.f(t, w)
            t = self.a + i*h
            print("\nt{0:<2} = {1:.2f}, w{0:<2} = {2:.6f}".format(i, t, w))
        return w

    def RK2(self):
        h = (self.b - self.a)/self.n
        t = self.a
        w = self.y0
        print("t0 = {0:.2f}, w0 = {1:.6f}".format(t, w))

        for i in range(1, self.n+1):
            k1 = h*self.f(t, w)
            k2 = h*self.f(t + h, w + k1)
            w = w + (k1 + k2)/2
            t = a + i*h
            print(f"\nk1 = {k1:<6f}, k2 = {k2:<6f}")
            print("t{0:<2} = {1:.2f}, w{0:<2} = {2:.6f}".format(i, t, w))
        return w

    def RK4(self):
        h = (self.b - self.a)/self.n
        t = self.a
        w = self.y0
        print("t0 = {0:.2f}, w0 = {1:.6f}".format(t, w))

        for i in range(1, self.n+1):
            k1 = h*self.f(t, w)
            k2 = h*self.f(t + h/2, w + k1/2)
            k3 = h*self.f(t + h/2, w + k2/2)
            k4 = h*self.f(t + h, w + k3)
            w = w + (k1 + 2*k2 + 2*k3 + k4)/6
            t = a + i*h
            print(f"\nk1 = {k1:<6f}, k2 = {k2:<6f}, k3 = {k3:<6f}, k4 = {k4:<6f}")
            print("t{0:<2} = {1:.2f}, w{0:<2} = {2:.6f}".format(i, t, w))
        return w


def f(x,y):
    return x**2-4*y

a, b = 0, 0.2
y0 = 1
n = 5

ins = ecu_dif(a, b, y0, f, n)
ins.RK2()