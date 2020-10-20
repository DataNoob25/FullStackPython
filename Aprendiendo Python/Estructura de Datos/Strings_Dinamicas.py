name="Agustin"
" Hola %s " %name
"El numero es %d" %10
"El numero es %02d" %5 #Autocompletado con 0#
"El decimal es %f" %5.6
"El decimal es %.2f" %5.6 #Hace mas corto la parte decimal#
"Hola %(ty)s" %{'ty':name} #Diccionario#
"Hola {}".format(name) #Reemplaza las llaves por la variable#
"La suma de 1+2 es {}".format(1+2)

" ".join(["hola", name]) #Concatenamos una lista con la funcion join#