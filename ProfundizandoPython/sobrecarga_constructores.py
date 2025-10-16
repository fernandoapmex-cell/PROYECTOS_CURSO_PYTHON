#simulacion de sobrecarga de constructores en py
#otras formas de crear objetos en python
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
    #con metodo estaitco
    @classmethod
    def crear_persona_vacia(cls):
        return cls(None,None)
    #con metodo estatico
    @classmethod
    def crear_persona_con_valores (cls,nombre,apellido):
        return cls(nombre,apellido)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'


persona_vacio=Persona.crear_persona_vacia()
#aca estamos modificando que se pueda autollamar la funcion vacia para crear un objeto en None
print(persona_vacio)
persona_con_valores=Persona.crear_persona_con_valores('Fernando','Andrade')
print(persona_con_valores)