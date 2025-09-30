print('Alcance de variables')

contador_global = 0

def incrementar_contador():
    #declaramos variable local
    contador_local= 0
    #usar una variable global
    global contador_global
    contador_global+=1
    contador_local+=1
    #imprimos ambos contadores
    print(f'contador local: {contador_local}')
    print(f'contador global: {contador_global}')


#llamos la funcion varias veces

incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()

#termianndo el programa

print(contador_global)
