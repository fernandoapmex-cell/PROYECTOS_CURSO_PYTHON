print(f'*** Calculadora con funciones ***')

def mostrar_menu():
    print('\n\t--- Menu de operaciones matematicas ---')
    print(f'''
    1.-Suma
    2.-Resta
    3.-Multiplicacion
    4.-Division
    5.-Salir
    ''')
    return int(input('Escoge una opción: '))

#programa principal
def pedir_valores():
    operando1 = float(input('Dame el valor 1: '))
    operando2 = float(input('Dame el valor 2: '))
    return operando1, operando2

def ejecutar_operacion(opcion:int, salir:bool):
    #solicitar los valores de los operandos
    if 1 <= opcion <= 4:
        operando1,operando2 = pedir_valores()
    reultado = 0
    if opcion == 1:
        reultado = operando1 + operando2
        print(f'El resultado de la suma es: {reultado}')
    elif opcion == 2:
        reultado = operando1 - operando2
        print(f'El resultado de la resta es: {reultado}')
    elif opcion == 3:
        reultado = operando1 * operando2
        print(f'El resultado de la multiplicacion es: {reultado}')
    elif opcion == 4:
        reultado = operando1 / operando2
        print(f'El resultado de la division es: {reultado}')
    elif opcion == 5:
        print(f'Saliendo del programa...')
        salir = True
        return salir
    else:
        print('Opcion no valida,Ingresa otra opcion')


if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)

