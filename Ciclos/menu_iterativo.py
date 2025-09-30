print('***Sistema de administracion de cuentas ***')

salir=False

while not salir :
 print(f'''
      Menu:
    1- Crear Cuenta
    2- Eliminar Cuenta
    3- Salir
    ''')
 opcion=int(input('Ingrese una opcion: '))
 if opcion == 1:
     print('Creando Cuenta....')
 elif opcion == 2:
     print('Eliminando Cuenta....')
 elif opcion == 3:
     salir=True
     print('Saliando Cuenta....')
 else:
     print('Opcion no valida, proporciona otra opcion')
else:
    print('Terminando el programa')