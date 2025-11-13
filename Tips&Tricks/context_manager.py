# with open('prueba.txt','w')as archivo:
#     archivo.write('hola desde python')
#
# #esto es equivalente a :
#
# archivo=open('prueba.txt','w')
# try:
#     archivo.write('hola desde python')
# finally:
#     archivo.close()
from contextlib import contextmanager


# #esto no es equivalente
# archivo=open('prueba.txt','w')
# archivo.write('hola sin with')
#esto no asegura el cierre de recursos en caso de error

#manejo de context manager en clases
#1.-implementando el protocolo o interface con las funciones (__enter__) y (__exit__)
#2.- utilizando la libreria de context lib

#veamos la opcion 1

# class ManejoArchivos:
#     def __init__(self, nombre):
#         self.nombre=nombre
#
#     def __enter__(self):
#         self.archivo=open('prueba.txt','w')
#         return self.archivo
#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.archivo:
#             self.archivo.close()
@contextmanager
def manejador_archivos(nombre):
    try:
        archivo = open(nombre, 'w')
        yield archivo
    finally:
        archivo.close()
#Ejercicio de Identador
class Identador():
    def __init__(self):
        self.nivel = 0
    def __enter__(self):
        self.nivel += 1
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.nivel -= 1
    def imprimir(self,texto):
        print(' '*self.nivel + texto)

#mismo ejercicio de identador pero con context lib
class Identador2():
    def __init__(self):
        self.nivel = 0
    @contextmanager
    def identador(self):
        try:
            self.nivel += 1
            yield self
        finally:
            self.nivel -= 1
    def imprimir(self,texto):
        print(' '*self.nivel + texto)



#este metodo es un generador, en primer lugar adquiere el recurso y posteriormente suspende la ejecucion al utilizar yield
if __name__ == '__main__':

    # #prueba implementando  el protocolo de context Manager
    # # with ManejoArchivos('prueba.txt') as archivo:
    # #     archivo.write('prueba desde manejo archivo')
    #
    # #prueba d ela libreria contexto lib
    # with manejador_archivos('prueba.txt') as archivo:
    #     archivo.write('prueba desde decorador')
    #     archivo.write('adios')
    # prueba de identador
    # with Identador() as identador:
    #     identador.imprimir('primer nivel')
    #     with identador:
    #         identador.imprimir('segundo nivel')
    #         identador.imprimir('continua segundo nivel')
    #         with identador:
    #             identador.imprimir('tercer nivel')
    #     identador.imprimir('fin primer nivel')

    #prueba de class identificador2
    objeto= Identador2()
    with objeto.identador():
        #este es el primer nivel
        objeto.imprimir('primer nivel')
        objeto.imprimir('continua primer nivel')
        with objeto.identador():
            objeto.imprimir('segundo nivel')
            with objeto.identador():
                objeto.imprimir('tercer nivel')
        objeto.imprimir('fin primer nivel')

