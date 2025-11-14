#los decoradores permiten extender y modificar el comportamiento de las funciones
#un decorador es codigo reutilizable
#ejemplo 1
def decorador_envolvente(funcion_para_decorar):
    #recibir funcion y regresarla
    print('Estamos dentro de la funcion decoradora')
    return funcion_para_decorar

#usar decorador
def saludar():
    return 'Saludos desde mi funcion...'

#LLmamar manualmente el decorador (no es lo comun)
funcion_retornada = decorador_envolvente(saludar)
print(funcion_retornada)

#de forma comun

@decorador_envolvente
def saludar_funcion_para_decorar():
    return 'Saludos desde mi funcion...'

print(saludar_funcion_para_decorar())

#decorador que convierte el texto a mayusculas
def mayusculas(funcion_para_decorar):
    def envolvente():
        #mandamos a llamar la funcion original(closure)
        print('Antes de la llamada a la funcion a decorar')
        resultado_original=funcion_para_decorar()
        print('Despues de la llamada a la funcion a decorar')
        resultado_modificado=resultado_original.upper()
        return resultado_modificado
    return envolvente

@mayusculas
def saludar_minusculas():
    return 'Saludos desde mi funcion en minusculas...'

print(saludar_minusculas())

#Decoradores multiples y el orden que se aplican
#<strong><em>Hola</em></strong>
def negritas(funcion):
    def funcion_envolvente():
        return '<strong>' + funcion() + '</strong>'
    return funcion_envolvente
def enfatizar(funcion):
    def funcion_envolvente():
        return '<em>' + funcion() + '</em>'
    return funcion_envolvente

@negritas
@enfatizar
def saludar_html():
    return 'Hola con HTML'

print(saludar_html())

#Decoradores con argumentos
#*args  y **kwargs
def decorador_con_argumentos(funcion):
    def funcion_envolvente(*args, **kwargs):
        #progragamos los parametros a la funcion original
        print('Se esta ejecutando decorador con argumentos')
        print('args:',args)
        print('kwargs:',kwargs)
        #modificar los argumentos antes de enviarlos
        lista_arg=[]
        for indice,valor_tupla in enumerate(args):
            lista_arg.append(args[indice].upper())
        #return funcion(*args, **kwargs)
        #agregamos mas elementos a la lista
        lista_arg.append('nuevo arg 1')
        lista_arg.append('nuevo arg 2')
        #agregamos info al diccionario
        kwargs['valor 1'] = 1
        kwargs['valor 2'] = 2
        kwargs['valor 3'] = 3
        #propagar los valores modificados
        return funcion(*lista_arg,**kwargs)
    return funcion_envolvente
@decorador_con_argumentos
def funcion_saludar(titulo,nombre,*args, **kwargs):
    #imprimir el titulo con el nombre
    print(f'{titulo}. {nombre}')
    print(args)
    print(kwargs)
funcion_saludar('Ingeniera','Maria Quiroz')