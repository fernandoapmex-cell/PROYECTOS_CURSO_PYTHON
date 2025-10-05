#para hacer una clase abstracta tenemos que extender de la clase abc = Abstract Base Class
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, ancho,alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0

    def getAncho(self):
        return self._ancho
    def getAlto(self):
        return self._alto
    def setAncho(self, ancho):
        self._ancho = ancho
    def setAlto(self, alto):
        self._alto = alto
    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return (f'Figura Geometrica:'
                f'ancho: {self._ancho}, alto: {self._alto}')

    def _validar_valor(self,valor):
        return True if 0 < valor < 10 else False