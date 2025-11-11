from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPalette, QColor, QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, \
    QToolButton, QToolBar, QStatusBar, QCheckBox


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
        self.setWindowTitle('Barra estado  en Pyside')
        #publicamos una etiqueta
        etiqueta = QLabel('Hola')
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)
        #creamos la barra de herramientas
        barra = QToolBar('Mi barra de herramientas')
        barra.setIconSize(QSize(16,16))
        #configuracion para mostrar la barra de herramientas
        #barra.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        #barra.setToolButtonStyle(Qt.ToolButtonTextOnly)
        #.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        barra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(barra)
        #agregamos un elementoa nuestra barra de herramientas
        boton_nuevo=QAction(QIcon('nuevo.png'),'Nuevo',self)
        #agregamos el boton a la barra
        barra.addAction(boton_nuevo)
        #barra de estado
        self.setStatusBar(QStatusBar(self))
        #Mostramos un mensaje en el boton de accion
        boton_nuevo.setStatusTip('Nuevo archivo')
        #asociamos el evento click
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        #hacemos chequeable el boton
        #boton_nuevo.setCheckable(True)
        #agregamos la opcion de guardar
        boton_guardar=QAction(QIcon('guardar.png'),'Guardar',self)
        #agregamos el boton a la barra
        barra.addAction(boton_guardar)
        boton_guardar.setStatusTip('Guardar archivo')
        boton_guardar.triggered.connect(self.click_boton_guardar)
        barra.addSeparator()
        barra.addWidget(QCheckBox())
        barra.addWidget(QLabel('Salir'))
        menu=self.menuBar()
        menu_archivo=menu.addMenu('&Archivo')
        menu_archivo.addAction(boton_nuevo)
        #agregamos una segunda opcion
        menu_archivo.addAction(boton_guardar)
        #agregamos un separador
        menu_archivo.addSeparator()
        #agregamos una tercera opcion
        boton_acerca_de=QAction(QIcon('acerca.png'),'Acerca de ',self)
        #submenu ayuda
        menu_ayuda=menu.addMenu('&Ayuda')
        menu_ayuda.addAction(boton_acerca_de)
        boton_acerca_de.triggered.connect(self.click_boton_acerca_de)
        boton_salir=QAction('Salir',self)
        menu_archivo.addAction(boton_salir)

        #agregamos el submenu de ayuda
        menu_archivo.addMenu(menu_ayuda)
        #creamos atajos en nuestro menu
        #Ej.Combinacion de teclas
        #boton_nuevo.setShortcut(QKeySequence('Ctrl+N'))
        #esta forma hace shorcut igual que la de arriba
        boton_nuevo.setShortcut(Qt.CTRL|Qt.Key_N)
        #atajo para la opcion acerca de - Ctrl + 1
        boton_acerca_de.setShortcut(Qt.CTRL|Qt.Key_1)
        #atajo de guardar
        boton_guardar.setShortcut(Qt.CTRL|Qt.Key_G)


    def click_boton_acerca_de(self,estado):
        print('Acerca de:',estado)
    def click_boton_nuevo(self,estado):
        print('Nuevo archivo:',estado)
    def click_boton_guardar(self,estado):
        print('Guardar archivo:',estado)

# ejecutamos prueba
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()