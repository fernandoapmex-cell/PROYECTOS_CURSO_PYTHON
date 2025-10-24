import sys

from PySide6.QtWidgets import QApplication, QWidget

#Clase Base de QT (PySide)
#se encarga de manejar y procesar los eventos (event loop)
app = QApplication()
# creamos un primer objeto ventana
ventana = QWidget()
#cambiamos el titulo de la ventana
ventana.setWindowTitle("Hola mundo con PySide")
#modificamos el tamaño de la ventan
ventana.resize(600,400)
#Mostrar la ventana
ventana.show()
#Se ejecuta la aplicacion
sys.exit(app.exec())