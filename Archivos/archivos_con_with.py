#with open('prueba.txt','r',encoding='utf8') as archivo:
 # print(archivo.read())
from manejo_archivos_dos import ManejoArchivos

with ManejoArchivos('prueba.txt')as archivo:
    print(archivo.read())