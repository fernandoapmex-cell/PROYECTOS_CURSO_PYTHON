#Decoradores de clase
#permiten transformar de manera programatica nuestra clase
#es smilar a los decoradores de funciones (metaprogramacion)
import inspect
from sqlite3.dbapi2 import paramstyle


#usamos cls para recibir la clase
def decorador_repr(cls):
    print(f'Se ejecuta decorador de la clase y recibimos el objeto de la clase {cls.__name__}')
    #revisamos los atributos de la clase con el metodo vars
    atributos = vars (cls)
    #iteramos los atriburtos
    for nombre,valor in atributos.items():
        print(f'La clase {nombre} tiene {valor}')
    #revisamos si se ha rescrito el meotdo init
    #if '__init__' not in atributos:
    #   raise TypeError(f'{cls.__name__} no tiene la clase __init__')
    firma_init= inspect.signature(cls.__init__)
    print(f'Firma metodo init:{firma_init}')
    #regresar solo los parametros del primero en adelante para quitar el self
    pametros_init=list(firma_init.parameters)[1:]
    print(pametros_init)
    #revisamos si cada parametro tiene un metodo property asociado
    for parametro in pametros_init:
        #property es un valor build in para preguntar si se esta utilizando el decorador de property
        es_metodo_property=isinstance(atributos.get(parametro),property)
        if not es_metodo_property:
            raise TypeError (f'No Existe un metodo property para:{parametro}')
    #crear metodo repr dinamicamente
    def metodo_repr(self):
        #obtenemos el nombre de la clase dinamicamente
        nombre_clase = self.__class__.__name__
        print(f'Nombre de la clase{nombre_clase}')
        # obtenemos los nombres de las propiedades y sus valores dinamicamente
        # usamos una experesion generadora para crear la siguiente cadena con la forma del nombre dle atributo
        generador_args = (f'{nombre} = {getattr(self, nombre)!r}' for nombre in pametros_init)
        lista_args=list(generador_args)
        # lista dle generador
        print(f'Lista del generador:{lista_args}')
        #cramos la cadena apartir de la lista de argumentos
        argumentos=', '.join(lista_args)
        print(f'Argumentos del metodo repr:{argumentos}')
        resultado_metodo_repr=f'{nombre_clase}.{argumentos}'
        print(f'Resultado del metodo repr:{resultado_metodo_repr}')
        return f'Resultado de ejecutar el metodo repr'
    #agregar dinamicamente el metodo repr a la calse
    setattr(cls,'__repr__',metodo_repr)

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
    #def __repr__(self):
    #   return f'Persona(nombre={self._nombre}, apellido={self._apellido})'

persona1=Persona('Juan','Perez')
print(persona1)
persona2=Persona('Karla','Gomez')
print(persona2)
#comprobar que tenemos el metodo properti nombre,apellido,repor
print(persona1.__dir__())
#saber si esta sobreescrito
codigo_repr=inspect.getsource(persona1.__repr__)
print(codigo_repr)