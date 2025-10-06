archivo = open('prueba.txt', 'r',encoding='utf8')
#print(archivo.read())

#leer algunos caracteres
#print(archivo.read(4))
#leer lineas completas
#print(archivo.readline())
#print(archivo.readline())

#iterar nuestro archivo y cada una de las lineas

#for linea in archivo:
    #print(linea)

#print(archivo.readlines())

#acceder a una linea de la lista

#print(archivo.readlines()[2])

#abrimos un nuevo archivo y pasamos el contenido de un archvio existente al nuevo
#a - anexar informacion

archvo2 = open('copia.txt','a',encoding='utf8')
archvo2.write(archivo.read())

archivo.close()
archvo2.close()
print('se ha terminado el proceso de leer y copiar archivos')
