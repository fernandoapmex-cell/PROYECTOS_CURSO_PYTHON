#Valores Aleatorios con la funcion randint

#import random

from random import randint

#generar un numero aleatorio entre 1 y 10

numero_aleatorio = randint(1,10)
print(f'Numero aleatorio: {numero_aleatorio}')

#siumlar un dado

dado=randint(1,6)
print(f'resultado de lanzar el dado: {dado}')