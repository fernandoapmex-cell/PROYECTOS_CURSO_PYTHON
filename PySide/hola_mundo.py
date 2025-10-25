import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

#Clase Base de QT (PySide)
#se encarga de manejar y procesar los eventos (event loop)
app = QApplication()
# creamos un primer objeto ventana
#cualquier objeto puyede ser una ventana en pyside
#ventana = QPushButton('Boton de PySide')
ventana = QMainWindow()
#cambiamos el titulo de la ventana
ventana.setWindowTitle("Hola mundo con PySide")
#modificamos el tamaño de la ventan
ventana.resize(600,400)
#Mostrar la ventana
ventana.show()
#Se ejecuta la aplicacion
sys.exit(app.exec())