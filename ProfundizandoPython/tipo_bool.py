#bool tiene true o false
#tipos numericos

# valor = 0
# resultado=bool(valor)
# print(resultado)

#tipo string
# va a regresar falso si la cadena esta vacia distinto va a ser verdadero
# valor=''
# resultado=bool(valor)
# print(resultado)

#tipo colecciones Flase para colecciones vacias y verdadero para todas las demas conexiones
#lista

# valor=[]
# resultado=bool(valor)
# print(resultado)

#tupla es como la lista
#
#Diccionario
# valor ={}
# resultado=bool(valor)
# print(resultado)
# valor={'nombre':'Juan'}
# resultado=bool(valor)
# print(resultado)

#aca se lllama automaticamente bool si cadenas enteros listas tuplas o diccionarios estan vacios manda falso
if {}:
    print('Regreso verdadero')
else:
    print('Regreso falso')

cadena=' '
#asi como el if funciona el while
while cadena:
    print('ejecucion del ciclo del while')
    break
else:
    print('no se ejecuta el ciclo del while')