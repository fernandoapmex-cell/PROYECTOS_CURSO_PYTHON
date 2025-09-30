print('Obtener coordenadas x y z')

def obtener_coordenadas(x,y,z):
    x,y,z=10,20,30
    return x,y,z

#llamar a la funcion

resultado=obtener_coordenadas(10,20,30)
print(resultado)
#unpaking de la tupla
x1,y1,z1=resultado
print(f'coordenada x = {x1},y={y1},z={z1}')