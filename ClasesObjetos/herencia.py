class Animal:
    def comer (self):
        print('Como muchas veces al dia')
    def dormir(self):
        print('Duermo muchas horas')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

    #sobreescritura del metodo dormir de la clase padre
    def dormir(self):
        print('Duermo 15 horas al dia')

#programa principal

print('*** Ejemplo de herencia en py ***')
print('Clase padre,Soy un animal')
animal1=Animal()
animal1.comer()
animal1.dormir()

print('Clase hija perro')
perro1= Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()