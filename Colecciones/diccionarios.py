print('Diccionarios en python')

#creamos un diccionario con clave y valor

persona={
    'nombre':'Sergio',
    'Apellido':'Ramirez',
    'Edad':22,
    'Ciudad':'CDMX'
}
print('Diccionario de persona',persona)

#accder a los elementos del diccionario


print(f'Nombre:{persona["nombre"]}')
print(f'Apellido:{persona.get("Apellido")}')
print(f'Ciudad:{persona.get("Ciudad")}')

#Modificar un valor en el doccionario
persona['Edad']=35
print(f'Diccionario de persona',persona)
#agregar un nuevo elemento
persona['Profesion']='Ingeniero'
print(f'Diccionario de persona',persona)
#eliminar un elemento del diccionario
del persona['Ciudad']
print(f'Diccionario de persona',persona)
#eliminar con pop
persona.pop('Profesion')
print(f'Diccionario de persona',persona)

#iterar los elementos de un diccionario (llave,valor) va a ser una tupla
print('\n')
for llave,valor in persona.items():
    print(f'Llave:{llave}')
    print(f'Valor:{valor}')
print('\n')

#obtener solo los valores
for valor in persona.values():
    print(f'valor:{valor}')
print('\n')
#obtener solo las llaves
for llave in persona.keys():
    print(f'llave:{llave}')