#scope o alcance de variables

variable_global='Variable global'

def imprimir():
    #para poder editar una variable global es necesario identificarla como una variable global y no una local
    global variable_global
    #accder a una variable gloabal
    print('Variable global accedida desde una funcion',variable_global)
    variable_global='Nuevo valor variable global'
    #variable local - solo funciona dentro de la funcion
    variable_local='Variable local desde una funcion'
    print(variable_local)
    def funcion_anidada():
        print('Variable local dentro de la funcion anidada',variable_local)
    funcion_anidada()


imprimir()
print(f'variable global fuera de la funcion',variable_global)
#no es posible usar variables locales fuera del bloque donde se definieron
#print(f'variable local fuera de la funcion',variable_local)