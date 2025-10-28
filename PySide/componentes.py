from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        self.setFixedSize(500,600)
        #creamos un componente de tipo etiqueta o label
        etiqueta=QLabel('Hola')
        etiqueta.setPixmap(QPixmap('layla.jpg'))
        #asi ajustamos la imagen al tamaño nuevo de la ventana
        etiqueta.setScaledContents(True)
        # #modificamos el valor inicial
        # etiqueta.setText('Saludos')
        # #modificaciones sobre la fuente
        # fuente=etiqueta.font()
        # fuente.setPointSize(25)
        # etiqueta.setFont(fuente)
        # #modificar la alineacion de la etiqueta al centro usando una constante de qt
        # #etiqueta.setAlignment(Qt.AlignCenter)
        # #tambien se puede centrar de otra forma
        # etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter )
        # #publicamos este componente
        self.setCentralWidget(etiqueta)
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()