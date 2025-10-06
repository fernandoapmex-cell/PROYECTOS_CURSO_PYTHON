class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def __add__(self,other):
        return self.nombre+other.nombre
    def __sub__(self,other):
        return self.edad-other.edad

# obj1 + obj2 al querer sobre escribir objetos se llama obj1.__add__(obj2)
#programa principal
persona1=Persona('Juan',24)
persona2=Persona('Gabriel',20)
print(persona1+persona2)
print(persona1-persona2)