from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit, QSpinBox


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        #QSpinBox
        numero = QSpinBox()
        #componente qlineedit
        linea_texto=QLineEdit()
        #establecemos el maximo de caracteres a capturar
        linea_texto.setMaxLength(15)
        #Establecemos un texto de ayuda o placeholder
        linea_texto.setPlaceholderText('Introduce tu nombre: ')
        #solo lectura 
        #linea_texto.setReadOnly(True)
        #validacion aplicando una mascara (mask)
        linea_texto.setInputMask('00-0000-0000')
        #Evento enter,cambio  seleccion de texto,cambio de texto
        linea_texto.returnPressed.connect(self.enter_presionado)
        linea_texto.selectionChanged.connect(self.cambio_seleccion)
        linea_texto.textChanged.connect(self.cambio_texto)
        self.setCentralWidget(numero)
    def enter_presionado(self):
        print('Se presiono el enter')
        self.centralWidget().setText('Juan Perez!')
    def cambio_seleccion(self):
        print('Cambio seleccion de texto')
        print(self.centralWidget().selectedText())
    def cambio_texto(self,nuevo_texto):
        print(f'Texto seleccionado:{nuevo_texto}')




if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()