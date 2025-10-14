# #profundizando en tipo str
#
# #concatenaciona automatica en py
# variable='Adios'
# print('camion''coche' + variable)
# help(str)
# #pasar un metodo en concreto
# help(str.strip)
#from Cadenas.formatero_de_cadenas import mensaje

# from mi_clase import MiClase
#
# help(MiClase)
#
# # para ver el docstring de la clase
# print(MiClase.__doc__)
# print(MiClase.__init__.__doc__)
# print(MiClase.mi_metodo.__doc__)
# print(MiClase.mi_metodo)
# print(type(MiClase.mi_metodo))

#las cadenas son inmutables en py

#help(str.capitalize)

# mensaje1 = 'hola mundo'
# mensaje2 = mensaje1.capitalize()
#mensaje 2 con la primera en mayuscula
#el id es la direccion de memoria donde esta el objeto
# print(mensaje2,f': id -> {id(mensaje2)}')


# #metodo join
# #agrega cierto valor entre una tupla de valores en este caso un espacio
# tupla_cadenas = ('Hola','Mundo','Universidad','Python')
# mensaje = ' '.join(tupla_cadenas)
# print(mensaje)
# #tambien sirve con listas y cadenas
# lista_cursos=['Java','Python','C++','Java']
# mensaje=','.join(lista_cursos)
# print(mensaje)
# #string
# mensaje='.'.join('HolaMundo')
# print(mensaje)
# #diccionario
# diccionario={'nombre':'Juan','apellido':'Chavez','edad':'18'}
# llaves='-'.join(diccionario.keys())
# valores='-'.join(diccionario.values())
# print(f'llaves: {llaves},type(llaves): {type(llaves)}')
# print(f'valores: {valores},type(valores): {type(valores)}')


# metodo split
#para convertir una cadena en una lista
#cursos = 'Java Python Javascript Angular Spring Excel'
#convierte el string en cadena si no se especifica un parametro se toma espacio por default
# lista_cursos=cursos.split()
# print(lista_cursos)
# print(type(lista_cursos))

#parametros opcionales
#especificar separador
#cursos_separados_coma='Java,python,Javascript,Angular,Spring'
# lista_cursos_separados_coma=cursos_separados_coma.split(',')
# print(len(lista_cursos_separados_coma))

#max delimiter
#maximo de veces que se va aseparar la cadena
# lista_cursos = cursos_separados_coma.split(',',2)
# print(lista_cursos)

#dar formato a un str

# nombre = 'Juan'
# edad=28
# mensaje_con_formato='Mi nombre es %s y mi edad es %d'%(nombre,edad)
# print(mensaje_con_formato)
#
# persona=('Karla','Gomez',50000.000)
#el.2f espara especificar que es un valor flotante
# mensaje_con_formato='Hola %s %s.Tu sueldo es %.2f'
# print(mensaje_con_formato%persona)

#metodo format

# nombre='Juan'
# edad=28
# sueldo=3000.00
# mensaje_con_formato='Nombre{} Edad{} Sueldo{:.2f}'.format(nombre,edad,sueldo)
# print(mensaje_con_formato)
#
# mensaje='Sueldo {2:.5f} Nombre {0} edad {1} '.format(nombre,edad,sueldo)
# print(mensaje)
#parametros indexados
# mensaje='Nombre {n} Edad{e} Sueldo={s:.2f}'.format(n=nombre,e=edad,s=sueldo)
# print(mensaje)

# diccionario= {'Nombre':'Ivan','Edad':35,'Sueldo':800.00}
#aca usamos el diccionario de terminos y le asignamos la variable con el diccionario
# mensaje='Nombre {persona[Nombre]},Edad {persona[Edad]},Sueldo {persona[Sueldo]}'.format(persona=diccionario)
# print(mensaje)

#f-string
# mensaje=f'Nombre{nombre},Edad{edad},Sueldo{sueldo}'
# print(mensaje)
# print(nombre,edad,sueldo,sep=',')

#multiplicacion str

# resultado=3*'Hola'
# print(resultado)
#
# #multiplicacion de tuplas
#
# resultado=5*('Hola','Mundo')
# print(resultado)
#
# #multiplicacion de listas
#
# resultado=10*[0]
# print(resultado)
# print(type(resultado))
# print(len(resultado))

#caracteres de escape

# resultado = 'Hola \' Mundo'
# print(resultado)
# #borra el caracter detras
# resultado = 'Se va a eliminar el punto.\b\b\b'
# print(resultado)

#el caracter de diagonal es para escapar \
# resultado ='c:\\juan\\nuevo'
# print(resultado)

#raw string
#invalida los caracteres especiales
# resultado=r'Cadena con salto de linea \n \\\\ salto de linea'
# print(resultado)

#caracteres unicode

# print('Hola\u0020Mundo')
# print('\u0041')
# print('Notacion Extendida en unicode : \U00000041')
# print('Notcacion Hexadecimal','\x41')
# print('Corazon en unicode \u2665')
# print('Cara sonriendo \U0001F600')
# print('Serpiente \U0001F40D')

#ASCII

# caracter = chr(65)
# #A Mayuscula
# print(caracter)

#caracteres en bytes

# caracteres_bytes=b'Hola Mundo'
# print(caracteres_bytes)
#
# mensaje=b'Universidad Python'
# print(mensaje[0])
# print(chr(mensaje[0]))
#
# lista_caracteres = mensaje.split()
# print(lista_caracteres)

#convertir de str a bytes

cadena='Programacion con Python'
# print(f'String original: {cadena}')
# #asi se convierte una cadena a bytes
bytes= cadena.encode('utf-8')
# print(bytes)
string2= bytes.decode('utf8')
print(string2)
print(cadena == string2)