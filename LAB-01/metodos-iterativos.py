import numpy as np

class iterativos():
    def __init__(self,A,b):
        self.A = A
        self.b = b
        self.D = np.diag(np.diagonal(A))
        self.Al = np.tril(A)*(-1)
        self.Au = np.triu(A)*(-1)

inst = iterativos(np.array([[4,1,-1,0],[1,3,-1,0],[-1,-1,5,2],[0,0,2,4]],dtype='f'), [-1,-1,5,2])

print(inst.D)
print(inst.Au)