def peso(masa, gravedad=9.8): 
    "Formula del peso"
    return masa*gravedad

print(peso(4))  #Argumentos posicionales#
print(peso(4,3))
print(peso(masa=4,gravedad=3))
print(peso(gravedad=5,masa=3))

def lista(*args):  #Lista de parametros#
    return args[1]

print(lista(6,5,3,6,8))


def suma(n):
    "sumar n numeros"
    n2=4
    return n2+n

print(suma(4))