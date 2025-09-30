print('***Operadores de asignacion***')
numero= 5
print(f'valor de numero{numero}')
numero= 10
print(f'valor de numero{numero}')
cadena = 'Saludos desde python'
print(f'{cadena}')
#asignacion multiple
x,y,z = 1,'hola ',3
print(f'{x},{y},{z}')
#asignacion en cadena
a=b=c=d=f= 9
print(f'{a},{b},{c},{d},{f}')

#asignacion multiple / intercambio de valores de una variable sin utilizar variables temporales

x,y=5,10
#aplicando el concepto de asignacion multiple intercambiamos los valores de las variables
x,y=y,x
print(f'{x},{y}')

#recibir multiples valores de la entrada del usuario

nombre,apellido=input('ingresa nombre y apellido separados por una coma').split(',')
print(f'tu nombre es {nombre.strip()} y tu apellido es {apellido.strip()}')

