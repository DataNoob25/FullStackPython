"""import string
print(string.digits)
print(string.whitespace)"""

import string#Importamos la libreria String#
name = 'Agustín'
formatter=string.Formatter()#Instancia de la clase Formatter#
formatter.format('Hola {}', name)#LLamamos al metodo format de la clase#
'{} + {} + {} = {}'.format(1,2,3,6)
'{2} + {0} + {1} = {3}'.format(1,2,3,6)#Damos la posicion de los parametros en las llaves#
'{0} + {1}  = {result}'.format(2,10,result=12)

'{0:f} + {1:f}  = {result:f}'.format(2,10,result=12)

