print('***sistema generador de id unico***')
nombre = input('Cual es tu nombre: ')
apellido= input('Cual es tu apellido: ')
anio_nacimiento=input('Cual es tu año de nacimiento(YYYY): ')

#normalizar valores
nombre_2=nombre.strip().upper()[0:2]
apellido_2=apellido.strip().upper()[0:2]
anio_nacimiento_2=anio_nacimiento.strip()[2:]# se pone solo dos puntos para que use hasta el fial de la cadena

from random import randint

numero_aleatorio = randint(1000,9999)
#generamos el valor de ID unico

id_unico=f'{nombre_2}{apellido_2}{anio_nacimiento_2}{numero_aleatorio}'
print(f'Hola {nombre},\n Tu nuevo numero de identificacion generado por el sistema es:\n{id_unico}\n Felicidades!)')