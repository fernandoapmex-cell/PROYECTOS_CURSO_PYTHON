#leer contenido online

from urllib.request import urlopen
palabras=[]
with urlopen('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
#     for linea in mensaje:
#         palabras_por_linea = linea.decode('utf-8').split()
#         for palabra in palabras_por_linea:
#             palabras.append(palabra)
# print(palabras)
# #contenido_mensaje = mensaje.read()
# #se decodigica para que en vez de bytes sea un string unicode
# contenido = mensaje.read().decode('utf-8')
# print(contenido)
#
# #usamos un with para guardar la informacion en un archivo
#
# with open('nuevo_archivo.txt','w',encoding='utf-8') as archivo:
#     archivo.write(contenido)
    contenido=mensaje.read().decode('utf-8')
    #contar ocurrencias de una cadena dentro de otra
    print('No.Veces que sale la palabra :',contenido.count('Universidad'))
#convierte a mayusculas un str
#print(contenido.upper())

#lower conviette a minusculas
#print(contenido.lower())

#python busca si esta la palbra en el contenido pero convertimos el contenido a minusculas o no lo encuentra
print('Existe pyhon?','python' in contenido.lower())

#startswith - inicia con
print(contenido.startswith('En GlobalMentoring.com.mx'))
#endswith - termina con
print(contenido.lower().endswith('globalmentoring.com.mx'))

#preguntar si cadena unicamente tiene caracteres en minuscula
mensaje='Hola Mundo'
print('Es minuscula?',mensaje.lower().islower())
print('Es mayuscula?',mensaje.isupper())