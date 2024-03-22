import numpy as np

M = [[3,2], [7,-2]]
#M = [[2,0,0],[1,1,2],[1,-1,4]]
#M = [[3,2], [1,4]]

#metodo 1

A = np.array(M)

x, v = np.linalg.eig(A)
print('\neigenvalores:\n', x)
print('\neigenvectores:\n', v)#/(np.sqrt(2)/2))

#metodo 2

import sympy as sp

B = sp.Matrix(M)

print('\neigenvalores:\n', B.eigenvals())
print('\neigenvectores:\n', B.eigenvects())