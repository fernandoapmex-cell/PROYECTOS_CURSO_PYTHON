#signals y slots
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signals y slots")
        #Boton
        self.boton=QPushButton('Click Aqui')
        #asociamos la señal del click al slot evento_click
        # #se puede hacer que el boton se quede chequeado con set cehakeable
        # boton.setCheckable(True)
        # #conectamos otro slot al evento checkable
        # boton.clicked.connect(self.evento_checar)
        # #conectamos el evento (signal) click con el slot(evento_click)
        self.boton.clicked.connect(self.evento_click)
        #conectar a la señal de cambio de titulo
        self.windowTitleChanged.connect(self.cambio_titulo_aplicacion)
        # #publicamos el boton
        self.setCentralWidget(self.boton)
    def evento_click(self):
        #cambiar el texto del boton y el titulo de la ventana
        self.boton.setText('Nuevo texto boton')
        self.boton.setEnabled(False)
        self.setWindowTitle('Nuevo titulo de la Aplicacion')
    def cambio_titulo_aplicacion(self,nuevo_titulo):
        print('Nuevo titulo de la aplicacion :',{nuevo_titulo})


    #slot
    # def evento_click(self):
    #     print('Evento clicked')
    #     #accedemos al estado del boton con el atributo
    #     print('Boton checado desde evento click',self.boton_checado)
    # def evento_checar(self,checar):
    #     self.boton_checado=checar
    #     print('Checado?',self.boton_checado)

if __name__ == '__main__':
    #creamos el objeto de aplicacion
    app = QApplication()
    #creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    #aca se ejecuta la app y se envuele en exit para que salga bien cuando termine
    sys.exit(app.exec())