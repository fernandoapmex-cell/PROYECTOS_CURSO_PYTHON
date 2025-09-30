print('Lista de suscriptores ***')
#definimos set inicial

suscriptores={}
suscriptores=set()  #asi se inicializa un set
print('lista de suscriptores inicial',suscriptores)

numero_suscriptores=int(input('Proporciona el numero de suscriptores inciiales: '))

for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor(Correo electronico): )'))
# Verificar si un nuevo suscriptor ya esta en la lista
nuevo_suscriptor=input('Proporciona el nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'el suscritor ya se encuentra en la lista: {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'el suscriptor se ah agregado a la lista : {suscriptores}')

#eliminar un suscriptor existente

suscriptor_a_eliminar=print(input('ingresa el suscriptor a eliminar : '))
suscriptores.remove(suscriptor_a_eliminar)
print(f'el suscritor{suscriptor_a_eliminar} se ha eliminado de la lista : {suscriptores}')

#verificamos la cantidad de suscriptores

print(f'Cantidad total de suscriptores: {len(suscriptores)}')

#mostramos suscriptores

print('Lista de suscriptores')
for suscriptor in suscriptores:
    print(suscriptor)