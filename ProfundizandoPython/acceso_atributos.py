#ejemplo de atributos publicos,protegidos,y privados
class MiClase:
    def __init__(self,publico,protegido,privado):
        self.publico=publico
        self._protegido=protegido
        self.__privado=privado
objeto=MiClase('Valor publico','Valor protegido','Valor privado')
#accdeder al atributo publico
print(objeto.publico)
#modificar el valor publico
objeto.publico='Valor publico Nuevo'
print(objeto.publico)
#acceso al valor protegido
#usar solo dentro de la misma clase o clases hijas no directamente pero aun asi es posible accederlo
print(objeto._protegido)
#modificar atributo protegido (no buena practica)
objeto._protegido='Valor protegido Nuevo'
print(objeto._protegido)

#acceder al valor privado
#este solo funciona en la misma clase no dejara ingresar
#print(objeto.__privado)
#pero automaticamente convierte el objeto de la siguiente forma objeto._clase__atributo_privado
print(objeto._MiClase__privado)
#modificar valor privado no recomendable
objeto._MiClase__privado='Valor privado Nuevo'
print(objeto._MiClase__privado)