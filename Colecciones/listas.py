print('***Manejo de Listas***')

mi_lista=[1,2,3,4,5]

print(f'{mi_lista} -> Lista original')

#largo de lista

print(f'largo de la lista: {len(mi_lista)}')

#accder al valor de las listas

print(f'accedemos al valor 4 :{mi_lista[4]}')

#accder al ultimo valor de la lista

print(f'accedemos al valor 4 :{mi_lista[-1]}')

#modificar los elementos de una lista

mi_lista[1]=10

print(f'modificamos el valor del indice 1 de la lista :{mi_lista[1]}')

#agregar un nuevo elemento al final de la lista

mi_lista.append(6)
print(mi_lista,' ->se agrego el elemento 6')

#añadir un indice en una pocision especifica

mi_lista.insert(2,15)
print(mi_lista,' ->se agrego el elemento 15 en el indice 2')

#Eliminar elementos de una lista
#usando metodo remove para eliminar indice conforme a su valor no el indice
mi_lista.remove(5)
print(mi_lista,'-> se elimino el valor 5')

#removemos por indice utilizando el metodo pop

mi_lista.pop(1)#remueve el elemento del indice 1 de la lista

print(mi_lista,'-> se elimino el indice 1')

#eliminar usando del

del mi_lista[2]
print(mi_lista,'-> se elimino el indice 2')

#obtener sublistas de la lista original

sublista = mi_lista[1:3] # genera una sublista  del indice 1 al 2 ya que el 3 no se incluye

print(sublista,'-> sublista del indice 1 al 3 sin incluir el 3')