from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QMenu


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Contextual')
        self.show()
        #nos conectamos a la señal de customcontext menu requestd
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.montrar_menu_contexto)
    def montrar_menu_contexto(self, posicion):
        menu_contextual=QMenu(self)
        boton_nuevo=QAction(QIcon('nuevo.png'),'Nuevo',self)
        boton_guardar=QAction(QIcon('guardar.png'),'Guardar',self)
        boton_salir=QAction('Salir',self)
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.click_boton_guardar)
        boton_salir.triggered.connect(self.click_boton_salir)
        menu_contextual.addAction(boton_nuevo)
        menu_contextual.addAction(boton_guardar)
        menu_contextual.addAction(boton_salir)
        #recuperamos la posicion del cursor como posicion global de la ventana padre
        #y ejecutamos el menu contextual
        menu_contextual.exec(self.mapToGlobal(posicion))
    def click_boton_nuevo(self):
       print('Opcion Nuevo...')
    def click_boton_guardar(self):
       print('Opcion Guardar...')
    def click_boton_salir(self):
       print('Opcion Salir...')
# ejecutamos prueba
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()