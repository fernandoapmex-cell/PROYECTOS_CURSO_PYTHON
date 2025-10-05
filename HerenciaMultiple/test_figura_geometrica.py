from HerenciaMultiple.cuadrado import Cuadrado
from HerenciaMultiple.figura_geometrica import FiguraGeometrica
from HerenciaMultiple.rectangulo import Rectangulo
#no podemos instanciar una clase abstracta
#figura = FiguraGeometrica()
print('creacion objeto cuadrado'.center(50,'-'))
cuadrado1=Cuadrado(14,'Rojo')
cuadrado1._alto = -10
print(cuadrado1)
print('creacion objeto rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(13,18,'Amarillo')
print(rectangulo1)
#print(cuadrado1.getAncho())
#print(cuadrado1.getAlto())
#print(cuadrado1.getColor())

#metodo MRO - Method Resolution Order|