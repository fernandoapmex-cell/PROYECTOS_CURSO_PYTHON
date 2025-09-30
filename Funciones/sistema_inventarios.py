print('Sistema de inventarios con funciones')

#inventario de nuestro almacen

inventario = [
    {'Id' : 1, 'Nombre' : 'Camisa','Precio':25.99,'Cantidad':50},
    {'Id' : 2, 'Nombre' : 'Pantalon','Precio':39.99,'Cantidad':30},
    {'Id' : 3, 'Nombre' : 'Zapatos','Precio':45.99,'Cantidad':20}
]
#funcion para mostrar el inventario

def mostrar_inventario(inventario:list):
    print('Inventario del alamacen')
    for producto in inventario:
        print(f'Id: {producto.get("Id")},Nombre: {producto.get('Nombre')}'
              f'Precio: ${producto.get("Precio")},Cantidad: {producto.get("Cantidad")}')

#llamar en el progrmaa principal
def agregar_producto():
    print('----- Agregar nuevo producto ----------')
    id= int(input('Id del producto: '))
    nombre= input('Nombre del producto: ')
    precio= float(input('Precio del producto: '))
    cantidad= int(input('Cantidad del producto: '))
    nuevo_producto = {'Id' : id , 'Nombre':nombre, 'Precio':precio, 'Cantidad':cantidad}
    inventario.append(nuevo_producto)
    print('Producto agregado al inventario')
def buscar_producto_id():
    pass

def buscar_producto_id():
    print('---Buscar producto por id---')
    id_buscar = int(input('ingresa el id Id del producto a buscar: '))
    for producto in inventario:
        if producto.get('Id') == id_buscar:
            print('\n informacion del producto encontrado')
            print(f'Id: {producto.get('Id')}.'
                  f'Nombre: {producto.get("Nombre")},'
                  f'Precio: ${producto.get("Precio")},'
                  f'Cantidad: {producto.get("Cantidad")}')
            return
    print('\n Producto no encontrado')


if __name__ == '__main__':
    while True:
        print('''
            1. Mostrar Inventario
            2. Agregar nuevo producto
            3. Buscar productor por Id
            4. Salir 
        ''')
        opcion = input('Ingrese una opcion del (1 - 4): ')
        #revisamos las opciones del menu
        if opcion == '1':
            mostrar_inventario(inventario)
        elif opcion == '2': #agregar nuevo producto
            agregar_producto()
        elif opcion == '3':
            buscar_producto_id()
        elif opcion == '4':
            print('Hasta luego')
            break
        else:
            print('Opcion no valida')
