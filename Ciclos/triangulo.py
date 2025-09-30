print('*** TRIANGULO ***')
numero_filas=int(input('ingresa el numero de filas: '))

#iterar sobre cada fila del triangulo

for fila in range (1,numero_filas+1,1):
    espacios_blanco=' ' * (numero_filas-fila)
    cantidad_asteriscos= '*' * (2*fila-1)
    print(espacios_blanco,cantidad_asteriscos)

