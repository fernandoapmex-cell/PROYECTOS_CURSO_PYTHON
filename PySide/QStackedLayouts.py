from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout


class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        # indicamos que se puede agregar un color de fondo backgroud
        self.setAutoFillBackground(True)
        paleta_colores = self.palette()
        # creamos el componente de color de fondo aplicando el nuevo color que hemos recibido en el constructor+
        paleta_colores.setColor(QPalette.Window, QColor(nuevo_color))
        # aplicamos el nuevo color
        self.setPalette(paleta_colores)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layout en Pyside')
        layout = QStackedLayout()
        #por default solo se ve el primer wiget agregado
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.setCurrentIndex(1)
        # el componente se expande para cubrir el tamaño disponible
        componente = QWidget()
        componente.setLayout(layout)
        self.setCentralWidget(componente)


# ejecutamos prueba
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()