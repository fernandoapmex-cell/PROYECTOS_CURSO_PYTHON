print('Aplicacion de Cajero Automatico')
saldo = 1000
salir = False

while not salir :
    print(f'''Operaciones que puedes realizar: 
    1.Consultar Saldo
    2.Retirar
    3.Depositar dinero a cuenta
    4.Salir
    ''')
    opcion=int(input('Ingresa una opcion: '))
    if opcion == 1:
        print(f'Saldo actual:${saldo:.2f} \n')
    elif opcion == 2:
        retiro = float(input('Ingresa la cantidad a retirar: '))
        if(retiro <= saldo):
            saldo = saldo - retiro
            print(f'Saldo retirado:${retiro:.2f} \n')
            print(f'Saldo actual:${saldo:.2f} \n')
        else:
            print(f'No cuentas con el Saldo a retirar, tu saldo actual es : ${saldo:.2f} \n')
    elif opcion == 3:
        deposito = float(input('Ingresa la cantidad a depositar: '))
        saldo = saldo + deposito
        print(f'Saldo nuevo:${saldo:.2f} \n')
    elif opcion == 4:
        print('Saliendo del cajero automatico,Hasta luego')
        salir = True
else:
    print('Termino el programa')