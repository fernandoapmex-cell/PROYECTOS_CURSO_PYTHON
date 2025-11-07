from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QSlider


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        #qslider o barra deslizadora
        componente = QSlider(Qt.Horizontal)
        #establecer valores tambien se puede con range
        # componente.setMinimum(-5)
        # componente.setMaximum(8)
        #componente.setRange(3,5)
        componente.valueChanged.connect(self.cambio_valor)
        componente.sliderMoved.connect(self.slider_cambio_posicion)
        componente.sliderPressed.connect(self.slider_presionado)
        componente.sliderReleased.connect(self.slider_soltado)
        self.setCentralWidget(componente)
    def slider_presionado(self):
        print('slider presionado')
    def slider_soltado(self):
        print('slider soltado')
    def cambio_valor(self,nuevo_valor):
        print(f'Nuevo valor{nuevo_valor}')
    def slider_cambio_posicion(self,nueva_posicion):
        print(f'Nuevo posicion{nueva_posicion}')
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()