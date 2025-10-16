class Persona:
    contador_personas = 0

    def  __init__(self,nombre,apellido):
        self._nombre = nombre
        self._apellido = apellido

#mostrar atributos de un objeto

persona1=Persona('Fernando','Sanchez')
print(persona1.__dict__)

#crear un atributo al vuelo (en este momento) 1 linea
print(persona1.contador_personas) # accediento al atributo de clase
#no es posible modificarlo con el objeto solo con la clase
persona1.contador_personas = 10
print(persona1.__dict__)
#para accder al atributo de la clase es con el nombre de la clase misma
print(Persona.contador_personas)#atributo de clase
print(persona1.contador_personas)#atributo de objeto 1

#un segundo objeto
persona2=Persona('Fernando','Cristobal')
print(persona2.__dict__)
print(persona2.contador_personas)

#asociar un atributo de clase al vuelo
#al crear un atributo de calse al vuelo ya es accesible tambien en el objeto 1
Persona.contador2= 20
print(Persona.contador2)