print('***MANEJO DE SETS****')
#crear un conjunto el ultimo 4 se borra
mi_set={1,2,3,4,5,4}
print(mi_set)
#agregar elementos al set
mi_set.add(6)
print(mi_set)
mi_set.add(7)
print(mi_set)
mi_set.add(1)
print(mi_set)
#Eliminar un elemento del conjunto
mi_set.remove(4)
print(mi_set)
#iterar los elementos del set
for elemento in mi_set:
    print(elemento,end=' ')
#comprobar si existe un elemento en el set
print(f'\n{4 in mi_set}')

#obtener la longitud del set

print(len(mi_set))