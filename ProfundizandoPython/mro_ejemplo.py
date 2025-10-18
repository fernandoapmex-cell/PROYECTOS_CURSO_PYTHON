class Clase1:
    def __init__(self):
        print('Clase1.__init__')
    def metodo(self):
        print('Metodo Clase1')
class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')
    def metodo(self):
        print('Metodo Clase2')
class Clase3(Clase2):
    def __init__(self):
        print('Clase3.__init__')
    def metodo(self):
        print('Metodo Clase3')