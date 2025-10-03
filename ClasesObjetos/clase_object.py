class Persona:
    def __init__(self, nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        #sobreescribir el metod __str__
    def __str__(self):
        return f'''
            nombre: {self.nombre}
            apellido: {self.apellido}
            direccion de memoria: {super.__str__(self)}
        '''
#codigo principal
persona1= Persona("Ana","Martinez")
print(persona1) #el metodo str se llama automaticamente desde le metodo print