from HerenciaMultiple.cuadrado import Cuadrado
from HerenciaMultiple.rectangulo import Rectangulo
print('creacion objeto cuadrado'.center(50,'-'))
cuadrado1=Cuadrado(14,'Rojo')

#print(cuadrado1.getAncho())
#print(cuadrado1.getAlto())
#print(cuadrado1.getColor())
print(cuadrado1.calcular_area())
print(cuadrado1)
print('creacion objeto rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(13,18,'Amarillo')
print(rectangulo1.calcular_area())
print(rectangulo1)
#metodo MRO - Method Resolution Order|