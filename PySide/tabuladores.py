from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QTabWidget


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
        self.setWindowTitle('Tabuladores  en Pyside')
        #creamos el componente de tab
        tabulador = QTabWidget()
        #posicion de las etiquetas del tabulador
        tabulador.setTabPosition(QTabWidget.West)
        #Indicamos si queremos que se muevan las etiquetas del tabulador
        tabulador.setMovable(True)
        #para que se vea similar en macOS
        tabulador.setDocumentMode(True)
        #agregamos colores al tabulador
        tabulador.addTab(Color('red'), "Rojo")
        tabulador.addTab(Color('green'), "Verde")
        tabulador.addTab(Color('yellow'), "Amarillo")

        self.setCentralWidget(tabulador)

# ejecutamos prueba
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()