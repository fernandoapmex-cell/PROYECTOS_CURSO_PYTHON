#diccionarios o dics
#tambien se les conoce como maps mapas hashmaps lookup tables,etc (llave  - valor)
#Diccionario clasico: Directorio
directorio = {
    'Juan': 58689001,
    'Alicia':5543534,
    'Carlos':23452354
}
print(directorio)
#Recuperar un elemento
print(directorio['Juan'])

#llave que no exite arroja error tipo keyerror
#(directorio['Juan22'])

#Podemos usar una expresiuon para crear un diccionario
valores_al_cuadrado = {x:x*x for x in range(0,4)}
print(valores_al_cuadrado)
#tipos mutables no pueden definirse en un diccionario
# lista=[1,2,3,4,5]
# directorio_erroneo ={lista:'A'}
tupla=(1,2,3,4,5)
directorio_erroneo ={tupla:'A'}
print(directorio_erroneo)

#si queremos garantizar un orden de insersion,OrderedDict

from collections import OrderedDict, defaultdict, ChainMap

diccionario_ordenado=OrderedDict(uno =1,dos=2,tres=3,cuatro=4)
print(diccionario_ordenado)
#agregamos un nuevo elemento
diccionario_ordenado['cinco']=5
print(diccionario_ordenado)
#obtenemos las llaves
print(diccionario_ordenado.keys())
#obtenemos los valores
print(diccionario_ordenado.values())
#cambiamos el valor de una llave
diccionario_ordenado['uno']=-1
print(diccionario_ordenado)
#eliminamos una llave
diccionario_ordenado.pop('uno')
print(diccionario_ordenado)
#volvemos a insertar el elemento prviamente eliminado
diccionario_ordenado['uno']=-1
print(diccionario_ordenado)
#diccionario por default
#defaultdict es una subclase de la clase dict
diccionario_default=defaultdict(lambda :'Valor Erroneo')
diccionario_default['a']=1
diccionario_default['b']=2
print(diccionario_default.items())
#imprimir un elemento no existente
print(diccionario_default['c'])
#podemos crear valores por default como una lista por default
diccionario_default_lista = defaultdict(list)
#si accedemos a una llave no existente la crea y los valores se asignan como una lista
diccionario_default_lista['nombres'].append('Juan')
diccionario_default_lista['nombres'].append('Alicia')
diccionario_default_lista['nombres'].append('Carlos')
diccionario_default_lista['telefono'].append('123456')
print(diccionario_default_lista.items())
print(diccionario_default_lista.keys())
print(diccionario_default_lista.values())
#Buscar en multiples diccionarios como si fuera un diccionario unico
diccionario1 = {'uno':1,'dos':2,'tres':3}
diccionario2={'cuatro':4,'cinco':5}
#queremos unir los 2 diccionarios en 1 solo
#combinakos los diccionarios
combinacion_diccionarios=ChainMap(diccionario1,diccionario2)
print(combinacion_diccionarios)
#buscamos en todos los diccionarios de izquierda a derecha osea si hay repetidos arroja el primero en encontrar
print(combinacion_diccionarios['cinco'])
#si proporcionamos una llave no existente manda keyerror
#print(combinacion_diccionarios['seis'])

#obtencio de diccionarios de solo lectura read only
from types import  MappingProxyType
diccionario_modificable={'uno':1,'dos':2,'tres':3}
diccionario_solo_lectura=MappingProxyType(diccionario_modificable)
#leemos el valor del diccionario
print(diccionario_solo_lectura)
#no se puede agregar elementos nuevos
# diccionario_solo_lectura['cuatro']=4
# print(diccionario_solo_lectura)
#modificar valores
# diccionario_solo_lectura['uno']=8
# print(diccionario_solo_lectura)

#si modificamos el diccionario mutable afecta al de solo lectura
diccionario_modificable['dos']=22
#veamos lso cambios en los 2 diccionarios
print(diccionario_modificable)
print(diccionario_solo_lectura)
