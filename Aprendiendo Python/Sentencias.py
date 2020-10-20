"""def buscar_numero(numero, lista):
 indice=-1
 for i, item in enumerate(lista):
    if item == numero:
     indice=i
     break
 return indice
print(buscar_numero(1,[2,3,4,1,5,6]))"""



"""for i in range(2,10):
    if i%2==0:
        print(i," es un numero par")
        continue
        print(i," es un numero impar")"""

"""def buscar_numero(numero, lista):
 indice=-1
 for i, item in enumerate(lista):
    if item == numero:
     indice=i
     break
 else :
     indice=-2
 return indice

print(buscar_numero(1,[2,3,4,1,5,6]))
print(buscar_numero(1,[2,3,4,8,5,6]))"""

"""def es_primo(numero):
   
   resultado = True

   for divisor in range(2, numero):

       if (numero % divisor) == 0:

           resultado = False

           break

   return resultado

print(es_primo(13))"""


   
s=0
for n in range(1, 10):

 if n % 2 != 0:

  continue

 s+=n
  
print(s)










        

