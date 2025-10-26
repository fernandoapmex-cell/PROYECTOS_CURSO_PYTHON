#signals y slots
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signals y slots")
        self.setFixedSize(400, 200)
        #definimos la etiqueta y linea de edicion
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        #conectar la entrada de texto con la etiqueta
        #la señal es textchanged y el slot es settext
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        #Publicamos los componentes usando un layout
        layout = QVBoxLayout()
        #agregamos los componentes al layout
        layout.addWidget(self.entrada_texto)
        layout.addWidget(self.etiqueta)
        #creamos un contenedor para poder publicar el layout
        contenedor=QWidget()
        contenedor.setLayout(layout)
        #publicamos el contenedor,el cual ya usa los demas elementos
        self.setCentralWidget(contenedor)

if __name__ == '__main__':
    #creamos el objeto de aplicacion
    app = QApplication()
    #creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    #aca se ejecuta la app y se envuele en exit para que salga bien cuando termine
    sys.exit(app.exec())