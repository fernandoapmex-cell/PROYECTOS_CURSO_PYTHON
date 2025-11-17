#namedtuples son una estension de tuple
#son una buena alternativa para escribir clases simples(atributos son tipos inmutables)
#asignar un identificador a cada elemento de nuestras tuplas
from collections import namedtuple
#definimos una clase con atributos inmutables usando namedtuple
Persona1 = namedtuple('Persona1','nombre apellido edad')
#creamos una instancia de la clase (se agrega un constructor por default con los atributos)
persona1=Persona1('Juan','Perez',28)
#En automatico se crea un metodo repr con los atributos proporcionados
print(persona1)

#creamos nuestra clase con los atributos usando una lista
Persona2=namedtuple('Persona2',['nombre','apellido','edad'])
persona2=Persona2('Juan','Perez',28)
print(persona2)

#podemos acceder a los atributos de manera individual por nombre y por indice como una tupla

print(f'Nombre: {persona1.nombre}')
print(f'Apellido: {persona1.apellido}')
print(f'Edad: {persona1.edad}')

#accedemos a los atributos por indice
print(f'Nombre: {persona1[0]}')
print(f'Apellido: {persona1[1]}')
print(f'Edad: {persona1[2]}')

#podemos convertir los valores a una tupla
print(tuple(persona1))
#podemos acer unpaking
nombre,apellido,edad=persona1
print(f'Nombre: {nombre}')
print(f'Apellido: {apellido}')
print(f'Edad: {edad}')
#acer unpaing como argumento a una funcion
print(*persona1)

#las tuplas son inmutables al igual que namedtuple
#persona1.edad= 30

#subclases de namedtuples

class Persona3 (Persona2):
    #agregamos un nuevo metodo a la clase hija
    def convertir_mayusculas(self):
        return f'Nombre:{self.nombre.upper()}{self.apellido.upper()}'
persona3=Persona3('maria','lara',56)
print(persona3)
print(persona3.convertir_mayusculas())

#existe otra forma de hacer extends de la clase(la forma recomendada con named tuple
#con el fields y el mas agregamos un elemento nuevo tomando los atributos de otra clase

Persona4=namedtuple('Persona4',Persona2._fields+('email',))
persona4=Persona4('fernando','perez',43,'fer@mail.com')
print(persona4)
#metodos de ayuda (built-in) en mnamedtuple
print(persona4._fields)
#Convertir a un diccionario
dic_persona4=persona4._asdict()
print(dic_persona4)