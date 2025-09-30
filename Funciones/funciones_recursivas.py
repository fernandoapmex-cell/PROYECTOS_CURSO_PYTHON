print(' imprimir del 1 al 5 Funciones recursivas')

#definir la funcion recursiva

def funcion_recursiva(numero):
    #caso base
    if numero == 1:
        print(numero,end=' ')# 1 2 3 4 5
    else:
        funcion_recursiva(numero - 1)
        print(numero,end=' ')

#llamar a la funcion
funcion_recursiva(5)

