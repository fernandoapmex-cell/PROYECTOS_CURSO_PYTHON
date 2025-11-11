from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, \
    QDialog, QDialogButtonBox, QLabel, QMessageBox


class VentanaDialogo(QDialog):
    def __init__(self,padre=None):
        super().__init__(padre)
        self.setWindowTitle('Ventana de dialogo')
        #Agregamos un boton de aceptar y otro de cancelar
        botones=QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.botones_dialogo = QDialogButtonBox(botones)
        self.botones_dialogo.accepted.connect(self.accept)
        self.botones_dialogo.rejected.connect(self.reject)
        #creamos un layout para publicar los botones
        self.layout=QVBoxLayout()
        mensaje=QLabel('Presiona alguno de los botones')
        self.layout.addWidget(mensaje)
        self.layout.addWidget(self.botones_dialogo)
        self.setLayout(self.layout)
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
        self.setWindowTitle('Dialogos')
        #agregamos un boton
        boton=QPushButton('Mostrar dialogo')
        boton.clicked.connect(self.click_boton)
        self.setCentralWidget(boton)
    def click_boton(self,estado):
        dialogo=QMessageBox.critical(self,'Problema Critico','Ventana con problema critico',buttons=QMessageBox.Discard | QMessageBox.NoToAll |QMessageBox.Ignore,defaultButton=QMessageBox.Discard)
        if dialogo == QMessageBox.Discard:
            print('Regreso el valor de Discard')
        elif dialogo == QMessageBox.NoToAll:
            print('Regreso el valor de Not to All')
        else:
            print('Regreso el valor de Ignore')

# ejecutamos prueba
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()