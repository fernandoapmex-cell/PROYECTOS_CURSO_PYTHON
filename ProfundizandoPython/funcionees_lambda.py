#funcion lambda son funciones anonimas y pequeñas una linea de codigo
def sumar(a,b):
    return a+b

#no es posible asignar una funcion a una variable de forma directa
#mifuncion = def restar(a,b):return a-b
#con una funcion lambda (anonima sin nombre) y una sola linea de codigo
#no se necesita agregar parentesis para los parametros
#no se necesita usar return pero si regresar una expresion valida
mi_funcion_lambda=lambda a,b:a+b
resultado=mi_funcion_lambda(3,4)
print(f'Resultado sumarcon funcion lambda {resultado}')

#funcion lambda que no recibe argumentos
mi_funcion_lambda=lambda:'Funcion sin argumentos'
print(f'llamar funcion lambda sin argumentos : {mi_funcion_lambda()}')
#funcion lambda con parametros por default
mi_funcion_lambda=lambda a=2,b=3:a+b
resultado=mi_funcion_lambda()
print(f'Resultados de argumentos por default:{resultado}')
#FUncion lambda con argumentos variables utulizando *args keargs
mi_funcion_lambda=lambda *args,**kwargs:len(args)+len(kwargs)
print(f'Resultado de arguemntos variables:{mi_funcion_lambda(1,2,3,a=1,b=2,c=3)}')
#funciones lambda con argumentos,argumentos variables y valores por default
mi_funcion_lambda=lambda a,b,c=3,*args,**kwargs:a+b+c+len(args)+len(kwargs)

print(f'Resultado de la funcion lambda:{mi_funcion_lambda(1,2,4,5,6,7,d=1,e=2,f=3)}')