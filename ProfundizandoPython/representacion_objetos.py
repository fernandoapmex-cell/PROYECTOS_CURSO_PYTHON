#Representacion de objetos (str,repr,format)
# print(dir(object))

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
    #diferencias entre str repr y format mas enfocado para los programadores

    def __repr__(self):
        #asi podemos obtener el nombre de la clase de manera dinamica con class name
        return f'{self.__class__.__name__}(nombre:{self.nombre},apellido:{self.apellido})'
    #el metodo str es mas para el usuario final u otros sistemas
    #la implementacion por default llama al metodo repr
    def __str__(self):
        return f'{self.__class__.__name__}:({self.nombre},{self.apellido})'
    #format implementacion por default es str
    #se manda a llamar un f-string auto
    def __format__(self,format_spec):
        return f'{self.__class__.__name__}(con nombre :{self.nombre} y apellido :{self.apellido})'

persona1=Persona('Fernando','Andrade')
#asi podemos mandar a llamar el metodo repr
print(f'Mi objeto persona1:{persona1!r}')
#str (el metodo print llama al metodo str automaticamente
print(persona1)
#format
print(f'{persona1}')