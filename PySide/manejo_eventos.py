#signals y slots
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signals y slots")
        #Boton
        boton=QPushButton('Click Aqui')
        #conectamos el evento (signal) click con el slot(evento_click)
        boton.clicked.connect(self.evento_click)
        #publicamos el boton
        self.setCentralWidget(boton)
    #slot
    def evento_click(self):
        print('Evento clicked')

if __name__ == '__main__':
    #creamos el objeto de aplicacion
    app = QApplication()
    #creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    #aca se ejecuta la app y se envuele en exit para que salga bien cuando termine
    sys.exit(app.exec())