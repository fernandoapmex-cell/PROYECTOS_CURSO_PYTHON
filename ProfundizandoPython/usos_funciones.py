#las funciones en python son ciudadanas de primera clase
#First class citizens
#definimos una funcion
def sumar(a,b):
    return a+b

#primer uso asignar funcion a una variable no se usan parentesis
mi_funcion=sumar

#verificar el tipo de la variable
print(type(mi_funcion))

#llamamos la funcion atraves de la variable

# resultado=mi_funcion(10,20)
# print(resultado)

#funcion como argumento

def operacion(a,b,sumar_arg):
    print('Resultado de sumar:',sumar_arg(a,b))

operacion(1,2,sumar)

def retornar_funcion():
    #retornamos una funcion
    return sumar

funcion_retornada=retornar_funcion()
print(type(funcion_retornada))
print(f'resultado funcion retoranada',funcion_retornada(4,5))