#definimos una variable global
contador = 0

def mostrar_contador():
    print('El contador es: ',contador)
def modificar_contador(c):
    #primero se declara siempre
    global contador
    contador = c
modificar_contador(5)
mostrar_contador()