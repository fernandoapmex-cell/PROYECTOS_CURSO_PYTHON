#profundizando en diccionarios
#los diccionarios guardan un orden a diferencia de un set
diccionario={'Nombre':'Juan','Apellido':'Pedro','Edad':29}
print(diccionario)
#los dic son mutables pero las llaves deben ser inmutables
#diccionario={[1,2]:'Valor'}
#si lo convertimos a tupla
diccionario={(1,2):'Valor'}
print(diccionario)
#se agrega una llave con su valor si no se encuentra dentro del diccionario
diccionario['Departamento']='Sistemas'
print(diccionario)
#los diccionarios al igual que los set no usan llaves duplicadas(si ya existe se reemplaza)
diccionario['Nombre']='Juan Carlos'
print(diccionario)
#recuperar elementos de un diccionario indicando una llave
print(diccionario['Nombre'])
#si no encuentra la llave lanza una excepcion
#print(diccionario['nombre'])

#metodo get recupera una llave y si no existe no lanza excepcion
#ademas podemos regresar un valor en caso de que no exista la llave asi no falla el programa con get
print(diccionario.get('nombre','No se encontro la llave'))
print(diccionario)
#set default si modifica el diccionario en caso de que no se encuentre la llave y se puede agregar un valor por default
nombre = diccionario.setdefault('nombre','Valor por default')
print(nombre)
print(diccionario)
#imprimir un diccionario de otra manera con pprint

from pprint import pprint as pp
pp(diccionario,sort_dicts=False)