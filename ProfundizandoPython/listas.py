#profundizando listas
#listas son mutables
from turtledemo.penrose import start

#sumar 2 listas

nombres=['fernando','carlos','gerardo']
apellidos='Fernandez Gonzalez Chavelo Carvajal Tempes Rendon Zepeda'.split()
#sumar listas
print('Sumar listas : ',nombres+apellidos)
#extender una lista sobre otra lista
nombres.extend(apellidos)
print(nombres)

#lista de numeros

numeros1=[10,40,15,4,20,90,4]
#obtener indice del primer elemento encontrado en una lista
#ewncuentra el index del primer valor encontrado entre parentesis
print(f'Lista original: {numeros1}')
print(f'Indice 4: {numeros1.index(4)}')

#invertir el orden de una lista
numeros1.reverse()
print(f'Lista reversa: {numeros1}')

#ordenar los elementos de una lista
#ordena de mayor a menor
numeros1.sort()
print(f'Lista ordenada: {numeros1}')

#ordenas de descendente
numeros1.sort(reverse=True)
print(f'Lista ordenada en reversa: {numeros1}')

#obtener el valor minimo y maximo de una lista

print(f'Valor minimo de una lista: {min(numeros1)}')
print(f'Valor maximo de una lista: {max(numeros1)}')

#copiar elementos de una lista

# numeros2 = numeros1.copy()
# print(numeros1)
# print(numeros2)
# print(f'Misma Referencia: {numeros1 is numeros2}')
# print(f'Mismo contenido? {numeros1 == numeros2}')

#podemos utilizar el constructor de la lista
numeros2 = list(numeros1)

print(f'Misma Referencia: {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

#slicing
#sirve para copiar listas igual
#se ponen solo los dos puntos para no especificar donde va a empezar y donde va terminar
numeros2 = numeros1[:]
print(f'Misma Referencia: {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

#multiplicacion de listas

lista_multiplicacion=5*[[2,5]]
print(f'Lista multiplicacion: {lista_multiplicacion}')
print(f'Misma referencia:{lista_multiplicacion[0] is lista_multiplicacion[1]}')
print(f'Mismo contenido? {lista_multiplicacion[0] == lista_multiplicacion[1]}')
#si multiplico cualquier sublista siempre se va a actualizar todas por que tienen la misma referencia en memoria
lista_multiplicacion[2].append(10)
print(f'Lista multiplicacion: {lista_multiplicacion}')

#matrices en python
#lista de listas

matriz=[[10,20],[30,40,50],[60,70,80,90]]
print(f'Matriz original: {matriz}')

print(f'Reglon 0 columna 0: {matriz[0][0]}')
print(f'Reglon 2 columna 2: {matriz[2][2]}')
matriz[2][0]=65
print(f'Matriz Modificada: {matriz}')

#lista de listas

lista_listas=[[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
#se ordena con sort y en el parametro pasamaos key len para que ordene por largo de cada sublista
print(f'Lista original: {lista_listas}')
lista_listas.sort(key=len)
print(f'Lista ordenada: {lista_listas}')

#build in
nombres=['fernando','carlos','gerardo']
nombres.sorted(nombres)