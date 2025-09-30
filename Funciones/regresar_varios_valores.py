print('Regresar una tupla de valores desde una funcion')

#Definicion de la funcion

def personas_mayusculas(nombre:str,apellido:str,edad:int):
    print(f'Esta funcion regresa varios valores(tupla)')
    return nombre.upper(),apellido.upper(),edad

#programa principal
nombre,apellido,edad=personas_mayusculas('carla','carlangas',23)
print(f'Resultados de persona en mayusculas = nombre: {nombre},apellido:{apellido},Edad: {edad}')