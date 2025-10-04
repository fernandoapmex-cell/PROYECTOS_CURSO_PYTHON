from HerenciaMultiple.color import Color
from HerenciaMultiple.figura_geometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):
        #super().__init__(lado)
        #llamar al super constructor cuando tienes 2 clases padre
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)
    def calcular_area(self):
        return self._alto * self._alto

