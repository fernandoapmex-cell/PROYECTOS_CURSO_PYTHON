print('***Desempaquetado de tuplas ***') #unpacking

producto=('P001','Camisa',20.00)

#desempaquetado de tuplas
id,descripcion,precio = producto

#imprimir los valores
print(f'Tupla completa:{producto}')

#valores indepndientes ya desempaquetados

print(f'Producto:id = {id} ,Descripcion: {descripcion} ,Precio: {precio}')