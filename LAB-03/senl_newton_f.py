import numpy as np
 # Metodo de Newton
def newtonRaphsonMV (F, J, x, imax =400 , tol =1e-8):
 cumple = False
 k =0
 while (not cumple and k < imax ) :
     deltax = np . linalg . solve ( J(x) ,-F(x))
     x = x + deltax
     print ('iteracion :{} - > {} '.\
            format (k , x ) )
     cumple = np . linalg . norm (F(x)) <= tol
     k +=1
 if k < imax :
    return x
 else :
    raise ValueError ('La funcion no converge ')

 # Vector de Funciones
def f ( x ) :
    return np . array ([(x[0]**2)-3*x[1]+x[2]+np.sin(x[3])+np.log(abs(x[4]))+6 ,x [0]+x[2]-np.cos(x[4])-(1.532*(10)**-4),x[0]+((x[1])**2)-x[2]-13,x[0]+x[2]-x[3]+((x[4])**2)-2,x[0]+x[1]+((x[2])**2)+((x[3])**2)-6])
 # Matriz Jacobiana
def j(x) :
    return np . array ([[2*x[0] , -3,1,np.cos(x[3]),1/x[4]],[ 1 , 0,1,0,np.sin(x[4]) ],[1,2*x[1],-1,0,0],[1,0,1,-1,2*x[4]],[1,1,2*x[2],2*x[3],0]])
# valores iniciales
x0 = np . array ([ 1, 1,1,1,1])
# Llamada al algoritmo
raiz = newtonRaphsonMV (f ,j, x0 )
print ('f ({}) ={} '. format ( raiz , f ( raiz ) ) )
print(raiz,'resultado')

#TEST Metodo de newton para sistemas de ecuaciones no lineales
 # Metodo de Newton
def newtonRaphsonMV (F ,J,x , imax =400 , tol =1e-8) :
 cumple = False
 k =0
 while (not cumple and k < imax ) :
     deltax = np . linalg . solve ( J(x) ,-F(x))
     x = x + deltax
     print ('iteracion :{} - > {} '.\
            format (k , x ) )
     cumple = np . linalg . norm (F(x)) <= tol
     k +=1
 if k < imax :
    return x
 else :
    raise ValueError ('La funcion no converge ')

 # Vector de Funciones
# Vector de Funciones
def f ( x ) :
  return np . array ([2* x [0] - x [1] - np . exp ( - x [0]) ,\
                       -x [0] + 2* x [1] - np . exp ( - x [1]) ])
# Matriz Jacobiana
def j ( x ) :
 return np . array ([[2 + np . exp ( - x [0]) , -1] ,\
                     [ -1 , 2 + np . exp ( - x [1]) ]])


# valores iniciales
x0 = np . array ([ 1, 1])
# Llamada al algoritmo
raiz = newtonRaphsonMV (f ,j, x0 )
print ('f ({}) ={} '. format ( raiz , f ( raiz ) ) )
print(raiz,'resultado')