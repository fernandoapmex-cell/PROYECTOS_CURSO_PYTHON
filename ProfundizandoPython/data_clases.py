from dataclasses import dataclass
from typing import ClassVar
@dataclass(eq=True, frozen=True)
class Domicilio:
    calle:str
    numero:int =0


@dataclass(frozen=True)
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_personas:ClassVar[int]=0

    #hacer que las variables de instancia no acepten objetos vacios
    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Nombre debe contener caracter y no estar vacio {self.nombre}')
domicilio1=Domicilio('Saturno',15)
#aca se genera automaticamente el metodo repl
persona1=Persona('Juan','Perez',domicilio1)
#asi mandamos el repr con !r
print(f'{persona1!r}')
print(f'Variable de clase: {Persona.contador_personas}')
#variables de instancia
print(f'Variables de instancia {persona1.__dict__}')
#Variable con valores vacios
persona_vacia=Persona('Fer','Perez',None)
print(f'{persona_vacia!r}')
#revisar igualdad entre dos objetos de persona dataclass utilizan el metodo __eq__
persona2 = Persona('Juan','Perez',Domicilio('Jupiter',30))
print(f'Son objetos iguales? {persona2 == persona1}')
#agregar esta calse a una coleccion
coleccion={persona1,persona2}
print(coleccion)
