#profundizando en tuplas

#declarar variables

a,b='hola','adios'

print(a,b)
#swap (intercambio de variables)

a,b=b,a

print(a,b)

#regresar multiples valores en una funcion

def minmax(elementos):
    return min(elementos),max(elementos)

min,max=minmax([1,2,3,4,5])
print('valor minimo:',min,'Valor maximo:',max)

#regresar la suma de una tupla

resultado=sum((1,2,3,4,5))
print(resultado)
#args es para pasar una tupla *kwargs para pasar diccionarios a funciones
def sumar(*args):
    return sum(args)

resultado=sumar(1,2,3,4,5)
print(resultado)