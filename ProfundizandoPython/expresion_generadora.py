#Expresion generadora (es un generador anonimo)
from diccionarios import nombre

multiplicacion=(valor*valor for valor in range(4))
print(multiplicacion)
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
#print(next(multiplicacion))

#expresion generadora a una funcion

import math

suma = sum(valor*valor for valor in range(4))
print(suma)


#tambien podemos usar una lista o cualquier otro iterador

lista = ['Juan','Daniel']
generador=(valor for valor in lista)
print(next(generador))
print(next(generador))

#crear un stirng apartir de un generador apartir de una lista

lista =['Karla','Gomez',22]
contador=0
#funcion incrementar el contador
def incrementar():
    global contador
    contador+=1
    return contador
# la primera parte es el yield y la segunda es el for entre parentesis
generador=(f'{incrementar()}.{nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena=', '.join(lista)
print(cadena)