from PySide6.QtWidgets import QMainWindow, QApplication, QSpinBox, QDoubleSpinBox


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        #qspinbox es para valores enteros
        #numero = QSpinBox()
        #qdoublespinbox es para flotantes
        numero=QDoubleSpinBox()
        #establecer valor minimo y maximo
        # numero.setMinimum(-5)
        # numero.setMaximum(3)
        #tambien se puede delimitar asi
        #numero.setRange(-5,3)
        #establecemos un prefijo y un sufijo
        numero.setPrefix('$')
        numero.setSuffix('c')
        self.setCentralWidget(numero)
        #establecemos el salto o step
        numero.setSingleStep(3.5)
        #nos conectamos al evento o señal de cambio de valor
        #envia el valor nuevo pero solo el valor numerico
        numero.valueChanged.connect(self.cambio_valor)
        #envia el valor en texto incluyendo prefijo y sufijo
        numero.textChanged.connect(self.cambio_texto)
    def cambio_valor(self,nuevo_valor):
        print(f'Valor: {nuevo_valor}')
    def cambio_texto(self,nuevo_texto):
        print(f'Nuevo Texto: {nuevo_texto}')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()