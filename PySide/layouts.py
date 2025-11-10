from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout


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
        self.setWindowTitle('Layout En Pyside')
        #anidar layouts (un layout dentro de otro)
        #creamos en primer lugar un layout en horizontal y otro en vertical
        layout_horizontal=QHBoxLayout()
        #agregamos espacio al margen del layout horizontal
        layout_horizontal.setContentsMargins(10,10,10,10)
        layout_horizontal.setSpacing(20)
        layout_vertical=QVBoxLayout()
        #agregamos el espacio en el layout vertical
        layout_vertical.setContentsMargins(5,10,5,10)
        #agregamos un espacio en cada elemento del layout vertical
        layout_vertical.setSpacing(20)
        #agregamos elementos al layout vertical
        layout_vertical.addWidget(Color('red'))
        layout_vertical.addWidget(Color('green'))
        layout_vertical.addWidget(Color('blue'))
        #agregamos el layout vertical dentro del layout horizontal
        #Es decir se agrega de manera anidada
        layout_horizontal.addLayout(layout_vertical)
        #agregamos mas elementos al layout horizontal
        layout_horizontal.addWidget(Color('yellow'))
        layout_horizontal.addWidget(Color('cyan'))
        # componente_con_color_fondo=Color('blue')
        #layout vertical o horizontal se cambia h por v o alreves
        #layout=QHBoxLayout()
        #agregamos un nuevo componente de color
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('blue'))
        #publicamos un laylout
        #creamos un componente generico para poder publicar el layout
        componente= QWidget()
        componente.setLayout(layout_horizontal)
        #el componente se expande para cubrir el tamaño disponible
        self.setCentralWidget(componente)
#ejecutamos prueba
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()