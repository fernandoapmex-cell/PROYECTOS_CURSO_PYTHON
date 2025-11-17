#ABC - Abstract Base Class
#Nos permite asegurarnos que las clases que heredan implementen los metodos de la clase padre
#ABC permite escribir una jerarquia de clases mas robusta y codigo mas mantenible
from abc import ABCMeta, abstractmethod


#Ej.Sin usar ABC y los posibles problemas

class ClaseBase1:
    def metodo1(self):
        raise NotImplementedError
    def metodo2(self):
        raise NotImplementedError
class ClaseConcreta1(ClaseBase1):
    #Implementacion de la clase padre
    def metodo1(self):
        print('Metodo 1 implementado')
    #el metodo 2 no lo vamos a implementar
    #esto ya es un problema por si solo por que no se reporta la falta de implementacion
#Hay un problema.se puede instanciar la clase base
clase_base=ClaseBase1()
#clase_base.metodo1() esto es algo no deseado

#Esto funciona segun lo esperado
clase_concreta=ClaseConcreta1()
clase_concreta.metodo1()
#el metodo 2 no ha sido definido por la clase hija por eso se llama el de la clase padre
#clase_concreta.metodo2()
#vamos a resolver los detalles anteriores usando ABC
class ClaseBase2(metaclass=ABCMeta):
    #No tenemos que agregar la implementacion a ser un metodo abstracto
    @abstractmethod
    def metodo1(self):
        pass
    @abstractmethod
    #estamos obligados a implementar todos los metodos de la clase padre en las clases ABC
    def metodo2(self):
        pass
class ClaseConcreta2(ClaseBase2):
    def metodo1(self):
        print('Metodo 1 implementado')
    def metodo2(self):
        print('Metodo 2 implementado')
    #dejamos sin implementar el metodo 2
#no se puede crear un objeto de una clase abstracta
#clase_base=ClaseBase2()

#Instanciamos la claseconcreta 2
clase_concreta=ClaseConcreta2()

