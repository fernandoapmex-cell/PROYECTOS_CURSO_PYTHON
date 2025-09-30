#definimos la clase coche

class Coche:
    def __init__(self, marca, modelo,color):
        self._marca = marca #atributo publico
        self._modelo = modelo #atributo protegido
        self._color = color #atributo privado

    def conducir(self):
        print(f'''
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}
        ''')

    # def get_marca(self):
    #     return self._marca
    @property
    def marca(self):
        return self._marca
    #usar notacion stter para metodo set y hacerlo mas pythonico
    @marca.setter
    def marca(self,marca):
        self._marca = marca
    def get_modelo(self):
        return self._modelo
    def set_modelo(self,modelo):
        self._modelo = modelo
    def get_color(self):
        return self._color
    def set_color(self,color):
        self._color = color
#Programa principal

if __name__ == '__main__':
    # #cracion de primer coche
    coche1= Coche('Toyota','Yaris','Azul')
    # coche1.conducir()
    # #ejemplo de como se encapsulan los atributos
    # coche1.marca = 'Toyota 2'
    # coche1._modelo = 'Yaris 2' #esto no es una buena practica
    # coche1.__color = 'Azul 2'#ignoro la modificacion
    # coche1.conducir()
    coche1.conducir()
    coche1.marca='Toyota 2'
    coche1.set_modelo('Yaris 3')
    coche1.set_color('Rojo')
    coche1.conducir()
    print(f'Atrubuto de marca utilizando property: {coche1.marca}')
    coche1.marca = 'Toyota 4'
    coche1.conducir()
    #intentamos agregar un nuevo atributo
    setattr(coche1,'placas','puebla')
    coche1.conducir()
    #los atributos de setattr solo son para objetos que se le meten no para la clase directamente
    print(coche1.placas)
    #otra manera de agregar atributos a un objeto directamente
    coche1.llantas='michelin'
    print(coche1.llantas)
    #preguntar a python los atributos de cierto objeto
    print(f'Atributos del coche1: {coche1.__dict__}')
