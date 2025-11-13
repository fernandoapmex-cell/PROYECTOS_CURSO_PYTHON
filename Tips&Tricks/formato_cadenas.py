#Distintas formas de dar formato a cadenas en py
#1.- Estilo antiguo
nombre ='Juan'
mi_cadena ='Hola,%s'%nombre
print(mi_cadena)
#Podemos convertir enteros a hexadecimales
error=500
#convertimos a hexa
cadena_hexadecimal = 'Error en hexadecimal:%x'%error
print(cadena_hexadecimal)

# si queremos pasar varios valores tenemos que usar una tupla
cadena = 'Hola %s hay un error: %x'%(nombre,error)
print(cadena)
#podemos referenciar por sustitucion de variables usando un diccionario
cadena = 'Hola %(nombre)s hay un error: %(error)x, usamos otra vez nombre : %(nombre)s'%{'nombre':nombre,'error':error}
print(cadena)
