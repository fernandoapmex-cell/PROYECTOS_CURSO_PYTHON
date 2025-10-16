#Mas de funciones anidadas y alcance de variables

def funncion_externa():
    variable_local_externa='variable local externa'
    def funcion_anidada():
        variable_local_anidada='variable local anidada'
        #el nonlocal es para trabajar con variables de clases externas dentro de las anidadas
        nonlocal variable_local_externa
        variable_local_externa=' nuevo valor variable local externa'
    funcion_anidada()
    #no es posible ingresar a una variable local mas interna
    #variable_local_anidada
    print(f'Valor variable local externa:{variable_local_externa}')
funncion_externa()