# manejo de cadenas
cadena='Hola, mundo!'
#Obtenemos la sub cadena de hola [inicio:fin (sin incluirlo)]
subcadena_hola = cadena[6:12]
print(f'subcadena : {subcadena_hola}')

cadena2='Hola Mundo'
nueva_cadena = cadena2.replace('Mundo','a todos')
print(nueva_cadena)

#sustituir hola por adios
nueva_cadena=cadena2.replace('Hola','Adios')
print(nueva_cadena)