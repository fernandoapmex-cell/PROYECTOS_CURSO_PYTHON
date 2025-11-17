#comparacion del operador == o el operador is en POO

#el operador == compara el contenido de 2 objetos (contenido igual)
#no es necesario que sea el mismo objeto

#operador is revisa si dos objetos son identicos(
#ambos deben apuntar a la misma direccion de memoria para ser iguales

#ejemplo de una lista

lista_a=[1,2,3]
lista_b=lista_a

#en este caso ambas tienen el mismo contenido y apuntan a la misma referencia
print(f'Lista a y b tienen el mismo contenido :{lista_a == lista_b}')
print(f'Lista a y b apuntan al mismo objeto: {lista_a is lista_b}')

#sin embargo si creamos un nuevo objeto
lista_c = list(lista_a)
#en este caso la lista a tiene el mismo contenido que c pero es un diferente objeto
print(f'Lista a y c tienen el mismo contenido :{lista_a == lista_c}')
print(f'Lista a y c apuntan al mismo objeto: {lista_a is lista_c}')