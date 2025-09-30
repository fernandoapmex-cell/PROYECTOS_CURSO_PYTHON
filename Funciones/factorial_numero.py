print('Factorial de n numero')

#definimos la funcion factorial recursiva

def factorial_recursiva(numero):
    #caso base,factorial 0!= 1 ,1! = 1
    if numero == 0 or numero == 1:
        print(f'resultado factorial parcial al momento {numero} es 1')
        return 1
    else: #caso recursivo
        factorial_parcial = numero*factorial_recursiva(numero-1)
        print(f'Resultado del factorial al momento {numero} es {factorial_parcial}')
        return factorial_parcial
#llamo la funcion
numero = 10
resultado = factorial_recursiva(numero)
print(f'El factorial de {numero} es {resultado}')


