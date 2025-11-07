from PySide6.QtWidgets import QMainWindow, QApplication, QComboBox


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        #creamos un combo box o drop down list
        combobox=QComboBox()
        #agregar elementos al combo box
        combobox.addItem('Uno')
        combobox.addItems(['Dos','Tres'])
        #monitoreamos el cambio de elemento seleccionando ,tanto de indice como de texto
        combobox.currentIndexChanged.connect(self.cambio_indice)
        #monitoreamos cambio de texto
        combobox.currentTextChanged.connect(self.cambio_texto)
        #hacemos editable el combobox
        combobox.setEditable(True)
        #espeficamos la politica de insercion
        # combobox.setInsertPolicy(QComboBox.NoInsert)
        # #agregar al inicio de el combobox
        # combobox.setInsertPolicy(QComboBox.InsertAtTop)
        # #modifica el elementos actual
        # combobox.setInsertPolicy(QComboBox.InsertAtCurrent)
        # #insertar al final del bcombobox
        # combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        #limitar cuantos elementos agregamos al combobox
        combobox.setMaxCount(6)
        #insertar antes del elemento actual
        combobox.setInsertPolicy(QComboBox.InsertBeforeCurrent)
        #insertar despues del elemento actual
        combobox.setInsertPolicy(QComboBox.InsertAfterCurrent)
        #insertar alfabeticamente
        combobox.setInsertPolicy(QComboBox.InsertAlphabetically)
        #publicamos nuestro componente de combobox
        self.setCentralWidget(combobox)
    def cambio_indice(self,nuevo_indice):
        print(f'Nuevo Indice Seleccionado:{nuevo_indice}')
    def cambio_texto(self,texto):
        print(f'Texto seleccionado:{texto}')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()