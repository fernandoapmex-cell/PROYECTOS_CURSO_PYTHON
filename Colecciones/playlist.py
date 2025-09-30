print('*** Playlist de canciones ***')

#creamos la lista vacia

lista_reproduccion=[]
numero_canciones = int(input('Cuantas canciones deseas agregar? '))

#iteramos cada elemento para agregar un elemento

for indice in range(numero_canciones):
    cancion = input(f'proporciona la cancion {indice + 1} :')
    lista_reproduccion.append(cancion)
#empezamos a agregar canciones

#lista_reproduccion.append('Hotel california - Eagles')
##lista_reproduccion.append('Staying Alive - Bee Gees')
#lista_reproduccion.append('Dream on - Aerosmith')

#ordennar la lista en orden alfabetico

lista_reproduccion.sort()

#mostrar lista de canciones

print(f'\n Lista de reproduccion en orden alfaberico : ')
print(lista_reproduccion)

#ordenar la lista en orden alfabetico alreves
lista_reproduccion.sort(reverse=True)
print(f'\n Lista de reproduccion en orden alfaberico : ')
print(lista_reproduccion)

#mostrar lista iterando sus elementos

for cancion in lista_reproduccion:
    print('-',cancion)