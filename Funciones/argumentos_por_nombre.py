print('Funcion con argumentos por nombre')

def imprimir_persona(nombre:str,apellido:str='',edad:int=0):
    print(f'Persona: nombre= {nombre}, apellido= {apellido}, edad= {edad}')

#primero llamamos la funcion pasando los argumentos de manera posicional
imprimir_persona('ricardo','quitana',24)
#llamar la funcion usando arguementos por nombre
imprimir_persona(nombre='carlos',apellido='rojas',edad=28)
#llamar la funcion usando argumentos por nombre pero cambiando el orden
imprimir_persona(edad=28,apellido='rojas',nombre='carlos')
#argumentos con valores por default
imprimir_persona('Carlos')