import numpy as np
import sympy as sp

class sisEcuNoLin():

    def __init__(self, F, x0, itera, tol):
        self.F = sp.sympify(F)
        
        self.x0 = x0
        var = ''
        for i in range(len(x0)):
            var += f'x{i+1} '
        self.var = sp.symbols(var)
        
        self.F0 = sp.lambdify([i for i in self.var], self.F, 'numpy')

        self.J = sp.zeros(len(self.F),len(self.var)) # Initialise Jacobian matrix

        # Fill Jacobian matrix with entries
        for i, fi in enumerate(self.F):
            for j, s in enumerate(self.var):
                self.J[i,j] = sp.diff(fi, s)

        self.J0 = sp.lambdify([i for i in self.var], self.J, 'numpy')
    
    def newton_method(x, itera, tol):
        k = 1
        while k <= itera:
            F_x = F0(x)
            J_x = J0(x)
            y = np.linalg.solve(J_x, -F_x)
            x = x + y
            if np.linalg.norm(y) < tol:
                return x
            k += 1
        return 'Número máximo de iteraciones excedido'

x0 = sp.sympify([0.1, 0.1, -0.1])
print(type(x0))
var = ''
for i in range(len(x0)):
    var += f'x{i+1} '
x1, x2, x3 = sp.symbols(var)

f1 = 3*x1 - sp.cos(x2*x3) - 1/2
f2 = x1**2 - 81*(x2+0.1)**2 + sp.sin(x3) +1.06
f3 = sp.exp(-x1*x2) + 20*x3 + (10*sp.pi-3)/3
F = [f1, f2, f3] #matriz funcion
#x0 = np.array((0.1, 0.1, -0.1)).T #aproximacion inicial
itera = 100 # Número máximo de iteraciones
tol = 1e-6 # Tolerancia

r = sisEcuNoLin(F, x0, itera, tol)
print(r.F0(x0[0],x0[1],x0[2]))

#expr.evalf(20, subs={a:100, b:3})

#expr=a**2+b**2
#f=lambdify([a,b],expr)
#f(2,3)
#f=lambdify([a,b],expr, "numpy")