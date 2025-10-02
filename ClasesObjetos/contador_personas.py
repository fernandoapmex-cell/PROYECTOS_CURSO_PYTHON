class Persona:
    #atributo de clase
    contador_personas = 0
    def __init__(self,nombre,apellido):
        #el contructor crea a los objetos
        #incrementamos el valor del atributo de clase
        Persona.contador_personas +=1
        self.id= Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id} - Nombre: {self.nombre} - Apellido: {self.apellido}')

    @staticmethod
    def get_contador_personas_estatico():
        print('Metodo estatico')
        return Persona.contador_personas
    #forma mas paytonica
    @classmethod
    def get_contador_personas_clase(cls):
        print('Metodo clase')
        return cls.contador_personas
if __name__ == '__main__':
    print('Emjemplo contador objetos persona de tipo Persona')
    persona1=Persona('Carlos','Tevez')
    persona1.mostrar_persona()
    #segundo objeto
    persona2=Persona('Salazar','Carrillo')
    persona2.mostrar_persona()

    #imprimir el valor del contador personas
    print(f'Contador de objetos Persona: {Persona.contador_personas}')
    #imprimir usando metodo estatico
    print(f'Contador de objetos Persona:(Statico) {Persona.get_contador_personas_estatico()}')
    print(f'Contador de objetos Persona:(Clase) {Persona.get_contador_personas_clase()}')
