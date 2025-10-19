#Decoradores de clase
#permiten transformar de manera programatica nuestra clase
#es smilar a los decoradores de funciones (metaprogramacion)

#usamos cls para recibir la clase
def decorador_repr(cls):
    print(f'Se ejecuta decorador de la clase y recibimos el objeto de la clase {cls.__name__}')
    # el decorador siempre tiene que regresar una clase
    return cls
@decorador_repr
class Persona:
    def __init__(self,nombre,apellido):
        print('Se ejecuta inicializador de la clase Persona')
        self._nombre=nombre
        self._apellido=apellido

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self,apellido):
        self._apellido=apellido

persona1=Persona('Juan','Perez')