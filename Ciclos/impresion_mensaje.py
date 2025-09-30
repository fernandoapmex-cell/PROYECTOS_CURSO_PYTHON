print('****Repeticion Mensaje ***')

mensaje=input('ingresa el mensaje a repetir: ')
numero_repeticiones=int(input('ingresa el numero repeticiones: '))
for i in range(0,numero_repeticiones,1):
    print(f'numero de repeticion {i+1} .mensaje : {mensaje}')
