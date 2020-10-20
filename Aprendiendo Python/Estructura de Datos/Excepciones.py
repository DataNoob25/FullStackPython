

try:
    t=1/0
except ZeroDivisionError:
    print("No se puede dividir por cero")

def find(n,lista):
    index=0
    while True:
        try:
            if lista[index]==n:
                return index
        except IndexError: #error que se paso del indice de la lsita#
            return -1
        index+=1

print(find(1,[2,3,4,1]))
print(find(1,[2,3,4,0]))

def divide(x,y):
    try:
      result=x/y
    except ZeroDivisionError:
        print("Division por cero")
    else:
        print("El resultado es:", result)
    finally:
        print("Ejecutamos la clausula finally")

divide(3,5)
divide(2,0)

"""import math
def raiz_cuadrada(n):
    if n<0:
        #Levantamos errores#
        raise ValueError(" Numero negativo")
    return math.sqrt(n)
    
print(raiz_cuadrada(4))
print(raiz_cuadrada(-2))"""

class NegativeNumber(Exception):
    "Excepcion de tipo numero negativo"
    pass

import math
def raiz_cuadrada(n):
    if n<0:
        #Levantamos errores#
        raise NegativeNumber(" Numero negativo")
    return math.sqrt(n)
    
print(raiz_cuadrada(4))
print(raiz_cuadrada(-2))












