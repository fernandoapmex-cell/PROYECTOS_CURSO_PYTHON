print('Sistema de inventarios')
inventario = []

numero_productos=int(input('Cuantos productos deseas agregar al inventario: '))
for indice in range(numero_productos):
    print(f'proporciona los valores del producto: {indice+1}')
    nombre=input('Ingrese el nombre del producto: ')
    precio=float(input('Ingrese el precio del producto: '))
    cantidad=int(input('Ingrese la cantidad del producto: '))
    #creamos el diccionario con el detalle del producto
    producto={
        'id': indice+1,
        'nombre':nombre,
        'precio':precio,
        'cantidad':cantidad
    }
    #agregamos el nuevo producto al inventario
    inventario.append(producto)
#mostrar el inventario inicial
print(inventario)

#Mostrar el inventario detallado

for producto in inventario:
    print(f'''
        id : {producto.get('id')}
        nombre:{producto.get('nombre')}
        precio:{producto.get('precio')}
        cantidad:{producto.get('cantidad')}
    ''')
#buscar un producto por id

id_buscar=int(input('Ingrese el id del producto: '))
producto_encontrado=None
for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado=producto
        break
if producto_encontrado is not None:
    print('Informacion Del Producto Encontrado')
    print(f'''
        id : {producto_encontrado.get('id')}
        nombre:{producto_encontrado.get('nombre')}
        precio:{producto_encontrado.get('precio')}
        cantidad:{producto_encontrado.get('cantidad')}
    ''')
else:
    print(f'Producto con id: {id_buscar} no encontrado')

