#Clonacion o copia de objetos
#copia superficial o shadow o copia poco profunda
import copy

lista_a=[[1,2],[3,4],[5,6]]
#copia superficial o shadow
lista_b=list(lista_a)
#las listas son 2 objetos distintos ,apuntan a diferente posicion en memoria
#pero los niveles internos solo copio la referencia no se creo nuevos objetos para las sublistas
print(f'Lista a:{lista_a}')
print(f'Lista b:{lista_b}')
#comprobacion que los objetos son distintos (a nivel superior)
#un cambio en el nivel superior,no afecta a la otra lista
lista_a.append([7,8])
#son distintos objetos a nivel superior
print(f'Lista a:{lista_a}')
print(f'Lista b:{lista_b}')
#comprobacion de que los objetos internos tienen la misma referencia del objeto
#un cambio en un elemento de una sublista afecta a el del otro objeto
lista_a[0][1]='A'
print(f'Lista a:{lista_a}')
print(f'Lista b:{lista_b}')
#crear copias profundas (import copy)
lista_c=[[3,4],[5,6],[7,8]]
lista_d=copy.deepcopy(lista_c)
#comprobacion de que son objetos distintos
lista_c.append([9,10])
print(f'Son distintos objetos a nivel superior')
print(f'Lista a:{lista_c}')
print(f'Lista b:{lista_d}')
#ahora si hacemos la comprobacion mas importante (elementos internos) son nuevos objetos,no solo copio la referencia
lista_c[0][1]='A'
print(f'Lista a:{lista_c}')
print(f'Lista b:{lista_d}')
#el metodo copy sirve para realizar copias poco profundas (recomendado que no sean colecciones)