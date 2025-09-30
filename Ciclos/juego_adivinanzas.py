from random import randint
print('****Juego de adivinanzas***')
numero_secreto=randint(1,50)
intentos = 0
adivinanza = None
INTENTOS_MAXIMOS=5
while adivinanza != numero_secreto and intentos < INTENTOS_MAXIMOS:
    adivinanza = int(input('Ingresa un numero entre 1 y 50: '))
    #agregamos una ayuda para orientar al jugador
    if adivinanza < numero_secreto:
        print('El numero secreto es mayor')
    elif adivinanza > numero_secreto:
        print('El numero secreto es menor')
    intentos = intentos + 1
else:
    if adivinanza == numero_secreto:
        print(f'Felicidades encontraste el numero secreto: {numero_secreto} en {intentos} intentos')
    else:
        print(f'Perdiste, no pudiste encontrar el numero secreto en {INTENTOS_MAXIMOS} intentos')