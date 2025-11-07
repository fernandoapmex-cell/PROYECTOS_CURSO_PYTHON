from PySide6.QtWidgets import QMainWindow, QApplication, QListWidget


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        #componente qlistwidget se parece al combobox
        lista = QListWidget()
        lista.addItem('Uno')
        lista.addItems(['Dos','Tres'])
        #monitoreamos el cambio del elemento seleccionado, tanto el elemento con el texto
        lista.currentItemChanged.connect(self.cambio_elemento)
        lista.currentTextChanged.connect(self.cambio_texto)

        #desplegamos el componente
        self.setCentralWidget(lista)
    def cambio_elemento(self,nuevo_elemento):
        print(f'Nuevo elemento seleccionado:{nuevo_elemento}')
    def cambio_texto(self,texto):
        print(f'Texto seleccionado:{texto}')
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()