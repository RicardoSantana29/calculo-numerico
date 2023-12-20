import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
#import sympy.plotting as plot

def lagrange_coefi(X, Y):
    x = sp.symbols('x')
    
    n = len(X)
    C = 0 #[0] * n
    for k in range(n):
        d = 1
        for i in range(n):
            if i != k:
                d = d * (x - X[i]) / (X[k] - X[i])
        C += Y[k] * d

        C = sp.simplify(C) #simplificando a su minima expresion el polinomio de lagrage
    return C

def Interpol_Lag(xi,yi,n):
    x=sp.symbols('x')
    L=[]
    for i in range(n):
      Li=1
      for j in range(n):
        if j!=i:
          Li=Li*((x-xi[j])/(xi[i]-xi[j]))
      L.append(Li)

    ecuacion=0
    for i in range(n):
      ecuacion=ecuacion+L[i]*yi[i]

    ecuacion=sp.expand(ecuacion)
    print(ecuacion)
    return(ecuacion)

x = [0,1,2]
y = [1,2,5]
X = np.array(x)
Y = np.array(y)

c = lagrange_coefi(X, Y)

x = sp.symbols('x')
print(c)
print(c.subs(x,2))

plt.grid()
plt.plot(X,Y,'bo')

d = np.linspace(min(X),max(X),100)
f = [c.subs(x,i) for i in d]
plt.plot(d,f,'r-')

plt.title('Grafica Polinomio de lagrange')
plt.ylabel('Y')
plt.xlabel('X')
plt.show()