from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, \
    QPushButton


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
        layout_principal=QVBoxLayout()
        layout_botones=QHBoxLayout()
        self.layout_stack=QStackedLayout()
        #agregamos los layout hijos al principal
        layout_principal.addLayout(layout_botones)
        layout_principal.addLayout(self.layout_stack)
        #creamos los botones
        boton_rojo=QPushButton('Rojo')
        boton_azul=QPushButton('Azul')
        boton_amarillo=QPushButton('Amarillo')
        #publicamos los colores al layout tipo stack
        self.layout_stack.addWidget(Color('red'))
        self.layout_stack.addWidget(Color('blue'))
        self.layout_stack.addWidget(Color('yellow'))
        #publicamos el boton en el layout de botones
        layout_botones.addWidget(boton_rojo)
        layout_botones.addWidget(boton_azul)
        layout_botones.addWidget(boton_amarillo)
        #conectamos el evento press del boton respectivo
        boton_rojo.pressed.connect(lambda :self.activar_color(0))
        boton_azul.pressed.connect(lambda :self.activar_color(1))
        boton_amarillo.pressed.connect(lambda :self.activar_color(2))

        #se publica el layout principal
        componente = QWidget()
        componente.setLayout(layout_principal)
        # el componente se expande para cubrir el tamaño disponible
        self.setCentralWidget(componente)
    def activar_color(self,indice):
        self.layout_stack.setCurrentIndex(indice)

# ejecutamos prueba
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()