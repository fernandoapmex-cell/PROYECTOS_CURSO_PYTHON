print('***Valor Dentro del rango***')

MINIMO = 5
MAXIMO = 10

dato= int(input(f'proporciona un dato entre {MINIMO} Y {MAXIMO}: '))

esta_dentro_rango = dato >= MINIMO and dato <= MAXIMO
print(f'¿Tu dato esta dentro del rango?: {esta_dentro_rango}')