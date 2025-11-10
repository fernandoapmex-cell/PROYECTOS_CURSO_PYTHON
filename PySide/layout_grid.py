from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout


class Color(QWidget):
    def __init__(self,nuevo_color):
        super().__init__()
        #indicamos que se puede agregar un color de fondo backgroud
        self.setAutoFillBackground(True)
        paleta_colores=self.palette()
        #creamos el componente de color de fondo aplicando el nuevo color que hemos recibido en el constructor+
        paleta_colores.setColor(QPalette.Window,QColor(nuevo_color))
        #aplicamos el nuevo color
        self.setPalette(paleta_colores)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layout en Pyside')
        layout=QGridLayout()
        layout.addWidget(Color('red'),0,0)
        layout.addWidget(Color('green'),0,2)
        layout.addWidget(Color('blue'),1,1)
        componente= QWidget()
        componente.setLayout(layout)
        #el componente se expande para cubrir el tamaño disponible
        self.setCentralWidget(componente)
#ejecutamos prueba
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()