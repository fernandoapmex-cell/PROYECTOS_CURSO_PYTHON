print('***Revisar si un numero es negativo o positivo***')

numero=int(input('Ingresa un numero : '))

if numero < 0:
    print('Eres un numero negativo')
elif numero > 0 :
    print('Eres un numero positivo')
else:
    print(f'Eres un numero neutro el numero {numero}')