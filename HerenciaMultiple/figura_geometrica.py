class FiguraGeometrica:
    def __init__(self, ancho,alto):
        if 0 < ancho < 10:
            self._ancho = ancho
        else:
            self._ancho = 0
        self._alto = alto
        if 0 < alto < 10:
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
    def __str__(self):
        return (f'Figura Geometrica:'
                f'ancho: {self._ancho}, alto: {self._alto}')