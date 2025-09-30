#funcion sumar que acepta argumentos variables

def sumar(*args):
    total = 0
    for numero  in args:
        total = total + numero
    return total

# llamamos a la funcion sumar

resultado = sumar(1,2,3,4,5)
print(f'Resultado de la suma de los primeros 5 numeros:',resultado)