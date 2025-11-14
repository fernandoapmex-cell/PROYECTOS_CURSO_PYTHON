def imprimir_vector(x,y,z):
    print(f'<{x},{y},{z}>')

imprimir_vector(10,3,12)
#desempaquetar tuplas
tupla_vector = (10,3,12)
imprimir_vector(*tupla_vector)

lista_vector = [10,3,12]
imprimir_vector(*lista_vector)
#desempaquetar un generador

expresion_generador = (x*x for x in range(3))
imprimir_vector(*expresion_generador)
#desempaquetar un diccionario
diccionario_vector={'x':1,'y':2,'z':3}
imprimir_vector(**diccionario_vector)
#pasar llaves
imprimir_vector(*diccionario_vector)