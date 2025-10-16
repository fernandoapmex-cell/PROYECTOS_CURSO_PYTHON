#un closure es una funcion que define a otra y ademas la puede regresar
#la funcion anidada puede acceder a las varaibles locales o externas

#funcion principal o externa

def operacion(a,b):
    #definimos una funcion interna o anidada
    def sumar():
        return a+b
    #return sumar
    return sumar()
mi_funcion_closure=operacion(5,4)
print(f'Resultado de la funcion closure: ',mi_funcion_closure)
#llamar la funcion regresada al vuelo
print(f'Resultado de la funcion closure pero ejecutada al vuelo: {operacion(2,3)}')

#funcion principal
def operacion2(a,b):
    #definimos y regresamos con lambda
    return lambda:a+b
mi_funcion_closure=operacion2(5,3030)
print(f'Resultado de la funcion closure: ',mi_funcion_closure())
