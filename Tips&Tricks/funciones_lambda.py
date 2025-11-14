#lambda son funciones q permiten declarar funciones anonimas en solo 1 linea de codigo
#ejemplo normal
from funciones import mostrar_ing


def sumar(a,b):
    return a+b
print(sumar(2,4))
#funcion Lambda
sumar_lambda = lambda a,b: a+b
print(sumar_lambda(2,4))

#Utilizando 1 sola linea de codigo
print((lambda a,b: a+b)(2,4))

#podemos usar una funcion lambda siempre que necesitemos una funcion muy concreta
#Ej.ordenar una lista de tuplas por su segundo valor proporcionando una llave(key)
lista_tuplas=[(1,'b'),(2,'f'),(5,'a'),(4,'c')]
#asi se ordena una lista de tuplas con llaves y puedo pasarle el reverse
lista_tuplas_ordenada = sorted(lista_tuplas,key=lambda tupla:tupla[0],reverse=True)
print(lista_tuplas_ordenada)
#ordenar por letras
lista_tuplas_ordenada = sorted(lista_tuplas,key=lambda tupla:tupla[1])
print(lista_tuplas_ordenada)
#otro ejemplo de ordenamiento usando una expresion lambda
print(list(range(-3,4)))
#Si queremos ordenar por el valor absoluto sin considerar signo
for valor in range(-3,4):
    print(valor ,valor*valor)
#ahora lo aplicamos a una expresion lambda
lista_ordenada= sorted(range(-3,4),key=lambda valor:valor*valor)
print(lista_ordenada)

#las funciones lambda tambien pueden aplicar el concepto de clousure

def mostrar(titulo):
    return lambda mensaje:titulo+'.'+mensaje
mostrar_ing=mostrar('Ingenieria')
mostrar_lic=mostrar('Licenciada')
print(mostrar_ing('Daniela tellez'))
print(mostrar_lic('Juliteta benes'))

#ejemplos de casos de funciones lambda no recomendables
class Prueba:
    mostrar = lambda self:print('funcion mostrar')
    saludar = lambda self:print('funcion saludar')

prueba = Prueba()
prueba.mostrar()
prueba.saludar()

#otro ejemplo donde una funcion lambda agregaria complejidad innecesaria
lista_pares = list(filter(lambda valor:valor%2 == 0,range(0,9)))
print(lista_pares)
#resolviendo el mismo ejercicio peor usando list comprehensions
lista_pares_modificada=[valor for valor in range(10) if valor % 2 == 0]
print(lista_pares_modificada)