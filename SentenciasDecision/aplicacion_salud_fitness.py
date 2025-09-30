print('Aplicacion Salud Fitness')

# CONSTANTES

META_PASOS_DIARIO= 10000
CALORIAS_POR_PASO=0.04 # SON KILOCALORIAS

#PEDIMOS LOS VALORES AL USUARIO

nombre_usuario=input('Ingrese su nombre: ')
pasos_diarios=int(input('Ingrese la cantidad de pasos caminados hoy: '))

#verificar si el usuario alcanzo la meta de pasos diarios

meta_alcanzada=pasos_diarios >= META_PASOS_DIARIO
meta_alcanzada_txt='Si'if meta_alcanzada else 'No'

#calculamos las calorias quemadas

calorias_quemadas=pasos_diarios*CALORIAS_POR_PASO

#Mostramos La Informacion

print(f''''
Nombre del usuario: {nombre_usuario}
Cantidad de pasos hoy: {pasos_diarios}
Calorias quemadas: {calorias_quemadas} kcal
Meta de pasos diarios alcanzada: {meta_alcanzada_txt}
''')
