#funciones anidadas

def calculadora(a,b,operacio='sumar'):
    #funcion anidada
    def sumar(a,b):
        return a+b
    #llamada a la funcion anidada
    def restar(a,b):
        return a-b
    if operacio=='sumar':
        print('Resultado sumar:',sumar(a,b))
    elif operacio=='restar':
        print('Resultado restar:',restar(a,b))
calculadora(4,5,'restar')