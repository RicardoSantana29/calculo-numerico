import pandas as pd
import numpy as np
import sympy as sp

#funcion de creacion en dataframe de los sistema lineales y su error
def a_df(df, sist, metodo, resp):
    if type(df) != str:
        return pd.DataFrame(df, index=resp, columns=[metodo]), pd.DataFrame(np.dot(sist.A, df)-sist.b, index=[1,2,3], columns=[metodo])
    else:
        print(df)
        return pd.DataFrame(None, index=resp, columns=[metodo]), pd.DataFrame(None, index=[1,2,3], columns=[metodo])

#transforma los ángulos hacia un intervalo entre 0 y 2pi
def angulo(a):
    if a<-360 or a>360:
        return a%360
    if a<0:
        return a+360
    return a

#para el analisis y guardado en csv de el analisis de sistemas no lineales
def analisis_SENL(metodo, ruta, x0, F, itera, tol, var, i):
    angles = metodo(x0, F, itera, tol) #aplicando metodo de Newton para ecuaciones no lineales
    angles = [angulo(i) for i in angles] 
    print('\nphi = ', angles[0])
    print('\nalpha = ', angles[1])
    print('\ntheta = ', angles[2])
    F0 = sp.lambdify([i for i in var], sp.matrices.Matrix(F)) #creacion de función que evalua el sistema en el resultado

    #guardado de resultado en .csv
    dferr = pd.DataFrame(F0(angles[0],angles[1],angles[2]), index=['phi','alpha','theta'], columns=[f'error {i}'])
    dfx0 = pd.DataFrame(x0, index=['phi','alpha','theta'], columns=[f'inicial {i}'])
    dfang = pd.DataFrame([angles[0],angles[1],angles[2]], index=['phi','alpha','theta'], columns=[f'resultado {i}'])
    pd.concat([dfx0,dfang,dferr], axis=1).to_csv(f'{ruta}/respuesta3_{i}.csv')

    return angles