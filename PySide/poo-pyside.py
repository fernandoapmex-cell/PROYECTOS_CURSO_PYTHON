import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton


class VentanaPySide(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("POO con PySide")
        self.resize(600,400)
        #con este se desabilita el hacer grande la ventana
        self.setFixedSize(QSize(600,400))
        #creamos algunos componente
        self._agregar_componentes()

    def _agregar_componentes(self):
        #agregar un menu
        menu=self.menuBar()
        menu_archivo=menu.addMenu("Archivo")
        #agregamos opciones al menu
        accion_nuevo=QAction('Nuevo',self)
        menu_archivo.addAction(accion_nuevo)
        #agregamos un texto a la barra de estado
        accion_nuevo.setStatusTip('Nuevo Archivo')
        #agregamos un mensaje en la barra de estado
        self.statusBar().showMessage('Informacion de la barra de estado')
        #agegamos un boton
        boton=QPushButton('Nuevo boton')
        #publicamos el boton
        self.setCentralWidget(boton)



if __name__ == '__main__':
    app = QApplication([])
    #creamos un objeto de tipo ventana
    ventana1 = VentanaPySide()
    ventana1.show()
    #ejecutamos la ventana
    sys.exit(app.exec_())