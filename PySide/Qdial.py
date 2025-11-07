from PySide6.QtWidgets import QMainWindow, QApplication, QDial


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        #es una rueda para audio
        componente=QDial()
        componente.setRange(-5,50)
        componente.valueChanged.connect(self.cambio_valor)
        componente.sliderMoved.connect(self.slider_cambio_posicion)
        componente.sliderPressed.connect(self.slider_presionado)
        componente.sliderReleased.connect(self.slider_soltado)
        self.setCentralWidget(componente)

    def slider_presionado(self):
        print('Dial presionado')

    def slider_soltado(self):
        print('Dial soltado')

    def cambio_valor(self, nuevo_valor):
        print(f'Nuevo valor{nuevo_valor}')

    def slider_cambio_posicion(self, nueva_posicion):
        print(f'Nuevo posicion{nueva_posicion}')
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()