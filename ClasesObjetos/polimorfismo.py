#polimorfismo
class Animal:
    def hacer_sonido(self):
        print('Hago mucho pitido')
class Perro(Animal):
    def hacer_sonido(self):
        print('puedo Ladrar')
class Gato(Animal):
    def hacer_sonido(self):
        print('puedo Maullar')
#funcion polimorfica o duck typeing
def hacer_sonido_animal(animal):
    animal.hacer_sonido()
#programa principal
print('Ejemplo polimorfismo')
print('Clase Padre Animal:')
animal1=Animal()
animal1.hacer_sonido()
print('Clase Hija Perro: ')
perro1=Perro()
perro1.hacer_sonido() #Polimorfismo
print('Clase Hija Gato: ')
gato1=Gato()
gato1.hacer_sonido()

#imprimir usando la funcion polimorfica
hacer_sonido_animal(animal1)
hacer_sonido_animal(perro1)
hacer_sonido_animal(gato1)
