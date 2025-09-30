#Definicion de una clase

class Persona:
    #constructor

    def __init__(self, nombre, apellido):
        #creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        rint(f'Dir Mem : {id(self)}')
        print(f'Dir Mem en exa : {hex(id(self))}')
        ''')

#creacion de objetos
if __name__ == '__main__':
    #creacion de un primer objeto
    persona1 = Persona('Layla','Acosta') #crea un objeto vacio en memoria
    #persona1.inicializar_persona(nombre='layla', apellido='Acosta')
    persona1.mostrar_persona()
    print(f'Dir Mem : {id(persona1)}')
    print(f'Dir Mem en exa : {hex(id(persona1))}')
    #creamos un segundo objeto
    persona2 = Persona('Elias','Chavez') #aca ya no usamos la creacion del objeto vacio por que ya tenemos constructor y se ejecutan automaticamente sin llamarlos
    #persona2.inicializar_persona(nombre='Ian', apellido='Sanchez') aca ya no usamos este metodo por que ya tenemos constructor para inicalizar valores
    persona2.mostrar_persona()
