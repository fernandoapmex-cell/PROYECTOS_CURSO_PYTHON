
#este comendo es para ver de que se compone python
#print(dir(__builtins__))
numeros=[1,2,3]
letras=['a','b','c']
identificadores=321,323,323,324,325,326
conjunto={6,4,0,9,8,15,10}
mezcla=zip(numeros,letras,identificadores,conjunto)
#print(mezcla)
print(list(mezcla))
#print(tuple(zip(numeros,letras)))

#iterar en paralelo
for numero,letra,identificador,aleatorio in zip(numeros,letras,identificadores,conjunto):
    print(f'{numero},{letra},{identificador},{aleatorio}')

nueva_lista=[]
for numero,letra,identificador,aleatorio in zip(numeros,letras,identificadores,conjunto):
    nueva_lista.append((f'{identificador}-{numero}-{letra}-{aleatorio}'))
print(nueva_lista)

#unzip
mezcla =[(1,'a'),(2,'b'),(3,'c')]
numeros,letas=zip(*mezcla)
print(f'Numeros: {numeros}',f'Letas: {letas}')

#ordenamiento usando zip
letras = ['c','d','a','e','b']
numeros=[3,2,4,1,0]
mezcla=zip(letras,numeros)
#sin ordenar
print(tuple(mezcla))
#ordenar por letra
print(sorted(zip(letras,numeros)))
#ordenar por numero
print(sorted(zip(numeros,letras)))
#crear un diccionario con zip y 2 iterables
#tambien funciona con tuplas
llaves=['Nombre','Apellido','Edad']
valores=['Juan','Perez',18]
#creamos un dic con los iterables
diccionario=dict(zip(llaves,valores))
print(diccionario)
#Actualizar un elemento de un diccionario
llave=['Edad']
nueva_edad=[90]
#update es un metodo de los diccionarios para actualizar
diccionario.update(zip(llave,nueva_edad))
print(diccionario)