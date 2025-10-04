class FiguraGeometrica:
    def __init__(self, ancho,alto):
        self._ancho = ancho
        self._alto = alto

    def getAncho(self):
        return self._ancho
    def getAlto(self):
        return self._alto
    def setAncho(self, ancho):
        self._ancho = ancho
    def setAlto(self, alto):
        self._alto = alto