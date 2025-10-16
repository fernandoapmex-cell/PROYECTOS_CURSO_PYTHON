#decoradores
#un decorador es una funcion que recibe a su vez una funcion y regresa otra
#lo utilizamos para extender funcionabilidad
#1.-Funcion decorar
#2.- Funcion a decorar(b)
#3,.Funcion decorada (c)
from funcionees_lambda import resultado


def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        print('Antes de ejecutar la funcion')
        resultado=funcion_a_decorar_b(*args, **kwargs)
        print('Despues de ejecutar la funcion')
        return resultado
    return funcion_decorada_c

@funcion_decorador_a
def mostrar_mensaje():
    print('Hola desde funcion mostrar mensaje')

mostrar_mensaje()
@funcion_decorador_a
def imprimir():
    print('Hola desde funcion imprimir')

imprimir()
@funcion_decorador_a
def sumar(a,b):
    return a+b

resultado = sumar(5,6)
print(f'Resultado de la funcion sumar: {resultado}')