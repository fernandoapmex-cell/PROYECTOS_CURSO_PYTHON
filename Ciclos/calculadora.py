print('***  Calculadora ***')

operando1=operando2=resultado=0
salir = False

while not salir:
    print(f'''
    Operaciones que puedes realizar:
    1.-Suma
    2.-Resta
    3.-Multiplicacion
    4.-Division
    5.-Salir
    ''')
    opcion=int(input('Escoje una opcion: ').strip())
    if 1<= opcion <=4:
        operando1 = float(input('Ingresa el valor del operando 1 : ').strip())
        operando2 = float(input('Ingresa el valor del operando 2 : ').strip())
    if opcion == 1:
        resultado=operando1+operando2
        print(f'El resultado de la suma es : {resultado:.2f}\n')
    elif opcion == 2:
        resultado=operando1-operando2
        print(f'El resultado de la resta es : {resultado:.2f}\n')
    elif opcion == 3:
        resultado=operando1*operando2
        print(f'El resultado de la multiplicacion es : {resultado:.2f}\n')
    elif opcion == 4:
        resultado=operando1/operando2
        print(f'El resultado de la division es : {resultado:.2f}\n')
    elif opcion == 5:
        print('Saliendo del programa')
        salir = True
    else:
        print('Opcion no valida')