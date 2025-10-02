from ClasesObjetos.persona import Persona


class Persona:
    atributo_clase = 0
    def __init__(self,atributo_instancia):
        self.atributo_instancia = atributo_instancia

    #programa principal

if __name__ == '__main__':  
    print(f'*** Atributos de Clase ***')
    print(f'Atributo de clase: {Persona.atributo_clase}')
    #modificamos el atributo de calse
    Persona.atributo_clase = 10
    print(f'Atributo de clase: {Persona.atributo_clase}')
    #creamos un objeto de persona1
    persona1 = Persona(15)
    print(f'Atributo de clase desde persona 1: {persona1.atributo_clase}')
    print(f'Atributo de instancia desde persona 1: {persona1.atributo_instancia}')