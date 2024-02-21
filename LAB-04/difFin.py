import numpy as np

def difer(x, y, tipo = 0, orden = 1):
    # tipo = (-1: Diferecia hacia atras , 0: Centrada , 1: Diferencia hacia adelante )
    # orden = (1: Primer orden , 2: Segundo orden )

    n=x. size #shape
    if tipo == -1: # Diferencias hacia atras
        if orden ==1:
            return [(y[i]-y[i -1]) /(x[i]-x[i -1]) for i in range (1,n)]
        elif orden ==2:
            return [(y[i] -2*y[i -1]+ y[i -2]) /(x[i]-x[i -1])**2 for i in range (2,n)]
        else :
            raise ValueError ( ' Parametro <Orden> incorrecto ')
    elif tipo == 0: # Diferencias centradas
        if orden ==1:
            return [(y[i+1] -y[i-1]) / (2*(x[i]-x[i -1])) for i in range (1,n -1) ]
        elif orden ==2:
            return [(y[i +1] -2* y[i]+y[i -1]) /(x[i]-x[i -1])**2 for i in range (1,n -1) ]
        else :
            raise ValueError ( ' Parametro <Orden> incorrecto ')
    elif tipo ==1: # Diferencias hacia adelante
        if orden ==1:
            return [(y[i+1] -y[i]) /(x[i+1] -x[i]) for i in range (n -1) ]
        elif orden ==2:
            return [(y[i +2] -2* y[i +1]+ y[i]) /(x[i]-x[i -1]) **2 for i in range (0,n -2) ]
        else :
            raise ValueError ( ' Parametro <Orden> incorrecto ')
    else :
        raise ValueError ( ' Parametro <Tipo > incorrecto ')