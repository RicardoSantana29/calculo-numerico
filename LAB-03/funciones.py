import math as mt

#funciones definidas para el problema test
def trig(x):
    return mt.cos(x) - x

def trigPrima(x):
    return -mt.sin(x) - 1

def trigPuntoFijo(x):
    return mt.cos(x)

def trigPuntoFijoPrima(x):
    return -mt.sin(x)

#funciones definidas para el problema 1
def exp(x):
    return mt.exp(x)-2-x

def expPrima(x):
    return mt.exp(x)-1

def expPuntoFijo(x):
    return mt.exp(x)-2

def expPuntoFijoPrima(x):
    return mt.exp(x)

