#__str__ su objetivo es que la informacion sea legible para el usuario
#__repr__ su objetivo es que la informacion no sea ambigua(formato tipo constructor)

#la implementacion por default del metodo str llama al metodo repr

class Auto:
    def __init__(self, marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

#por default solo se muestra el nombre de la clase y el id del objeto (direccion de memoria)
audi_a3=Auto('audi','a3','rojo')
print(audi_a3)

class AutoStr:
    def __init__(self, marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    def __str__(self):
        return f'str:Marca: {self.marca}, modelo: {self.modelo}, color: {self.color}'
    # def __repr__(self):
    #     return f'repr:Marca: {self.marca}, modelo: {self.modelo}, color: {self.color}'
    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.marca!r}, {self.modelo!r}, {self.color!r})')
audi_a3=AutoStr('audi','a3','rojo')
#tenemos diferntes formas de imprimir el objeto
print(audi_a3)
print(audi_a3.__str__())
print(str(audi_a3))
print('{}'.format(audi_a3))
print(f'{audi_a3}')
#sin embargo es mas recomendable usar repr en lugar de str
#ejemplo: cualquier coleccion utiliza repr en lugar de str para mostrar la informacion
print([audi_a3])
#tambien usando !r
print(f'{audi_a3!r}')

#Tambien manualmente podemos escoger que metodo utilizar
print(str(audi_a3))
print(repr(audi_a3))