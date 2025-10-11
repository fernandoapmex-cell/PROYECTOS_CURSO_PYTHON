from zona_fit.cliente import Cliente
from zona_fit.cliente_dao import ClienteDAO

print('*** Clientes de Zona fit (GYM) ***')
opcion = None
while opcion != 5:
    print('''Menu:
    1.-Listar clientes
    2.-Agregar cliente
    3.-Editar cliente
    4.-Eliminar cliente
    5.-Salir
    
    ''')
    opcion = int(input('Escribe tu opcion: '))
    if opcion == 1:
        print('-----Lista de clientes-------\n')
        clientes=ClienteDAO.seleccionar()
        for cliente in clientes:
            print(cliente)
        print()
    elif opcion == 2:
        print('-----Agregar cliente-----\n')
        nombre_var=input('Nombre del cliente: ')
        apellido_var=input('Apellido del cliente: ')
        membresia_var=int(input('Membresia del cliente(numero): '))
        cliente=Cliente(nombre_cliente=nombre_var,apellido_cliente=apellido_var,membresia_cliente=membresia_var)
        clientes_insertados=ClienteDAO.insertar(cliente)
        print(f'\nSe han insertado {clientes_insertados} clientes de manera exitosa')
        print()
    elif opcion == 3:
        print('-----Editar cliente-----\n')
        id_cliente_var=int(input('Id del cliente: '))
        nombre_var=input('Nombre del cliente: ')
        apellido_var=input('Apellido del cliente: ')
        membresia_var=int(input('Membresia del cliente(numero): '))
        cliente=Cliente(id_cliente_var,nombre_var,apellido_var,membresia_var)
        clientes_actualizados=ClienteDAO.actualizar(cliente)
        print(f'\nSe han actualizado {clientes_actualizados} clientes de manera exitosa')
        print()
    elif opcion == 4:
        print('-----Eliminar cliente-----\n')
        id_cliente_var=int(input('Id del cliente: '))
        cliente=Cliente(id_cliente=id_cliente_var)
        clientes_eliminados=ClienteDAO.eliminar(cliente)
        print(f'\nSe han eliminado {clientes_eliminados} clientes de manera exitosa')
        print()
else:
    print('*** Saliendo de la aplicacion ***')
