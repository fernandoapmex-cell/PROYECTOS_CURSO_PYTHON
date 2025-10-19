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
class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')
    def metodo(self):
        print('Metodo Clase3')
class Clase4(Clase2,Clase3):
    def metodo(self):
        print('Metodo Clase4')
        super().metodo()
#objeto de clase 4
clase4 = Clase4()
#usamos bases para ver como se ejecuta el obj
print(Clase4.__bases__)
#usamos mro para ver como se ejecutan las clases hasta la chase padre
print(Clase4.__mro__)
#cual metodo se ejecuta
clase4.metodo()